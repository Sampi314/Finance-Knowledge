---
type: concept
title: "Levered vs unlevered IRR"
aliases: ["Leveraged vs unleveraged IRR", "Project IRR", "Equity IRR"]
tags: ["real-estate", "valuation", "project-finance"]
difficulty: intermediate
prerequisites: ["[[IRR]]", "[[Present value]]", "[[Discount rate]]"]
related: ["[[WACC]]", "[[Cost of debt]]"]
sources: ["[[Pivotal180 - An introduction to the Internal Rate of Return IRR]]", "[[Finexmod - Equity Return Metrics in a Project Finance Structure- Project IRR - Finexmod]]"]
status: stub
updated: 2026-04-17
---

# Levered vs unlevered IRR

> **TL;DR.** Unlevered IRR measures the return of a project assuming it is funded entirely by equity, while levered IRR measures the return specifically to equity investors after accounting for debt financing.

## When you'd use this

You use these metrics when evaluating an investment or project to understand its standalone profitability versus its profitability when debt is used. The unlevered IRR (often called Project IRR) is used during early appraisal stages to evaluate the fundamental strength of the project before a financing structure is finalized. Levered IRR (often called Equity IRR) is used by equity investors to determine the actual financial returns they will achieve after debt service obligations are met.

## The 30-second version

Unlevered IRR looks at a project's cash flows on a standalone basis without any debt. It helps determine if the project itself is fundamentally sound. Levered IRR, on the other hand, factors in borrowed money; it calculates the return to the equity investor after the debt (principal and interest) has been paid. Because debt must be paid before equity holders receive returns, leveraging a project can increase the equity return if the cost of the debt is lower than the project's unlevered return.

## The full explanation

### Unlevered IRR (Project IRR)
The unlevered Internal Rate of Return (IRR) represents the return of a project if it were funded 100% with equity. It is calculated from the project's cash flows before any financing costs are applied. This metric demonstrates how strong a project is on a standalone basis, separate from the effects of how much the returns are geared up by borrowing money. If the unlevered IRR is lower than the cost of debt, the project cannot support debt financing and might need a concessional loan, grants, or a purely equity-based funding structure. It is typically compared against the Weighted Average Cost of Capital (WACC).

### Levered IRR (Equity IRR)
The levered IRR specifies the financial returns directly to the equity investor. It is calculated using the cash flows available after all debt service (interest and principal repayments) has been satisfied. As leverage increases, the equity IRR will generally improve as long as the cost of debt remains below the unlevered IRR. If the cost of debt exceeds the project IRR, levered returns will fall, indicating the financing structure is not viable.

### Pre-tax vs Post-tax IRR
When calculating project IRR, precision is important. Pre-tax project IRR is based on the cash flow left after non-financing construction and operating costs are paid, but before taxes. Post-tax project IRR factors in taxes as well. However, when calculating post-tax project IRR, you must ensure you exclude any financing costs (like deductible interest) from the tax calculation to maintain the unlevered assumption.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

In financial models, calculating the unlevered IRR involves using the cash flow available before financing and tax (or post-tax equivalent without financing impacts). Excel’s built-in `IRR` function can be used on these cash flow streams, which requires selecting the full range of cash flows starting at time period zero. The function will iteratively find the discount rate that sets the Net Present Value to zero.

## Interview-ready answer

Unlevered IRR is the return of a project on a standalone basis, assuming it is financed with 100% equity, which helps assess the project's fundamental viability. Levered IRR is the return to the equity investor after debt has been serviced. If the cost of debt is cheaper than the unlevered IRR, using leverage will boost the levered IRR for equity holders.

## Pitfalls and gotchas

- Confusing terminology: People sometimes refer to "Project IRR" when they actually mean "Equity IRR." Always clarify what someone means when they use the term.
- Presenting an IRR value without specifying whether it is levered or unlevered, or pre-tax or post-tax, which can lead to significant misunderstandings.
- Mixing financing effects into tax calculations when determining the post-tax unlevered IRR (e.g., leaving tax shields from interest deductions in the cash flow).

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Pivotal180 - An introduction to the Internal Rate of Return IRR]]
- [[Finexmod - Equity Return Metrics in a Project Finance Structure- Project IRR - Finexmod]]
