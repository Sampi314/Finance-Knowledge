---
type: concept
title: "Time value of money"
aliases: ["TVM"]
tags: ["foundations", "discounting", "opportunity-cost"]
difficulty: beginner
prerequisites: []
related: ["[[Present value]]", "[[Future value]]"]
sources: ["[[BIWS - The Time Value of Money Excel Calculations and Real-Life Examples]]", "[[CFI - Cash - Definition, Business Operations, Economics]]"]
status: draft
updated: 2024-05-23
---

# Time value of money

> **TL;DR.** The time value of money means that money today is worth more than the same amount of money tomorrow because you could invest it today and earn a return on it in the future.

## When you'd use this

You use the time value of money concept every time you value an asset, make investment decisions, or compare different cash flow scenarios across time periods. It is the core foundation behind discounted cash flow (DCF) models, pricing bonds, and assessing whether to accept a sum of money now versus a series of payments in the future.

## The 30-second version

If you have $100 today, it is inherently more valuable than receiving $100 a year from now. This is because you can take the $100 today and invest it (in a bank account, stocks, or other assets) to earn a return. If your investment earns a 5% return, you will have $105 next year. Therefore, $100 today is actually equal to $105 next year, and getting $100 next year means you missed out on earning that extra $5. This missed potential return is called your opportunity cost.

## The full explanation

The time value of money (TVM) is the financial principle that any sum of money is worth more the sooner it is received.

Many people mistakenly attribute the time value of money purely to inflation—the idea that money loses purchasing power over time. While inflation does erode purchasing power, the fundamental driver of TVM is **opportunity cost**. By not having the cash today, you lose the opportunity to invest it and generate a yield.

### Discounting future cash flows
Because money tomorrow is worth less than money today, finance professionals "discount" future cash flows to determine their present equivalent (Present Value). If you know your opportunity cost—the return you could earn on other investments of similar risk—you use that rate to discount the future amount back to today.

For example, if you are analyzing an asset that pays $100 in 10 years, and your opportunity cost is 10% per year, the present value of that payment is only $38.60 ($100 / (1 + 0.10)^10). The further into the future a cash flow is, the heavier it is discounted, which is why near-term cash flows have a much bigger impact on valuation than long-term cash flows.

## Formula

(none)

## Worked example

[[Renting an Apartment with High Deposit vs Monthly Rent]]

## Excel and modeling notes

When modeling TVM concepts in Excel, you often rely on functions like `PV` (Present Value), `FV` (Future Value), `NPV` (Net Present Value), or `XNPV` for specific dates. In a cash flow model, it's common practice to multiply future cash flows by a "discount factor" that is explicitly calculated for each period using the discount rate.

## Interview-ready answer

The time value of money dictates that a dollar today is worth more than a dollar tomorrow because of its potential earning capacity. If I have cash today, I can invest it and earn a return, which means any future cash flow must be discounted back to the present using an opportunity cost of capital to reflect what I could have earned elsewhere.

## Pitfalls and gotchas

- **Confusing it with just inflation:** Inflation is a factor, but opportunity cost (foregone investment returns) is the primary reason money today is worth more.
- **Ignoring risk:** The discount rate used to calculate present value must match the risk profile of the cash flows. Using a risk-free rate for a highly uncertain future cash flow overvalues the future money.
- **Comparing nominal cash flows over time:** Comparing $1,000 paid today to $1,000 paid over five years without discounting is a flawed analysis, as it ignores the time value of money.

## Sources

- [[BIWS - The Time Value of Money Excel Calculations and Real-Life Examples]]
- [[CFI - Cash - Definition, Business Operations, Economics]]
