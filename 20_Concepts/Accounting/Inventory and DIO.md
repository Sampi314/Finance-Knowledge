---
type: concept
title: "Inventory and DIO"
aliases: ["Days Inventory Outstanding"]
tags: ["accounting", "working capital", "turnover", "liquidity"]
difficulty: beginner
prerequisites: ["[[COGS and gross margin]]", "[[Working capital]]"]
related: ["[[Accounts payable and DPO]]", "[[Accounts receivable and DSO]]"]
sources: ["[[Quantus Finance - Working Capital Metrics Cheat Sheet (DSO, DPO, DIO) + 3‑Statement Forecasts]]", "[[Wall Street Prep - Days Inventory Outstanding (DIO) - Formula + Calculator]]"]
status: draft
updated: 2026-04-11
---

# Inventory and DIO

> **TL;DR.** Days Inventory Outstanding (DIO) measures the average number of days it takes for a company to turn its inventory into sales.

## When you'd use this

You look at Days Inventory Outstanding (DIO) or inventory turnover when assessing a company's operational efficiency, liquidity, and product demand. Lower DIO suggests the business is efficiently selling its goods, avoiding stockpiles, and freeing up cash flow. Higher DIO might indicate weak sales, obsolete products, or poor inventory management. It is a critical component for forecasting working capital and calculating a company's cash conversion cycle.

## The 30-second version

Days Inventory Outstanding (DIO) represents the average time a company holds its inventory before selling it. To calculate DIO, you divide average inventory by Cost of Goods Sold (COGS) and multiply the result by 365 days. A shorter DIO means inventory is selling quickly, turning over into revenue and boosting cash flow. Conversely, a longer DIO suggests inventory is lingering, which ties up capital and may hint at pricing issues, lagging demand, or obsolescence.

## The full explanation

**What is DIO?**
Days Inventory Outstanding (DIO) tracks the time it takes to cycle through inventory on hand. Since inventory purchases tie up a company’s cash (which hurts free cash flow), converting that inventory into sales as quickly as possible is generally optimal.

**DIO vs. Inventory Turnover**
While DIO is measured in days, **Inventory Turnover** measures how many times the company cycles through its inventory balance over a period (usually a year). The two metrics are two sides of the same coin:
- High inventory turnover equals a low DIO.
- Low inventory turnover equals a high DIO.

**Why DIO Matters**
1. **Cash Flow Impact:** Inventory requires cash. If it sits on shelves, the business’s cash is tied up. If sold rapidly (low DIO), the business converts inventory into cash, improving liquidity.
2. **Operational Efficiency:** Low DIO signals strong customer demand, effective sales strategies, and "just-in-time" inventory practices.
3. **Risk of Obsolescence:** If the DIO is exceptionally high compared to industry peers, a company risks holding outdated or expired goods, potentially leading to inventory write-downs.

**What is a "Good" DIO?**
There is no universal "good" DIO, as it varies widely by industry. For instance, a grocery store selling perishable goods will naturally have a much lower DIO than a heavy machinery manufacturer. To effectively use DIO, you should benchmark a company against its direct competitors and historical performance.

## Formula

![[Days Inventory Outstanding (DIO)]]

## Worked example

(none)

## Excel and modeling notes

When forecasting a 3-statement financial model, future inventory balances are typically projected by making an assumption for future DIO or inventory turnover. If you assume a DIO of 45 days, and you've already projected the COGS for the year, you can forecast the ending inventory balance:
`Ending Inventory = (Projected COGS / 365) * Assumed DIO`

Additionally, comparing changes in inventory period-over-period will give you the impact on operating cash flow (an increase in inventory is a use of cash).

## Interview-ready answer

Days Inventory Outstanding (DIO) measures how many days it takes for a company to sell its inventory. A lower DIO implies higher operational efficiency and stronger cash flows, as capital isn't trapped in unsold goods. Conversely, a high DIO could suggest an inability to sell products, risking obsolescence or write-downs.

## Pitfalls and gotchas

- **Industry specifics:** Always compare a company’s DIO against peers within the exact same industry. Retail operations and heavy equipment manufacturers cannot be compared directly using DIO.
- **Supply chain shocks:** A very low DIO is usually positive, but if it approaches zero, the business may be at risk of stockouts and lost sales if demand surges unexpectedly.
- **Average vs. Ending:** DIO can be calculated using either ending inventory or average inventory. Using the average is usually preferred to account for seasonality, but be consistent across comparisons.

## Sources

- [[Quantus Finance - Working Capital Metrics Cheat Sheet (DSO, DPO, DIO) + 3‑Statement Forecasts]]
- [[Wall Street Prep - Days Inventory Outstanding (DIO) - Formula + Calculator]]
