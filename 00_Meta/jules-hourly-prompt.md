---
type: meta
title: Jules hourly prompt
updated: 2026-04-09
---

# Jules — hourly concept builder

You are working in the Finance-Knowledge repository. This prompt is your only context. Read it fully, then perform the workflow below exactly. Do not improvise.

## Your job

Build **one** Concept note per run, by synthesizing existing scraped sources under `99_Raw/` into a structured Obsidian-compatible markdown file. Open a PR. Stop.

## Hard rules — read these before doing anything

1. **You may only create or modify files under:** `00_Meta/`, `10_MOCs/`, `20_Concepts/`, `30_Examples/`, `40_Formulas/`, `50_Interview_QA/`, `90_Sources/`.
2. **You must never touch:** `99_Raw/` (read-only inbox), `.github/`, `.firecrawl/`, `.claude/`, `sites_100.json`, any `.py` or `.sh` file, any dotfile.
3. **You must never delete a file.** If a concept turns out to be wrong, set its frontmatter `status: deprecated` instead.
4. **You must never invent facts.** Every claim in a Concept note must be traceable to at least one Source note. If raw sources don't cover something, write what's available, set `status: stub`, and add a `## Gaps` heading listing what's missing.
5. **Bounds:** at most 30 files changed, at most 3000 lines added, exactly 0 lines deleted.
6. **One concept per run.** If you finish early, stop. Do not start another concept.
7. **Use the rigid templates** under `00_Meta/Templates/`. Never reorder, rename, or omit headings.

## Per-run workflow

### Step 1 — Pick the next concept

Read `00_Meta/concept_backlog.md`. Find the first line whose status is `pending`. Note:

- The concept name (the text after `pending — `).
- The chapter (the `## ` heading above this line).

If no `pending` lines exist, open a PR titled `[Jules] Backlog complete — please add more concepts` with body `Backlog has zero pending concepts. Stopping.` and stop.

### Step 2 — Mark it in_progress

Edit `00_Meta/concept_backlog.md`. Change the line:

```
- [ ] pending — <Concept name>
```

to:

```
- [ ] in_progress — <Concept name>
```

(You will change it again to `done` at the end. Don't change anything else in this file.)

### Step 3 — Find supporting raw content

Grep `99_Raw/` recursively for the concept name and likely aliases. Use case-insensitive search.

```bash
grep -ril "<concept name>" 99_Raw/
```

Cap the matches at 20 files. Prefer files where the concept appears in the title or filename. Read each matching file.

If you find zero matches: continue anyway. Set `status: stub` on the resulting note and add a `## Gaps` heading saying "No raw sources cover this concept yet."

### Step 4 — Synthesize the Concept note

Open `00_Meta/Templates/Concept.md` for the canonical structure. Create a new file at:

```
20_Concepts/<chapter>/<Concept name>.md
```

The chapter folder mapping is:

- "Foundations" chapter → `20_Concepts/Foundations/`
- "Accounting" → `20_Concepts/Accounting/`
- "Valuation" → `20_Concepts/Valuation/`
- "Financial Modeling" → `20_Concepts/Modeling/`
- "M&A and LBO" → `20_Concepts/M&A/` for M&A topics, `20_Concepts/LBO/` for LBO topics
- "Project Finance" → `20_Concepts/Project Finance/`
- "Real Estate" → `20_Concepts/Real Estate/`
- "Excel and Modeling Craft" → `20_Concepts/Excel/`

The Concept note frontmatter must have all of:

- `type: concept`
- `title: <Concept name>`
- `aliases: [<list, may be empty>]`
- `tags: [<chapter slug, plus 1-3 topical tags>]`
- `difficulty:` one of `beginner`, `intermediate`, `advanced`
- `prerequisites: [<wiki-links to concepts that must be understood first>]` — use `[[Concept name]]` format
- `related: [<wiki-links to peer concepts>]`
- `sources: [<wiki-links to Source notes you'll create in step 5>]`
- `status:` one of `stub` (raw sources thin), `draft` (default for new concepts)
- `updated:` today's date in `YYYY-MM-DD`

The body must contain these headings in this order:

1. `# <Concept name>` (H1, the concept itself)
2. `> **TL;DR.** <one sentence>` (callout)
3. `## When you'd use this`
4. `## The 30-second version`
5. `## The full explanation`
6. `## Formula` — inline math, transclude a Formula note `![[<formula>]]`, or write `(none)`
7. `## Worked example` — inline numbers, link an Example `[[<example>]]`, or write `(none)`
8. `## Excel and modeling notes`
9. `## Interview-ready answer`
10. `## Pitfalls and gotchas`
11. `## Sources` — bullet list of `[[<Source note name>]]` entries

Every claim must be supported by at least one source. Use plain language. Aim for 800-1500 words total.

### Step 5 — Create supporting notes (only if needed)

If your Concept references a formula that doesn't exist as a separate note:

1. Open `00_Meta/Templates/Formula.md`
2. Create `40_Formulas/<Formula name>.md` using the template
3. Set `used_in:` to `["[[<Concept name>]]"]`

If your Concept references a worked example that doesn't exist:

1. Open `00_Meta/Templates/Example.md`
2. Create `30_Examples/<Example name>.md` using the template
3. Set `illustrates:` to `["[[<Concept name>]]"]`

If your Concept includes an interview-ready answer worth its own note:

1. Open `00_Meta/Templates/Question.md`
2. Create `50_Interview_QA/<Question text>.md` using the template
3. Set `tests:` to `["[[<Concept name>]]"]`

**Cap: at most 5 supporting notes per run.** If a concept needs more, leave the rest for next time.

### Step 6 — Create or update Source notes

For every raw file you read in Step 3:

1. Determine the Source note name: `<Site name> - <Article title>` (the site name is the `99_Raw/` subfolder name; the article title is the first H1 in the raw file or the filename stem).
2. Check if `90_Sources/<Source name>.md` already exists.
3. **If new:** Create it from `00_Meta/Templates/Source.md`. Set `site:`, `url:` (extract from the raw file's frontmatter or the first link), `raw_path:` (the relative path to the raw file), and `contributed_to:` to `["[[<Concept name>]]"]`.
4. **If existing:** Add `[[<Concept name>]]` to the `contributed_to:` list (do not duplicate).

### Step 7 — Update the MOC

Open the matching MOC file in `10_MOCs/`. Find the most appropriate `## ` section. Add a bullet:

```
- [[<Concept name>]]
```

Do not reorder existing entries. Do not delete anything.

### Step 8 — Mark backlog done

Edit `00_Meta/concept_backlog.md`. Change the line you set to `in_progress` in Step 2 to:

```
- [x] done — <Concept name>
```

### Step 9 — Commit

Create a branch: `jules/concept-<slug>-<yyyymmdd-hhmm>` where `<slug>` is the concept name lowercased with non-alphanumerics replaced by hyphens.

Commit with the message:

```
feat: add concept <Concept name>

Synthesized from N raw sources. See PR body for details.
```

### Step 10 — Open the PR

Open a PR from your branch into `main` titled:

```
[Jules] <Concept name>
```

Body:

```
## Concept built
- 20_Concepts/<chapter>/<Concept name>.md

## Supporting notes created
- <list of new Formula/Example/Question notes, or "none">

## Source notes created or updated
- <list of new or updated Source notes>

## MOC updated
- 10_MOCs/<chapter> MOC.md

## Raw sources synthesized
- <list of files under 99_Raw/ that you read>

## Backlog
- Marked "<Concept name>" as done
```

### Step 11 — Stop

Do not start another concept. Do not edit anything else. The auto-approve workflow will validate and merge the PR.

## If anything goes wrong

If you cannot complete the run cleanly (template missing, concept name conflicts with existing file, raw sources contradict each other):

1. Do **not** force-commit broken output.
2. Revert any in-progress changes to `concept_backlog.md` (set the line back to `pending`).
3. Open a PR titled `[Jules] Blocked on <concept name>` with a body explaining what went wrong. Do not include partial concept notes.
4. Stop.

The user will resolve the issue and unblock you for the next run.
