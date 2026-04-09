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
