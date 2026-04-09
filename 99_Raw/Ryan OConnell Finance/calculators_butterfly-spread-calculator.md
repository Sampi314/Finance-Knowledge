# Butterfly Spread Calculator | Options Profit/Loss Tool | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/butterfly-spread-calculator

---

Butterfly Spread Calculator
===========================

Options Profit/Loss Calculator for Long Call Butterfly Spreads

Calculate breakeven, max profit/loss, and visualize the tent-shaped P/L at expiration and today

Embed This Calculator

Butterfly Parameters
--------------------

Current Stock Price ?

$ 

Current market price per share

Lower Strike (K1) ?

$ 

Buy 1 call at this strike (lower wing)

Middle Strike (K2) ?

$ 

Sell 2 calls at this strike (body)

Upper Strike (K3) ?

$ 

Buy 1 call at this strike (upper wing)

Days to Expiration ? 

Calendar days remaining

Calculate With ?

 Implied Volatility  Premium

Implied Volatility ?

 %

Annualized implied volatility (same for all strikes)

K1 Call Premium (per share) ?

$ 

Premium for the long K1 call

K2 Call Premium (per share) ?

$ 

Premium for each short K2 call (×2)

K3 Call Premium (per share) ?

$ 

Premium for the long K3 call

Risk-Free Rate ?

 %

Annualized risk-free rate

Dividend Yield ?

 %

Annualized dividend yield

Butterflies ? 

Each butterfly = buy 1 K1 call + sell 2 K2 calls + buy 1 K3 call (×100 shares)

Reset to Defaults

### Butterfly Quick Reference

**P/L at Expiration (4 regions):**

If S ≤ K1: P/L = −D × 100 × Qty

If K1 < S ≤ K2: P/L = (S − K1 − D) × 100 × Qty

If K2 < S < K3: P/L = (2K2 − K1 − S − D) × 100 × Qty

If S ≥ K3: P/L = (2K2 − K1 − K3 − D) × 100 × Qty

**Key Terms:**

*   **S** = Stock price at expiration
*   **K1, K2, K3** = Lower, middle, upper strike prices
*   **D** = Net Debit per share = K1 Premium − 2 × K2 Premium + K3 Premium
*   **Lower BE** = K1 + D
*   **Upper BE** = 2K2 − K1 − D
*   **Max Profit** = (K2 − K1 − D) × 100 × Qty (at S = K2)
*   **Max Loss** = D × 100 × Qty (equal-wing); may differ per side for broken-wing

### Key Metrics

Total Cost \--

Max Profit \--

Max Loss \--

Lower Breakeven \--

Upper Breakeven \--

Premiums (K1 / K2 / K3) \--

### Formula Breakdown

Net Debit = K1 Prem − 2 × K2 Prem + K3 Prem

Lower BE = K1 + D  |  Upper BE = 2K2 − K1 − D

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

Understanding the Butterfly Spread
----------------------------------

### What Is a Butterfly Spread?

A **long call butterfly spread** involves buying one call at a lower strike (K1), selling two calls at a middle strike (K2), and buying one call at a higher strike (K3), all with the **same expiration date**. The strategy has a tent-shaped payoff that peaks at the middle strike.

In a standard butterfly the wing widths are equal (K2−K1 = K3−K2), but this calculator also supports **broken-wing variations** where the wing widths differ. The net debit is calculated as K1 Premium − 2 × K2 Premium + K3 Premium.

### Key Characteristics

*   **Max Profit:** (K2 − K1 − Net Debit) × 100 × Qty. Occurs when the stock equals exactly the middle strike at expiration.
*   **Max Loss:** Net Debit × 100 × Qty. For equal-wing butterflies, this occurs when the stock is at or below K1, or at or above K3. For broken-wing butterflies, the loss on each side may differ.
*   **Lower Breakeven:** K1 + Net Debit per share
*   **Upper Breakeven:** 2K2 − K1 − Net Debit per share
*   **Outlook:** Neutral — expecting the stock to stay near the middle strike
*   **Cost:** Net debit (you pay the spread cost upfront)
*   **Time Decay:** Works for you near K2 — the short options at K2 lose time value faster than the long wings

### How to Read the P/L Chart

The **solid blue line (At Expiration)** shows the butterfly’s tent-shaped payoff. The peak occurs at the middle strike K2, where profit is maximized. Moving away from K2 in either direction, the P/L decreases linearly until reaching the wings, where it flattens out at the maximum loss.

The **dashed dark blue line (Today / T+0)** represents the theoretical P/L at trade entry, computed using Black-Scholes for all three strikes. The smooth curve shows how the position value changes with the stock price while time value remains in the options.

### IV Mode vs. Premium Mode

**IV Mode:** Enter implied volatility, and the calculator uses Black-Scholes to estimate all three strike premiums. This mode also enables the “Today (T+0)” P/L curve on the chart, showing theoretical value before expiration.

**Premium Mode:** Enter the exact call premiums for K1, K2, and K3 that you paid (or expect to pay). Useful when you know the actual market prices. Only the expiration payoff curve is shown because IV is needed to compute theoretical values before expiration.

### When to Use a Butterfly Spread

*   When you expect the stock to stay **range-bound** near a specific price through expiration
*   During periods of **low expected volatility** after an event has passed
*   When you want to profit from **time decay** with defined, limited risk
*   As a **low-cost, high-reward** alternative to selling naked options
*   When you have a specific **price target** for the underlying stock

**Model Assumptions:** This calculator uses the Black-Scholes model which assumes European-style exercise. For a long butterfly, the long wings cap the risk from the short middle-strike options, but early assignment on the short calls is possible with American-style options (particularly near ex-dividend dates). The model also assumes constant volatility, continuous dividend yield, and a constant risk-free rate. In practice, each strike may have a different IV due to skew; this calculator uses a single IV for all three strikes.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/butterfly-spread-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a long butterfly spread?

A long call butterfly spread involves buying one call at a lower strike price (K1), selling two calls at a middle strike price (K2), and buying one call at a higher strike price (K3), all with the same expiration date. In a standard butterfly the wing widths are equal, but the calculator also supports broken-wing variations where K2-K1 and K3-K2 differ. The strategy profits when the stock stays near the middle strike at expiration, and has limited risk defined by the net debit paid.

### What is the maximum profit and loss on a butterfly spread?

The maximum profit is the wing width (K2 minus K1) minus the net debit, multiplied by 100 shares per contract and the number of contracts. This occurs when the stock price equals exactly the middle strike at expiration. The maximum loss is the net debit paid, multiplied by 100 shares per contract and the number of contracts. For a standard equal-wing butterfly, this maximum loss occurs when the stock price is at or below the lower strike, or at or above the upper strike at expiration. For broken-wing butterflies, the loss on each side may differ.

### How are the breakeven prices calculated for a butterfly spread?

A butterfly spread has two breakeven points. The lower breakeven is the lower strike price plus the net debit per share. The upper breakeven is calculated as two times the middle strike minus the lower strike minus the net debit per share. For equal-wing butterflies this simplifies to the upper strike minus the net debit. The stock must stay between these two breakeven points at expiration for the position to be profitable.

### How does implied volatility affect a butterfly spread?

A long butterfly centered near at-the-money is generally a short-vega position, meaning it benefits from a decrease in implied volatility after entry. The effect depends on strike placement and skew. Higher IV at entry makes the butterfly more expensive because all four option premiums increase, but the net effect on the spread cost depends on how IV varies across strikes. After entry, lower realized volatility helps the position because the strategy profits from the stock staying near the middle strike.

### Should I use IV mode or enter the premiums directly?

Use **IV mode** when you want the calculator to estimate all three strike premiums using Black-Scholes with a single implied volatility input. This also enables the Today (T+0) P/L curve on the chart. Use **premium mode** when you know the exact premiums being offered for each strike and want to see the expiration payoff based on those known costs.

### Can I use this calculator for American-style options?

This calculator uses the Black-Scholes model, which assumes European-style options. For a long butterfly spread, the long options at the wings cap the theoretical risk from the short middle-strike options. However, early assignment on the short calls is possible with American-style options, particularly near ex-dividend dates, which can create temporary margin requirements or operational complexity even though the wings limit overall risk. The **expiration P/L diagram remains accurate** regardless of exercise style.

### When should I use a butterfly spread?

A butterfly spread is best used when you expect the stock price to stay near a specific price (the middle strike) through expiration. It is a neutral strategy that profits from low volatility. Common scenarios include range-bound stocks, periods of expected low volatility after an event has passed, or when you want to profit from time decay with defined risk. The butterfly offers a favorable risk-reward ratio but requires precise timing and strike selection.

##### Disclaimer

This calculator is for educational purposes only. Options trading involves significant risk of loss. Actual option prices and P/L may differ due to market conditions, bid-ask spreads, dividends, early exercise (American options), and other factors. The Black-Scholes model makes simplifying assumptions including constant volatility and European-style exercise. This is not financial advice. Consult a qualified professional before making investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Straddle Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Straddle Calculator\
\
Calculate straddle strategy profit, loss, and breakeven prices. Analyze this volatility strategy combining a call...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/straddle-calculator/)

[![Professional finance illustration representing Bear Call Spread Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bear Call Spread Calculator\
\
Calculate bear call spread profit, loss, and breakeven. Analyze this bearish credit spread strategy with...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bear-call-spread-calculator/)

[![Professional finance illustration representing Bull Call Spread Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bull Call Spread Calculator\
\
Calculate bull call spread profit, loss, and breakeven. Analyze this bullish options strategy with net...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bull-call-spread-calculator/)

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