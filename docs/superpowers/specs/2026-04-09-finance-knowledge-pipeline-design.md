---
title: Finance Knowledge Pipeline — Design
date: 2026-04-09
status: approved
authors: [SamNgo, Claude]
---

# Finance Knowledge Pipeline — Design

## 1. Goal

Turn the existing scraped finance content (~40 source folders, thousands of markdown files in flat directories named by URL slug) into a structured, navigable Obsidian vault that serves both as a **self-study curriculum** (read top-down through Maps of Content) and a **professional reference** (look up any topic atomically). The pipeline runs largely on its own:

- **Jules** (Google async coding agent) runs hourly, picks the next concept from a backlog, synthesizes it from raw sources, opens a PR.
- **Claude** runs on demand via a `/discover-finance-sites` skill — proposes new sites to crawl, the user approves, Claude crawls with Firecrawl and opens a PR.
- **A GitHub Actions workflow** auto-approves and squash-merges PRs from Jules and Claude when they stay inside agreed lanes; otherwise the PR stays open for the user.

## 2. Non-goals

- Not a public-facing site. The vault is for the repo owner only.
- Not a question-answering chatbot. The output is markdown notes, not a live LLM interface.
- Not a replacement for the existing scraper. The Python scripts and `sites_100.json` remain the crawl primitive; nothing in this pipeline rewrites them.
- No deletion of existing scraped content. Original files stay under `99_Raw/` untouched.

## 3. Vault structure

```
Finance-Knowledge/                       (vault root = repo root)
├── 00_Meta/
│   ├── How to use this vault.md
│   ├── Reading order.md
│   ├── concept_backlog.md               (Jules state file)
│   ├── jules-hourly-prompt.md           (the prompt user pastes into Jules)
│   └── Templates/
│       ├── Concept.md
│       ├── Formula.md
│       ├── Example.md
│       ├── Question.md
│       ├── MOC.md
│       └── Source.md
├── 10_MOCs/
│   ├── Foundations MOC.md
│   ├── Accounting MOC.md
│   ├── Valuation MOC.md
│   ├── Financial Modeling MOC.md
│   ├── M&A and LBO MOC.md
│   ├── Project Finance MOC.md
│   ├── Real Estate MOC.md
│   └── Excel and Modeling Craft MOC.md
├── 20_Concepts/
│   ├── Foundations/
│   ├── Accounting/
│   ├── Valuation/
│   ├── Modeling/
│   ├── M&A/
│   ├── LBO/
│   ├── Project Finance/
│   ├── Real Estate/
│   └── Excel/
├── 30_Examples/
├── 40_Formulas/
├── 50_Interview_QA/
├── 90_Sources/
├── 99_Raw/                              (existing scraped folders moved here)
│   ├── A Simple Model/
│   ├── BIWS/
│   ├── CFI/
│   ├── ChallengeJP/
│   ├── Chandoo/
│   ├── Damodaran/
│   └── ... (~40 total)
├── .github/
│   ├── workflows/
│   │   └── auto-approve-bots.yml
│   └── scripts/
│       └── validate_frontmatter.py
├── .claude/
│   └── skills/
│       └── discover-finance-sites/
│           ├── SKILL.md
│           └── references/
│               ├── firecrawl-search.md
│               └── sites-json-schema.md
├── docs/
│   └── superpowers/
│       └── specs/
│           └── 2026-04-09-finance-knowledge-pipeline-design.md
├── README.md
├── sites_100.json                       (untouched by Jules; Claude appends only)
├── *.py                                 (existing scrapers; never modified by automation)
└── ...
```

Numeric folder prefixes follow the Johnny Decimal convention so the file tree sorts predictably in Obsidian. `99_Raw/` is the inbox: Jules reads from it, never writes to it. Claude (via the discovery skill) is the only automation that may add new files under `99_Raw/`.

## 4. Note types and templates

Six note types. Each has rigid YAML frontmatter so output is consistent and Dataview-queryable.

### 4.1 Concept

The atom of the vault. One concept = one file. Headings appear in the same order in every Concept note.

```markdown
---
type: concept
title: DCF valuation
aliases: [Discounted Cash Flow, DCF]
tags: [valuation, intrinsic-value, modeling]
difficulty: intermediate          # beginner | intermediate | advanced
prerequisites: ["[[WACC]]", "[[Free cash flow]]", "[[Time value of money]]"]
related: ["[[Comparable company analysis]]", "[[Precedent transactions]]"]
sources: ["[[CFI - Introduction to DCF]]", "[[A Simple Model - DCF basics]]"]
status: draft                     # stub | draft | reviewed | stable | deprecated
updated: 2026-04-09
---

# DCF valuation

> **TL;DR.** Value a company as the present value of its future free cash flows, discounted at its cost of capital.

## When you'd use this

## The 30-second version

## The full explanation

## Formula
![[WACC formula]]

## Worked example
See [[DCF example - SaaS company]].

## Excel and modeling notes

## Interview-ready answer
See [[Walk me through a DCF]].

## Pitfalls and gotchas

## Sources
- [[CFI - Introduction to DCF]]
- [[A Simple Model - DCF basics]]
```

**Required frontmatter keys:** `type`, `title`, `tags`, `difficulty`, `prerequisites`, `related`, `sources`, `status`, `updated`.
**Required headings (in order):** When you'd use this, The 30-second version, The full explanation, Formula, Worked example, Excel and modeling notes, Interview-ready answer, Pitfalls and gotchas, Sources.
A heading may contain "(none)" if not applicable, but it must still exist.

### 4.2 Formula

```markdown
---
type: formula
title: WACC formula
used_in: ["[[WACC]]", "[[DCF valuation]]"]
updated: 2026-04-09
---

# WACC formula

$$WACC = \frac{E}{V} \cdot R_e + \frac{D}{V} \cdot R_d \cdot (1 - T_c)$$

**Variables**
- $E$ = market value of equity
- $D$ = market value of debt
- $V = E + D$
- $R_e$ = [[Cost of equity]]
- $R_d$ = [[Cost of debt]]
- $T_c$ = marginal tax rate
```

### 4.3 Example

```markdown
---
type: example
title: DCF example - SaaS company
illustrates: ["[[DCF valuation]]", "[[Terminal value]]"]
updated: 2026-04-09
---

# DCF example — SaaS company

## Assumptions
## Cash flow projection
## Discount and sum
## Sensitivity
```

### 4.4 Question

```markdown
---
type: question
title: Walk me through a DCF
tests: ["[[DCF valuation]]", "[[WACC]]", "[[Terminal value]]"]
difficulty: intermediate
updated: 2026-04-09
---

# Walk me through a DCF

## The question
## Short answer (30 seconds)
## Long answer (2 minutes)
## Common follow-ups
```

### 4.5 MOC (Map of Content)

```markdown
---
type: moc
title: Valuation MOC
chapter_order: 3
updated: 2026-04-09
---

# Valuation — reading order

## 1. Foundations
- [[Time value of money]]
- [[Present value]]
- [[Free cash flow]]

## 2. Cost of capital
- [[CAPM]] → [[Beta]] → [[Equity risk premium]]
- [[Cost of debt]]
- [[WACC]]

## 3. Intrinsic valuation
- [[DCF valuation]]
- [[Terminal value]]
- [[Sensitivity analysis]]
```

### 4.6 Source

```markdown
---
type: source
title: CFI - Introduction to DCF
site: Corporate Finance Institute
url: https://corporatefinanceinstitute.com/resources/valuation/dcf-formula-guide/
raw_path: 99_Raw/CFI/resources_valuation_dcf-formula-guide.md
contributed_to: ["[[DCF valuation]]", "[[Free cash flow]]", "[[Terminal value]]"]
updated: 2026-04-09
---

Brief 2-3 sentence summary of what this source covers.
```

## 5. Linking model

| Link kind | Direction | Where it lives | Purpose |
|---|---|---|---|
| **Prerequisite** | Concept → simpler concepts | `prerequisites:` frontmatter | "You need to know X first." Drives auto-generated reading order. |
| **Related** | Concept ↔ peer concepts | `related:` frontmatter + inline `[[links]]` | Same neighborhood. Drives the graph view. |
| **Uses** | Concept → formulas/examples/questions | Inline `[[links]]` and transclusions `![[Formula]]` | Pulls in supporting material. |
| **Sourced-from** | Concept → Source → raw file | `sources:` frontmatter + Source's `contributed_to:` | Traceability. |

Backlinks (auto-tracked by Obsidian) handle reverse direction for free. Jules only writes forward links.

## 6. Jules hourly workflow

### 6.1 State

The single source of truth for "what's done / what's next" is `00_Meta/concept_backlog.md`. Format:

```markdown
# Concept backlog

Jules reads top-down. Picks the first concept whose status is `pending`, builds it, marks it `done`, opens a PR, stops.

## Foundations
- [ ] pending — Time value of money
- [ ] pending — Present value
- [ ] pending — Future value
- [x] done — Compound interest                  (PR #12, 2026-04-08T14:03Z)
- [ ] pending — Simple vs compound returns

## Accounting
- [ ] pending — The accounting equation
- [ ] pending — Double-entry bookkeeping
...
```

The initial backlog (~200 concepts) is seeded once during bootstrap. The user may freely reorder, add, or remove concepts at any time; Jules will pick up the new top-of-list `pending` entry on the next run.

### 6.2 Per-run sequence

1. Read `00_Meta/concept_backlog.md`. Pick the first concept whose status is `pending`. If none exist, open a PR titled `[Jules] Backlog complete — please add more concepts` and stop.
2. Mark that concept `in_progress` with the current ISO timestamp.
3. Grep `99_Raw/` recursively for the concept name and any aliases. Cap matches at 20 files (prefer the most substantive matches first — longer files, files with the concept in the title).
4. Read each matching file. Synthesize a single Concept note using `00_Meta/Templates/Concept.md`. Use the same headings in the same order, every time.
5. If the concept needs a Formula, Example, or Question note that does not yet exist, create it from the matching template. Cap: ≤5 supporting notes per run.
6. For every source file referenced, ensure a Source note exists in `90_Sources/`. If new, create it. Update its `contributed_to:` frontmatter to include the new concept.
7. Locate the right MOC in `10_MOCs/` (chapter mapping comes from the backlog grouping). Add the concept under the right section as a `[[wiki-link]]`.
8. Mark the concept `done` in the backlog with the run timestamp. The PR number annotation is optional (Jules does not yet know its own PR number at commit time); the consistency check only inspects the `pending → done` status transition, not the annotation.
9. Commit on a branch named `jules/concept-<slug>-<yyyymmdd-hhmm>`.
10. Open a PR titled `[Jules] <Concept Name>` with a body listing every file created or modified, plus the raw sources used.
11. Stop. Do not start another concept.

### 6.3 Hard rules (baked into the prompt)

- **Lanes:** May only create or modify files under `00_Meta/`, `10_MOCs/`, `20_Concepts/`, `30_Examples/`, `40_Formulas/`, `50_Interview_QA/`, `90_Sources/`.
- **Forbidden:** Never touch `99_Raw/`, `.github/`, `.firecrawl/`, `.claude/`, `sites_100.json`, any `.py` or `.sh` file, any dotfile.
- **No deletions, ever.** A wrong concept gets `status: deprecated` in frontmatter; the user does the actual deletion manually.
- **No invented facts.** Every claim must be traceable to at least one Source. If raw sources are thin, write what's available, mark `status: stub`, and add a `## Gaps` section listing what's missing.
- **Rigid template.** Never reorder, rename, or omit headings.
- **Bounds:** ≤30 files changed, ≤3000 lines added, 0 lines deleted.
- **One concept per run.** Even if the run finishes early, do not start another.

### 6.4 The prompt

The full self-contained prompt lives at `00_Meta/jules-hourly-prompt.md`. The user pastes this into Jules's scheduled task configuration. Each hourly run reads only this prompt + the current state of the repo — no other context is preserved between runs.

## 7. Auto-approve PR workflow

File: `.github/workflows/auto-approve-bots.yml`.

### 7.1 Trigger

`pull_request` events: `opened`, `synchronize`, `reopened`. Target branch: `main`.

### 7.2 Author gate

Job runs only if `github.event.pull_request.user.login` matches one of:
- `google-labs-jules[bot]` (placeholder; actual identity confirmed on first PR)
- `claude[bot]` / `claude-code[bot]` (whichever Claude integration the user uses)

For all other authors, the workflow is a no-op.

### 7.3 The six checks

Each is a separate workflow step so failures are individually visible.

1. **Path lane check.** Every changed file path must match an allowlist regex.
   - Jules allowlist: `^(00_Meta|10_MOCs|20_Concepts|30_Examples|40_Formulas|50_Interview_QA|90_Sources)/`
   - Claude allowlist: Jules's allowlist **plus** `^99_Raw/` and `^sites_100\.json$` (Claude may add new raw content via the discovery skill).
2. **Forbidden path check.** Fails if any changed file matches: `^\.github/`, `^\.firecrawl/`, `^\.claude/`, `\.py$`, `\.sh$`, `^\.env`, dotfiles at the repo root.
3. **Diff size check.** Fails if `> 30 files changed` OR `> 3000 lines added` OR `> 0 lines deleted`.
4. **Frontmatter validation.** Runs `.github/scripts/validate_frontmatter.py` against every new/changed `.md` in `10_MOCs/`, `20_Concepts/`, `30_Examples/`, `40_Formulas/`, `50_Interview_QA/`, `90_Sources/`. (Files under `99_Raw/` are explicitly skipped — they are raw Firecrawl output and have no required schema.) Confirms required keys exist for the note type and that `[[wiki-links]]` in `prerequisites:`/`related:`/`sources:` are syntactically valid.
5. **Secret scan.** Regex over the full diff for `sk-[A-Za-z0-9]{20,}`, `gh[ps]_[A-Za-z0-9]{20,}`, `AKIA[0-9A-Z]{16}`, `firecrawl-[A-Za-z0-9]{20,}`, `xoxb-`, etc. Any match fails the check.
6. **Backlog consistency check (Jules PRs only).** Diffs `00_Meta/concept_backlog.md` and confirms that exactly one line changed status from `pending` to `done` (no other lines may transition). Trailing PR-number annotations are ignored. Catches runaway runs that try to do multiple concepts at once.

### 7.4 Outcomes

- **All six pass:** workflow runs `gh pr review --approve` then `gh pr merge --squash --auto`.
- **Any fail:** workflow posts a comment naming the failing check and the offending paths or lines. PR stays open. The user decides manually.

### 7.5 Branch protection

The user enables branch protection on `main` once via the GitHub UI:
- Require status check `auto-approve-bots / decide` to pass before merge.
- Require linear history (squash merges only).
- Block force pushes and deletions on `main`.

This is documented in the README and called out in the implementation plan as a manual step.

## 8. Discovery skill

A user-invocable skill at `.claude/skills/discover-finance-sites/SKILL.md` (project-scoped, lives in the repo so it's versioned alongside the pipeline).

### 8.1 Invocation

```
/discover-finance-sites
/discover-finance-sites infrastructure project finance
/discover-finance-sites real estate modeling
```

### 8.2 Workflow

1. **Read inventory.** Open `sites_100.json`. Build a set of existing domains and `key` slugs to avoid re-suggesting.
2. **Search.** Use Firecrawl search (preferred — already used in this repo) with queries derived from the user's hint, or a default rotation if no hint: `"financial modeling tutorials"`, `"DCF walkthrough"`, `"LBO modeling guide"`, `"private equity blog"`, `"FP&A SaaS metrics"`, `"corporate finance interview"`, `"Excel finance tutorial"`.
3. **Filter.** Discard:
   - Domains already in `sites_100.json`.
   - Aggregator sites (Reddit, Quora, YouTube, Wikipedia, Medium tag pages).
   - Paywalled or login-only sites.
   - Sites with no article archive (pure landing pages or product sites).
4. **Inspect each candidate.** Firecrawl-fetch the homepage, locate an articles/blog/resources section, summarize coverage in 2-3 sentences, estimate overlap with existing sources (low/medium/high) by comparing topic keywords against existing folder names under `99_Raw/`.
5. **Present a ranked table** of up to 8 candidates:

   ```
   | # | Site            | URL          | Covers          | Overlap | Recommend |
   | 1 | Example Finance | example.com  | LBO modeling    | Low     | Yes       |
   ```

   With per-candidate proposed `include` paths.
6. **Wait for approval.** User replies `approve 1,3,5` or `approve all` or `reject all`.
7. **For each approved site, in parallel:**
   - Append a new entry to `sites_100.json` (alphabetical by `key`).
   - Create the target folder `99_Raw/<New Site Name>/`.
   - Kick off a Firecrawl crawl as a **background bash task** (using `run_in_background: true`). This lets multiple crawls run concurrently instead of serially.
8. **Wait and consolidate.** The skill continues monitoring the background crawls. As each one completes, it posts a brief progress line to the user (`Crawl finished: <site> — N pages`). When all crawls have completed (or hit a 30-minute timeout per crawl), the skill stages `sites_100.json` + every new `99_Raw/<site>/` folder, commits on a branch `claude/discover-<yyyymmdd-hhmm>`, and opens a single PR titled `[Claude] Discovered: <site list>`.
9. **The auto-merge workflow** sees a Claude-authored PR touching only `sites_100.json` and `99_Raw/`, the size check passes, and it merges.
10. **The next Jules run** sees new files in `99_Raw/` and the new content is naturally pulled into existing concepts on subsequent runs.

### 8.3 Skill files

- `.claude/skills/discover-finance-sites/SKILL.md` — frontmatter (`name`, `description`, `allowed-tools`) plus the workflow above as instructions.
- `.claude/skills/discover-finance-sites/references/firecrawl-search.md` — exact commands for Firecrawl search/scrape using the `firecrawl:firecrawl-cli` plugin.
- `.claude/skills/discover-finance-sites/references/sites-json-schema.md` — the exact shape of a `sites_100.json` entry (`key`, `name`, `url`, `include`, `folder`).

## 9. Bootstrap sequence

The implementation plan executes these in order. Each step is independently verifiable.

1. **Move existing scraped folders into `99_Raw/`.** A `git mv` for each of the ~40 existing folders. Content unchanged.
2. **Create `00_Meta/`** with `How to use this vault.md`, `Reading order.md`, the empty `concept_backlog.md` (filled in step 6), the empty `jules-hourly-prompt.md` (filled in step 7), and the six templates under `00_Meta/Templates/`.
3. **Create `10_MOCs/`** with eight stub MOC files (frontmatter + chapter heading + empty bullet list per section). Jules fills these as concepts complete.
4. **Create empty target folders:** `20_Concepts/<chapter>/`, `30_Examples/`, `40_Formulas/`, `50_Interview_QA/`, `90_Sources/`. Each gets a `.gitkeep` to make sure the folder is tracked.
5. **Write `.github/workflows/auto-approve-bots.yml`** + `.github/scripts/validate_frontmatter.py`.
6. **Seed `00_Meta/concept_backlog.md`** with ~200 concepts grouped by MOC chapter, in pedagogical order. (Claude writes this once during bootstrap based on standard finance curricula.)
7. **Write `00_Meta/jules-hourly-prompt.md`** — the full self-contained prompt the user pastes into Jules.
8. **Write `.claude/skills/discover-finance-sites/`** (SKILL.md + 2 references).
9. **Write `README.md`** at the repo root explaining the vault, the pipeline, and how to read it as a learner.
10. **Manual step:** the user enables branch protection on `main` per section 7.5.
11. **First Jules run.** The user pastes the prompt into Jules's scheduled task config and watches the first PR land.
12. **First discovery run.** The user invokes `/discover-finance-sites`, approves a couple of candidates, and watches the end-to-end flow.

## 10. Open issues / known unknowns

- **Bot identity strings.** The exact GitHub login for Jules and Claude is not yet confirmed. The auto-approve workflow uses placeholder logins; on the first PR from each, the user updates the workflow with the real string. This is called out in the README.
- **Firecrawl rate limits and credits.** Discovery-driven crawls consume Firecrawl credits at an unknown rate. The skill should warn the user if a candidate looks like a very large site (>500 pages) before kicking off the crawl.
- **Concept name collisions.** Two raw sources may use the same term for slightly different concepts (e.g., "free cash flow" — FCFF vs FCFE). Jules's prompt instructs it to prefer the most common usage and add a `## Disambiguation` section in the body, with separate concept notes if the meanings are truly different.
- **MOC chapter mapping.** A few concepts could belong in two chapters (e.g., "Working capital" — Accounting or Modeling?). The backlog assigns each concept to exactly one MOC chapter; Jules follows the backlog without second-guessing.

## 11. Success criteria

The pipeline is working when:

- Each hourly Jules run produces a PR that auto-merges, adding one concept (and zero to a few supporting notes) to the vault.
- After ~200 hours, the backlog is exhausted and the vault has ~200 polished Concept notes plus their supporting Formulas, Examples, Questions, MOCs, and Sources.
- A `/discover-finance-sites` invocation finds at least 3 new substantive sites the user wasn't already crawling, and the approved ones land in `99_Raw/` via an auto-merged PR within 30 minutes.
- The user can open the vault in Obsidian, click `10_MOCs/Valuation MOC.md`, and read the Valuation curriculum top-to-bottom by following `[[wiki-links]]`.
- The graph view shows clear topic clusters with MOCs as visible hubs.
