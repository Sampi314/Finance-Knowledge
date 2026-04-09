# Game Theory Payoff Matrix Calculator | Nash Equilibrium | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/game-theory-payoff-calculator

---

Game Theory Payoff Matrix Calculator
====================================

2×2 Nash Equilibrium & Dominant Strategy Finder

Analyze strategic interactions, find Nash equilibria, and identify Prisoner's Dilemma games

Embed This Calculator

Game Setup
----------

Preset Game ? Prisoner's Dilemma Battle of the Sexes Chicken Matching Pennies Custom Game

Players

Player 1 (Rows) ? 

Player 2 (Columns) ? 

Player 1 Strategies

Strategy 1 

Strategy 2 

Player 2 Strategies

Strategy 1 

Strategy 2 

Payoff Matrix ?

P1 ↓ / P2 →

Cooperate

Defect

Cooperate

 

(P1, P2)

 

(P1, P2)

Defect

 

(P1, P2)

 

(P1, P2)

Reset to Defaults

##### Normal-Form Game

|     |     |     |
| --- | --- | --- |
|     | **P2: S1** | **P2: S2** |
| **P1: S1** | (a, b) | (c, d) |
| **P1: S2** | (e, f) | (g, h) |

Each cell shows **(P1 payoff, P2 payoff)**. P1 picks rows, P2 picks columns. Higher payoff = better outcome.

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Payoff Matrix

■ = Nash Equilibrium  |  Underline = P1 best response  |  Underline = P2 best response

### Analysis Results

#### Strictly Dominant Strategies

Firm A \--

Firm B \--

#### Pure-Strategy Nash Equilibria

\--

#### Game Properties

Prisoner's Dilemma? \--

NE Pareto Status \--

#### Pareto-Efficient Outcomes

### Model Assumptions

*   Simultaneous, one-shot game — players choose at the same time, in one round only
*   Complete information — both players know the full payoff matrix
*   Rational players — each player maximizes their own payoff
*   Pure strategies only — no mixed-strategy equilibria computed
*   2 players, 2 strategies — 2×2 matrices only
*   No binding agreements — non-cooperative game
*   For educational purposes. Not financial advice. Market conventions simplified.

Understanding Game Theory
-------------------------

### What is Game Theory?

**Game theory** is the study of strategic decision-making where the outcome for each participant depends on the choices of all participants. In economics, it is essential for analyzing oligopoly markets, where a small number of firms must consider competitors' actions when setting prices or output levels.

### The Prisoner's Dilemma

The **Prisoner's Dilemma** demonstrates why individually rational choices can lead to collectively suboptimal outcomes. Each player has a strictly dominant strategy (defect), yet both would be better off cooperating. This structure appears in many economic contexts: firms in a cartel have incentives to cheat on production agreements, countries in arms races prefer to arm rather than disarm, and shared resources get overused when each user maximizes their own consumption.

### Nash Equilibrium

A **Nash equilibrium** is an outcome where no player can improve their payoff by unilaterally changing their strategy. In this calculator, we identify _pure-strategy_ Nash equilibria by checking whether each player's choice is a best response to the other player's choice. Some games have no pure-strategy NE but always have a mixed-strategy equilibrium (not computed here).

### Dominant Strategies

A **strictly dominant strategy** yields a strictly higher payoff regardless of the opponent's choice. Not all games have dominant strategies. When both players have one, the outcome is determined — even if it leaves both worse off than some alternative (as in the Prisoner's Dilemma). This calculator uses _strict_ dominance, meaning ties do not count.

### Pareto Efficiency

An outcome is **Pareto efficient** if no other outcome can make at least one player better off without making anyone worse off. Note that Pareto-efficient outcomes are not necessarily fair or equal — an outcome where one player gets everything can still be Pareto efficient. In the Prisoner's Dilemma, three of the four outcomes are Pareto efficient; only the mutual defection (Nash equilibrium) is Pareto dominated.

**Scope:** This calculator analyzes pure strategies in 2×2 games only. Mixed-strategy equilibria, sequential games, and games with more than 2 players or strategies require more advanced analysis.

### Game Theory in Oligopoly (Mankiw Ch. 17)

Mankiw's Chapter 17 on oligopoly shows that firms in concentrated markets face a Prisoner's Dilemma. The monopoly outcome (low output, high prices) maximizes joint profit, but each firm has an incentive to increase production unilaterally. This tension between cooperation and self-interest drives oligopoly behavior and explains why cartels like OPEC historically struggle to maintain production agreements.

#### Related Topics

**Articles:**

*   [Game Theory & Oligopoly](https://ryanoconnellfinance.com/game-theory-oligopoly/)
    
*   [Monopoly & Market Power](https://ryanoconnellfinance.com/monopoly-market-power/)
    

**Calculators:**

*   [Monopoly Profit Calculator](https://ryanoconnellfinance.com/calculators/monopoly-profit-calculator/)
    
*   [Cost Curves Calculator](https://ryanoconnellfinance.com/calculators/cost-curves-calculator/)
    
*   [Competitive Firm Profit Calculator](https://ryanoconnellfinance.com/calculators/competitive-firm-profit-calculator/)
    
*   [Pigouvian Tax Calculator](https://ryanoconnellfinance.com/calculators/pigouvian-tax-calculator/)
    

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/game-theory-payoff-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a Nash equilibrium and how do you find it?

A Nash equilibrium is an outcome where neither player can improve their payoff by unilaterally changing their strategy, given what the other player is doing. To find it in a 2×2 game, check all four outcomes: for each cell, verify that Player 1 wouldn't prefer to switch rows (given Player 2's column) and Player 2 wouldn't prefer to switch columns (given Player 1's row). If no player wants to deviate, it's a pure-strategy Nash equilibrium. Some games have zero, one, or multiple pure-strategy Nash equilibria.

### What is a strictly dominant strategy?

A strictly dominant strategy yields a strictly higher payoff regardless of what the other player does. It must beat the alternative against _both_ possible opponent strategies — ties don't count. Not all games have dominant strategies. When both players have one, they will play them — even if the resulting outcome is suboptimal for both, as in the Prisoner's Dilemma. This is distinct from _weakly_ dominant strategies, where ties are allowed.

### What is the Prisoner's Dilemma and why is it important in economics?

The Prisoner's Dilemma is a game where both players have a strictly dominant strategy that leads to a Nash equilibrium, but both would be better off if they cooperated. Specifically, it requires the payoff ordering T > R > P > S for each player (Temptation to defect > Reward for cooperation > Punishment for mutual defection > Sucker's payoff). It's important in economics because it shows how rational self-interest can produce collectively suboptimal outcomes. This explains why cartels break down (firms cheat on agreements), arms races persist, and common resources get overused.

### Can a game have more than one pure-strategy Nash equilibrium?

Yes. Some 2×2 games have zero pure-strategy Nash equilibria (like Matching Pennies, which has only a mixed-strategy equilibrium), some have exactly one (like the Prisoner's Dilemma), and some have two or more (like Battle of the Sexes or Chicken). Multiple equilibria create a coordination problem — players may not know which equilibrium will be reached. In such cases, focal points, communication, or social norms may guide players to one equilibrium.

### What is the difference between a Nash equilibrium and a Pareto-efficient outcome?

A Nash equilibrium is self-enforcing: no player wants to deviate unilaterally. A Pareto-efficient outcome means no other outcome can make at least one player better off without making someone else worse off. These concepts are independent — a Nash equilibrium can be Pareto dominated (as in the Prisoner's Dilemma, where mutual defection is the NE but mutual cooperation makes both better off), and a Pareto-efficient outcome might not be a Nash equilibrium (players would want to deviate). Note that Pareto efficiency does not imply fairness: an outcome can be Pareto efficient even if one player gets everything.

### How does game theory apply to oligopoly markets?

In an oligopoly, firms' profits depend on competitors' choices — a strategic game. Firms face a Prisoner's Dilemma: all benefit from keeping output low and prices high (cooperation), but each has an incentive to produce more and capture market share (defection). This tension between cooperation and self-interest is a central theme in Mankiw's Chapter 17. While this incentive to defect pushes oligopoly output away from the monopoly level, the exact outcome depends on market structure, repeated interaction, and the ability to monitor competitors. OPEC's historical difficulty maintaining production agreements illustrates this tension.

##### Disclaimer

This calculator is for educational purposes only. It analyzes 2×2 normal-form games with pure strategies. Real-world strategic interactions may involve more players, more strategies, incomplete information, repeated games, and mixed strategies not captured here. For educational purposes. Not financial advice. Market conventions simplified.

Related Calculators
-------------------

[![Professional finance illustration representing Cost Curves Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Cost Curves Calculator\
\
Calculate and graph marginal cost, average total cost, average variable cost, and average fixed cost...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/cost-curves-calculator/)

[![Professional finance illustration representing Monopoly Profit & Deadweight Loss Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Monopoly Profit & Deadweight Loss Calculator\
\
Calculate monopoly profit, price, and deadweight loss.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/monopoly-profit-calculator/)

[![Professional finance illustration representing Competitive Firm Profit & Shutdown Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Competitive Firm Profit & Shutdown Calculator\
\
Calculate profit for firms in perfectly competitive markets.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/competitive-firm-profit-calculator/)

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