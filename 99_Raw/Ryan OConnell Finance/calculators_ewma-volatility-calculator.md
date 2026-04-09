# EWMA & GARCH Volatility Calculator | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/ewma-volatility-calculator

---

EWMA Volatility Calculator
==========================

EWMA and GARCH(1,1) Volatility Estimation

Estimate daily volatility using exponentially weighted models

Embed This Calculator

Enter Values
------------

Model ? EWMA Only GARCH(1,1) Both (Compare)

Previous Volatility Estimate (σₙ₋₁) ?

 %

Previous period's estimated daily volatility

Latest Return (rₙ₋₁) ?

 %

Most recent period's percentage return (e.g., -2 for a 2% decline)

Lambda (λ) ?

EWMA decay factor (0.94 = RiskMetrics daily)

###### Advanced: GARCH(1,1) Parameters

Parameters must satisfy α + β < 1 for a stationary process.

ω (omega) ? 

GARCH long-run variance weight (decimal-variance units)

α (alpha) ? 

GARCH return shock weight

β (beta) ? 

GARCH persistence weight

Reset to Defaults

##### EWMA & GARCH Formulas

EWMA: σ²ₙ = λ · σ²ₙ₋₁ + (1 - λ) · r²ₙ₋₁

**σ²** = Variance | **λ** = Decay factor | **r** = Return

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Volatility Estimate

EWMA Daily Volatility (σₙ) \--

GARCH Daily Volatility (σₙ) \--

Annualized EWMA \--

Annualized GARCH \--

EWMA Half-Life \--

GARCH Half-Life \--

Long-Run Daily Vol \--

Long-Run Annual Vol \--

α + β Sum \--

EWMA Vol Change \--

GARCH Vol Change \--

### Formula Breakdown

EWMA: σ²ₙ = λ · σ²ₙ₋₁ + (1 - λ) · r²ₙ₋₁

Step-by-step calculation breakdown

### Interpretation Guide

###### Volatility Change

| Change | Interpretation |
| --- | --- |
| < -10% | Volatility Declining |
| \-10% to -0.5% | Slightly Lower |
| ±0.5% | Stable |
| +0.5% to +10% | Slightly Higher |
| \> +10% | Volatility Rising |

###### GARCH Stationarity (α + β)

| α + β | Interpretation |
| --- | --- |
| < 0.99 | Stationary — mean-reverting |
| 0.99 – 1.0 | Near unit root — slow reversion |
| ≥ 1.0 | Non-stationary! VL undefined |

##### Model Assumptions

*   Single-asset volatility estimation (not multivariate)
*   Uses simple percentage returns (Hull Eq. 23.2), not log returns
*   EWMA: no mean reversion — volatility follows a random walk
*   GARCH: mean-reverting to long-run variance VL = ω/(1 - α - β)
*   Assumes returns are demeaned (mean ≈ 0 for daily data)
*   Annualization: 252 trading days/year

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding EWMA and GARCH Volatility
---------------------------------------

### What is the EWMA Model?

The **Exponentially Weighted Moving Average (EWMA)** model estimates volatility by giving exponentially declining weights to past squared returns. Unlike equal-weighted historical volatility, EWMA adapts quickly to changing market conditions by placing more weight on recent observations.

EWMA Variance Update (Hull Eq. 23.7)

**σ²ₙ = λ · σ²ₙ₋₁ + (1 - λ) · r²ₙ₋₁**  
λ = decay factor (0.94 = RiskMetrics daily) | r = percentage return

JP Morgan's **RiskMetrics** popularized EWMA with λ = 0.94 for daily data, finding this value produces variance forecasts closest to realized variance across many market variables. The half-life of a shock at λ = 0.94 is about 11.2 days.

### EWMA vs. GARCH(1,1)

#### EWMA

**No mean reversion**  
Volatility follows a random walk. Simple, only needs λ. Special case of GARCH with ω = 0.

#### GARCH(1,1)

**Mean-reverting**  
Volatility reverts to long-run level VL = ω/(1 - α - β). More parameters but captures volatility clustering better.

GARCH(1,1) Variance Update (Hull Eq. 23.9)

**σ²ₙ = ω + α · r²ₙ₋₁ + β · σ²ₙ₋₁**  
ω = long-run weight | α = shock weight | β = persistence weight | α + β < 1 for stationarity

### Mean Reversion in GARCH

The GARCH(1,1) model recognizes that volatility tends to revert to a long-run level. The expected future variance follows:

**E\[σ²ₙ₊ₜ\] = VL + (α + β)t · (σ²ₙ - VL)**

When α + β < 1, the (α + β)t term decays to zero, pulling volatility back to VL. The **half-life** = ln(0.5) / ln(α + β) measures how quickly this reversion occurs.

**Stationarity Requirement:** For a well-defined GARCH model, α + β must be strictly less than 1. When α + β ≥ 1, the process is non-stationary and the long-run variance is undefined.

### Practical Applications

*   **Value at Risk (VaR):** EWMA/GARCH volatility feeds directly into [parametric VaR calculations](https://ryanoconnellfinance.com/course-articles/value-at-risk/)
    
*   **Option Pricing:** Volatility estimates are critical inputs for Black-Scholes and other option pricing models
*   **Risk Management:** Tracking volatility changes helps in [portfolio risk assessment](https://ryanoconnellfinance.com/course-articles/standard-deviation-in-finance/)
     and position sizing
*   **Volatility Forecasting:** GARCH enables forecasting the [term structure of volatility](https://ryanoconnellfinance.com/course-articles/volatility-estimation-garch/)
    

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/ewma-volatility-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the EWMA model for volatility?

The EWMA model estimates volatility by applying exponentially declining weights to past squared returns. The formula σ²ₙ = λσ²ₙ₋₁ + (1-λ)r²ₙ₋₁ updates the variance using only the previous estimate and latest return, making it computationally efficient. RiskMetrics popularized this approach with λ = 0.94 for daily data. Unlike equal-weighted methods, EWMA gives more weight to recent observations, making it responsive to market regime changes.

### What is the difference between EWMA and GARCH?

EWMA is a special case of GARCH(1,1) where ω = 0 (no long-run variance term). The key difference is mean reversion: GARCH pulls volatility back toward a long-run average VL = ω/(1-α-β), while EWMA treats volatility as a random walk with no reversion level. GARCH requires α + β < 1 for stationarity, whereas EWMA implicitly has α + β = 1 (λ = β, 1-λ = α). In practice, GARCH is theoretically preferred because volatility does tend to mean-revert.

### Why does RiskMetrics use λ = 0.94?

JP Morgan's RiskMetrics found that λ = 0.94 for daily data produces variance forecasts closest to realized variance across a broad range of market variables. This value balances responsiveness to new information against stability. The half-life of a volatility shock at λ = 0.94 is about 11.2 days (ln(0.5)/ln(0.94) ≈ 11.2), meaning a shock's influence halves roughly every two weeks. For monthly data, RiskMetrics uses λ = 0.97.

### What does the half-life of a volatility shock mean?

The half-life measures how many periods it takes for the impact of a volatility shock (a large return) to decay to half its initial effect. For EWMA, half-life = ln(0.5)/ln(λ); for GARCH, half-life = ln(0.5)/ln(α+β). A shorter half-life means volatility adapts quickly to new information but is also more erratic. A longer half-life means smoother estimates but slower reaction to regime changes.

### When is GARCH(1,1) preferred over EWMA?

GARCH is preferred when you believe volatility mean-reverts to a long-run level — which is the case for most financial assets. Hull notes (Section 23.4) that if the best-fit ω is positive, GARCH provides better forecasts than EWMA. A negative best-fit ω may indicate the GARCH model is poorly specified for the data, and EWMA (which has no ω term) may be more appropriate. GARCH also enables volatility term structure forecasting via E\[σ²ₙ₊ₜ\] = VL + (α+β)t × (σ²ₙ - VL).

### What does it mean when α + β ≥ 1 in GARCH?

When α + β ≥ 1, the GARCH process is non-stationary: the weight on the long-run variance VL becomes zero or negative, meaning volatility does not revert to any long-run level. Instead, it exhibits “mean fleeing” behavior where shocks have permanent effects. In practice, this signals an unstable model, and you should either re-estimate parameters or switch to EWMA. A well-specified GARCH(1,1) model should have α + β < 1.

##### Disclaimer

This calculator is for educational purposes only. It implements the EWMA and GARCH(1,1) models as described in Hull's "Options, Futures, and Other Derivatives" (Chapter 23). Actual volatility estimation may require parameter calibration via maximum likelihood estimation. This tool should not be used as the sole basis for trading or risk management decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Value at Risk (VaR) Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Value at Risk (VaR) Calculator\
\
Calculate parametric, historical, and Monte Carlo Value at Risk for any portfolio. Estimate potential losses...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/var-calculator/)

[![Professional finance illustration representing Put Call Parity Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Put Call Parity Calculator\
\
Verify put-call parity relationships and identify potential arbitrage opportunities between call and put options.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/put-call-parity-calculator/)

[![Professional finance illustration representing Black Scholes Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Black Scholes Calculator\
\
Price European call and put options using the Black-Scholes model. Calculate option values, Greeks, and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/black-scholes-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Value at Risk (VaR) Course

Master Value at Risk from theory to implementation. Covers parametric, historical, and Monte Carlo VaR methods with hands-on Excel exercises using real market data.

*   Parametric, Historical & Monte Carlo VaR methods
*   Expected Shortfall (CVaR) and backtesting
*   EWMA & GARCH volatility estimation
*   Hands-on Excel exercises with real market data

[View Course](https://ryanoconnellfinance.com/courses/value-at-risk/)

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