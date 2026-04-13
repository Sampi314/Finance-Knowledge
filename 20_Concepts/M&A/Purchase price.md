---
type: concept
title: "Purchase price"
aliases: ["Purchase Price Allocation", "PPA"]
tags: ["m-and-a", "accounting", "valuation"]
difficulty: intermediate
prerequisites: ["[[M&A overview]]", "[[The balance sheet]]"]
related: ["[[Accretion dilution analysis]]"]
sources: ["[[IB Interview Questions - Purchase Price Allocation in M&A Accounting Explained]]"]
status: draft
updated: 2026-04-13
---

# Purchase price

> **TL;DR.** Purchase price allocation (PPA) is the accounting process of assigning the total consideration paid in an acquisition to the individual assets acquired, liabilities assumed, and any residual goodwill.

## When you'd use this

You would use purchase price allocation whenever a company completes an acquisition or business combination. It is required under ASC 805 to determine how the purchase consideration affects the acquirer's balance sheet and future income statements.

## The 30-second version

When one company buys another, it doesn't just add the target's old book values to its own balance sheet. Instead, the acquirer must record all acquired tangible and intangible assets and assumed liabilities at their current fair market values as of the acquisition date. Any purchase consideration paid above the net fair value of these identifiable assets and liabilities is recorded as goodwill. This process directly impacts future earnings because the newly stepped-up assets and identified intangibles must be depreciated or amortized over time.

## The full explanation

Purchase price allocation (PPA) is an essential accounting exercise under ASC 805 (Business Combinations). The standard requires the acquisition method, meaning all assets and liabilities are marked to their fair value. This creates a "fresh start" balance sheet rather than simply carrying over historical costs.

The process generally involves:
1. **Tangible Assets:** Adjusting property, plant, equipment, and inventory to their fair values. Since fair value usually exceeds depreciated book value, this increases the asset base and leads to higher future depreciation expense.
2. **Intangible Assets:** Identifying and separately valuing intangibles like customer relationships, technology, trademarks, and patents. These are typically valued using an income approach (like the Multi-Period Excess Earnings Method) and are then amortized over their useful lives (e.g., 3-15 years), creating ongoing non-cash expenses.
3. **Liabilities:** Marking assumed debt and contingent liabilities to fair value. Notably, deferred revenue is often written down to its fulfillment cost plus a reasonable profit, creating a temporary "revenue haircut" post-acquisition.
4. **Goodwill:** The residual amount paid over the net identifiable assets. Goodwill is not amortized but must be tested annually for impairment. High goodwill often indicates an asset-light target where value resides in assembled workforce or expected synergies.

PPA creates immediate balance sheet changes and significant income statement impacts, primarily through the new depreciation and amortization expenses which reduce reported net income (leading to the use of "adjusted earnings").

## Formula

Goodwill = Purchase Consideration - Fair Value of Net Identifiable Assets

Where:
Fair Value of Net Identifiable Assets = Tangible Assets + Intangible Assets - Liabilities Assumed

## Worked example

Consider an acquisition with $500 million total consideration:

- **Identified Assets at Fair Value:** Cash ($30M) + Inventory ($40M) + PP&E ($80M) + Customer relationships ($100M) + Technology ($50M) + Trademark ($25M) = $325 million total assets.
- **Assumed Liabilities at Fair Value:** Accounts payable ($20M) + Debt assumed ($50M) + Deferred revenue ($15M) = $85 million total liabilities.

Net Identifiable Assets = $325M - $85M = $240 million.
Goodwill = $500M - $240M = $260 million.

## Excel and modeling notes

In a merger model, you must account for PPA by creating schedules for the new depreciation on written-up tangible assets and the amortization of newly identified intangible assets. This amortization expense makes the transaction more dilutive in an accretion/dilution analysis, so sensitizing PPA assumptions (e.g., assuming $50M vs $100M in intangibles) is critical when evaluating deals.

## Interview-ready answer

[[Walk me through purchase price allocation]]

## Pitfalls and gotchas

- Forgetting that deferred revenue is written down to fair value during an acquisition, which artificially lowers recognized revenue in the post-closing periods.
- Assuming all intangibles are amortized; goodwill and certain indefinite-lived trademarks are not amortized but are instead tested for impairment.
- Failing to realize that the measurement period for PPA can last up to a year, causing early post-acquisition financial statements to be provisional and potentially restated.

## Sources

- [[IB Interview Questions - Purchase Price Allocation in M&A Accounting Explained]]
