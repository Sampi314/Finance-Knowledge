# Forward Value at Expiration Calculator - Calculate Forward Payoff | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/forward-value-expiration-calculator

---

Forward Value at Expiration Calculator
======================================

Calculate the Payoff of a Forward Contract at Maturity

Essential for understanding forward contract settlement

Enter Values
------------

Position Type ?

 Long  Short

Long receives the asset, Short delivers the asset

Spot Price at Expiration (ST) ?

$ 

Market price of the asset at expiration

Delivery Price (K) ?

$ 

Contract price from original agreement

Contract Size ?

 units

Number of units in the contract

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Understanding Forward Value

*   **Long Position:** V = ST - K (profit when spot rises)
*   **Short Position:** V = K - ST (profit when spot falls)
*   **Zero-Sum:** Long's gain = Short's loss
*   **At Initiation:** K is set so initial value = 0

### Forward Value at Expiration

Value per Unit +$5.00 Small Profit Modest gain on the forward position

Total Contract Value +$5.00

Value as % of K +4.76%

### Formula Breakdown

VT(T) = ST - K

### Understanding the Result

#### What This Means

At expiration, the forward contract's value equals the difference between the spot price and the delivery price. A positive value means profit for the long position (loss for short), while negative means loss for long (profit for short).

#### Settlement

Forwards can settle via physical delivery (exchange of asset for cash) or cash settlement (payment of the net value). Either way, the economic result is the same: VT = ST - K for long positions.

#### Value Interpretation Guide

| Value as % of K | Result | Interpretation |
| --- | --- | --- |
| \> 10% | Large Profit | Significant favorable move |
| 5% to 10% | Moderate Profit | Good return on position |
| 0% to 5% | Small Profit | Modest gain |
| \-5% to 0% | Small Loss | Minor adverse move |
| < -5% | Large Loss | Significant adverse move |

Understanding Forward Contract Value at Expiration
--------------------------------------------------

### What is Forward Contract Value at Expiration?

At expiration, a forward contract's value is simply the difference between the current spot price (ST) and the delivery price (K) agreed upon when the contract was initiated. This is the **payoff** or **terminal value** of the forward contract.

Forward Value at Expiration

VT = ST - K

**Key Insight:** Forward contracts are zero-sum games. The long position's gain exactly equals the short position's loss, and vice versa. The total value across both positions always sums to zero.

### Long vs. Short Positions

#### Long Forward

Agrees to **BUY** the asset at delivery price K. Value: VT = ST - K. Profits when spot rises above K.

#### Short Forward

Agrees to **SELL** the asset at delivery price K. Value: VT = K - ST. Profits when spot falls below K.

At contract initiation, K is set so that the forward has zero initial value to both parties. K is typically the forward price F₀(T) = S₀ × (1+r)T based on the cost of carry model.

### Settlement Methods

Forward contracts can be settled in two ways, both economically equivalent:

*   **Physical Delivery:** The short delivers the asset, long pays K. If ST > K, long receives an asset worth more than they paid.
*   **Cash Settlement:** The party with negative value pays the absolute value to the other party. No asset changes hands.

**Caution:** Unlike exchange-traded futures, forwards typically have no daily mark-to-market and carry counterparty credit risk. The losing party must be able to pay at expiration.

### Relationship to Forward Pricing

*   **At initiation (t=0):** K is set equal to the forward price F₀(T), making initial value = 0
*   **Before expiration:** Value depends on current forward price vs. delivery price (discounted)
*   **At expiration (t=T):** Value is simply ST - K (no discounting needed)

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/forward-value-expiration-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is forward contract value at expiration?

At expiration, a forward contract's value is the difference between the spot price (ST) and the delivery price (K). For long positions: V = ST - K. For short positions: V = K - ST. This represents the profit or loss on the position, also called the payoff or terminal value.

### How do long and short positions affect value?

Long positions profit when the spot price exceeds the delivery price (ST > K), while short positions profit when the delivery price exceeds spot (K > ST). The two positions are mirror images: if long gains $5, short loses $5. This zero-sum nature is fundamental to forward contracts.

### What happens when spot exceeds the delivery price?

When ST > K, the long position holder can buy the asset at K (the agreed delivery price) when it's worth ST in the market. They profit by the difference (ST - K). Conversely, the short must sell at K when they could get ST in the market, losing (ST - K).

### Is forward value the same as profit?

At expiration, yes - the forward contract value equals the profit or loss. Before expiration, the mark-to-market value represents unrealized P&L. Note that forward contracts typically have zero initial value (no premium paid), so the terminal value is the entire profit or loss.

### How does contract size affect total value?

Total contract value = Value per unit × Contract size. If the value per unit is $5 and you have a contract for 100 units, total value is $500. Contract size scales both profits and losses proportionally without affecting the per-unit economics.

### What about settlement vs. delivery?

Forward contracts can settle via physical delivery (actual exchange of asset for payment K) or cash settlement (payment of the net value). Both methods produce the same economic result. Physical delivery: long pays K, receives asset worth ST, net gain = ST - K. Cash settlement: long receives ST - K directly.

##### Disclaimer

This calculator is for educational purposes only and does not constitute financial advice. Forward contracts involve significant risk, including counterparty credit risk. Always consult with a qualified financial advisor before entering derivative contracts.

Related Calculators
-------------------

[![Professional finance illustration representing Forward Value Time T Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Value Time T Calculator\
\
Calculate the mark-to-market value of a forward contract before expiration. Determine current contract value using...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-value-time-t-calculator/)

[![Professional finance illustration representing Forward Price Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Price Calculator\
\
Calculate theoretical forward prices for financial assets using the cost of carry model. Determine fair...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-price-calculator/)

[![Professional finance illustration representing Holding Period Return Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Holding Period Return Calculator\
\
Calculate holding period return for any investment over a given time frame. Measure total return...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/holding-period-return-calculator/)

Contact Me
----------

Have a question or want to work together? Fill out the form below and we’ll get back to you as soon as possible.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20378'%3E%3C/svg%3E)

Contact Form Demo

First Name

Last Name

Email

Subject

Your Message

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy)
 and [Terms of Service](https://policies.google.com/terms)
 apply.

Submit Form