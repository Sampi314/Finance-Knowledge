---
type: example
title: Hiding values and text with custom number formatting
illustrates: ["[[Custom number formats]]"]
updated: 2026-04-09
---

# Hiding values and text with custom number formatting

## Setup

We are creating an Excel dashboard and need to store intermediate calculation values on a sheet, but we don't want the user to see the clutter of these background numbers or any text variables.

## Assumptions

- We have a cell containing the value `50000`.
- We have another cell containing the text `NA`.

## Walk-through

1. We select the cell containing `50000` and open the Format Cells dialog (`Ctrl + 1`).
2. Under the Number tab, we choose "Custom".
3. We type three semicolons `;;;` in the Type field.
4. For the text cell containing `NA`, we type a format that omits the text section: `General; -General; General;`.

## Result

The cell with `50000` appears completely empty on the worksheet, as `;;;` provides an empty format for Positive, Negative, Zero, and Text values. However, selecting the cell shows `50000` in the formula bar, allowing dashboard formulas to still reference it. The cell with `NA` also appears blank because the text format part of `General; -General; General;` is empty.

## What this teaches

- The structure `Positive; Negative; Zero; Text` can be weaponized to hide specific data types.
- Leaving a formatting block blank hides that specific type of data.
- Hiding data with custom formatting preserves the actual cell value for use in calculations, unlike deleting the data.
