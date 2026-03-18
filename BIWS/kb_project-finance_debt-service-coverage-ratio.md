# Debt Service Coverage Ratio (DSCR): Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio

---

The Debt Service Coverage Ratio (DSCR): Full Guide to a Critical Metric in Project Finance
==========================================================================================

The Debt Service Coverage Ratio in Project Finance is defined as the Cash Flow Available for Debt Service (CFADS) in One Year / Debt Service in One Year, where the Debt Service equals the scheduled Interest + Principal Repayments for that year.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#tab-signup)
    

The Debt Service Coverage Ratio (DSCR): Full Guide to a Critical Metric in Project Finance

> **Debt Service Coverage Ratio (DSCR) Definition:** The Debt Service Coverage Ratio in Project Finance is defined as the Cash Flow Available for Debt Service (CFADS) in One Year / Debt Service in One Year, where the Debt Service equals the _scheduled_ Interest + Principal Repayments for that year.

We’ll define [Cash Flow Available for Debt Service (CFADS)](https://breakingintowallstreet.com/kb/project-finance/cash-flow-available-for-debt-service-cfads/)
 below, but let’s illustrate the DSCR with a simple example first.

Let’s say that the CFADS for an asset such as a solar plant in one year is $150.

The DSCR is 1.50x, which means the asset can support “Debt Service” of $150 / 1.50x = $100.

If the Debt balance here is $800 with a 10% Interest Rate, the Interest Expense is $80.

Therefore, the “allowed” or “sculpted” principal repayment in this period is $100 – $80 = $20 because this means the total Debt Service will be $100.

You can certainly calculate the DSCR for normal companies, but it is **most common** in [Project Finance & Infrastructure Modeling](https://breakingintowallstreet.com/project-finance-modeling/)
.

Its two primary use cases are:

1.  **Sizing and Sculpting Debt** – The simple above illustrates the “sculpting” process. We determine the maximum allowed Debt Service in one period, calculate the Interest Expense, and then back into the Principal Repayment based on that. Sizing the Debt in the beginning is trickier ([see our separate tutorial](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
    ) but uses related concepts.
2.  **Evaluating Credit Risk and Testing Loan Covenants** – For example, if the minimum DSCR is 1.30x, what happens in the Downside Case of your model? Does the DSCR ever fall below that minimum if there are operational problems, equipment wear-and-tear, or high expense inflation? What happens if a key customer cancels its contract?

### **Files & Resources:**

*   [The DSCR and LLCR in Project Finance – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-03/PF-03-DSCR-LLCR-Slides.pdf)
    
*   [Debt Sizing and Sculpting with VBA/Macro Support (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **0:42:** The Short Version
*   **4:30:** Part 1: Debt Sculpting and Sizing Uses (Quick Review)
*   **6:28:** Part 2: Additional Items and Complexities
*   **9:24:** Part 3: Variable Dates and Discount Rates
*   **11:22:** Part 4: Multiple Debt Tranches
*   **12:51:** Part 5: The DSCR and LLCR in Covenant Analysis
*   **14:47:** Recap and Summary

**How to Calculate the Debt Service Coverage Ratio and Cash Flow Available for Debt Service**
---------------------------------------------------------------------------------------------

In Project Finance, the Cash Flow Available for Debt Service is typically defined as follows:

*   **Cash Flow Available for Debt Service (CFADS)** = EBITDA – Maintenance Capex +/- Change in Working Capital – Cash Taxes

![Cash Flow Available for Debt Service (CFADS)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201825%20611'%3E%3C/svg%3E "Cash Flow Available for Debt Service (CFADS)")

The idea is to say, “How much cash flow does this asset generate on an _ongoing basis_ that is related to _just the asset in its current form_, ignoring future expansions and upgrades?”

We do not subtract the Interest Expense or Principal Repayments here because we’re assessing **how much is available _for_ that Debt Service**.

In an [LBO model](https://mergersandinquisitions.com/lbo-modeling-test/)
 for a normal company, the “Cash Flow Available for Debt Repayment” metric is slightly different.

For example, _all_ Capital Expenditures should be deducted – both Growth and Maintenance – and the Interest Expense is also deducted.

The definition differs because in the analysis of a normal company, the [Debt Schedule](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
 _determines_ the total Debt Principal Repayments it can make or how much extra it must borrow.

In other words, these Principal Repayments are not “fixed” in advance – other than small percentages for tranches like Term Loans – and are mostly linked to the company’s ability to repay Debt optionally.

By contrast, [in Project Finance](https://mergersandinquisitions.com/project-finance-vs-corporate-finance/)
, the Interest Expense and Principal Repayments are both **scheduled** in advance, so there’s nothing to “determine.”

Because of this pre-scheduling, the cash flows and Debt Schedule differ.

“Growth CapEx” is not deducted because growth initiatives in Project Finance typically have separate funding sources, such as new Debt or Equity raised specifically to fund these efforts (e.g., a new loan to fund the construction of an additional airport terminal).

By contrast, normal companies might re-invest some of their cash flow in new stores, factories, or equipment upgrades and don’t necessarily need separate funding for them.

In the CFADS calculation, many items affect the Cash Taxes, including the Interest Expense, the Depreciation of the asset’s initial price, and the Depreciation of the Maintenance CapEx:

![Taxable Income in CFADS](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201729%20660'%3E%3C/svg%3E "Taxable Income in CFADS")

These relationships may create **circular references**, which we can resolve with some simple VBA code for a “Copy/Paste Macro.”

**Nuances and Fine Print in the Debt Service Coverage Ratio Definition**
------------------------------------------------------------------------

Several additional items could go into CFADS, such as allocations to Reserve accounts for Maintenance CapEx, Decommissioning CapEx, and Working Capital.

These allocations **reduce** the asset’s cash flow because they require the owners to set aside cash flow today to pay for significant expenditures in the future:

![Cash Flow Available for Debt Service in a Mining Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202081%20521'%3E%3C/svg%3E "Cash Flow Available for Debt Service in a Mining Model")

Also, in some Project Finance models, there are **optional repayments** of the Debt principal, like the “[cash flow sweep](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-lbo/)
” concept in LBO models for normal companies.

In other words, if the asset generates $100 in CFADS in one period and spends only $70 on the Debt Service, it could optionally repay Debt principal with the remaining $30.

**These optional repayments are NOT part of the DSCR calculation because only scheduled Debt Service counts.**

Lenders do not necessarily _like_ being repaid early because it means they earn less interest and must reallocate their capital, but it depends on the context.

If a project is going “off the rails” (budget overruns, delays, problematic contracts, etc.), the lender might be fine with these early/optional Debt principal repayments so it can exit its investment more quickly and find something better.

![Project Finance & Infrastructure Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Project Finance Modeling for Energy, Transportation, and Mining Assets

*   #### Evaluate infrastructure deals like a pro
    
    You’ll evaluate the risks and rewards and make investment recommendations
    
*   #### Master financial modeling
    
    Model solar, wind, gas, nuclear, toll road, airport, and mining assets
    
*   #### Complete 8 case studies
    
    Build 4 shorter “crash course” models and 4 detailed “on the job” ones
    

[Full Details](https://breakingintowallstreet.com/project-finance-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Project-Finance-Modeling-Course-Outline.pdf)

**The Debt Service Coverage Ratio in the Debt Sculpting and Sizing Process**
----------------------------------------------------------------------------

For more details on this point, please see our [debt sculpting vs. debt sizing tutorial](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
.

But to summarize: If you use the DSCR to size and sculpt Debt, you need to use **Goal Seek** in Excel (Alt, A, W, G in the PC version) to size the initial Debt balance such that it reaches $0 by the maturity date or the end of the asset’s life.

For example, let’s say we’ve projected the CFADS for an asset and “guessed” the initial Debt balance at $800.

Then, we calculate the Interest Expense, Max Debt Service, and Debt Amortization in each period based on the interest rate (10%) and the minimum or targeted DSCR (1.50x here).

**Max Debt Service** = CFADS / DSCR, so it is $150 / 1.5x = $100 in Year 1.

We “back into” the Max Debt Amortization based on the Max Debt Service minus the Interest Expense this year:

![The Debt Service Coverage Ratio (DSCR) and Debt Principal Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201609%20674'%3E%3C/svg%3E "The Debt Service Coverage Ratio (DSCR) and Debt Principal Repayments")

**The results are not quite correct because we get a 1.52x DSCR in the final year, indicating the initial Debt balance was too low:**

![A DSCR That's Too High in the Final Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201448%201101'%3E%3C/svg%3E "A DSCR That's Too High in the Final Year")

This means we need to _resize_ the initial Debt.

To do this, we can set the balance to a higher number, such as $850, and use Goal Seek in the Year 10 cell to find the initial balance that results in $0 in Year 10.

This is the simplest possible method for Debt Sizing, but it lacks flexibility and is cumbersome to use in models because we need to use Goal Seek whenever anything changes.

It’s smarter to use the [Loan Life Coverage Ratio (LLCR)](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
 to size the initial Debt, but it requires more setup in Excel and may require VBA if we properly account for the Taxes and Interest.

**The Debt Service Coverage Ratio in Covenant Analysis**
--------------------------------------------------------

In Project Finance, as in standard corporate-level [Debt vs. Equity analysis](https://breakingintowallstreet.com/kb/debt-equity/debt-vs-equity-analysis/)
, lenders are always more concerned about the **downside risk** because their upside is very limited.

At best, they can earn the interest rates on their loans and, for more junior forms of Debt, potentially get a tiny percentage of equity or incentive payment.

**But if the project completely fails, they might lose all their money.**

Therefore, they often use metrics like the Debt Service Coverage Ratio, Loan Life Coverage Ratio, and Project Life Coverage Ratio to evaluate assets and quantify the risk they are assuming.

In some cases, they might even evaluate the initial development of an asset and then adjust the size of the loan based on whether they think the Upside Case, Base Case, or Downside Case is most likely in the operational period.

In other cases, they might assume a fixed loan size and evaluate how much these ratios fall in the downside scenarios.

If there’s serious default risk, they might establish new **covenants** that mandate a higher DSCR or LLCR or that require the asset to create a **Debt Service Reserve Account (DSRA)** to handle possible cash-flow shortfalls.

Here are a few examples, starting with a solar plant development with a 1.50x DSCR target in the Base Case (i.e., everything goes as planned):

![Solar Development Model Base Case - DSCR and LLCR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201994%201099'%3E%3C/svg%3E "Solar Development Model Base Case - DSCR and LLCR")

![Solar Development Model Extreme Downside Case - DSCR and LLCR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201998%201118'%3E%3C/svg%3E "Solar Development Model Extreme Downside Case - DSCR and LLCR")

The DSCR is only 1.10x in this Extreme Downside Case, but the lenders anticipated it and used less Debt in the beginning to account for this poor performance.

Even though the DSCR is lower, _the asset never falls below the minimum level_. The numbers at the end look like ~0 or below because the Debt has been completely repaid by then.

These ratios are **more interesting** when the Debt is _not_ sculpted and sized to match the future cash flows and is instead based on something like an [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/)
 multiple.

For example, here are the DSCR, CFADS, and 1.10x minimum DSCR covenant in the Base Case of an airport acquisition and expansion deal:

![Airport Model Base Case DSCR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201927%201112'%3E%3C/svg%3E "Airport Model Base Case DSCR")

And here they are in the Downside Case:

![Airport Model Downside Case DSCR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201930%201112'%3E%3C/svg%3E "Airport Model Downside Case DSCR")

**The asset does not even come close to complying with the 1.10x minimum DSCR in the Downside Case and falls short in several years of the Base Case.**

Therefore, the lenders in this deal would ask the owner/acquirer of the airport to significantly reduce the Debt so the asset complies with the 1.10x minimum.

Alternatively, they could also accept lower DSCR numbers but require a much higher interest rate or other terms to compensate them for the risk.

**However, there are limits to this, and 1.00x is usually the “bare minimum” for the DSCR in any context because a transportation asset like this one must be able to always service its Debt.**

It’s not like a high-growth tech company that can just “grow its way out” of an overly aggressive Debt burden because growth rates in this sector are limited.

**What Debt Service Coverage Ratio Do Lenders Typically Require?**
------------------------------------------------------------------

This varies widely based on the asset type and how much of the revenue is “locked in” by contracts such as Power Purchase Agreements (PPAs) or Offtake Agreements.

A rough set of guidelines might be:

*   **1.20x – 1.50x:** Lenders might accept these ratios for a simple asset with mostly “locked in” revenue, such as a small solar plant with rates and production governed 100% by a PPA with a nearby utility company. A regulated water utility or PPA-governed onshore wind farm might also fall in this category.
*   **1.50x – 2.00x:** This ratio might be used for riskier assets or those with less locked-in revenue (or no locked-in revenue). For example, an offshore wind farm with higher development and operating costs or a private roll road with revenue based on traffic volume and modestly escalated rates might be in this category.
*   **2.00x – 2.50x:** Energy assets without _any_ locked-in revenue could go here; natural resource assets (e.g., mines and oil & gas fields) might also qualify, even if they have a percentage of locked-in revenue via offtake agreements.
*   **2.50x – 3.50x+:** These higher DSCR levels are usually used for much riskier assets, such as mining developments without _any_ locked-in revenue that are subject to swings in commodity prices. Lenders need to protect against the risk of lithium or copper prices falling by 50% in one year.

The basic idea is simple: **The higher the risk, the higher the DSCR that lenders want to see.**

Also, note that there is a difference between DSCR _targets_ and DSCR _covenants_.

Debt may be sized and sculpted based on the targeted DSCR levels, but if the asset falls below those levels, it’s not necessarily the end of the world.

Lenders might not be happy, but if they receive their scheduled payments, they won’t necessarily impose penalties.

The _covenants_ are usually lower than the _targets_ and serve more like “hard requirements.”

If an asset falls below these minimums, the lenders might impose penalty fees, or, in extreme cases, even seize collateral, as all loans in Project Finance are secured against the specific assets used in the project.

[Sign Up for Project Finance Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Debt Sizing and Sculpting with VBA/Macro Support (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) The DSCR and LLCR in Project Finance - Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-03/PF-03-DSCR-LLCR-Slides.pdf)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Project Finance & Infrastructure Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[Learn More](https://breakingintowallstreet.com/project-finance-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Project Finance Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/2uXiVPKF/checkout)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with project finance and infrastructure modeling case studies. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/2uXiVPKF/checkout)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&mini=true)
[Email](mailto:?subject=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)

#### Project Finance & Infrastructure Modeling

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[LEARN MORE](https://breakingintowallstreet.com/project-finance-modeling/)

[](https://x.com/intent/tweet?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&mini=true)
[](mailto:?subject=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[](https://api.whatsapp.com/send?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Copy](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#)
[Email](mailto:?subject=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&t=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
[Pinterest](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#)
[Print](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[SMS](sms:?&body=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[X](https://x.com/intent/tweet?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-service-coverage-ratio%2F&title=The%20Debt%20Service%20Coverage%20Ratio%20%28DSCR%29%3A%20Full%20Guide%20to%20a%20Critical%20Metric%20in%20Project%20Finance&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand