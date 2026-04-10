# Portfolio optimization and the Alter Domus Score: A use case for CLOs - Alter Domus

**Source:** https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos

---

[Skip to content](https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos/#content)

Analysis

Portfolio optimization and the Alter Domus Score: A use case for CLOs
=====================================================================

Why the Alter Domus Scores’ simplicity, robustness, and capacity for automation makes it an effective metric for trade optimization.

* * *

Rudolph Bunja

Head of Portfolio Credit Risk

30 May 2025

![colleagues celebrating success](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202560%201707%22%3E%3C/svg%3E)

**Overview**

Alter Domus recently introduced the [Alter Domus Score (ADS)](https://alterdomus.com/insight/the-ad-score-an-objective-framework-for-optimal-portfolio-allocation/)
, a metric for fixed income assets that managers can use to improve their portfolio trade optimization decisions. The ADS is unit-based and can be applied universally across all types of fixed income assets, allowing managers to rank order assets based on relative value. The ADS is useful for managers when considering portfolio allocation tradeoffs where constraints exist. These constraints can be market, investor, or regulatory based.

In this paper, collateralized loan obligations (CLOs) are referenced as a use case to demonstrate how a CLO manager can apply the ADS framework to help optimize portfolio allocations. An example of ADS portfolio optimization in a typical environment for CLO managers is presented. The objective of the CLO manager in this case is to maximize the overall portfolio ADS while adhering to various constraints.

The examples first cover the case for a single CLO portfolio and then expand to a scenario in which a CLO manager seeks to optimize its portfolio allocations across multiple CLO portfolios. The goal is to provide an overview of the practical applications of the ADS framework.

**Portfolio optimization and ADS: a use case for CLOs**

A typical US-based CLO portfolio includes primarily first-lien senior secured loans to corporate borrowers. These portfolios are managed actively, with trading adhering to reinvestment criteria outlined in the CLO’s indenture. The lifecycle of a CLO usually includes a ramp-up period, a reinvestment period, and an amortization period.

The reinvestment criteria establish the rules within which the asset manager can trade. In addition to defining the types of assets that can be purchased (such as eligible collateral obligations), these criteria generally include various categories of portfolio-level constraints [\[1\]](https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos/#_ftn1)
:

*   Portfolio concentration limitations,
*   Collateral quality tests, and
*   Coverage tests.

To enhance the efficiency and productivity of investable capital while adhering to reinvestment criteria, managers carefully navigate various trade-offs in portfolio allocation decisions. By adopting a trade optimization approach, managers effectively refine their investment choices so that they strike the right balance between risk and return. This strategic method not only maximizes capital utilization but also aligns with the overarching investment goals.

A CLO manager has a range of metrics to optimize, such as yield, portfolio par, or average life. In this context, we previously outlined the benefits of utilizing ADS as a foundation for potentially enhancing optimization or generating trade ideas. The ADS, unlike other metrics, offers a parsimonious, objective, and easy-to-use measure that is ideal for trade optimization.

It is important to recognize that, beyond the general reinvestment criteria outlined in the CLO indenture, managers are faced with additional key external constraints dictated by market conditions – specifically, the array of investments available for purchase as well as prevailing market prices. Consequently, fundamental questions arise, such as determining the universe of eligible assets available for acquisition and their corresponding prices. Furthermore, it is necessary to consider whether asset substitutions within the existing portfolio could lead to a more optimal solution. This consideration applies to prospective assets in both the primary and secondary loan markets. Incorporating robust trade optimization methods and tools, alongside the manager’s credit and trading expertise, enhances the manager’s ability to balance a portfolio’s risk-return profile while adhering to constraints.

Exhibit 1 outlines the primary objective of maximizing the overall weighted average ADS, in accordance with the constraints generally specified by a CLO indenture. The exhibit includes examples of typical constraints applicable to a CLO, assuming that any asset under consideration meets the eligibility criteria for purchase. In other words, the goal is to find the optimal asset weights in a portfolio that will maximize ADS while adhering to specified constraints [\[2\]](https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos/#_ftn2)
.

**Exhibit 1: ADS optimization objective for a typical CLO portfolio**

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20900%20546%22%3E%3C/svg%3E)

In theory, there could be multiple optimal solutions due to various possible portfolio compositions that could meet all constraints, though in practice this is a remote possibility. Typically, some flexibility remains within certain constraints given the available assets and considering a CLO manager’s discretion. In many CLOs, specific tests can often be adjusted, allowing room for one test (like recovery rate) to impact (or modify) the WARF or WAS test. This ultimately leads to finding a more optimal solution, assuming the manager determines that the tradeoff is justified.

**Portfolio allocations across CLOs**

The optimization objective described above pertains to a single CLO portfolio. However, CLO managers often oversee multiple CLOs simultaneously as they are repeat issuers. The complexity increases as these CLOs may have been issued under different market conditions over time. Additionally, there could be some differences in the constraints applicable to each CLO. Other examples include varying experiences in ratings migration within the portfolio, and some CLOs may be at different stages in their lifecycle, such as during reinvestment or amortization periods. These factors contribute to the complexity of constraints.

In the simplest scenario, the ADS can be optimized independently for each CLO, assuming there are no constraints on the availability of assets to be purchased or traded. In this case, the proportion of allocation to each individual asset is chosen optimally to provide the maximum marginal increase to the ADS for each CLO portfolio. Therefore, it is possible for the optimal portfolio allocation of any prospective asset to range from 0% to 100% for any given CLO.

However, it is not straightforward in practice. The following scenarios are examples that point out potential constraints that may limit an optimal solution across CLO portfolios:

*   Limited availability – the CLO manager may encounter a limited supply of certain assets within the marketplace.
*   Legal/compliance requirements – the CLO manager may be subject to internal directives imposed by legal and compliance guidelines, which govern asset allocations across the manager’s CLOs.

**Exhibit 2: Potential portfolio allocations to a loan under various scenarios**

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20900%20546%22%3E%3C/svg%3E)

Exhibit 2 above provides an example of a manager looking to reinvest cash proceeds with potential allocations for a particular loan, Loan #1, across three CLOs. The optimal allocation suggests that a total of $16MM should be distributed across the CLOs as shown in the unconstrained scenario. This assumes that the optimal solution is based on the maximization objective described earlier, where the analysis is subject to each individual CLO’s constraints.

If the manager determines that only $10MM of Loan #1 is available, the optimal solution (assuming the greatest marginal benefit is realized by CLO #3) then suggests a different allocation accordingly as shown in the constrained scenario. The analysis also suggests that the remaining $6MM of cash proceeds should be invested in two additional loans, Loan #2 and Loan #3, with respective allocations.

In instances where there is a strict legal or compliance requirement for proportional distribution of the asset, the process is straightforward. Although internal guidelines may recommend a specific portfolio allocation for an individual investment, various factors related to any CLO could prevent this. These factors include potential breaches of certain portfolio constraints, such as limits on borrower, industry, or rating concentrations.

It is understood that these additional limitations result in a suboptimal solution compared to the theoretical unconstrained case – essentially, we could say that this solution is the ‘optimal practical’ solution.

This example suggests that an iterative process would likely occur in practice to find an optimal practical solution, especially if the analysis is conducted on a pro forma basis or after the manager learns what is ultimately available in the marketplace, potentially even with changes in market prices.

**To conclude**

Fixed income managers often consider tradeoffs when making investment decisions to efficiently deploy investable capital. Alter Domus has introduced the ADS as a basis for managers to enhance their portfolio trade optimization decisions based on one objective and sound metric that is applicable across all fixed income investments. The ADS can be particularly useful in helping managers achieve the best relative value for their investments while facing constraints.

CLOs have been presented as a use case to demonstrate how a CLO manager can apply the ADS framework to optimize portfolio allocations. The example described earlier illustrated ADS portfolio optimization in an environment typical for CLO managers. The objective of the CLO manager is to maximize the overall portfolio ADS while adhering to various constraints as outlined in a CLO indenture. While managers can use other variables such as yield or portfolio par to optimize their portfolio, it has been demonstrated that using the ADS as an alternative metric can be beneficial since it incorporates into _one measure_ the major variables considered in trading credit instruments.

The ADS serves as an effective metric for trade optimization, thanks to its simplicity, robustness, and capacity for automation. Its straightforward nature allows for easy interpretation, while its consistency supports investment decision-making across different market conditions for fixed income investments. Additionally, the automation aspect streamlines the optimization process, making it a valuable tool for enhancing trading strategies.

For AD clients, including clients of Solvas and Enterprise Credit & Risk Analytics, the ADS is offered as an additional measure to support our clients with their trade optimization, portfolio allocation, and risk analytics.

Please contact [\[email protected\]](https://alterdomus.com/cdn-cgi/l/email-protection#cd88bfa4aee399aca3a3a8a3afacb8a08daca1b9a8bfa9a2a0b8bee3aea2a0)
 for further information on how to access the ADS.

* * *

[\[1\]](https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos/#_ftnref1)
 The reinvestment criteria often involve more detailed requirements than mentioned here. These include par maintenance conditions, variations in criteria based on different trading classifications (such as credit risk/improved, defaulted or discretionary), and can vary depending on the CLO’s lifecycle stage. Additionally, the criteria can differ across CLOs with trading conditions that may be agreed upon between parties before the CLO’s inception, such as deep discount conditions, excess Caa/CCC haircut conditions, or amend to extend guidelines.

[\[2\]](https://alterdomus.com/insight/portfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos/#_ftnref2)
 Alter Domus utilizes a mixed integer linear programming platform to find the optimal solution for these situations. This method of optimization is well-documented in scientific literature.

* * *

* * *

* * *

*   [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Falterdomus.com%2Finsight%2Fportfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos%2F&title=Portfolio%20optimization%20and%20the%20Alter%20Domus%20Score%3A%20A%20use%20case%20for%20CLOs)
    
*   [Email this Page](https://x.com/share?url=https%3A%2F%2Falterdomus.com%2Finsight%2Fportfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos%2F&text=Portfolio%20optimization%20and%20the%20Alter%20Domus%20Score%3A%20A%20use%20case%20for%20CLOs)
    
*   [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Falterdomus.com%2Finsight%2Fportfolio-optimization-and-the-alter-domus-score-a-use-case-for-clos%2F&title=Portfolio%20optimization%20and%20the%20Alter%20Domus%20Score%3A%20A%20use%20case%20for%20CLOs)
    

Insights
--------

![Technology data on screen plus fountain pen and notepad](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 9, 2026

#### Consistency at Scale: Private Equity’s Data Challenge

[Read article](https://alterdomus.com/insight/consistency-at-scale-private-equity-data/)

[](https://alterdomus.com/insight/consistency-at-scale-private-equity-data/)

![Location in New York](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 7, 2026

#### The $12.9 Million Hidden Cost of Fragmented Data

[Read article](https://alterdomus.com/insight/the-12-9-million-hidden-cost-of-fragmented-data/)

[](https://alterdomus.com/insight/the-12-9-million-hidden-cost-of-fragmented-data/)

![Gherkin architecture](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 1, 2026

#### When Borders Become Background: Operating Across Jurisdictions

[Read article](https://alterdomus.com/insight/operating-across-jurisdictions-private-markets/)

[](https://alterdomus.com/insight/operating-across-jurisdictions-private-markets/)