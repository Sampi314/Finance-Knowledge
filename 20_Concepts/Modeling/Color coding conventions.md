---
type: concept
title: "Color coding conventions"
aliases: ["excel color coding", "financial modeling colors"]
tags: ["financial-modeling", "excel", "best-practices"]
difficulty: beginner
prerequisites: []
related: ["[[Three-statement model]]", "[[Model checks and balances]]"]
sources: ["[[BIWS - How to Color Code in Excel - Shortcuts for Formulas, Constants & Inputs]]", "[[Macabacus - Improving Financial Modeling Readability with Color Formatting Codes]]", "[[Financial Modeling NYC - Clean Financial Model Architecture- How to Build Break-Proof Excel Models for Investment Banking]]"]
status: draft
updated: 2026-04-13
---

# Color coding conventions

> **TL;DR.** Standardized font colors in financial models instantly communicate the nature of a cell, differentiating hard-coded inputs from formulas and external links.

## When you'd use this

You apply these conventions anytime you are building or auditing a financial model. Consistent color coding allows users to quickly navigate complex spreadsheets and understand what can be safely changed versus what is driven by calculations.

## The 30-second version

In professional financial modeling, font colors convey meaning. The universal standard dictates that hard-coded inputs (constants) are colored blue, formulas on the same sheet are black, and links to other worksheets are green. Links to external files are typically red. This visual separation prevents users from accidentally overwriting critical formulas and speeds up the audit process.

## The full explanation

Visual cues are essential for instantly diagnosing errors and navigating financial models. Adhering to industry-standard color coding is a fundamental best practice that improves readability and reduces risk.

The core conventions are:
- **Blue:** Hard-coded inputs or constants. These are the only cells a user should ever modify.
- **Black:** Formulas that reference cells within the same worksheet.
- **Green:** Links or formulas that reference cells on a different worksheet within the same workbook.
- **Red:** Links referencing an entirely separate, external Excel file (which should generally be avoided).

Using these colors uniformly across all model tabs builds familiarity and transparency, ensuring the model's architecture is clean and understandable.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

To quickly apply color formatting in Excel, you can use shortcuts to select specific cell types. For example, pressing `F5` (Go To), then `Alt + S, O, X` selects all numerical constants, allowing you to quickly change their font color to blue. Similarly, `F5, Alt + S, F, X` selects numerical formulas.

## Interview-ready answer

In financial modeling, color coding is critical for clarity and error prevention. The standard practice is to use blue font for hard-coded inputs, black for formulas on the same sheet, and green for links to other worksheets. This allows anyone opening the model to instantly know which cells they can safely change without breaking the underlying calculations.

## Pitfalls and gotchas

- **Inconsistency:** Failing to apply the colors universally across all sheets confuses users and negates the benefits of the system.
- **Poor Contrast:** Using low-contrast combinations, such as dark blue or purple against black, makes the model hard to read and strains the eyes.

## Sources

- [[BIWS - How to Color Code in Excel - Shortcuts for Formulas, Constants & Inputs]]
- [[Macabacus - Improving Financial Modeling Readability with Color Formatting Codes]]
- [[Financial Modeling NYC - Clean Financial Model Architecture- How to Build Break-Proof Excel Models for Investment Banking]]
