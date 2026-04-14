---
type: concept
title: IRR
aliases: ["Internal Rate of Return"]
tags: ["lbo", "valuation", "modeling"]
difficulty: intermediate
prerequisites: ["[[Time value of money]]", "[[Present value]]", "[[Discount rate]]"]
related: ["[[Sponsor returns]]"]
sources: ["[[A Simple Model - Everything IRR - A Simple Model]]", "[[A Simple Model - The IRR Formula Explained - A Simple Model]]", "[[A Simple Model - Excel- =XIRR vs =IRR - A Simple Model]]", "[[A Simple Model - Excel- =IRR() vs. =XIRR() (continued...) - A Simple Model]]", "[[A Simple Model - Determine the Proceeds Required to Achieve a Specific IRR - A Simple Model]]", "[[Sumproduct - Irreverent IRR]]"]
status: draft
updated: 2026-04-14
---

# IRR

> **TL;DR.** The Internal Rate of Return (IRR) is the discount rate that makes the Net Present Value (NPV) of all future cash flows from a project equal to zero.

## When you'd use this

You use IRR to evaluate the profitability of potential investments, compare different projects, and measure the annualized effective compounded return rate of a private equity investment or LBO. It is the key performance metric published by private equity firms.

## The 30-second version

If an investment achieves an IRR of 20%, it means the investment grew at an annualized rate of 20% each year. It's the rate `r` at which the present value of future cash inflows equals the initial investment (cash outflow). For example, if you invest $10 today and receive $17.28 in three years, the IRR is 20% because $10 * (1+0.20)^3 = $17.28.

## The full explanation

The IRR is the annualized effective compounded return rate. It measures the rate at which an investment grows over time.

### Calculating the Proceeds
If you know the IRR hurdle rate and the time horizon, you can calculate the required exit proceeds. The investment grows by the IRR each year. If you invest X dollars for 5 years at an IRR of 20%, the proceeds required are `X * (1 + 20%)^5`. In Excel, adjusting for exact dates, the formula is `Proceeds = Investment * (1 + IRR)^YEARFRAC(date1, date2)`.

### Excel: =IRR vs =XIRR
In Excel, `=IRR` expects equal time periods between cash flows and returns the rate of return per period. The `=XIRR` formula is designed for incongruous time periods and returns an annualized IRR, adjusting for exact days between cash flows using a 365-day year. Using `=IRR` for unequally spaced cash flows will yield incorrect results. A common discrepancy arises in leap years, as `=XIRR` accounts for the extra day.

## Formula

![[Internal Rate of Return]]

## Worked example

If you invest $10 in period zero and three years later receive $17.28, the formula is:
$10 * (1 + r)^3 = $17.28
(1 + r)^3 = 1.728
1 + r = 1.20
r = 20%

## Excel and modeling notes

- `=IRR(values, [guess])` assumes regular periodic cash flows and ignores blank cells. To calculate correctly with gaps, use zeroes.
- `=XIRR(values, dates, [guess])` requires a non-zero first cash flow (often negative) and dates to be numerical (not text). It calculates an annualized rate.
- `XIRR` can sometimes fail to calculate and return `2.98E-09` instead of an error, often due to formatting or convergence issues. A common workaround is to provide a better guess, or use a very small negative number (e.g., -0.000001) for the initial cash flow.
- When business-critical accuracy is needed, setting up the NPV manually and using `Goal Seek` to find the rate that makes NPV zero is more reliable than `=XIRR`.

## Interview-ready answer

The Internal Rate of Return is the discount rate that makes the net present value of a series of cash flows equal to zero. It represents the annualized compounded return of an investment.

## Pitfalls and gotchas

- **Multiple IRRs:** When cash flows change signs more than once (e.g., negative, positive, negative), there can be multiple solutions for the IRR.
- **Excel `=XIRR` errors:** `=XIRR` can return `2.98E-09` instead of a proper error when it fails to converge; it also truncates dates to midnight, which can cause slight inaccuracies compared to manual NPV calculations.
- **Periodicity:** Using `=IRR` for non-periodic cash flows or forgetting to annualize the output if the periods are monthly or quarterly will result in an incorrect annual return.

## Sources

- [[A Simple Model - Everything IRR - A Simple Model]]
- [[A Simple Model - The IRR Formula Explained - A Simple Model]]
- [[A Simple Model - Excel- =XIRR vs =IRR - A Simple Model]]
- [[A Simple Model - Excel- =IRR() vs. =XIRR() (continued...) - A Simple Model]]
- [[A Simple Model - Determine the Proceeds Required to Achieve a Specific IRR - A Simple Model]]
- [[Sumproduct - Irreverent IRR]]
