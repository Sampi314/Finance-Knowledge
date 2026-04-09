---
type: concept
title: "Discount rate"
aliases: ["Discount rates"]
tags: ["foundations", "valuation", "time-value-of-money"]
difficulty: beginner
prerequisites: ["[[Time value of money]]", "[[Present value]]"]
related: ["[[WACC]]", "[[Internal rate of return]]"]
sources: ["[[Pivotal180 - What Ohtanis Contract can Teach us About Discount Rates]]", "[[IB Interview Questions - How to Calculate WACC Step-by-Step]]", "[[IB Interview Questions - How to Answer Walk Me Through a DCF in IB Interviews]]", "[[Pivotal180 - An introduction to the Internal Rate of Return IRR]]"]
status: draft
updated: 2026-04-09
---

# Discount rate

> **TL;DR.** The discount rate is the interest rate used to determine the present value of future cash flows, reflecting both the time value of money and the riskiness of the investment.

## When you'd use this

You use a discount rate anytime you need to convert future expectations into a current valuation. This is the cornerstone of discounted cash flow (DCF) analysis, valuing bonds or long-term contracts, and determining if a project or investment meets a company's required return hurdles.

## The 30-second version

Because of the time value of money, a dollar received in the future is worth less than a dollar received today. A discount rate is the percentage rate at which we reduce those future cash flows to figure out their equivalent value right now (their present value). In corporate finance, the discount rate usually represents the blended cost of financing for a company, known as the Weighted Average Cost of Capital (WACC), which reflects the minimum return investors require for the level of risk they are taking.

## The full explanation

### The Time Value of Money and Risk
The discount rate mathematically links the future value (FV) to the present value (PV). Any money you have today can be invested to earn a return (like interest in a savings account). Therefore, future payments must be discounted to account for the lost opportunity of having that money today. Furthermore, the discount rate incorporates risk: riskier future cash flows require a higher discount rate, which mathematically drives their present value lower.

### Discount Rates in DCF Valuations
In a Discounted Cash Flow (DCF) valuation, the discount rate applied to unlevered free cash flows is typically the Weighted Average Cost of Capital (WACC). Because unlevered free cash flow belongs to all capital providers (both debt and equity holders), the discount rate must reflect the blended cost of that capital. Discounting the projected cash flows and the terminal value at WACC gives you the Enterprise Value of the firm. Small changes in the discount rate assumption can have massive impacts on the final valuation, especially when calculating the terminal value.

### Relationship to Internal Rate of Return (IRR)
The discount rate and the Internal Rate of Return (IRR) are mathematically linked. The IRR is defined as the specific discount rate at which the net present value (NPV) of all future cash flows of an investment equals exactly zero. When evaluating an investment, if the IRR exceeds your required discount rate (your hurdle rate), the investment is generally considered worthwhile because its NPV will be greater than zero.

## Formula

The core relationship relies on the Present Value formula, where $r$ is the discount rate:
$PV = \frac{FV}{(1+r)^n}$

## Worked example

[[Ohtani Contract Discounting]]

## Excel and modeling notes

- In Excel, you can use the `NPV` function (for fixed, regular periods) or `XNPV` (for exact dates) along with a stated discount rate to calculate the present value of future cash flows.
- When sizing debt in project finance, Excel formulas often use debt discount factors derived from interest rates to determine how much a project can borrow based on its expected cash flows.
- You can use Excel's `IRR` or `XIRR` function to find the exact discount rate that results in a zero NPV for a given series of cash flows.

## Interview-ready answer

[[What is a discount rate and how is it used in a DCF]]

## Pitfalls and gotchas

- **Mismatching cash flows and discount rates:** Applying a levered discount rate (like cost of equity) to unlevered free cash flows, or applying WACC to levered free cash flows. Unlevered FCF must be discounted by WACC.
- **Ignoring the compounding periods:** Assuming an annual discount rate applies linearly rather than compounding, or mismatching the discount rate's period with the cash flow period (e.g., using an annual rate for monthly cash flows without adjusting).
- **Underestimating terminal value sensitivity:** Failing to realize that because the terminal value often makes up the majority of a DCF's value, tiny tweaks to the discount rate can drastically swing the final valuation.

## Sources

- [[Pivotal180 - What Ohtanis Contract can Teach us About Discount Rates]]
- [[IB Interview Questions - How to Calculate WACC Step-by-Step]]
- [[IB Interview Questions - How to Answer Walk Me Through a DCF in IB Interviews]]
- [[Pivotal180 - An introduction to the Internal Rate of Return IRR]]
