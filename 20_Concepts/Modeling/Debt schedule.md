---
type: concept
title: "Debt schedule"
aliases: ["Debt Schedule", "Business Debt Schedule"]
tags: ["modeling", "LBO", "3-statement", "credit-models"]
difficulty: intermediate
prerequisites: ["[[Three-statement model]]"]
related: ["[[The income statement]]", "[[The cash flow statement]]", "[[The balance sheet]]"]
sources: ["[[Financial Modeling NYC - Debt Schedules- A Comprehensive Guide for Financial Modeling]]", "[[Wall Street Prep - Debt Schedule - Formula + Calculator]]", "[[BIWS - Debt Schedule- Video Tutorial and Excel Example]]"]
status: draft
updated: 2026-04-12
---

# Debt schedule

> **TL;DR.** A debt schedule uses a company's cash flow projections to track debt balances, calculate interest expenses, and model mandatory and optional principal repayments over time.

## When you'd use this

Debt schedules are a core component of financial modeling, used extensively in 3-statement models, LBO models, and credit models. They help assess a company’s debt capacity, credit risk, and future cash flows available for debt repayment or stock repurchases.

## The 30-second version

A debt schedule connects a company's cash flow generation to its capital structure obligations. It lays out the beginning balance, tracks new issuances, subtracts mandatory and optional repayments, and calculates the ending balance for each debt tranche. It dynamically models interest expenses based on average debt balances and flows these costs back into the income statement, affecting net income and free cash flow.

## The full explanation

A debt schedule outlines total debt obligations over time. Tranches can include Senior Debt (like term loans and revolvers) and Subordinated Debt. Mandatory amortization requires an incremental paydown, while optional cash sweeps use discretionary cash to prepay debt, contingent on covenants and seniority limits.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

Interest expense should be calculated using the average debt balance (between the beginning and ending balance) to smooth intra-year fluctuations, though this requires a circularity breaker toggle in Excel to avoid circular reference errors.

## Interview-ready answer

A debt schedule models a company’s interest expenses and principal repayments over a forecast period. It links the three financial statements by projecting cash flows available for debt service and adjusting the balance sheet's outstanding debt accordingly.

## Pitfalls and gotchas

- Circular references can crash models if interest expense calculations lack a circuit breaker toggle switch.
- Confusing mandatory principal amortization with optional cash sweep repayments.

## Sources

- [[Financial Modeling NYC - Debt Schedules- A Comprehensive Guide for Financial Modeling]]
- [[Wall Street Prep - Debt Schedule - Formula + Calculator]]
- [[BIWS - Debt Schedule- Video Tutorial and Excel Example]]
