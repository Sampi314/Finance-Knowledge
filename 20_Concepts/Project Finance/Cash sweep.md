---
type: concept
title: "Cash sweep"
aliases: ["Optional Debt Repayment", "Cash flow sweep"]
tags: ["project-finance", "debt", "lbo"]
difficulty: intermediate
prerequisites: ["[[Project finance overview]]"]
related: []
sources: ["[[Wall Street Prep - LBO Cash Sweep - Formula + Calculator]]", "[[BIWS - Cash Flow Sweep in LBO Models- Full Tutorial]]"]
status: stub
updated: 2026-04-16
---

# Cash sweep

> **TL;DR.** In leveraged buyout and credit models, the cash flow sweep is the company's ability to optionally repay debt based on its excess free cash flows in a period, in addition to mandatory scheduled amortization.

## When you'd use this

This concept applies when a company has excess cash flow after meeting all operational and required financing needs, such as mandatory debt amortization. In an LBO, optional debt paydown through a cash sweep lowers the overall debt burden and interest expense. In Project Finance, debt is typically sculpted to cash flows, so cash flow sweeps allow for "bonus" repayments if cash flow exceeds targeted levels.

## The 30-second version

A cash sweep mechanism allows a borrower to use excess free cash flows to pay down outstanding debt balances earlier than scheduled. The excess cash is the amount left over after operating cash flow, investing cash flows, financing obligations, and minimum cash balance requirements are all covered. By paying down principal early, the borrower reduces future interest expenses and improves their credit profile. However, some lenders may impose prepayment penalties or prohibit cash sweeps to protect their targeted yields.

## The full explanation

A cash sweep is an arrangement common in Senior Debt structures (such as Term Loans issued by banks) in leveraged buyouts. When a company voluntarily pre-pays debt, it reduces the senior lenders' credit risk because there's less outstanding principal at risk of default.

However, it introduces reinvestment risk to lenders because they must take the returned capital and lend it elsewhere, possibly at less favorable rates. As a result, cash flow sweeps are often limited to a certain percentage of the available free cash flow (e.g., 50% or 100%), which is defined in the credit agreement. Some junior debt forms prohibit early prepayment or carry substantial penalty fees to guarantee the lender's overall return.

While early prepayment lowers interest expense, it also reduces the tax shield benefits associated with debt financing. In models involving multiple tranches of debt (e.g., Revolver, Term Loan A, Term Loan B), cash flow sweeps usually apply in order of seniority. The Revolver is typically paid down first, followed by Term Loan A and Term Loan B.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

In simple modeling scenarios, Cash Flow Available for Debt Repayment (CFADR) equals Beginning Cash plus Free Cash Flow minus Minimum Cash required on the balance sheet. In Excel, calculate the mandatory amortization first, then apply the cash sweep percentage to the remaining excess cash, and use the `MIN` function to ensure you do not repay more than the remaining beginning principal balance.

## Interview-ready answer

A cash flow sweep is an optional debt repayment mechanism where a borrower uses excess free cash flow, after all mandatory obligations and minimum cash requirements are met, to pay down debt principal early. This helps reduce future interest expense and deleverage the company, though it can trigger prepayment penalties and reduce the interest tax shield.

## Pitfalls and gotchas

- **Exceeding the principal balance**: Always use a `MIN` formula (e.g., `MIN(Excess Cash, Beginning Balance - Mandatory Amortization)`) to avoid negative debt balances in projections.
- **Prepayment penalties**: Failing to account for prepayment penalties when analyzing the economics of a cash sweep can overestimate the benefit of paying down debt early.
- **Capital structure hierarchy**: Applying cash sweeps improperly across multiple tranches of debt; senior debt like revolvers and Term Loan A usually must be repaid before Term Loan B.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[BIWS - Cash Flow Sweep in LBO Models- Full Tutorial]]
- [[Wall Street Prep - LBO Cash Sweep - Formula + Calculator]]
