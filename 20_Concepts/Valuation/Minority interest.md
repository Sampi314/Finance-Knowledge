---
type: concept
title: "Minority interest"
aliases: ["Noncontrolling interest", "NCI"]
tags: ["Valuation", "accounting", "enterprise value"]
difficulty: beginner
prerequisites: ["[[Enterprise value]]"]
related: []
sources: ["[[CFI - Minority Interest in Enterprise Value Calculation]]", "[[CFI - What is a Non-Controlling Interest (NCI)? - Defined]]", "[[Macabacus - Noncontrolling (Minority) Interest - Examples, Templates]]"]
status: draft
updated: 2026-04-11
---

# Minority interest

> **TL;DR.** Minority interest (or noncontrolling interest) is the portion of a subsidiary's equity that is not owned by the parent company but is still consolidated into the parent's financial statements.

## When you'd use this

You need to understand minority interest when valuing a company using Enterprise Value multiples (like EV/EBITDA), analyzing consolidated financial statements where a parent owns between 50% and 100% of a subsidiary, or properly accounting for net income and equity attributable to non-controlling shareholders.

## The 30-second version

When a company owns more than 50% but less than 100% of another company, accounting rules require it to consolidate 100% of the subsidiary's financial results (revenue, expenses, assets, and liabilities) into its own statements. To adjust for the portion it doesn't actually own, it records a "minority interest" (or "noncontrolling interest") on its balance sheet under equity, and deducts the non-controlling share of net income on the income statement. When calculating Enterprise Value, minority interest must be added back so that EV aligns with consolidated metrics like EBITDA, which include 100% of the subsidiary's earnings.

## The full explanation

Minority interest, also known as noncontrolling interest (NCI), arises when one company (the parent) acquires a controlling stake—typically defined as owning more than 50% but less than 100%—in another company (the subsidiary).

Because the parent company exercises control, accounting standards (like US GAAP and IFRS) require the parent to fully consolidate the subsidiary's financials. This means the parent company's financial statements will report 100% of the subsidiary's revenue, expenses, assets, and liabilities, despite the parent only owning a fractional share.

To correct for this overstatement of ownership, two primary adjustments are made:
1. **On the Income Statement:** Consolidated net income is split into the portion attributable to the parent company's shareholders and the portion attributable to the noncontrolling interests (the minority shareholders).
2. **On the Balance Sheet:** The parent company records a line item for noncontrolling interest within the shareholders' equity section. This represents the book value of the subsidiary's equity that the parent does not own.

When valuing a company, noncontrolling interest plays a critical role in calculating Enterprise Value (EV). EV is considered the total value of a company's core business available to all investors (both debt and equity). Because valuation multiples like EV/EBITDA use EBITDA in the denominator—which, due to consolidation, includes 100% of the subsidiary's earnings—the numerator (EV) must also reflect 100% of the subsidiary's value to ensure an "apples-to-apples" comparison. Therefore, the value of the minority interest is added to EV.

## Formula

The inclusion of minority interest in Enterprise Value is represented as:

$$ Enterprise Value = Equity Value + Total Debt + Preferred Stock + Minority Interest - Cash $$

## Worked example

(none)

## Excel and modeling notes

When building a three-statement model or a valuation model, ensure that noncontrolling interest is correctly projected. On the income statement, net income attributable to NCI should be subtracted to arrive at net income available to common shareholders. On the balance sheet, NCI should be tracked as a separate equity account. In an M&A context or purchase price allocation (PPA), remember that under modern accounting rules (like FAS 141r), 100% of the acquired net assets are recorded at fair value, which can result in goodwill attributable to both the acquirer and the noncontrolling interest.

## Interview-ready answer

If asked why minority interest is added to Enterprise Value, you can say: "When a parent company owns more than 50% but less than 100% of a subsidiary, it must consolidate 100% of the subsidiary's financials. As a result, metrics like EBITDA include 100% of the subsidiary's earnings. To ensure an apples-to-apples comparison in multiples like EV/EBITDA, we must add the value of the minority interest we don't own into Enterprise Value so that the numerator and denominator both reflect 100% of the subsidiary."

## Pitfalls and gotchas

- Failing to add minority interest to Enterprise Value when using consolidated EBITDA, leading to a mismatched valuation multiple.
- Misinterpreting the noncontrolling interest line item on the balance sheet as a liability instead of equity.
- Overlooking the fact that the NCI value on the balance sheet is usually a book value, while for EV calculations, the market value of the minority interest should ideally be used if it's available.

## Sources

- [[CFI - Minority Interest in Enterprise Value Calculation]]
- [[CFI - What is a Non-Controlling Interest (NCI)? - Defined]]
- [[Macabacus - Noncontrolling (Minority) Interest - Examples, Templates]]
