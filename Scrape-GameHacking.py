#!/usr/bin/env python3
"""
Scrape-GameHacking.py
=====================
Scrapes https://gamehacking.org/search for every game and its cheat codes,
then writes the CheatArchiver folder structure:

  consoles/<Console>/<Region>/<Game Title>/cheats.yaml

Usage
-----
    python Scrape-GameHacking.py [--out-dir /path/to/CheatArchiver]
                                  [--system <system_id_or_name>]
                                  [--delay 1.0]
                                  [--dry-run]

Options
-------
--out-dir     Root of the CheatArchiver repo.  Defaults to the directory
              that contains this script.
--system      Filter to a single system by numeric ID or partial name.
--delay       Seconds to wait between HTTP requests (default 1.0).
--dry-run     Print what would be written without creating any files.

Cheat-type detection
--------------------
gamehacking.org labels codes by device.  The script maps known device
strings to canonical cheat-type labels:

  Action Replay / AR Max / AR V2 -> "Action Replay"
  CodeBreaker / CB               -> "CodeBreaker"
  GameShark / Game Shark / GS    -> "GameShark"
  Game Genie                     -> "Game Genie"
  Pro Action Replay / PAR        -> "Pro Action Replay"
  (unrecognised)                 -> "RAW"
"""

import argparse
import os
import random
import re
import sys
import time
import urllib3
from pathlib import Path
from urllib.parse import urljoin, urlencode, quote

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit(
        "Required packages not found.\n"
        "Install them with:  pip install requests beautifulsoup4"
    )

BASE_URL = "https://gamehacking.org"

# ---------------------------------------------------------------------------
# Cheat-type detection
# ---------------------------------------------------------------------------

CHEAT_TYPE_MAP = [
    (re.compile(r"action\s*replay", re.I),    "Action Replay"),
    (re.compile(r"\bAR\b"),                   "Action Replay"),
    (re.compile(r"codebreaker",    re.I),     "CodeBreaker"),
    (re.compile(r"\bCB\b"),                   "CodeBreaker"),
    (re.compile(r"gameshark",      re.I),     "GameShark"),
    (re.compile(r"game\s*shark",   re.I),     "GameShark"),
    (re.compile(r"\bGS\b"),                   "GameShark"),
    (re.compile(r"game\s*genie",   re.I),     "Game Genie"),
    (re.compile(r"pro\s*action\s*replay", re.I), "Pro Action Replay"),
    (re.compile(r"\bPAR\b"),                  "Pro Action Replay"),
    (re.compile(r"xploder",        re.I),     "Xploder"),
    (re.compile(r"swap\s*magic",   re.I),     "Swap Magic"),
]


def detect_cheat_type(device_string: str) -> str:
    """Return a canonical cheat-type label, or 'RAW' if unrecognised."""
    if not device_string:
        return "RAW"
    for pattern, label in CHEAT_TYPE_MAP:
        if pattern.search(device_string):
            return label
    return "RAW"


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------

def _yaml_str(value: str) -> str:
    """Return a YAML double-quoted string, escaping backslashes and quotes."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_cheats_yaml(
    game: str,
    console: str,
    region: str,
    serial: str,
    cheat_type: str,
    source_url: str,
    cheats: list,
) -> str:
    """Render a cheats.yaml string from structured data."""
    lines = [
        f"# {game} cheat data",
        f"# Console: {console}",
        f"# Region:  {region}",
    ]
    if serial:
        lines.append(f"# Serial:  {serial}")
    lines += [
        f"# Source:  {source_url}",
        "",
        f"game: {_yaml_str(game)}",
        f"console: {_yaml_str(console)}",
        f"region: {_yaml_str(region)}",
    ]
    if serial:
        lines.append(f"serial: {_yaml_str(serial)}")
    lines += [
        f"cheat_type: {_yaml_str(cheat_type)}",
        f"source: {_yaml_str(source_url)}",
        "",
        "cheats:",
    ]

    for cheat in cheats:
        name   = cheat.get("name", "Unknown")
        author = cheat.get("author", "")
        notes  = cheat.get("notes", "")
        codes  = cheat.get("codes", [])

        lines.append(f"  - name: {_yaml_str(name)}")
        if author:
            lines.append(f"    author: {_yaml_str(author)}")
        if notes:
            lines.append(f"    notes: {_yaml_str(notes)}")
        if codes:
            lines.append("    codes:")
            for code in codes:
                lines.append(f'      - {_yaml_str(code)}')

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File-system helpers
# ---------------------------------------------------------------------------

INVALID_PATH_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_name(text: str) -> str:
    """Strip characters that are illegal in directory/file names."""
    return INVALID_PATH_CHARS.sub("", text).strip(" .")


def ensure_yaml(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        print(f"[DRY-RUN] Would write: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return
    path.write_text(content, encoding="utf-8")
    print(f"  Written: {path}")


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def random_delay(base_delay: float) -> None:
    """Sleep for base_delay with +/- 30% random jitter to avoid detection patterns."""
    jitter = random.uniform(-0.3, 0.3)
    actual_delay = base_delay * (1 + jitter)
    time.sleep(max(0.1, actual_delay))  # Minimum 0.1 second delay


def get_soup(
    session: requests.Session,
    url: str,
    delay: float,
    retries: int = 3,
    referer: str | None = None,
) -> BeautifulSoup:
    """Fetch *url* and return a BeautifulSoup object (HTML parser).

    Retries up to *retries* times on transient network or server errors,
    with exponential back-off.  Raises the last exception if all attempts fail.
    """
    verbose = getattr(session, 'verbose', False)
    
    if verbose:
        print(f"  [DEBUG] Fetching {url}")
        if referer:
            print(f"  [DEBUG] Referer: {referer}")
    
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            # Add referer header for this specific request if provided
            headers = {}
            if referer:
                headers["Referer"] = referer
            resp = session.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
            
            if verbose:
                print(f"  [DEBUG] Response status: {resp.status_code}")
                print(f"  [DEBUG] Response headers: {dict(resp.headers)}")
                print(f"  [DEBUG] Content length: {len(resp.text)} bytes")
            
            random_delay(delay)  # Use random delay instead of fixed delay
            return BeautifulSoup(resp.text, "html.parser")
        except requests.exceptions.SSLError as exc:
            raise requests.exceptions.SSLError(
                f"SSL certificate verification failed for {url}.\n"
                "Try running with --no-verify-ssl to skip verification."
            ) from exc
        except requests.exceptions.ConnectionError as exc:
            last_exc = exc
            print(
                f"  [WARN] Connection error on attempt {attempt}/{retries} for {url}: {exc}",
                flush=True,
            )
        except requests.exceptions.Timeout as exc:
            last_exc = exc
            print(
                f"  [WARN] Timeout on attempt {attempt}/{retries} for {url}: {exc}",
                flush=True,
            )
        except requests.exceptions.HTTPError as exc:
            # Non-transient HTTP errors (4xx) are not worth retrying.
            status = exc.response.status_code if exc.response is not None else "?"
            if exc.response is not None and exc.response.status_code < 500:
                error_msg = f"HTTP {status} error fetching {url}."
                if status == 403:
                    error_msg += (
                        "\n  The site is actively blocking this request. This could be due to:"
                        "\n  - Anti-bot protection (e.g., Cloudflare, Imperva)"
                        "\n  - Rate limiting (try increasing --delay)"
                        "\n  - IP blocking (try using a VPN or proxy)"
                        "\n  - User-Agent detection (headers may need updating)"
                    )
                else:
                    error_msg += " The site may be blocking requests or the URL has changed."
                raise requests.exceptions.HTTPError(error_msg) from exc
            last_exc = exc
            print(
                f"  [WARN] HTTP {status} on attempt {attempt}/{retries} for {url}: {exc}",
                flush=True,
            )
        if attempt < retries:
            backoff = delay * (2 ** attempt)
            print(f"  [WARN] Retrying in {backoff:.1f}s …", flush=True)
            random_delay(backoff)  # Use random delay for retries too
    raise requests.exceptions.RequestException(
        f"Failed to fetch {url} after {retries} attempt(s)."
    ) from last_exc


# ---------------------------------------------------------------------------
# gamehacking.org scraping logic
# ---------------------------------------------------------------------------

def scrape_systems(session: requests.Session, delay: float, retries: int = 3) -> list:
    """Return a list of {id, name} dicts for all systems on the search page."""
    # Use BASE_URL as referer to simulate navigation from homepage
    soup = get_soup(session, f"{BASE_URL}/search", delay, retries=retries, referer=BASE_URL)
    systems = []
    # The system select box is typically id="system" or name="system"
    select = (
        soup.find("select", {"name": re.compile(r"system", re.I)}) or
        soup.find("select", {"id":   re.compile(r"system", re.I)})
    )
    if not select:
        # Fallback: look for any <select> that has many <option> children
        for sel in soup.find_all("select"):
            opts = sel.find_all("option")
            if len(opts) > 5:
                select = sel
                break
    if not select:
        print("[WARN] Could not find system selector on search page.")
        return systems
    for opt in select.find_all("option"):
        val  = opt.get("value", "").strip()
        name = opt.get_text(strip=True)
        if val and val != "0":
            systems.append({"id": val, "name": name})
    return systems


def scrape_game_list(
    session: requests.Session,
    system_id: str,
    delay: float,
    retries: int = 3,
) -> list:
    """Return a list of {id, title, url} dicts for every game in *system_id*."""
    url  = f"{BASE_URL}/search"
    games = []
    page  = 1

    while True:
        params = {"system": system_id, "page": page}
        page_url = f"{url}?{urlencode(params)}"
        # Use BASE_URL as referer for search pages
        referer = BASE_URL if page == 1 else f"{url}?{urlencode({'system': system_id, 'page': page - 1})}"
        soup = get_soup(session, page_url, delay, retries=retries, referer=referer)

        # Game links are typically <a href="/game/NNN">Game Title</a>
        found_any = False
        for a in soup.find_all("a", href=re.compile(r"^/game/\d+")):
            m = re.search(r"/game/(\d+)", a["href"])
            if not m:
                continue
            game_id = m.group(1)
            title   = a.get_text(strip=True)
            games.append({"id": game_id, "title": title, "url": urljoin(BASE_URL, a["href"])})
            found_any = True

        # Stop if no games found or if there's no "next page" link
        next_link = soup.find("a", string=re.compile(r"next", re.I))
        if not found_any or not next_link:
            break
        page += 1

    return games


def scrape_game(
    session: requests.Session,
    game_url: str,
    delay: float,
    retries: int = 3,
) -> dict:
    """
    Fetch a game page and return:
      {
        title, console, region, serial, cheat_type, source_url,
        cheats: [{name, author, notes, codes}]
      }
    """
    # Use search page as referer when fetching game pages
    soup = get_soup(session, game_url, delay, retries=retries, referer=f"{BASE_URL}/search")

    # --- Title ---
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Unknown Game"

    # --- Metadata table (console, region, serial) ---
    console = ""
    region  = ""
    serial  = ""

    for row in soup.find_all("tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) >= 2:
            label = cells[0].get_text(strip=True).lower()
            value = cells[1].get_text(strip=True)
            if "system" in label or "console" in label:
                console = value
            elif "region" in label:
                region = value
            elif "serial" in label or "id" in label:
                serial = value

    # --- Cheat codes ---
    # gamehacking.org groups codes by device/type in sections or tables.
    # We detect the device name from headings and map it to a cheat type.
    cheats      = []
    cheat_types_found = set()

    # Strategy: look for <h2>/<h3> headings that name a device, then collect
    # the code rows that follow until the next heading.
    current_device = ""
    for tag in soup.find_all(["h2", "h3", "tr"]):
        if tag.name in ("h2", "h3"):
            text = tag.get_text(strip=True)
            # Headings like "CodeBreaker Codes", "Action Replay Codes"
            m = re.match(r"(.+?)\s*(codes?|cheats?)?$", text, re.I)
            if m:
                current_device = m.group(1).strip()
        elif tag.name == "tr":
            cells = tag.find_all("td")
            if len(cells) >= 2:
                # Typical layout: | Code | Description | [Author] |
                code_text  = cells[0].get_text(separator=" ", strip=True)
                desc_text  = cells[1].get_text(strip=True)
                author_text = cells[2].get_text(strip=True) if len(cells) > 2 else ""

                # Validate that the first cell looks like a cheat code.
                # Require at least one hex digit sequence to avoid matching
                # strings composed entirely of separators.
                if (
                    re.match(r"^[0-9A-Fa-f\s\-:]+$", code_text)
                    and re.search(r"[0-9A-Fa-f]{2,}", code_text)
                    and len(code_text) >= 4
                ):
                    code_lines = [
                        line.strip()
                        for line in code_text.splitlines()
                        if line.strip()
                    ]
                    if code_lines:
                        cheat_types_found.add(current_device)
                        cheats.append({
                            "name":   desc_text or "Unknown",
                            "author": author_text,
                            "notes":  "",
                            "codes":  code_lines,
                        })

    # Determine canonical cheat type.
    # Priority order: prefer any recognised type over RAW.  When multiple
    # recognised types are present, the first match in CHEAT_TYPE_MAP order
    # wins (i.e. Action Replay > CodeBreaker > GameShark > …).
    if cheat_types_found:
        canonical = "RAW"
        for _, label in CHEAT_TYPE_MAP:
            for device in cheat_types_found:
                if detect_cheat_type(device) == label:
                    canonical = label
                    break
            if canonical != "RAW":
                break
        cheat_type = canonical
    else:
        cheat_type = "RAW"

    return {
        "title":      title,
        "console":    console,
        "region":     region,
        "serial":     serial,
        "cheat_type": cheat_type,
        "source_url": game_url,
        "cheats":     cheats,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scrape gamehacking.org and populate the CheatArchiver repo structure."
    )
    parser.add_argument(
        "--out-dir",
        default=str(Path(__file__).parent),
        help="Root of the CheatArchiver repo (default: script directory).",
    )
    parser.add_argument(
        "--system",
        default=None,
        help="Filter to a single system by numeric ID or partial name.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Seconds to wait between HTTP requests (default 1.0).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without creating any files.",
    )
    parser.add_argument(
        "--no-verify-ssl",
        action="store_true",
        help="Disable SSL certificate verification (use if you get SSL errors).",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of times to retry a failed HTTP request (default 3).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose debug output for HTTP requests.",
    )
    parser.add_argument(
        "--proxy",
        default=None,
        help="HTTP/HTTPS proxy URL (e.g., http://127.0.0.1:8080 or socks5://127.0.0.1:9050).",
    )
    args = parser.parse_args()

    out_dir      = Path(args.out_dir)
    consoles_dir = out_dir / "consoles"

    if args.no_verify_ssl:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use latest Chrome version (as of March 2026) and realistic headers
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/132.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Ch-Ua": '"Chromium";v="132", "Not(A:Brand";v="24", "Google Chrome";v="132"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Cache-Control": "max-age=0",
    }
    session = requests.Session()
    session.headers.update(headers)
    session.verify = not args.no_verify_ssl
    session.verbose = args.verbose  # Store verbose flag on session object
    
    # Configure proxy if provided
    if args.proxy:
        session.proxies = {
            "http": args.proxy,
            "https": args.proxy,
        }
        if args.verbose:
            print(f"Using proxy: {args.proxy}")
    
    if args.verbose:
        print("Session configuration:")
        print(f"  User-Agent: {headers['User-Agent']}")
        print(f"  SSL verification: {session.verify}")
        print(f"  Delay: {args.delay}s (with random jitter)")
        print(f"  Retries: {args.retries}")

    # First, visit the homepage to establish session cookies and look more legitimate
    try:
        print(f"Initializing session with {BASE_URL} …")
        resp = session.get(BASE_URL, timeout=30)
        resp.raise_for_status()
        random_delay(args.delay)  # Use random delay after homepage visit
    except requests.exceptions.RequestException as exc:
        print(f"  [WARN] Could not initialize session: {exc}")
        print("  Continuing anyway...")

    print(f"Fetching system list from {BASE_URL}/search …")
    try:
        systems = scrape_systems(session, args.delay, retries=args.retries)
    except requests.exceptions.RequestException as exc:
        sys.exit(f"ERROR: Could not fetch the system list.\n  {exc}")

    if not systems:
        sys.exit("No systems found. The page layout may have changed.")

    print(f"Found {len(systems)} system(s).")

    # Filter systems if --system was given
    if args.system:
        filter_val = args.system.lower()
        systems = [
            s for s in systems
            if filter_val in s["id"].lower() or filter_val in s["name"].lower()
        ]
        if not systems:
            sys.exit(f"No systems matched '{args.system}'.")
        print(f"Filtered to {len(systems)} system(s).")

    total_written = 0

    for system in systems:
        sys_id   = system["id"]
        sys_name = system["name"]
        print(f"\n=== System: {sys_name} (id={sys_id}) ===")

        try:
            games = scrape_game_list(session, sys_id, args.delay, retries=args.retries)
        except requests.exceptions.RequestException as exc:
            print(f"  ERROR fetching game list: {exc}  Skipping system.")
            continue
        print(f"  {len(games)} game(s) found.")

        for game_meta in games:
            print(f"  Scraping: {game_meta['title']} …", end=" ", flush=True)
            try:
                data = scrape_game(session, game_meta["url"], args.delay, retries=args.retries)
            except Exception as exc:
                print(f"ERROR: {exc}")
                continue

            console    = safe_name(data["console"] or sys_name)
            region     = safe_name(data["region"]  or "Unknown")
            game_title = safe_name(data["title"]   or game_meta["title"])
            cheat_type = data["cheat_type"] or "RAW"

            if not console:
                console = safe_name(sys_name)
            if not region:
                region = "Unknown"
            if not game_title:
                game_title = f"game_{game_meta['id']}"

            yaml_content = build_cheats_yaml(
                game       = data["title"]   or game_meta["title"],
                console    = data["console"] or sys_name,
                region     = data["region"]  or "Unknown",
                serial     = data["serial"],
                cheat_type = cheat_type,
                source_url = data["source_url"],
                cheats     = data["cheats"],
            )

            yaml_path = consoles_dir / console / region / game_title / "cheats.yaml"
            ensure_yaml(yaml_path, yaml_content, args.dry_run)
            total_written += 1
            print(f"OK ({len(data['cheats'])} cheats, type={cheat_type})")

    print(f"\nDone. {total_written} game(s) processed.")


if __name__ == "__main__":
    main()
