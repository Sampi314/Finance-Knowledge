# Endowment Spending Rule Calculator | Yale & Cap-Floor Rules | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/endowment-spending-rule-calculator

---

Endowment Spending Rule Calculator
==================================

Yale, Cap-Floor & Rolling Average Policies

Compare endowment spending rules and project long-term sustainability

Embed This Calculator

Spending Parameters
-------------------

Spending Rule ? Simple Spending Rate Rolling Average Yale-Style Smoothing Cap-Floor Compare All

Endowment Parameters

Beginning Endowment Value ?

$ 

Target Spending Rate ?

 %

Expected Annual Return ?

 %

Inflation Rate ?

 %

Rule-Specific Settings

Weight on Prior Spending (w) ?

Averaging Window ?

 years

Spending Floor ?

 % of prior

Spending Cap ?

 % of prior

Additional Settings

Annual Contributions ?

$ 

Simulation Horizon ?

 years

Reset to Defaults

##### Spending Rule Formulas

**Simple:** Rate × PostReturnMV

**Rolling Avg:** Rate × Avg(MV, N yrs)

**Yale:** w × S(t-1) × (1+inf) + (1-w) × Rate × MV

**Cap-Floor:** Rate × MV, clamped to \[Floor, Cap\]

**MV** = Post-Return Market Value | **S(t-1)** = Prior Year Spending | **w** = Weight on Prior | **inf** = Inflation

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Spending Analysis

Year 1 Spending $5,000,000 Sustainable

Terminal Endowment \--

Total Spending \--

Avg Spending / Year \--

Spending Volatility \--

Real Growth (CAGR) \--

\* Real Growth includes external contributions

### Rule Comparison

\* Real Growth includes external contributions

### Spending Path

Simple

Rolling Avg

Yale

Cap-Floor

### Year-by-Year Projection

### Formula Breakdown

##### Model Assumptions

*   Investment returns are constant (expected return achieved every year)
*   No stochastic modeling of returns, spending, or inflation
*   Annual contributions and inflation rate are constant over the horizon
*   Spending is withdrawn after investment returns are applied (end-of-year)
*   Year 0 is a pure snapshot: seed spending is shown for reference but not deducted from the endowment
*   Yale-Style Smoothing uses current-year post-return market value (not lagged); actual Yale endowment timing may differ
*   Rolling average uses available years when fewer than the window size exist
*   If endowment is depleted, actual spending is capped at available funds and simulation stops
*   Real Growth uses the exact Fisher formula: (1 + nominal CAGR) / (1 + inflation) - 1

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Endowment Spending Rules
--------------------------------------

### What is an Endowment Spending Rule?

An **endowment spending rule** (or spending policy) determines how much an endowment distributes each year to fund operations, scholarships, research, or other purposes. The fundamental challenge is balancing two competing goals: providing adequate current funding while preserving the endowment's real (inflation-adjusted) purchasing power for future generations. This is known as the principle of **intergenerational equity**.

### The Four Spending Rules

#### Simple Spending Rate

**Formula:** Spending = Rate × PostReturnMV  
Applies a fixed percentage to current market value. Simple and transparent, but spending fluctuates directly with investment returns, creating budget volatility.

#### Rolling Average

**Formula:** Spending = Rate × Average(MV over N years)  
Smooths spending by averaging market values over a window (typically 3-5 years). Reduces volatility but lags behind market movements.

#### Yale-Style Smoothing

**Formula:** S(t) = w × S(t-1) × (1+inf) + (1-w) × Rate × MV  
Blends inflation-adjusted prior spending (weight w) with current endowment value (weight 1-w). Used by Yale, Stanford, and many large endowments. Produces very smooth, predictable distributions.

#### Cap-Floor Policy

**Formula:** Spending = Rate × MV, clamped to \[Floor%, Cap%\] of prior spending  
Starts with the simple rule but constrains year-over-year changes. Prevents both excessive spending in bull markets and painful cuts in downturns.

### Spending Volatility vs. Endowment Sustainability

There is a fundamental trade-off between spending smoothness and responsiveness to market conditions:

*   **More smoothing** (Yale with high w, narrow cap-floor bands) provides budget predictability but can lead to over-spending in prolonged downturns or under-spending in prolonged bull markets
*   **Less smoothing** (simple rule, wide cap-floor bands) keeps spending aligned with actual endowment performance but creates budget volatility that can disrupt operations

The **spending volatility** metric (standard deviation of year-over-year spending changes) quantifies this trade-off. Lower volatility means more predictable budgets.

Key Sustainability Condition

**Real Return** = (1 + Nominal Return) / (1 + Inflation) - 1  
If Real Return > Spending Rate, endowment grows in real terms  
This is a necessary (but not sufficient) condition for long-term sustainability

**Important:** This calculator uses deterministic (constant) returns. Real endowments experience volatile returns, and the **sequence of returns matters** — poor early returns combined with fixed spending can permanently impair an endowment even if average returns are adequate. Consider Monte Carlo simulation for a more realistic assessment.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/endowment-spending-rule-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is an endowment spending rule?

An endowment spending rule is a policy that determines how much an endowment distributes each year to fund operations, scholarships, or other purposes. The goal is to balance current spending needs with preserving the endowment's purchasing power for future generations. Common rules include a simple percentage of market value, rolling averages, Yale/Stanford-style smoothing, and cap-floor policies. The choice of spending rule affects both the predictability of annual distributions and the long-term sustainability of the endowment.

### How does the Yale/Stanford spending rule work?

The Yale/Stanford spending rule (also called the smoothing rule) blends two components: (1) last year's spending adjusted for inflation, weighted by _w_, and (2) the target spending rate applied to current post-return market value, weighted by _(1-w)_. The formula is: Spending(t) = w × \[Spending(t-1) × (1 + inflation)\] + (1-w) × \[Rate × PostReturnMV(t)\]. A typical weight of 0.80 means 80% of spending is based on the inflation-adjusted prior year and 20% on current endowment value, providing smooth, predictable distributions while still responding gradually to changes in endowment value. This calculator implements the Yale-style variant using current-year post-return market value, consistent with the MTMP textbook presentation; actual university endowment policies may use lagged market values or other timing conventions.

### What is the difference between simple and rolling average spending rules?

The simple spending rule applies a fixed percentage to the current year's post-return market value: Spending = Rate × PostReturnMV. This is straightforward but produces volatile spending that fluctuates with market returns. The rolling average rule applies the same rate to the average market value over a window of N years: Spending = Rate × Average(PostReturnMV over N years). This smooths spending by dampening the impact of any single year's returns, though it lags behind market movements. The rolling average is a middle ground between the simple rule's volatility and more sophisticated smoothing approaches.

### How does a cap-floor spending policy protect endowments?

A cap-floor policy starts with the simple spending calculation (Rate × PostReturnMV) but constrains year-over-year changes. If spending would increase more than the cap (e.g., 105% of prior year), it is capped. If it would decrease more than the floor (e.g., 95% of prior year), a floor is applied. This prevents both excessive spending in bull markets and painful cuts in bear markets, providing budget stability while still responding to endowment performance over time. The tighter the bands, the smoother the spending — but also the slower the adjustment to changing market conditions.

### What spending rate do most endowments use?

Most university and foundation endowments target a spending rate between 4% and 5.5% of market value. The most common target is 5%. This rate is designed to allow the endowment to maintain its real (inflation-adjusted) value over time while providing meaningful annual distributions. The actual sustainable rate depends on expected investment returns, inflation, and the specific spending rule used. If expected real returns (nominal return minus inflation) exceed the spending rate, the endowment should grow in real terms over long horizons.

### How do I know if my endowment spending is sustainable?

Endowment spending is sustainable when the real (inflation-adjusted) value of the endowment is maintained or growing over time. Key indicators include: (1) the spending rate is below the expected real return, (2) the terminal endowment value exceeds the initial value in real terms, (3) the real growth rate of spending is positive, and (4) the endowment does not deplete during the projection horizon. This calculator's Real Growth metric shows the annualized inflation-adjusted growth rate of the endowment, with positive values indicating sustainability. When annual contributions are included, Real Growth may overstate sustainability — the calculator flags these cases as "Contribution-Dependent." Note that deterministic projections can be misleading — volatile real-world returns mean sustainability also depends on return sequence risk.

##### Disclaimer

This calculator is for educational purposes only and uses simplified, deterministic assumptions. Actual endowment management involves stochastic return modeling, spending policy committees, and consideration of donor restrictions, tax implications, and regulatory requirements. This tool should not be used for actual endowment spending decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Breakeven Spread Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Breakeven Spread Calculator\
\
Calculate the breakeven spread for credit bond investments.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/breakeven-spread-calculator/)

[![Professional finance illustration representing Pension Funded Status Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Pension Funded Status Calculator\
\
Calculate defined benefit pension funded status and funded ratio.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/pension-funded-status-calculator/)

[![Professional finance illustration representing Bond Immunization Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Immunization Calculator\
\
Check if your bond immunizes a future liability through duration matching.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-immunization-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Portfolio Analytics & Risk Management Course

Master portfolio theory and risk management from fundamentals to advanced analytics. Covers modern portfolio theory, risk metrics, performance evaluation, and factor models.

*   Endowment management and spending policy analysis
*   Modern Portfolio Theory and efficient frontier construction
*   Risk metrics: VaR, CVaR, drawdown analysis
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