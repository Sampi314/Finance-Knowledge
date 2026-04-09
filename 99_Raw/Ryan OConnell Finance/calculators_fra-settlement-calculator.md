# FRA Settlement Calculator - Forward Rate Agreement Payment | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/fra-settlement-calculator

---

FRA Settlement Calculator
=========================

Calculate Forward Rate Agreement Cash Settlement

Essential for interest rate hedging and derivatives pricing

Embed This Calculator

Enter Values
------------

Position Type

 Pay Fixed  Receive Fixed

Pay fixed: profit if rates rise | Receive fixed: profit if rates fall

Notional Principal (NP) ?

$ 

Face value of the underlying loan

FRA Rate (Contracted) ?

 %

Fixed rate agreed in the FRA contract

Reference Rate (Actual) ?

 %

Actual market rate at settlement

Contract Period ?

 days

Number of days in the FRA period

Day Count Convention ? Actual/360 (Money Market) Actual/365 (Fixed)

Actual/360 is standard for most FRAs

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### FRA Notation Guide

*   **1×4 FRA:** Starts in 1 month, ends in 4 months (3-month loan)
*   **3×6 FRA:** Starts in 3 months, ends in 6 months (3-month loan)
*   **6×12 FRA:** Starts in 6 months, ends in 12 months (6-month loan)
*   **Settlement:** Cash payment at start of loan period

### FRA Settlement Result

Settlement Amount +$1,234.57 Moderate Settlement Notable rate differential

Rate Differential +0.500%

Interest Diff +$1,250.00

Discount Factor 0.986193

Day Fraction 90/360 = 0.250000

### Formula Breakdown

Settlement = NP × \[(R - FRA) × (days/DCC)\] / \[1 + R × (days/DCC)\]

### Settlement Interpretation

| Scenario | Pay Fixed | Receive Fixed |
| --- | --- | --- |
| R > FRA (Rates Rose) | Receive (+) | Pay (-) |
| R = FRA (No Change) | None (0) | None (0) |
| R < FRA (Rates Fell) | Pay (-) | Receive (+) |

Understanding Forward Rate Agreements
-------------------------------------

### Video Explanation

Video: FRA Settlement Explained

### What is an FRA?

A **Forward Rate Agreement (FRA)** is an OTC derivative that allows parties to lock in an interest rate for a future borrowing or lending period. Unlike interest rate swaps with multiple payments, an FRA covers a single period with cash settlement at the beginning.

FRA Settlement Formula

Settlement = NP × \[(R - FRA) × (days/DCC)\] / \[1 + R × (days/DCC)\]

### Why Settlement at Start?

FRAs settle at the beginning of the loan period, not at the end. Since the payment covers interest that would accrue over the period, we discount it back to present value. This is why we divide by \[1 + R × (days/DCC)\].

**Day Count Convention:** Most FRAs use Actual/360 (money market convention). This means actual calendar days are used in the numerator, but 360 is used as the year basis.

### Pay Fixed vs Receive Fixed

#### Pay Fixed (FRA Buyer)

Profits when rates **rise**. You've locked in a lower rate than the market. Hedges against borrowing cost increases.

#### Receive Fixed (FRA Seller)

Profits when rates **fall**. You're betting the contracted rate will be better than market. Hedges lending income.

### Common FRA Uses

*   **Hedging:** Lock in borrowing costs for planned loans
*   **Speculation:** Profit from interest rate views
*   **Arbitrage:** Exploit rate discrepancies

**Reference Rates:** LIBOR was discontinued in 2023. FRAs now reference SOFR (USD), SONIA (GBP), EURIBOR (EUR), or TONAR (JPY).

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/fra-settlement-calculator-excel/)

Frequently Asked Questions
--------------------------

### What does 3×6 FRA mean?

A 3×6 FRA covers a 3-month loan starting in 3 months and ending in 6 months. The first number is when the FRA period begins, the second is when it ends. The difference (6-3=3 months) is the loan duration.

### Why is the settlement discounted?

The settlement represents interest that would accrue over the FRA period, but it's paid at the start. To be economically equivalent, we discount it to present value using the reference rate. This is called "advance" or "in-arrears" adjustment.

### How does an FRA differ from a futures contract?

FRAs are OTC contracts (customizable, counterparty risk) while interest rate futures are exchange-traded (standardized, marked-to-market daily). FRAs settle in cash at one point; futures have daily settlements. Both can hedge interest rate exposure.

### What happened to LIBOR-based FRAs?

LIBOR was discontinued in 2023 due to manipulation scandals. FRAs now reference alternative rates: SOFR (USD), SONIA (GBP), EURIBOR (EUR - reformed), TONAR (JPY). The formulas remain the same; only the reference rate changed.

### Is notional principal exchanged?

No. The notional principal is never exchanged - it's only used to calculate the settlement amount. Only the interest rate differential is settled. This is why it's called "notional" - it's a reference amount, not an actual loan.

### Can I use this for interest rate swaps?

An interest rate swap is essentially a series of FRAs. Each swap period can be valued using this formula. However, swap payments are typically settled in arrears (at period end), not in advance like FRAs, so the discounting differs.

##### Disclaimer

This calculator is for educational purposes only. Actual FRA settlements may differ due to market conventions, documentation terms, and counterparty agreements. Consult a qualified professional for hedging decisions.

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

[![Professional finance illustration representing Annualized Return Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Annualized Return Calculator\
\
Convert holding period returns to annualized returns for consistent comparison. Normalize investment performance across different...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/annualized-return-calculator/)

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