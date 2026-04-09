---
type: concept
title: Time value of money
aliases: []
tags: [foundations]
difficulty: beginner
prerequisites: []
related: ["[[Present value]]", "[[Future value]]", "[[Discount rate]]"]
sources: ["[[BIWS - The Time Value of Money Excel Calculations and Real-Life Examples]]"]
status: draft
updated: 2026-04-09
---

# Time value of money

> **TL;DR.** The time value of money means that money today is worth more than money tomorrow because you could invest it today and earn a return on it in the future.

## When you'd use this

The time value of money is the fundamental principle behind nearly all financial analysis and valuation. You use it whenever you need to evaluate an investment, decide between different payment options over time, or determine what a company or asset is worth today based on the cash flow it is expected to generate in the future.

## The 30-second version

If you have $100 today, it is worth more than receiving $100 a year from now. This is because you could take that $100 today, invest it, and have $105 or $110 in a year. The core reason future cash flow is less valuable is not just inflation, but the opportunity cost of not having the money to invest today. Therefore, any future cash flow must be discounted back to its present value to accurately compare it to money you hold right now.

## The full explanation

The time value of money is critical in valuation because it serves as the foundation behind concepts like Present Value and Net Present Value, which dictate how much assets and companies are worth.

To properly value an asset, you have to discount its future cash flows to their present value. This discounting is based on your opportunity cost—the return you could earn if you invested that same money today in other, similar opportunities.

A common misconception is that future cash flow is less valuable solely because of inflation. While it's true that inflation erodes purchasing power, making uninvested money less valuable over time, the real reason future cash flow is worth less than money today is the opportunity cost associated with the time value of money.

When comparing investments or payment structures (such as paying a large upfront deposit versus paying ongoing rent), you cannot simply look at the absolute dollars paid and received. Instead, you must account for what you could have earned by investing the money that was paid upfront. The lost earnings on that capital must be factored into the true cost of the decision. Furthermore, when comparing potential returns, it's essential to compare similar types of assets with comparable risk profiles (e.g., comparing real estate to real estate, rather than real estate to government bonds).

## Formula

(none)

## Worked example

[[South Korea apartment rental options]]

## Excel and modeling notes

When evaluating cash flows that are re-invested over a holding period, the time value of money dictates that those cash flows become more valuable by the end of the period. To accurately reflect different re-investment rates in Excel, you might use the `MIRR` (Modified Internal Rate of Return) function rather than `IRR` or `XIRR`. `MIRR` allows you to assume a different rate of return for the re-invested proceeds.

## Interview-ready answer

The time value of money dictates that a dollar today is worth more than a dollar tomorrow because of its potential earning capacity. You could invest the dollar today and earn a return, so any future cash flows must be discounted back to their present value based on your opportunity cost to determine what an asset or company is truly worth today.

## Pitfalls and gotchas

- Failing to recognize opportunity cost: Assuming that getting your money back in the future means you haven't "lost" anything, while ignoring what you could have earned by investing that money in the meantime.
- Blaming only inflation: Believing that future cash flows are less valuable merely because of inflation, rather than the core concept of the time value of money and opportunity cost.
- Comparing apples and oranges: Trying to compare the potential returns of a high-risk investment (like real estate or stocks) directly to a low-risk investment (like government bonds) without adjusting for the different risk profiles and opportunity costs.

## Sources

- [[BIWS - The Time Value of Money Excel Calculations and Real-Life Examples]]
