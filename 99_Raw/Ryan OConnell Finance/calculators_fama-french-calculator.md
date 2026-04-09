# Fama-French Three-Factor Model Calculator: Expected Return and Factor Analysis

**Source:** https://ryanoconnellfinance.com/calculators/fama-french-calculator

---

Fama-French Three-Factor Model Calculator
=========================================

Multi-Factor Expected Return & Factor Analysis Tool

Calculate expected returns using three-factor and five-factor asset pricing models

Embed This Calculator

Factor Inputs
-------------

Model ? Three-Factor (1993) Five-Factor (2015)

* * *

###### Factor Premiums

Risk-Free Rate (Rf) ?

 %

Annualized risk-free rate (e.g., T-bill yield)

Market Risk Premium ?

 %

E(RM) - Rf, already excess over risk-free

Size Premium (SMB) ?

 %

Illustrative default ~2-3% (Ken French Data Library)

Value Premium (HML) ?

 %

Illustrative default ~3-5% (Ken French Data Library)

Profitability Premium (RMW) ?

 %

Profitability factor premium (~3%)

Investment Premium (CMA) ?

 %

Investment factor premium (~2-3%)

* * *

###### Factor Loadings (Betas)

Market Beta (βM) ?

Sensitivity to market excess returns

Size Beta (βSMB) ?

Positive = small-cap, negative = large-cap

Value Beta (βHML) ?

Positive = value, negative = growth

Profitability Beta (βRMW) ?

Sensitivity to profitability factor

Investment Beta (βCMA) ?

Sensitivity to investment factor

* * *

Actual Return (optional) ?

 %

Enter to compute single-period abnormal return

Reset to Defaults

##### Fama-French Formula

E(Ri) = Rf + βM(RM - Rf) + βSMB·SMB + βHML·HML

**Rf** = Risk-free rate | **βM** = Market beta | **SMB** = Size premium | **HML** = Value premium

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Expected Return

Expected Return E(Ri) 11.9000% Small-Cap Value

Expected Excess Return 7.9000%

Risk-Free 4.0000%

Market 6.0000%

Size (SMB) 1.0000%

Value (HML) 0.9000%

Profitability (RMW) 0.0000%

Investment (CMA) 0.0000%

Abnormal Return (α) 0.0000%

### Formula Breakdown

E(Ri) = Rf + βM·MRP + βSMB·SMB + βHML·HML

Step-by-step factor contribution breakdown

### Factor Profile Interpretation

| Factor | Positive Loading | Negative Loading |
| --- | --- | --- |
| Market (βM) | Aggressive (high market risk) | Defensive (low market risk) |
| SMB (βSMB) | Small-cap tilt | Large-cap tilt |
| HML (βHML) | Value tilt | Growth tilt |

##### When to Use This Calculator

Use the **Fama-French Calculator** when you need multi-factor asset pricing that accounts for size and value effects beyond market beta alone.

Use the [CAPM Calculator](https://ryanoconnellfinance.com/calculators/capm-calculator/)
 for single-factor (market beta only) expected return estimates.

The Fama-French model explains cross-sectional return differences better than CAPM by capturing size and value premiums (BKM Ch 10.5).

Understanding the Fama-French Model
-----------------------------------

### What is the Fama-French Three-Factor Model?

The **Fama-French three-factor model** is an asset pricing model developed by Eugene Fama and Kenneth French in 1993. It extends the Capital Asset Pricing Model (CAPM) by adding two factors beyond market risk: a **size factor (SMB)** capturing the historical outperformance of small-cap stocks, and a **value factor (HML)** capturing the outperformance of high book-to-market (value) stocks.

Expected Return (Pricing Form)

E(Ri) = Rf + βM(E(RM) - Rf) + βSMB·E(SMB) + βHML·E(HML)

**BKM Note:** BKM Eq 10.9 presents the _realized-return regression form_: Ri - Rf = αi + βM(RM - Rf) + βSMB·SMB + βHML·HML + εi. This calculator uses the _expected-return pricing form_, which sets α = 0 and takes expectations. Both forms share the same factor loadings.

### The Three Factors

#### SMB (Small Minus Big)

**Size premium**  
Return difference between small-cap and large-cap stock portfolios. Small firms historically earn higher returns, possibly due to greater vulnerability to business deterioration and limited capital access.

#### HML (High Minus Low)

**Value premium**  
Return difference between high book-to-market (value) and low book-to-market (growth) stocks. Value stocks historically outperform, possibly because high B/M signals financial distress risk.

### Five-Factor Extension (2015)

The five-factor model adds two more factors:

*   **RMW (Robust Minus Weak):** Profitability premium. Firms with high operating profitability tend to earn higher returns.
*   **CMA (Conservative Minus Aggressive):** Investment premium. Firms that invest conservatively (low asset growth) tend to earn higher returns than aggressive investors.

### Model Assumptions

*   Factor returns (SMB, HML, RMW, CMA) are exogenous and specified by the user
*   Linear factor model — no interaction effects between factors
*   Factor premiums are assumed constant (user provides point estimates)
*   Does not account for liquidity risk, momentum, or other factors outside the specified model
*   Based on Fama-French empirical factor definitions (portfolio sorts by size and book-to-market)
*   All inputs assumed annualized on the same basis — no mixed-frequency adjustment
*   Default factor premiums are illustrative; actual premiums are time-varying and regime-dependent (source: Ken French Data Library)
*   For educational purposes. Not financial advice. Market conventions simplified.

### Related Resources

*   [Fama-French Three-Factor Model (Article)](https://ryanoconnellfinance.com/fama-french-three-factor-model/)
    
*   [Equity Risk Premium](https://ryanoconnellfinance.com/equity-risk-premium/)
    
*   [Growth vs Value Investing](https://ryanoconnellfinance.com/growth-vs-value-investing/)
    
*   [CAPM: Capital Asset Pricing Model](https://ryanoconnellfinance.com/capm-capital-asset-pricing-model/)
    

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/fama-french-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the Fama-French three-factor model?

The Fama-French three-factor model is an asset pricing model developed by Eugene Fama and Kenneth French in 1993. It extends the Capital Asset Pricing Model (CAPM) by adding two additional factors beyond market risk: a size factor (SMB, Small Minus Big) and a value factor (HML, High Minus Low book-to-market). The model explains approximately 90% of diversified portfolio return variation, compared to about 70% for CAPM alone.

### What are the SMB and HML factors?

SMB (Small Minus Big) captures the size premium: the historical tendency of small-cap stocks to outperform large-cap stocks. It is calculated as the return difference between portfolios of small and large stocks. HML (High Minus Low) captures the value premium: the tendency of high book-to-market (value) stocks to outperform low book-to-market (growth) stocks. Both factors are empirical and their premiums are time-varying. Historical factor data is available from the Ken French Data Library at Dartmouth College.

### How is the Fama-French model different from CAPM?

CAPM uses a single factor (market beta) to explain expected returns, while the Fama-French three-factor model adds size (SMB) and value (HML) exposures beyond market beta. This captures cross-sectional return differences that CAPM cannot explain, such as the size and value premiums. The five-factor extension further adds profitability (RMW) and investment (CMA) factors for even broader coverage of return patterns.

### What is the Fama-French five-factor model?

The Fama-French five-factor model, introduced in 2015, extends the three-factor model by adding two additional factors: RMW (Robust Minus Weak), which captures the profitability premium — firms with high operating profitability tend to earn higher returns — and CMA (Conservative Minus Aggressive), which captures the investment premium — firms that invest conservatively tend to outperform aggressive investors. The five-factor model provides a more comprehensive explanation of cross-sectional stock returns.

### Where can I find Fama-French factor data?

The primary source for Fama-French factor data is the Ken French Data Library, hosted at Dartmouth College. It provides daily, weekly, and monthly factor returns for U.S. and international markets. The data includes the market factor (Mkt-RF), SMB, HML, RMW, CMA, and the risk-free rate. The data is updated regularly and freely available for academic and research purposes.

### What does a negative factor loading mean?

A negative factor loading indicates inverse sensitivity to that factor. For example, a negative HML beta means the asset behaves like a growth stock (low book-to-market), moving opposite to the value factor. A negative SMB beta indicates large-cap exposure. Negative loadings are common and valid — they reduce the expected return contribution from that factor when the factor premium is positive.

##### Disclaimer

This calculator is for educational purposes only. Factor premiums are illustrative defaults; actual premiums are time-varying and regime-dependent. The abnormal return shown is a single-period comparison, not a regression-estimated alpha. This tool should not be used for investment decisions without professional consultation.

Related Calculators
-------------------

[![Professional finance illustration representing Beta Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Beta Calculator\
\
Calculate beta coefficient to measure a stock's systematic risk relative to the market. Analyze volatility...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/beta-calculator/)

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