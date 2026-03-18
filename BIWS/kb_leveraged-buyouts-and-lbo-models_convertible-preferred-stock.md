# Convertible Preferred Stock in Leveraged Buyouts

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock

---

Convertible Preferred Stock in Leveraged Buyouts: Full Guide + Excel Examples
=============================================================================

In a leveraged buyout, Convertible Preferred Stock gives the investors downside protection plus potential equity upside by giving them the option to convert into common shares in the exit if the deal performs well enough – or stay in Preferred and earn back a higher balance by the end.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#tab-signup)
    

> **Convertible Preferred Stock Definition:** In a leveraged buyout, Convertible Preferred Stock gives the investors downside protection _plus_ potential equity upside by giving them the _option_ to convert into common shares in the exit if the deal performs well enough – or stay in Preferred and earn back a higher balance by the end.

Convertible Preferred Stock is common in many situations, ranging from standalone company operations to venture capital deals, but this article focuses on its uses in **leveraged buyouts**.

It’s easiest to illustrate the mechanics with a simple example: Suppose a company acquired in a leveraged buyout has issued Convertible Preferred Stock with a 12% coupon rate attached.

If the [internal rate of rate (IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
 to the Common Equity investors (i.e., the private equity firm) in the deal is 5%, the Convertible Preferred investors will stay in Preferred and earn a 12% IRR in the exit due to the 12% coupon rate.

But if the Common Equity IRR is 25%, the Convertible Preferred investors will **convert into common shares** in the exit and earn this 25% IRR.

There are some limitations to the downside protection and the amount of Convertible Preferred that may be used to fund deals, but it is still useful in many deals.

### **Files & Resources:**

*   [Convertible Preferred Stock in LBO Models (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-25-Convertible-Preferred-Stock.xlsx)
    
*   [Convertible Preferred Stock in LBO Models – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-25-Convertible-Preferred-Stock-Slides.pdf)
    

**Convertible Preferred Stock Mechanics in a Simple LBO Model**
---------------------------------------------------------------

Setting up Convertible Preferred Stock in a [simple LBO model](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/simple-lbo-model-excel/)
 requires **initial assumptions**, modifications to the **3 financial statements (or cash flow projections)**, and changes to the **exit calculations**.

The first two parts are straightforward, but the last one is tricky:

### **Convertible Preferred Stock, Part 1: Assumptions**

First, you make assumptions about the Convertible Preferred Stock used in the deal, the Conversion Price, and the number of Potential Shares it represents.

The traditional Debt used in an LBO is typically based on a **leverage ratio**, or multiple of EBITDA, and so is the Convertible Preferred.

This model uses 4.0x EBITDA for the traditional Debt and 1.0x for the Convertible Preferred:

![Convertible Preferred Stock Assumptions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201862%20859'%3E%3C/svg%3E "Convertible Preferred Stock Assumptions")

The **Conversion Price** is normally based on the Offer Price per Share in the initial deal, which equals the Purchase Equity Value / Pre-Deal Share Count, or $10.00 here.

The Potential Shares equal the Convertible Preferred Balance / Conversion Price, or $50 million / $10.00 = 5.0 million.

You also assume a **coupon rate** on the Convertible Preferred Stock, such as 12% here.

This is normally [accrued or Paid-in-Kind (PIK)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
, meaning the company does not pay these Preferred Dividends in Cash; instead, they increase the Convertible Preferred balance each year.

You can also plot the **fully diluted ownership** in the [Sources & Uses schedule](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/sources-and-uses/)
:

![Convertible Preferred Stock Sources & Uses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201855%20510'%3E%3C/svg%3E "Convertible Preferred Stock Sources & Uses")

### **Convertible Preferred Stock, Part 2: LBO Model Flow**

In the cash flow projections, Convertible Preferred Stock with 100% Accrued Dividends makes no net impact because the Preferred Dividends are **non-cash and not tax-deductible**.

So, you deduct them on the [Income Statement](https://breakingintowallstreet.com/kb/accounting/income-statement/)
 under the “Net Income” line to calculate “Net Income to Common” and then add them back on the [Cash Flow Statement](https://breakingintowallstreet.com/kb/accounting/cash-flow-statement/)
.

These Dividends then increase the Convertible Preferred Stock on the [Balance Sheet](https://breakingintowallstreet.com/kb/accounting/balance-sheet/)
 each year:

![Convertible Preferred Stock - Cash Flow and Balance Sheet Links](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201853%20917'%3E%3C/svg%3E "Convertible Preferred Stock - Cash Flow and Balance Sheet Links")

![Private Equity Modeling (LBO Course)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Practice 12+ LBO Models and Prepare Like a Pro for Private Equity Interviews

*   #### Build 6 "conceptual" LBO models
    
    Start by learning the concepts and formulas with these models
    
*   #### Prep for interview questions
    
    Practice with LBO math interview questions, paper LBOs, and more
    
*   #### Complete 6 full case studies
    
    Learn real-life LBO models and how to make investment recommendations
    

[Full Details](https://breakingintowallstreet.com/private-equity-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Private-Equity-Modeling-Course-Outline.pdf)

### **Convertible Preferred Stock, Part 3: Exit Calculations**

The trickiest part of this model setup is the **exit** because many formulas must change.

Also, Convertible Preferred Stock creates a [circular reference](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
, and you need a special setup to avoid it with an approximation.

You can start by changing the [Enterprise Value / Equity Value bridge](https://breakingintowallstreet.com/kb/equity-value-enterprise-value/how-to-calculate-enterprise-value/)
 so there are separate lines for Cash, Non-Convertible Debt, and the Convertible Preferred treated as either Debt or Equity (depending on the deal results):

![Convertible Preferred Stock in the Exit Enterprise Value Bridge](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201857%20505'%3E%3C/svg%3E "Convertible Preferred Stock in the Exit Enterprise Value Bridge")

You can leave the “Convert to Common” line blank for now and calculate the Common Share Price by dividing the Exit Equity Value by the Diluted Share Count in the exit:

![Convertible Preferred Stock - Common Share Price in Exit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201856%20937'%3E%3C/svg%3E "Convertible Preferred Stock - Common Share Price in Exit")

The Convertible Preferred Share Count is based on the 5.0 million shares times this “Convert to Common” switch, which may be 1 or 0 (it’s still blank for now, which effectively means 0).

Next, you compare the “Accrued Value” of the Convertible Preferred to its Value as Common Shares, which is based on the 5.0 million shares \* Common Share Price in Exit:

![Convertible Preferred Stock - Conversion Switch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201862%20486'%3E%3C/svg%3E "Convertible Preferred Stock - Conversion Switch")

The “Convert to Common” switch is 1 if the Convertible Preferred is worth more as Common Shares and 0 if it’s worth more as Debt (the “Accrued Value”).

This creates a **circular reference** because the Diluted Share count in the exit depends on the conversion decision, but the conversion decision also depends on the Diluted Share count!

There are some tricks to get around this (see below), but it’s a common issue with Convertible Preferred Stock.

As the next step, you return to the bridge calculations at the top and deduct either the Convertible Preferred as **Debt** or **Equity**, depending on the investors’ conversion decision:

![Convertible Preferred Stock - Conversion Comparison and Decision](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201865%20769'%3E%3C/svg%3E "Convertible Preferred Stock - Conversion Comparison and Decision")

You use a negative sign for the Accrued Value and multiply by (1 – Conversion Switch) for the Debt; for the Equity, multiply the Value as Common Shares by the Conversion Switch and put a negative sign in front.

You can then calculate the [cash-on-cash multiple and IRR](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
 for each group, which demonstrates the advantages of Convertible Preferred Stock in different deal outcomes:

![Convertible Preferred Stock - IRRs and Multiples](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201861%20815'%3E%3C/svg%3E "Convertible Preferred Stock - IRRs and Multiples")

**Why Convertible Preferred Stock Does Not “Guarantee” Returns in an LBO**
--------------------------------------------------------------------------

Suppose this deal is a complete disaster and the multiple falls from 12x in the initial deal to the **2 – 4x range** in the exit.

In this case, there won’t be enough exit proceeds after the repayment of the traditional Debt to cover the full Convertible Preferred Stock balance.

You can set this up with MIN formulas based on the remaining proceeds and the owed Debt balances:

![Convertible Preferred Stock - Poor Returns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201867%201046'%3E%3C/svg%3E "Convertible Preferred Stock - Poor Returns")

The Convertible Preferred Stock IRRs fall to the 2 – 5% range in this case because the investors **are not fully repaid in the exit**.

The same issue comes up with [liquidation preferences](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
 in VC deals: Yes, they protect the investors in the case of an exit at a reduced valuation, but they don’t help if it’s a true disaster.

**How to Avoid Circular References from the Convertible Preferred Stock Calculations**
--------------------------------------------------------------------------------------

Circular references make models unstable and more difficult to modify, so many groups and firms do not allow them.

If your model has circular references, you should **always** build in the option to disable them by using a simple approximation for the numbers.

**One “trick” here is to escalate the initial Investor Equity AT the rate of return on the Convertible Preferred Stock and compare that to the Exit Equity Proceeds assuming the Convertible Preferred is counted as traditional Debt.**

This tells you whether the Common Equity has increased by more than 12% per year.

If it has, the investors should convert into Common Shares; if not, they should stay in the Convertible Preferred Stock:

![Convertible Preferred Stock - Avoiding Circular References](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201871%20905'%3E%3C/svg%3E "Convertible Preferred Stock - Avoiding Circular References")

You can add this feature by building in a “switch” for circular references at the top and then referencing it in the Convert to Common switch at the bottom, as shown above.

If circular references are enabled, compare the Accrued Value to the Value as Common Shares.

If they’re disabled, compare the Common Equity at the Convertible Preferred Rate of Return to the Exit Equity Value with the Convertible Preferred treated _as Debt_ and base the decision on that.

This method is slightly less accurate, but it also produces models that are more stable and easier to modify.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Convertible Preferred Stock in LBO Models - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-25-Convertible-Preferred-Stock-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Convertible Preferred Stock in LBO Models (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-25-Convertible-Preferred-Stock.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&mini=true)
[Email](mailto:?subject=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[](https://www.linkedin.com/shareArticle?title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&mini=true)
[](mailto:?subject=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[](https://api.whatsapp.com/send?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#)
[Email](mailto:?subject=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&t=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[SMS](sms:?&body=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[X](https://x.com/intent/tweet?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fconvertible-preferred-stock%2F&title=Convertible%20Preferred%20Stock%20in%20Leveraged%20Buyouts%3A%20Full%20Guide%20%2B%20Excel%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand