#!/usr/bin/env python3
"""
Convert-Database.py  —  CheatArchiver

Reads every CMP-format file from the Database/ folder tree and writes a
cheats.yaml (and matching README.md) into the consoles/ directory tree that
is used by Generate-ReadmeFiles.ps1.

Usage
-----
    python Convert-Database.py                # dry-run (print what would change)
    python Convert-Database.py --write        # write files, skip existing cheats.yaml
    python Convert-Database.py --write --overwrite  # overwrite everything

Notes
-----
* The MODS (^6) section is preserved as a raw comment block appended to the
  last cheat's notes so no information is lost.
* When the same (console, region, game) appears in multiple DB folders the
  cheats are merged; identical cheat names (case-insensitive) are kept only
  once (first occurrence wins).
"""

import argparse
import os
import re
import sys
from collections import defaultdict, OrderedDict
from pathlib import Path

# ---------------------------------------------------------------------------
# Folder → (console_name, cheat_type, forced_region)
# ---------------------------------------------------------------------------

FOLDER_META = {
    "MEMORY-PS2-CMP":               ("PlayStation 2",    "CodeBreaker",  None),
    "MEMORY-PS2-CODEBREAKER":       ("PlayStation 2",    "CodeBreaker",  None),
    "MEMORY-PS2-GSHI-DB":           ("PlayStation 2",    "CodeBreaker",  None),
    "MEMORY-PS2-XPLODER-DB-[EU]":   ("PlayStation 2",    "Xploder",      "PAL"),
    "MEMORY-GBA":                   ("Game Boy Advance", "CodeBreaker",  None),
    "MEMORY-GEN":                   ("Sega Genesis",     "Game Genie",   None),
    "MEMORY-NDS":                   ("Nintendo DS",      "Action Replay", None),
    "MEMORY-PS1":                   ("PlayStation 1",    "GameShark",    None),
    "MEMORY-WII":                   ("Nintendo Wii",     "Gecko",        None),
    "PS3-WIP":                      ("PlayStation 3",    "AP",           None),
    "PS4-WIP":                      ("PlayStation 4",    "AP",           None),
    "SAVES-PS2":                    ("PlayStation 2",    "Save Editor",  None),
    "SAVES-PS3":                    ("PlayStation 3",    "Save Editor",  None),
    "SAVES-PS4-SAVEWIZARD-CLEAN":   ("PlayStation 4",    "SaveWizard",   None),
    "SAVES-PSP":                    ("PSP",              "Save Editor",  None),
    "SAVES-PSV":                    ("PlayStation Vita", "Save Editor",  None),
}

# Priority used when merging cheats from multiple DB folders.
# Lower number = higher priority (first source wins for duplicate cheat names).
FOLDER_PRIORITY = {
    "MEMORY-PS2-GSHI-DB":           1,
    "MEMORY-PS2-CMP":               2,
    "MEMORY-PS2-CODEBREAKER":       3,
    "MEMORY-PS2-XPLODER-DB-[EU]":   4,
    "MEMORY-GBA":                   1,
    "MEMORY-GEN":                   1,
    "MEMORY-NDS":                   1,
    "MEMORY-PS1":                   1,
    "MEMORY-WII":                   1,
    "PS3-WIP":                      1,
    "PS4-WIP":                      1,
    "SAVES-PS2":                    5,
    "SAVES-PS3":                    5,
    "SAVES-PS4-SAVEWIZARD-CLEAN":   5,
    "SAVES-PSP":                    5,
    "SAVES-PSV":                    5,
}

# ---------------------------------------------------------------------------
# Region detection
# ---------------------------------------------------------------------------

# Prefix → region for serial numbers
_SERIAL_REGION = [
    # PS2 / PS1
    (("SLUS", "SCUS"), "NTSC-U"),
    (("SLES", "SCES"), "PAL"),
    (("SLPM", "SCPS", "SCAJ", "SLPJ", "SLAJ", "SLPS"), "NTSC-J"),
    # PS3
    (("BLUS", "NPUA", "BCUS"), "NTSC-U"),
    (("BLES", "NPEB", "BCES"), "PAL"),
    (("BLAS", "NPJB", "BCAS", "BLJM"), "NTSC-J"),
    # PS4
    (("CUSA",), "NTSC-U"),
    # PSN digital
    (("NPUB", "NPUG"), "NTSC-U"),
    (("NPEB", "NPEG"), "PAL"),
    (("NPJB", "NPJG"), "NTSC-J"),
    # PSP
    (("ULUS", "UCUS"), "NTSC-U"),
    (("ULES", "UCES"), "PAL"),
    (("ULJM", "UCJS"), "NTSC-J"),
    # PS Vita
    (("PCSE", "PCSA", "VCAS"), "NTSC-U"),
    (("PCSB", "VCES"), "PAL"),
    (("PCSG", "VCJS"), "NTSC-J"),
]


def detect_region(serial: str, console: str, forced_region: str | None) -> str:
    if forced_region:
        return forced_region

    if not serial:
        return "Unknown"

    s = serial.upper().replace("-", "").replace("_", "").replace(".", "")

    for prefixes, region in _SERIAL_REGION:
        for pfx in prefixes:
            if s.startswith(pfx):
                return region

    # GBA: AGB-XXXX-USA etc.
    if "USA" in s:
        return "NTSC-U"
    if "EUR" in s or "EUU" in s:
        return "PAL"
    if "JPN" in s or "JAP" in s:
        return "NTSC-J"

    # NDS 4-char code (last char = region)
    bare = re.sub(r"[^A-Z0-9]", "", s)
    if len(bare) == 4:
        last = bare[-1]
        if last == "E":
            return "NTSC-U"
        if last == "P":
            return "PAL"
        if last == "J":
            return "NTSC-J"

    # Wii 6-char code (4th char = region)
    if len(bare) == 6 and "Wii" in console:
        rc = bare[3]
        if rc == "E":
            return "NTSC-U"
        if rc == "P":
            return "PAL"
        if rc == "J":
            return "NTSC-J"

    return "Unknown"


# ---------------------------------------------------------------------------
# Folder-name sanitisation
# ---------------------------------------------------------------------------

_ILLEGAL_CHARS = r'[<>:"/\\|?*\x00-\x1f]'


def sanitize_name(name: str) -> str:
    """Return a filesystem-safe folder/file name."""
    name = re.sub(_ILLEGAL_CHARS, lambda m: "_" if m.group() == ":" else "", name)
    name = name.strip(". ")
    return name or "Unknown"


# ---------------------------------------------------------------------------
# CMP file parser
# ---------------------------------------------------------------------------

def parse_cmp(filepath: Path) -> dict:
    """
    Parse one CMP-format cheat file.

    Returns a dict:
        {
            'hash':    str,
            'game_id': str,
            'name':    str,
            'ap_cred': str,
            'cheats':  list[dict]   # see below
        }

    Each cheat dict:
        {
            'name':     str,
            'author':   str,
            'notes':    str,
            'codes':    list[str],
            'category': str,   # from !Category: header (informational)
            'file':     str,   # from ^4 = FILE: (for save-editor cheats)
        }
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}

    lines = text.splitlines()

    result = {
        "hash": "",
        "game_id": "",
        "name": "",
        "ap_cred": "",
        "cheats": [],
    }

    current_category = ""
    current_file = ""
    current_cheat: dict | None = None
    in_mods = False
    mods_lines: list[str] = []

    def flush_cheat():
        nonlocal current_cheat
        if current_cheat is not None:
            result["cheats"].append(current_cheat)
            current_cheat = None

    for raw in lines:
        line = raw.rstrip("\r\n")
        stripped = line.strip()

        if not stripped:
            continue

        # ---- MODS section (^6) ----
        if re.match(r"^\^6\s*=\s*MODS", stripped, re.IGNORECASE):
            in_mods = True
            flush_cheat()
            continue
        if in_mods:
            # A new ^ line that is NOT ^6 closes the mods section
            if stripped.startswith("^") and not re.match(r"^\^6", stripped):
                # Attach collected mods as a note on the last cheat (or a
                # synthetic cheat) so the raw data is preserved.
                if mods_lines:
                    mods_text = "MODS: " + " | ".join(mods_lines[:40])
                    synthetic = {
                        "name": "__MODS__",
                        "author": "",
                        "notes": mods_text,
                        "codes": [],
                        "category": "__meta__",
                        "file": current_file,
                    }
                    result["cheats"].append(synthetic)
                    mods_lines = []
                in_mods = False
                # Fall through to process this ^ line below
            else:
                mods_lines.append(stripped)
                continue

        # ---- Metadata (^N = KEY: value) ----
        m = re.match(r"^\^(\d+)\s*=\s*([^:]+):\s*(.*)", stripped)
        if m:
            key = m.group(2).strip().upper()
            val = m.group(3).strip()
            if key == "HASH":
                result["hash"] = val
            elif key == "GAMEID":
                result["game_id"] = val.replace("_", "-").replace(".", "")
            elif key == "NAME":
                result["name"] = val
            elif key == "FILE":
                flush_cheat()
                current_file = val
            elif key == "APCRED":
                result["ap_cred"] = val
            continue

        # ---- End of category ----
        if stripped == "!!":
            flush_cheat()
            current_category = ""
            continue

        # ---- Category header  !Category Name: ----
        if stripped.startswith("!") and not stripped.startswith("!!"):
            flush_cheat()
            current_category = stripped[1:].rstrip(":").strip()
            continue

        # ---- Cheat name  +Name ----
        if stripped.startswith("+"):
            flush_cheat()
            cheat_name = stripped[1:].strip()
            # Strip inline notes like {<I>You Must…</I>}
            cheat_name = re.sub(r"\{[^}]*\}", "", cheat_name).strip()
            current_cheat = {
                "name": cheat_name or "Unnamed",
                "author": "",
                "notes": "",
                "codes": [],
                "category": current_category,
                "file": current_file,
            }
            continue

        # ---- Author/credit  %Credits: Name ----
        if stripped.startswith("%"):
            if current_cheat is not None:
                credit = stripped[1:].strip()
                credit = re.sub(r"^Credits?\s*:\s*", "", credit, flags=re.IGNORECASE)
                current_cheat["author"] = credit
            continue

        # ---- Code line  $XXXXXXXX YYYYYYYY ----
        if stripped.startswith("$"):
            if current_cheat is not None:
                code = stripped[1:].strip()
                if code:
                    current_cheat["codes"].append(code)
            continue

        # ---- Anything else in cheat context = notes ----
        if current_cheat is not None:
            note = re.sub(r"\{[^}]*\}", "", stripped).strip()
            if note:
                if current_cheat["notes"]:
                    current_cheat["notes"] += " " + note
                else:
                    current_cheat["notes"] = note

    flush_cheat()

    # Attach any trailing MODS
    if mods_lines:
        mods_text = "MODS: " + " | ".join(mods_lines[:40])
        result["cheats"].append(
            {
                "name": "__MODS__",
                "author": "",
                "notes": mods_text,
                "codes": [],
                "category": "__meta__",
                "file": current_file,
            }
        )

    return result


# ---------------------------------------------------------------------------
# YAML writer (hand-rolled to match existing repo style)
# ---------------------------------------------------------------------------

def _yaml_str(s: str) -> str:
    """Wrap a string in double quotes, escaping inner quotes and backslashes."""
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def build_yaml(
    game: str,
    console: str,
    region: str,
    serial: str,
    cheat_type: str,
    source: str,
    cheats: list[dict],
) -> str:
    lines: list[str] = []

    # Header comment
    lines.append(f"# {game} cheat data")
    lines.append(f"# Console: {console}")
    lines.append(f"# Region:  {region}")
    if serial:
        lines.append(f"# Serial:  {serial}")
    lines.append("")

    # Top-level fields
    lines.append(f"game: {_yaml_str(game)}")
    lines.append(f"console: {_yaml_str(console)}")
    lines.append(f"region: {_yaml_str(region)}")
    lines.append(f"serial: {_yaml_str(serial)}")
    lines.append(f"cheat_type: {_yaml_str(cheat_type)}")
    lines.append(f"source: {_yaml_str(source)}")
    lines.append("")
    lines.append("cheats:")

    for cheat in cheats:
        # Skip internal __MODS__ entries — preserved as notes on last real cheat
        if cheat["name"] == "__MODS__":
            continue

        name = cheat["name"]
        author = cheat.get("author", "")
        notes_parts: list[str] = []

        # Prepend category to notes if present and not __meta__
        cat = cheat.get("category", "")
        if cat and cat != "__meta__":
            notes_parts.append(f"[{cat}]")

        # Prepend file if present (for save-editor cheats)
        cf = cheat.get("file", "")
        if cf:
            notes_parts.append(f"File: {cf}")

        raw_notes = cheat.get("notes", "")
        if raw_notes:
            notes_parts.append(raw_notes)

        notes = "  ".join(notes_parts)
        codes = cheat.get("codes", [])

        lines.append(f"  - name: {_yaml_str(name)}")
        if author:
            lines.append(f"    author: {_yaml_str(author)}")
        if notes:
            # Cap notes at 300 chars to avoid absurdly long single-line strings
            if len(notes) > 300:
                notes = notes[:297] + "..."
            lines.append(f"    notes: {_yaml_str(notes)}")
        if codes:
            lines.append("    codes:")
            for code in codes:
                lines.append(f"      - {_yaml_str(code)}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_game_name(name: str, console: str) -> str:
    """
    Strip region suffixes like "(Ntsc-U)" or "(PAL-M5)" that some DB sources
    embed in the NAME field, then return a sanitised name.
    """
    name = re.sub(r"\s*\((Ntsc-[UJ]|PAL[^)]*|Pal[^)]*|NTSC[^)]*)\)\s*$", "", name, flags=re.IGNORECASE)
    name = name.strip()
    return sanitize_name(name)


def first_serial(game_id: str) -> str:
    """Return the first serial from a comma-separated list."""
    return game_id.split(",")[0].strip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Database/ CMP files to consoles/ YAML.")
    parser.add_argument("--write", action="store_true", help="Actually write files (default: dry-run).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing cheats.yaml files.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).parent),
        help="Repository root (default: same directory as this script).",
    )
    args = parser.parse_args()

    root = Path(args.root)
    db_root = root / "Database"
    consoles_root = root / "consoles"

    if not db_root.is_dir():
        print(f"ERROR: Database/ not found at {db_root}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Step 1: Collect all cheats keyed by (console, region, game_name)
    # Each entry is:
    #   {
    #       'serial':     str (first one found),
    #       'cheat_type': str (first one found),
    #       'source':     str,
    #       'cheats':     list[dict]   (de-duplicated by name)
    #   }
    # -----------------------------------------------------------------------

    # game_key → {serial, cheat_type, source, cheats, seen_names}
    GameData = dict  # just for documentation
    collected: dict[tuple, GameData] = defaultdict(
        lambda: {"serial": "", "cheat_type": "", "source": "", "cheats": [], "seen_names": set()}
    )

    # Process subfolders in priority order (highest priority last so it can
    # override metadata but NOT cheats already seen by a higher-priority source)
    db_folders = sorted(
        (d for d in db_root.iterdir() if d.is_dir() and d.name in FOLDER_META),
        key=lambda d: FOLDER_PRIORITY.get(d.name, 99),
    )

    total_files = 0
    skipped_parse = 0

    for folder in db_folders:
        folder_name = folder.name
        console, cheat_type, forced_region = FOLDER_META[folder_name]

        for filepath in sorted(folder.iterdir()):
            if not filepath.is_file():
                continue
            total_files += 1

            parsed = parse_cmp(filepath)
            if not parsed or not parsed.get("name"):
                skipped_parse += 1
                continue

            raw_name = parsed["name"]
            game_id = parsed.get("game_id", "")
            serial = first_serial(game_id)
            region = detect_region(serial, console, forced_region)
            game_name = clean_game_name(raw_name, console)

            if not game_name:
                skipped_parse += 1
                continue

            key = (console, region, game_name)
            entry = collected[key]

            # Set metadata only if not yet assigned (higher-priority folder wins)
            if not entry["serial"] and serial:
                entry["serial"] = serial
            if not entry["cheat_type"] and cheat_type:
                entry["cheat_type"] = cheat_type
            if not entry["source"]:
                entry["source"] = parsed.get("ap_cred", "")

            # Merge cheats (first occurrence of a name wins)
            for cheat in parsed.get("cheats", []):
                cname_key = cheat["name"].lower().strip()
                if cname_key not in entry["seen_names"]:
                    entry["seen_names"].add(cname_key)
                    entry["cheats"].append(cheat)

    print(f"Scanned {total_files} files, skipped {skipped_parse} (no name or parse error).")
    print(f"Unique games to write: {len(collected)}")

    if not args.write:
        print("\nDry-run mode — pass --write to create files.")
        # Show a sample of what would be written
        for i, (key, entry) in enumerate(sorted(collected.items())):
            if i >= 20:
                print("  ... (truncated)")
                break
            console, region, game_name = key
            path = consoles_root / console / region / game_name / "cheats.yaml"
            print(f"  {path.relative_to(root)}  ({len(entry['cheats'])} cheats)")
        return

    # -----------------------------------------------------------------------
    # Step 2: Write YAML files
    # -----------------------------------------------------------------------

    written = 0
    skipped_exist = 0
    errors = 0

    for (console, region, game_name), entry in sorted(collected.items()):
        game_dir = consoles_root / console / region / game_name
        yaml_path = game_dir / "cheats.yaml"

        if yaml_path.exists() and not args.overwrite:
            skipped_exist += 1
            continue

        cheats = [c for c in entry["cheats"] if c["name"] != "__MODS__"]
        if not cheats:
            continue

        yaml_content = build_yaml(
            game=game_name,
            console=console,
            region=region,
            serial=entry["serial"],
            cheat_type=entry["cheat_type"],
            source=entry["source"],
            cheats=cheats,
        )

        try:
            game_dir.mkdir(parents=True, exist_ok=True)
            yaml_path.write_text(yaml_content, encoding="utf-8")
            written += 1
        except Exception as exc:
            print(f"ERROR writing {yaml_path}: {exc}", file=sys.stderr)
            errors += 1

    print(f"\nWritten:          {written}")
    print(f"Skipped (exist):  {skipped_exist}")
    print(f"Errors:           {errors}")


if __name__ == "__main__":
    main()
