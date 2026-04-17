---
type: concept
title: "Preferred return"
aliases: ["Hurdle Rate", "Hurdle", "Preferred Return"]
tags: ["real-estate", "private-equity", "waterfall", "investing"]
difficulty: intermediate
prerequisites: ["[[Real estate waterfall]]", "[[Promote and carried interest]]"]
related: ["[[Promote and carried interest]]"]
sources: ["[[Alter Domus - How Private Equity Waterfalls Work - Alter Domus]]", "[[Financial Modeling NYC - Private Equity Waterfall Models- European vs American Structures, Carry and Clawback]]", "[[SMB Investor Network - SMB Investment Glossary - Small Business Acquisition Terms - SMB Investor Network Resources]]"]
status: stub
updated: 2026-04-17
---

# Preferred return

> **TL;DR.** The preferred return, or hurdle rate, is the minimum annual return that Limited Partners (LPs) must receive on their invested capital before the General Partner (GP) begins to earn carried interest (performance fees).

## When you'd use this

You will encounter the preferred return in real estate joint ventures, private equity funds, and syndicate deals. It is a structural element in a distribution waterfall designed to align the incentives of the sponsor/General Partner (GP) with the passive investors/Limited Partners (LPs).

## The 30-second version

The preferred return is effectively a "first-in-line" profit threshold for passive investors. Before the fund manager or sponsor takes their cut of the upside, they must generate enough profit to clear this hurdle—commonly around an 8% annual return. Think of it as a risk-free floor for LPs; it guarantees that only real outperformance is rewarded with performance fees for the GP. Once cumulative distributions clear the preferred return, the waterfall usually shifts to a catch-up or profit-sharing phase.

## The full explanation

In partnership structures like real estate syndications or private equity funds, profits are distributed according to a "waterfall." The preferred return constitutes a critical tier in this waterfall, usually Tier 2, following the return of invested capital (Tier 1).

The preferred return is expressed as a compound annual return (IRR). If the preferred return is 8%, the LPs must receive their initial capital back plus an 8% annualized return on that capital before the GP earns their "carry" or "promote."

### Why it exists
- **Downside Protection for LPs:** It ensures that LPs are compensated for the time value of their money and the baseline risk of the investment before the GP profits.
- **Incentive Alignment:** It acts as a "scorecard" for the GP. The GP is forced to focus on absolute value creation because they only get paid performance fees for outperforming the market baseline.
- **Fairness:** It separates standard returns (which investors could arguably get in passive index funds or standard real estate holding) from true active-manager value-add (alpha).

### Tiered Hurdles
Some agreements feature tiered hurdles. For example, a sponsor might earn 20% carry after an 8% preferred return is met, but the carry could escalate to 25% or 30% if performance exceeds a higher hurdle, like a 15% IRR or a certain multiple on invested capital.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling the preferred return tier in a waterfall, analysts must track cumulative distributions against cumulative contributions and the aggregate preferred return. You will need to calculate the compounding interest on the LP's unreturned capital balance using XIRR or a structured period-by-period calculation.

## Interview-ready answer

The preferred return, often called the hurdle rate, is the minimum annual return that Limited Partners must receive before the General Partner can start earning carried interest. It is typically set around 8% and serves to align GP incentives by ensuring they only get paid a performance fee when they generate returns above this baseline threshold.

## Pitfalls and gotchas

- **Compounding Methods:** Pay close attention to how the hurdle is compounded. An "annual" hurdle with no compounding method specified can lead to distribution disputes.
- **European vs. American Waterfalls:** In a European (whole-of-fund) waterfall, the hurdle applies to the entire fund's aggregate capital. In an American (deal-by-deal) structure, it applies on a per-deal basis, which allows GPs to take carry earlier but increases clawback risk.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Alter Domus - How Private Equity Waterfalls Work - Alter Domus]]
- [[Financial Modeling NYC - Private Equity Waterfall Models- European vs American Structures, Carry and Clawback]]
- [[SMB Investor Network - SMB Investment Glossary - Small Business Acquisition Terms - SMB Investor Network Resources]]