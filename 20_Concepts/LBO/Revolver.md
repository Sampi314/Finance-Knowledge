---
type: concept
title: "Revolver"
aliases: ["Revolving Credit Facility", "RCF"]
tags: ["lbo", "debt", "financing"]
difficulty: intermediate
prerequisites: ["[[Senior debt]]"]
related: ["[[LBO sources and uses]]", "[[PIK toggle]]"]
sources: ["[[Wall Street Prep - Revolving Credit Facility (RCF) - Definition + Interest Rates]]", "[[Macabacus - Cash Sweep & Revolving Debt Repayment Guide]]"]
status: stub
updated: 2026-04-15
---

# Revolver

> **TL;DR.** A revolving credit facility (revolver) acts like a corporate credit card, allowing companies to borrow up to a limit, repay, and borrow again to fund working capital or serve as a liquidity backstop.

## When you'd use this

Companies use revolvers as a liquidity backstop or to fund day-to-day working capital needs. Investment grade companies typically keep their revolvers undrawn as an emergency option, while leveraged borrowers often rely on them as a primary liquidity source for operations.

## The 30-second version

A revolver allows a company to borrow money as needed up to a predetermined limit, repay the loan, and borrow again, usually over a 5-year term. Borrowers pay upfront fees, a margin on the utilized portion based on a benchmark rate plus a spread, and a commitment fee on the unused portion. If a company generates excess cash flow, it can use a cash sweep to periodically pay down its drawn revolver balance to reduce interest expenses.

## The full explanation

### Overview and Function
A revolving credit facility is a core product in corporate banking. The borrowing company can draw from the facility at any time up to a specified limit. The terms often allow for optional early repayment, and companies use excess cash to service this debt.

### Fees and Pricing
Banks charge three main types of fees on a revolver:
1. **Upfront Fees:** Charged when the facility is put together (often sub-10 basis points per year of the tenor).
2. **Utilization/Drawn Margin:** Interest charged on the amount actually drawn, typically priced as a benchmark rate (like LIBOR) plus a spread. The spread depends on the borrower's credit rating (for investment grade) or credit ratios like Debt/EBITDA (for leveraged borrowers).
3. **Commitment Fees:** Charged on the undrawn portion of the credit facility to compensate the bank for keeping capital available and incurring a loan loss provision.

### Cash Sweeps
If a borrower has excess cash beyond minimum operating requirements, they may use it to periodically repay debt ahead of schedule, known as a cash sweep. Total cash available for debt service is calculated by taking excess cash and adjusting for cash flows from operating, investing, and certain financing activities. If this amount is positive after scheduled debt repayment, the excess can pay down the revolver. If negative, the company must draw down from the revolver.

## Formula
(none)

## Worked example
(none)

## Excel and modeling notes

Modeling the revolver is complex because its balance changes based on the company's liquidity needs. You must calculate total cash available for debt service. If there is insufficient cash, the model should trigger a drawdown from the revolver. If there is excess cash, the model should trigger an optional repayment of the revolver (a cash sweep). Note that senior debt is typically scheduled to be repaid before junior debt, though this is a modeling choice.

## Interview-ready answer

A revolver is a flexible loan that functions like a corporate credit card, allowing companies to borrow, repay, and borrow again up to a limit. Borrowers pay interest on drawn amounts and a commitment fee on the undrawn portion. In financial models, excess cash flow is typically swept to pay down the revolver, reducing the company's debt load.

## Pitfalls and gotchas

- **Underestimating commitment fees:** Remember that banks charge a commitment fee on the undrawn portion, which must be factored into interest calculations.
- **Miscalculating cash available:** Ensure minimum cash balances are deducted before calculating the cash sweep available for debt repayment.
- **Circular references:** Modeling a revolver can create circular references since interest expense depends on the debt balance, which depends on cash flow, which is affected by interest expense.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Wall Street Prep - Revolving Credit Facility (RCF) - Definition + Interest Rates]]
- [[Macabacus - Cash Sweep & Revolving Debt Repayment Guide]]
