# CheatArchiver

> A community-maintained archive of emulator cheats, designed to preserve codes from sites that are disappearing from the internet.

---

## Table of Contents

1. [Live Example](#live-example)
2. [Goals](#goals)
3. [Why GitHub?](#why-github)
4. [Repository Strategy — One Repo or Many?](#repository-strategy--one-repo-or-many)
5. [Folder Hierarchy](#folder-hierarchy)
6. [File Formats](#file-formats)
7. [Cheat Entry Structure](#cheat-entry-structure)
8. [Pointer and Offset Structure](#pointer-and-offset-structure)
9. [README Index Pages](#readme-index-pages)
10. [Naming Conventions](#naming-conventions)
11. [Workflow for Adding Cheats](#workflow-for-adding-cheats)
12. [Scraping Source Data](#scraping-source-data)
13. [GitHub Pages (Future)](#github-pages-future)
14. [Contributing](#contributing)

---

## Live Example

A working example of the full structure is already in this repository. Follow the links to browse each level:

```
consoles/
└── PlayStation 2/
    └── NTSC-U/
        └── Grand Theft Auto - San Andreas/
            ├── README.md        ← game index page with all cheats
            ├── cheats.yaml      ← machine-readable cheat data
            └── patches/
                └── NTSC-U-Patch-v1.0/
                    ├── README.md    ← patch-specific cheat page
                    └── cheats.yaml
```

| Level | Link |
|---|---|
| All consoles | [consoles/](./consoles/) |
| PlayStation 2 | [consoles/PlayStation 2/](./consoles/PlayStation%202/) |
| NTSC-U region | [consoles/PlayStation 2/NTSC-U/](./consoles/PlayStation%202/NTSC-U/) |
| GTA San Andreas (game) | [consoles/PlayStation 2/NTSC-U/Grand Theft Auto - San Andreas/](./consoles/PlayStation%202/NTSC-U/Grand%20Theft%20Auto%20-%20San%20Andreas/) |
| GTA SA cheats (YAML) | [cheats.yaml](./consoles/PlayStation%202/NTSC-U/Grand%20Theft%20Auto%20-%20San%20Andreas/cheats.yaml) |
| Fan patch cheats | [patches/NTSC-U-Patch-v1.0/](./consoles/PlayStation%202/NTSC-U/Grand%20Theft%20Auto%20-%20San%20Andreas/patches/NTSC-U-Patch-v1.0/) |

---



- **Preserve** cheat codes from disappearing websites (e.g., gamehacking.org).
- **Organise** codes by Console → Region → Game → Patch (optional) → Cheat → Pointer/Offset.
- **Keep it human-readable** directly on GitHub without any tooling.
- **Keep it machine-readable** so scrapers, frontends, and tools can consume it.
- **Scale gracefully** as more consoles and thousands of games are added.

---

## Why GitHub?

| Feature | Benefit |
|---|---|
| **Always available** | GitHub has near-100% uptime and is backed by Microsoft. |
| **Version history** | Every change is tracked; codes can be restored if accidentally deleted. |
| **Free storage** | Repositories up to 1 GB are free; text-based cheat files are tiny. |
| **Rendered Markdown** | Every `README.md` in every folder is rendered as a browsable web page. |
| **GitHub Pages** | A free static site can be generated from the same files for a polished UI. |
| **Pull Requests** | Community contributions can be reviewed before merging. |
| **Issues** | Users can report incorrect or missing codes. |

---

## Repository Strategy — One Repo or Many?

### Option A — One repo per console ❌
Creates fragmentation. A user looking for "all SNES cheats" and "all Genesis cheats" would need to know which repo to visit. Cross-console searches are impossible. Maintenance overhead grows with every new console.

### Option B — One repo per game ❌
Produces thousands of micro-repositories. GitHub search cannot span repositories effectively. Indexing, linking, and discoverability all break down.

### Option C — Single monorepo ✅ **(Recommended)**

One repository (`CheatArchiver`) holds everything. GitHub renders a `README.md` at **every folder level**, so each console, region, and game automatically gets its own browsable index page. A single GitHub Pages site can be generated from the same folder tree.

Benefits:
- One URL to share.
- Global search works across all games.
- A single `git clone` gives a complete local archive.
- One set of contribution guidelines and CI scripts.

---

## Folder Hierarchy

```
CheatArchiver/
├── README.md                          ← Master index (this file)
│
└── consoles/
    ├── README.md                      ← Index of all consoles
    │
    ├── PlayStation 2/
    │   ├── README.md                  ← PS2 index + region list
    │   │
    │   ├── NTSC-U/
    │   │   ├── README.md              ← Region index + game list
    │   │   │
    │   │   └── Grand Theft Auto - San Andreas/
    │   │       ├── README.md          ← Game index (metadata + cheat list)
    │   │       ├── cheats.yaml        ← All base-game cheats (machine-readable)
    │   │       │
    │   │       └── patches/
    │   │           └── Some-Fan-Patch-v1.0/
    │   │               ├── README.md  ← Patch index
    │   │               └── cheats.yaml
    │   │
    │   └── PAL/
    │       └── ...
    │
    ├── Super Nintendo/
    │   └── ...
    │
    └── Game Boy Advance/
        └── ...
```

### Hierarchy levels

| Level | Folder / File | Purpose |
|---|---|---|
| 1 | `consoles/` | Root of all console data |
| 2 | `consoles/<Console>/` | One folder per hardware platform |
| 3 | `consoles/<Console>/<Region>/` | NTSC-U, NTSC-J, PAL, etc. |
| 4 | `consoles/<Console>/<Region>/<Game Title>/` | One folder per game |
| 5 *(optional)* | `.../patches/<Patch Name>/` | Applied patch variant of a game |
| 6 | `cheats.yaml` | Machine-readable cheat data for that game (or patch) |

---

## File Formats

Two files live at the game (or patch) level:

| File | Format | Purpose |
|---|---|---|
| `README.md` | Markdown | Human-readable display on GitHub; acts as the index page |
| `cheats.yaml` | YAML | Machine-readable data for tools, scrapers, and GitHub Pages |

Using **YAML** is preferred over JSON for cheat data because:
- Multi-line strings are readable without escape characters.
- Comments (`#`) allow documenting quirks inline.
- GitHub renders it with syntax highlighting.

---

## Cheat Entry Structure

Each entry in `cheats.yaml` follows this schema:

```yaml
# cheats.yaml
game: "Grand Theft Auto - San Andreas"
console: "PlayStation 2"
region: "NTSC-U"
serial: "SLUS-20946"          # optional disc serial number

cheats:
  - name: "Master Code"
    author: "ReallyCoolName"
    notes: "Must be enabled first."  # optional
    codes:
      - "F0100008 0000000E"

  - name: "Infinite Health"
    author: "AnotherCoder"
    codes:
      - "2A456B10 00000063"
      - "2A456B14 00000063"
```

The same entry rendered in `README.md` for human browsing:

```markdown
### Master Code [NTSC-U]
**Author:** ReallyCoolName  
**Notes:** Must be enabled first.

```
F0100008 0000000E
```
```

---

## Pointer and Offset Structure

Some cheats are **pointer-based**: the cheat engine first reads a base address, then follows one or more offsets to reach the final memory location. These are represented as a nested structure inside a cheat entry.

Each offset is an object with an `offset` (hex value) and an optional `label` that names what that hop in the chain represents. The base pointer and the final code also accept optional labels.

```yaml
  - name: "Infinite Ammo (Pointer)"
    author: "SomeHacker"
    notes: "Pointer chain to current weapon ammo."
    codes:
      - "D0000000 00000001"   # activator line (if any)
    pointers:
      - base: "203F8A00 00000000"   # base pointer read/write line
        base_label: "Player Pointer"
        offsets:
          - offset: "0x10"
            label: "Player Object"
          - offset: "0x24"
            label: "Weapon Slot"
          - offset: "0x08"
            label: "Ammo Count"
        final_code: "10456B00 000003E7"  # code applied at resolved address
        final_label: "Max Ammo Value"
```

The `label` fields are **optional** — you may omit them for any offset (or the base/final) if the meaning is unknown or self-evident.

### Pointer field definitions

| Field | Required | Description |
|---|---|---|
| `base` | ✅ | The code line that establishes the base address (same format as a regular code line) |
| `base_label` | ❌ | Human-readable name for the base pointer (e.g. `"Player Pointer"`) |
| `offsets` | ✅ | Ordered list of offset objects to dereference from the base |
| `offsets[].offset` | ✅ | Hex offset value (e.g. `"0x10"`) |
| `offsets[].label` | ❌ | Human-readable name for what this offset leads to (e.g. `"Health"`) |
| `final_code` | ✅ | The code applied at the fully resolved address |
| `final_label` | ❌ | Human-readable name for what the final write targets (e.g. `"Max Ammo Value"`) |

In the `README.md` this renders as:

```markdown
### Infinite Ammo (Pointer)
**Author:** SomeHacker

**Pointer chain:**
```
Base   [Player Pointer]:   203F8A00 00000000
  → +0x10  [Player Object]
  → +0x24  [Weapon Slot]
  → +0x08  [Ammo Count]
Final  [Max Ammo Value]:   10456B00 000003E7
```
```

---

## README Index Pages

GitHub automatically renders the `README.md` of any folder when you browse to it. We use this to create a navigable index at every level of the hierarchy.

### `consoles/README.md` — Console index

```markdown
# Consoles

| Console | Regions | Games |
|---|---|---|
| [PlayStation 2](./PlayStation%202/) | NTSC-U, NTSC-J, PAL | 1,240 |
| [Super Nintendo](./Super%20Nintendo/) | NTSC-U, PAL | 875 |
```

### `consoles/<Console>/README.md` — Region index

```markdown
# PlayStation 2

## Regions
- [NTSC-U](./NTSC-U/)
- [NTSC-J](./NTSC-J/)
- [PAL](./PAL/)
```

### `consoles/<Console>/<Region>/README.md` — Game index

```markdown
# PlayStation 2 — NTSC-U

## Games (A–Z)
- [Grand Theft Auto - San Andreas](./Grand%20Theft%20Auto%20-%20San%20Andreas/)
- [Kingdom Hearts](./Kingdom%20Hearts/)
```

### `consoles/<Console>/<Region>/<Game>/README.md` — Game detail page

```markdown
# Grand Theft Auto - San Andreas
**Console:** PlayStation 2  
**Region:** NTSC-U  
**Serial:** SLUS-20946  
**Source:** gamehacking.org

## Cheats

### Master Code [NTSC-U]
**Author:** ReallyCoolName  
**Notes:** Must be enabled first.
```
F0100008 0000000E
```

### Infinite Health
**Author:** AnotherCoder
```
2A456B10 00000063
2A456B14 00000063
```

## Patches
- [Some Fan Patch v1.0](./patches/Some-Fan-Patch-v1.0/)
```

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Console folder | Title case, no abbreviations | `PlayStation 2`, `Super Nintendo` |
| Region folder | Standard region codes | `NTSC-U`, `NTSC-J`, `PAL`, `World` |
| Game folder | Official title, dashes allowed, no slashes | `Grand Theft Auto - San Andreas` |
| Patch folder | Descriptive name + version | `Some-Fan-Patch-v1.0` |
| Cheat file | Always `cheats.yaml` | `cheats.yaml` |
| Index file | Always `README.md` | `README.md` |

- Use **spaces** in folder names (GitHub handles them; URL encoding is done automatically by browsers).
- Do **not** use special characters that break URLs: `/`, `?`, `#`, `%`, `&`.
- Replace `:` in game titles with ` -` (e.g., `Metroid - Zero Mission`).

---

## Workflow for Adding Cheats

1. **Fork** this repository.
2. Create the folder path for the console, region, and game if it does not exist.
3. Add or update `cheats.yaml` with the new cheat entries.
4. Add or update `README.md` to include the new cheats in a human-readable format.
5. Update the parent region `README.md` if the game is new (add it to the game list).
6. Open a **Pull Request** with a description of the source and any notes.

A future CI script will validate the YAML schema automatically before merging.

---

## Scraping Source Data

The initial dataset will be bootstrapped from [gamehacking.org](https://gamehacking.org/). The scraping process should:

1. Walk the site's console → game → cheat hierarchy.
2. Map each page to the folder structure above.
3. Write `cheats.yaml` and `README.md` for each game.
4. Commit in batches by console to keep pull requests reviewable.
5. Record the source URL in each `cheats.yaml` for attribution and future re-scraping.

---

## GitHub Pages (Future)

Once enough data is in place, a static site can be generated from the folder tree using a tool such as Jekyll, Hugo, or a custom script. The same `cheats.yaml` files power both the GitHub-rendered Markdown view and the GitHub Pages site.

A future `gh-pages` branch (or `docs/` folder) will contain the generated site. The plan is:

- A searchable game catalogue page.
- Individual game pages that render cheats with copy-to-clipboard buttons.
- Console and region filter pages.
- Mobile-friendly layout.

---

## Contributing

- Open an **Issue** to report a missing game, incorrect code, or broken link.
- Open a **Pull Request** to add or correct cheat data.
- Follow the naming conventions above.
- Provide a source URL wherever possible.

All contributions are welcome. The goal is to preserve this community knowledge before it disappears entirely.
