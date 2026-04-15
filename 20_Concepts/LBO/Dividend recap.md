---
type: concept
title: "Dividend recap"
aliases: ["Dividend Recapitalization", "Leveraged Dividend Recap"]
tags: ["LBO", "private equity", "returns"]
difficulty: intermediate
prerequisites: ["[[LBO overview]]", "[[IRR]]", "[[Debt covenants]]", "[[Multiple of money]]"]
related: ["[[PIK toggle]]", "[[LBO exit]]", "[[Cash-on-cash return]]", "[[LBO sources and uses]]"]
sources: ["[[IB Interview Questions - Dividend Recapitalization- How PE Firms Return Capital]]", "[[Financial Modeling NYC - Dividend Recap Modeling- Excel Tutorial + IRR Boost]]", "[[BIWS - Dividend Recap- LBO Tutorial With Excel Examples]]"]
status: draft
updated: 2026-04-15
---

# Dividend recap

> **TL;DR.** A dividend recapitalization is a transaction where a private equity-owned portfolio company borrows new money specifically to pay a special dividend to its equity holders, primarily the PE sponsor.

## When you'd use this

Private equity firms use dividend recapitalizations when a portfolio company performs well, generates strong cash flows, and has increased its debt capacity (e.g., through operational improvements pushing EBITDA higher). Sponsors often execute these transactions mid-holding period (e.g., Year 2 or 3) to de-risk their investment, accelerate capital returns to their Limited Partners (LPs), or when traditional exit routes like M&A or IPOs are challenging or unappealing.

## The 30-second version

In a standard LBO, the sponsor realizes their return primarily at the exit. In a dividend recap, the PE firm extracts cash from the business early by loading it with new debt (like a new Term Loan B) and paying out a special dividend. By getting some or all of their initial equity back sooner, the PE firm significantly boosts its Internal Rate of Return (IRR) because of the time value of money. The sponsor maintains control and upside potential, though the company now carries a heavier debt burden.

## The full explanation

There are two main types of dividend recaps: unleveraged (paying a dividend from existing free cash flow) and leveraged. The more impactful and common "leveraged dividend recap" involves issuing additional debt to fund the dividend.

If a company was bought for €100M (€60M debt, €40M equity) and its EBITDA grows from €20M to €25M, the sponsor might refinance. They could issue €50M in new debt, repay portions of the existing debt, and distribute a €40M dividend. This effectively reduces the sponsor's remaining equity basis, often down to zero. The IRR jumps significantly (e.g., from 25% to 35% annualized) due to the early cash realization, even if the ultimate exit value is reduced by the higher debt outstanding.

However, this strategy hinges on the company's senior debt capacity (typically 3.0-4.0x trailing EBITDA) and total leverage headroom. If the company performs poorly after a recap, the increased financial leverage can make negative returns even worse.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

To model a dividend recap:
1. **Determine timing and size:** Typically Year 2-3, constrained by debt incurrence tests and covenant capacity (e.g., total net leverage capped at 4.0-5.0x).
2. **Debt schedule:** Add the new debt issuance to the debt waterfall in the recap year, and flow it through mandatory prepayments and interest calculations. Update the sources and uses dynamically.
3. **Dividend logic:** Create a cash outflow line item for the equity distribution, reducing Sponsor Equity on the balance sheet.
4. **Returns calculation:** Calculate IRR across all cash flows—initial investment (outflow), the mid-hold dividend (inflow), and the final exit proceeds net of the now-higher debt (inflow).

## Interview-ready answer

[[What is a dividend recapitalization and why do PE firms do them]]

## Pitfalls and gotchas

- Overleveraging the portfolio company can cause interest coverage to dip below critical levels (e.g., 2.0x), risking covenant breaches and distress or bankruptcy.
- Lenders face lower recovery prospects because the recap proceeds immediately leave the company rather than staying available for creditor recovery.
- Rating agencies may downgrade the company due to the aggressive financial policy.
- Aggressive recaps can damage relationships with lenders and affect the sponsor's future access to financing.

## Sources

- [[IB Interview Questions - Dividend Recapitalization- How PE Firms Return Capital]]
- [[Financial Modeling NYC - Dividend Recap Modeling- Excel Tutorial + IRR Boost]]
- [[BIWS - Dividend Recap- LBO Tutorial With Excel Examples]]