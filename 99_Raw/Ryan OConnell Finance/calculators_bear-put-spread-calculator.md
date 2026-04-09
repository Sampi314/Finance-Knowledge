# Bear Put Spread Calculator | Options Profit/Loss Tool | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bear-put-spread-calculator

---

Bear Put Spread Calculator
==========================

Options Profit/Loss Calculator for Bear Put Spread Positions

Calculate breakeven, max profit/loss, and visualize P/L at expiration and today

Embed This Calculator

Spread Parameters
-----------------

Stock Price ?

$ 

Current stock price at trade entry

Short Put Strike (K1) ?

$ 

Strike of the put you sell (lower)

Long Put Strike (K2) ?

$ 

Strike of the put you buy (higher)

Long put strike must be higher than short put strike.

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

### Bear Put Spread Quick Reference

**P/L at Expiration:**

P/L = \[max(K2 - S, 0) - max(K1 - S, 0)\]

     × 100 × Qty - Net Debit

**Key Terms:**

*   **S** = Stock price at expiration
*   **K1** = Short put strike (lower)
*   **K2** = Long put strike (higher)
*   **Breakeven** = K2 - Net Debit per share
*   **Max Profit** = (K2 - K1) × 100 × Qty - Net Debit
*   **Max Loss** = Net Debit

### Key Metrics

Net Debit \--

Max Profit \--

Max Loss \--

Breakeven \--

Short Put Premium \--

Long Put Premium \--

### Formula Breakdown

P/L = \[max(K2 - S, 0) - max(K1 - S, 0)\] × 100 × Qty - Net Debit

Breakeven = K2 - Net Debit per share

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

Understanding Bear Put Spreads
------------------------------

### Video Explanation

Video: Bear Put Spread Explained

### What Is a Bear Put Spread?

A **bear put spread** (also called a long put spread or put debit spread) involves buying a put option at a higher strike price (K2) and simultaneously selling a put option at a lower strike price (K1), both with the same expiration date.

This strategy expresses a **moderately bearish** view: you profit when the stock declines below your breakeven. It is a net debit trade because the long put (higher strike) costs more than the short put (lower strike) collects.

### Key Characteristics

*   **Max Profit:** (K2 - K1) × 100 × Qty - Net Debit. Occurs when S ≤ K1 at expiration.
*   **Max Loss:** Limited to the Net Debit (entry cost). Occurs when S ≥ K2 at expiration.
*   **Breakeven:** K2 - Net Debit per share
*   **Outlook:** Moderately bearish
*   **Cost:** Net debit (you pay money to enter because the long put premium exceeds the short put premium)
*   **Time Decay:** Works against you — as time passes, both options lose value, hurting the net long position

### How to Read the P/L Chart

The **solid blue line (At Expiration)** shows three distinct regions: a flat profit region below K1 (max profit is capped), a linearly decreasing P/L from K1 to K2 as the stock price rises through the spread, and a flat loss region above K2 (you lose the full net debit).

The **dashed dark blue line (Today / T+0)** represents the theoretical P/L at trade entry using Black-Scholes for both legs. The smooth S-curve shows how the spread value changes with the stock price before expiration.

### IV Mode vs. Premium Mode

**IV Mode:** Enter a single implied volatility, and the calculator uses Black-Scholes to estimate both the long put and short put premiums. This mode also enables the "Today (T+0)" P/L curve on the chart.

**Premium Mode:** Enter the exact premiums for both legs. Useful when you know the actual market prices. Only the expiration payoff curve is shown because IV is needed to compute theoretical values before expiration.

### When to Use a Bear Put Spread

*   You have a **moderately bearish outlook** on the stock
*   You want to **reduce the cost** of buying a long put by selling a lower-strike put
*   You prefer **defined risk** with both max profit and max loss known at entry
*   You expect the stock to **decline below the breakeven** through expiration

**Model Assumptions:** This calculator uses the Black-Scholes model with the same implied volatility for both legs. In practice, different strikes may have different IVs (volatility skew). The model assumes European-style options, constant IV, continuous dividend yield, and a constant risk-free rate.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bear-put-spread-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a bear put spread?

A bear put spread (also called a long put spread or put debit spread) involves buying a put option at a higher strike price and simultaneously selling a put option at a lower strike price, both with the same expiration date. It is a net debit strategy that profits when the underlying stock declines below the breakeven price. Both maximum profit and maximum loss are defined at entry, making it a **defined-risk** strategy.

### What is the maximum profit and loss on a bear put spread?

The **maximum profit** is (Higher Strike - Lower Strike) × 100 × Number of Contracts minus the Net Debit paid. This occurs when the stock price is at or below the lower strike at expiration. The **maximum loss** is limited to the Net Debit (entry cost), which occurs when the stock price is at or above the higher strike at expiration (both puts expire worthless). Both outcomes are known before entering the trade.

### How is the breakeven price calculated for a bear put spread?

The breakeven price is **Higher Strike Price - Net Debit per share**. The Net Debit per share is the premium paid for the long put minus the premium received for the short put. At the breakeven stock price at expiration, the intrinsic value of the long put exactly equals the net cost of entry.

### What does implied volatility mean for a bear put spread?

Implied volatility (IV) affects both legs of the spread. Higher IV increases both the long put and short put premiums, but the long put (higher strike, higher delta) is generally more sensitive to IV changes. This means the net debit typically increases with higher IV, making the spread more expensive to enter. This calculator uses a single IV for both legs; in practice, different strikes may have different IVs due to volatility skew.

### Should I use IV mode or enter the premiums directly?

Use **IV mode** when you want the calculator to estimate both put premiums using Black-Scholes with a single implied volatility. This also enables the T+0 (today) P/L curve on the chart. Use **premium mode** when you know the exact market prices for both legs and want to see the expiration payoff based on those known costs.

### When should I use a bear put spread instead of a long put?

Use a bear put spread when you are **moderately bearish** and want to reduce the cost of a long put by selling a lower-strike put against it. The spread has a lower entry cost and smaller maximum loss than a standalone long put, but your profit is capped at the width of the strikes minus the net debit. A long put is preferable when you expect a large downward move and want maximum profit potential (down to zero).

### Can this calculator be used for American-style options?

This calculator uses the Black-Scholes model, which assumes European-style options (exercisable only at expiration). The **expiration P/L diagram is identical** for American and European put spreads on non-dividend-paying stocks. The short put leg may face early assignment risk when it is deep in-the-money, particularly when interest rates are high (the option holder may prefer to exercise early to invest the proceeds). This differs from short calls, where early assignment is mainly driven by ex-dividend dates. Early assignment could change the actual outcome versus the theoretical model.

##### Disclaimer

This calculator is for educational purposes only. Options trading involves significant risk of loss. Actual option prices and P/L may differ due to market conditions, bid-ask spreads, dividends, early exercise (American options), and other factors. The Black-Scholes model makes simplifying assumptions including constant volatility, a single IV for both strikes, and European-style exercise. This is not financial advice. Consult a qualified professional before making investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Bear Call Spread Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bear Call Spread Calculator\
\
Calculate bear call spread profit, loss, and breakeven. Analyze this bearish credit spread strategy with...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bear-call-spread-calculator/)

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