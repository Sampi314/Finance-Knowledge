---
type: concept
title: "Compound interest"
aliases: ["Compounding", "Interest on interest"]
tags: ["foundations", "finance", "time-value-of-money"]
difficulty: beginner
prerequisites: ["[[Time value of money]]", "[[Present value]]"]
related: ["[[Future value]]", "[[Discount rate]]"]
sources: ["[[Wall Street Prep - Compound Interest]]", "[[ExcelJet - Calculate compound interest]]"]
status: draft
updated: 2026-04-09
---

# Compound interest

> **TL;DR.** Compound interest is the process of earning interest not only on your original investment but also on the accumulated interest from prior periods.

## When you'd use this

You will use this concept practically everywhere in finance. Whenever an investment grows over multiple periods, or whenever you borrow money and the debt balance increases over time, compounding is at work. It is essential for calculating the future value of a deposit, determining loan balances, and understanding how an investment's value balloons over a long time horizon.

## The 30-second version

Compound interest means you earn "interest on interest." Unlike simple interest, which only pays out based on your initial deposit (the principal), compounding takes the interest you earned in the first period, adds it to the principal, and then calculates the next period's interest on that new, larger total. Because the base grows over time, your money grows exponentially. This creates a "snowball effect" that is especially powerful over long time horizons or with more frequent compounding periods (like daily or monthly instead of annually).

## The full explanation

In finance, compound interest is a central part of how money grows over time. It is driven by two main components:

1.  **Original Principal:** The initial amount invested, lent, or borrowed.
2.  **Accumulated Interest:** The interest generated from earlier periods.

### The compounding cycle

At the end of a compounding period, the accumulated interest is added directly to the principal amount. In the next period, interest is calculated on this newly increased balance. This continuous cycle means that even a modest, seemingly low interest rate can cause the principal to grow substantially over a very long time horizon.

### The effect of compounding frequency

The speed at which the compounding effect accumulates depends heavily on the compounding frequency. This frequency defines how often the interest is calculated and added to the balance. Common compounding periods include:

-   **Annual Compounding:** Interest is calculated and added once a year.
-   **Semi-Annual Compounding:** Twice a year (the annual rate is divided by 2).
-   **Quarterly Compounding:** Four times a year (the annual rate is divided by 4).
-   **Monthly Compounding:** Twelve times a year (the annual rate is divided by 12).
-   **Daily Compounding:** Every day (the annual rate is divided by 365).

The greater the number of compounding periods in a year, the greater the compounding effect. For example, a $100,000 investment at 5% for 10 years will yield more total interest if it is compounded daily compared to if it is compounded annually.

## Formula

![[Future value formula]]

## Worked example

[[Future value of a $100,000 deposit]]

## Excel and modeling notes

In Excel, the most common way to calculate the effects of compound interest over a standard number of periods is to use the `FV` (Future Value) function.

The syntax is `=FV(rate, nper, pmt, [pv], [type])`.

-   **rate:** The interest rate per compounding period. For example, if you have a 5% annual rate compounding monthly, the `rate` would be `5% / 12`.
-   **nper:** The total number of periods. For a 10-year investment compounding monthly, `nper` would be `10 * 12 = 120`.
-   **pmt:** The payment made each period (use `0` if there are no periodic additions).
-   **pv:** The present value or initial investment. By convention, this is usually input as a negative number because it represents cash leaving your wallet for the investment.

For instance, `=FV(0.05/12, 10*12, 0, -100000)` will calculate the future value of a $100,000 deposit over 10 years at a 5% annual interest rate, compounded monthly.

## Interview-ready answer

[[Compound vs simple interest]]

## Pitfalls and gotchas

-   **Confusing the annual rate with the period rate:** If compounding is semi-annual, quarterly, or monthly, you must divide the annual interest rate by the number of compounding periods in a year.
-   **Forgetting to adjust `nper`:** Just as you adjust the rate, you must multiply the number of years by the number of periods per year to get the total number of compounding periods.
-   **Excel sign conventions:** Remember that the `FV` function typically expects the `pv` (Present Value) to be negative, as it represents a cash outflow (an investment). If you enter a positive `pv`, the resulting future value will be negative.

## Sources

- [[Wall Street Prep - Compound Interest]]
- [[ExcelJet - Calculate compound interest]]
