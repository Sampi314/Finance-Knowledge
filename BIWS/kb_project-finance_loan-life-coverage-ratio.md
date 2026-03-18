# Loan Life Coverage Ratio (LLCR): Full Tutorial + Excel

**Source:** https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio

---

The Loan Life Coverage Ratio (LLCR): The Most Important Credit Stat in Project Finance?
=======================================================================================

The Loan Life Coverage Ratio (LLCR) in Project Finance equals the Present Value of All Cash Flow Available for Debt Service (CFADS) in the Remaining Debt Tenor / Current Debt Balance.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#tab-signup)
    

The Loan Life Coverage Ratio (LLCR): The Most Important Credit Stat in Project Finance?

> **Loan Life Coverage Ratio (LLCR) Definition:** The Loan Life Coverage Ratio in Project Finance equals the Present Value of All Cash Flow Available for Debt Service (CFADS) in the Remaining Debt Tenor / Current Debt Balance.

The **Cash Flow Available for Debt Service (CFADS)** equals EBITDA – Maintenance Capex +/- Change in Working Capital – Cash Taxes in simple models (but can get more complex in real life).

Before doing anything with the [Debt sizing or sculpting](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
 in a Project Finance model, we must forecast the [Cash Flow Available for Debt Service (CFADS)](https://breakingintowallstreet.com/kb/project-finance/cash-flow-available-for-debt-service-cfads/)
 in each period.

The **LLCR** is the “Present Value Version” of the [Debt Service Coverage Ratio (DSCR)](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
, and the two are equivalent when we size and sculpt the Debt based on one or the other (with a few exceptions).

For example, let’s say that in a simple Project Finance model, the asset’s CFADS grows from $150 to $250 over a 10-year period. The Debt also **matures** in Year 10, so its **tenor** at the start of the project is 10 years.

This Debt has a 10% interest rate attached, so the [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
 of the CFADS over this 10-year Debt tenor is $1,201.4, based on the [NPV](https://breakingintowallstreet.com/kb/finance/net-present-value/)
 function in Excel:

![Present Value of CFADS](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20559'%3E%3C/svg%3E "Present Value of CFADS")

If the Loan Life Coverage Ratio is 1.50x, this means that the **starting Debt balance** – how we initially fund the deal – should be $1,201.4 / 1.50x = $800.9:

![The Loan Life Coverage Ratio for Debt Sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201162%20399'%3E%3C/svg%3E "The Loan Life Coverage Ratio for Debt Sizing")

Since the LLCR and DSCR are **equivalent** in this simple example, the DSCR is also 1.50x in each period:

![DSCR with LLCR-Based Debt Sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201755%20740'%3E%3C/svg%3E "DSCR with LLCR-Based Debt Sizing")

We have **sized** the initial Debt balance based on the LLCR, which is one of its main use cases in models.

Its other main use case is to help lenders **evaluate credit risk and test loan covenants**.

For example, if the minimum LLCR specified by a loan covenant is 1.30x, does it ever fall below this level in the Downside Case of the model?

What happens if there’s higher expense inflation, a contract cancellation, or a budget overrun in the asset’s development?

### **Files & Resources:**

*   [The DSCR and LLCR in Project Finance – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-03/PF-03-DSCR-LLCR-Slides.pdf)
    
*   [Simple Project Finance Model with LLCR-Based Debt Sizing (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-03/PF-03-LLCR-Debt-Sizing.xlsx)
    
*   [Simple Project Finance Model with Debt Sizing, Sculpting, and LLCR (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **0:42:** The Short Version
*   **4:30:** Part 1: Debt Sculpting and Sizing Uses (Quick Review)
*   **6:28:** Part 2: Additional Items and Complexities
*   **9:24:** Part 3: Variable Dates and Discount Rates
*   **11:22:** Part 4: Multiple Debt Tranches
*   **12:51:** Part 5: The DSCR and LLCR in Covenant Analysis
*   **14:47:** Recap and Summary

**How to Calculate the Loan Life Coverage Ratio and Use It In Real Life**
-------------------------------------------------------------------------

In most models, we don’t “calculate” the LLCR; instead, we already know what it is and use it to back into the starting Debt balance, as in the example above.

Continuing with this example, the next step is to calculate the Interest Expense each year based on the 10% rate \* the starting balance.

We can then back into the “allowed” Amortization each year based on the 1.50x DSCR (since the LLCR equals the DSCR when the Debt is sculpted/sized based on one or the other):

![Sculpted Amortization](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201624%20733'%3E%3C/svg%3E "Sculpted Amortization")

As stated in [the DSCR article](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
, the Debt Service Coverage Ratio includes only _scheduled_ Interest Expense and Principal Repayments – not optional ones or “prepayments.”

The definition of CFADS is also discussed more fully in [the DSCR article](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
, so we recommend reviewing that for the details.

Stepping back from this example, if you wanted to _calculate_ the LLCR in each year of this model, you could do so with a simple NPV function in Excel divided by the Debt balance in the year:

![LLCR Calculation with NPV Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201049'%3E%3C/svg%3E "LLCR Calculation with NPV Function")

Note that we **anchor** cell O18 for the Year 10 CFADS because we do not want this to shift around at all – it should always stay in place because the Debt always matures at the end of Year 10.

**Why the Loan Life Coverage Ratio is Better Than the DSCR for Sizing and Sculpting Debt**
------------------------------------------------------------------------------------------

When you use the LLCR to **size** the initial Debt balance, you do not need to use Goal Seek in Excel – everything updates when there’s a change in the Interest Rate, the CFADS in the period, or other factors.

However, using the LLCR to size the Debt does **not** resolve the issue with [circular references](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
.

Specifically, the Taxes in the CFADS calculation change based on the Interest Expense, but the Interest Expense is affected by the Taxes since the CFADS determines the initial Debt balance.

To resolve that, we need simple VBA code for a copy/paste macro (see the [Debt sizing/sculpting tutorial](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
).

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

**The Loan Life Coverage Ratio with Variable Dates and Discount Rates**
-----------------------------------------------------------------------

If we’re building a more complex model with variable issuance and maturity dates for the Debt and a variable Discount Rate (e.g., the Debt Interest Rate equals the Benchmark Rate + 5.0%, and the Benchmark Rate changes over the years), the LLCR calculation gets more complex.

The **easiest approach** in this case is to create a “flag” for the Debt Tenor at the top of the schedule and to calculate the PV of CFADS during the Debt Tenor based on this flag, a running cumulative sum, and the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
 in each period.

Here’s an example:

![PV of CFADS with Variable Dates and Discount Rates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201950%201013'%3E%3C/svg%3E "PV of CFADS with Variable Dates and Discount Rates")

It “works” because we _start at the end_ and “go back” to _the start of the period_, so we only have to worry about discounting the CFADS and the running sum at the appropriate Discount Rate for each specific period.

With the PV of CFADS and Debt balance in each period, it’s the standard LLCR calculation:

![LLCR Calculation with Variable Dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201957%201152'%3E%3C/svg%3E "LLCR Calculation with Variable Dates")

**The Loan Life Coverage Ratio with Multiple Tranches of Debt**
---------------------------------------------------------------

If we’re building a model with multiple tranches of Debt, the approach shown above also works, but we need to calculate the **weighted average interest rate** in each period.

To do that, we need to know the split between the initial tranches, such as 70% in the First Lien and 30% in the Second Lien.

If we don’t know this percentage split, there’s no way to calculate the LLCR because we don’t know the weighted average interest rate.

Here’s an example:

![LLCR Calculation with Two Debt Tranches](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201963%20962'%3E%3C/svg%3E "LLCR Calculation with Two Debt Tranches")

Sizing and sculpting multiple Debt tranches with this setup gets more complicated and requires us to calculate a “local” LLCR for each tranche based on its specific interest rate; we may cover this topic in a separate article.

**When Does the Loan Life Coverage Ratio NOT Equal the Debt Service Coverage Ratio?**
-------------------------------------------------------------------------------------

In more complex models with features such as **grace periods** (i.e., no Debt Service or no Interest Expense for a certain period), plenty of factors could cause the LLCR and DSCR to be mismatched, even if the initial Debt is sized and sculpted based on one of them.

But in simple cases, there are two main model issues that might cause a mismatch:

1.  **Optional Debt Repayments or the Cash Flow Sweep** – Since the DSCR and LLCR are based on only _scheduled_ Debt Service, they don’t work as intended if there are prepayments or optional repayments of the principal; these repayments distort the Debt balance and make it lower than expected.
2.  **Insufficient Cash Flow to Service the Debt** – For example, if the Debt is sized and sculpted based on a 1.50x LLCR and DSCR, and the schedule Debt Service in one period is $100, but the CFADS is only $80, the asset cannot possibly meet the 1.50x minimum because the CFADS can’t even pay for the minimum Debt Service.

Outcome #2 should not happen with the appropriate assumptions, but it could happen in real life, especially with riskier assets that are more subject to cost overruns (e.g., offshore wind farms).

Outcome #1 is quite common in any models with support for cash flow sweeps (see: our [Debt Schedule tutorial](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
). Here’s an example:

![LLCR Calculation with a Cash Flow Sweep](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202092%201106'%3E%3C/svg%3E "LLCR Calculation with a Cash Flow Sweep")

The interpretation depends on the **context** (i.e., _why_ this happened).

If lenders want to exit their investment earlier than initially planned because it’s performing poorly, they might be fine with this faster repayment.

But in general, lenders prefer to be repaid as originally scheduled so they can maximize their returns without having to redeploy the capital elsewhere.

**The Loan Life Coverage Ratio in Covenant Analysis**
-----------------------------------------------------

Because lenders have extremely limited upside in any deal – whether for a normal company or in a Project Finance setting – they are always more concerned with the **downside risk**.

They often use metrics like the DSCR and LLCR not only to size and sculpt Debt, but also to determine the **covenants** that the asset must comply with.

For example, they might size the Debt based on a **1.50x LLCR target**, but there might be **a 1.20x LLCR covenant**.

So, if something goes wrong with the asset, the lenders could potentially charge penalty fees, restrict the asset’s activities, or, in the worst case, even seize collateral in dire situations.

One of the most common restrictions is the **Cash Trap**, which limits the dividends an asset can distribute if the LLCR, DSCR, or other metrics fall below a certain level.

Sometimes, it also requires **Reserve accounts** to be fully funded so that large upcoming spending needs (e.g., for replacement parts or decommissioning) can be funded without reducing the CFADS in a future period (without the Reserves, it would fall due to very high Maintenance CapEx).

Here’s an example taken from our lithium mining development model:

![LLCR Test in a Cash Trap to Restrict Dividends](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202135%20519'%3E%3C/svg%3E "LLCR Test in a Cash Trap to Restrict Dividends")

If this type of Cash Trap forces the asset to postpone dividend payments, the **equity IRR** will decrease due to [the time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
.

The equity investors might eventually earn their dividends, but they’ll receive them later – after the asset has come into compliance with the LLCR and DSCR and other requirements.

And since money today is worth more than money tomorrow, [this will reduce their IRR](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
, even if the multiple of invested capital stays the same.

But the LLCR can be used in dozens of ways when drafting loan terms and covenants; this is just a simple example that often comes up in Project Finance models.

[Sign Up for Project Finance Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Project Finance Model with LLCR-Based Debt Sizing (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-03/PF-03-LLCR-Debt-Sizing.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Project Finance Model with Debt Sizing, Sculpting, and LLCR (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    
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

[X](https://x.com/intent/tweet?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&mini=true)
[Email](mailto:?subject=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)

#### Project Finance & Infrastructure Modeling

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[LEARN MORE](https://breakingintowallstreet.com/project-finance-modeling/)

[](https://x.com/intent/tweet?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&mini=true)
[](mailto:?subject=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[](https://api.whatsapp.com/send?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Copy](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#)
[Email](mailto:?subject=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&t=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
[Pinterest](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#)
[Print](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[SMS](sms:?&body=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[X](https://x.com/intent/tweet?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Floan-life-coverage-ratio%2F&title=The%20Loan%20Life%20Coverage%20Ratio%20%28LLCR%29%3A%20The%20Most%20Important%20Credit%20Stat%20in%20Project%20Finance%3F&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand