---
type: concept
title: "Three-statement model"
aliases: ["3-statement model", "Three Statement Models"]
tags: ["modeling", "foundations", "excel"]
difficulty: beginner
prerequisites: ["[[The income statement]]", "[[The balance sheet]]", "[[The cash flow statement]]"]
related: []
sources: ["[[Full Stack Modeller - What Is Financial Modelling]]", "[[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]"]
status: draft
updated: 2026-04-12
---

# Three-statement model

> **TL;DR.** A forward-looking model that interlinks the income statement, balance sheet, and cash flow statement to forecast a company's financial performance.

## When you'd use this

A three-statement model is the fundamental structure behind almost all corporate financial modeling. It is used continuously by financial professionals to forecast budgets, analyze potential acquisitions, evaluate capital structure (like LBOs), or determine intrinsic value through DCF.

## The 30-second version

At its core, a three-statement model takes historical financial data, applies assumptions and drivers about future operations, and projects the income statement, balance sheet, and cash flow statement over a set period. By keeping the fundamental accounting equation intact across all three interlinked statements, the model provides a holistic, unified view of a company's potential future financial position and performance.

## The full explanation

A traditional three-statement model connects the three foundational accounting statements to forecast future financial health.

### The Income Statement
This statement forecasts profitability over a period of time. You project revenue down to Net Income, which then acts as a bridge to the other two statements. The Income Statement operates on an accrual basis, meaning revenues and expenses are recognized when incurred, not necessarily when cash changes hands.

### The Cash Flow Statement
Since Net Income does not reflect actual cash generated, the Cash Flow Statement adjusts the accrual-based income back to cash. Starting with Net Income in Cash Flow from Operations, non-cash charges like Depreciation are added back. Then, working capital changes and investments (like CapEx) are accounted for, leading to the net change in cash.

### The Balance Sheet
This statement provides a snapshot of the company's financial position at a specific time and is governed by the equation `Assets = Liabilities + Equity`. The net change in cash updates the cash balance, Net Income updates Retained Earnings, and items like CapEx and Depreciation update the value of assets. Because the statements are linked, the balance sheet naturally balances if the inputs and links are correct.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When building these models in Excel, a best practice is to separate your work into Control, Input, Calculation, and Output worksheets. Clear color coding and consistent structure make the model easier to read and audit. A common complexity in three-statement modeling is the circular reference caused by interest expense depending on debt, which depends on cash, which in turn depends on interest expense.

## Interview-ready answer

Understanding how the three financial statements link together is a fundamental requirement. You must be able to explain how Net Income bridges to the top of the Cash Flow Statement, how adjustments like Depreciation are handled, and how the net change in cash and Retained Earnings ultimately flow into a balanced Balance Sheet.

## Pitfalls and gotchas

- Starting your explanation in the wrong place. Always begin with Net Income, as it bridges the three statements.
- Losing track of the Balance Sheet equation. In a model, every change must ensure that Assets = Liabilities + Equity.
- Forgetting key connections, like adding back Depreciation or how CapEx increases Property, Plant & Equipment.

## Sources

- [[Full Stack Modeller - What Is Financial Modelling]]
- [[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]
