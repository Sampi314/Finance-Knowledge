# Forward Price with Cost of Carry Calculator - Full Model | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/forward-price-cost-carry-calculator

---

Forward Price with Cost of Carry Calculator
===========================================

Calculate Forward Price Including Benefits and Costs of Holding

Full cost of carry model for accurate forward pricing

Enter Values
------------

Spot Price (S₀) ?

$ 

Current market price of the asset

PV of Benefits (γ) ?

$ 

PV of dividends, coupons, convenience yield

PV of Costs (θ) ?

$ 

PV of storage, insurance, other costs

Risk-Free Rate (r) ?

 %

Annual risk-free interest rate

Time to Maturity (T) ?

 years

Time until contract expiration

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Cost of Carry Components

*   **Benefits (γ):** Dividends, coupons, convenience yield - reduces forward price
*   **Costs (θ):** Storage, insurance, spoilage - increases forward price
*   **Net Carry:** (S₀ - γ + θ) is the adjusted spot basis
*   **Compounding:** (1+r)^T accounts for financing costs

### Forward Price Results

Forward Price F₀(T) $103.95 Moderate Premium Normal forward premium with net cost of carry

Adjusted Spot $99.00

Net Carry Cost \-$1.00

Compound Factor 1.0500

Premium/Discount +$3.95

Premium % +3.95%

### Formula Breakdown

F₀(T) = (S₀ - γ + θ) × (1 + r)T

### Cost of Carry Interpretation

| Scenario | Effect on Forward | Typical Assets |
| --- | --- | --- |
| High Benefits (γ > θ) | Lower Forward | Dividend stocks, bonds |
| High Costs (θ > γ) | Higher Forward | Commodities, precious metals |
| No Carry (γ = θ = 0) | Basic F = S(1+r)^T | Non-dividend stocks |
| Convenience Yield | Backwardation | Oil, agricultural goods |

Understanding the Cost of Carry Model
-------------------------------------

### Video Explanation

Video: Forward Price with Cost of Carry Explained

### What is Cost of Carry?

Cost of carry is the total cost of holding a physical asset or financial position over time. It includes all costs and benefits associated with ownership until the forward contract matures. The full cost of carry model adjusts the basic forward pricing formula to account for these factors.

Full Cost of Carry Formula

F₀(T) = (S₀ - γ + θ) × (1 + r)T

### Cost of Carry Components

#### Benefits (γ) - Reduces Forward

Income from holding: **Dividends** (stocks), **Coupons** (bonds), **Convenience Yield** (commodities). Spot holder receives these while forward holder does not.

#### Costs (θ) - Increases Forward

Expenses of holding: **Storage** (warehousing), **Insurance** (protection), **Spoilage** (perishables). Spot holder pays these, forward holder avoids them.

**Present Value Adjustment:** Benefits and costs in the formula are expressed as present values. If you know future cash flows, discount them: PV = FV / (1+r)t.

### Arbitrage Relationship

The cost of carry model ensures no-arbitrage pricing. If the forward price differs from (S₀ - γ + θ)(1+r)T, traders can profit through:

*   **Cash-and-Carry:** Buy spot, sell forward if forward is too high
*   **Reverse Cash-and-Carry:** Sell spot, buy forward if forward is too low

**Note:** When γ = 0 and θ = 0, this reduces to the basic formula F = S(1+r)T. Use the full model when dividends, storage costs, or convenience yield are significant.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/forward-price-cost-carry-calculator-excel/)

Frequently Asked Questions
--------------------------

### What's the difference between γ and θ?

γ (gamma) represents benefits or income from holding the asset - things that make owning the spot position valuable. θ (theta) represents costs of holding - expenses incurred. Benefits reduce forward price; costs increase it. Net carry = θ - γ.

### Why use present values for costs and benefits?

Present values ensure all cash flows are measured at the same point in time (today). A $5 dividend paid in 6 months isn't worth $5 today - it's worth less. Using PV makes the formula mathematically consistent and reflects true economic value.

### What is convenience yield?

Convenience yield is the non-monetary benefit of holding physical inventory. For commodities, having physical stock provides security of supply, ability to meet unexpected demand, and operational flexibility. It's included in γ and can cause backwardation.

### How do I calculate PV of dividends?

For each expected dividend D paid at time t: PV = D / (1+r)^t. Sum all dividend PVs for the contract period. Example: $2 dividend in 6 months at 5% rate: PV = $2 / (1.05)^0.5 = $1.95. Enter this sum as γ.

### When does this model differ from basic forward pricing?

When γ = 0 and θ = 0, this reduces to the basic formula F = S(1+r)^T. Use the full model when: the asset pays dividends/coupons, storage costs are significant, or there's material convenience yield. For simple assets with no income or costs, basic pricing suffices.

### Why might forward price be less than spot?

Forward price can be less than spot (backwardation) when benefits exceed costs plus financing. High dividend yield stocks, bonds with large coupons, or commodities with strong convenience yield can all create backwardation. It's also possible with negative interest rates.

##### Disclaimer

This calculator is for educational purposes only. Forward prices depend on accurate estimates of benefits, costs, and rates. Actual market prices may differ due to liquidity, transaction costs, and market conditions. Consult a qualified professional for investment decisions.

Related Calculators
-------------------

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