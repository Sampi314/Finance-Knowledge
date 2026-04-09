---
name: discover-finance-sites
description: Use when the user wants to find new finance/modeling/Excel websites to add to the knowledge vault. Searches the web with Firecrawl, presents up to 8 candidates with overlap analysis, waits for user approval, then crawls approved sites in parallel and opens a PR adding the raw content to 99_Raw/. Triggers - "/discover-finance-sites", "find new finance sites", "add a finance source", "discover sources".
---

# discover-finance-sites

This skill discovers new finance sources, gets the user's approval, and crawls them into `99_Raw/` so the next Jules run can synthesize them into concepts.

## When to use

- The user invokes `/discover-finance-sites` (with or without a topic hint).
- The user says "find new finance sites" or "add a finance source" or similar.
- The user wants to expand the knowledge vault's source coverage.

## Workflow

### Step 1 — Read the existing inventory

Read `scripts/sites_100.json`. Build a set of:

- Domains already covered (extract from each entry's `url` field)
- `key` slugs already used

You will use these as deny-lists in Step 3.

### Step 2 — Search the web

Use Firecrawl search (preferred — see `references/firecrawl-search.md` for exact commands) with queries derived from the user's hint.

If no hint was given, rotate through these default queries (pick 2-3):

- "financial modeling tutorials"
- "DCF walkthrough guide"
- "LBO modeling guide"
- "private equity analyst blog"
- "FP&A SaaS metrics"
- "corporate finance interview prep"
- "Excel for finance tutorial"

If the user gave a hint like `infrastructure project finance`, build queries from it: `"infrastructure project finance"`, `"infrastructure finance modeling tutorial"`, etc.

### Step 3 — Filter candidates

Discard search results matching any of:

- Domains already in `scripts/sites_100.json` (compare normalized hostname).
- Aggregator sites: `reddit.com`, `quora.com`, `youtube.com`, `wikipedia.org`, `medium.com` (tag pages).
- Paywall or login-only sites (heuristic: title contains "Subscribe to read", "Sign in to continue").
- Pure landing pages (no `/blog`, `/articles`, `/resources`, `/learn` paths visible).

### Step 4 — Inspect each candidate

For each remaining candidate (up to 8):

1. Firecrawl-fetch the homepage.
2. Locate an articles/blog/resources index.
3. Summarize what the site covers in 2-3 sentences (topics, depth, format).
4. Estimate overlap with existing sources by comparing topic keywords against existing folder names under `99_Raw/`. Return `Low`, `Medium`, or `High`.
5. Propose `include` paths for the scraper (e.g. `/blog,/resources`) — match what already-similar entries in `scripts/sites_100.json` use.

### Step 5 — Present the candidates

Show a table:

```
| # | Site            | URL              | Covers              | Overlap | Recommend |
| 1 | Example Finance | example.com      | LBO modeling        | Low     | Yes       |
| 2 | ...             | ...              | ...                 | ...     | ...       |
```

Then ask the user verbatim:

> "Reply with `approve 1,3,5` (specific indexes), `approve all`, or `reject all`."

### Step 6 — Wait for approval

Do not crawl anything until the user replies with an approval. If the user asks follow-up questions about a candidate, answer them, then re-prompt for approval.

### Step 7 — Append to scripts/sites_100.json

For each approved site:

1. Build the entry following `references/sites-json-schema.md`.
2. Insert it into `scripts/sites_100.json`, preserving the existing JSON formatting style (one entry per line, terminating comma except on the last entry).
3. Sort the entries alphabetically by `key` after inserting.

### Step 8 — Crawl in parallel

For each approved site, start a Firecrawl crawl as a **background bash task** (`run_in_background: true`). Do not run them serially — they can run concurrently.

For each background task, store:

- The site name and `key`
- The expected output folder `99_Raw/<folder>/`
- The background task handle so you can poll it

### Step 9 — Monitor and report

While crawls are running, periodically check progress (read the background task output). When each crawl completes, post a one-line update to the user:

```
Crawl finished: <site name> — <N> pages
```

Use a 30-minute hard timeout per crawl. If a crawl exceeds the timeout, kill it and report the failure to the user.

### Step 10 — Open the PR

After all crawls have finished (or timed out):

1. Check `git status` — confirm only `scripts/sites_100.json` and files under `99_Raw/<new folder>/` are changed.
2. Create a branch: `claude/discover-<yyyymmdd-hhmm>`.
3. Stage and commit:
   ```bash
   git add scripts/sites_100.json 99_Raw/<new folder 1>/ 99_Raw/<new folder 2>/ ...
   git commit -m "feat: discover and crawl <N> new finance sources

   Sources added:
   - <Site 1>: <N> pages
   - <Site 2>: <N> pages
   ..."
   ```
4. Push the branch and open a PR titled `[Claude] Discovered: <comma-separated site names>` with a body listing:
   - Each site, its URL, the proposed `include` paths, and the page count.
   - A note that the auto-merge workflow will land this if all checks pass.

### Step 11 — Hand off

After the PR is open, tell the user:

> "PR opened: <PR URL>. The auto-merge workflow will validate and land it. The next Jules hourly run will start synthesizing the new content into concepts."

Stop.

## Hard rules

- Never write outside `scripts/sites_100.json` and `99_Raw/<new folder>/`.
- Never modify existing files under `99_Raw/`.
- Never approve a site on the user's behalf — always wait for explicit `approve` reply.
- Never run more than 8 crawls in parallel (rate-limit safety).

## References

- `references/firecrawl-search.md` — exact Firecrawl commands for search and crawl.
- `references/sites-json-schema.md` — the shape of a `sites_100.json` entry.
