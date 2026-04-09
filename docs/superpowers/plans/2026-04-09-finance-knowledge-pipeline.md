# Finance Knowledge Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap a self-running finance knowledge pipeline: an Obsidian vault structure, a hourly Jules workflow that fills it from raw scraped sources, an auto-approve PR workflow for bot-authored PRs, and a Claude skill for discovering new finance sites to crawl.

**Architecture:** The repo becomes the vault root. Existing scraped folders move under `99_Raw/` (read-only inbox). Six numbered folders hold structured output (`00_Meta/`, `10_MOCs/`, `20_Concepts/`, `30_Examples/`, `40_Formulas/`, `50_Interview_QA/`, `90_Sources/`). Jules runs hourly off a checked-in backlog file. A GitHub Actions workflow auto-merges bot PRs that pass six guardrail checks. A `.claude/skills/discover-finance-sites/` skill lets Claude propose and crawl new sources on demand.

**Tech Stack:** Markdown + YAML frontmatter (Obsidian); Python 3 + PyYAML (validator); GitHub Actions YAML; Firecrawl (existing scraper); Jules (Google async coding agent, configured outside this repo).

**Spec:** `docs/superpowers/specs/2026-04-09-finance-knowledge-pipeline-design.md`

---

## File map

**Created in this plan:**

- `99_Raw/<existing folder>` × 20 — moved from repo root
- `00_Meta/How to use this vault.md`
- `00_Meta/Reading order.md`
- `00_Meta/concept_backlog.md` — Jules state file (~200 concepts)
- `00_Meta/jules-hourly-prompt.md` — self-contained prompt for Jules
- `00_Meta/Templates/Concept.md`
- `00_Meta/Templates/Formula.md`
- `00_Meta/Templates/Example.md`
- `00_Meta/Templates/Question.md`
- `00_Meta/Templates/MOC.md`
- `00_Meta/Templates/Source.md`
- `10_MOCs/Foundations MOC.md` and 7 more (8 total)
- `20_Concepts/<chapter>/.gitkeep` × 9
- `30_Examples/.gitkeep`
- `40_Formulas/.gitkeep`
- `50_Interview_QA/.gitkeep`
- `90_Sources/.gitkeep`
- `.github/workflows/auto-approve-bots.yml`
- `.github/scripts/validate_frontmatter.py`
- `.github/scripts/test_validate_frontmatter.py`
- `.claude/skills/discover-finance-sites/SKILL.md`
- `.claude/skills/discover-finance-sites/references/firecrawl-search.md`
- `.claude/skills/discover-finance-sites/references/sites-json-schema.md`
- `README.md`

**Untouched:** all existing `*.py`, `*.sh`, `*.html`, `sites_100.json`, `.firecrawl/`.

---

## Task 1: Move existing scraped folders into 99_Raw/

**Files:**
- Create: `99_Raw/` (empty parent directory)
- Move: 20 existing scraped folders from repo root into `99_Raw/`

**Why:** The Jules workflow and auto-approve guardrails treat `99_Raw/` as the read-only inbox. Until the move happens, Jules has no place to read from.

- [ ] **Step 1: Verify the current scraped folders**

Run:
```bash
cd C:/Users/SamNgo/Documents/GitHub/Finance-Knowledge
ls -d */ | grep -v '^docs/$'
```

Expected output (20 folders):
```
A Simple Model/
Andy Pope/
BIWS/
CFI/
ChallengeJP/
Chandoo/
Damodaran/
ExcelJet/
FAST Standard/
Financial Modelling Handbook/
Forvis Mazars/
Full Stack Modeller/
Gridlines/
Macabacus/
Mergers and Inquisitions/
Pivotal180/
Project Finance/
Sumproduct/
Trump Excel/
Wall Street Prep/
```

If the list differs (more or fewer folders), update the move command in Step 3 accordingly.

- [ ] **Step 2: Create the 99_Raw parent directory**

Run:
```bash
cd C:/Users/SamNgo/Documents/GitHub/Finance-Knowledge
mkdir -p 99_Raw
```

- [ ] **Step 3: Move all 20 folders with git mv**

Run each line individually (the spaces and `&` in folder names need exact quoting):
```bash
git mv "A Simple Model" "99_Raw/A Simple Model"
git mv "Andy Pope" "99_Raw/Andy Pope"
git mv "BIWS" "99_Raw/BIWS"
git mv "CFI" "99_Raw/CFI"
git mv "ChallengeJP" "99_Raw/ChallengeJP"
git mv "Chandoo" "99_Raw/Chandoo"
git mv "Damodaran" "99_Raw/Damodaran"
git mv "ExcelJet" "99_Raw/ExcelJet"
git mv "FAST Standard" "99_Raw/FAST Standard"
git mv "Financial Modelling Handbook" "99_Raw/Financial Modelling Handbook"
git mv "Forvis Mazars" "99_Raw/Forvis Mazars"
git mv "Full Stack Modeller" "99_Raw/Full Stack Modeller"
git mv "Gridlines" "99_Raw/Gridlines"
git mv "Macabacus" "99_Raw/Macabacus"
git mv "Mergers and Inquisitions" "99_Raw/Mergers and Inquisitions"
git mv "Pivotal180" "99_Raw/Pivotal180"
git mv "Project Finance" "99_Raw/Project Finance"
git mv "Sumproduct" "99_Raw/Sumproduct"
git mv "Trump Excel" "99_Raw/Trump Excel"
git mv "Wall Street Prep" "99_Raw/Wall Street Prep"
```

- [ ] **Step 4: Verify the move**

Run:
```bash
ls 99_Raw/ | wc -l
```
Expected: `20`

Run:
```bash
ls -d */ | grep -v '^docs/$' | grep -v '^99_Raw/$'
```
Expected: empty output (no scraped folders remain at root).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "$(cat <<'EOF'
chore: move scraped source folders into 99_Raw/

Per the Finance Knowledge Pipeline design, all existing scraped folders
become the read-only inbox at 99_Raw/. Content is unchanged.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Create the six note templates

**Files:**
- Create: `00_Meta/Templates/Concept.md`
- Create: `00_Meta/Templates/Formula.md`
- Create: `00_Meta/Templates/Example.md`
- Create: `00_Meta/Templates/Question.md`
- Create: `00_Meta/Templates/MOC.md`
- Create: `00_Meta/Templates/Source.md`

**Why:** Templates are the rigid contract for every note Jules writes. The validator script in Task 7 enforces the frontmatter shape against these templates.

- [ ] **Step 1: Create the templates directory**

Run:
```bash
mkdir -p "00_Meta/Templates"
```

- [ ] **Step 2: Write Concept template**

Create `00_Meta/Templates/Concept.md`:
````markdown
---
type: concept
title: <Concept name>
aliases: []
tags: []
difficulty: beginner
prerequisites: []
related: []
sources: []
status: stub
updated: YYYY-MM-DD
---

# <Concept name>

> **TL;DR.** <One-sentence definition.>

## When you'd use this

<2-4 sentences on the situations this concept applies to.>

## The 30-second version

<Plain-language explanation in ~100 words.>

## The full explanation

<Detailed explanation with sub-headings as needed.>

## Formula

<Inline math, or transclude a Formula note: ![[<formula name>]]. Use "(none)" if not applicable.>

## Worked example

<Inline numbers, or link a separate Example note: [[<example name>]]. Use "(none)" if not applicable.>

## Excel and modeling notes

<Practical Excel/modeling tips. Use "(none)" if not applicable.>

## Interview-ready answer

<2-3 sentences as you'd say in an interview, or link a Question note: [[<question name>]]. Use "(none)" if not applicable.>

## Pitfalls and gotchas

- <Pitfall 1>
- <Pitfall 2>

## Sources

- [[<Source note 1>]]
- [[<Source note 2>]]
````

- [ ] **Step 3: Write Formula template**

Create `00_Meta/Templates/Formula.md`:
````markdown
---
type: formula
title: <Formula name>
used_in: []
updated: YYYY-MM-DD
---

# <Formula name>

$$<LaTeX formula>$$

**Variables**

- $<symbol>$ — <definition, link to concept if applicable>

**Notes**

<Any caveats, alternate forms, or assumptions.>
````

- [ ] **Step 4: Write Example template**

Create `00_Meta/Templates/Example.md`:
````markdown
---
type: example
title: <Example name>
illustrates: []
updated: YYYY-MM-DD
---

# <Example name>

## Setup

<What we're modeling and why.>

## Assumptions

<Bulleted assumptions with values.>

## Walk-through

<Numbered steps with intermediate calculations.>

## Result

<Final answer with interpretation.>

## What this teaches

<2-3 bullets on the takeaways.>
````

- [ ] **Step 5: Write Question template**

Create `00_Meta/Templates/Question.md`:
````markdown
---
type: question
title: <Question text>
tests: []
difficulty: beginner
updated: YYYY-MM-DD
---

# <Question text>

## The question

<Verbatim question.>

## Short answer (30 seconds)

<3-4 sentences.>

## Long answer (2 minutes)

<Full structured answer with bullet points or numbered steps.>

## Common follow-ups

- <Follow-up 1 and how to handle it>
- <Follow-up 2 and how to handle it>
````

- [ ] **Step 6: Write MOC template**

Create `00_Meta/Templates/MOC.md`:
````markdown
---
type: moc
title: <Chapter name> MOC
chapter_order: 0
updated: YYYY-MM-DD
---

# <Chapter name> — reading order

<1-2 sentences describing what this chapter covers and who it's for.>

## 1. <Section name>

- [[<concept>]]
- [[<concept>]]

## 2. <Section name>

- [[<concept>]]
- [[<concept>]]
````

- [ ] **Step 7: Write Source template**

Create `00_Meta/Templates/Source.md`:
````markdown
---
type: source
title: <Site name> - <Article title>
site: <Site display name>
url: <https://example.com/article>
raw_path: 99_Raw/<Site folder>/<file>.md
contributed_to: []
updated: YYYY-MM-DD
---

<2-3 sentence summary of what this source covers and why it's useful.>
````

- [ ] **Step 8: Verify all six templates exist**

Run:
```bash
ls "00_Meta/Templates/" | sort
```
Expected:
```
Concept.md
Example.md
Formula.md
MOC.md
Question.md
Source.md
```

- [ ] **Step 9: Commit**

```bash
git add "00_Meta/Templates/"
git commit -m "$(cat <<'EOF'
feat: add six note templates for the vault

Concept, Formula, Example, Question, MOC, Source. Each template defines
the rigid frontmatter and headings Jules must follow.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Create vault meta documents

**Files:**
- Create: `00_Meta/How to use this vault.md`
- Create: `00_Meta/Reading order.md`

**Why:** When you (the user) open the vault in Obsidian, these are the two notes that orient you. They're written for a human reader, not Jules.

- [ ] **Step 1: Write How to use this vault.md**

Create `00_Meta/How to use this vault.md`:
````markdown
---
type: meta
title: How to use this vault
updated: 2026-04-09
---

# How to use this vault

This is a self-built finance knowledge vault. It's designed for two reading modes:

## Curriculum mode (read top-down)

Open [[Reading order]] and follow the chapters in order. Each chapter is a Map of Content (MOC) under `10_MOCs/` that links to concept notes in pedagogical order.

## Reference mode (look up a topic)

Press `Ctrl+O` and type the concept name. Land on the concept note. Skim the TL;DR callout for the answer; read further for depth.

## What's in each folder

| Folder | Purpose |
|---|---|
| `00_Meta/` | This file, the reading order, the concept backlog, templates, and the Jules prompt |
| `10_MOCs/` | Maps of Content — curriculum chapters that link to concepts in order |
| `20_Concepts/` | Atomic concept notes (one concept per file), grouped into chapter sub-folders |
| `30_Examples/` | Worked numerical examples referenced from concept notes |
| `40_Formulas/` | One formula per file, transcluded into concept notes via `![[formula]]` |
| `50_Interview_QA/` | Interview-style questions and answers |
| `90_Sources/` | Pointer notes back to the original scraped articles in `99_Raw/` |
| `99_Raw/` | Untouched output from the Firecrawl scraper. Read-only — Jules never modifies this. |

## How content gets added

- **Hourly:** Jules picks the next concept from `concept_backlog.md`, synthesizes it from `99_Raw/`, opens a PR, the auto-merge workflow lands it.
- **On demand:** Run the `/discover-finance-sites` skill in Claude. Claude proposes new sites to crawl. You approve. Claude crawls with Firecrawl into `99_Raw/`.

## Editing the backlog

`00_Meta/concept_backlog.md` is the to-do list. Reorder, add, or remove entries any time. Jules picks up the new top-of-list `pending` entry on the next hourly run.
````

- [ ] **Step 2: Write Reading order.md**

Create `00_Meta/Reading order.md`:
````markdown
---
type: meta
title: Reading order
updated: 2026-04-09
---

# Reading order

The eight chapters in pedagogical order. Read top to bottom for a finance curriculum.

1. [[Foundations MOC]] — time value of money, risk and return, discounting
2. [[Accounting MOC]] — the three financial statements, accruals, working capital
3. [[Valuation MOC]] — DCF, comparable companies, precedent transactions
4. [[Financial Modeling MOC]] — three-statement modeling, schedules, audit
5. [[M&A and LBO MOC]] — accretion-dilution, sources and uses, sponsor returns
6. [[Project Finance MOC]] — limited recourse, DSCR, debt sculpting
7. [[Real Estate MOC]] — cap rates, NOI, real estate waterfalls
8. [[Excel and Modeling Craft MOC]] — formulas, dynamic arrays, modeling conventions
````

- [ ] **Step 3: Commit**

```bash
git add "00_Meta/How to use this vault.md" "00_Meta/Reading order.md"
git commit -m "$(cat <<'EOF'
docs: add vault orientation documents

How to use this vault explains both reading modes. Reading order links
the eight chapter MOCs in pedagogical order.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: Create eight stub MOC files

**Files:**
- Create: `10_MOCs/Foundations MOC.md`
- Create: `10_MOCs/Accounting MOC.md`
- Create: `10_MOCs/Valuation MOC.md`
- Create: `10_MOCs/Financial Modeling MOC.md`
- Create: `10_MOCs/M&A and LBO MOC.md`
- Create: `10_MOCs/Project Finance MOC.md`
- Create: `10_MOCs/Real Estate MOC.md`
- Create: `10_MOCs/Excel and Modeling Craft MOC.md`

**Why:** Jules needs target MOC files to add concept links into. Stubs let the validator pass on day 1 with empty bullet lists, which Jules fills as concepts complete.

- [ ] **Step 1: Create the MOCs directory**

```bash
mkdir -p "10_MOCs"
```

- [ ] **Step 2: Write all eight MOC stubs**

Create `10_MOCs/Foundations MOC.md`:
```markdown
---
type: moc
title: Foundations MOC
chapter_order: 1
updated: 2026-04-09
---

# Foundations — reading order

Core financial concepts every analyst needs before touching valuation, modeling, or anything else.

## 1. Time and money

(none yet — Jules fills this as concepts complete)

## 2. Risk and return

(none yet)
```

Create `10_MOCs/Accounting MOC.md`:
```markdown
---
type: moc
title: Accounting MOC
chapter_order: 2
updated: 2026-04-09
---

# Accounting — reading order

The three financial statements and how they connect. Required reading before financial modeling.

## 1. The income statement

(none yet)

## 2. The balance sheet

(none yet)

## 3. The cash flow statement

(none yet)

## 4. Working capital and accruals

(none yet)
```

Create `10_MOCs/Valuation MOC.md`:
```markdown
---
type: moc
title: Valuation MOC
chapter_order: 3
updated: 2026-04-09
---

# Valuation — reading order

Intrinsic and relative valuation methods, from DCF to trading multiples to precedent transactions.

## 1. Enterprise value and equity value

(none yet)

## 2. Cost of capital

(none yet)

## 3. Intrinsic valuation (DCF)

(none yet)

## 4. Relative valuation

(none yet)
```

Create `10_MOCs/Financial Modeling MOC.md`:
```markdown
---
type: moc
title: Financial Modeling MOC
chapter_order: 4
updated: 2026-04-09
---

# Financial Modeling — reading order

Building three-statement models, supporting schedules, and audit-ready workbooks.

## 1. Three-statement model

(none yet)

## 2. Supporting schedules

(none yet)

## 3. Modeling craft and audit

(none yet)
```

Create `10_MOCs/M&A and LBO MOC.md`:
```markdown
---
type: moc
title: M&A and LBO MOC
chapter_order: 5
updated: 2026-04-09
---

# M&A and LBO — reading order

Mergers, acquisitions, and leveraged buyouts: deal structures, accretion-dilution, sponsor returns.

## 1. M&A fundamentals

(none yet)

## 2. Accretion-dilution analysis

(none yet)

## 3. LBO mechanics

(none yet)

## 4. Sponsor returns and exits

(none yet)
```

Create `10_MOCs/Project Finance MOC.md`:
```markdown
---
type: moc
title: Project Finance MOC
chapter_order: 6
updated: 2026-04-09
---

# Project Finance — reading order

Limited-recourse financing for infrastructure and energy projects: SPVs, coverage ratios, debt sculpting.

## 1. Structure and parties

(none yet)

## 2. Coverage ratios and debt sizing

(none yet)

## 3. Construction and operations phases

(none yet)
```

Create `10_MOCs/Real Estate MOC.md`:
```markdown
---
type: moc
title: Real Estate MOC
chapter_order: 7
updated: 2026-04-09
---

# Real Estate — reading order

Real estate underwriting and modeling: cap rates, NOI, development pro formas, partnership waterfalls.

## 1. Income property fundamentals

(none yet)

## 2. Development pro forma

(none yet)

## 3. Partnership structures and waterfalls

(none yet)
```

Create `10_MOCs/Excel and Modeling Craft MOC.md`:
```markdown
---
type: moc
title: Excel and Modeling Craft MOC
chapter_order: 8
updated: 2026-04-09
---

# Excel and Modeling Craft — reading order

The Excel skills and conventions that separate clean models from messy ones.

## 1. Lookup and array functions

(none yet)

## 2. Logic and conditionals

(none yet)

## 3. Modeling conventions

(none yet)

## 4. Charts and dashboards

(none yet)
```

- [ ] **Step 3: Verify all eight MOC files exist**

Run:
```bash
ls "10_MOCs/" | wc -l
```
Expected: `8`

- [ ] **Step 4: Commit**

```bash
git add "10_MOCs/"
git commit -m "$(cat <<'EOF'
feat: add eight stub MOC files for the curriculum chapters

Foundations, Accounting, Valuation, Financial Modeling, M&A and LBO,
Project Finance, Real Estate, Excel and Modeling Craft. Empty bullet
lists that Jules fills as concepts complete.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Create empty content folders with .gitkeep

**Files:**
- Create: `20_Concepts/Foundations/.gitkeep`
- Create: `20_Concepts/Accounting/.gitkeep`
- Create: `20_Concepts/Valuation/.gitkeep`
- Create: `20_Concepts/Modeling/.gitkeep`
- Create: `20_Concepts/M&A/.gitkeep`
- Create: `20_Concepts/LBO/.gitkeep`
- Create: `20_Concepts/Project Finance/.gitkeep`
- Create: `20_Concepts/Real Estate/.gitkeep`
- Create: `20_Concepts/Excel/.gitkeep`
- Create: `30_Examples/.gitkeep`
- Create: `40_Formulas/.gitkeep`
- Create: `50_Interview_QA/.gitkeep`
- Create: `90_Sources/.gitkeep`

**Why:** Git doesn't track empty folders. The `.gitkeep` placeholder is the standard pattern for committing an empty directory so Jules has a place to write files.

- [ ] **Step 1: Create all the directories and .gitkeep files**

Run:
```bash
mkdir -p "20_Concepts/Foundations" "20_Concepts/Accounting" "20_Concepts/Valuation" "20_Concepts/Modeling" "20_Concepts/M&A" "20_Concepts/LBO" "20_Concepts/Project Finance" "20_Concepts/Real Estate" "20_Concepts/Excel"
mkdir -p "30_Examples" "40_Formulas" "50_Interview_QA" "90_Sources"
touch "20_Concepts/Foundations/.gitkeep"
touch "20_Concepts/Accounting/.gitkeep"
touch "20_Concepts/Valuation/.gitkeep"
touch "20_Concepts/Modeling/.gitkeep"
touch "20_Concepts/M&A/.gitkeep"
touch "20_Concepts/LBO/.gitkeep"
touch "20_Concepts/Project Finance/.gitkeep"
touch "20_Concepts/Real Estate/.gitkeep"
touch "20_Concepts/Excel/.gitkeep"
touch "30_Examples/.gitkeep"
touch "40_Formulas/.gitkeep"
touch "50_Interview_QA/.gitkeep"
touch "90_Sources/.gitkeep"
```

- [ ] **Step 2: Verify the structure**

Run:
```bash
find 20_Concepts 30_Examples 40_Formulas 50_Interview_QA 90_Sources -name '.gitkeep' | sort
```
Expected: 13 lines.

- [ ] **Step 3: Commit**

```bash
git add 20_Concepts 30_Examples 40_Formulas 50_Interview_QA 90_Sources
git commit -m "$(cat <<'EOF'
feat: create empty content folders for vault structure

20_Concepts (with 9 chapter subfolders), 30_Examples, 40_Formulas,
50_Interview_QA, 90_Sources. .gitkeep placeholders so git tracks them.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: Seed the concept backlog

**Files:**
- Create: `00_Meta/concept_backlog.md`

**Why:** This is Jules's only state file. Without it, the hourly workflow has no work queue. ~200 concepts grouped by MOC chapter, in pedagogical order.

- [ ] **Step 1: Write the full backlog file**

Create `00_Meta/concept_backlog.md`:

````markdown
---
type: meta
title: Concept backlog
updated: 2026-04-09
---

# Concept backlog

Jules reads top-down. Picks the first concept whose status is `pending`, builds it, marks it `done`, opens a PR, stops.

Edit this file freely — reorder, add, remove. Jules picks up changes on the next hourly run.

**Status values:** `pending`, `in_progress`, `done`, `skipped`.

## Foundations

- [ ] pending — Time value of money
- [ ] pending — Present value
- [ ] pending — Future value
- [ ] pending — Compound interest
- [ ] pending — Simple vs compound returns
- [ ] pending — Discount rate
- [ ] pending — Risk and return basics
- [ ] pending — The risk-free rate
- [ ] pending — Inflation and real vs nominal
- [ ] pending — Annuity and perpetuity

## Accounting

- [ ] pending — The accounting equation
- [ ] pending — Double-entry bookkeeping
- [ ] pending — Debits and credits
- [ ] pending — The income statement
- [ ] pending — Revenue recognition
- [ ] pending — COGS and gross margin
- [ ] pending — Operating expenses
- [ ] pending — EBITDA
- [ ] pending — EBIT
- [ ] pending — Depreciation and amortization
- [ ] pending — Net income
- [ ] pending — The balance sheet
- [ ] pending — Current assets
- [ ] pending — Non-current assets
- [ ] pending — Working capital
- [ ] pending — Current liabilities
- [ ] pending — Long-term debt
- [ ] pending — Shareholders equity
- [ ] pending — Retained earnings
- [ ] pending — The cash flow statement
- [ ] pending — Cash from operations
- [ ] pending — Cash from investing
- [ ] pending — Cash from financing
- [ ] pending — Free cash flow
- [ ] pending — FCFF vs FCFE
- [ ] pending — Accruals vs cash accounting
- [ ] pending — Deferred revenue
- [ ] pending — Accounts receivable and DSO
- [ ] pending — Accounts payable and DPO
- [ ] pending — Inventory and DIO

## Valuation

- [ ] pending — Intrinsic vs relative valuation
- [ ] pending — Enterprise value
- [ ] pending — Equity value
- [ ] pending — The bridge from EV to equity value
- [ ] pending — Net debt
- [ ] pending — Minority interest
- [ ] pending — Cost of equity
- [ ] pending — CAPM
- [ ] pending — Beta
- [ ] pending — Levered vs unlevered beta
- [ ] pending — Equity risk premium
- [ ] pending — Cost of debt
- [ ] pending — Pre-tax vs after-tax cost of debt
- [ ] pending — Capital structure
- [ ] pending — WACC
- [ ] pending — Free cash flow projection
- [ ] pending — DCF valuation
- [ ] pending — Terminal value
- [ ] pending — Gordon growth method
- [ ] pending — Exit multiple method
- [ ] pending — Mid-year discounting convention
- [ ] pending — Sensitivity analysis
- [ ] pending — Scenario analysis
- [ ] pending — Comparable company analysis
- [ ] pending — Trading multiples
- [ ] pending — EV/EBITDA
- [ ] pending — EV/Revenue
- [ ] pending — P/E ratio
- [ ] pending — PEG ratio
- [ ] pending — Precedent transaction analysis
- [ ] pending — Control premium
- [ ] pending — Synergy adjustments
- [ ] pending — Football field chart
- [ ] pending — Sum-of-the-parts valuation
- [ ] pending — Dividend discount model

## Financial Modeling

- [ ] pending — Three-statement model
- [ ] pending — Linking the three statements
- [ ] pending — Revenue build top-down
- [ ] pending — Revenue build bottom-up
- [ ] pending — Cost build
- [ ] pending — Capex schedule
- [ ] pending — Depreciation schedule
- [ ] pending — Debt schedule
- [ ] pending — Interest expense circularity
- [ ] pending — Iterative calculations in Excel
- [ ] pending — Working capital schedule
- [ ] pending — Tax schedule
- [ ] pending — Equity schedule
- [ ] pending — Cash flow waterfall
- [ ] pending — Scenario manager
- [ ] pending — Data tables for sensitivity
- [ ] pending — Model checks and balances
- [ ] pending — Plug for balance sheet
- [ ] pending — Model documentation
- [ ] pending — Color coding conventions
- [ ] pending — FAST modeling standard
- [ ] pending — Hardcoded vs formula cells
- [ ] pending — Named ranges
- [ ] pending — Model audit
- [ ] pending — Model versioning

## M&A and LBO

- [ ] pending — M&A overview
- [ ] pending — Strategic vs financial buyers
- [ ] pending — Accretion dilution analysis
- [ ] pending — Purchase price
- [ ] pending — Sources and uses table
- [ ] pending — Goodwill creation
- [ ] pending — Synergies revenue and cost
- [ ] pending — Earn-outs
- [ ] pending — Pro forma combined model
- [ ] pending — Hostile vs friendly takeovers
- [ ] pending — Tender offers
- [ ] pending — Stock vs cash consideration
- [ ] pending — Tax-free reorganizations
- [ ] pending — Section 338 election
- [ ] pending — LBO overview
- [ ] pending — Sponsor returns
- [ ] pending — IRR
- [ ] pending — Multiple of money
- [ ] pending — Cash-on-cash return
- [ ] pending — LBO sources and uses
- [ ] pending — Senior debt
- [ ] pending — Mezzanine debt
- [ ] pending — Subordinated debt
- [ ] pending — PIK toggle
- [ ] pending — Revolver
- [ ] pending — Debt covenants
- [ ] pending — LBO exit
- [ ] pending — Management equity rollover
- [ ] pending — Dividend recap
- [ ] pending — Add-on acquisitions

## Project Finance

- [ ] pending — Project finance overview
- [ ] pending — Limited recourse financing
- [ ] pending — SPV structure
- [ ] pending — Equity vs debt in project finance
- [ ] pending — Debt service coverage ratio
- [ ] pending — Loan life coverage ratio
- [ ] pending — Project life coverage ratio
- [ ] pending — Cash sweep
- [ ] pending — Debt sculpting
- [ ] pending — Refinancing risk
- [ ] pending — Construction phase financing
- [ ] pending — Operations phase financing
- [ ] pending — Take-or-pay contracts
- [ ] pending — Power purchase agreements
- [ ] pending — Availability payments
- [ ] pending — Concession agreements
- [ ] pending — Public-private partnerships
- [ ] pending — Infrastructure asset classes
- [ ] pending — Real options in project finance
- [ ] pending — Distribution waterfall

## Real Estate

- [ ] pending — Real estate asset classes
- [ ] pending — Cap rate
- [ ] pending — Net operating income
- [ ] pending — Gross potential rent
- [ ] pending — Vacancy and credit loss
- [ ] pending — Operating expenses in RE
- [ ] pending — Replacement reserves
- [ ] pending — Cash-on-cash return for RE
- [ ] pending — Levered vs unlevered IRR
- [ ] pending — Real estate development pro forma
- [ ] pending — Hard costs and soft costs
- [ ] pending — Construction loans
- [ ] pending — Permanent loans
- [ ] pending — Real estate waterfall
- [ ] pending — Promote and carried interest
- [ ] pending — Preferred return
- [ ] pending — Refinance proceeds
- [ ] pending — Sale proceeds
- [ ] pending — Tax considerations in RE
- [ ] pending — 1031 exchange

## Excel and Modeling Craft

- [ ] pending — INDEX MATCH vs VLOOKUP
- [ ] pending — XLOOKUP
- [ ] pending — SUMIFS and COUNTIFS
- [ ] pending — IF and nested IF
- [ ] pending — IFS function
- [ ] pending — IFERROR and IFNA
- [ ] pending — INDIRECT
- [ ] pending — OFFSET
- [ ] pending — CHOOSE
- [ ] pending — Array formulas
- [ ] pending — Dynamic arrays
- [ ] pending — LET function
- [ ] pending — LAMBDA function
- [ ] pending — Pivot tables basics
- [ ] pending — Pivot tables for finance
- [ ] pending — Power Query
- [ ] pending — Power Pivot
- [ ] pending — Conditional formatting for models
- [ ] pending — Data validation
- [ ] pending — Form controls
- [ ] pending — Macro recording basics
- [ ] pending — VBA fundamentals for models
- [ ] pending — Goal seek
- [ ] pending — Solver
- [ ] pending — What-if analysis
- [ ] pending — Custom number formats
- [ ] pending — Charts for finance dashboards
- [ ] pending — Sparklines
- [ ] pending — Keyboard shortcuts for analysts
- [ ] pending — Cell styles and themes
````

- [ ] **Step 2: Verify the file is well-formed**

Run:
```bash
grep -c '^- \[ \] pending' "00_Meta/concept_backlog.md"
```
Expected: `200`

Run:
```bash
grep -c '^## ' "00_Meta/concept_backlog.md"
```
Expected: `8`

- [ ] **Step 3: Commit**

```bash
git add "00_Meta/concept_backlog.md"
git commit -m "$(cat <<'EOF'
feat: seed concept backlog with 200 concepts across 8 chapters

Foundations (10), Accounting (30), Valuation (35), Financial Modeling
(25), M&A and LBO (30), Project Finance (20), Real Estate (20), Excel
and Modeling Craft (30). Pedagogical order. Jules picks the next
pending entry each hourly run.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Write the frontmatter validator (TDD)

**Files:**
- Create: `.github/scripts/validate_frontmatter.py`
- Create: `.github/scripts/test_validate_frontmatter.py`

**Why:** The auto-merge workflow calls this script as one of the six guardrail checks. It must reject malformed notes (missing required keys, wrong type) before they reach `main`. TDD ensures the validator's behavior matches the templates exactly.

- [ ] **Step 1: Create scripts directory and install pyyaml**

```bash
mkdir -p .github/scripts
pip install pyyaml pytest
```

If `pip` is not on PATH, try `python -m pip install pyyaml pytest` or `py -m pip install pyyaml pytest`.

- [ ] **Step 2: Write the test file (failing tests)**

Create `.github/scripts/test_validate_frontmatter.py`:
````python
"""Tests for validate_frontmatter.py.

Run with: pytest .github/scripts/test_validate_frontmatter.py -v
"""
from pathlib import Path
import pytest

from validate_frontmatter import (
    parse_frontmatter,
    validate_note,
    REQUIRED_KEYS,
    ValidationError,
)


def make_note(frontmatter: str, body: str = "# Title\n\ncontent") -> str:
    return f"---\n{frontmatter}\n---\n\n{body}\n"


# parse_frontmatter

def test_parse_frontmatter_extracts_yaml_block():
    note = make_note("type: concept\ntitle: WACC")
    fm = parse_frontmatter(note)
    assert fm == {"type": "concept", "title": "WACC"}


def test_parse_frontmatter_missing_block_raises():
    with pytest.raises(ValidationError, match="no YAML frontmatter"):
        parse_frontmatter("# Just a heading\n\nNo frontmatter.")


def test_parse_frontmatter_malformed_yaml_raises():
    note = "---\ntype: concept\ntitle: [unclosed\n---\nbody"
    with pytest.raises(ValidationError, match="invalid YAML"):
        parse_frontmatter(note)


# validate_note — concept

def test_concept_with_all_required_keys_passes():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": ["valuation"],
        "difficulty": "intermediate",
        "prerequisites": ["[[Cost of equity]]"],
        "related": ["[[DCF valuation]]"],
        "sources": ["[[CFI - WACC guide]]"],
        "status": "draft",
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_missing_required_key_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        # missing tags, difficulty, prerequisites, related, sources, status, updated
    }
    with pytest.raises(ValidationError, match="missing required key"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_wrong_difficulty_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "expert",  # not in allowed set
        "prerequisites": [],
        "related": [],
        "sources": [],
        "status": "draft",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="difficulty"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_wrong_status_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "beginner",
        "prerequisites": [],
        "related": [],
        "sources": [],
        "status": "in_review",  # not in allowed set
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="status"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


def test_concept_invalid_wikilink_in_prerequisites_fails():
    fm = {
        "type": "concept",
        "title": "WACC",
        "tags": [],
        "difficulty": "beginner",
        "prerequisites": ["Cost of equity"],  # missing [[ ]]
        "related": [],
        "sources": [],
        "status": "draft",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="wiki-link"):
        validate_note(fm, Path("20_Concepts/Valuation/WACC.md"))


# validate_note — formula

def test_formula_with_all_required_keys_passes():
    fm = {
        "type": "formula",
        "title": "WACC formula",
        "used_in": ["[[WACC]]"],
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("40_Formulas/WACC formula.md"))


def test_formula_missing_used_in_fails():
    fm = {
        "type": "formula",
        "title": "WACC formula",
        "updated": "2026-04-09",
    }
    with pytest.raises(ValidationError, match="missing required key"):
        validate_note(fm, Path("40_Formulas/WACC formula.md"))


# validate_note — moc

def test_moc_with_all_required_keys_passes():
    fm = {
        "type": "moc",
        "title": "Valuation MOC",
        "chapter_order": 3,
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("10_MOCs/Valuation MOC.md"))


# validate_note — source

def test_source_with_all_required_keys_passes():
    fm = {
        "type": "source",
        "title": "CFI - WACC guide",
        "site": "Corporate Finance Institute",
        "url": "https://example.com",
        "raw_path": "99_Raw/CFI/wacc-guide.md",
        "contributed_to": ["[[WACC]]"],
        "updated": "2026-04-09",
    }
    validate_note(fm, Path("90_Sources/CFI - WACC guide.md"))


# validate_note — type detection

def test_unknown_type_fails():
    fm = {"type": "blogpost", "title": "x", "updated": "2026-04-09"}
    with pytest.raises(ValidationError, match="unknown type"):
        validate_note(fm, Path("20_Concepts/x.md"))


def test_missing_type_fails():
    fm = {"title": "x", "updated": "2026-04-09"}
    with pytest.raises(ValidationError, match="missing required key.*type"):
        validate_note(fm, Path("20_Concepts/x.md"))
````

- [ ] **Step 3: Run the tests to verify they fail**

Run:
```bash
cd .github/scripts && python -m pytest test_validate_frontmatter.py -v
```
Expected: import error or all tests fail (because `validate_frontmatter.py` does not exist yet).

- [ ] **Step 4: Write the validator implementation**

Create `.github/scripts/validate_frontmatter.py`:
````python
"""Validate YAML frontmatter in vault markdown notes.

Used by the auto-approve PR workflow to enforce the rigid contract for
each note type. See docs/superpowers/specs/2026-04-09-finance-knowledge-pipeline-design.md
section 4 for the schema.

Usage:
    python validate_frontmatter.py <file1.md> <file2.md> ...

Exits 0 on success, non-zero on any validation failure (with messages on
stderr).

Files under 99_Raw/ are skipped — they are raw scraper output and have
no required schema.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


class ValidationError(Exception):
    """Raised when a note's frontmatter does not match its type's contract."""


# Per-type required frontmatter keys.
REQUIRED_KEYS: dict[str, list[str]] = {
    "concept": [
        "type", "title", "tags", "difficulty", "prerequisites",
        "related", "sources", "status", "updated",
    ],
    "formula": ["type", "title", "used_in", "updated"],
    "example": ["type", "title", "illustrates", "updated"],
    "question": ["type", "title", "tests", "difficulty", "updated"],
    "moc": ["type", "title", "chapter_order", "updated"],
    "source": [
        "type", "title", "site", "url", "raw_path",
        "contributed_to", "updated",
    ],
}

ALLOWED_DIFFICULTY = {"beginner", "intermediate", "advanced"}
ALLOWED_STATUS = {"stub", "draft", "reviewed", "stable", "deprecated"}

# Wiki-link list keys: every entry must look like "[[...]]"
WIKILINK_LIST_KEYS = {
    "prerequisites", "related", "sources",
    "used_in", "illustrates", "tests", "contributed_to",
}

WIKILINK_RE = re.compile(r"^\[\[[^\[\]]+\]\]$")

FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL
)


def parse_frontmatter(text: str) -> dict[str, Any]:
    """Extract and parse the YAML frontmatter block at the top of a note."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValidationError("no YAML frontmatter found at start of file")
    raw = match.group(1)
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise ValidationError(f"invalid YAML in frontmatter: {e}") from e
    if not isinstance(data, dict):
        raise ValidationError("frontmatter is not a YAML mapping")
    return data


def validate_note(fm: dict[str, Any], path: Path) -> None:
    """Validate a parsed frontmatter dict for the given note path.

    Raises ValidationError on failure with a path-prefixed message.
    """
    if "type" not in fm:
        raise ValidationError(f"{path}: missing required key 'type'")

    note_type = fm["type"]
    if note_type not in REQUIRED_KEYS:
        raise ValidationError(
            f"{path}: unknown type '{note_type}' "
            f"(allowed: {sorted(REQUIRED_KEYS)})"
        )

    for key in REQUIRED_KEYS[note_type]:
        if key not in fm:
            raise ValidationError(
                f"{path}: missing required key '{key}' for type '{note_type}'"
            )

    # difficulty (concept, question)
    if "difficulty" in REQUIRED_KEYS[note_type]:
        if fm["difficulty"] not in ALLOWED_DIFFICULTY:
            raise ValidationError(
                f"{path}: difficulty '{fm['difficulty']}' not in {sorted(ALLOWED_DIFFICULTY)}"
            )

    # status (concept only)
    if note_type == "concept":
        if fm["status"] not in ALLOWED_STATUS:
            raise ValidationError(
                f"{path}: status '{fm['status']}' not in {sorted(ALLOWED_STATUS)}"
            )

    # wiki-link list values
    for key in WIKILINK_LIST_KEYS:
        if key not in fm:
            continue
        value = fm[key]
        if not isinstance(value, list):
            raise ValidationError(
                f"{path}: '{key}' must be a list, got {type(value).__name__}"
            )
        for entry in value:
            if not isinstance(entry, str) or not WIKILINK_RE.match(entry):
                raise ValidationError(
                    f"{path}: '{key}' entry {entry!r} is not a valid wiki-link "
                    "(expected '[[Note name]]')"
                )


def should_skip(path: Path) -> bool:
    """Skip files that don't need validation."""
    parts = path.parts
    if not parts:
        return True
    if parts[0] == "99_Raw":
        return True
    if path.name == ".gitkeep":
        return True
    if not path.name.endswith(".md"):
        return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_frontmatter.py <file.md> [...]", file=sys.stderr)
        return 2

    errors: list[str] = []
    checked = 0

    for arg in argv[1:]:
        path = Path(arg)
        if should_skip(path):
            continue
        if not path.exists():
            errors.append(f"{path}: file does not exist")
            continue
        try:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            validate_note(fm, path)
            checked += 1
        except ValidationError as e:
            errors.append(str(e))

    if errors:
        print(f"FAIL: {len(errors)} validation error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {checked} note(s) validated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

- [ ] **Step 5: Run the tests to verify they pass**

Run:
```bash
cd .github/scripts && python -m pytest test_validate_frontmatter.py -v
```
Expected: all tests pass.

- [ ] **Step 6: Smoke-test against the actual templates**

Run from repo root:
```bash
python .github/scripts/validate_frontmatter.py "00_Meta/Templates/Concept.md" "00_Meta/Templates/MOC.md"
```

The templates have placeholder `<...>` values, so they will fail (e.g., `difficulty: beginner` is fine, but `updated: YYYY-MM-DD` will fail YAML parsing or pass as a string — and `tags: []` is valid). Run it and observe what fails.

If templates fail validation: that's expected — templates are not valid notes, they're scaffolds. The validator only runs against real notes the workflow encounters.

- [ ] **Step 7: Smoke-test against the eight stub MOCs**

Run from repo root:
```bash
python .github/scripts/validate_frontmatter.py 10_MOCs/*.md
```
Expected: `OK: 8 note(s) validated`

If this fails, fix the MOC stubs from Task 4 to satisfy the validator before continuing.

- [ ] **Step 8: Commit**

```bash
git add .github/scripts/
git commit -m "$(cat <<'EOF'
feat: add frontmatter validator with TDD test suite

Enforces the rigid per-note-type schema from the design spec. Skips
99_Raw/ (raw scraper output, no schema). Used by the auto-approve PR
workflow as one of the six guardrail checks.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Write the auto-approve PR workflow

**Files:**
- Create: `.github/workflows/auto-approve-bots.yml`

**Why:** This is the workflow that lets Jules and Claude land PRs without manual review when the PR stays within the agreed lanes. Spec section 7 defines the six checks.

- [ ] **Step 1: Create workflows directory**

```bash
mkdir -p .github/workflows
```

- [ ] **Step 2: Write the workflow**

Create `.github/workflows/auto-approve-bots.yml`:
````yaml
name: Auto-approve bot PRs

on:
  pull_request:
    types: [opened, synchronize, reopened]
    branches: [main]

permissions:
  contents: write
  pull-requests: write

jobs:
  decide:
    runs-on: ubuntu-latest
    # Author gate: only run for known bot accounts.
    # Update these logins on the first real PR from each bot.
    if: >
      github.event.pull_request.user.login == 'google-labs-jules[bot]' ||
      github.event.pull_request.user.login == 'jules-bot' ||
      github.event.pull_request.user.login == 'claude[bot]' ||
      github.event.pull_request.user.login == 'claude-code[bot]'
    steps:
      - name: Checkout PR head
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.sha }}

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install validator dependencies
        run: pip install pyyaml

      - name: Compute changed files
        id: diff
        run: |
          set -euo pipefail
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"
          git fetch origin "$BASE" --depth=1 || true
          CHANGED=$(git diff --name-only "$BASE" "$HEAD")
          echo "$CHANGED" > /tmp/changed.txt
          echo "Files changed:"
          cat /tmp/changed.txt

          ADDED=$(git diff --numstat "$BASE" "$HEAD" | awk '{a+=$1} END {print a+0}')
          DELETED=$(git diff --numstat "$BASE" "$HEAD" | awk '{d+=$2} END {print d+0}')
          COUNT=$(wc -l < /tmp/changed.txt | tr -d ' ')

          echo "added=$ADDED" >> $GITHUB_OUTPUT
          echo "deleted=$DELETED" >> $GITHUB_OUTPUT
          echo "count=$COUNT" >> $GITHUB_OUTPUT

      - name: Check 1 — path lane
        run: |
          set -euo pipefail
          AUTHOR="${{ github.event.pull_request.user.login }}"
          # Jules allowlist
          ALLOW='^(00_Meta|10_MOCs|20_Concepts|30_Examples|40_Formulas|50_Interview_QA|90_Sources)/'
          # Claude allowlist adds 99_Raw/ and sites_100.json
          if [[ "$AUTHOR" == "claude[bot]" || "$AUTHOR" == "claude-code[bot]" ]]; then
            ALLOW='^(00_Meta|10_MOCs|20_Concepts|30_Examples|40_Formulas|50_Interview_QA|90_Sources|99_Raw)/|^sites_100\.json$'
          fi
          BAD=$(grep -vE "$ALLOW" /tmp/changed.txt || true)
          if [ -n "$BAD" ]; then
            echo "::error::Path lane check failed for $AUTHOR. Files outside allowed lanes:"
            echo "$BAD"
            exit 1
          fi

      - name: Check 2 — forbidden paths
        run: |
          set -euo pipefail
          FORBID='^\.github/|^\.firecrawl/|^\.claude/|\.py$|\.sh$|^\.env|^\.[^/]+$'
          BAD=$(grep -E "$FORBID" /tmp/changed.txt || true)
          if [ -n "$BAD" ]; then
            echo "::error::Forbidden path check failed. Files match forbidden patterns:"
            echo "$BAD"
            exit 1
          fi

      - name: Check 3 — diff size
        run: |
          set -euo pipefail
          COUNT=${{ steps.diff.outputs.count }}
          ADDED=${{ steps.diff.outputs.added }}
          DELETED=${{ steps.diff.outputs.deleted }}
          echo "files=$COUNT added=$ADDED deleted=$DELETED"
          if [ "$COUNT" -gt 30 ]; then
            echo "::error::Diff size check failed: $COUNT files changed (max 30)"
            exit 1
          fi
          if [ "$ADDED" -gt 3000 ]; then
            echo "::error::Diff size check failed: $ADDED lines added (max 3000)"
            exit 1
          fi
          if [ "$DELETED" -gt 0 ]; then
            echo "::error::Diff size check failed: $DELETED lines deleted (must be 0)"
            exit 1
          fi

      - name: Check 4 — frontmatter validation
        run: |
          set -euo pipefail
          MD_FILES=$(grep -E '^(10_MOCs|20_Concepts|30_Examples|40_Formulas|50_Interview_QA|90_Sources)/.*\.md$' /tmp/changed.txt || true)
          if [ -z "$MD_FILES" ]; then
            echo "No vault markdown files in this PR, skipping frontmatter check"
            exit 0
          fi
          echo "Validating: $MD_FILES"
          python .github/scripts/validate_frontmatter.py $MD_FILES

      - name: Check 5 — secret scan
        run: |
          set -euo pipefail
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"
          DIFF=$(git diff "$BASE" "$HEAD")
          # Patterns: OpenAI sk-, GitHub gh[ps]_, AWS AKIA, Firecrawl, Slack xoxb-
          PATTERN='sk-[A-Za-z0-9]{20,}|gh[psour]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|firecrawl-[A-Za-z0-9]{20,}|xoxb-[0-9]+-[0-9]+-[A-Za-z0-9]+'
          MATCHES=$(echo "$DIFF" | grep -Eo "$PATTERN" || true)
          if [ -n "$MATCHES" ]; then
            echo "::error::Secret scan failed. Possible secrets in diff:"
            echo "$MATCHES"
            exit 1
          fi

      - name: Check 6 — backlog consistency (Jules only)
        run: |
          set -euo pipefail
          AUTHOR="${{ github.event.pull_request.user.login }}"
          if [[ "$AUTHOR" != "google-labs-jules[bot]" && "$AUTHOR" != "jules-bot" ]]; then
            echo "Not a Jules PR, skipping backlog check"
            exit 0
          fi
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"
          DIFF=$(git diff "$BASE" "$HEAD" -- "00_Meta/concept_backlog.md" || true)
          if [ -z "$DIFF" ]; then
            echo "::error::Jules PR did not touch concept_backlog.md"
            exit 1
          fi
          # Count lines that transitioned from "[ ] pending" (removed) to "[x] done" (added)
          REMOVED_PENDING=$(echo "$DIFF" | grep -c '^-.*\[ \] pending' || true)
          ADDED_DONE=$(echo "$DIFF" | grep -c '^+.*\[x\] done' || true)
          # Filter out diff header lines that start with --- or +++
          if [ "$REMOVED_PENDING" -ne 1 ] || [ "$ADDED_DONE" -ne 1 ]; then
            echo "::error::Backlog consistency check failed: expected exactly 1 pending→done transition (got removed_pending=$REMOVED_PENDING, added_done=$ADDED_DONE)"
            exit 1
          fi
          echo "Backlog check passed: 1 concept transitioned pending→done"

      - name: Approve PR
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh pr review --approve "${{ github.event.pull_request.number }}"

      - name: Enable auto-merge (squash)
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh pr merge --squash --auto "${{ github.event.pull_request.number }}"
````

- [ ] **Step 3: Sanity-check the YAML syntax**

Run:
```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/auto-approve-bots.yml'))"
```
Expected: no output (parse succeeds).

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/auto-approve-bots.yml
git commit -m "$(cat <<'EOF'
feat: add auto-approve workflow for Jules and Claude PRs

Six guardrail checks: path lane, forbidden paths, diff size, frontmatter
validation, secret scan, and Jules-only backlog consistency. PRs that
pass all six are auto-approved and squash-merged. Failures leave the PR
open for manual review.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Write the Jules hourly prompt

**Files:**
- Create: `00_Meta/jules-hourly-prompt.md`

**Why:** This is the prompt the user pastes into Jules's scheduled task config. It must be fully self-contained — Jules sees only this prompt + the current repo state on every hourly run, no prior context.

- [ ] **Step 1: Write the prompt file**

Create `00_Meta/jules-hourly-prompt.md`:
````markdown
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
````

- [ ] **Step 2: Verify the file is well-formed and self-contained**

Run:
```bash
wc -l "00_Meta/jules-hourly-prompt.md"
```
Expected: roughly 200 lines.

Read through the file once. Confirm it does not reference any external context, conversation history, or "the user said" — it should be readable cold.

- [ ] **Step 3: Commit**

```bash
git add "00_Meta/jules-hourly-prompt.md"
git commit -m "$(cat <<'EOF'
feat: add self-contained Jules hourly prompt

Includes hard rules, the per-run workflow (11 steps), the chapter→folder
mapping, the rigid Concept frontmatter contract, and the failure-mode
escape hatch. The user pastes this into Jules's scheduled task config.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 10: Write the discover-finance-sites skill

**Files:**
- Create: `.claude/skills/discover-finance-sites/SKILL.md`
- Create: `.claude/skills/discover-finance-sites/references/firecrawl-search.md`
- Create: `.claude/skills/discover-finance-sites/references/sites-json-schema.md`

**Why:** The user invokes `/discover-finance-sites` to add new finance sources. Claude proposes candidates, the user approves, Claude crawls with Firecrawl, opens a PR. The auto-merge workflow lands the PR in `99_Raw/`. The next Jules run picks up the new content.

- [ ] **Step 1: Create skill directory**

```bash
mkdir -p .claude/skills/discover-finance-sites/references
```

- [ ] **Step 2: Write SKILL.md**

Create `.claude/skills/discover-finance-sites/SKILL.md`:
````markdown
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

Read `sites_100.json` at the repo root. Build a set of:
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
- Domains already in `sites_100.json` (compare normalized hostname).
- Aggregator sites: `reddit.com`, `quora.com`, `youtube.com`, `wikipedia.org`, `medium.com` (tag pages).
- Paywall or login-only sites (heuristic: title contains "Subscribe to read", "Sign in to continue").
- Pure landing pages (no `/blog`, `/articles`, `/resources`, `/learn` paths visible).

### Step 4 — Inspect each candidate

For each remaining candidate (up to 8):
1. Firecrawl-fetch the homepage.
2. Locate an articles/blog/resources index.
3. Summarize what the site covers in 2-3 sentences (topics, depth, format).
4. Estimate overlap with existing sources by comparing topic keywords against existing folder names under `99_Raw/`. Return `Low`, `Medium`, or `High`.
5. Propose `include` paths for the scraper (e.g. `/blog,/resources`) — match what already-similar entries in `sites_100.json` use.

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

### Step 7 — Append to sites_100.json

For each approved site:
1. Build the entry following `references/sites-json-schema.md`.
2. Insert it into `sites_100.json`, preserving the existing JSON formatting style (one entry per line, terminating comma except on the last entry).
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

1. Check `git status` — confirm only `sites_100.json` and files under `99_Raw/<new folder>/` are changed.
2. Create a branch: `claude/discover-<yyyymmdd-hhmm>`.
3. Stage and commit:
   ```bash
   git add sites_100.json 99_Raw/<new folder 1>/ 99_Raw/<new folder 2>/ ...
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

- Never write outside `sites_100.json` and `99_Raw/<new folder>/`.
- Never modify existing files under `99_Raw/`.
- Never approve a site on the user's behalf — always wait for explicit `approve` reply.
- Never run more than 8 crawls in parallel (rate-limit safety).

## References

- `references/firecrawl-search.md` — exact Firecrawl commands for search and crawl.
- `references/sites-json-schema.md` — the shape of a `sites_100.json` entry.
````

- [ ] **Step 3: Write references/firecrawl-search.md**

Create `.claude/skills/discover-finance-sites/references/firecrawl-search.md`:
````markdown
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
````

- [ ] **Step 4: Write references/sites-json-schema.md**

Create `.claude/skills/discover-finance-sites/references/sites-json-schema.md`:
````markdown
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
````

- [ ] **Step 5: Verify the skill files exist**

Run:
```bash
find .claude/skills/discover-finance-sites -type f | sort
```
Expected:
```
.claude/skills/discover-finance-sites/SKILL.md
.claude/skills/discover-finance-sites/references/firecrawl-search.md
.claude/skills/discover-finance-sites/references/sites-json-schema.md
```

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/discover-finance-sites/
git commit -m "$(cat <<'EOF'
feat: add /discover-finance-sites skill

User-invokable skill that searches the web for new finance sources,
presents candidates with overlap analysis, waits for explicit approval,
then crawls approved sites with the existing Firecrawl scraper as
background tasks. Opens a PR adding sites_100.json entries and
99_Raw/<folder>/ content.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: Write the README

**Files:**
- Create: `README.md`

**Why:** The repo currently has no README. Anyone (including future-you) opening this repo cold needs to understand what it is, how the pipeline works, and what manual setup steps remain (branch protection, Jules schedule, bot identity adjustments).

- [ ] **Step 1: Write README.md**

Create `README.md`:
````markdown
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
````

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
docs: add README explaining the vault and pipeline

Covers folder layout, how to read in curriculum vs reference mode, how
Jules and Claude add content, the six guardrail checks, and the
one-time setup steps (branch protection, bot logins, Jules schedule).

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: Final smoke test

**Files:** none created; verifies the pipeline state.

**Why:** Catch any inconsistencies between tasks before declaring the bootstrap done.

- [ ] **Step 1: Run the validator against everything that should validate**

Run from repo root:
```bash
python .github/scripts/validate_frontmatter.py 10_MOCs/*.md
```
Expected: `OK: 8 note(s) validated`

```bash
python .github/scripts/validate_frontmatter.py 90_Sources/*.md 2>&1 || true
```
Expected: validates 0 notes (no real source notes exist yet) — should not error.

- [ ] **Step 2: Confirm forbidden paths are unchanged**

Run:
```bash
git log --oneline --all -- 'sites_100.json' '*.py' '*.sh' '.firecrawl/*' '.github/workflows/*.yml' | head
```

Confirm: only this plan's commits should appear, and only for `.github/workflows/auto-approve-bots.yml` (created in Task 8) — no `.py` or `.sh` files should have been modified.

- [ ] **Step 3: Confirm the structure**

Run:
```bash
ls -d 0[0-9]_*/ 1[0-9]_*/ 2[0-9]_*/ 3[0-9]_*/ 4[0-9]_*/ 5[0-9]_*/ 9[0-9]_*/
```
Expected:
```
00_Meta/
10_MOCs/
20_Concepts/
30_Examples/
40_Formulas/
50_Interview_QA/
90_Sources/
99_Raw/
```

- [ ] **Step 4: Confirm 99_Raw/ is intact**

Run:
```bash
ls 99_Raw/ | wc -l
```
Expected: `20`

- [ ] **Step 5: Run the validator test suite once more**

Run:
```bash
cd .github/scripts && python -m pytest test_validate_frontmatter.py -v
```
Expected: all tests pass.

- [ ] **Step 6: Final commit (no changes — just a checkpoint marker if you want one)**

If everything passes, you're done. Optionally tag this checkpoint:
```bash
git tag -a bootstrap-complete -m "Finance Knowledge Pipeline bootstrap complete"
```

---

## Post-bootstrap manual steps (user does these)

These are NOT part of any task — they're things only the user can do via the GitHub UI or external systems:

1. **Push to GitHub:** `git push origin main` (and `git push --tags` if you tagged).
2. **Enable branch protection on `main`** per the README's "One-time setup" section.
3. **Confirm or update bot logins** in `.github/workflows/auto-approve-bots.yml` once you see the first real PR from Jules and Claude (the placeholders may not match exactly).
4. **Schedule Jules hourly** by pasting `00_Meta/jules-hourly-prompt.md` into a Jules scheduled task pointed at this repo.
5. **Run `/discover-finance-sites` once** in Claude to verify the skill loads and the end-to-end discovery flow works.

---

## Spec coverage check

Cross-reference: every section of `docs/superpowers/specs/2026-04-09-finance-knowledge-pipeline-design.md` is implemented by at least one task in this plan.

| Spec section | Task(s) |
|---|---|
| 3. Vault structure | Tasks 1, 4, 5 |
| 4. Note types and templates | Task 2 |
| 5. Linking model | Implicit in templates (Task 2) and Jules prompt (Task 9) |
| 6. Jules hourly workflow | Tasks 6, 9 |
| 7. Auto-approve PR workflow | Tasks 7, 8 |
| 8. Discovery skill | Task 10 |
| 9. Bootstrap sequence | Tasks 1-12 (this entire plan) |
| 10. Open issues | Documented in README (Task 11) — bot identity placeholders called out |
| 11. Success criteria | Verifiable after Tasks 1-12 complete and the post-bootstrap steps are done |
