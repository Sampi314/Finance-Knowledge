# Bull Put Spread Calculator | Options Profit/Loss Tool | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bull-put-spread-calculator

---

Bull Put Spread Calculator
==========================

Options Profit/Loss Calculator for Bull Put Spread Positions

Calculate breakeven, max profit/loss, and visualize P/L at expiration and today

Embed This Calculator

Spread Parameters
-----------------

Stock Price ?

$ 

Current stock price at trade entry

Long Put Strike (K1) ?

$ 

Strike of the put you buy (lower)

Short Put Strike (K2) ?

$ 

Strike of the put you sell (higher)

Short put strike must be greater than long put strike.

Days to Expiration ? 

Calendar days remaining

Calculate With ?

 Implied Volatility  Premium

Implied Volatility ?

 %

Annualized implied volatility (same for both legs)

Short Put Premium (per share) ?

$ 

Long Put Premium (per share) ?

$ 

Risk-Free Rate ?

 %

Annualized risk-free rate

Dividend Yield ?

 %

Annualized dividend yield

Contracts ? 

Each contract = 100 shares per leg

Reset to Defaults

### Bull Put Spread Quick Reference

**P/L at Expiration:**

P/L = Net Credit

     - max(K2 - S, 0) × 100 × Qty

     + max(K1 - S, 0) × 100 × Qty

**Key Terms:**

*   **S** = Stock price at expiration
*   **K1** = Long put strike (lower)
*   **K2** = Short put strike (higher)
*   **Breakeven** = K2 - Net Credit per share
*   **Max Profit** = Net Credit
*   **Max Loss** = (K2 - K1) × 100 × Qty - Net Credit

### Key Metrics

Net Credit \--

Max Profit \--

Max Loss \--

Breakeven \--

Short Put Premium \--

Long Put Premium \--

### Formula Breakdown

P/L = Net Credit - \[max(K2 - S, 0) - max(K1 - S, 0)\] × 100 × Qty

Breakeven = K2 - Net Credit per share

### P/L Diagram

 At Expiration

 Today (T+0)

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

CALCULATOR BY

[Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

CFA Charterholder & Finance Educator

Finance professional building free tools for options pricing, valuation, and portfolio management.

[About](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)
 [YouTube](https://www.youtube.com/@RyanOConnellCFA)

Understanding Bull Put Spreads
------------------------------

### Video Explanation

Video: Bull Put Spread Explained

### What Is a Bull Put Spread?

A **bull put spread** (also called a short put spread or put credit spread) is an options strategy that involves selling a put option at a higher strike price (K2) and simultaneously buying a put option at a lower strike price (K1), both with the same expiration date.

This strategy expresses a **moderately bullish** view: you profit if the stock stays above your breakeven price. It is a net credit trade because the short put (higher strike) collects more premium than the long put (lower strike) costs.

### Key Characteristics

*   **Max Profit:** Limited to the Net Credit received at entry. Occurs when S ≥ K2 at expiration (both puts expire worthless).
*   **Max Loss:** Limited to (K2 - K1) × 100 × Qty - Net Credit. Occurs when S ≤ K1 at expiration.
*   **Breakeven:** K2 - Net Credit per share
*   **Outlook:** Moderately bullish or neutral
*   **Income:** Net credit (you receive money to enter because the short put premium exceeds the long put cost)
*   **Time Decay:** Works in your favor — as time passes, both options lose value, benefiting the net short position

### How to Read the P/L Chart

The **solid blue line (At Expiration)** shows three distinct regions: a flat loss region below K1 (max loss is capped), a rising profit/loss line between K1 and K2, and a flat profit region above K2 (you keep the full net credit).

The **dashed dark blue line (Today / T+0)** represents the theoretical P/L at trade entry using Black-Scholes for both legs. The smooth S-curve shows how the spread value changes with the stock price before expiration.

### IV Mode vs. Premium Mode

**IV Mode:** Enter a single implied volatility, and the calculator uses Black-Scholes to estimate both the short put and long put premiums. This mode also enables the "Today (T+0)" P/L curve on the chart.

**Premium Mode:** Enter the exact premiums for both legs. Useful when you know the actual market prices. Only the expiration payoff curve is shown because IV is needed to compute theoretical values before expiration.

### When to Use a Bull Put Spread

*   You have a **moderately bullish or neutral outlook** on the stock
*   You want to **collect premium income** with defined risk
*   You prefer **defined risk** over a naked short put (large loss potential)
*   You expect the stock to **stay above the higher strike** through expiration

**Model Assumptions:** This calculator uses the Black-Scholes model with the same implied volatility for both legs. In practice, different strikes may have different IVs (volatility skew). The model assumes European-style options, constant IV, continuous dividend yield, and a constant risk-free rate. For American-style puts, early exercise may occur when the short put is deep in-the-money.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bull-put-spread-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a bull put spread?

A bull put spread (also called a short put spread or put credit spread) involves selling a put option at a higher strike price and simultaneously buying a put option at a lower strike price, both with the same expiration date. It is a net credit strategy that profits when the underlying stock stays above the higher strike. Both maximum profit and maximum loss are defined at entry, making it a **defined-risk** strategy.

### What is the maximum profit and loss on a bull put spread?

The **maximum profit** is limited to the Net Credit received at entry, which occurs when the stock price is at or above the higher strike at expiration (both puts expire worthless). The **maximum loss** is (Higher Strike - Lower Strike) × 100 × Number of Contracts minus the Net Credit received, which occurs when the stock price is at or below the lower strike at expiration. Both outcomes are known before entering the trade.

### How is the breakeven price calculated for a bull put spread?

The breakeven price is **Higher Strike Price (K2) minus Net Credit per share**. The Net Credit per share is the premium received for the short put minus the premium paid for the long put. At the breakeven stock price at expiration, the loss on the short put exactly equals the net credit collected, resulting in zero profit or loss.

### What does implied volatility mean for a bull put spread?

Implied volatility (IV) affects both legs of the spread. Higher IV increases both the short put and long put premiums, but the short put (higher strike, higher delta) is generally more sensitive to IV changes. This means the net credit typically increases with higher IV, which benefits the bull put spread seller. This calculator uses a single IV for both legs; in practice, different strikes may have different IVs due to volatility skew.

### Should I use IV mode or enter the premiums directly?

Use **IV mode** when you want the calculator to estimate both put premiums using Black-Scholes with a single implied volatility. This also enables the T+0 (today) P/L curve on the chart. Use **premium mode** when you know the exact market prices for both legs and want to see the expiration payoff based on those known prices.

### When should I use a bull put spread instead of a short put?

Use a bull put spread when you are **moderately bullish** and want defined risk. A naked short put has large loss potential (strike price × 100 minus premium received), while the bull put spread caps your maximum loss to the width of the strikes minus the net credit. The trade-off is a smaller credit received compared to a naked short put.

### Can this calculator be used for American-style options?

This calculator uses the Black-Scholes model, which assumes European-style options (exercisable only at expiration). The **expiration P/L diagram is identical** for American and European put spreads on non-dividend-paying stocks. For dividend-paying stocks, the short put leg may face early assignment risk when the put is deep in-the-money, which could change the actual outcome versus the theoretical model.

##### Disclaimer

This calculator is for educational purposes only. Options trading involves significant risk of loss. Actual option prices and P/L may differ due to market conditions, bid-ask spreads, dividends, early exercise (American options), and other factors. The Black-Scholes model makes simplifying assumptions including constant volatility, a single IV for both strikes, and European-style exercise. This is not financial advice. Consult a qualified professional before making investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Short Put Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Short Put Calculator\
\
Calculate short put option profit, loss, breakeven price, and maximum risk. Visualize P/L at expiration...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/short-put-calculator/)

[![Professional finance illustration representing Long Put Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Long Put Calculator\
\
Calculate long put option profit, loss, and breakeven price. Supports Black-Scholes pricing with P/L visualization...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/long-put-calculator/)

[![Professional finance illustration representing Option Profit/Loss Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Option Profit/Loss Calculator\
\
Visualize potential profit and loss for any options strategy. Add multiple legs, view expiration curves,...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/option-profit-loss-calculator/)

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