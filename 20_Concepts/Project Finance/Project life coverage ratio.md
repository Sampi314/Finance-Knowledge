---
type: concept
title: "Project life coverage ratio"
aliases: ["PLCR"]
tags: ["project-finance", "debt-sizing", "ratios"]
difficulty: intermediate
prerequisites: ["[[Debt service coverage ratio]]", "[[Loan life coverage ratio]]", "[[Project finance overview]]"]
related: ["[[Equity vs debt in project finance]]"]
sources: ["[[Lentran Solutions - Project Finance Ratios - Lentran Modelling Solutions]]", "[[Project Finance - LLCR and PLCR Complexities and Meaning for Break Even]]"]
status: stub
updated: 2026-04-16
---

# Project life coverage ratio

> **TL;DR.** The Project Life Coverage Ratio (PLCR) is the ratio of the present value of cash flows over the entire project life to the outstanding debt.

## When you'd use this
The PLCR is used by lenders in project finance to evaluate a project's debt repayment capacity. Lenders pay close attention to project finance ratios because loans are non-recourse, meaning they can only rely on the projected cashflows of the project rather than the balance sheet of its sponsors. It is a critical metric found in loan documentation and term sheets alongside the Debt Service Coverage Ratio (DSCR) and Loan Life Coverage Ratio (LLCR).

## The 30-second version
Like the DSCR and LLCR, the PLCR provides a measure of a project's ability to cover its debt obligations. While the LLCR measures the present value of cash flows over the life of the loan, the PLCR measures the present value of cash flows over the entire life of the project. The difference between the LLCR and the PLCR provides an added buffer that provides safety from the "tail"—the difference between the end of the debt tenure and the project life.

## The full explanation
The PLCR is a key financial ratio in project finance, used to assess break-even points from a lender's perspective. It evaluates how much the cash flows over the entire project life can drop while still allowing the loan to be fully repaid.

If the DSCR is CFADS/Debt Service, the PLCR puts PV factors around the CFADS and the Debt Service. But since the PV of debt service is the same as debt at COD (or after COD), the PLCR compares the PV of cash flows directly to the outstanding debt balance. If there is a debt service reserve account (DSRA), this should be subtracted from debt using the principal of net debt in corporate finance (where cash is like negative debt).

The PLCR can also be used to compute the percent decline in cash flow over the entire project life that can occur and the loan can still be repaid in full. If the cash flow percentage drops below the LLCR implied break-even, the debt cannot be repaid over the debt life. However, the debt can still be repaid by the end of the project life as long as the PLCR is above 1.0.

## Formula
![[Project life coverage ratio formula]]

## Worked example
(none)

## Excel and modeling notes
When calculating the present value of cash flows for coverage ratios like the LLCR and PLCR, computing the prospective debt IRR can be used for the discount rate. Care must be taken if there are multiple debt issues with different interest rates and different debt tenors. For example, a second debt issue might have a long-tenor, a grace period, and a very low interest rate.

## Interview-ready answer
The Project Life Coverage Ratio (PLCR) is the ratio of the present value of Cash Flow Available for Debt Service (CFADS) over the entire project life to the outstanding debt. It provides lenders an assessment of the added buffer and safety from the tail—the difference between the end of the debt tenure and the project life.

## Pitfalls and gotchas
- **Discount Rate:** The discount rate used for calculating the PV of cash flows can impact the PLCR, particularly when dealing with changing interest rates and multiple debt issues.
- **Net Debt Consideration:** Failing to subtract the Debt Service Reserve Account (DSRA) from the outstanding debt balance can distort the calculated PLCR.

## Gaps
- Missing worked example
- Missing explicit calculation formula for break-even percent decline.

## Sources
- [[Lentran Solutions - Project Finance Ratios - Lentran Modelling Solutions]]
- [[Project Finance - LLCR and PLCR Complexities and Meaning for Break Even]]
