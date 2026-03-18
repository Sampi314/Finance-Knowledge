# Bank Regulatory Capital: Requirements, Calculations, Excitement?

**Source:** https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital

---

Bank Regulatory Capital and the Tragic Tale of Silicon Valley Bank and Credit Suisse
====================================================================================

In this tutorial, you’ll learn about bank regulatory capital, such as Common Equity Tier 1 and Tier 1 Capital, and why it did not stop firms such as Silicon Valley Bank and Signature Bank from failing.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/#tab-signup)
    

Bank Regulatory Capital and the Tragic Tale of Silicon Valley Bank and Credit Suisse

Bank Regulatory Capital Definition
----------------------------------

Bank regulatory capital consists primarily of common shareholders’ equity and ensures that banks can survive unexpected loan losses; banks must also maintain enough liquid assets to withstand high deposit withdrawals and enough “stable funding” to last if they lose access to certain funding sources.

The most common forms of bank regulatory capital are **Common Equity Tier 1 (CET 1)** and **Tier 1 Capital**, both of which are based on the bank’s **common shareholders’ equity (CSE):**

**CET 1** = CSE – Goodwill & Other Intangibles +/- Other Adjustments

**Tier 1 Capital** = CET 1 + Preferred Stock

(For more about the accounting, see our tutorial on [the Statement of Owner’s Equity](https://breakingintowallstreet.com/kb/accounting/statements-of-owners-equity/)
).

These metrics are typically divided by the bank’s **Risk-Weighted Assets (RWA)**, and banks must maintain certain “ratios,” such as a CET 1 / RWA of 7% or greater, or a Tier 1 Capital / RWA of 8.5% or greater:

[![Bank Regulatory Capital - Key Ratios](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20446'%3E%3C/svg%3E "Bank Regulatory Capital - Key Ratios")](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2023/03/19074757/Bank-Regulatory-Capital-01.jpg)

Other requirements include the **Liquidity Coverage Ratio (LCR)**, which measures a bank’s high-quality liquid assets vs. its possible cash outflows over a stressed 30-day period, and the **Net Stable Funding Ratio (NSFR)**, which measures a bank’s “stable” funding sources (stickier deposits, long-term debt, equity, etc.) vs. its “required” funding (percentages of various assets).

Banks must maintain an **LCR above 100%** and an **NSFR above 100%**, which, theoretically, should reduce their risk of failure.

Obviously, though, banks still fail or get forced into acquisitions – with Silicon Valley Bank and Credit Suisse as a few recent examples.

![Bank Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Bank and Financial Institution Valuation and Financial Modeling

*   #### Master financial institution modeling and valuation
    
    Build operating models, perform valuations, and analyze M&A deals with 4 global case studies
    
*   #### Dominate interviews and excel on the job
    
    Create professional deliverables like stock pitches, equity research reports, and IB pitch books
    
*   #### Explore private equity and growth equity scenarios
    
    Study buyouts and minority-stake deals in the financial services sector
    

[Full Details](https://breakingintowallstreet.com/bank-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Bank-Modeling-Course-Outline.pdf)

This article will explain the **rationale** behind these regulatory capital metrics, demonstrate a few simple calculations, and explain why they didn’t save these troubled banks.

You can get the Files & Resources, including an Excel file with the full calculations, below:

*   [Regulatory Capital Calculations and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/Bank-Regulatory-Capital.xlsx)
    
*   [Bank Regulatory Capital Slide Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/Bank-Regulatory-Capital-Slides.pdf)
    
*   [Key Extracts from Credit Suisse’s Annual Report](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/CS-Annual-Report-Extracts.pdf)
    
*   [Key Extracts from Silicon Valley Bank’s Annual Report](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/SVB-10-K-Extracts.pdf)
    
*   [Credit Suisse – Full Annual Report](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/CS-Annual-Report.pdf)
    
*   [Silicon Valley Bank – Full Annual Report](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/SVB-10-K.pdf)
    

**What is Bank Regulatory Capital?**
------------------------------------

Unlike most normal companies, commercial banks _expect_ that a certain percentage of their Assets will “go bad,” i.e., lose value or become worthless.

When a bank issues loans, it knows that a certain percentage of borrowers will default, fall behind on their payments, and so on.

To account for these scenarios, all banks create a **contra-Asset** on the Balance Sheet called the “[Allowance for Loan Losses](https://breakingintowallstreet.com/kb/bank-modeling/allowance-for-loan-losses-for-banks-fig/)
,” which represents the _expected future losses_ on the entire Loan balance.

It’s netted against a bank’s Gross Loans to calculate its Net Loans.

As the bank’s loss expectations change, it can adjust this Allowance up or down based on the **Provision for Credit Losses** on the Income Statement. You can see an example below:

![Allowance for Loan Losses and Provision for Credit Losses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201813%201001'%3E%3C/svg%3E "Allowance for Loan Losses and Provision for Credit Losses")

Banks create the Allowance when they first issue loans, and it’s designed to handle **expected losses** at the time of the loan issuance.

But there are also **unexpected losses**, which is a problem – because if the bank’s Loans _decrease_ on the Assets side, something on the Liabilities & Equity side must also decrease to match this change.

The L&E side of the Balance Sheet for most banks consists of **Deposits, Debt, and Equity**, and the _worst-case possible outcome_ is for the depositors – the bank’s customers – to take a loss.

The Equity investors should take losses first, followed by the Debt investors (lenders), and the Depositors should lose money only in the absolute worst-case scenario.

**So, the regulatory capital requirements ensure that there’s enough of a “buffer” in the bank’s Equity (and Debt) to absorb these unexpected losses.**

Mechanically, this works via the Provision for Credit Losses on the Income Statement (IS).

When a bank increases its loss expectations or records _unexpected losses_, it increases the Provision, which reduces its Net Income at the bottom of the IS.

This reduced Net Income then flows into Common Shareholders’ Equity on the Balance Sheet, reducing both CSE and metrics that are based on CSE, such as the CET 1 and Tier 1 ratios:

![The Provision for Credit Losses and Bank Regulatory Capital](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201747%20936'%3E%3C/svg%3E "The Provision for Credit Losses and Bank Regulatory Capital")

The exact requirements for these ratios differ based on the region and bank type, but the _absolute minimums_ worldwide are:

**CET 1 / RWA >= 4.5%**

**Tier 1 Capital / RWA >= 6.0%**

**Total Capital / RWA >= 8.0%**

And most banks add a 2.5% “capital conservation buffer” to all these ratios, so the **true minimums** are:

**CET 1 / RWA >= 7.0%**

**Tier 1 Capital / RWA >= 8.5%**

**Total Capital / RWA >= 10.5%**

Some “systemically important banks” also have additional surcharges, and regulators may also require a “countercyclical capital buffer,” “stress capital buffer,” and others.

[This page from SIFMA has a great summary of the rules for small and large banks in the U.S.](https://www.sifma.org/resources/news/understanding-the-current-regulatory-capital-requirements-applicable-to-us-banks/)

**The bottom line is that these required ratios can increase to much higher levels, and the specific numbers vary based on the bank type, size, region, and macro environment.**

Banks must also maintain a Liquidity Coverage Ratio (LCR) above 100% and a Net Stable Funding Ratio (NSFR) above 100%, but these are not always enforced for smaller banks.

For example, in the lead-up to Silicon Valley Bank’s failure, regulators in the U.S. didn’t require LCR or NSFR compliance for banks with under $250 billion in Total Assets.

**Why Didn’t Bank Regulatory Capital Save Silicon Valley Bank?**
----------------------------------------------------------------

[Silicon Valley Bank failed because of a complete lack of risk management and some very bad management decisions](https://mergersandinquisitions.com/silicon-valley-bank/)
.

The bank got a huge influx of deposits in 2020 – 2021 because of the very favorable funding environment for tech startups, but it had no idea what to do with the money and couldn’t issue enough loans.

Rather than letting it sit in cash on its Balance Sheet, SVB decided to purchase long-term government bonds and mortgage-backed securities.

The problem is that it did this when **interest rates were very low** – and if interest rates ever rose, these bonds’ prices would fall significantly.

And… that’s exactly what happened.

As the Fed and other central banks raised interest rates, SVB’s “Held to Maturity” securities lost value, but since the bank planned to hold them to maturity, they did not have to record these losses directly on the Balance Sheet.

Based on a quick Excel calculation, the HTM Securities were worth ~17% less with yields on similar bonds at 4% than they were when originally purchased, when yields on similar bonds were at 1.5:

![Silicon Valley Bank - HTM Securities](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202084%20627'%3E%3C/svg%3E "Silicon Valley Bank - HTM Securities")

Here are SVB’s regulatory capital ratios before and after this adjustment for the loss in value of the HTM Securities:

![Silicon Valley Bank - Regulatory Capital After Adjustments for Unrealized Losses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201801%20860'%3E%3C/svg%3E "Silicon Valley Bank - Regulatory Capital After Adjustments for Unrealized Losses")

That said, the bank didn’t _necessarily_ have to fail.

It could have simply held these securities to maturity and never taken the losses.

It was pushed over the edge because it _announced_ in early March that it had sold a portfolio of securities at a $1.8 billion loss and would raise additional equity.

Venture capitalists and startup people on social media noticed this and started telling everyone to withdraw their money, assuming that the bank would collapse.

That led to a **run on the bank**, as it quickly lost its deposits and didn’t have enough cash to cover the full outflow quickly enough.

It could have potentially sold some of its assets and used the proceeds to cover depositors, but that process takes time, and the bank experienced _massive_ withdrawals in a short period.

The government ended up stepping in and taking over, and most of SVB’s assets will be acquired by First Citizens.

The sad thing about this story is that if the bank had simply hedged its interest-rate risk using swaps or even purchased shorter-term bonds, it could have avoided the entire disaster:

![Silicon Valley Bank with Shorter-Term Bonds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201214%20340'%3E%3C/svg%3E "Silicon Valley Bank with Shorter-Term Bonds")

**Why Didn’t Bank Regulatory Capital Save Credit Suisse?**
----------------------------------------------------------

For over a decade, Credit Suisse had been a troubled bank, with poor/nonexistent risk management and a [long list of scandals](https://en.wikipedia.org/wiki/Credit_Suisse#Controversies)
.

In 2022, it recorded a loss of CHF 7.3 billion, and most people assumed the bank would sell assets, spin off divisions, or otherwise restructure itself.

Unlike SVB, CS did not have a huge amount of unrealized losses on HTM Securities, and it wasn’t catering exclusively to tech startups flush with cash.

And all its regulatory capital ratios looked fine:

[![Credit Suisse - Bank Regulatory Capital Ratios](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20533'%3E%3C/svg%3E "Credit Suisse - Bank Regulatory Capital Ratios")](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2023/03/19074752/Bank-Regulatory-Capital-07.jpg)

Even its Liquidity Coverage Ratio and Net Stable Funding Ratio – neither of which SVB reported – were both well above 100%.

**But regulatory capital ratios don’t tell the full story with banks.**

If everyone suddenly “loses confidence” in a bank and starts to withdraw their money, no capital ratio or regulation can save it.

As confidence in CS deteriorated, it lost 40-50+ of its Cash and Deposits from 2021 to 2022:

[![Credit Suisse - Cash and Deposit Losses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20650'%3E%3C/svg%3E "Credit Suisse - Cash and Deposit Losses")](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2023/03/19074751/Bank-Regulatory-Capital-08.jpg)

At the rate that customers were withdrawing money, CS would have lasted for another _1-2 weeks_ – [which is why the Swiss government forced UBS to step in and save it, with a government-sponsored backstop](https://mergersandinquisitions.com/ubs-and-credit-suisse/)
.

In this case, “The Eye of Sauron” turned its attention to CS in its search for the next-weakest bank after the failures of SVB and Signature.

Modern fractional reserve banking is **a confidence game**, and when everyone panics about the same bank at once, it can fail quite easily.

Smartphones, mobile devices, and the ability to withdraw money quickly from anywhere in the world have made this problem even worse; a rumor spread on social media can propel a bank into collapse if enough people believe it.

**Is Bank Regulatory Capital Useful? Should It Change in the Future?**
----------------------------------------------------------------------

My main message in this article is that bank regulatory capital is _useful but not sufficient_ to evaluate the health or riskiness of a bank.

It’s like going to the doctor and reporting good numbers for your blood pressure, cholesterol, and body fat percentage: your risk is lower, but you still have _some risk_ even if you’re in very good physical condition.

Rather than relying strictly on metrics such as the CET 1 and Tier 1 Ratios or the Liquidity Coverage Ratio, you should also think about **the bigger picture** when evaluating banks.

Is the bank’s business growing or shrinking? What types of customers is it attracting? How risky are its deposits? What does the bank do when it gets _too many_ deposits? Has the bank been involved in high-profile scandals or other problems?

Because of these bank failures, there are now many proposals to insure _all_ deposits (above the $250K maximum in the U.S. and the CHF 100K maximum in Switzerland), impose stricter regulations and requirements on banks, create “free” national banks, and so on.

Some of these are potentially good ideas, but, again, **no single rule or regulation can “stop” a bank from failing**.

If a bank fails, the goal should be to provide an **orderly** wind-down / liquidation process that protects the depositors as much as possible.

The real problem is that the entire commercial banking system is **too fragile** with too much concentration among the “Big 4” banks in the U.S. (JPM, Citi, Wells Fargo, and BofA); many other countries also have highly concentrated banking industires.

This creates an environment where there are “Too Big to Fail” banks, meaning that if one of them runs into trouble, governments need to step in with a bailout – which is **not** how a healthy economy should function.

I believe we should be thinking about **breaking up** the large banks and splitting them into smaller entities to encourage more competition and reduce the systemic risk.

Unfortunately, regulators and the overall economy are moving in the opposite direction, [as there are now fewer and fewer banks in the U.S. each year](https://www.stlouisfed.org/on-the-economy/2021/december/steady-decline-number-us-banks)
:

![Bank Consolidation in the U.S.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20839%20626'%3E%3C/svg%3E "Bank Consolidation in the U.S.")

We’ll see if these trends reverse, but I am not hopeful unless something dramatic _forces_ regulators and governments into different positions.

[Sign Up To BIWS Bank Modeling](https://breakingintowallstreet.com/bank-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Bank Regulatory Capital Slide Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/Bank-Regulatory-Capital-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Key Extracts from Credit Suisse's Annual Report (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/CS-Annual-Report-Extracts.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Key Extracts from Silicon Valley Bank's Annual Report (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/SVB-10-K-Extracts.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Credit Suisse - Full Annual Report (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/CS-Annual-Report.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Silicon Valley Bank - Full Annual Report (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/SVB-10-K.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Regulatory Capital Calculations and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Banks/Bank-Regulatory-Capital.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Bank Modeling](https://breakingintowallstreet.com/bank-modeling/)

Master bank accounting, valuation, M&A, and buyouts with 4 global case studies based on Shawbrook, KeyCorp / First Niagara, ANZ, and the Philippine Bank of Communications.

[Learn More](https://breakingintowallstreet.com/bank-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Bank Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/CfRbkrvF)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with commercial banks and insurance firms and how everything differs for them. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/CfRbkrvF)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&mini=true)
[Email](mailto:?subject=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)

#### Master Bank & Insurance Modeling

BIWS Bank & Financial Institution Modeling Course prepares you for FIG interviews and the job itself with tutorials on bank accounting, valuation, M&A, and buyout modeling.

[LEARN MORE](https://breakingintowallstreet.com/bank-modeling/)

[](https://x.com/intent/tweet?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[](https://www.linkedin.com/shareArticle?title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&mini=true)
[](mailto:?subject=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[](https://api.whatsapp.com/send?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Copy](https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/#)
[Email](mailto:?subject=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&t=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/01/19075641/The-Allowance-for-Loan-Losses-for-Banks-FIG.jpg&description=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[Print](https://breakingintowallstreet.com/kb/bank-modeling/bank-regulatory-capital/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[SMS](sms:?&body=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[X](https://x.com/intent/tweet?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fbank-regulatory-capital%2F&title=Bank%20Regulatory%20Capital%20and%20the%20Tragic%20Tale%20of%20Silicon%20Valley%20Bank%20and%20Credit%20Suisse&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/01/19075641/The-Allowance-for-Loan-Losses-for-Banks-FIG.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand