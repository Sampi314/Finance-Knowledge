---
type: concept
title: "Stock vs cash consideration"
aliases: ["Cash vs stock consideration", "Mixed consideration"]
tags: ["m-and-a", "valuation", "modeling"]
difficulty: intermediate
prerequisites: ["[[Accretion dilution analysis]]", "[[Pro forma combined model]]", "[[Purchase price]]"]
related: ["[[Synergies revenue and cost]]"]
sources: ["[[CFI - Cash Consideration - Definition, How it Works, Limits]]", "[[IB Interview Questions - How to Build a Merger Model (Beginner Guide)]]", "[[IB Interview Questions - Understanding Accretion-Dilution Analysis- Step-by-Step Guide]]"]
status: draft
updated: 2026-04-14
---

# Stock vs cash consideration

> **TL;DR.** In an M&A transaction, stock consideration uses the acquirer's shares as payment while cash consideration uses cash (from existing balances or new debt), each carrying different implications for earnings dilution, capital structure, and taxation.

## When you'd use this

You encounter this decision when structuring an M&A deal and determining how to pay the purchase price. The mix of stock versus cash consideration directly impacts whether the transaction will be accretive or dilutive to the acquirer's earnings per share (EPS). The choice also affects the acquirer's balance sheet flexibility and the tax treatment for the target's shareholders.

## The 30-second version

Cash consideration involves paying for a target company using existing cash reserves or newly issued debt. It generally leads to higher EPS accretion because no new shares are issued to dilute existing owners, but it depletes liquidity or increases leverage. Stock consideration involves issuing new shares of the acquirer to the target's shareholders. This avoids depleting cash or increasing debt but creates ownership dilution, meaning existing earnings must be spread across a larger share count. A mixed consideration uses a combination of both to balance these trade-offs.

## The full explanation

When acquiring a company, the buyer is essentially purchasing its future earnings stream. The payment method determines the ultimate impact on the combined company's financial profile.

**Cash Consideration**
Paying with existing cash is often the most accretive financing method because it does not create any share dilution and avoids new interest expenses. However, it results in the loss of foregone interest income on that cash. If cash is raised through new debt, the deal remains accretive as long as the after-tax cost of debt is lower than the target's earnings yield. The downside is that paying in cash depletes balance sheet liquidity and, if debt-funded, increases financial risk and leverage. Furthermore, for the seller, receiving cash is an immediate taxable event.

**Stock Consideration**
Paying with stock involves dividing the stock consideration value by the acquirer's share price to determine the number of new shares issued. This method preserves cash and balance sheet flexibility, leaving the combined company with lower leverage. However, it dilutes the ownership of existing shareholders. If the acquirer issues new stock to buy earnings at a higher multiple than its own stock trades at, the deal will be dilutive to EPS. On the positive side for sellers, stock-for-stock transactions can often be structured as tax-deferred reorganizations, meaning taxes are only paid when the newly acquired shares are eventually sold.

**Mixed Consideration**
Many deals use a mix of both stock and cash. This allows the acquirer to optimize the trade-off between maximizing EPS accretion (via cash/debt) and preserving balance sheet health (via stock), while tailoring the offer to the target shareholders' tax and liquidity preferences.

## Formula

New shares issued for stock consideration:
$$ \text{New Shares} = \frac{\text{Stock Consideration Value}}{\text{Acquirer Share Price}} $$

## Worked example

Assume an acquirer is purchasing a target for a total equity purchase price of $2.5 billion. The deal structure is 60% cash and 40% stock.

- **Cash consideration:** $2.5B \times 60\% = \$1.5B$
- **Stock consideration:** $2.5B \times 40\% = \$1.0B$

If the acquirer's stock trades at $50 per share, the acquirer will issue 20 million new shares ($1.0B / $50) to the target's shareholders to cover the stock portion of the consideration.

## Excel and modeling notes

When building a merger model, you must carefully calculate the new shares issued based on the stock consideration amount and the acquirer's current share price. For the cash portion, ensure you link the reduction in interest income (from cash used) or the increase in interest expense (from newly issued debt) to the pro forma income statement, applying the appropriate tax rate to find the after-tax impact.

## Interview-ready answer

The key differences between stock and cash consideration center on dilution, leverage, and taxes. Cash consideration is generally more accretive to EPS because it avoids share dilution, but it depletes liquidity or increases debt. Stock consideration preserves cash and balance sheet flexibility but dilutes existing shareholders. Additionally, cash payments are immediately taxable for sellers, while stock transactions can often be structured to defer taxes.

## Pitfalls and gotchas

- Miscounting shares by using an incorrect stock price or failing to calculate the exact number of new shares issued.
- Forgetting to account for the foregone interest income on the cash used for cash consideration in a merger model.
- Assuming an all-stock deal is always dilutive or an all-cash deal is always accretive; the ultimate EPS impact depends on relative P/E multiples, cost of debt, and synergies.

## Sources

- [[CFI - Cash Consideration - Definition, How it Works, Limits]]
- [[IB Interview Questions - How to Build a Merger Model (Beginner Guide)]]
- [[IB Interview Questions - Understanding Accretion-Dilution Analysis- Step-by-Step Guide]]