# sites_100.json schema

Each entry is a JSON object with these fields. The file is a JSON array.

| Field | Type | Required | Notes |
|---|---|---|---|
| `key` | string | yes | Lowercase, alphanumeric only, no spaces. Used as a stable identifier. |
| `name` | string | yes | Human-readable site name. |
| `url` | string | yes | Site root URL, no trailing slash. |
| `include` | string | yes | Comma-separated path prefixes to crawl, or empty string for whole site. e.g. `/blog,/resources`. |
| `folder` | string | yes | Display name for the folder under `99_Raw/`. May contain spaces. |

## Example entries (already in sites_100.json)

```json
{"key": "mergersandinquisitions", "name": "Mergers & Inquisitions", "url": "https://mergersandinquisitions.com", "include": "/financial-modeling,/investment-banking,/private-equity,/hedge-funds,/real-estate,/articles", "folder": "Mergers and Inquisitions"}
```

```json
{"key": "asimplemodel", "name": "A Simple Model", "url": "https://www.asimplemodel.com", "include": "", "folder": "A Simple Model"}
```

## When adding a new entry

1. Pick a `key` that's lowercase, alphanumeric, unique, and short.
2. Pick `include` paths conservatively — start with the obvious blog/article roots only. The user can expand later.
3. The `folder` should match the site's display name without unsafe characters.
4. Insert preserving alphabetical order by `key`.
5. Preserve the existing one-entry-per-line formatting; do not reformat with `jq` or a pretty-printer.
