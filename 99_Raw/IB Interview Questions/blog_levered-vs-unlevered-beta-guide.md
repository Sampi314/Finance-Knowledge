# Levered vs Unlevered Beta: When and Why to Unlever

**Source:** https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide

---

![Levered vs Unlevered Beta: When and Why to Unlever](https://ibinterviewquestions.com/assets/levered-vs-unlevered-beta-guide-C-vUuXez.webp)

On this pageIntroduction

*   [Understanding Beta in Valuation](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#understanding-beta-in-valuation)
    
*   [Levered vs. Unlevered Beta: Key Differences](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#levered-vs-unlevered-beta-key-differences)
    
*   [What is Levered Beta?](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#what-is-levered-beta)
    
*   [What is Unlevered Beta?](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#what-is-unlevered-beta)
    
*   [The Unlevering Formula](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#the-unlevering-formula)
    
*   [The Relevering Formula](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#the-relevering-formula)
    
*   [When to Unlever and Relever Beta](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#when-to-unlever-and-relever-beta)
    
*   [When You Must Unlever and Relever](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#when-to-unlever-and-relever-beta-when-you-must-unlever-and-relever)
    
*   [When Direct Use May Be Appropriate](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#when-to-unlever-and-relever-beta-when-direct-use-may-be-appropriate)
    
*   [The Step-by-Step Process](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#the-step-by-step-process)
    
*   [Practical Example](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#practical-example)
    
*   [Common Interview Questions](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#common-interview-questions)
    
*   [Common Mistakes to Avoid](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#common-mistakes-to-avoid)
    
*   [Alternative Formulas](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#alternative-formulas)
    
*   [Key Takeaways](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#key-takeaways)
    
*   [Conclusion](https://ibinterviewquestions.com/blog/levered-vs-unlevered-beta-guide#conclusion)
    

Latest on the blog

[![Introducing Our Industrials Guide for Investment Banking](https://ibinterviewquestions.com/assets/introducing-industrials-guide-ib-DD1Fn9FI.webp)\
\
#### Introducing Our Industrials Guide for Investment Banking\
\
April 1, 2026](https://ibinterviewquestions.com/blog/introducing-industrials-guide-ib)
[![Mezzanine Debt and Preferred Equity Explained](https://ibinterviewquestions.com/assets/mezzanine-debt-preferred-equity-explained-N5Lp3Azu.webp)\
\
#### Mezzanine Debt and Preferred Equity Explained\
\
March 30, 2026](https://ibinterviewquestions.com/blog/mezzanine-debt-preferred-equity-explained)
[![Growth Equity vs Private Equity vs Venture Capital](https://ibinterviewquestions.com/assets/growth-equity-vs-private-equity-vs-venture-capital-CbTfWoN9.webp)\
\
#### Growth Equity vs Private Equity vs Venture Capital\
\
March 27, 2026](https://ibinterviewquestions.com/blog/growth-equity-vs-private-equity-vs-venture-capital)

Understanding Beta in Valuation
-------------------------------

Beta measures a stock's **sensitivity to overall market movements** and serves as a key input in the **Capital Asset Pricing Model (CAPM)** for calculating cost of equity. A beta of 1.0 means the stock moves in line with the market. Beta above 1.0 indicates the stock is **more volatile** than the market, while beta below 1.0 indicates **lower volatility**.

The concept matters for valuation because beta determines the **risk premium investors require** to hold a particular stock. Higher beta stocks demand higher expected returns to compensate for greater **systematic risk**. When you calculate [WACC for a DCF valuation](https://ibinterviewquestions.com/blog/how-to-calculate-wacc-guide)
, cost of equity depends directly on your beta assumption.

However, the beta you observe for a publicly traded company reflects **two distinct types of risk**: business risk from the company's operations and financial risk from its capital structure. Separating these risks is essential when applying beta from comparable companies to value a target with a different capital structure.

This distinction between levered and unlevered beta appears frequently in investment banking interviews and is fundamental to proper valuation methodology. Understanding when and why to unlever beta demonstrates **technical sophistication** that interviewers expect from strong candidates.

Levered vs. Unlevered Beta: Key Differences
-------------------------------------------

Before diving deeper into each concept, here is a side-by-side comparison of levered and unlevered beta.

| Feature | Levered Beta | Unlevered Beta |
| --- | --- | --- |
| **Also called** | Equity beta, observed beta | Asset beta |
| **Risk captured** | Business risk + financial risk | Business risk only |
| **Source** | Bloomberg, Capital IQ, Yahoo Finance | Calculated from levered beta |
| **Affected by debt?** | Yes, increases with leverage | No, independent of capital structure |
| **Use case** | Valuing company with current structure | Comparing risk across companies |
| **CAPM input?** | Yes, directly used in CAPM | No, must relever first |
| **Changes when D/E changes?** | Yes | No  |

This table highlights the core principle: **levered beta includes financial risk from debt**, while **unlevered beta isolates the operating risk** of the underlying business. The sections below explore each concept in detail.

What is Levered Beta?
---------------------

Levered Beta

Levered beta (also called equity beta) measures the systematic risk of a company's equity, reflecting both the inherent business risk of its operations and the additional financial risk created by debt in its capital structure. It is the beta you observe directly from market data.

Levered beta is what you find when you look up a company's beta on **Bloomberg, Capital IQ, or Yahoo Finance**. It measures the volatility of a company's stock returns relative to market returns and reflects both the underlying **business risk** and the additional risk from **financial leverage**.

When a company uses debt financing, **equity holders bear amplified risk**. If the business generates lower than expected returns, debt payments still must be made, leaving less for equity holders. Conversely, if returns exceed expectations, equity holders capture the upside after debt obligations. This leverage effect makes equity returns **more volatile** than the underlying business returns.

Consider two identical businesses with the same operating risk. Company A is financed entirely with equity, while Company B uses 50% debt. Company B's equity will be more volatile because the **fixed debt obligations amplify gains and losses** for shareholders. Company B's levered beta will be higher than Company A's, even though the underlying businesses have identical risk profiles.

**Levered beta captures total equity risk** including both:

*   **Business risk**: Volatility inherent in the company's operations, industry, and competitive position
*   **Financial risk**: Additional volatility created by debt in the capital structure

This combined measure is appropriate when valuing a company as it currently exists with its current capital structure. However, it becomes problematic when comparing companies with **different leverage levels** or applying beta to a company with a different target capital structure.

What is Unlevered Beta?
-----------------------

Unlevered Beta

Unlevered beta (also called asset beta) measures only the systematic business risk of a company's operations, with the effect of financial leverage removed. It represents the beta a company would have if it were financed entirely with equity and carried no debt.

Unlevered beta strips out the effect of financial leverage to isolate **pure business risk**. It represents the beta a company would have if it were financed entirely with equity and had no debt.

Unlevering beta removes the **financial risk component**, leaving only the operating risk inherent in the business itself. Two companies in the same industry with similar operations should have **similar unlevered betas** regardless of how they choose to finance themselves.

**Unlevered beta is useful for:**

*   Comparing risk across companies with **different capital structures**
*   Applying comparable company betas to a target company
*   Understanding the underlying business risk separate from financing decisions
*   Building up cost of equity for companies with different target leverage

The key insight is that **capital structure is a choice**, not an inherent characteristic of the business. A company can change its leverage over time through debt issuance, repayment, or equity offerings. Unlevered beta captures the risk that **cannot be changed** through financing decisions.

Understanding the relationship between levered and unlevered beta is essential for properly applying [comparable company analysis](https://ibinterviewquestions.com/blog/how-to-build-comparable-company-analysis)
 to valuation.

The Unlevering Formula
----------------------

To convert levered beta to unlevered beta, use this formula:

βunlevered\=βlevered1+(1−T)×DE\\beta\_{unlevered} = \\frac{\\beta\_{levered}}{1 + (1-T) \\times \\frac{D}{E}}βunlevered​\=1+(1−T)×ED​βlevered​​

Where:

*   **Beta unlevered** = Asset beta (what we are solving for)
*   **Beta levered** = Observed equity beta from market data
*   **T** = Marginal tax rate
*   **D** = Market value of debt
*   **E** = Market value of equity
*   **D/E** = Debt-to-equity ratio

The formula shows that **higher leverage increases levered beta** relative to unlevered beta. The **(1-T) term** accounts for the tax shield benefit of debt, which partially offsets the risk-increasing effect of leverage.

**Example calculation:**

A comparable company has:

*   Levered beta: 1.30
*   Debt-to-equity ratio: 0.40
*   Tax rate: 25%

βunlevered\=1.301+(1−0.25)×0.40\=1.301+0.30\=1.301.30\=1.00\\beta\_{unlevered} = \\frac{1.30}{1 + (1-0.25) \\times 0.40} = \\frac{1.30}{1 + 0.30} = \\frac{1.30}{1.30} = 1.00βunlevered​\=1+(1−0.25)×0.401.30​\=1+0.301.30​\=1.301.30​\=1.00

The unlevered beta of **1.00** represents the pure business risk, while the observed beta of **1.30** reflects both business risk and the financial risk from 40% debt-to-equity leverage.

The Relevering Formula
----------------------

Once you have unlevered beta (typically by averaging across comparable companies), you must **relever to the target company's capital structure** to calculate its cost of equity:

βlevered\=βunlevered×(1+(1−T)×DE)\\beta\_{levered} = \\beta\_{unlevered} \\times \\left(1 + (1-T) \\times \\frac{D}{E}\\right)βlevered​\=βunlevered​×(1+(1−T)×ED​)

This is simply the unlevering formula rearranged to solve for levered beta.

**Example calculation:**

You have determined that the industry unlevered beta is 1.00. Your target company has:

*   Target debt-to-equity ratio: 0.60
*   Tax rate: 25%

βlevered\=1.00×(1+(1−0.25)×0.60)\=1.00×(1+0.45)\=1.45\\beta\_{levered} = 1.00 \\times \\left(1 + (1-0.25) \\times 0.60\\right) = 1.00 \\times (1 + 0.45) = 1.45βlevered​\=1.00×(1+(1−0.25)×0.60)\=1.00×(1+0.45)\=1.45

The relevered beta of **1.45** is higher than the unlevered beta because the target company uses more leverage than the average comparable company. This higher beta will increase the cost of equity in your WACC calculation.

**Get the complete guide:** Download our comprehensive 160-page PDF covering valuation concepts, technical questions, and interview frameworks for investment banking. [Access the IB Interview Guide](https://ibinterviewquestions.com/ib-interview-guide)
 for complete preparation.

When to Unlever and Relever Beta
--------------------------------

Understanding **when this process is necessary** is as important as knowing the mechanics. Not every situation requires unlevering and relevering.

### When You Must Unlever and Relever

**Using comparable company betas:** When you derive beta from publicly traded comparable companies, you must unlever their observed betas, calculate an average or median unlevered beta, then relever to your target's capital structure. The comparables likely have **different leverage** than your target, making direct use of their levered betas inappropriate.

**Valuing private companies:** Private companies have no observable beta. You must estimate beta using public comparables, which requires the unlever-relever process to adjust for [capital structure differences](https://ibinterviewquestions.com/blog/private-company-valuation)
.

**Analyzing leverage changes:** If you are modeling a scenario where the company changes its capital structure (such as in an [LBO](https://ibinterviewquestions.com/blog/lbo-modeling-explained)
), you need to relever beta to the new capital structure to properly calculate cost of equity.

**Target capital structure differs from current:** Even for public companies, if you believe the optimal or target capital structure differs from current leverage, you should relever beta to the target structure for valuation purposes.

### When Direct Use May Be Appropriate

**Valuing the company as-is:** If you are valuing a public company with no expected capital structure changes and using its own historical beta, direct use of observed beta may be appropriate.

**Single comparable with identical structure:** In the rare case where you have one perfect comparable with the same capital structure as your target, you might use its levered beta directly. However, this situation is uncommon in practice.

**Quick approximations:** For rough analysis or screening purposes, direct beta comparisons may suffice. **Formal valuations** for transactions always require proper adjustment.

The Step-by-Step Process
------------------------

Here is the complete process for deriving beta from comparables and applying it to a target company.

1

Identify Comparable Companies

Select 4-8 publicly traded companies with similar business characteristics to your target, considering industry, size, growth profile, and geographic exposure.

2

Gather Data for Each Comparable

Collect the current levered beta, market value of debt, market value of equity, and marginal tax rate for each company.

3

Unlever Each Comparable's Beta

Apply the Hamada equation to strip out each company's financial leverage and isolate pure business risk.

4

Calculate Central Tendency

Take the median (preferred) or mean of the unlevered betas to find the industry asset beta.

5

Determine Target Capital Structure

Decide on the appropriate D/E ratio for your target, whether current, management target, or industry average.

6

Relever to Target Capital Structure

Apply the relevering formula using the target's D/E ratio and tax rate to get the appropriate equity beta.

7

Use Relevered Beta in CAPM

Plug the relevered beta into the CAPM formula with the risk-free rate and equity risk premium to calculate cost of equity.

When selecting your target capital structure in Step 5, common options include:

*   Current capital structure
*   Target or optimal capital structure per management
*   Industry average capital structure
*   Capital structure implied by your valuation assumptions

The relevered beta from Step 6 becomes the input for CAPM:

Re\=Rf+βlevered×(Rm−Rf)R\_e = R\_f + \\beta\_{levered} \\times (R\_m - R\_f)Re​\=Rf​+βlevered​×(Rm​−Rf​)

This cost of equity then flows into your [WACC calculation](https://ibinterviewquestions.com/blog/how-to-calculate-wacc-guide)
 and ultimately your DCF valuation. Understanding how each piece connects is essential for building [enterprise value bridges](https://ibinterviewquestions.com/blog/enterprise-value-vs-equity-value-guide)
 and arriving at a defensible equity value.

Practical Example
-----------------

Let's work through a complete example with multiple comparables.

**Target company:** Private manufacturing company **Target capital structure:** 35% debt, 65% equity (D/E = 0.54) **Target tax rate:** 25%

**Comparable company data:**

**Company A:**

*   Levered beta: 1.25
*   D/E ratio: 0.30
*   Tax rate: 25%
*   Unlevered beta: 1.25 / (1 + 0.75 x 0.30) = 1.25 / 1.225 = **1.02**

**Company B:**

*   Levered beta: 1.45
*   D/E ratio: 0.50
*   Tax rate: 25%
*   Unlevered beta: 1.45 / (1 + 0.75 x 0.50) = 1.45 / 1.375 = **1.05**

**Company C:**

*   Levered beta: 1.10
*   D/E ratio: 0.20
*   Tax rate: 25%
*   Unlevered beta: 1.10 / (1 + 0.75 x 0.20) = 1.10 / 1.15 = **0.96**

**Company D:**

*   Levered beta: 1.55
*   D/E ratio: 0.65
*   Tax rate: 25%
*   Unlevered beta: 1.55 / (1 + 0.75 x 0.65) = 1.55 / 1.49 = **1.04**

**Median unlevered beta:** (0.96, 1.02, 1.04, 1.05) -> Median = **1.03**

**Relever to target capital structure:**

βlevered\=1.03×(1+0.75×0.54)\=1.03×1.405\=1.45\\beta\_{levered} = 1.03 \\times (1 + 0.75 \\times 0.54) = 1.03 \\times 1.405 = 1.45βlevered​\=1.03×(1+0.75×0.54)\=1.03×1.405\=1.45

The target company's levered beta is **1.45**, which you would use in CAPM to calculate cost of equity.

Common Interview Questions
--------------------------

Beta concepts appear frequently in [technical interviews](https://ibinterviewquestions.com/blog/most-common-investment-banking-interview-mistakes)
. Here are questions you should be prepared to answer.

**"What is the difference between levered and unlevered beta?"**

Levered beta is the observed equity beta that reflects both **business risk** and **financial risk** from debt. Unlevered beta strips out financial leverage to isolate pure business risk. We unlever when using comparable company betas to value a target with different capital structure.

**"Why do we unlever beta?"**

Capital structure differs across companies, but **business risk should be similar** for comparable businesses. Unlevering removes the leverage effect so we can compare pure operating risk, then relever to the target's specific capital structure for an accurate cost of equity estimate.

**"What happens to beta as a company increases leverage?"**

Levered beta increases because equity holders bear more risk when debt increases. **Fixed debt obligations amplify equity returns** in both directions. The unlevered beta remains unchanged since it reflects only business risk.

**"Walk me through calculating cost of equity using comparable company betas."**

Gather levered betas and D/E ratios for comparables. Unlever each beta using the formula. Take the **median unlevered beta**. Relever to the target's capital structure. Use the relevered beta in CAPM with the risk-free rate and equity risk premium to calculate cost of equity.

**"Why do we multiply by (1-T) in the beta formulas?"**

The **tax shield** from interest expense reduces the effective cost of debt and partially offsets leverage risk. The (1-T) term accounts for this tax benefit. Higher tax rates mean a larger tax shield, so the leverage adjustment is smaller.

**Master interview fundamentals:** Practice 400+ technical and behavioral questions with AI-powered feedback. [Download our iOS app](https://ibinterviewquestions.com/)
 for comprehensive interview prep.

Common Mistakes to Avoid
------------------------

Several errors frequently occur when working with levered and unlevered beta. Knowing these pitfalls helps you avoid them in both modeling work and interview answers.

**Using book values instead of market values:** The D/E ratio should use **market value of debt** and **market value of equity**. Book values can significantly differ from market values, leading to incorrect beta adjustments.

**Forgetting to relever:** Some analysts unlever comparable betas but forget to relever to the target capital structure. The median unlevered beta is an **intermediate step**, not the final answer for cost of equity.

**Using inconsistent tax rates:** Apply each company's own tax rate when unlevering. When relevering, use the **target company's tax rate**. Mixing tax rates introduces errors.

**Ignoring outliers:** One comparable with unusual leverage or beta can skew your analysis. Use **median rather than mean**, and consider excluding clear outliers from your comparable set.

**Applying beta adjustments inappropriately:** Not every situation requires unlevering. If you are using a company's own beta with its current capital structure, direct use may be appropriate.

**Circular reference issues:** In some models, capital structure depends on equity value, which depends on WACC, which depends on capital structure. Be aware of these dynamics and **iterate or use target weights** to resolve the circularity.

Alternative Formulas
--------------------

Hamada Equation

The Hamada equation is the standard formula used in practice to convert between levered and unlevered beta. It assumes debt beta is zero and accounts for the tax shield benefit of debt through the (1-T) factor. Named after finance professor Robert Hamada, it is the expected formula in most investment banking interviews.

The formula presented above is the **Hamada equation**, which is most common in practice. However, you may encounter variations.

**Hamada equation (standard):**

βunlevered\=βlevered1+(1−T)×DE\\beta\_{unlevered} = \\frac{\\beta\_{levered}}{1 + (1-T) \\times \\frac{D}{E}}βunlevered​\=1+(1−T)×ED​βlevered​​

**Alternative assuming debt has beta:**

βunlevered\=βequity×E+βdebt×D×(1−T)E+D×(1−T)\\beta\_{unlevered} = \\frac{\\beta\_{equity} \\times E + \\beta\_{debt} \\times D \\times (1-T)}{E + D \\times (1-T)}βunlevered​\=E+D×(1−T)βequity​×E+βdebt​×D×(1−T)​

Most practitioners assume **debt beta is zero** for investment-grade companies, simplifying to the standard formula. For highly leveraged or distressed companies, incorporating debt beta may be more accurate.

The **Fernandez formula** and other variations exist in academic literature but are less common in practice. For interviews and most professional applications, the Hamada equation is standard.

Key Takeaways
-------------

*   **Levered beta** reflects both business risk and financial risk from leverage; it is what you observe in market data
*   **Unlevered beta** isolates pure business risk by removing the leverage effect
*   **Unlever comparable betas** to enable comparison across companies with different capital structures
*   **Relever to the target's capital structure** before using beta in CAPM for cost of equity
*   The formula accounts for the **tax shield** from debt through the (1-T) term
*   **Higher leverage increases levered beta** because equity holders bear amplified risk
*   Use **median unlevered beta** from comparables to reduce outlier impact
*   Always use **market values** for debt and equity in the D/E ratio

Conclusion
----------

The distinction between levered and unlevered beta is **fundamental to proper valuation methodology**. When you use comparable company betas without adjusting for capital structure differences, you introduce errors that can materially affect your cost of equity and ultimately your valuation conclusions.

The mechanics are straightforward: unlever to remove financial risk, find central tendency across comparables, relever to the target's structure. The key is understanding **why this process matters** and when it applies. Interviewers test this understanding because it reveals whether you grasp the relationship between capital structure, risk, and value.

For investment banking interviews, be prepared to explain the concept, walk through the formulas, and discuss the intuition behind why leverage affects beta. Demonstrating command of this topic signals **technical competence** that interviewers expect from candidates who will build and review valuation models daily.

As you build [DCF models](https://ibinterviewquestions.com/blog/walk-me-through-dcf-answer)
 and calculate WACC, proper beta treatment ensures your cost of capital reflects appropriate risk for the specific company you are valuing rather than the risk profile of different companies with different financing choices.

Frequently Asked Questions
--------------------------

### What is the difference between levered and unlevered beta?

### Why do you need to unlever beta when using comparable companies?

### How does increasing leverage affect a company's beta?

### What formula do you use to unlever beta?

### Should you use book value or market value for the debt-to-equity ratio when unlevering beta?

Explore More
------------

[![FIG: Financial Institutions Group in Banking](https://ibinterviewquestions.com/assets/fig-financial-institutions-group-banking-CkYNBe6W.webp)](https://ibinterviewquestions.com/blog/fig-financial-institutions-group-banking)

Guides

Technical

### [FIG: Financial Institutions Group in Banking](https://ibinterviewquestions.com/blog/fig-financial-institutions-group-banking)

Learn about the Financial Institutions Group in investment banking. Understand deal types, client base, required skills, and career paths in FIG.

January 7, 2026

[![Energy Investment Banking: Deals, Skills & How to Break In](https://ibinterviewquestions.com/assets/energy-investment-banking-guide-BYA6PTkU.webp)](https://ibinterviewquestions.com/blog/energy-investment-banking-guide)

Guides

Technical

### [Energy Investment Banking: Deals, Skills & How to Break In](https://ibinterviewquestions.com/blog/energy-investment-banking-guide)

Inside energy investment banking: oil & gas, renewables, and power deals. The technical skills you need, which banks lead the sector, and how to recruit into energy groups.

February 17, 2026

[![Staying in Investment Banking Long-Term: MD Track Explained](https://ibinterviewquestions.com/assets/investment-banking-md-track-career-BoPbCWNF.webp)](https://ibinterviewquestions.com/blog/investment-banking-md-track-career)

Guides

Behavioral

### [Staying in Investment Banking Long-Term: MD Track Explained](https://ibinterviewquestions.com/blog/investment-banking-md-track-career)

Explore the path to Managing Director in investment banking. Learn about each career stage, timeline expectations, what it takes to advance, compensation progression, and whether the MD track is right for you.

December 28, 2025

Ready to Transform Your Interview Prep?
---------------------------------------

Join 3,000+ students preparing smarter

[Download on App Store](https://apps.apple.com/app/apple-store/id6473167324?pt=126757215&ct=website&mt=8)
[![](https://ibinterviewquestions.com/assets/pdf-icon-CDdLRpwr.webp)Free Interview PDF Guide](https://ibinterviewquestions.com/ib-interview-guide)

Join 3,000+ students who have downloaded this resource

[![](https://ibinterviewquestions.com/assets/pdf-icon-CDdLRpwr.webp)Download Free PDF](https://ibinterviewquestions.com/ib-interview-guide)
[Download the App](https://apps.apple.com/app/apple-store/id6473167324?pt=126757215&ct=website&mt=8)