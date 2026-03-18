# Debt Sculpting vs Debt Sizing in Project Finance

**Source:** https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing

---

Debt Sculpting vs Debt Sizing in Project Finance: Full Tutorial
===============================================================

In Project Finance, Debt Sculpting means that the required principal repayment in each period changes based on the available cash flows, the interest expense, and the targeted coverage ratio; Debt Sizing means that you set the initial Debt balance such that it is completely repaid on a certain date based on these sculpted principal repayments and the other Debt terms.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#tab-signup)
    

Debt Sculpting vs Debt Sizing in Project Finance: Full Tutorial

> **Debt Sculpting vs Debt Sizing Definition:** In Project Finance, Debt Sculpting means that the required principal repayment in each period changes based on the available cash flows, the interest expense, and the targeted coverage ratio; Debt Sizing means that you set the initial Debt balance such that it is completely repaid on a certain date based on these sculpted principal repayments and the other Debt terms.

In most financial models for “normal companies,” such as [leveraged buyout models](https://mergersandinquisitions.com/lbo-modeling-test/)
 and [debt vs. equity models](https://breakingintowallstreet.com/kb/debt-equity/debt-vs-equity-analysis/)
, the initial Debt balance is based on a multiple of [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/)
 or a percentage of the purchase price.

**But in Project Finance, Debt tends to be sculpted and sized based on the future cash flows because these cash flows are very predictable due to contracts that lock in prices and volumes, such as power purchase agreements (PPAs) in the energy sector.**

Some assets, such as solar and wind plants, are _seasonal_, so their cash flows fluctuate each month, but they are still _predictable_ because we know the high and low seasons in advance.

Linking the **Debt Service** – the Interest Expense + Principal Repayments – to the cash flow in each period **reduces the risk for the lenders** because it allows for more repayment when the cash flows are stronger and less when they are weaker.

Equity investors also like this approach because it often means they can **use more Debt** to fund deals, which increases their potential returns if a development or acquisition performs well.

Debt based on a multiple of the project’s initial EBITDA **would ignore future cash-flow growth** and, therefore, increase the required Equity by reducing the initial Debt.

By linking the Debt to these future cash flows, investors ensure the maximum Debt possible is used, within the constraints desired by the lenders.

### **Files & Resources:**

*   [Debt Sculpting vs Debt Sizing – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-Debt-Sculpting-vs-Debt-Sizing-Slides.pdf)
    
*   [Simple “Cash Flow Only” Debt Sculpting vs Debt Sizing with No VBA or Circular References (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-LLCR-Debt-Sizing.xlsx)
    
*   [Debt Sizing and Sculpting with VBA/Macro Support (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **1:09:** Part 1: The TL;DW of Debt Sculpting and Sizing
*   **3:07:** Part 2: Simple Debt Sculpting Example
*   **4:49:** Part 3: DSCR-Based Debt Sizing
*   **7:10:** Part 4: LLCR-Based Debt Sizing
*   **9:25:** Part 5: VBA to Automate Debt Sizing and Avoid Circ Ref’s
*   **17:24:** Recap and Summary

**Simple Debt Sculpting vs Debt Sizing Example**
------------------------------------------------

“Sculpting” Debt is not complicated; the tricky part is sizing it initially.

Here’s a simple example of Debt Sculpting: Let’s say the Cash Flow in a period is $150, and the targeted [Debt Service Coverage Ratio (DSCR)](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
 is 1.5x.

The asset can, therefore, support Debt Service of $150 / 1.5x = $100.

If the initial Debt balance is $800 with a 10% interest rate, the Interest Expense is $80.

Therefore, the “sculpted” principal repayment in this period is $100 – $80 = $20. This will increase each year as the Cash Flow grows and the Interest Expense falls.

The **hard part** is the Debt Sizing – in other words, determining that this initial balance _should be_ $800 (see below).

**Simple Debt Sculpting vs Debt Sizing Example Based on the Debt Service Coverage Ratio (DSCR)**
------------------------------------------------------------------------------------------------

The simplest approach to Debt Sizing is to base it on a key credit metric in Project Finance: **The Debt Service Coverage Ratio (DSCR) or the Loan Life Coverage Ratio (LLCR).**

The required formulas are as follows:

*   **Cash Flow Available for Debt Service (CFADS)** = EBITDA – Maintenance Capex +/- Change in Working Capital – Cash Taxes
*   **Debt Service Coverage Ratio (DCSR)** = CFADS in One Year / Debt Service in One Year
*   **Loan Life Coverage Ratio (LLCR)** = Present Value of All CAFDS in Remaining Debt Tenor / Current Debt Balance

The LLCR is the “Present Value version” of the DSCR, and **the two are equivalent when we size and sculpt the Debt based on one or the other** (with some exceptions in more advanced cases).

We’ll start with a simple Debt Sizing example based on the DSCR.

If we’ve projected the [CFADS](https://breakingintowallstreet.com/kb/project-finance/cash-flow-available-for-debt-service-cfads/)
 for an asset, Step 1 is to “guess” the initial Debt balance ($800 in this ongoing example).

Then, we calculate the Interest Expense, Max Debt Service, and Debt Amortization in each period based on the interest rate (10%) and the minimum or targeted DSCR (1.50x here).

Max Debt Service = CFADS / DSCR, so it is $150 / 1.5x = $100 in Year 1.

We “back into” the Max Debt Amortization based on the Max Debt Service minus the Interest Expense this year:

![The DSCR for Debt Sculpting vs Debt Sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201224%20992'%3E%3C/svg%3E "The DSCR for Debt Sculpting vs Debt Sizing")

**With these assumptions, the Debt balance reaches $0 by Year 10, but the DSCR is 1.52x in this final year, which means we used too little Debt initially.**

Therefore, we need to _resize_ the initial Debt balance.

To do this, we can set the initial balance to a higher number, such as $850, and then use **Goal Seek** (Alt, A, W, G in PC Excel) in the Year 10 cell to find the initial balance that results in a $0 balance in Year 10.

This is the simplest possible method for Debt Sizing, but it lacks flexibility and is cumbersome to use in models because we need to use Goal Seek whenever anything changes.

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

**Improved Debt Sculpting vs Debt Sizing with the Loan Life Coverage Ratio (LLCR)**
-----------------------------------------------------------------------------------

We can resolve some of these issues by sizing the Debt based on the [loan life coverage ratio](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
 instead.

We can solve for the initial Debt balance using algebra:

*   **Initial LLCR** = Present Value (PV) of All CFADS in Entire Debt Tenor / Initial Debt Balance
*   **LLCR \* Debt Balance** = PV of All CFADS
*   **Debt Balance** = PV of All CFADS / LLCR

Here’s the Excel setup:

![LLCR-Based Debt Sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201508%20610'%3E%3C/svg%3E "LLCR-Based Debt Sizing")

The [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
 from Years 1 to 10 is $1,201.4, so the Initial Debt Balance = $1,201.4 / 1.50x = $800.9.

**We do not need to change anything else because the targeted DSCR and targeted LLCR are equivalent.**

**So, we can use the targeted LLCR to determine the Max Debt Service in each period; it’s still CFADS / 1.50x.**

This method is better than Goal Seek because everything updates automatically if the CFADS, Interest Rate, or LLCR change.

However, it works only if we ignore the **circular relationship** between Interest, Taxes, and Debt Sizing, which comes up when we calculate the Cash Flow Available for Debt Service (CFADS) “the real way.”

**Why Debt Sizing Creates Circular References**
-----------------------------------------------

To explain these issues, we must calculate CFADS by starting with Revenue, subtracting Operating Expenses, and then deducting Maintenance CapEx, Cash Taxes, and the [Change in Working Capital](https://breakingintowallstreet.com/kb/financial-statement-analysis/change-in-working-capital/)
.

Since the Interest Expense is tax-deductible, the Cash Taxes will change based on the Interest Rate, the initial Debt balance, and the Debt principal repayments.

If we set it up this way and make the Interest Expense a tax deduction when calculating Cash Taxes, we get the following “circular death loop”:

![Circular References from Debt Sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201512%201010'%3E%3C/svg%3E "Circular References from Debt Sizing")

We could solve this issue by **enabling circular references in Excel**, but that makes models less stable, and some groups do not accept models with circular references (for more, see [our tutorial on circular references in Excel](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
).

Another option is to use **pre-tax numbers** and ignore the tax deduction for the Interest Expense, but that results in less accurate Debt balances.

**Debt Sculpting vs Debt Sizing with a Copy/Paste VBA Macro**
-------------------------------------------------------------

The **real way** to fix this problem is to use [VBA](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
 to create a “copy / paste macro” that “tricks” the model into using a hard-coded of the CFADS rather than the calculated one.

To do this, we’ll **copy** the calculated CFADS, **paste** it as hard-coded values, and **feed** this hard-coded version into the model.

Then, we’ll calculate the CFADS series again, copy and paste them as hard-coded values, feed them into the model, and keep doing that until the calculated and pasted CFADS are the same.

Essentially, we’re “tricking” Excel into thinking that the pasted CFDAS is the same as the calculated CFADS, thereby avoiding true circular references.

To set this up, start by creating a separate “Macros” tab in Excel that can store the calculated and pasted CFADS, and **name each range of cells** so you can easily refer to them in the macro.

We’ll also need a “Check / Comparison” cell that sums up each series and determines the difference between them:

![Named Ranges for VBA Copy/Paste Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201499%20456'%3E%3C/svg%3E "Named Ranges for VBA Copy/Paste Macro")

Next, on the main Model tab, link the pasted CFADS from the Macros tab and change all the formulas referencing the CFADS to use the _pasted version_ instead:

![Model Links for VBA Copy/Paste Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201503%20859'%3E%3C/svg%3E "Model Links for VBA Copy/Paste Macro")

Also, change the NPV formula used in the “Present Value of CFADS Over Debt Tenor” in the top area to reference these pasted CFADS values.

To **automate** this process, we can write a macro to repeat these steps until the sums of the two cell ranges (“CFADS\_Paste” and “CFADS\_Links”) are equal (i.e., the  “Check / Comparison” cell will be 0).

Start by going to the VBA Recorder (Alt, L, R in PC Excel) and setting this macro to the Ctrl + Shift + S shortcut. Then, go to the Macros tab, do the manual copy/paste, and stop the recording.

Go into the VBA Editor (Alt, L, V), delete the recorded code, and enter the following code to make the process repeat until the pasted and calculated CFADS equal each other:

_Do_

_Range(“CFADS\_Paste”).Value = Range(“CFADS\_Links”).Value_       

_Loop Until Range(“Check\_CFADS”).Value = 0_

It should look like this in the VBA Editor:

![VBA Copy/Paste Macro Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20274'%3E%3C/svg%3E "VBA Copy/Paste Macro Code")

Now, whenever we change an assumption, such as the minimum LLCR, the Interest Rate, or the Tax Rate, we can press Ctrl + Shift + S to change all the CFADS values and resize the initial Debt balance automatically.

**Debt Sculpting vs Debt Sizing: More Advanced Topics**
-------------------------------------------------------

This article is just an introduction to the topic.

There are dozens of more advanced points related to Debt Sizing and Debt Sculpting, such as:

*   **Cash flow sweeps**, i.e., optional Debt principal repayments based on cash flows.
*   **Variable issuance and maturity dates**, which require a system of “flags” to mark different periods.
*   **Monthly and quarterly models**, which shift the formulas.
*   **Multiple Debt tranches**, such as 1st lien and 2nd lien loans that are both sized and sculpted – or perhaps only one tranche is, and the other is not.
*   **Construction Loans** and how they are sized during the development period of a project and linked to the post-development financing.

We cover all these points and more in the introductory and more advanced case studies in our [Project Finance & Infrastructure Modeling course](https://breakingintowallstreet.com/project-finance-modeling/)
.

[Sign Up for Project Finance Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Debt Sculpting vs Debt Sizing – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-Debt-Sculpting-vs-Debt-Sizing-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple “Cash Flow Only” Debt Sculpting vs Debt Sizing with No VBA or Circular References (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-LLCR-Debt-Sizing.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Debt Sizing and Sculpting with VBA/Macro Support (XLSM)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-02/PF-02-VBA-Debt-Sizing.xlsm)
    

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

[X](https://x.com/intent/tweet?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&mini=true)
[Email](mailto:?subject=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)

#### Project Finance & Infrastructure Modeling

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[LEARN MORE](https://breakingintowallstreet.com/project-finance-modeling/)

[](https://x.com/intent/tweet?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[](https://www.linkedin.com/shareArticle?title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&mini=true)
[](mailto:?subject=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[](https://api.whatsapp.com/send?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Copy](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#)
[Email](mailto:?subject=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&t=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
[Pinterest](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#)
[Print](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[SMS](sms:?&body=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[X](https://x.com/intent/tweet?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fdebt-sculpting-vs-debt-sizing%2F&title=Debt%20Sculpting%20vs%20Debt%20Sizing%20in%20Project%20Finance%3A%20Full%20Tutorial&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand