# Capital Allocation Calculator: Optimal Risky Asset Allocation with Utility Maximization | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/capital-allocation-calculator

---

Capital Allocation Calculator
=============================

Optimal Risky Asset Allocation Tool

Calculate the utility-maximizing allocation between risky and risk-free assets (BKM Ch. 6)

Embed This Calculator

Enter Values
------------

Expected Return on Risky Portfolio E(rP) ?

 %

Annualized expected return

Volatility of Risky Portfolio (σP) ?

 %

Annualized standard deviation

Risk-Free Rate (rf) ?

 %

T-bill or other risk-free rate

Risk Aversion Coefficient (A) ?

Higher = more risk averse. Typical range: 2–6

Calculate Reset

[![Ryan O'Connell, CFA, FRM](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2048%2048'%3E%3C/svg%3E)](https://ryanoconnellfinance.com/about/)

Created by [Ryan O'Connell, CFA, FRM](https://ryanoconnellfinance.com/about/)

### Optimal Allocation

Optimal Risky Allocation (y\*) \--

### Complete Portfolio Details

Risk-Free Allocation \--

Expected Return E(rC) \--

Portfolio Risk σC \--

CAL Slope (Sharpe) \--

Portfolio Utility \--

Risk-Free Utility \--

_Higher utility = preferred under this model_

### Step-by-Step Calculation

y\* = \[E(rP) − rf\] / (A × σP²)

BKM Equation 6.7 — Optimal Allocation to Risky Asset

### Interpretation Guide

| Range | Status | Meaning |
| --- | --- | --- |
| 0% < y\* ≤ 100% | Standard | Normal allocation — split between risky and risk-free assets |
| y\* > 100% | Leveraged | Borrowing at risk-free rate to invest more than 100% in risky portfolio |
| y\* ≤ 0% | Short / No Risky | Negative allocation: short the risky portfolio and invest more than 100% in risk-free |

##### Model Assumptions

*   Mean-variance utility function (quadratic utility or normally distributed returns)
*   Single risky portfolio and single risk-free asset
*   Unlimited borrowing and lending at the risk-free rate (for y\* > 1)
*   Risk aversion coefficient is constant and known
*   No transaction costs or taxes

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Capital Allocation
--------------------------------

### Video Explanation

Video: Capital Allocation Explained

### What Is Capital Allocation?

**Capital allocation** is the fundamental decision of how to divide your investment portfolio between risky assets (stocks, bonds, real estate) and a risk-free asset (Treasury bills). In the BKM framework (Chapter 6), this decision is formalized using a **mean-variance utility function** that balances expected return against risk based on the investor's personal risk aversion.

Utility Function (BKM Eq. 6.1)

**U = E(r) − ½ × A × σ²**  
Higher utility = preferred portfolio under mean-variance framework

### Optimal Risky Allocation (y\*)

The optimal weight in the risky portfolio maximizes the investor's utility. Taking the derivative and solving yields:

Optimal y\* (BKM Eq. 6.7)

**y\* = \[E(rP) − rf\] / (A × σP²)**  
Risk premium divided by (risk aversion × variance)

This formula reveals that investors allocate **more** to the risky portfolio when the risk premium is higher or volatility is lower, and **less** when they are more risk-averse.

### The Capital Allocation Line (CAL)

The **Capital Allocation Line** plots all possible combinations of the risk-free asset and the risky portfolio in expected return vs. standard deviation space. Its slope equals the **Sharpe ratio** of the risky portfolio:

*   **CAL Slope** = \[E(rP) − rf\] / σP
*   A steeper CAL means a better risk-return tradeoff
*   Every investor on the same CAL has the same risky portfolio but different y\* values based on their risk aversion

### When to Use This Calculator

#### Capital Allocation Calculator

**Quantitative optimizer** — BKM Chapter 6 mean-variance utility maximization. Input specific return, volatility, and risk aversion to compute the mathematically optimal y\*.

#### Asset Allocation Calculator

**Qualitative questionnaire** — guided risk-tolerance assessment that recommends a stock/bond/cash split based on your answers. No formulas required.

**Tip:** Use this calculator if you know your risk aversion coefficient and want a precise, formula-driven allocation. Use the [Asset Allocation Calculator](https://ryanoconnellfinance.com/calculators/asset-allocation-calculator/)
 for a guided approach based on your personal risk tolerance.

Frequently Asked Questions
--------------------------

### What is the optimal allocation between risky and risk-free assets?

The optimal allocation (y\*) is determined by the formula y\* = \[E(rP) - rf\] / (A × σP²), where E(rP) is the expected return on the risky portfolio, rf is the risk-free rate, A is the investor's risk aversion coefficient, and σP² is the variance of the risky portfolio. This formula maximizes the investor's mean-variance utility function U = E(r) - ½Aσ². A higher risk premium or lower volatility increases the optimal risky allocation, while higher risk aversion decreases it.

### What is the risk aversion coefficient and how is it estimated?

The risk aversion coefficient (A) measures how much an investor dislikes risk relative to expected return. Typical values range from 2 to 6, where A=2 represents a relatively aggressive investor and A=6 a conservative one. It can be estimated through revealed preference (observing actual portfolio choices), questionnaires, or calibration against historical portfolio decisions. In the BKM framework, A determines how much return an investor demands per unit of variance.

### What does it mean when the optimal allocation exceeds 100%?

When y\* exceeds 100%, the model recommends a leveraged position — borrowing at the risk-free rate to invest more than your total wealth in the risky portfolio. For example, y\*=150% means borrowing 50% of your wealth at rate rf and investing 150% in the risky portfolio. This is theoretically optimal under BKM assumptions (unlimited borrowing at rf) but impractical for most investors due to margin requirements, borrowing costs exceeding rf, and amplified downside risk.

### What is the Capital Allocation Line (CAL)?

The Capital Allocation Line represents all possible combinations of the risk-free asset and a single risky portfolio, plotted in expected return vs. standard deviation space. Its slope equals the Sharpe ratio of the risky portfolio: S = \[E(rP) - rf\] / σP. The CAL starts at the risk-free rate (σ=0) and extends through the risky portfolio point. Every point on the CAL represents a different allocation y between 0 (100% risk-free) and beyond 1 (leveraged).

### How does the utility function work in portfolio theory?

The mean-variance utility function U = E(r) - ½Aσ² assigns a score to any portfolio based on its expected return and risk. Higher expected return increases utility while higher variance decreases it, scaled by the investor's risk aversion A. The optimal portfolio maximizes this utility. For a risk-free asset, utility simply equals rf (since σ=0). A higher utility score means the portfolio is preferred under this framework.

### What is the relationship between the CAL and the Sharpe ratio?

The CAL slope equals the Sharpe ratio of the risky portfolio: \[E(rP) - rf\] / σP. A steeper CAL means a better risk-return tradeoff — more expected return per unit of risk. The optimal allocation y\* places the investor at the point on the CAL that maximizes their personal utility given their risk aversion. All investors using the same risky portfolio face the same CAL, but each chooses a different point on it based on their risk aversion coefficient A.

##### Disclaimer

This calculator is for educational purposes only and assumes the mean-variance utility framework from BKM Chapter 6. Actual portfolio allocation decisions involve additional factors like liquidity needs, investment horizon, tax considerations, and behavioral biases. The model assumes unlimited borrowing at the risk-free rate and normally distributed returns, which may not hold in practice. This tool should not be used as the sole basis for investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Portfolio Variance Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Portfolio Variance Calculator\
\
Calculate portfolio variance and standard deviation for two-asset portfolios. Analyze how asset weights, volatilities, and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/portfolio-variance-calculator/)

[![Professional finance illustration representing CAPM Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### CAPM Calculator\
\
Calculate expected returns using the Capital Asset Pricing Model. Determine the required rate of return...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/capm-calculator/)

[![Professional finance illustration representing Sharpe Ratio Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Sharpe Ratio Calculator\
\
Calculate the Sharpe ratio to measure risk-adjusted portfolio returns. Compare investment performance relative to the...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/sharpe-ratio-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Portfolio Analytics & Risk Management Course

Master portfolio theory and risk management from fundamentals to advanced analytics. Covers modern portfolio theory, risk metrics, performance evaluation, and factor models.

*   Sharpe, Sortino, Treynor & Information Ratio deep dives
*   Modern Portfolio Theory and efficient frontier construction
*   Factor models including CAPM and Fama-French
*   Hands-on exercises with real portfolio data

[View Course](https://ryanoconnellfinance.com/courses/portfolio-analytics-risk-management/)

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