# Forward Value at Time t Calculator - Mark-to-Market Valuation | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/forward-value-time-t-calculator

---

Forward Value at Time t Calculator
==================================

Calculate the Mark-to-Market Value of a Forward Contract

Value forward contracts before expiration using present value of delivery price

Enter Values
------------

Position Type

 Long  Short

Long: obligated to buy | Short: obligated to sell

Current Spot Price (St) ?

$ 

Current market price of the asset

Delivery Price (K) ?

$ 

Contracted delivery price (equals F₀(T) at inception)

Risk-Free Rate (r) ?

 %

Annual risk-free interest rate

Time Remaining (T - t) ?

 years

Time until contract expiration

Contract Size ?

 units

Number of units per contract

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Key Concepts

*   **Mark-to-Market:** Current value of existing contract
*   **PV(K):** Present value of delivery price obligation
*   **Long Value:** St - PV(K) (benefits from price increases)
*   **Short Value:** PV(K) - St (benefits from price decreases)

### Forward Value Results

Contract Value (Vt) +$5.44 In-the-Money Favorable position with positive mark-to-market value

Value Per Unit +$5.44

PV of Delivery $102.56

Discount Factor 0.9768

Value as % of Spot +5.04%

### Formula Breakdown

Vt(T) = St - K(1 + r)\-(T-t) (Long Position)

### Mark-to-Market Interpretation

| Scenario | Long Position | Short Position |
| --- | --- | --- |
| St > PV(K) | In-the-Money (+) | Out-of-the-Money (-) |
| St = PV(K) | At-the-Money (0) | At-the-Money (0) |
| St < PV(K) | Out-of-the-Money (-) | In-the-Money (+) |

Understanding Forward Contract Valuation
----------------------------------------

### What is Mark-to-Market Value?

Mark-to-market (MTM) value represents what a forward contract is worth at any point before expiration. Unlike at expiration where value is simply ST - K, before expiration we must account for the time value of the delivery price by discounting K back to present value.

Forward Value at Time t (Long)

Vt(T) = St - K(1 + r)\-(T-t)

**K = F₀(T) at Inception:** The delivery price K is set equal to the forward price F₀(T) when the contract is initiated, making the initial contract value zero. Once established, K remains fixed while market forward prices change, causing the contract to gain or lose value.

### Why Discount the Delivery Price?

The delivery price K won't be paid until maturity. To compare it fairly with today's spot price St, we must calculate its present value: PV(K) = K(1+r)\-(T-t). This makes both values comparable at the same point in time.

### Long vs. Short Position Formulas

#### Long Forward

Vt = St - K(1+r)\-(T-t). You're entitled to buy at K but can currently sell at St. The value is what you could "lock in" by entering an offsetting short.

#### Short Forward

Vt = K(1+r)\-(T-t) - St. You're obligated to sell at K but must buy at St. Short has opposite value to long - what one gains, the other loses.

**Zero-Sum Nature:** Forward contracts are zero-sum: Vlong + Vshort = 0. At inception, both parties agree to terms that make the contract worthless (fair deal). As prices move, value transfers between parties but the sum remains zero.

### Closing Out Positions

The MTM value represents what you'd receive (or pay) to close out your position early. You can offset a long by entering a new short at current forward prices, or vice versa. The net cash flow equals the MTM value.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/forward-value-time-t-calculator-excel/)

Frequently Asked Questions
--------------------------

### How does this differ from value at expiration?

At expiration (t = T), the discount factor equals 1, so PV(K) = K. The formula becomes VT = ST - K, which is the expiration payoff. Before expiration, we discount K to reflect that payment isn't due yet.

### Why does time remaining affect value?

More time means more discounting of K. With longer time remaining, PV(K) is lower, making long positions more valuable and short positions less valuable, all else equal. As expiration approaches, PV(K) converges to K.

### What if time remaining is zero?

When T - t = 0, the discount factor is (1+r)^0 = 1, so PV(K) = K. The formula becomes the expiration value: V = ST - K for long, V = K - ST for short. This is why we call it the "value at time t" - it works for any t including T.

### How do interest rate changes affect value?

Higher rates mean more discounting, so PV(K) decreases. For long positions, lower PV(K) increases value. For short positions, lower PV(K) decreases value. This interest rate sensitivity is greater with longer time remaining.

### Can I use this for futures contracts?

Futures are marked-to-market daily with cash settlements, so they always have zero value after settlement. This formula is for forwards which accumulate value until expiration without intermediate cash flows. However, the economics are similar.

### What about cost of carry adjustments?

This basic formula assumes no dividends, storage costs, or convenience yield. For assets with cost of carry, the spot price St should be replaced with the adjusted spot (St - PV of remaining benefits + PV of remaining costs).

##### Disclaimer

This calculator is for educational purposes only. Actual forward contract values may differ due to credit risk, liquidity, transaction costs, and market conventions. Consult a qualified professional for trading decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Forward Price Cost Carry Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Price Cost Carry Calculator\
\
Calculate forward prices including storage costs, income yields, and convenience yields. Apply the full cost...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-price-cost-carry-calculator/)

[![Professional finance illustration representing Forward Value Expiration Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Value Expiration Calculator\
\
Calculate the value of a forward contract at expiration. Determine the payoff for long and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-value-expiration-calculator/)

[![Professional finance illustration representing Forward Price Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Price Calculator\
\
Calculate theoretical forward prices for financial assets using the cost of carry model. Determine fair...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-price-calculator/)

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