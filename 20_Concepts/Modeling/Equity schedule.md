---
type: concept
title: "Equity schedule"
aliases: []
tags: ["modeling", "three-statement", "schedules"]
difficulty: intermediate
prerequisites: ["[[Three-statement model]]", "[[Working capital schedule]]", "[[Debt schedule]]"]
related: ["[[Linking the three statements]]"]
sources: ["[[IB Interview Questions - 3-Statement Financial Model- How to Build One]]", "[[CFI - Modular Model – What is a Modular Financial Model]]", "[[BIWS - Real Estate Development Modeling- Equity, Debt Draws & Repayment]]"]
status: stub
updated: 2026-04-13
---

# Equity schedule

> **TL;DR.** Track diluted shares outstanding and retained earnings roll-forward to complete the equity section of the balance sheet in a financial model.

## When you'd use this

This schedule is used in 3-statement models, modular models, and real estate development models to track equity balances. It details new equity issuance, share buybacks, retained earnings, and dividends.

## The 30-second version

In a modular or 3-statement model, you need to track the components of Equity on the balance sheet. An equity schedule does this by rolling forward beginning balances. Retained earnings are rolled forward by adding Net Income from the income statement and subtracting dividends. Shares outstanding are rolled forward by tracking new issuance, buybacks, and option/RSU dilution.

## The full explanation

The schedule tracks:
- **Retained Earnings Roll-Forward**: Ending Retained Earnings = Beginning RE + Net Income - Dividends. (Sourced from IB Interview Questions).
- **Share Count Roll-Forward**: Ending Shares = Beginning Shares + New Issuance - Buybacks + Option/RSU Dilution. (Sourced from IB Interview Questions).
- **Equity / Debt Draws in Projects**: In real estate development models, equity schedules determine how much developer or investor equity is drawn down to fund the project before taking on debt tranches (e.g., mezzanine debt).

## Formula

- $\text{Ending Shares} = \text{Beginning Shares} + \text{New Issuance} - \text{Buybacks} + \text{Option/RSU Dilution}$
- $\text{Ending Retained Earnings} = \text{Beginning RE} + \text{Net Income} - \text{Dividends}$

## Worked example

(none)

## Excel and modeling notes

Model this schedule sequentially in the model's Flow (after Assumptions and Operating Schedules, usually grouped with the Debt Schedule in the "Financing Engine"). Keep external links green, formulas black, inputs blue.

## Interview-ready answer

The equity schedule is a supporting schedule in a modular 3-statement model that rolls forward the components of equity. It tracks the change in retained earnings (adding net income and subtracting dividends), models new share issuances and buybacks, and tracks total shares outstanding.

## Pitfalls and gotchas

- Forgetting to link dividends correctly as a negative cash outflow in the financing section of the cash flow statement.
- Not ensuring that the retained earnings roll-forward perfectly matches the Net Income flowing from the income statement.

## Gaps

The raw sources are thin, covering basic roll-forwards and development project draws, but they lack deeper explanations and a comprehensive example. More extensive source material is needed.

## Sources

- [[IB Interview Questions - 3-Statement Financial Model- How to Build One]]
- [[CFI - Modular Model – What is a Modular Financial Model]]
- [[BIWS - Real Estate Development Modeling- Equity, Debt Draws & Repayment]]
