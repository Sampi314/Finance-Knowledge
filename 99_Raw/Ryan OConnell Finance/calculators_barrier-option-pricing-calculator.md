# Barrier Option Pricing Calculator | Knock-In & Knock-Out Options | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/barrier-option-pricing-calculator

---

Barrier Option Pricing Calculator
=================================

Knock-In & Knock-Out Option Pricing

Price all 8 barrier option types and verify in-out parity

Embed This Calculator

Enter Values
------------

Option Type ? Call Put

Barrier Type ? Down-and-Out Down-and-In Up-and-Out Up-and-In

Barrier must be below spot price

Stock Price (S) ?

$ 

Current price of underlying asset

Strike Price (K) ?

$ 

Exercise price of the option

Barrier Level (H) ?

$ 

Knock-in or knock-out trigger level

Risk-Free Rate (r) ?

 %

Enter as percentage (e.g., 5 for 5%)

Volatility (σ) ?

 %

Annualized volatility

Time to Expiration (T) ?

 years

Time until option expiration

Dividend Yield (q) ?

 %

Continuous dividend yield

Rebate ?

$ 

Rebate PV shown separately (informational)

Monitoring: **Continuous** (analytical Hull Ch. 26 formulas)

Reset to Defaults

##### In-Out Parity

Knock-In + Knock-Out = Vanilla

For matching strike, barrier, and expiration:  
**cdi + cdo = c**  |  **pui + puo = p**

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Barrier Option Price

Down-and-Out Call Price $0.0000 Moderate Distance

Vanilla Price $0.0000

Discount from Vanilla 0.00%

Barrier Distance 10.00%

In-Out Parity Check $0.0000

Rebate PV $0.0000

Formula Branch H ≤ K

### Formula Breakdown

Barrier Option Pricing (Hull Ch. 26)

Continuous monitoring, European exercise

##### Model Assumptions

*   Continuous barrier monitoring (analytical formulas from Hull Table 26.1) — discrete monitoring materially changes prices
*   Lognormally distributed underlying price (geometric Brownian motion)
*   European exercise for the option component
*   No discrete dividend payments (continuous yield only)
*   Constant risk-free rate, volatility, and dividend yield over option life
*   Formulas branch by barrier/strike relative position (8 combinations)

_For educational purposes. Not financial advice. Market conventions simplified._

### Barrier Type Comparison

| Barrier Type | Behavior | Typical Use |
| --- | --- | --- |
| Down-and-Out | Extinguished if S falls to H | Cheap downside hedge |
| Down-and-In | Activates if S falls to H | Contingent protection |
| Up-and-Out | Extinguished if S rises to H | Capped upside |
| Up-and-In | Activates if S rises to H | Momentum entry |

Understanding Barrier Options
-----------------------------

### What Are Barrier Options?

**Barrier options** are exotic options whose payoff depends on whether the underlying asset price reaches a specified barrier level during the option's life. They are classified as either **knock-out** (option ceases to exist at the barrier) or **knock-in** (option comes into existence at the barrier).

In-Out Parity

**Knock-In + Knock-Out = Vanilla Option**  
For matching strike, barrier, and expiration

### The 8 Barrier Option Types

#### Down Barriers (H < S)

**Down-and-Out:** Knocked out if price falls to H.  
**Down-and-In:** Activated if price falls to H.  
Used for: Downside protection, structured notes.

#### Up Barriers (H > S)

**Up-and-Out:** Knocked out if price rises to H.  
**Up-and-In:** Activated if price rises to H.  
Used for: Capped strategies, momentum trades.

### Pricing Framework

Hull Chapter 26 provides analytical formulas for all 8 barrier option types using combinations of standard BSM components. The formulas depend on the relative position of the barrier (H) to the strike (K), creating different formula branches.

*   **Continuous monitoring:** The analytical formulas assume the barrier is monitored continuously. Discrete monitoring (e.g., daily close) materially changes prices.
*   **Formula branching:** Different formulas apply depending on whether H ≤ K or H > K.
*   **In-out parity:** A key verification tool — the sum of a knock-in and knock-out with identical terms must equal the vanilla price.

**Important:** Barrier options are generally cheaper than vanilla options because the knock-out/knock-in conditions restrict the payoff space. However, this discount depends on barrier proximity, volatility, and time to expiration.

### Key Considerations

*   Barrier distance affects price significantly — closer barriers mean larger discounts for knock-outs
*   Vega can be negative for barrier options (unlike vanilla options)
*   Rebate timing is contract-specific: paid on barrier breach (knock-out) or at expiry (knock-in)
*   Widely used in FX markets, structured products, and hedging strategies

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/barrier-option-pricing-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a barrier option?

A barrier option is an exotic option whose payoff depends on whether the underlying asset price reaches a specified barrier level during the option's life. Unlike vanilla options that only depend on the asset price at expiration, barrier options can be activated (knock-in) or extinguished (knock-out) when the barrier is breached. They are popular in OTC markets because they are generally cheaper than equivalent vanilla options.

### What is the difference between knock-in and knock-out options?

A knock-out option ceases to exist (is extinguished) when the underlying asset price reaches the barrier level. A knock-in option only comes into existence when the barrier is reached. For knock-out options, the holder may receive a rebate when the barrier is hit. Both types can be "up" (barrier above current price) or "down" (barrier below current price), creating four combinations: up-and-in, up-and-out, down-and-in, and down-and-out.

### Why are barrier options generally cheaper than vanilla options?

Barrier options are generally cheaper because they have additional conditions that can reduce or eliminate their payoff. A knock-out option may cease to exist before expiration if the barrier is hit, while a knock-in option requires the barrier to be hit before it becomes active. These restrictions reduce the expected payoff compared to a vanilla option with the same strike price and expiration, making them less expensive. The discount increases as the barrier gets closer to the current asset price.

### What is in-out parity for barrier options?

In-out parity states that the sum of a knock-in and knock-out option (with the same strike, barrier, and expiration) equals the price of the corresponding vanilla option. For example: Down-and-In Call + Down-and-Out Call = Vanilla Call. This relationship holds because either the barrier is hit (activating the knock-in) or it is not (keeping the knock-out alive), but never both. This parity provides a useful verification check for barrier option prices.

### How does barrier proximity affect option price?

Barrier proximity (or barrier distance) measures how close the current asset price is to the barrier level. For knock-out options, closer proximity means higher probability of the barrier being hit and the option being extinguished, resulting in a lower price. For knock-in options, closer proximity means higher probability of activation, resulting in a higher price. Volatility amplifies this effect since higher volatility increases the probability of reaching the barrier regardless of distance.

### What are common uses of barrier options?

Barrier options are widely used in foreign exchange markets, structured products, and hedging strategies. Importers and exporters use them for cheaper currency hedging (e.g., a down-and-out put provides downside protection unless the currency weakens beyond the barrier). Banks embed them in structured notes to offer enhanced yields. Traders use them to express views on price ranges. Note that prices differ materially depending on whether monitoring is continuous or discrete (e.g., daily close).

##### Disclaimer

This calculator is for educational purposes only and uses analytical formulas for continuously monitored European barrier options. Actual barrier option pricing involves additional factors including discrete monitoring adjustments, bid-ask spreads, transaction costs, and counterparty risk. For precise pricing, use professional derivatives pricing systems. This tool should not be used for trading decisions.

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

[![Professional finance illustration representing Black Scholes Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Black Scholes Calculator\
\
Price European call and put options using the Black-Scholes model. Calculate option values, Greeks, and...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/black-scholes-calculator/)

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