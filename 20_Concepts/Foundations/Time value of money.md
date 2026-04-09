---
type: concept
title: Time value of money
aliases: [TVM, Time Value of Money]
tags: [foundations, valuation, present-value]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[BIWS - The Time Value of Money: Excel Calculations and Real-Life Examples]]", "[[CFI - Discounting]]", "[[Wall Street Prep - Discount Factor (DCF)]]"]
status: draft
updated: 2026-04-09
---

# Time value of money

> **TL;DR.** Money today is worth more than the same amount of money tomorrow because you could invest it today and earn a return on it in the future.

## When you'd use this

The time value of money (TVM) is the foundational concept behind almost all of finance and valuation. You use it whenever you need to compare cash flows occurring at different points in time, such as calculating the present value of an investment, determining the return on a project, valuing a company using a Discounted Cash Flow (DCF) model, or evaluating the cost-benefit trade-offs of financing options (like paying a larger upfront deposit versus paying ongoing rent).

## The 30-second version

If someone offers you $100 today or $100 in a year, you should take the $100 today. Why? Because if you take it today, you can invest it (for instance, in a savings account or a bond) and earn interest. By the end of the year, you'll have your original $100 plus the interest earned (e.g., $105). Therefore, future cash flow is inherently less valuable than cash flow today, due to this "opportunity cost" of not having the money to invest in the meantime. To make fair comparisons between cash flows across different time periods, we "discount" future values back to their present value using a discount rate.

## The full explanation

The time value of money argues that a dollar today is worth more than a dollar tomorrow. Many people mistakenly believe this is solely due to inflation reducing the purchasing power of money over time. While inflation does play a role in making uninvested cash less valuable, the *real* reason behind TVM is the **opportunity cost**.

When you do not have the cash in hand today, you forfeit the ability to invest it and earn a return. This forgone return is your opportunity cost. In corporate finance and investment analysis, you must discount future cash flows to their Present Value based on this opportunity cost—that is, what you would earn if you invested the money in other, similar opportunities with similar risk.

Because of the time value of money, you cannot simply add up cash flows from different years. To compare an investment that pays $100 annually for 10 years, the $100 received in Year 10 is worth significantly less *today* than the $100 received in Year 1. A discount factor (driven by the discount rate) is applied to each future period to compute its Present Value.

### Applications in Valuation
This principle is widely used in models like the Discounted Cash Flow (DCF) model and the Dividend Discount Model (DDM). The assumption is that cash flows generated during the holding period can be reinvested at a specific rate of return. The time value of money also directly influences calculations for bond yields, the yield to maturity, and leveraged buyout (LBO) returns.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling the time value of money in Excel, analysts often use discount factors to scale down future cash flows. A discount factor can be calculated as `1 / (1 + Discount Rate) ^ Period Number`. Multiplying the future cash flow by this factor gives the present value. Excel also has built-in functions like `PV` (Present Value), `NPV` (Net Present Value), and `IRR` (Internal Rate of Return) to streamline these calculations.

## Interview-ready answer

[[Why is money today worth more than money tomorrow?]]

## Pitfalls and gotchas

- **Confusing TVM with inflation:** While inflation decreases purchasing power, TVM is fundamentally about the opportunity cost of capital (what you could have earned by investing the money).
- **Using an inappropriate discount rate:** Comparing cash flows accurately requires a discount rate that reflects similar risks. You should not use the risk-free rate of U.S. Treasuries to discount the cash flows of a high-risk start-up.
- **Ignoring the timing of cash flows:** Adding nominal (undiscounted) cash flows across different years without adjusting for TVM gives an inaccurate picture of an investment's true value.

## Sources

- [[BIWS - The Time Value of Money: Excel Calculations and Real-Life Examples]]
- [[CFI - Discounting]]
- [[Wall Street Prep - Discount Factor (DCF)]]
