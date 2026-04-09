---
type: concept
title: "Annuity and perpetuity"
aliases: ["annuities", "perpetuities", "growing annuity", "growing perpetuity"]
tags: ["foundations", "time-value", "discounting", "cash-flows"]
difficulty: beginner
prerequisites: ["[[Time value of money]]", "[[Present value]]", "[[Discount rate]]"]
related: ["[[Future value]]"]
sources: ["[[Damodaran - The Mechanics of Time Value]]"]
status: draft
updated: 2026-04-09
---

# Annuity and perpetuity

> **TL;DR.** An annuity is a constant cash flow paid or received at regular intervals for a fixed period of time, whereas a perpetuity is a constant cash flow that continues forever.

## When you'd use this

You use annuity formulas to calculate the present or future value of fixed, repeating payments like mortgages, auto loans, or regular savings contributions. Perpetuity formulas are most often used in valuation, specifically to estimate the terminal value of a company or an asset that is expected to generate cash flows indefinitely.

## The 30-second version

Both annuities and perpetuities deal with streams of cash flows. An **annuity** has a set end date—for example, $100 paid at the end of each year for four years. Its present value depends on the payment amount, the interest (discount) rate, and the number of periods. A **perpetuity** has no end date—it's an endless stream of constant payments. Its present value is simply the cash flow divided by the discount rate. Both can also have a "growing" variant, where the cash flows increase at a constant growth rate each period.

## The full explanation

When discounting or compounding streams of cash flows, doing it individually for each payment can be tedious. Annuities and perpetuities provide mathematical shortcuts.

### Annuities

An annuity is a constant cash flow that occurs at regular intervals for a fixed period. There are two main types depending on when the cash flow occurs:
- **End-of-period annuities (Ordinary Annuities):** The cash flow occurs at the end of each period. This is standard for most loans and bonds.
- **Beginning-of-period annuities (Annuities Due):** The cash flow occurs at the beginning of each period, like rent or lease payments. The present value of a beginning-of-the-period annuity will be higher than an equivalent end-of-period annuity because every cash flow is discounted for one less period.

### Perpetuities

A perpetuity is simply an annuity that lasts forever. The most common example of a perpetuity is a preferred stock that pays a fixed dividend indefinitely. Because the cash flows continue forever, you don't need a number of periods ($n$) to find the present value.

### Growing variants

- **Growing Annuity:** A cash flow stream that grows at a constant rate for a specified period of time. This is useful for forecasting cash flows that are expected to increase with inflation or company growth over a set forecast period.
- **Growing Perpetuity:** A cash flow stream that is expected to grow at a constant rate forever. This is heavily used in the Gordon Growth Model to calculate terminal value. The growth rate ($g$) must be less than the discount rate ($r$) for the formula to work mathematically.

## Formula

The present value (PV) formulas are:

- **Perpetuity:** $PV = \frac{A}{r}$
- **Growing Perpetuity:** $PV = \frac{CF_1}{r - g}$

Where $A$ is the constant annuity payment, $CF_1$ is the expected cash flow next year, $r$ is the discount rate, and $g$ is the constant growth rate.

*(Note: There are also standard formulas for the PV and Future Value of regular and growing annuities, which are built into Excel.)*

## Worked example

(none)

## Excel and modeling notes

In Excel, you rarely calculate the PV of a regular annuity manually. Instead, use the built-in functions:
- `=PV(rate, nper, pmt, [fv], [type])` to find the present value of an annuity.
- `=PMT(rate, nper, pv, [fv], [type])` to find the annuity payment itself (e.g., a loan payment).

Set the `[type]` argument to 0 (or omit it) for end-of-period cash flows, and 1 for beginning-of-period cash flows.

For perpetuities, you must calculate them manually using the formula `=CF / (r - g)` since Excel has no infinite period functions.

## Interview-ready answer

An annuity is a stream of constant cash flows for a fixed number of periods, like a car loan, while a perpetuity is a stream of constant cash flows that lasts forever. In finance, we use the growing perpetuity formula extensively to calculate a company's terminal value at the end of our discrete projection period in a DCF model.

## Pitfalls and gotchas

- Applying the growing perpetuity formula when the growth rate ($g$) is greater than or equal to the discount rate ($r$). This will result in a negative or undefined present value. In reality, no company can grow faster than the economy forever.
- Forgetting to adjust for the timing of cash flows. Ensure you know whether payments occur at the beginning or the end of the period, as this significantly impacts the present and future values.
- Assuming the growth rate in a growing annuity can't exceed the discount rate. Unlike a perpetuity, the PV of a growing annuity can still be calculated (using a different formula) even if $g = r$ or $g > r$, because the time period is finite.

## Sources

- [[Damodaran - The Mechanics of Time Value]]
