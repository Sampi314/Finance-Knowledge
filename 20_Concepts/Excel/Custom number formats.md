---
type: concept
title: Custom number formats
aliases: ["Excel custom number formats"]
tags: ["Excel", "Formatting", "UI"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[ExcelJet - Excel custom number formats - Exceljet]]", "[[Trump Excel - 7 Amazing Excel Custom Number Format Tricks (you Must know)]]"]
status: stub
updated: 2026-04-09
---

# Custom number formats

> **TL;DR.** Custom number formats change how numeric values look in Excel without actually altering the underlying data.

## When you'd use this

You would use custom number formats whenever you need a consistent and professional display of numbers without losing their underlying precision or value. Typical cases involve displaying values in millions or billions, adding text like "units" or "months" next to numbers, dynamically changing font color (e.g. red for negatives), or hiding data from plain view while keeping it in formulas.

## The 30-second version

A custom number format is a special code to control how a value is displayed in Excel. Excel provides a syntax structure divided into up to four sections separated by semicolons: `Positive format ; Negative format ; Zero format ; Text format`. Placeholders like `0` (force insignificant zeros), `#` (display significant digits only), and `?` (align decimals) govern the layout. Applying these codes creates a layer of visual formatting, preventing you from accidentally converting calculation-ready numbers into static text strings.

## The full explanation

### The four-section structure

Excel custom number formats have a specific structure, broken into four parts:

`Positive values ; Negative values ; Zero values ; Text values`

Although a number format can include up to four sections, only one is required. If you only provide one format, Excel uses it for all values. If you provide two sections, the first is used for positive numbers and zeros, while the second is used for negative numbers. To skip a section, include a semicolon in its location but don't specify a format code.

### Key placeholders

- **0 (Zero):** Forces the display of insignificant zeros. E.g., `0.00` makes `5` display as `5.00`.
- **# (Pound sign):** Displays significant digits. Nothing is displayed when a number has fewer digits than `#` symbols. E.g., `#.##` displays `1.1` as `1.1`.
- **? (Question mark):** Aligns digits. Used to maintain visual alignment of decimals.
- **. (Period):** Decimal point placeholder.
- **, (Comma):** Thousands separator, or scales numbers. Using commas at the end of a format scales the number by thousands.

### Escaping characters

Certain characters require escaping to display properly. The backslash `\` is used as the escape character for symbols like `*`, `#`, or `%`. Double quotes `""` allow inserting arbitrary text within the number (e.g., `0.0 "Million"`).

### Conditional formatting in custom numbers

Custom number formats can apply up to two conditions enclosed in brackets `[]`. When conditions are used, they override the standard `Positive;Negative;Zero;Text` structure. For example, `[Red][<100]0;[Blue][>=100]0` will display numbers below 100 in red and numbers 100 or greater in blue.

## Formula

(none)

## Worked example

[[Hiding values and text with custom number formatting]]

## Excel and modeling notes

When building financial models, you often encounter large numbers that are hard to read. A common modeling convention is to display these numbers in millions. By using a custom number format like `0.0,, "M"`, a value of `1200000` visually turns into `1.2 M`. Because the underlying number is still `1200000`, the rest of your model can reference the cell safely without `VALUE!` errors.

## Interview-ready answer

Custom number formats let you alter the visual presentation of numbers, dates, or text without modifying the cell's actual value. They utilize a four-part structure `Positive; Negative; Zero; Text` and allow you to dynamically assign colors or scale values (like displaying in thousands) while preserving the underlying data for calculations.

## Pitfalls and gotchas

- Deleting custom number formats cannot be undone via "Undo".
- Because Excel does "visual rounding" with number formats, what you see isn't always the exact decimal stored in the cell, which can lead to confusion if calculations seem "off" by a decimal point.
- Hardcoded formats in the `TEXT` function require extra escaping of quotes.

## Gaps

- Missing exact formula

## Sources

- [[ExcelJet - Excel custom number formats - Exceljet]]
- [[Trump Excel - 7 Amazing Excel Custom Number Format Tricks (you Must know)]]
