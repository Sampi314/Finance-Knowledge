---
type: concept
title: "Loan life coverage ratio"
aliases: ["LLCR"]
tags: ["project-finance", "debt-sizing", "covenants"]
difficulty: intermediate
prerequisites: ["[[Debt service coverage ratio]]", "[[Present value]]"]
related: []
sources: ["[[Finexmod - Loan Life Coverage Ratio- Legal, Technical and financial perspective – Finexmod]]", "[[BIWS - Loan Life Coverage Ratio (LLCR)- Full Tutorial + Excel]]"]
status: draft
updated: 2026-04-16
---

# Loan life coverage ratio

> **TL;DR.** The Loan Life Coverage Ratio (LLCR) is a debt metric that measures the present value of all future Cash Flow Available for Debt Service (CFADS) over the remaining life of a loan divided by the current outstanding debt balance.

## When you'd use this

You'd use this metric when sizing the initial debt balance in a project finance model or when lenders need to evaluate credit risk and test loan covenants. It is a long-term debt metric used alongside the shorter-term Debt Service Coverage Ratio (DSCR) to ensure the project's overall cash flows can support the loan.

## The 30-second version

The Loan Life Coverage Ratio (LLCR) tells lenders if the discounted cash flows over the remaining life of a loan are enough to cover the outstanding loan balance. An LLCR of 1.42x means the present value of future cash flows is 1.42 times the outstanding debt. It's used both to determine the maximum amount of debt a project can support at financial close and as an ongoing covenant to monitor downside risk throughout the life of the loan.

## The full explanation

The Loan Life Coverage Ratio (LLCR) is the "Present Value Version" of the Debt Service Coverage Ratio (DSCR). While DSCR looks at cash flows on a period-by-period basis (typically 12 months), LLCR evaluates the cash flow over the entire remaining tenor of the debt.

The calculation takes the Present Value of All Cash Flow Available for Debt Service (CFADS) in the Remaining Debt Tenor and divides it by the Current Debt Balance. The discount rate used for the PV calculation is the interest rate on the debt.

LLCR serves two primary purposes:
1. **Debt Sizing:** It can be used to size the initial debt balance. Lenders will specify a minimum or target LLCR (e.g., 1.50x), and the initial debt is calculated as the NPV of CFADS divided by this target LLCR. Sizing debt using LLCR has the advantage of avoiding circular references in Excel that often occur when using Goal Seek for DSCR-based sizing.
2. **Covenant Testing:** Lenders use LLCR to monitor the project's health. If the LLCR falls below a specified covenant level (e.g., 1.20x), lenders may impose restrictions, such as a "Cash Trap" which prevents the distribution of dividends to equity sponsors until the ratio improves.

If a project has multiple debt tranches, calculating the LLCR requires finding the weighted average interest rate across the tranches to use as the discount rate.

In simple sculpted debt models without grace periods or sweeps, sizing based on a target LLCR will result in an identical DSCR in each period. However, optional debt repayments, cash flow sweeps, or grace periods will cause the LLCR and DSCR to diverge.

## Formula

![[Loan Life Coverage Ratio]]

## Worked example

(none)

## Excel and modeling notes

When sizing debt using LLCR in Excel, it does not completely resolve circular reference issues related to taxes. Specifically, taxes in the CFADS calculation change based on interest expense, but interest expense is affected by taxes because CFADS determines the initial debt balance. This circularity usually requires a VBA copy/paste macro to resolve. For models with variable interest rates or debt tenors, LLCR is often calculated by creating a running sum and discounting back from the end of the period to the start using a flag for the debt tenor.

## Interview-ready answer

The Loan Life Coverage Ratio (LLCR) measures the present value of a project's future cash flows over the remaining life of the loan divided by the outstanding debt balance. It's a long-term metric used by lenders to size the initial debt amount and to test covenants, ensuring the project can withstand downside scenarios.

## Pitfalls and gotchas

- Assuming LLCR and DSCR will always be equal; while they align in simple sculpting scenarios, they will diverge if there are cash sweeps, optional prepayments, or grace periods.
- Failing to ask lenders exactly how they want LLCR calculated, as some may define it as the NPV of CFADS divided by the NPV of Debt Service.
- Not properly calculating the weighted average interest rate when applying LLCR to a capital structure with multiple debt tranches.

## Sources

- [[Finexmod - Loan Life Coverage Ratio- Legal, Technical and financial perspective – Finexmod]]
- [[BIWS - Loan Life Coverage Ratio (LLCR)- Full Tutorial + Excel]]
