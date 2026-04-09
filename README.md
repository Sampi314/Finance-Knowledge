# Finance Knowledge

A self-building Obsidian vault that turns scraped finance content from ~20 sources into a structured curriculum and reference for self-study. The vault grows itself: an hourly Jules run picks the next concept from a backlog and synthesizes it from the raw sources, opening a PR that auto-merges if it stays within agreed lanes.

## What's in this repo

```
00_Meta/         meta docs, templates, the Jules prompt, the concept backlog
10_MOCs/         curriculum chapters (Maps of Content)
20_Concepts/     atomic concept notes (one concept per file), grouped by chapter
30_Examples/     worked numerical examples
40_Formulas/     one formula per file, transcluded into concepts
50_Interview_QA/ interview-style questions and answers
90_Sources/      pointer notes back to raw scraped articles
99_Raw/          raw Firecrawl output from ~20 finance sites — read-only
.github/         auto-approve workflow + frontmatter validator
.claude/         the /discover-finance-sites skill for adding new sources
docs/            design specs and implementation plans
```

## How to read the vault

Open this folder as an Obsidian vault.

- **Curriculum mode:** open `00_Meta/Reading order.md` and follow the eight chapter MOCs in order.
- **Reference mode:** `Ctrl+O`, type a concept name, land on the note. The TL;DR callout is the answer.
- **Graph view:** clusters of concepts emerge naturally because Jules links every concept to its prerequisites and related notes.

For details, see `00_Meta/How to use this vault.md`.

## How content gets added

### Hourly: Jules synthesizes one concept per run

`00_Meta/concept_backlog.md` is the to-do list. Jules picks the first `pending` line each hour, builds the corresponding Concept note (plus any supporting Formula/Example/Question/Source notes and a MOC link), opens a PR, and stops.

The full self-contained prompt is at `00_Meta/jules-hourly-prompt.md`. To set up Jules:

1. Open the prompt file. Copy the entire contents.
2. Paste it into a Jules scheduled task pointed at this repo, set to run hourly.
3. Done.

### On demand: Claude discovers new sources

In Claude Code (or another Claude environment that loads this repo's `.claude/skills/`), run:

```
/discover-finance-sites
/discover-finance-sites <topic hint>
```

Claude will search the web with Firecrawl, present up to 8 candidate sites, wait for your approval (`approve 1,3,5` or `approve all`), then crawl approved sites in parallel and open a PR adding them to `sites_100.json` and `99_Raw/`. The next Jules run will pick up the new content.

## Auto-approve PR workflow

`.github/workflows/auto-approve-bots.yml` runs on every PR. For PRs authored by Jules or Claude, it runs six guardrail checks:

1. **Path lane** — only allowed folders are touched
2. **Forbidden paths** — no edits to `.github/`, `.firecrawl/`, `.claude/`, scripts, dotfiles
3. **Diff size** — ≤30 files, ≤3000 lines added, 0 deleted
4. **Frontmatter validation** — required keys present per note type
5. **Secret scan** — no API keys in the diff
6. **Backlog consistency** (Jules only) — exactly one concept transitioned `pending → done`

If all six pass, the workflow auto-approves and squash-merges. If any fail, it leaves a comment on the PR explaining which check failed and waits for manual review.

## One-time setup

After cloning this repo, do these once:

1. **Enable branch protection on `main`** via the GitHub UI:
   - Settings → Branches → Add rule → Branch name pattern: `main`
   - Require status check `decide` (from `Auto-approve bot PRs`) to pass
   - Require linear history
   - Block force pushes and deletions
2. **Confirm the Jules and Claude bot logins** in `.github/workflows/auto-approve-bots.yml`. The current values are placeholders (`google-labs-jules[bot]`, `claude[bot]`, `claude-code[bot]`) — adjust on the first PR from each bot if the actual login differs.
3. **Schedule Jules hourly** with the prompt from `00_Meta/jules-hourly-prompt.md`.
4. **Verify the discovery skill loads** by running `/discover-finance-sites` once in Claude.

## Design and implementation docs

- `docs/superpowers/specs/2026-04-09-finance-knowledge-pipeline-design.md` — the design spec
- `docs/superpowers/plans/2026-04-09-finance-knowledge-pipeline.md` — the bootstrap implementation plan

## Existing scraper (untouched by automation)

The Python scripts at the repo root (`scrape_with_firecrawl.py`, `scrape_site.py`, etc.) and `sites_100.json` are the existing crawl primitive. Jules never touches them. Claude's discovery skill only appends new entries to `sites_100.json` and writes new folders under `99_Raw/`.
