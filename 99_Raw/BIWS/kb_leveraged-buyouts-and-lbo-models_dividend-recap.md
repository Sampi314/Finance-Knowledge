# Dividend Recap: LBO Tutorial With Excel Examples

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap

---

The Dividend Recap in an LBO Model: Full Tutorial
=================================================

In this lesson, you’ll learn how the Dividend Recap works in a leveraged buyout and how you can implement a Dividend Recap in an LBO model.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/#tab-signup)
    

The Dividend Recap in an LBO Model: Full Tutorial

> **Dividend Recap Definition:** In a Dividend Recapitalization (“Dividend Recap”), a [private equity firm](https://www.mergersandinquisitions.com/private-equity/)
>  has a portfolio company issue additional Debt to fund a Dividend issuance that boosts the PE firm’s [internal rate of return (IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
>  on the deal.

A Dividend Recap is similar to a [commercial real estate loan refinancing](https://breakingintowallstreet.com/kb/real-estate-modeling/commercial-real-estate-loan-refinancing/)
 in the property sector: it’s a way to use additional Debt to _amplify_ the returns in a deal.

If a company performs well, a Dividend Recap can boost the PE firm’s IRR anywhere from “modestly” to “substantially.”

But if a company performs poorly, or the deal is likely to produce a negative IRR, a Dividend Recap will make the results even worse.

**The Dividend Recap Rationale and a Simple Example**
-----------------------------------------------------

There are two types of Dividend Recaps in leveraged buyouts: **unleveraged and leveraged**.

In an Unleveraged Dividend Recap, a private equity-owned portfolio company issues a Dividend to the PE firm during the holding period without issuing additional Debt.

The portfolio company might do this if it generates significant [Free Cash Flow](https://breakingintowallstreet.com/kb/financial-statement-analysis/how-to-calculate-free-cash-flow/)
 and has low Debt principal repayments.

There isn’t much to say about this type of Dividend Recap because it’s simple to build into models.

The more interesting variation is the **Leveraged Dividend Recap**, in which the portfolio company issues additional Debt to fund the Dividend.

If the company performs well, this mechanism can boost the IRR because of the [time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
.

For example, consider the scenario shown below, in which the PE firm acquires a company, operates it, and sells it in Year 5:

![LBO Model with No Dividend Recap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20894%20557'%3E%3C/svg%3E "LBO Model with No Dividend Recap")

This result is “OK,” but the PE firm could get better results by tweaking its strategy.

We know the company repays significant Debt because the Debt balance decreases from $600 to $240 by the end.

That Debt repayment provides a benefit because it reduces the company’s Interest Expense in the holding period and increases the Exit Equity Proceeds in Year 5.

**BUT** if the company could distribute its cash flows to the PE firm, or the company could issue more Debt and distribute the proceeds to the PE firm, the benefit could be even greater.

For example, here’s what it looks like if the company **repays no Debt** and issues 100% of its available cash flow to the PE firm:

![LBO Model with Dividend Distributions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20892%20573'%3E%3C/svg%3E "LBO Model with Dividend Distributions")

The IRR increases by ~3%, but this scenario is **not realistic** because the lenders in almost all leveraged buyouts require _some_ Debt principal repayment.

They want to see that the company is generating healthy cash flows and using them to repay some Debt over time.

Waiting until the exit for _any_ repayment creates too much risk, especially if the deal underperforms.

So, a more realistic option is to assume the normal Debt principal repayments in the holding period and _additional Debt issuances to fund Dividend distributions_ to the PE firm.

This option is the Leveraged Dividend Recap described above.

Here’s what happens if the company issues $126 million of extra Debt in Year 3, approximately 1x the Year 3 EBITDA, and distributes the proceeds to the PE firm (we ignore fees in this simplified model):

![LBO Model with Dividend Recap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20893%20576'%3E%3C/svg%3E "LBO Model with Dividend Recap")

The final Debt balance in Year 5 is higher than in the first scenario, but the PE firm also receives a cash distribution earlier in the holding period.

Since money in Year 3 is worth more than money in Year 5, the internal rate of return increases, even though the money-on-money multiple stays the same.

Remember that **leverage** is a double-edged sword: it doesn’t “boost returns” but _amplifies_ returns.

If a deal performs poorly, more leverage will make it perform even worse, and if it performs well, more leverage will make it even better.

A Leveraged Dividend Recap is a form of additional leverage, so the same principles apply here.

For example, consider a scenario in which this company’s [EBITDA](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
 _declines_ by nearly 20% from Year 1 through Year 5, resulting in a negative IRR:

![LBO with a Negative IRR and No Dividend Recap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20894%20408'%3E%3C/svg%3E "LBO with a Negative IRR and No Dividend Recap")

If the PE firm executed a Dividend Recap for 1x EBITDA in Year 3, it would make the deal results even worse:

![LBO with a Negative IRR and a Dividend Recap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20889%20546'%3E%3C/svg%3E)

**The Dividend Recap in a Full LBO Model**
------------------------------------------

Implementing a Leveraged Dividend Recap in an LBO model takes a moderate amount of work, but it’s not that difficult if you have a properly constructed model with a robust [Debt Schedule](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
.

First, you need to include the additional Debt issuances and add this new funding to the company’s “Cash Flow Available Before Revolver” or “Cash Flow Available for Debt Repayment”:

![Dividend Recap in the Sources of Funds Section in an LBO Debt Schedule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20241'%3E%3C/svg%3E "Dividend Recap in the Sources of Funds Section in an LBO Debt Schedule")

Often, you assume additional Term Loans to fund this Dividend because Term Loans have mandatory and optional principal repayments, meaning that the Term Loan balance tends to **decrease** over time.

For example, if the company starts with a 3x Term Loan / EBITDA ratio and it repays some of the balance and reaches 2x by Year 3, it may issue Term Loans for another 1x EBITDA.

Yes, its Debt load increases, but it’s not a problem because it’s simply returning to the initial level.

Once you have this set up, you can modify the Mandatory Repayment schedule to include the additional issuance(s) for the Dividend Recap:

![Dividend Recap in Mandatory Debt Repayments of an LBO Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20749'%3E%3C/svg%3E "Dividend Recap in Mandatory Debt Repayments of an LBO Model")

The Optional Repayment or “Cash Flow Sweep” formula should not need to change _if you’ve set it up properly_, i.e., it deducts Mandatory Repayments in the period.

Similarly, you shouldn’t need to change anything in the Interest Calculations as long as they’re based on the _changing Debt balances_ over time.

On the [Cash Flow Statement](https://breakingintowallstreet.com/kb/accounting/cash-flow-statement/)
 or “mini-Cash Flow Statement,” you can support the Leveraged Dividend Recap by deducting the Dividend Issuances, net of issuance fees, and adding the proceeds received:

![Dividend Recap on the Cash Flow Statement of an LBO Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20440'%3E%3C/svg%3E "Dividend Recap on the Cash Flow Statement of an LBO Model")

Finally, on the Income Statement, you should technically change the Amortization of Financing Fees to reflect the additional fees on this Term Loan issuance:

![Dividend Recap on the Income Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20708'%3E%3C/svg%3E "Dividend Recap on the Income Statement")

But this Amortization line item is small, non-cash, and only makes a tiny impact on the company’s taxes, so we ignore the change here.

If the company had substantial Dividend Recaps in each year of the model, it would be more important to reflect the higher Amortization number.

You can see the impact of this Dividend Recap directly on the Balance Sheet: a higher Debt balance and lower Common Shareholders’ Equity when it takes place:

![Dividend Recap on the Balance Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20700'%3E%3C/svg%3E)

**The Dividend Recap in the Returns Calculation of an LBO Model**
-----------------------------------------------------------------

There is one final step: you must reflect these Dividends in the returns calculations.

The Excel file and video tutorial here skip this step because they’re excerpts from a 20-part case study in which we calculate the returns in a later segment.

Here’s the finished product:

![Dividend Recap Impact on the Sponsor Returns in an LBO](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20243'%3E%3C/svg%3E "Dividend Recap Impact on the Sponsor Returns in an LBO")

As a result of this Leveraged Dividend Recap, the PE firm receives some of the proceeds earlier in the holding period, but it must also repay a higher Debt balance upon exit.

Here’s how the Dividend Recap in this model affects the results:

![Dividend Recap in an LBO: Before and After](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20531'%3E%3C/svg%3E)

The Dividend Recap boosts the IRR by less than 1% because it’s very low relative to the purchase and exit multiples and the initial amount of Debt.

Dividend Recaps can make “borderline” deals look a bit better (e.g., if the baseline IRR is 18%, a Recap might boost it to 20% or 21%), but they’re usually not enough to turn a “no” investment recommendation into a “yes.”

For example, if the deal produces a 10% or 15% IRR in the Base Case vs. a 20% target, a single Dividend Recap will not make the deal acceptable.

Dividend Recaps tend to make the biggest difference for **high-growth companies** and **high FCF margin companies**.

In the first case, the company’s EBITDA and FCF grow substantially, resulting in substantial Debt paydown and the ability to issue more Debt over time.

In the second case, the company’s EBITDA and FCF do not necessarily grow, but since the company can repay Debt quickly, it can easily issue more during the holding period.

You’ll see this strategy frequently in emerging and frontier markets, where many companies are growing quickly but cannot issue much Debt initially (e.g., 2-3x Debt / EBITDA rather than 5-6x).

In these deals, multiple Dividend Recaps in the holding period can make a substantial difference in the financial results.

_**This tutorial is a small taste of the knowledge you’ll gain in our paid courses.**_ **Breaking Into Wall Street** _**uses real-life modeling tests and interview case studies to prepare you for investment banking and private equity interviews – and a leg up once you win your offer and start working. Find out more about our advanced training by via the button below:**_

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/13-13-Debt-Schedule-Part-3-Div-Recap.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) More Advanced LBO Model - Dividend Recap - Before (XL)](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/13-13-Debt-Schedule-Part-3-Div-Recap-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) More Advanced LBO Model - Dividend Recap - After (XL)](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/13-13-Debt-Schedule-Part-3-Div-Recap-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&mini=true)
[Email](mailto:?subject=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&mini=true)
[](mailto:?subject=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[](https://api.whatsapp.com/send?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/#)
[Email](mailto:?subject=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&t=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2021/07/04225010/The-dividend-recap-1.jpg&description=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[SMS](sms:?&body=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[X](https://x.com/intent/tweet?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fdividend-recap%2F&title=The%20Dividend%20Recap%20in%20an%20LBO%20Model%3A%20Full%20Tutorial&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2021/07/04225010/The-dividend-recap-1.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand