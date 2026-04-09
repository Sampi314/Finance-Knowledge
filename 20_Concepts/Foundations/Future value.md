---
type: concept
title: "Future value"
aliases: ["FV"]
tags: ["foundations", "time-value-of-money"]
difficulty: beginner
prerequisites: ["[[Present value]]", "[[Time value of money]]"]
related: ["[[Compound interest]]", "[[Discount rate]]"]
sources: ["[[Wall Street Prep - Compound Interest]]", "[[Wall Street Prep - Discount Rate]]", "[[ExcelJet - Excel FV function]]"]
status: draft
updated: 2026-04-09
---

# Future value

> **TL;DR.** Future value (FV) is the value of a current asset at a specified date in the future based on an assumed rate of growth.

## When you'd use this

You use future value calculations when evaluating investments, savings plans, or any financial instrument where money grows over time due to interest. It helps answer questions like "How much will my $10,000 deposit be worth in 10 years if it earns 5% interest annually?" It is the reverse process of calculating present value, which discounts future cash flows back to today.

## The 30-second version

Future value represents the amount of money an initial investment will grow to over a specific period, assuming a certain interest rate. Due to the time value of money, a dollar today is worth more than a dollar tomorrow because it can be invested to earn interest. Future value calculations quantify exactly how much more it will be worth. The calculation depends heavily on two key factors: the interest rate and the compounding frequency (how often interest is added to the principal balance).

## The full explanation

### The role of compounding
Future value is driven by the concept of compound interest—meaning you earn interest not just on your initial principal deposit, but also on the accrued interest from prior periods. This is in contrast to simple interest, which is calculated strictly on the original principal.

Because interest compounds over time, the future value of an investment grows exponentially rather than linearly.

### Compounding frequency
The future value formula must account for how often interest is compounded. Common compounding periods include:
- **Annual:** 1x per year
- **Semi-Annual:** 2x per year
- **Quarterly:** 4x per year
- **Monthly:** 12x per year
- **Daily:** 365x per year

The more frequently interest is compounded, the higher the resulting future value, because the interest earned in each period starts earning its own interest sooner.

### Relationship with present value and discount rate
Future value is intrinsically linked to present value (PV) and the discount rate. While discounting brings future cash flows back to their present value, compounding projects present cash flows forward to their future value. If you subtract the present value from the future value, you isolate the total impact of compound interest earned over the period.

## Formula

![[Future value formula]]

## Worked example

[[Future value of a $100,000 deposit]]

## Excel and modeling notes

In Excel, future value is calculated using the built-in `FV` function:

`=FV(rate, nper, pmt, [pv], [type])`

- **rate:** The interest rate per period (ensure this aligns with the compounding frequency, e.g., an annual rate of 12% with monthly compounding means `rate` should be 12% / 12 = 1%).
- **nper:** The total number of payment or compounding periods (e.g., 4 years with monthly payments is 4 * 12 = 48).
- **pmt:** The payment made each period. Must be entered as a negative number for cash outflows.
- **pv:** (Optional) The present value, or lump sum investment amount. Entered as a negative number.
- **type:** (Optional) 0 if payments are at the end of the period (default), 1 if at the beginning.

## Interview-ready answer

Future value measures how much a present sum of money will grow to over a given time frame at a specified interest rate. It incorporates the effects of compounding, where interest is earned on both the initial principal and previously accumulated interest, which means higher compounding frequencies yield higher future values.

## Pitfalls and gotchas

- **Mismatched periods and rates:** The most common error in FV calculations is failing to match the interest rate and the number of periods to the compounding frequency (e.g., using an annual rate with monthly periods).
- **Sign conventions in Excel:** When using Excel's `FV` function, remember that cash outflows (like an initial deposit or regular payments) must be entered as negative numbers to get a positive future value result.

## Sources

- [[Wall Street Prep - Compound Interest]]
- [[Wall Street Prep - Discount Rate]]
- [[ExcelJet - Excel FV function]]
