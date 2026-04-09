# Firecrawl commands for the discovery skill

The repo already uses Firecrawl via the `firecrawl:firecrawl-cli` plugin. Use that plugin where possible — it's the same one already used by `scrape_with_firecrawl.py`.

## Search

Use the Firecrawl search tool (from the `firecrawl:firecrawl-cli` plugin):

```
Tool: firecrawl search (or equivalent in the plugin)
Query: <one of the rotation queries or user hint>
Limit: 10
```

Returns a list of `{ title, url, description }`. Filter per Step 3 of the SKILL workflow.

## Fetch a single page (for inspection)

```
Tool: firecrawl scrape (or equivalent)
URL: <candidate homepage>
Format: markdown
```

Use this in Step 4 to inspect a candidate before recommending it.

## Crawl an entire site

For Step 8 (the actual content crawl), use the existing `scrape_with_firecrawl.py` script — do NOT invent a new crawl path:

```bash
python scrape_with_firecrawl.py --site "<site key>" --url "<site url>" --include "<include paths>" --output "99_Raw/<folder>/"
```

If `scrape_with_firecrawl.py` does not support these flags exactly, read the script first and call it with the right invocation. The point is: **reuse the existing scraper, don't bypass it**.

Run the crawl as a background bash task:

```
Bash tool, run_in_background: true
command: python scrape_with_firecrawl.py --site "<key>" ...
```

## Rate limits

- Maximum 8 concurrent crawls.
- 30-minute hard timeout per crawl.
- If Firecrawl returns a rate-limit error, wait 60 seconds and retry once. If it still fails, report to the user and skip that site.
