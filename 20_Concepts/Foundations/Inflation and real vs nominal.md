---
type: concept
title: "Inflation and real vs nominal"
aliases: ["Real vs nominal", "Nominal cash flows", "Real cash flows"]
tags: ["foundations", "inflation", "macroeconomics", "modeling"]
difficulty: beginner
prerequisites: ["[[Time value of money]]"]
related: ["[[Discount rate]]"]
sources: ["[[Pivotal180 - real-financial-modeling-is-a-waste-of-your-time-2]]"]
status: draft
updated: 2024-11-08
---

# Inflation and real vs nominal

> **TL;DR.** Nominal figures represent actual cash amounts in the future, while real figures are adjusted for inflation to show purchasing power in today's dollars.

## When you'd use this

You need to understand the difference between real and nominal when building financial models, evaluating investment returns, or projecting future cash flows. It is crucial for determining whether to inflate revenues and costs, and ensuring that your discount rates and cash flows use the same basis.

## The 30-second version

"Real" cash flows are cash flows in the future but stated at today’s equivalent value (purchasing power). However, they are not actual cash flows you will pay or receive. "Nominal" cash flows are the actual amounts of cash you expect to pay or receive in the future, which account for inflation. Because inflation means things cost more over time, nominal cash flows increase each year compared to real cash flows. In financial modeling, it is almost always better to model in nominal terms because debt, taxes, and investor returns are all based on actual (nominal) cash.

## The full explanation

### Real modeling
Modeling assuming your purchasing power will remain the same is called "real modeling." For example, if rent is $1,000 today, real modeling assumes it stays $1,000 in year 10. While this keeps numbers constant and simplifies some comparisons, it ignores the reality that actual cash required will be higher due to inflation.

### Nominal modeling
Nominal modeling inflates numbers to the actual cash required in the future. If rent is $1,000 today and inflation is 5% per year, the actual amount you must pay in the future increases. Inflation is compounding, meaning the 5% is applied to the preceding year's inflated amount, not the original $1,000.

### Why nominal modeling is standard
Modeling in real terms creates massive complications below the operating cash flow line:
- **Debt repayments:** Loans specify actual cash to be repaid. Back-calculating these into "real" dollars is nonsensical.
- **Investor returns:** Investors target cash-on-cash returns based on actual money received.
- **Taxes and depreciation:** Governments tax actual (nominal) earnings. Depreciation and net operating losses are nominal.
- **Interest and FX:** Benchmark rates (like LIBOR/SOFR) and foreign exchange curves already build in inflation assumptions.

## Formula

The relationship between real and nominal cash flows for a specific time period is:

![[Real to Nominal Cash Flow Conversion]]

And the Fisher Equation approximates real returns from nominal returns:

![[Fisher Equation]]

## Worked example

[[Rent Inflation Example]]

## Excel and modeling notes

When modeling, inflate your revenues and costs based on contracted rates or assumed price escalation, and calculate the nominal rate of return. Avoid the complications of trying to deflate taxes, interest rates, and debt to real terms. It's essentially "crazy to work in real cash flows below operating cash flows."

## Interview-ready answer

"Nominal cash flows represent the actual dollars that will change hands in the future, while real cash flows adjust for inflation to reflect purchasing power in today's terms. In financial modeling, we almost always project in nominal terms because debt service, taxes, and investor distributions are all paid in actual nominal dollars."

## Pitfalls and gotchas

- **Mixing real and nominal:** The most common mistake is discounting nominal cash flows with a real discount rate, or vice versa. Both must match.
- **Applying flat inflation incorrectly:** Inflation compounds. A 5% inflation rate in Year 3 means the cash flow is multiplied by $(1 + 0.05)^3$, not just adding 15%.
- **Deflating non-operating items:** Trying to model taxes or debt service in real terms leads to unnecessary complexity and errors.

## Sources

- [[Pivotal180 - real-financial-modeling-is-a-waste-of-your-time-2]]
