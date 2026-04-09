# Credit Default Swap (CDS) Calculator: Spread, Premium & Default Probability | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/cds-calculator

---

Credit Default Swap (CDS) Calculator
====================================

Constant Hazard Rate Pricing Model

Calculate CDS premiums, implied default probabilities, and PV of protection & premium legs

Embed This Calculator

Enter Values
------------

Notional Amount ?

$ 

Face value of reference obligation

CDS Spread ?

 bps

Annual premium in basis points

Recovery Rate (R) ?

 %

Standard: 40% for senior unsecured debt

Risk-Free Rate ?

 %

Continuously compounded risk-free rate

CDS Tenor ?

 years

Contract duration — \= 20 payment periods

Payment Frequency ? Quarterly Semi-Annual Annual

Reset to Defaults

##### CDS Pricing Formulas

λ = s / (1 − R)

Q(t) = e−λt  |  PD(T) = 1 − e−λT

**λ** = Hazard rate | **s** = Spread | **R** = Recovery | **Q** = Survival prob

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### CDS Pricing Results

Annual CDS Premium \--

Periodic Premium \--

Implied Hazard Rate (Risk-Neutral) \--

Cumulative Default Prob (Risk-Neutral) \--

Survival Probability \--

Loss Given Default (LGD) \--

Credit Quality (Rule of Thumb) \--

##### Present Value of CDS Legs

PV Premium Leg \--

PV Protection Leg \--

Breakeven Spread (approx.) \--

### Payment Schedule Breakdown

| Period | ti (yrs) | Δt  | Q(ti) | DF(ti) | PV Prem ($) | PV Prot ($) |
| --- | --- | --- | --- | --- | --- | --- |

### Formula Breakdown

λ = s / (1 − R)   |   Q(t) = e−λt

Step-by-step calculation with your inputs

##### Model Assumptions

*   Constant hazard rate (time-homogeneous default intensity)
*   Recovery rate is fixed and known at contract inception
*   Risk-free rate is constant across all maturities (flat term structure)
*   Defaults occur uniformly within each period (midpoint approximation)
*   No counterparty risk (protection seller always pays)
*   Continuous discounting: DF(t) = e−rt
*   No accrued premium payment at default

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Credit Default Swaps
----------------------------------

### What Is a Credit Default Swap?

A **credit default swap (CDS)** is a derivative contract that transfers credit risk from one party to another. The **protection buyer** makes periodic premium payments (the CDS spread) to the **protection seller**. In return, if the reference entity defaults, the seller compensates the buyer for the loss.

CDS contracts function like insurance against default. They are the most widely traded credit derivatives and play a central role in credit markets for hedging, speculation, and price discovery.

Implied Hazard Rate (Hull Ch. 25)

λ = s / (1 − R)  
Where s = CDS spread (decimal), R = recovery rate, λ = constant hazard rate

### How CDS Pricing Works

CDS pricing equates the present value of two legs:

*   **Premium Leg**: The PV of periodic spread payments, weighted by survival probability
*   **Protection Leg**: The PV of the expected default payment, (1 − R) × Notional

At the fair spread, PV(Premium Leg) = PV(Protection Leg). The implied hazard rate λ = s/(1−R) makes this equality hold in continuous time.

PV of CDS Legs

PVpremium = s × N × Σ \[Δt × Q(ti) × DF(ti)\]  
PVprotection = (1−R) × N × Σ \[(Q(ti−1) − Q(ti)) × DF(tmid)\]  
Where Q(t) = e−λt is survival probability, DF(t) = e−rt is discount factor

### Practical Applications

*   **Hedging**: Bond holders buy CDS protection to hedge credit exposure without selling the bond
*   **Speculation**: Traders buy protection on entities they believe will deteriorate (naked CDS)
*   **Relative Value**: Exploit mispricings between CDS spreads and bond credit spreads (basis trades)
*   **Credit Indices**: CDX and iTraxx indices provide diversified credit exposure via standardized CDS baskets

**Note:** The implied default probabilities from this model are **risk-neutral** probabilities used for pricing, not real-world default frequencies. Real-world default rates are typically lower because CDS spreads include a risk premium.

Credit Default Swaps Explained
------------------------------

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/cds-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a credit default swap (CDS)?

A credit default swap (CDS) is a derivative contract that transfers credit risk from the protection buyer to the protection seller. The buyer makes periodic premium payments (the CDS spread) and in return receives a payment if the reference entity defaults. It functions like insurance against a bond issuer defaulting on its obligations.

### How is the implied default probability calculated from a CDS spread?

The implied risk-neutral hazard rate (λ) is derived from the CDS spread using λ = s / (1 − R), where s is the spread in decimal form and R is the recovery rate. The cumulative risk-neutral default probability over T years is PD(T) = 1 − e−λT. These are risk-neutral probabilities used for pricing, not real-world default frequencies. Real-world default rates are typically lower.

### What is the recovery rate and why does it matter?

The recovery rate (R) represents the fraction of the notional amount recovered in default. The standard assumption is 40% for senior unsecured debt. A higher recovery rate means a lower loss given default but implies a higher hazard rate for the same CDS spread, since λ = s/(1−R). The recovery rate directly determines the protection leg payout: (1 − R) × Notional.

### What is the difference between buying and selling CDS protection?

The protection buyer pays periodic premiums and profits if the reference entity defaults (similar to buying insurance). The protection seller receives premiums and must pay (1 − R) × Notional if default occurs (similar to selling insurance). Buying protection is a bearish bet on credit quality, while selling protection is a bullish bet.

### How are CDS spreads quoted?

CDS spreads are quoted in basis points (bps) per year. For example, a 200 bps spread on a $10 million notional means the protection buyer pays $200,000 per year, typically in quarterly installments of $50,000. Wider spreads indicate higher perceived credit risk. The 5-year tenor is the most liquid benchmark.

### What is the CDS-bond basis?

The CDS-bond basis is the difference between the CDS spread and the bond's credit spread (z-spread). In theory, they should be equal, but in practice the basis can be positive or negative due to funding costs, counterparty risk, delivery options, and market segmentation. Traders may exploit persistent basis differences through basis trades.

##### Disclaimer

This calculator is for educational purposes only. It uses a constant hazard rate model with simplifying assumptions including flat term structure, fixed recovery rate, and no counterparty risk. Real-world CDS pricing uses term structures of hazard rates, market-implied recovery rates, and accounts for accrued premiums. This tool should not be used for trading decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Value at Risk (VaR) Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Value at Risk (VaR) Calculator\
\
Calculate parametric, historical, and Monte Carlo Value at Risk for any portfolio. Estimate potential losses...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/var-calculator/)

[![Professional finance illustration representing Interest Rate Swap Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Interest Rate Swap Calculator\
\
Price plain vanilla interest rate swaps and calculate fixed swap rates. Determine the present value...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/interest-rate-swap-calculator/)

[![Professional finance illustration representing Bond Duration Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Duration Calculator\
\
Calculate Macaulay duration, modified duration, and estimate bond price sensitivity to interest rate changes. Essential...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-duration-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Options Mastery: From Theory to Practice

Master options trading from theory to practice. Covers fundamentals, Black-Scholes pricing, Greeks, and basic to advanced strategies with hands-on paper trading in Interactive Brokers.

*   100 lessons with 7 hours of video
*   Black-Scholes, Binomial & Greeks deep dives
*   Basic to advanced strategies (spreads, straddles, condors)
*   Hands-on paper trading with Interactive Brokers

[View Course](https://courses.ryanoconnellfinance.com/courses/options-theory-to-practice)

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