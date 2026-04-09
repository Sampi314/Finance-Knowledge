# Capital Market Line (CML) Calculator: Efficient Portfolio Risk-Return Tradeoff | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/capital-market-line-calculator

---

Capital Market Line (CML) Calculator
====================================

Efficient Portfolio Risk-Return Tradeoff

Calculate expected returns and optimal allocation between the market portfolio and the risk-free asset

Embed This Calculator

Enter Values
------------

Expected Market Return E(rM) ?

 %

Annualized expected return on market portfolio

Market Volatility (σM) ?

 %

Annualized standard deviation of market

Risk-Free Rate (rf) ?

 %

T-bill or other risk-free rate

Solve For ?

 From Target Risk (σC)  From Target Return E(rC)

Target Portfolio Risk (σC) ?

 %

Desired portfolio standard deviation

Target Portfolio Return E(rC) ?

 %

Desired portfolio expected return

Risk Aversion (A) ?

Computes portfolio utility U = E(rC) - ½AσC²

Reset to Defaults

##### CML Formula

E(rC) = rf + \[(E(rM) - rf) / σM\] × σC

**E(rC)** = Portfolio return | **rf** = Risk-free rate | **σM** = Market risk | **σC** = Portfolio risk Standard CML form (y ≥ 0). Calculator uses canonical form E(rC) = rf + y\[E(rM) − rf\] for all y.

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### CML Portfolio Result

Portfolio Expected Return E(rC) 7.3333% Lending

Portfolio Risk σC 12.0000%

Market Weight (y) 66.67%

Risk-Free Weight (1-y) 33.33%

CML Slope (Market Sharpe) 0.4444

Portfolio Sharpe 0.4444

Market Risk Premium 8.0000%

Portfolio Utility (A = 4) 0.044533

### Formula Breakdown

CML: E(rC) = rf + y × \[E(rM) - rf\]

Canonical form — valid for all allocation weights y

##### Model Assumptions

*   Market portfolio is mean-variance efficient (CAPM assumption)
*   Unlimited borrowing and lending at the risk-free rate
*   Homogeneous investor expectations
*   No transaction costs or taxes
*   Single-period model (one investment horizon)
*   CML applies only to efficient portfolios (combinations of market + risk-free)

_For educational purposes. Not financial advice. Market conventions simplified._

### Allocation Interpretation

| Weight (y) | Allocation | Meaning |
| --- | --- | --- |
| y = 0 | 100% Risk-Free | All capital in T-bills |
| 0 < y < 1 | Lending | Split between market and risk-free asset |
| y = 1 | 100% Market | Entire portfolio in market index |
| y > 1 | Leveraged | Borrowing at rf to invest beyond 100% in market |
| y < 0 | Short Market | CAL extension — shorting the market portfolio |

Understanding the Capital Market Line
-------------------------------------

### Video Explanation

Video: Capital Market Line Explained

### What is the Capital Market Line?

The **Capital Market Line (CML)** represents all efficient portfolios formed by combining the market portfolio with the risk-free asset. According to BKM Chapter 6, the CML is the capital allocation line (CAL) when the risky portfolio is the market portfolio itself — a well-diversified index that captures the entire investable universe.

Any point on the CML offers the highest expected return for a given level of total risk (standard deviation). The slope of the CML is the market's [Sharpe ratio](https://ryanoconnellfinance.com/calculators/sharpe-ratio-calculator/)
, representing the risk-return tradeoff available to all investors.

CML Equation (BKM Eq. 6.6)

**E(rC) = rf + \[(E(rM) - rf) / σM\] × σC**  
Slope = Market Sharpe Ratio = \[E(rM) - rf\] / σM

### CML vs. Security Market Line (SML)

#### Capital Market Line (CML)

**Total risk (σ) on x-axis**  
Efficient portfolios only — combinations of market portfolio + risk-free asset. Used for **portfolio construction** and capital allocation decisions.

#### Security Market Line (SML)

**Systematic risk (β) on x-axis**  
All assets and portfolios — including individual securities. Used for **asset pricing** via [CAPM](https://ryanoconnellfinance.com/calculators/capm-calculator/)
.

### Leverage and the CML

Portfolios to the left of the market portfolio (y < 1) involve **lending** — investing part of your capital in risk-free T-bills. Portfolios to the right (y > 1) involve **borrowing** — at the risk-free rate to lever your market exposure.

The key insight: regardless of where you are on the CML, the [Sharpe ratio](https://ryanoconnellfinance.com/calculators/sharpe-ratio-calculator/)
 remains constant and equal to the market's Sharpe ratio. Leverage amplifies both risk and return proportionally.

**When to Use This Calculator:** Use the CML Calculator to find the expected return and allocation for efficient **portfolios** — combinations of the market portfolio and the risk-free asset. Use the [CAPM Calculator](https://ryanoconnellfinance.com/calculators/capm-calculator/)
 to find the expected return of an individual **security** based on its beta.

### Related Concepts

*   [Efficient Frontier](https://ryanoconnellfinance.com/efficient-frontier/)
     — The set of optimal risky portfolios
*   [CAPM & Capital Asset Pricing Model](https://ryanoconnellfinance.com/capm-capital-asset-pricing-model/)
     — Pricing individual assets via the SML
*   [Sharpe Ratio](https://ryanoconnellfinance.com/calculators/sharpe-ratio-calculator/)
     — The CML slope equals the market Sharpe ratio
*   [Portfolio Diversification](https://ryanoconnellfinance.com/portfolio-diversification/)
     — Why only diversified portfolios reach the CML

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/capital-market-line-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the Capital Market Line (CML)?

The CML is a line in risk-return space that represents all efficient portfolios formed by combining the market portfolio with the risk-free asset. According to BKM Chapter 6, it is the capital allocation line (CAL) when the risky portfolio is the market portfolio. Any portfolio on the CML offers the highest expected return for its level of risk, as measured by the market Sharpe ratio.

### What is the difference between the CML and the Security Market Line (SML)?

The CML plots expected return versus total risk (standard deviation, σ) for efficient portfolios only — combinations of the market portfolio and the risk-free asset. The SML (from CAPM, BKM Chapter 9) plots expected return versus systematic risk (beta, β) for all assets and portfolios, including individual securities. The CML is about portfolio construction along the efficient frontier; the SML is about pricing any asset relative to its systematic risk. Only efficient portfolios lie on the CML, but all fairly priced assets lie on the SML.

### What does it mean to be "on" the CML?

Being on the CML means your portfolio is mean-variance efficient — it is some combination of the risk-free asset and the market portfolio. Points below the CML represent inefficient portfolios that could achieve higher returns for the same risk. Only diversified portfolios that combine the market portfolio with risk-free lending or borrowing can lie on the CML.

### How does leverage affect a portfolio on the CML?

When the market weight y exceeds 1, the investor borrows at the risk-free rate to invest more than 100% in the market portfolio. This creates a leveraged position with both higher expected return and higher risk, but the Sharpe ratio remains the same as the market’s. For example, y = 1.5 means borrowing 50% of your capital to invest 150% in the market.

### What is the slope of the CML?

The slope of the CML equals the market’s Sharpe ratio: \[E(rM) - rf\] / σM. It represents the additional expected return per unit of additional risk. A steeper CML means a better risk-return tradeoff. BKM reports the historical U.S. market Sharpe ratio at approximately 0.44 (1927–2021).

### Can individual securities lie on the CML?

Generally no. Individual securities carry unsystematic (diversifiable) risk, so they plot below the CML. Only perfectly diversified portfolios that are combinations of the market portfolio and the risk-free asset lie on the CML. This is why diversification is essential — it eliminates unsystematic risk and moves portfolios closer to the efficient frontier.

##### Disclaimer

This calculator is for educational purposes only. The Capital Market Line assumes the CAPM holds, investors can borrow and lend at the risk-free rate without limit, and the market portfolio is mean-variance efficient. Real-world constraints such as transaction costs, borrowing rate premiums, and non-normal returns will cause deviations from these theoretical results. This tool should not be used for trading decisions.

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