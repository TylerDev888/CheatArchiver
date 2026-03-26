# Debugging the Scraper

## Problem: "Could not find system selector on search page"

If you see this error message when running the scraper, it means the script cannot locate the HTML element that contains the list of gaming systems.

## Solution: Use the `--dump-html` flag

The `--dump-html` flag has been added to help debug these issues. It saves the actual HTML received from the server to a file so you can inspect it.

### Usage

```bash
python Scrape-GameHacking.py --system "PlayStation 2" --delay 5 --dump-html
```

### What happens

1. The script will attempt to scrape the search page
2. If it fails to find the system selector, it will save the HTML to `debug_search_page.html`
3. You can then open this file in a text editor or browser to see what the actual page structure looks like

### Inspecting the HTML

Once you have the `debug_search_page.html` file, look for:

1. **Select elements**: Search for `<select` tags
2. **System names**: Search for gaming system names like "PlayStation 2", "Nintendo", etc.
3. **Form elements**: Look for `<form>` tags that might contain the system selector
4. **JavaScript-rendered content**: Check if the content is loaded by JavaScript (in which case cloudscraper should handle it)

### Common Issues

1. **Page structure changed**: The website may have updated its HTML structure
   - Solution: Update the selector logic in `scrape_systems()` function

2. **JavaScript rendering**: Content may be loaded dynamically
   - Solution: cloudscraper should handle this, but check if JavaScript is disabled

3. **Cloudflare protection**: The page may be blocked by anti-bot measures
   - Solution: Try using `--proxy`, `--delay`, or check the HTML for Cloudflare challenge pages

### Example: Fixing the selector

If you find that the select element has a different attribute, you can update the code in `scrape_systems()`:

```python
# Current code looks for:
select = (
    soup.find("select", {"name": re.compile(r"system", re.I)}) or
    soup.find("select", {"id":   re.compile(r"system", re.I)})
)

# If the HTML shows the select has class="game-system-selector", update to:
select = (
    soup.find("select", {"name": re.compile(r"system", re.I)}) or
    soup.find("select", {"id":   re.compile(r"system", re.I)}) or
    soup.find("select", {"class": "game-system-selector"})
)
```

## Additional Debugging Options

Combine `--dump-html` with other debugging flags for more information:

```bash
# Maximum debugging information
python Scrape-GameHacking.py --system "PlayStation 2" --dump-html --verbose --delay 5

# Test with a proxy
python Scrape-GameHacking.py --system "PlayStation 2" --dump-html --proxy http://127.0.0.1:8080

# Dry run (no files written)
python Scrape-GameHacking.py --system "PlayStation 2" --dump-html --dry-run
```
