# CPPI Calculator | Buy-and-Hold vs Constant-Mix vs CPPI | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/cppi-calculator

---

CPPI Strategy Calculator
========================

Dynamic Rebalancing Strategy Comparison

Compare buy-and-hold, constant-mix, and CPPI side-by-side

Embed This Calculator

Portfolio Parameters
--------------------

Initial Portfolio Value ?

$ 

Total starting portfolio value

Target Stock Allocation ?

 %

Used by buy-and-hold and constant-mix (e.g., 60 for 60/40)

CPPI Floor Value ?

$ 

Minimum portfolio value CPPI aims to protect

CPPI Multiplier (m) ?

 x

Stocks = m × Cushion (typical range: 2-5)

Risk-Free Rate (Bills) ?

 %

Annual rate, converted to per-period rate

Number of Periods ?

Number of periods to simulate

Return Input Mode ?

 Manual  Random

Per-Period Stock Returns (%)

Expected Annual Return ?

 %

Annual Volatility ?

 %

Calculate

### Quick Reference

#### Buy-and-Hold

`No rebalancing; stocks and bills drift freely`

#### Constant-Mix

`Rebalance to target weight each period`

Stocks = w × Portfolio

#### CPPI

`Cushion = max(Portfolio - Floor, 0)`

Stocks = min(m × Cushion, Portfolio)

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Strategy Comparison

Buy-and-Hold

\--

Stock Weight: \--

Constant-Mix

\--

Stock Weight: \--

CPPI

\--

Cushion: \--

Stock Weight: \--

### Wealth Path

### Payoff Profile

Terminal portfolio value across a range of total stock returns (-30% to +30%), distributed evenly across periods.

### Period-by-Period Breakdown

| Period | Stock Return | B&H Value | B&H Wt | CM Value | CM Wt | CPPI Value | CPPI Wt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Enter values to see results |     |     |     |     |     |     |     |

### Model Assumptions

*   Stocks earn the specified per-period return; bills earn the risk-free rate (annual rate / # periods)
*   Buy-and-hold: no rebalancing; initial stock/bill split drifts with returns
*   Constant-mix: rebalanced to exact target weight at the start of each period
*   CPPI: stock allocation = min(m × cushion, portfolio); remainder in bills
*   No transaction costs, taxes, or bid-ask spreads
*   Random mode uses normally distributed returns (Box-Muller method)

_For educational purposes. Not financial advice. Market conventions simplified._

### Step-by-Step Breakdown

Enter values to see the step-by-step calculation.

Understanding Dynamic Rebalancing Strategies
--------------------------------------------

### What is Dynamic Rebalancing?

**Dynamic rebalancing** refers to strategies that adjust portfolio allocations over time in response to market movements. The three strategies compared here represent fundamentally different philosophies: letting markets drift (buy-and-hold), maintaining discipline (constant-mix), and protecting downside while capturing upside (CPPI).

### Three Strategy Philosophies

#### Buy-and-Hold

Set initial allocation and let it drift. Stock weight increases in bull markets, decreases in bear markets. Linear payoff profile. Lowest turnover and transaction costs.

#### Constant-Mix

Rebalance to target each period. Sells winners, buys losers. Concave payoff, benefits from mean reversion. Moderate turnover. Best in choppy, range-bound markets.

#### CPPI

Cushion-based allocation with floor protection. Convex payoff like a call option. Increases exposure in rallies, reduces in drawdowns. Best in trending markets.

### Payoff Profiles and Market Conditions

The payoff profile chart reveals the key insight: **buy-and-hold is linear** (proportional to market return), **constant-mix is concave** (underperforms in trending markets, outperforms in mean-reverting ones), and **CPPI is convex** (protects downside while amplifying upside). No single strategy dominates in all market environments.

**Key Insight:** Use the [Portfolio Rebalancing Calculator](https://ryanoconnellfinance.com/calculators/portfolio-rebalancing-calculator/)
 to explore optimal rebalancing frequencies, and the [Capital Allocation Calculator](https://ryanoconnellfinance.com/calculators/capital-allocation-calculator/)
 to determine your initial target allocation.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/cppi-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is CPPI and how does it work?

Constant Proportion Portfolio Insurance (CPPI) is a dynamic asset allocation strategy that sets a floor value for the portfolio and allocates to risky assets based on a multiple of the cushion (portfolio value minus floor). When markets rise, CPPI increases stock exposure; when markets fall, it reduces exposure to protect the floor. The formula is: Stocks = m × max(Portfolio - Floor, 0), where m is the multiplier.

### What is the difference between buy-and-hold, constant-mix, and CPPI?

Buy-and-hold sets an initial allocation and lets it drift with market returns (no rebalancing). Constant-mix rebalances to a fixed target allocation each period (e.g., always 60/40). CPPI dynamically adjusts based on a floor and multiplier, increasing stock exposure as portfolio value rises above the floor. Buy-and-hold produces a linear payoff, constant-mix is concave, and CPPI is convex.

### What is the CPPI multiplier and how do I choose it?

The CPPI multiplier (m) determines how aggressively the strategy allocates to stocks based on the cushion. A higher multiplier means more stock exposure for a given cushion. Typical values range from 2 to 5. Higher multipliers amplify gains in rising markets but increase the risk of hitting the floor in volatile markets. The multiplier should reflect your risk tolerance and market outlook.

### What is the CPPI floor and cushion?

The floor is the minimum acceptable portfolio value that the CPPI strategy aims to protect. The cushion is the difference between the current portfolio value and the floor: Cushion = Portfolio - Floor. When the cushion is large, more is allocated to stocks. When the portfolio approaches the floor, the strategy shifts heavily to bills to preserve capital. If the portfolio hits the floor, all assets move to bills.

### Why does CPPI have a convex payoff profile?

CPPI produces a convex payoff because it increases stock exposure as markets rise (capturing more upside) and decreases exposure as markets fall (limiting downside). This creates an option-like payoff pattern where losses are bounded by the floor but gains are amplified. In contrast, constant-mix has a concave payoff because it sells winners and buys losers (rebalancing to target), and buy-and-hold is linear.

### When does CPPI underperform constant-mix?

CPPI tends to underperform constant-mix in choppy, mean-reverting markets. When prices oscillate without a clear trend, CPPI buys at highs (increasing exposure after gains) and sells at lows (reducing after losses), suffering from whipsaw. Constant-mix benefits from mean reversion because it automatically buys low and sells high through rebalancing. CPPI performs best in trending markets with sustained moves.

##### Disclaimer

This calculator is for educational purposes only and uses simplified models. Actual portfolio management involves transaction costs, taxes, liquidity constraints, and market impact. CPPI does not guarantee the floor will be maintained in continuous markets with gap risk. Consult a qualified financial advisor for personalized investment advice.

Related Calculators
-------------------

[![Professional finance illustration representing Portfolio Rebalancing Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Portfolio Rebalancing Calculator\
\
Analyze portfolio rebalancing strategies and drift tolerance.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/portfolio-rebalancing-calculator/)

[![Professional finance illustration representing Capital Allocation Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Capital Allocation Calculator\
\
Optimize capital allocation between a risky portfolio and risk-free asset. Calculate the optimal weight using...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/capital-allocation-calculator/)

[![Professional finance illustration representing Portfolio Variance Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Portfolio Variance Calculator\
\
Calculate portfolio variance and standard deviation for two-asset portfolios. Analyze how asset weights, volatilities, and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/portfolio-variance-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Portfolio Analytics & Risk Management Course

Master portfolio theory and risk management from fundamentals to advanced analytics. Covers modern portfolio theory, risk metrics, performance evaluation, and factor models.

*   Dynamic rebalancing strategies: CPPI, constant-mix, buy-and-hold
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