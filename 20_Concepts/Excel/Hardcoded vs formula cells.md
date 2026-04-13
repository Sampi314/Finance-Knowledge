---
type: concept
title: "Hardcoded vs formula cells"
aliases: []
tags: ["excel", "modeling-conventions", "audit"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Chandoo - How to check for hard-coded values in Excel formulas- » Chandoo.org - Learn Excel, Power BI & Charting Online]]", "[[CFI - Model Audit - Overview, Scope and Purpose, Categories]]"]
status: draft
updated: 2026-04-13
---

# Hardcoded vs formula cells

> **TL;DR.** In financial modeling, hardcoded cells contain static, directly typed numbers, while formula cells calculate values dynamically; these two types must be visually distinct to prevent errors.

## When you'd use this

You apply this distinction whenever building or auditing a financial model. Differentiating between hardcoded inputs (constants) and formulas allows users to easily see which variables can be changed for scenario analysis and which numbers are calculated results.

## The 30-second version

A best practice in financial modeling is to use different font colors for different types of cells. Hardcoded numbers—those you type in directly, like a tax rate or historical revenue—should be formatted in a blue font. Formulas and calculations should be formatted in a black font. Ignoring this convention or applying it inconsistently can lead to substantial errors because users might overwrite a formula thinking it's an input, or fail to update a static assumption.

## The full explanation

Financial models are complex tools meant to project future performance based on a set of assumptions. The integrity of the model depends on the user's ability to identify inputs versus outputs.

### Best Practices for Formatting
The industry standard is to use a blue font for hardcoded numbers. These are your assumptions and historical inputs. Black font is used exclusively for formulas, referencing, and calculations. Some models also use a green font to denote a link to a different worksheet within the same workbook.

### Auditing for Hardcoded Values
Auditing a model often involves checking for hardcoded values inappropriately hidden inside formulas. A formula like `=SUM(A1:A5) + 50` contains a hidden constant (`50`). These are dangerous because they are not visible on the face of the spreadsheet and are easily forgotten when updating the model, leading to calculation errors. Advanced users often rely on custom VBA scripts to scan a workbook and highlight any formula that contains hardcoded constants.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When auditing a complex spreadsheet, standard Excel features like "Show Formulas" or "Go To Special > Constants" might not be sufficient to find hardcoded values *within* formulas. Creating a custom VBA User Defined Function (UDF) can help detect cells that contain formulas with embedded constants.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Inconsistently formatting cells can lead to substantial errors when users mistakenly overwrite a formula or fail to update an input.
- Embedding hardcoded numbers inside formulas (e.g., `=A1*1.05`) makes the model difficult to update and audit; inputs should always be separated into their own dedicated assumption cells.

## Sources

- [[Chandoo - How to check for hard-coded values in Excel formulas- » Chandoo.org - Learn Excel, Power BI & Charting Online]]
- [[CFI - Model Audit - Overview, Scope and Purpose, Categories]]
