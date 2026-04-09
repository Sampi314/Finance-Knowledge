# Covered Call Calculator | Options Profit/Loss Tool | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/covered-call-calculator

---

Covered Call Calculator
=======================

Options Profit/Loss Calculator for Covered Call Positions

Calculate breakeven, max profit/loss, and visualize P/L at expiration and today

Embed This Calculator

Covered Call Parameters
-----------------------

Stock Price ?

$ 

Entry price per share (the price you buy or already own the stock at)

Call Strike Price (K) ?

$ 

Strike of the call you sell (typically above current stock price)

Days to Expiration ? 

Calendar days remaining

Calculate With ?

 Implied Volatility  Premium

Implied Volatility ?

 %

Annualized implied volatility of the short call

Call Premium Received (per share) ?

$ 

Premium received reduces cost basis of the stock position

Risk-Free Rate ?

 %

Annualized risk-free rate

Dividend Yield ?

 %

Annualized dividend yield

Contracts ? 

Each contract = 100 shares of stock

Reset to Defaults

### Covered Call Quick Reference

**P/L at Expiration:**

If S ≤ K: P/L = (S - Stock Price + Premium) × 100 × Qty

If S > K: P/L = (K - Stock Price + Premium) × 100 × Qty

**Key Terms:**

*   **S** = Stock price at expiration
*   **K** = Call strike price
*   **Breakeven** = Stock Price - Premium per share
*   **Max Profit** = (K - Stock Price + Premium) × 100 × Qty
*   **Max Loss** = (Stock Price - Premium) × 100 × Qty (stock → $0)

### Key Metrics

Net Debit \--

Max Profit \--

Max Loss \--

Breakeven \--

Call Premium \--

Stock Cost \--

### Formula Breakdown

P/L (if S ≤ K) = (S - Stock Price + Premium) × 100 × Qty

Breakeven = Stock Price - Premium per share

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

Understanding Covered Calls
---------------------------

### Video Explanation

Video: Covered Call Options Strategy Explained

### What Is a Covered Call?

A **covered call** involves buying (or already owning) 100 shares of stock and selling one call option against those shares. You collect a premium upfront that reduces your cost basis in the stock. The strategy is called “covered” because the stock position covers the obligation of the short call.

This is a popular **income strategy** for investors with a neutral-to-moderately-bullish outlook. You profit when the stock stays flat, rises modestly, or even declines slightly (as long as it stays above your breakeven). Your upside is capped at the strike price because the short call obligates you to sell shares if exercised.

### Key Characteristics

*   **Max Profit:** (K - Stock Price + Premium) × 100 × Qty. Occurs when S ≥ K at expiration (shares are called away at the strike).
*   **Max Loss:** (Stock Price - Premium) × 100 × Qty. Occurs if the stock falls to $0 (you lose the full position value minus the premium collected).
*   **Breakeven:** Stock Price - Premium per share
*   **Outlook:** Neutral to moderately bullish
*   **Cost:** Net debit (stock purchase cost minus call premium received)
*   **Time Decay:** Benefits the short call leg — the option loses value as time passes, which helps the covered call seller

### How to Read the P/L Chart

The **solid blue line (At Expiration)** shows the covered call payoff: profit rises linearly as the stock price increases from the breakeven toward the strike, then flattens at the strike price (profit is capped because the short call is exercised and shares are sold). Below the breakeven, the position shows a loss that increases as the stock falls.

The **dashed dark blue line (Today / T+0)** represents the theoretical P/L at trade entry, computed using Black-Scholes for the short call. The smooth curve shows how the position value changes with the stock price while time value remains in the option.

### IV Mode vs. Premium Mode

**IV Mode:** Enter implied volatility, and the calculator uses Black-Scholes to estimate the call premium. This mode also enables the “Today (T+0)” P/L curve on the chart, showing theoretical value before expiration.

**Premium Mode:** Enter the exact premium you received (or expect to receive). Useful when you know the actual market price. Only the expiration payoff curve is shown because IV is needed to compute theoretical values before expiration.

### When to Use a Covered Call

*   You own (or are buying) 100 shares and want to **generate income** from selling the call
*   You have a **neutral-to-moderately-bullish outlook** on the stock
*   You are **willing to sell shares at the strike price** if the option is exercised
*   You want to **reduce your cost basis** in the stock position
*   You understand that your **upside is capped** at the strike price

**Model Assumptions:** This calculator uses the Black-Scholes model which assumes European-style exercise. Covered calls on American-style options carry early assignment risk, particularly near ex-dividend dates when the short call may be exercised by the buyer to capture the dividend. This risk is not reflected in the T+0 curve. The expiration payoff diagram remains accurate regardless of exercise style. The model also assumes constant volatility, continuous dividend yield, and a constant risk-free rate.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/covered-call-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a covered call?

A covered call involves buying (or already owning) 100 shares of stock and selling one call option at a strike price (typically above the current stock price). You collect a premium upfront that reduces your cost basis. The strategy is called “covered” because the stock position covers the obligation of the short call — if the buyer exercises, you deliver your existing shares rather than having to buy them at the market price.

### What is the maximum loss on a covered call?

The maximum loss is (Stock Price - Premium Received) × 100 × Number of Contracts, which occurs if the stock falls to $0. Unlike a naked short call, the downside is not unlimited, but it is still **substantial** — essentially the full cost of the stock position minus the premium collected. The premium provides a small cushion but does not eliminate the stock's downside risk.

### How is the breakeven price calculated for a covered call?

The breakeven price is **Stock Price - Premium Received per share**. At this stock price at expiration, the loss on the stock position exactly equals the premium collected from selling the call, resulting in zero profit or loss. Below the breakeven, the covered call position is at a net loss; above it, you have a net gain (capped at max profit when the stock reaches the strike).

### What does implied volatility mean for a covered call?

Higher implied volatility (IV) means a higher call premium received, which improves your income and lowers your breakeven price. However, high IV often signals greater market uncertainty, which can mean more downside risk in the stock itself. The covered call seller benefits from **elevated IV at entry** because they collect a richer premium, but should be aware that the stock may be more volatile than usual.

### Should I use IV mode or enter the premium directly?

Use **IV mode** when you want the calculator to estimate the call premium using Black-Scholes. This also enables the Today (T+0) P/L curve on the chart, showing theoretical value before expiration. Use **premium mode** when you know the exact premium being offered in the market and want to see the expiration payoff based on that known credit.

### Can I use this calculator for American-style options?

This calculator uses the Black-Scholes model, which assumes European-style options (exercisable only at expiration). American-style calls are rarely exercised early on non-dividend-paying stocks, so the **expiration P/L is nearly identical**. For dividend-paying stocks, the short call may face early assignment near ex-dividend dates, which could change actual outcomes versus the theoretical model.

### What happens if I'm assigned early on a covered call?

Early assignment means the call buyer exercises before expiration, requiring you to sell your shares at the strike price. This typically happens near ex-dividend dates when the call is in-the-money. You still keep the premium and receive the strike price for your shares. The P/L at assignment equals (Strike - Stock Price + Premium) × 100 × Qty, which is the **same as max profit** if the stock is above the strike. Early assignment ends the position early but is not necessarily a bad outcome.

##### Disclaimer

This calculator is for educational purposes only. Options trading involves significant risk of loss. Actual option prices and P/L may differ due to market conditions, bid-ask spreads, dividends, early exercise (American options), and other factors. The Black-Scholes model makes simplifying assumptions including constant volatility and European-style exercise. Early assignment risk on the short call is not modeled. This is not financial advice. Consult a qualified professional before making investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Short Call Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Short Call Calculator\
\
Calculate short call option profit, loss, and breakeven price. Visualize P/L at expiration and today...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/short-call-calculator/)

[![Professional finance illustration representing Long Call Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Long Call Calculator\
\
Calculate long call option profit, loss, and breakeven price. Supports Black-Scholes pricing with P/L visualization...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/long-call-calculator/)

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