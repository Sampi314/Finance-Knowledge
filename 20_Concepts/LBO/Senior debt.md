---
type: concept
title: "Senior debt"
aliases: ["Senior Debt", "Senior loans"]
tags: ["lbo", "debt", "capital-structure"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[A Simple Model - Senior Debt- Summary of Terms - A Simple Model]]", "[[A Simple Model - Senior Debt Summary of Terms (or Term Sheet) - A Simple Model]]", "[[Financial Modelling Handbook - Modelling debt - concepts and assignment]]", "[[Sapphire 45 - Understanding Subordinated Debt- Key Features and Risks]]"]
status: stub
updated: 2026-04-15
---

# Senior debt

> **TL;DR.** Senior debt is the most secure tier of a company's capital structure, having the highest priority of repayment in the event of default or bankruptcy.

## When you'd use this

You will model senior debt when building a leveraged buyout (LBO) model, project finance model, or any structured financing transaction. It is the cheapest and primary source of debt capital, and its specific terms (like amortization, covenants, and maturity) dictate the base debt schedule before any subordinated debt or equity is modeled.

## The 30-second version

Senior debt sits at the very top of the capital stack. Because it is paid back first if the business goes bankrupt, it carries the lowest risk for the lender. To reflect this lower risk, senior lenders charge lower interest rates compared to subordinated lenders or equity investors. Senior debt is typically secured by the company's assets serving as collateral. When modeling debt, it is essential to build the senior debt schedule first because its covenants and cash flow sweeps directly impact what cash is available for junior creditors.

## The full explanation

In highly structured transactions such as project finance and leveraged buyouts, capital is layered into a hierarchy known as the capital stack. This hierarchy determines the priority of payments.

Senior debt holders possess the highest priority. If a company faces liquidation or default, senior debt is satisfied before subordinated debt (junior debt) and equity. Because of this priority, senior debt represents the lowest risk to the capital provider, which translates to the lowest cost of capital (interest rate) for the borrower.

Senior debt is often secured by collateral, such as real estate, equipment, or receivables. In contrast, subordinated debt is usually unsecured. Furthermore, senior debt term sheets include strict financial covenants. A common covenant is the Total Leverage Ratio, which caps the amount of funded debt as a multiple of EBITDA. Breaching these covenants gives senior lenders the right to demand immediate repayment, which can put all subordinated capital at risk. Because of this, it is critical that senior and subordinated lenders agree on an intercreditor agreement that governs their relationship and rights.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling senior debt in an LBO, you need the initial loan amount, maturity, cash flow sweep provisions, interest rate, amortization schedule, and financial covenants from the term sheet. The amortization schedule dictates how the principal is paid down over time (e.g., straight-line vs. sculpted). Since senior debt requires mandatory principal repayments and interest payments, it sits at the top of the cash flow waterfall. Always calculate the senior debt schedule first, as it drives the cash available for subordinated debt service.

## Interview-ready answer

Senior debt is the most secure tranche of debt in a company's capital structure and has the first claim on assets in the event of default. Because of its priority and the fact that it is typically secured by collateral, it carries the lowest risk and therefore the lowest interest rate. In an LBO model, senior debt is modeled first in the debt schedule and cash flow waterfall.

## Pitfalls and gotchas

- Assuming subordinated debt can be modeled independently; subordinated debt terms heavily depend on the senior debt's covenants and intercreditor agreements.
- Using the wrong balance to calculate interest. In many models, interest is calculated on the beginning balance of the period unless repayments happen intra-period.
- Overlooking cash flow sweep provisions that force excess cash to rapidly pay down senior debt.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[A Simple Model - Senior Debt- Summary of Terms - A Simple Model]]
- [[A Simple Model - Senior Debt Summary of Terms (or Term Sheet) - A Simple Model]]
- [[Financial Modelling Handbook - Modelling debt - concepts and assignment]]
- [[Sapphire 45 - Understanding Subordinated Debt- Key Features and Risks]]