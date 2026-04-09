# Currency Option Pricing Calculator: Garman-Kohlhagen Model for FX Options

**Source:** https://ryanoconnellfinance.com/calculators/currency-option-pricing-calculator

---

Currency Option Pricing Calculator
==================================

Garman-Kohlhagen Model for FX Options

Price European currency options with dual interest rates, Greeks, and forward exchange rates

Embed This Calculator

Enter Values
------------

Option Type ?

 Call  Put

Call = buy foreign currency; Put = sell foreign currency

Spot Exchange Rate (S) ? 

e.g., 1.10 = 1 EUR costs 1.10 USD

Strike Rate (K) ? 

Exercise exchange rate

Domestic Risk-Free Rate (rd) ?

 %

Continuously compounded annual rate

Foreign Risk-Free Rate (rf) ?

 %

Continuously compounded annual rate

FX Volatility (σ) ?

 %

Annualized exchange rate volatility

Time to Expiration (T) ?

 years months days

Time until option expiration

Notional Amount (Foreign) ? 

Amount of foreign currency

Reset to Defaults

##### Garman-Kohlhagen Formula

C = Se\-rfTN(d1) - Ke\-rdTN(d2)

**S** = Spot rate | **K** = Strike | **rd** = Domestic rate | **rf** = Foreign rate

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Option Premium

Call Premium (per unit) \--

Total Premium \--

Premium % of Spot \--

Forward Rate (F) \--

d1 \--

d2 \--

N(d1) \--

N(d2) \--

### Option Greeks

Delta per unit foreign \--

Gamma per unit foreign \--

Theta per day \--

Vega per 1% vol \--

### Formula Breakdown

C = Se\-rfTN(d1) - Ke\-rdTN(d2)

Garman-Kohlhagen pricing with dual interest rates

### Moneyness Interpretation

| Moneyness | Condition (Call; reversed for Put) | Description |
| --- | --- | --- |
| Deep ITM | F >> K | High intrinsic value, delta near 1 |
| ITM | F > K | Positive intrinsic value |
| ATM | F ≈ K | Maximum time value, delta near 0.5 |
| OTM | F < K | No intrinsic value, all time value |
| Deep OTM | F << K | Low probability of expiring ITM |

_Moneyness is evaluated against the forward rate F = Se(rd\-rf)T, not the spot rate._

##### Model Assumptions

*   Continuous compounding for both domestic and foreign rates
*   Lognormally distributed exchange rates
*   European exercise only (no early exercise)
*   No transaction costs or bid-ask spreads
*   Exchange rate quoted as domestic per unit foreign (e.g., USD/EUR = 1.10)

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Currency Option Pricing
-------------------------------------

### What is the Garman-Kohlhagen Model?

The **Garman-Kohlhagen model** (1983) extends the Black-Scholes framework to price European options on foreign currencies. While BSM uses a single risk-free rate, the GK model incorporates **two interest rates** — one for each currency — reflecting the fact that holding foreign currency earns the foreign risk-free rate.

Garman-Kohlhagen Equations (Hull Eqs. 17.11–17.12)

**Call:** C = Se\-rfTN(d1) - Ke\-rdTN(d2)  
**Put:** P = Ke\-rdTN(-d2) - Se\-rfTN(-d1)  
Where d1 = \[ln(S/K) + (rd - rf + σ²/2)T\] / (σ√T)

### How Does It Differ from Black-Scholes?

#### Black-Scholes (Equities)

**One risk-free rate (r)**  
Dividend yield (q) is optional. The underlying is a stock that may pay discrete or continuous dividends.

#### Garman-Kohlhagen (FX)

**Two rates: rd (domestic) and rf (foreign)**  
The foreign rate replaces the dividend yield. Holding foreign currency earns rf continuously.

### Interest Rate Parity and FX Options

The **forward exchange rate** is determined by interest rate parity: F = S × e(rd - rf)T. When domestic rates exceed foreign rates, the forward rate is above spot (domestic currency expected to depreciate). This rate differential is the key driver that distinguishes FX option pricing from equity option pricing.

**Important:** The Garman-Kohlhagen model applies to **European options only**. American-style currency options require numerical methods (binomial trees or finite differences) due to the possibility of early exercise.

### When to Use This Calculator

Use the **Currency Option Calculator** when pricing FX options — it accounts for both domestic and foreign interest rates. A standard Black-Scholes calculator with a single risk-free rate would not correctly price currency options because it ignores the foreign interest rate that accrues on the underlying currency position.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/currency-option-pricing-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the Garman-Kohlhagen model?

The Garman-Kohlhagen model extends Black-Scholes to price European currency options. It replaces the dividend yield with the foreign risk-free rate, accounting for the interest rate differential between two currencies. Published in 1983, it remains the standard model for FX option valuation and is widely used by banks and institutional traders for pricing over-the-counter currency options.

### How does currency option pricing differ from stock option pricing?

Currency options use two interest rates (domestic and foreign) instead of one. The foreign interest rate acts like a continuous dividend yield on the underlying currency. This dual-rate structure reflects interest rate parity — the forward exchange rate is driven by the rate differential between two countries. In contrast, equity options use a single risk-free rate with an optional discrete or continuous dividend yield.

### What is the role of interest rate parity in FX options?

Interest rate parity determines the forward exchange rate: F = S × e(rd - rf) × T. Higher domestic rates relative to foreign rates push the forward rate above spot, meaning the domestic currency is expected to depreciate. This forward rate is embedded in Garman-Kohlhagen option pricing through the rate differential, affecting both the option premium and the Greeks.

### How do you interpret currency option Greeks?

Delta measures sensitivity to spot rate changes and is adjusted by e\-rfT to account for the foreign rate discount. Gamma measures the rate of delta change. Theta captures time decay per day (typically negative for long options, meaning the option loses value as expiry approaches). Vega shows premium sensitivity to a 1% change in FX volatility. All Greeks in the Garman-Kohlhagen model are modified from standard BSM to incorporate the foreign rate discount factor.

### What affects currency option premiums the most?

The key drivers are: (1) FX volatility — higher volatility increases both call and put premiums; (2) the interest rate differential between domestic and foreign rates, which affects forward rates and option values; (3) time to expiry — longer maturities increase premium through both time value and rate differential accumulation; and (4) moneyness, meaning how far the spot rate is from the strike price relative to the forward rate.

### What is the difference between a call and put on a currency pair?

A call on EUR/USD gives the right to buy euros at the strike rate in USD. A put gives the right to sell euros at the strike rate. Due to the symmetry of currency pairs, a call on EUR/USD is equivalent to a put on USD/EUR — buying euros is the same as selling dollars. In the Garman-Kohlhagen model, both are priced using the same dual-rate framework with continuous compounding.

##### Disclaimer

This calculator is for educational purposes only and assumes European options with continuously compounded rates. Actual FX option pricing involves additional factors like volatility smiles, market microstructure, and counterparty risk. This tool should not be used for trading decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Monte Carlo Option Pricing Simulator: GBM Simulation with Visualization](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Monte Carlo Option Pricing Simulator: GBM Simulation with Visualization\
\
Price European options using Monte Carlo simulation with geometric Brownian motion. Visualize simulated price paths...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/monte-carlo-option-pricing-calculator/)

[![Professional finance illustration representing Put Call Parity Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Put Call Parity Calculator\
\
Verify put-call parity relationships and identify potential arbitrage opportunities between call and put options.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/put-call-parity-calculator/)

[![Professional finance illustration representing Forward Price Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Price Calculator\
\
Calculate theoretical forward prices for financial assets using the cost of carry model. Determine fair...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-price-calculator/)

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