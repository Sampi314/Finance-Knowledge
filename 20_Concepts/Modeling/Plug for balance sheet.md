---
type: concept
title: "Plug for balance sheet"
aliases: ["plugs", "plug"]
tags: ["modeling", "balance-sheet", "audit"]
difficulty: intermediate
prerequisites: ["[[Model checks and balances]]", "[[The balance sheet]]"]
related: ["[[Iterative calculations in Excel]]"]
sources: ["[[Sumproduct - Spotting Inconsistencies and Plugs]]"]
status: draft
updated: 2026-04-13
---

# Plug for balance sheet

> **TL;DR.** A "plug" is a hard-coded number or one-off formula used to force a model, such as a balance sheet, to balance, which often indicates errors or a lack of consistency.

## When you'd use this

You would ideally *not* use a plug when building a financial model, as it obscures errors and inconsistencies. However, as an end user or auditor reviewing someone else's model, you would look for plugs to determine if the calculations are consistent or if balancing formulae have been improperly used to artificially force the balance sheet to balance.

## The 30-second version

In financial modeling, a "plug" refers to an arbitrary number or a one-off formula inserted into a model, typically to make the balance sheet balance. This practice is frowned upon because a well-built three-statement model should balance naturally through correct linkages. If a block of calculations has inconsistent formulae, it can lead to mistrust of the model.

## The full explanation

When reviewing financials and undertaking ratio analysis, you might discover that some formulae have been replaced with hard-coded numbers to force the Balance Sheet to balance. These "plugs" make it difficult to determine if calculations are consistent.

A best practice in financial modeling is that formulae should be consistent; ideally, using only one unique formula across a row or in a block of calculations. End users often view "one-off" formulae as plugs, leading to a mistrust of the model. Using fewer unique formulae makes models more trustworthy, easier to understand, and quicker to review or audit.

Identifying plugs visually can be difficult, but Excel provides tools like the **ISFORMULA** function in conditional formatting, or the 'Go To Special' dialog box (**CTRL+G** or **F5** > **Special** > **Constants** or **Formulas**) to quickly locate cells with hard-coded values or inconsistent formulae.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

To locate plugs or rogue formulae in an Excel model, you can use the 'Go To' dialog box (**CTRL+G** or **F5**). Click the 'Special...' button in the bottom left corner. From there, you can select 'Constants' to find hard-coded plugs, or use the 'Formulas' options to filter the types of formulae. Alternatively, the shortcut **CTRL+\`** toggles cell values with their formulae, and selecting data followed by **CTRL+\\** selects cells whose contents differ from the comparison cell in each row.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Using plugs leads to a mistrust of the model by end users and reviewers.
- Replacing formulae with hard-coded numbers obscures the underlying mechanics and hides actual errors in the model's linkages.

## Sources

- [[Sumproduct - Spotting Inconsistencies and Plugs]]
