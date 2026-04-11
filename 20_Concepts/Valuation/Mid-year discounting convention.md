---
type: concept
title: "Mid-year discounting convention"
aliases: ["Mid-year convention"]
tags: ["valuation", "dcf", "discount-rate"]
difficulty: intermediate
prerequisites: ["[[DCF valuation]]", "[[Free cash flow projection]]", "[[Terminal value]]"]
related: []
sources: ["[[BIWS - Mid-Year Convention DCF and Mid-Year Discounting]]"]
status: draft
updated: 2026-04-11
---

# Mid-year discounting convention

> **TL;DR.** The mid-year convention assumes that a company's cash flows arrive evenly throughout the year, so they are discounted by half a year less than if they arrived strictly at year-end.

## When you'd use this

You use the mid-year convention in almost any standard Discounted Cash Flow (DCF) analysis. It is more accurate than the standard convention for most companies since cash flows are generated continuously, rather than all at once on December 31. It generally boosts the implied valuation slightly since money received earlier has a higher present value. However, you might avoid it for highly seasonal businesses where most cash flow genuinely arrives at the end of the year.

## The 30-second version

A standard DCF calculates present value by discounting cash flows at the end of Year 1, Year 2, and so on, using discount periods of 1.0, 2.0, 3.0, etc. This artificially assumes you get zero cash all year until the stroke of midnight on the last day. The mid-year convention fixes this by assuming cash flows arrive exactly halfway through the year. Instead of 1.0, 2.0, and 3.0, your discount periods become 0.5, 1.5, and 2.5. Because the cash flows are discounted over a shorter time horizon, their present value—and thus the company's valuation—increases.

## The full explanation

In a DCF model, cash flows are typically projected on an annual basis. Standard discounting uses whole numbers for the discount periods: year 1 uses `1.0`, year 2 uses `2.0`, and so forth.

However, a company generates cash flow every day. On average, you can represent this continuous stream by assuming all the year's cash flow arrives exactly halfway through the year.

To implement the mid-year convention, you manually adjust the discount periods in your present value formula:
- Year 1: `0.5`
- Year 2: `1.5`
- Year 3: `2.5`
- Year $n$: $n - 0.5$

### Impact on Terminal Value

The mid-year convention affects your Terminal Value differently depending on the method you use to calculate it:

1. **Exit Multiple Method**: Nothing changes. The terminal multiple is applied to a financial metric (like EBITDA) at the end of the final projected year. The convention doesn't change when that snapshot is taken, so the discount period for the terminal value remains the full year period (e.g., `10.0` for a 10-year DCF).
2. **Gordon Growth (Perpetuity Growth) Method**: You must adjust the discount period. The perpetuity growth method is based on the company's future cash flows. Since the mid-year convention assumes these cash flows arrive halfway through the year, the terminal value itself is implicitly calculated as of the mid-point of the final year. Therefore, you must use a discount period half a year earlier to discount it (e.g., `9.5` instead of `10.0` for a 10-year DCF).

### Stub Periods and Mid-Year Convention

If you are valuing a company partway through the year, you have a **stub period**. For example, if it's April 30, the stub period to December 31 is roughly `0.67` years.

If you combine a stub period with the mid-year convention:
1. **Year 1 (The Stub)**: The cash flow arrives midway between today and the end of the year. The discount period is the stub fraction divided by 2 (e.g., `0.67 / 2 = 0.335`).
2. **Subsequent Years**: For Year 2 onwards, you take the "Normal Discount Period" (which adds the full stub plus full subsequent years) and subtract `0.5`. You do **not** keep dividing by 2. For Year 2, the discount period would be `0.67 + 1.0 - 0.5 = 1.17`. For Year 3, it would be `0.67 + 2.0 - 0.5 = 2.17`.

## Formula

The present value of a cash flow using the mid-year convention is:

$PV = \frac{CF_n}{(1 + r)^{n - 0.5}}$

Where:
- $PV$ = Present Value
- $CF_n$ = Cash Flow in year $n$
- $r$ = Discount rate (WACC)
- $n$ = The projected year (1, 2, 3...)

## Worked example

(none)

## Excel and modeling notes

When building a DCF in Excel, you often use a dedicated "Discount Period" row.
- For the standard convention, you might use an Excel formula like `=YEAR_COLUMN_HEADER - 0` (or just the year number).
- For the mid-year convention, you use `=YEAR_COLUMN_HEADER - 0.5`.
You then use this dedicated row as the exponent in your discount factor calculation `=1 / (1 + WACC)^Discount_Period`. This keeps the model flexible and easy to audit.

## Interview-ready answer

"The mid-year convention is a DCF modeling technique used to account for the fact that a company's cash flows are generated evenly throughout the year, rather than as a single lump sum on December 31st. By assuming the cash arrives midway through the year, we use discount periods of 0.5, 1.5, and 2.5 instead of 1, 2, and 3. This earlier arrival of cash increases its present value, slightly boosting the overall valuation of the company."

## Pitfalls and gotchas

- Applying the mid-year convention to highly seasonal companies (e.g., retailers earning 80% of revenue in December) is inaccurate; you should weight the discount periods towards the end of the year instead.
- Forgetting to adjust the discount period for the Terminal Value when using the Perpetuity Growth method.
- Incorrectly applying the terminal value discount adjustment to the Exit Multiple method.
- When dealing with stub periods, incorrectly dividing the normal discount period by 2 for *all* years, rather than just the first year.

## Sources

- [[BIWS - Mid-Year Convention DCF and Mid-Year Discounting]]
