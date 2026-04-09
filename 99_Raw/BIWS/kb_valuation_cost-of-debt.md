# Cost of Debt: Real-Life Examples and Excel Calculations

**Source:** https://breakingintowallstreet.com/kb/valuation/cost-of-debt

---

The Cost of Debt in Valuations, Credit, and Real Life
=====================================================

The Cost of Debt in corporate finance represents the effective rate a company would pay if it issued additional Debt today; most of this cost is the Interest Expense on the Debt, but some may also correspond to discounts, penalty fees, and face value vs. market value differences. The Cost of Debt is widely used in credit analysis and to calculate WACC in a DCF model.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#tab-signup)
    

The Cost of Debt in Valuations, Credit, and Real Life

> **Cost of Debt Definition:** The Cost of Debt in corporate finance represents the effective rate a company would pay if it issued _additional Debt_ today; most of this cost is the Interest Expense on the Debt, but some may also correspond to discounts, penalty fees, and face value vs. market value differences. The Cost of Debt is widely used in credit analysis and to calculate WACC in a DCF model.

To a company, the Cost of Debt represents the all-in future annual “expense percentage” of additional Debt.

To an investor, the Cost of Debt is the [effective annualized yield](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
 they could expect to earn over the long term by investing in a company’s Debt.

Consider a company with $1,000 of bonds and an annual interest expense of $50.

In this simple example, the Pre-Tax Cost of Debt is $50 / $1,000 = 5%.

Since the interest on Debt is tax-deductible, you multiply by (1 – Tax Rate) to use it in the [WACC formula](https://mergersandinquisitions.com/wacc-formula/)
, so at a 25% tax rate, the After-Tax Cost is 5% \* (1 – 25%) = 3.75%.

Of course, this is a naïve approach because we don’t know **the market value** of these bonds.

For example, if overall interest rates have **risen** since this issuance, the market value of these bonds is probably less than $1,000 now, and the company would have to pay more than 5% to issue new Debt.

As a simple example, let’s say the bonds’ market value is $900, and they have a 10-year maturity.

You could calculate the **yield to maturity** on these bonds with the following Excel formula to get a more accurate estimate for the Cost of Debt:

\=YIELD(Today’s Date, Maturity Date, Coupon Rate, 900 / 1000 \* 100, 100, 2)

Here are the results:

![Cost of Debt Based on the YTM](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20447'%3E%3C/svg%3E "Cost of Debt Based on the YTM")

The **yield to maturity** is 6.4%, which means that if the company issued Debt today, it would have to offer a higher coupon rate because interest rates have increased.

Assessing the Cost of Debt helps companies determine how additional borrowing will affect their profitability and cash flows and lets them make [Debt vs. Equity funding decisions](https://breakingintowallstreet.com/kb/debt-equity/debt-vs-equity-analysis/)
.

It’s also widely used in [Debt Schedules](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
 in 3-statement models and LBO models to estimate the interest rates on future issuances.

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

### **Files & Resources:**

*   [Cost of Debt – Excel Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-Cost-of-Debt.xlsx)
    
*   [Cost of Debt – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-Cost-of-Debt-Slides.pdf)
    
*   [Western Midstream Partners – 10-K Excerpts (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-WES-10-K-Excerpts.pdf)
    
*   [Steel Dynamics – 10-K Excerpts (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-STLD-10-K-Excerpts.pdf)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **5:37:** Part 1: Cost of Debt Interpretations
*   **7:45:** Part 2: Multiple Debt Issuances in Real Life
*   **9:53:** Part 3: No Fair Values of Debt Disclosed
*   **12:24:** Part 4: The Company Has No Debt
*   **13:19:** Recap and Summary

**Interpreting the Cost of Debt: Clarifications**
-------------------------------------------------

Before moving on, it’s worth making one more small point: If the Cost of Debt is 6.4%, as in the example above, that doesn’t necessarily mean the company will _pay_ $64 in cash interest expense on a new $1,000 bond issuance.

Instead, it means that investors should earn a [yield to maturity](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
 of 6.4%.

The company could let them achieve this by offering a _lower_ coupon rate but a higher [original issue discount (OID)](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
 or a _lower_ coupon rate and _higher call premiums_ or repayment penalty fees.

For example, instead of issuing a new $1,000 bond at a 6.4% coupon rate and 10-year maturity, the company could offer one of the following:

*   **Option #1:** Issue a 6% bond at a 3% original issue discount, i.e., let investors buy it for $970 rather than $1,000. This gives them approximately 0.4% extra yield per year, boosting the YTM to ~6.4%.
*   **Option #2:** Issue a 5% bond with a 5% repayment penalty fee and a ~7.7% original issue discount. With this method, the company limits itself to ongoing cash payments of 5% \* $1,000 = $50 per year. But the investors buy the bond for only $923, still receive $50 in interest per year, and get an additional $50 when the bond is repaid.

You can see these examples below:

![Cost of Debt Meaning and Interpretation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20518'%3E%3C/svg%3E "Cost of Debt Meaning and Interpretation")

In most valuations and credit models, you normally assume the Cost of Debt represents the cash cost of issuing a new bond.

These alternatives are more important for stressed or distressed companies that want to restructure while reducing their cash costs.

**Calculating the Cost of Debt in Real Life: Complexities and Missing Information**
-----------------------------------------------------------------------------------

The calculations above are simple since they are not based on “messy” real companies.

But when you analyze real companies and estimate their Costs of Debt, you will run into a few common problems:

1.  **Multiple Debt Issuances** – Most real companies have more than one Debt issuance, so you’ll have to calculate the YTM on each one and take a weighted average.
2.  **No Fair Values Disclosed** – Many companies, especially smaller ones, do not disclose the fair value or fair market value of their Debt, so it’s not possible to use the YIELD function in a meaningful way.
3.  **No Debt** – Finally, some companies may not have any Debt. In this case, you’ll have to rely on the [comparable public companies](https://breakingintowallstreet.com/kb/valuation/comparable-company-analysis-cca/)
     and make adjustments to estimate the company’s Cost of Debt.

To illustrate these scenarios, we’ll use **Western Midstream Partners** (an oil & gas company in the midstream sector) and **Steel Dynamics** in a few examples.

**Calculating the Cost of Debt in Real Life: Multiple Issuances**
-----------------------------------------------------------------

If the company discloses the fair value of each issuance, this issue is simple: Calculate the YTM of each one and use the weighted average to approximate the Cost of Debt.

Here are Western Midstream Partners’ disclosures:

![Fair Value of Debt for Western Midstream Partners](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20412'%3E%3C/svg%3E "Fair Value of Debt for Western Midstream Partners")

And here are our calculations based on the weighted average YTM:

![Cost of Debt Based on YTM for Western Midstream Partners](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20403'%3E%3C/svg%3E "Cost of Debt Based on YTM for Western Midstream Partners")

Since WES is a Master Limited Partnership (MLP), its corporate tax rate is 0% or close to 0%, which means that multiplying by (1 – Tax Rate) barely changes the Cost of Debt:

![Impact of Taxes on the Cost of Debt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20196'%3E%3C/svg%3E "Impact of Taxes on the Cost of Debt")

As an example for a company with corporate-level taxes, here are the numbers for Steel Dynamics:

![Steel Dynamics - Cost of Debt Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20162'%3E%3C/svg%3E "Steel Dynamics - Cost of Debt Calculation")

**Calculating the Cost of Debt in Real Life: No Fair Values Disclosed**
-----------------------------------------------------------------------

If the company you’re valuing does not disclose the “fair value” or “fair market value” of its Debt, you have several options.

**First**, you could look at the comparable public companies, see if any of them disclose the fair value of their Debt, and base the Cost of Debt on their numbers (e.g., the median YTM for the set).

This method works, but is time-consuming and may not produce useful results if only a few companies disclose the fair values.

**Second**, you could take the average interest rate on the company’s Debt and use that for its Cost of Debt.

For example, with Western Midstream, we could have done the following to estimate its Cost of Debt:

![Simple Interest Rate Method for the Cost of Debt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20180'%3E%3C/svg%3E "Simple Interest Rate Method for the Cost of Debt")

This produces a 4.8% Pre-Tax Cost of Debt, which is fairly close, but it’s still a big enough difference to affect the valuation.

**Finally,** you could take the [Risk-Free Rate](https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
 and add the company’s estimated Credit Default Spread based on its credit rating.

[Damodaran has an annually updated list right here](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html)
, which we used for an alternative calculation:

![Default Spread Method for the Cost of Debt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20153'%3E%3C/svg%3E "Default Spread Method for the Cost of Debt")

Although WES has a high interest coverage ratio (> 3.0x and > 4.0x in some periods), both S&P and Fitch have given it a “BBB-“ credit rating.

Therefore, we took the 1.2% spread from Damodaran’s current chart and added it to the U.S. Risk-Free Rate of 4.2% at the time of this valuation to get a Pre-Tax Cost of Debt of 5.4%.

This is lower than the 5.7% YTM but is more accurate than the “simple interest expense” method.

**Calculating the Cost of Debt in Real Life: No Debt**
------------------------------------------------------

One final complexity is that you may have to calculate the Cost of Debt for a company that does not have any Debt currently.

The simple interest rate, yield to maturity, and risk-free rate + credit default spread methods do **not** work in this case.

All you can do here is calculate the Cost of Debt for its comparable public companies and perhaps add a “size/risk premium” if it is much smaller.

For example, you might do this if you’re valuing a tech startup and comparing it to public companies with $100+ million in revenue.

A new tech startup with low revenue is _much_ riskier than companies with hundreds of millions in revenue, so its Cost of Debt should be higher.

Opinions vary on how much of a size/risk premium to add, but something in the 20 – 40% range might be appropriate.

So, if the public companies’ median YTM is 8%, perhaps your company’s Cost of Debt is 10% or 11%, representing premiums in that 20 – 40% range.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Cost of Debt – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-Cost-of-Debt-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Western Midstream Partners – 10-K Excerpts (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-WES-10-K-Excerpts.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Steel Dynamics – 10-K Excerpts (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-STLD-10-K-Excerpts.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Cost of Debt – Excel Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-32-Cost-of-Debt.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&mini=true)
[Email](mailto:?subject=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)

[](https://x.com/intent/tweet?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&mini=true)
[](mailto:?subject=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[](https://api.whatsapp.com/send?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Copy](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#)
[Email](mailto:?subject=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&t=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/valuation/cost-of-debt/)
[Pinterest](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#)
[Print](https://breakingintowallstreet.com/kb/valuation/cost-of-debt/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[SMS](sms:?&body=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[X](https://x.com/intent/tweet?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fvaluation%2Fcost-of-debt%2F&title=The%20Cost%20of%20Debt%20in%20Valuations%2C%20Credit%2C%20and%20Real%20Life&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand