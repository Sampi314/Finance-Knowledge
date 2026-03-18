# EBITDA to FCF: Full Tutorial, Examples, and Excel Files

**Source:** https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf

---

EBITDA to FCF: Interview Question and Modeling Test Walkthrough
===============================================================

FCF = EBITDA – Net Interest Expense – Taxes +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx; also, always clarify which type of Free Cash Flow you’re calculating since the formula changes for other FCF variations.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#tab-signup)
    

> **EBITDA to FCF Definition:** FCF = EBITDA – Net Interest Expense – Taxes +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx; also, always clarify _which type_ of Free Cash Flow you’re calculating since the formula changes for other FCF variations.

![EBITDA to FCF - Basic Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%20562'%3E%3C/svg%3E "EBITDA to FCF - Basic Calculation")

This definition assumes the “standard” [Free Cash Flow](https://breakingintowallstreet.com/kb/financial-statement-analysis/how-to-calculate-free-cash-flow/)
 that is used in [LBO models](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/)
 and [financial statement analysis](https://breakingintowallstreet.com/kb/financial-statement-analysis/)
, but there are other variations (see below).

In [investment banking interviews](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/)
, it’s common to get questions about _different ways_ to calculate metrics such as Free Cash Flow.

Unfortunately, many of the online tutorials for this topic skip the subtleties in the calculation and gloss over issues like lease accounting.

Outside of pure interview questions, this “EBITDA to FCF” question matters because, in many case studies and modeling tests, you will get a template or existing model and be asked to calculate other metrics based on EBITDA.

**You must understand the _type_ of Free Cash Flow you are calculating and the items it should deduct – if you know that, you’ll be able to calculate it starting with any metric.**

We cover a few examples, variations, subtleties, and lease accounting issues below:

### **Files & Resources:**

*   [EBITDA to FCF – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Financial-Statement-Analysis/EBITDA-to-FCF/101-09-EBITDA-to-FCF-Slides.pdf)
    
*   [EBITDA to FCF – Excel Demonstration (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Financial-Statement-Analysis/EBITDA-to-FCF/101-09-EBITDA-to-FCF-BMC.xlsx)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **4:21:** Part 1: Alternate Ways to Calculate FCF
*   **7:32:** Part 2: EBITDA to FCFE and FCFF
*   **9:37:** Part 3: Subtleties in the Calculations
*   **12:06:** Part 4: Lease Accounting (Your Favorite Topic)
*   **14:14:** Recap and Summary

**EBITDA to FCF Definitions: What is Free Cash Flow?**
------------------------------------------------------

**Free Cash Flow** is normally defined as Cash Flow from Operations – Capital Expenditures, _assuming_ that Cash Flow from Operations deducts the Net Interest Expense, Taxes, and the full Lease Expense.

(If it does not fully deduct all of these, you must adjust it.)

FCF tells you how much Debt principal the company could repay or how much it could spend on activities such as acquisitions, dividends, or stock repurchases.

In LBO models and credit models, it partially determines the “optional repayments” the company can make on its Debt balance (i.e., the [cash flow sweep](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-sweep/)
).

You could also calculate Free Cash Flow by starting with Net Income:

**FCF** = Net Income (to Common) + D&A +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx.

Here’s an example calculation for BMC Stock Holdings, a building materials company:

![Net Income to FCF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202064%20444'%3E%3C/svg%3E "Net Income to FCF")

It’s the same basic idea as Cash Flow from Operations minus CapEx because the first 3 terms in this formula _represent_ Cash Flow from Operations:

![Net Income to Free Cash Flow Equivalency](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202056%20600'%3E%3C/svg%3E "Net Income to Free Cash Flow Equivalency")

To move _from_ EBITDA to FCF, factor in all the items that affect FCF but _not_ EBITDA:

**FCF** = EBITDA – Net Interest Expense – Taxes +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx.

The tricky part is that you can’t just multiply EBITDA by the Tax Rate to calculate the Taxes.

Instead, you should deduct the D&A and Interest Expense from EBITDA to calculate Pre-Tax Income and then multiply that by the Tax Rate because these items are **tax-deductible**.

In other words, “Taxes” in this calculation equal (EBITDA – D&A – Net Interest) \* Tax Rate:

![Taxes in the FCF Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202058%20811'%3E%3C/svg%3E "Taxes in the FCF Calculation")

The “Other Non-Cash Adjustments” term might also have additional adjustments for Deferred Taxes, as FCF should always reflect a company’s Cash Taxes.

**From EBITDA to FCF… of Different Types**
------------------------------------------

There are also different _types_ of Free Cash Flow: [Unlevered Free Cash Flow](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/)
, also known as Free Cash Flow to Firm, and [Levered Free Cash Flow](https://breakingintowallstreet.com/kb/valuation/levered-free-cash-flow/)
, also known as Free Cash Flow to Equity.

In most cases, it’s pointless to walk through these bridges because these metrics are typically used for valuation purposes, such as in a [DCF model](https://mergersandinquisitions.com/dcf-model/)
, and you rarely build an entire DCF starting from EBITDA.

For completeness, however, we’ll walk through both bridges below.

**EBITDA to FCFE** is easier because FCFE is close to normal FCF: Take FCF, add Debt Issuances, and subtract Debt Repayments.

**FCFE** = EBITDA – Net Interest Expense – Taxes +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx + Debt Issuances – Debt Repayments

**EBITDA to FCFF** is shorter but requires more explanation:

**FCFF** = EBITDA – Taxes Excluding Impact of Interest +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx

“Taxes Excluding Impact of Interest” means what it sounds like: Deduct D&A, but not Net Interest Expense, to calculate Taxes.

FCFF or Unlevered Free Cash Flow is capital structure-neutral, so the company should pay the same amount of Taxes regardless of its Debt:

**FCFF** = EBITDA – EBIT \* Tax Rate +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx

Here are the calculations for BMC Stock Holdings, a building materials company used as an example in our courses:

![EBITDA to FCFF Variation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202074%20412'%3E%3C/svg%3E "EBITDA to FCFF Variation")

**Subtleties in the EBITDA to FCF Calculation**
-----------------------------------------------

The examples above represent the basic calculations and simple responses that work in interviews, but **real life** is more complicated.

Note that “real life” includes [3-statement modeling](https://mergersandinquisitions.com/3-statement-model/)
 and [LBO modeling tests](https://mergersandinquisitions.com/lbo-modeling-test/)
!

We’ll approach this section by explaining how the main deductions and adjustments in the calculation can be more complex in real life:

**FCF** = EBITDA – Net Interest Expense – Taxes +/- Other Non-Cash Adjustments +/- Change in Working Capital – CapEx

**First**, if the company has Preferred Stock, you must also deduct the Preferred Dividends along with the Net Interest since they’re also a financing cost:

![Preferred Dividends in Free Cash Flow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201704%201218'%3E%3C/svg%3E "Preferred Dividends in Free Cash Flow")

Similarly, anything like “Other Income” or “Other Expenses” above the Pre-Tax Income line should be factored in because FCF should capture _everything that affects the after-tax profits._

We use this approach in the BMC model, even though “Other Income” is small.

**Second**, Taxes can be tricky because you should technically subtract the company’s _Cash Taxes_.

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

So, if the company is using accelerated Depreciation or has items such as Stock-Based Compensation that are _not_ tax-deductible in the current period, you should adjust the Tax number or include the effects in the “Other Non-Cash Adjustments” section, as we do in the BMC model.

**Third**, the “Change in Working Capital” sometimes includes more than just the explicit line items in that section.

For example, consider this Netflix financial model:

![Netflix Content Assets and Liabilities in Free Cash Flow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201834%201054'%3E%3C/svg%3E "Netflix Content Assets and Liabilities in Free Cash Flow")

For a firm like Netflix, these “Content Assets” and “Content Liabilities” _are_ “Changes in Working Capital” because they represent content spending.

Netflix must purchase and develop streaming content if it wants to grow, so changes in these items are a core part of its business.

Therefore, if you calculate FCF starting with EBITDA, you should _definitely_ include these.

**Finally**, with the CapEx deduction, in some cases, you should also deduct items such as Intangible Purchases and Acquisitions… if they are truly recurring and core to the business.

For example, if you’re modeling a pharmaceutical company that constantly needs to acquire new drugs to remain competitive, you could easily justify a deduction for recurring Intangible Purchases.

But it would be more difficult to justify for a restaurant or retail company.

**Lease Accounting in the EBITDA to FCF Calculation**
-----------------------------------------------------

One final wrinkle is the issue of [lease accounting](https://mergersandinquisitions.com/lease-accounting/)
 and how the rules changed when IFRS 16 and ASC 842 were implemented in 2019.

**To simplify things, we recommend always deducting the full Lease Expense from both Operating and Finance Leases in FCF, no matter how it appears on the financial statements.**

That translates into the following:

*   Under **U.S. GAAP**, the Operating Lease Expense is already deducted on the Income Statement and reduces EBITDA, so you don’t need to do anything else. However, if the company has Finance Leases, you should deduct the Finance Lease Interest and Principal Repayments, which you may need to search for in the filings. If these items are small, this point makes a tiny difference and can be ignored.
*   Under **IFRS**, you should deduct the Total Lease Interest and Total Lease Principal Repayments when moving from EBITDA to FCF. The Lease Interest is usually within the Net Interest Expense on the Income Statement, but if it’s not, you will need to create a separate line for it. To get the Lease Principal Repayments, you must look under Cash Flow from Financing on the Cash Flow Statement.

In addition, there may also be a small “net cash effect” from the Lease Assets and Liabilities changing by slightly different amounts each year; you can include this as another adjustment with the Lease Principal Repayment deduction.

Here’s an example of the EBITDA to FCF calculation for Watches of Switzerland in our [Private Equity Modeling course](https://breakingintowallstreet.com/private-equity-modeling/)
:

![EBITDA to FCF Calculation with IFRS 16 Lease Accounting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201774%201610'%3E%3C/svg%3E "EBITDA to FCF Calculation with IFRS 16 Lease Accounting")

Under IFRS, EBITDA _excludes_ the entire Lease Expense, so we need to deduct the Lease Interest (included within “Net Interest Expense” here) and the Lease Principal Repayments (in the “IFRS 16 Lease Adjustments” line) to get a proper number.

You can also get the same effect by adjusting Depreciation to remove the Lease Depreciation portion, but it’s faster and easier to deduct the Lease Principal Repayment line since it’s always shown explicitly on the Cash Flow Statement.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) EBITDA to FCF - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Financial-Statement-Analysis/EBITDA-to-FCF/101-09-EBITDA-to-FCF-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) EBITDA to FCF - Excel Demonstration (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Financial-Statement-Analysis/EBITDA-to-FCF/101-09-EBITDA-to-FCF-BMC.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[BIWS Premium](https://breakingintowallstreet.com/biws-premium/)

Get the Excel & VBA, Core Financial Modeling, and PowerPoint Pro courses together and learn everything from Excel shortcuts up through financial modeling, valuation, M&A and LBO deals, and the key PowerPoint shortcuts and commands.

[Learn More](https://breakingintowallstreet.com/biws-premium/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)
: Learn accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up with 10+ real-life case studies from around the world. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/core-financial-modeling/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&mini=true)
[Email](mailto:?subject=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[](https://www.linkedin.com/shareArticle?title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&mini=true)
[](mailto:?subject=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[](https://api.whatsapp.com/send?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Copy](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#)
[Email](mailto:?subject=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&t=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[LinkedIn](https://www.linkedin.com/shareArticle?title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/)
[Pinterest](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#)
[Print](https://breakingintowallstreet.com/kb/financial-statement-analysis/ebitda-to-fcf/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[SMS](sms:?&body=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[X](https://x.com/intent/tweet?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[WhatsApp](https://api.whatsapp.com/send?text=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinancial-statement-analysis%2Febitda-to-fcf%2F&title=EBITDA%20to%20FCF%3A%20Interview%20Question%20and%20Modeling%20Test%20Walkthrough&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand