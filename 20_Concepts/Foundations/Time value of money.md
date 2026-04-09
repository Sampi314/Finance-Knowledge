---
type: concept
title: Time value of money
aliases: [TVM, Time Value of Money]
tags: [foundations, valuation, present-value, future-value]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[BIWS - The Time Value of Money: Excel Calculations and Real-Life Examples]]", "[[Wall Street Prep - DCF Interview Questions | Intrinsic Value Concepts]]", "[[Pivotal180 - What Ohtani’s Contract can Teach us About Discount Rates]]", "[[Pivotal180 - Glossary of Terms for Project Finance Training]]", "[[A Simple Model - Discounted Cash Flow Model Overview | A Simple Model]]"]
status: draft
updated: 2026-04-09
---

# Time value of money

> **TL;DR.** The time value of money states that a dollar today is worth more than a dollar tomorrow because it can be invested to earn a return.

## When you'd use this

The time value of money (TVM) is the foundational concept behind all of modern valuation and project finance. You will use it whenever you need to compare cash flows that occur at different points in time, such as when building a Discounted Cash Flow (DCF) model, pricing a bond, sizing a project finance loan, or deciding between taking a lump-sum payment versus an annuity.

## The 30-second version

If you have $100 today, it is worth more than $100 received a year from now. This is because you could invest that $100 today and earn interest (or a return) on it, ending up with, say, $105 in a year. Conversely, if someone offers you $100 a year from now, you would only be willing to pay something less than $100 for it today.

While inflation does erode the purchasing power of money over time, the real reason future cash flows are worth less today is **opportunity cost**—the lost opportunity to earn a return on that capital in the meantime. To make apples-to-apples comparisons of cash flows across different years, finance professionals use a discount rate (which reflects this opportunity cost) to calculate the Present Value (PV) of future cash flows.

## The full explanation

The time value of money is a core principle in finance that bridges the gap between present value and future value. It relies heavily on the concept of **opportunity cost**. When you commit capital to an investment or lock it up in a deferred payment, you are giving up the opportunity to invest that money elsewhere.

### The Role of the Discount Rate
To equate a future dollar to a present dollar, you must discount the future dollar using a discount rate. The discount rate represents the expected return on investment (or hurdle rate) for an investment of similar risk.
- A **higher discount rate** makes future cash flows less valuable today because it implies a higher opportunity cost or higher risk.
- A **lower discount rate** makes future cash flows more valuable today.

### Application in Corporate Valuation
In corporate valuation, particularly in a DCF model, the time value of money dictates that the cash flows a company generates in the near term are worth significantly more to an investor than those generated 10 or 20 years in the future. The Weighted Average Cost of Capital (WACC) is typically used as the discount rate to bring all projected Free Cash Flows (FCFF) back to their present value.

### Application in Project Finance
In project finance, TVM is used to size and sculpt non-recourse project loans. A project can only borrow an amount today equal to the present value of the future cash flows it will use to pay debt service, discounted at the interest rate of the loan.

### Extreme Deferrals and Present Value
A striking real-world example of TVM is Shohei Ohtani's baseball contract. Nominally valued at $700 million over 10 years, the vast majority of the payments are deferred for a decade. When discounted back to today's dollars at an appropriate rate, the actual present value of the contract is substantially lower than $700 million.

## Formula

![[Future Value]]

![[Present Value]]

## Worked example

Imagine you are valuing an asset that will generate exactly $100 of cash flow each year for 10 years.
If your opportunity cost (discount rate) is 5%, the $100 received in Year 1 is worth $95.24 today.
However, the $100 received in Year 10 is worth much less because of the time value of money:
$100 / (1 + 0.05)^10 = $61.39.

If the discount rate were higher, say 10%, that Year 10 cash flow would be worth only $38.55 today. This highlights why near-term cash flows carry the most weight in investment decisions.

## Excel and modeling notes

- Use Excel's `PV` and `FV` functions for regular, evenly spaced cash flows (like annuities).
- Use `NPV` for a series of irregular cash flows at regular intervals. **Note:** Excel's `NPV` function assumes the first cash flow occurs at the end of period 1.
- Use `XNPV` when cash flows occur at specific, irregular dates. `XNPV` is generally preferred in robust financial models (like project finance) because it precisely accounts for the exact timing of cash flows.
- When discounting cash flows in a DCF, you will often use a mid-year convention, which assumes cash flows are generated evenly throughout the year (meaning you discount by $n - 0.5$ periods instead of $n$).

## Interview-ready answer

[[Why is money today worth more than money tomorrow]]

## Pitfalls and gotchas

- **Confusing TVM with inflation:** While inflation reduces purchasing power, TVM is fundamentally about opportunity cost and the potential to earn a return on investment. Even in a 0% inflation environment, TVM still applies.
- **Ignoring the timing of cash flows:** Assuming cash flows arrive at the end of the year when they actually arrive mid-year (or vice versa) can materially skew valuation. Always use the mid-year convention or exact dates (`XNPV`) when appropriate.
- **Using the wrong discount rate:** Applying a risk-free rate to risky cash flows will overstate their present value. The discount rate must match the risk profile of the cash flows being discounted.

## Sources

- [[BIWS - The Time Value of Money: Excel Calculations and Real-Life Examples]]
- [[Wall Street Prep - DCF Interview Questions | Intrinsic Value Concepts]]
- [[Pivotal180 - What Ohtanis Contract can Teach us About Discount Rates]]
- [[Pivotal180 - Glossary of Terms for Project Finance Training]]
- [[A Simple Model - Discounted Cash Flow Model Overview | A Simple Model]]
