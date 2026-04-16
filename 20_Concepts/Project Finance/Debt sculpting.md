---
type: concept
title: "Debt sculpting"
aliases: []
tags: ["project-finance", "debt-sizing", "financial-modeling"]
difficulty: intermediate
prerequisites: ["[[Debt service coverage ratio]]", "[[Loan life coverage ratio]]"]
related: ["[[Project life coverage ratio]]", "[[Cash sweep]]"]
sources: ["[[BIWS - Debt Sculpting vs Debt Sizing in Project Finance]]", "[[Financial Modelling Handbook - Debt modelling - Debt sizing & debt sculpting]]"]
status: draft
updated: 2026-04-16
---

# Debt sculpting

> **TL;DR.** Debt sculpting matches the required principal repayment in each period to the available cash flows to maintain a targeted coverage ratio.

## When you'd use this

Debt sculpting is predominantly used in Project Finance where cash flows are highly predictable due to long-term contracts. Lenders use it to ensure that the debt service (principal and interest) tracks the project's actual cash generation capability over time.

## The 30-second version

Instead of setting a fixed repayment schedule, debt sculpting calculates the maximum debt service a project can afford in any given period based on its Cash Flow Available for Debt Service (CFADS) and a target Debt Service Coverage Ratio (DSCR) or Loan Life Coverage Ratio (LLCR). By subtracting the interest expense from this maximum debt service, we determine the sculpted principal repayment for that period.

## The full explanation

Debt sculpting is a technique used in Project Finance to link debt repayment directly to the project's cash flow profile. The process typically involves:
1. Forecasting the project's Cash Flow Available for Debt Service (CFADS).
2. Applying a target coverage ratio (like DSCR or LLCR) to determine the Maximum Debt Service for each period.
3. Calculating the Interest Expense for the period based on the outstanding debt balance.
4. Deriving the principal repayment ("sculpting") as the difference between the Maximum Debt Service and the Interest Expense.

This approach ensures that in periods with strong cash flows, debt repayment is higher, while in periods with weaker cash flows, the repayment drops, reducing default risk and maximizing the amount of debt the project can support.

## Formula

The core formula to determine the sculpted principal repayment in a given period is:

`Sculpted Principal Repayment = (CFADS / Target DSCR) - Interest Expense`

## Worked example

[[Debt Sculpting DSCR Example]]

## Excel and modeling notes

When modeling debt sculpting, you may encounter circular references because calculating CFADS requires subtracting Cash Taxes, which depend on the tax-deductible Interest Expense, which in turn depends on the debt sizing and principal repayments you are trying to solve for.

A common modeling technique to avoid Excel's "circular death loop" is to calculate the initial debt size using the present value of CFADS discounted at the debt interest rate, scaled by the target LLCR. Another approach is to use a VBA copy/paste macro to trick the model into using hard-coded CFADS rather than calculated ones to avoid circular references.

## Interview-ready answer

Debt sculpting is the process of structuring debt repayments in a project finance deal so that the principal repayment in each period fluctuates based on the project's available cash flow and a targeted coverage ratio, such as the DSCR. This approach reduces lender risk by matching debt service to cash generation and allows sponsors to maximize leverage.

## Pitfalls and gotchas

- Sculpting models can easily develop circular references when incorporating tax-deductible interest into CFADS calculations.
- Sculpted principal repayments can sometimes become negative in early periods if CFADS is insufficient to even cover the interest expense at the target ratio.

## Sources

- [[BIWS - Debt Sculpting vs Debt Sizing in Project Finance]]
- [[Financial Modelling Handbook - Debt modelling - Debt sizing & debt sculpting]]