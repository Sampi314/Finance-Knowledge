# Forward Price Calculator - Calculate F₀(T) = S₀(1+r)^T | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/forward-price-calculator

---

Forward Price Calculator
========================

Calculate the Theoretical Forward Price Using Cost of Carry

Essential for understanding no-arbitrage forward pricing

Enter Values
------------

Spot Price (S₀) ?

$ 

Current market price of the asset

Risk-Free Rate (r) ?

 %

Annual rate (discrete compounding)

Time to Maturity (T) ?

 years

Time until contract expiration

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Understanding Forward Pricing

*   **No-Arbitrage:** Forward price prevents risk-free profit
*   **Contango:** F > S (forward premium when r > 0)
*   **Backwardation:** F < S (rare, typically with benefits)
*   **Convention:** Uses discrete annual compounding

### Forward Price Result

Forward Price F₀(T) $105.00 Moderate Premium Normal forward premium due to cost of carry

Premium/Discount +$5.00

Premium % +5.00%

Compound Factor 1.0500

### Formula Breakdown

F₀(T) = S₀ × (1 + r)T

### Understanding the Result

#### Forward Premium

When F > S, the forward is at a **premium** (contango). This reflects the cost of financing the asset purchase. Holding an asset has opportunity cost equal to the risk-free rate.

#### No-Arbitrage Pricing

The forward price is determined by no-arbitrage. If F ≠ S₀(1+r)^T, arbitrageurs can earn risk-free profits through cash-and-carry or reverse cash-and-carry strategies.

#### Forward Premium/Discount Guide

| Premium % | Status | Interpretation |
| --- | --- | --- |
| \> 10% | High Premium | Strong contango (high rates or long maturity) |
| 5% to 10% | Moderate Premium | Normal forward premium |
| 0% to 5% | Low Premium | Minimal time value |
| \-5% to 0% | Low Discount | Slight backwardation |
| < -5% | High Discount | Strong backwardation (negative rates) |

Understanding Forward Pricing
-----------------------------

### Video Explanation

Video: Forward Price Explained

### What is a Forward Price?

The **forward price** is the delivery price that makes a forward contract have zero initial value. It's determined by no-arbitrage pricing:

Key Formula

F₀(T) = S₀ × (1 + r)T

*   **Cost of Carry:** The forward premium reflects the financing cost of holding the asset
*   **No Upfront Payment:** Unlike buying the asset directly, entering a forward costs nothing initially

**Compounding Convention:** This calculator uses discrete (annual) compounding as per CFA curriculum standards. The continuous compounding formula F = S₀ × erT gives similar results for short maturities.

### The No-Arbitrage Argument

Why does the forward price equal S₀(1+r)T? Consider these strategies:

*   **Cash-and-Carry:** Borrow $S₀, buy the asset, enter short forward at F. At expiration: sell asset for F, repay S₀(1+r)T. Profit = F - S₀(1+r)T.
*   **Reverse Cash-and-Carry:** Short sell the asset for S₀, invest at r, enter long forward at F. At expiration: receive S₀(1+r)T, buy asset at F, return to lender. Profit = S₀(1+r)T - F.

If F ≠ S₀(1+r)T, one of these strategies yields a risk-free profit, violating no-arbitrage.

### Contango vs. Backwardation

#### Contango (F > S)

Normal condition when r > 0. Forward price exceeds spot due to financing costs.

#### Backwardation (F < S)

Occurs when holding benefits (dividends, convenience yield) exceed financing costs.

**Note:** This basic model assumes no benefits (dividends, storage costs) from holding the asset. For assets with benefits or costs, use the full cost of carry model: F = (S₀ - Benefits + Costs) × (1+r)T.

### Relationship to Forward Value

1.  1
    
    ##### At Initiation
    
    Forward value = 0 (the forward price is chosen to make this true)
    
2.  2
    
    ##### During Life
    
    Value changes as spot moves: Vt = St - F₀(T)/(1+r)(T-t)
    
3.  3
    
    ##### At Expiration
    
    VT = ST - F₀(T) (no discounting needed)
    

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/forward-price-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a forward price?

The forward price is the delivery price set when a forward contract is initiated such that the contract has zero initial value. It represents the price at which the long position agrees to buy (and short agrees to sell) the asset at expiration. It's calculated as F₀(T) = S₀ × (1 + r)^T using the cost of carry model.

### How is forward price calculated?

The forward price is calculated using the cost of carry formula: F₀(T) = S₀ × (1 + r)^T, where S₀ is the current spot price, r is the risk-free rate, and T is time to maturity in years. This uses discrete compounding; the continuous version is F = S₀ × e^(rT).

### What is cost of carry in forward pricing?

Cost of carry refers to the costs (and benefits) of holding an asset until the forward expiration. The basic cost is the financing rate (opportunity cost of capital). The full model also includes storage costs, insurance, and potential benefits like dividends or convenience yield.

### What's the difference between forward price and future spot price?

The forward price is determined today by no-arbitrage pricing and is known with certainty. The future spot price (ST) is the actual market price at expiration, which is uncertain. They will generally differ - the forward price is not a prediction of the future spot price.

### Why is the risk-free rate used in forward pricing?

The risk-free rate is used because forward pricing is based on no-arbitrage arguments involving borrowing and lending. An arbitrageur can borrow/lend at the risk-free rate to construct cash-and-carry strategies. Using any other rate would allow risk-free arbitrage profits.

### What is contango and backwardation?

Contango occurs when the forward price exceeds the spot price (F > S), which is typical when the risk-free rate is positive. Backwardation occurs when F < S, which can happen with negative rates or when the convenience yield from holding the asset exceeds the financing cost.

##### Disclaimer

This calculator is for educational purposes only and does not constitute financial advice. Actual forward prices may differ due to transaction costs, market frictions, and asset-specific factors. Always consult with a qualified financial advisor.

Related Calculators
-------------------

[![Professional finance illustration representing Forward Price Cost Carry Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Price Cost Carry Calculator\
\
Calculate forward prices including storage costs, income yields, and convenience yields. Apply the full cost...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-price-cost-carry-calculator/)

[![Professional finance illustration representing Forward Value Time T Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Value Time T Calculator\
\
Calculate the mark-to-market value of a forward contract before expiration. Determine current contract value using...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-value-time-t-calculator/)

[![Professional finance illustration representing Forward Value Expiration Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Value Expiration Calculator\
\
Calculate the value of a forward contract at expiration. Determine the payoff for long and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-value-expiration-calculator/)

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