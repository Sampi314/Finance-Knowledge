# Cash Flow Sweep in LBO Models: Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep

---

The Cash Flow Sweep in an LBO: Walkthrough and Simple Examples
==============================================================

In leveraged buyout and credit models, the “Cash Flow Sweep” refers to the company’s ability to repay Debt optionally based on its cash flows in the period, in addition to the scheduled or mandatory principal repayments that are set at the time of the initial issuance.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#tab-signup)
    

> **Cash Flow Sweep Definition:** In leveraged buyout and credit models, the “Cash Flow Sweep” refers to the company’s ability to repay Debt _optionally_ based on its cash flows in the period, in addition to the scheduled or mandatory principal repayments that are set at the time of the initial issuance.

The Cash Flow Sweep, also known as the “Cash Sweep” or “Optional Debt Repayment,” is a term most common for **Senior Debt** in a [leveraged buyout](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/)
, such as Term Loans issued by banks:

![Cash Flow Sweep Definition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201784%20563'%3E%3C/svg%3E "Cash Flow Sweep Definition")

Some forms of **Junior Debt** (e.g., Subordinated Notes, Mezzanine, etc.) may allow for optional repayment before maturity, but it is much rarer there, and if it exists at all, it’s usually based on an “all or nothing” repayment condition and may have penalty fees attached.

The Cash Flow Sweep is common for Senior Debt because it’s part of the **trade-off** lenders make: Lower credit default risk, lower returns, and higher reinvestment risk.

Senior lenders take less default risk because they’re above junior lenders and equity investors in the capital structure, so they are the first to be repaid in a bankruptcy or liquidation.

When a company repays Debt optionally, it **reduces the senior lenders’ credit risk**, but it does _not_ reduce their [annualized returns (the IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
 in simple scenarios.

It does create **reinvestment risk** because the lenders must reallocate the proceeds from these repaid loans into other loans.

Therefore, the Cash Flow Sweep is often limited to a certain percentage of the company’s available cash flow, such as 50%.

The Cash Flow Sweep tends to **boost the returns for the equity investors** (the private equity firm) because it reduces the company’s future interest expense, which boosts its cash flow.

However, the effect size is small in normal scenarios, and it’s not a major motivation for using this term.

### **Files & Resources:**

*   [Cash Flow Sweep Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-26-Cash-Flow-Sweep-Slides.pdf)
    
*   [Simple Cash Flow Sweep Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-26-CF-Sweep-Simple-LBO-Model.xlsx)
    

**The Simplest Cash Flow Sweep: Implicit 100% Assumption**
----------------------------------------------------------

In a [simple LBO model](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/simple-lbo-model-excel/)
, the **Cash Flow Available for Debt Repayment (CFADR)** equals the Beginning Cash + Free Cash Flow – Minimum Cash. If there are mandatory or scheduled repayments, you also subtract them here.

We assume the company uses _all_ this CFADR to repay Debt to the maximum extent possible.

For example, if its CFADR is $100, and $500 of Debt remains, it repays $100. But if only $50 of Debt remains, it repays the entire remaining $50.

This setup makes an **implicit assumption of a 100% Cash Flow Sweep:**

![Simple Cash Flow Sweep](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201907%20910'%3E%3C/svg%3E "Simple Cash Flow Sweep")

This setup works for simple models, but it gets more complicated in real life because the sweep is often limited to specific percentages, and there are usually multiple tranches of Debt.

**A Cash Flow Sweep for Less Than 100% of the Debt Principal**
--------------------------------------------------------------

To limit the Cash Flow Sweep to a specific percentage of the CFADR, we can add an extra conditional check to the “Cash Flow Used for Debt Repayment” formula:

![Cash Flow Sweep Percentages](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201912%20756'%3E%3C/svg%3E "Cash Flow Sweep Percentages")

If the CFADR is positive, we repay the **minimum** of the remaining Debt balance or the CFADR \* Cash Flow Sweep percentage, which is defined in the assumptions at the top:

![Cash Flow Sweep Assumptions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20320'%3E%3C/svg%3E "Cash Flow Sweep Assumptions")

You might think, intuitively, that the Cash Flow Sweep reduces the IRR for lenders because it means they are repaid early and earn less Interest over time.

However, because of the way the IRR function works, this is **not** true – their money-on-money multiple falls due to lower Interest, but the IRR remains the same.

The results for different Cash Flow Sweep percentages and a fixed Year 5 exit are shown below:

![Lenders' Returns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201924%201139'%3E%3C/svg%3E "Lenders' Returns")

While the Interest declines over time, the **outstanding loan principal** (or the lenders’ “basis”) also decreases. So, the lenders earn the same annualized returns due to this adjustment for the size of their remaining investment.

This behavior may not hold when there are more complex terms, such as floating interest rates, [original issue discount (OID)](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
, or prepayment penalties.

![PowerPoint Pro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Financial Modeling for Investment Banking With **BIWS Core Financial Modeling**

*   #### Become a financial modeling pro
    
    158 videos, detailed written guides, Excel files, quizzes, and more
    
*   #### Complete 10+ detailed global case studies
    
    These include both the theory and the practical applications
    
*   #### Prepare for your internship or full-time job
    
    Gain the skills you need to “hit the ground running” on Day 1
    

[Full Details](https://breakingintowallstreet.com/core-financial-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Core-Financial-Modeling-Course-Outline.pdf)

**The Cash Flow Sweep with Multiple Debt Tranches**
---------------------------------------------------

In real life, most leveraged buyouts are funded by multiple tranches of Debt, such as a Revolver for short-term borrowing needs, a Term Loan, and Subordinated Notes.

This scenario is boring because the Cash Flow Sweep normally only applies to the Revolver and Term Loan, but we can make it more interesting by using a **Revolver, Term Loan A, and Term Loan B** (Term Loan B typically has a higher interest rate and reduced repayments):

![Term Loan A and B Terms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201430%20314'%3E%3C/svg%3E "Term Loan A and B Terms")

The **Revolver** handles the company’s temporary borrowing needs in Year 1, and all the company’s available cash flows are used to repay the Revolver _first_ in the following years:

![Revolver Draws and Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201854%20854'%3E%3C/svg%3E "Revolver Draws and Repayments")

Once the Revolver is repaid, the company can make optional repayments on its Term Loan A and B.

**The Cash Flow Sweep for these Debt tranches must factor in the _previous repayments on other, more senior Debt tranches_!**

For example, the Term Loan A Cash Flow Sweep formula is based on the minimum between Remaining Term Loan A Balance and (CFADR + Revolver Draws – Revolver Repayments) \* Sweep %.

In other words, if there’s a Revolver Repayment in the period, that _reduces_ the cash flow that can be used for optional repayments:

![Term Loan A Cash Flow Sweep](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201856%20784'%3E%3C/svg%3E "Term Loan A Cash Flow Sweep")

And with Term Loan B, we must also deduct the Term Loan A Cash Flow Sweep since Term Loan A is senior to Term Loan B in the [LBO capital structure](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/leveraged-buyout-capital-structure/)
:

![Term Loan B Cash Flow Sweep](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201864%201048'%3E%3C/svg%3E "Term Loan B Cash Flow Sweep")

The Term Loan B Cash Flow Sweep is only 25%, which we interpret as: “Use 25% of the cash flow available _after_ the Revolver and Term Loan A repayments.”

Even in this more complex example, the Term Loan A IRR does **not** change as the Cash Flow Sweep percentages change (only the multiple shifts slightly).

**Even More Complex Cash Flow Sweeps**
--------------------------------------

Once you move beyond 2 – 3 tranches of Debt, it becomes cumbersome to track all the Cash Flow Sweeps in separate areas.

It’s **best** to group together the optional repayments for all the tranches, as shown below in the KKR / Viridor model from our [Private Equity Modeling course](https://breakingintowallstreet.com/private-equity-modeling/)
:

![Optional Debt Repayment Schedule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202088%20400'%3E%3C/svg%3E "Optional Debt Repayment Schedule")

This setup allows us to write a single formula and copy and paste it around the entire schedule to handle different Cash Flow Sweeps.

Terms such as prepayment penalties may complicate this and introduce [circular references](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
 into such a schedule, but you do not need to worry about these details in interviews or case studies.

**The Cash Flow Sweep in Project Finance**
------------------------------------------

Although it is less common, the Cash Flow Sweep may also exist in [Project Finance](https://breakingintowallstreet.com/kb/project-finance/)
.

[Debt is normally sized and sculpted](https://breakingintowallstreet.com/kb/project-finance/debt-sculpting-vs-debt-sizing/)
 to match the asset’s future cash flows in Project Finance, so the Cash Flow Sweep term allows for optional, “bonus” repayments if the cash flows exceed the targeted levels.

**[DSCR](https://breakingintowallstreet.com/kb/project-finance/debt-service-coverage-ratio/)
 and [LLCR](https://breakingintowallstreet.com/kb/project-finance/loan-life-coverage-ratio/)
\-based Debt sizing and sculpting do _not_ change due to the Cash Flow Sweeps because sizing and sculpting are based on the _scheduled_ principal repayments and interest**.

So, the asset simply repays the Debt before its true maturity date, unless you adjust for it via a Reserve account or other methods:

![Project Finance Cash Flow Sweep Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20780'%3E%3C/svg%3E "Project Finance Cash Flow Sweep Example")

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Cash Flow Sweep Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-26-Cash-Flow-Sweep-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Cash Flow Sweep Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-26-CF-Sweep-Simple-LBO-Model.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Private Equity Modeling (LBO Course)](https://breakingintowallstreet.com/private-equity-modeling/)

Master LBO modeling, paper LBOs, and case studies with 6 conceptual models and 6 full, step-by-step case studies. Includes interview questions, paper LBOs, and "quick business evaluation" exercises as well.

[Learn More](https://breakingintowallstreet.com/private-equity-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Private Equity Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/mM8atoiV)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A modeling from the ground up, along with a "deep dive" into leveraged buyouts, LBO models, and PE case studies. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/mM8atoiV)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&mini=true)
[Email](mailto:?subject=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&mini=true)
[](mailto:?subject=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[](https://api.whatsapp.com/send?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#)
[Email](mailto:?subject=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&t=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[SMS](sms:?&body=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[X](https://x.com/intent/tweet?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fcash-flow-sweep%2F&title=The%20Cash%20Flow%20Sweep%20in%20an%20LBO%3A%20Walkthrough%20and%20Simple%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand