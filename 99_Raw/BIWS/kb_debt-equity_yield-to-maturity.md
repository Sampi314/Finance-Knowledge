# Yield to Maturity (YTM): Definition and Excel Examples

**Source:** https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity

---

Yield to Maturity (YTM): Definition, Calculations, Meaning, and Excel Examples
==============================================================================

The Yield to Maturity (YTM) of a bond is the annualized return an investor will receive if they buy a bond at its current market price and hold it until maturity, assuming the company makes all the required payments, and the investor reinvests the interest payments at the same rate as the overall return.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#tab-signup)
    

Yield to Maturity (YTM): Definition, Calculations, Meaning, and Excel Examples

Yield to Maturity Definition
----------------------------

> The Yield to Maturity (YTM) of a bond is the annualized return an investor will receive if they buy a bond at its current market price and hold it until maturity, assuming the company makes all the required payments, and the investor reinvests the interest payments at the same rate as the overall return.

The YTM measures “what should happen” when an investor buys a bond – but often does not.

In many cases, investors decide to sell bonds early because of changes in the macro environment or the company’s credit profile.

The YTM ignores all these possibilities and assumes that the investor _does_ hold the bond until the official maturity date, at which point, the company repays it in full.

Unlike metrics such as the [Current Yield](https://breakingintowallstreet.com/kb/debt-equity/current-yield/)
, the Yield to Maturity measures **the annualized return over many years**.

Unlike metrics such as the [Yield to Call](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
 or [Yield to Worst](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
, the Yield to Maturity **assumes NO early repayment**.

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

The Yield to Maturity changes based on the bond’s current market price, its coupon rate, the time until maturity, and the repayment probability – though this probability is assumed to be 100% for healthy companies.

Here’s a simple Excel example for the YTM calculation of a **discount bond** that trades at $900 vs. a par value of $1,000:

![YTM Calculation Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201514%20718'%3E%3C/svg%3E "YTM Calculation Example")

### **Files & Resources:**

[Bond Yields – Formulas and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Formula.xlsx)

[Yield to Maturity – Calculation Methods (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Example-Calculations.xlsx)

There are several ways to calculate or approximate the Yield to Maturity, which we’ll describe below:

**YTM Formula: How to Calculate the Yield to Maturity in Excel**
----------------------------------------------------------------

The easiest method, by far, is to use the YIELD function in Excel, which accounts for all the assumptions mentioned above.

We use this YIELD function in the screenshot shown above, and you can see it directly in the Excel download available on this page.

The assumptions here are as follows:

**Bond Price:** $900 (vs. par value of $1,000, so it’s trading at a 10% discount)

**Coupon Rate:** 5% (so, interest payments will be $1,000 \* 5% = $50 per year)

**Settlement Date (Purchase Date):** December 31, 2024

**Maturity Date:** December 31, 2029 (5-year holding period)

The output is as follows:

![YTM Output from the Excel YIELD Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201398%20714'%3E%3C/svg%3E "YTM Output from the Excel YIELD Function")

The Excel function is:

\=YIELD (Settlement Date, Maturity Date, Coupon Rate, Bond Price % Par Value out of Number 100, 100, Coupon Frequency)

The **intuition** here is that this 10% discount gives investors an “extra boost” over the 5% coupon rate.

Since they hold the bond for 5 years, this 10% discount is spread out over 5 years, and since 10% / 5 = 2%, the annualized return is ~2% higher than 5% (it’s actually closer to ~2.5% higher due to compounding).

**YTM Formula: How to Calculate the Yield to Maturity with the IRR Function**
-----------------------------------------------------------------------------

Since the Yield to Maturity represents the **annualized return** on a bond, you can also use the Internal Rate of Return (IRR) function in Excel to calculate it.

However, this approach takes far more time and effort because you must **project the cash flows of the bond**, including the initial purchase, the interest payments, and the repayment upon maturity.

You can see our setup below:

![Yield to Maturity via the IRR Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201438%20875'%3E%3C/svg%3E "Yield to Maturity via the IRR Function")

Just like how the IRR in an [LBO model](https://mergersandinquisitions.com/lbo-modeling-test/)
 tells you what a PE firm could earn, annualized, on its equity investment in a company, it’s the same principle here with a single bond.

Applying the IRR function to this stream of cash flows confirms that it’s nearly the same as the output from the YIELD function:

![Yield to Maturity - Output from the IRR Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201386%20758'%3E%3C/svg%3E "Yield to Maturity - Output from the IRR Function")

**YTM Formula: How to Calculate the Yield to Maturity with a Quick Approximation**
----------------------------------------------------------------------------------

Another option to calculate YTM is to skip Excel entirely and make a “quick and dirty estimate” using the following formula:

![Approximate YTM Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201318%20208'%3E%3C/svg%3E "Approximate YTM Calculation")

We can apply this formula to the ongoing example here:

**Annual Interest** = $1,000 \* 5% = $50

**(Par Value – Bond Price)** = $1,000 – $900 = $100

**(Par Value + Bond Price) / 2** = ($1,000 + $900) / 2 = $950

**Approximate YTM** = ($50 + $100 / 5) / $950 = $70 / $950 = ~7.4%

To do the math quickly yourself, you can say: $50 + $100 / 5 = $70.

Then, $950 is “halfway” between $1,000 and $900.

$70 / $1,000 = 7%, so you can say that $70 / $950 is “just above 7%” if you had to answer this question in an interview.

The **intuition** for this formula is that the top part shows how much interest you are earning each year PLUS the “annualized gain” (if the bond is purchased at a discount) or MINUS the “annualized loss” (if the bond is purchased at a premium).

Then, you divide by the “average price” of the bond in the denominator to reflect how the interest + gain or loss are earned relative to this “average price” over the holding period.

If you compare the numbers in Excel, you’ll see that the approximate YTM is **lower** than the real YTM:

![Approximate YTM - Differential to Real YTM Numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201380%20871'%3E%3C/svg%3E "Approximate YTM - Differential to Real YTM Numbers")

This happens because of **compounding** (i.e., when you earn 10% on a $1,000 investment and re-invest it, you now start with $1,100 the next year rather than $1,000 – so the annualized gain or loss is not just a simple percentage divided by the years in the holding period, as the principal keeps increasing over time).

The Excel YIELD and IRR functions account for compounding, but our approximation method does not.

Also, this bond trades at a relative high discount of **10%** (it’s a high discount for a healthy, non-distressed company); this method is more accurate when the discount is much lower.

**Limitations of the “Approximation Method” for the Yield to Maturity**
-----------------------------------------------------------------------

In general, this trick works best for bonds that trade at a low premium or discount and mature soon (e.g., within ~5 years rather than 10 – 15 years).

The longer the holding period and the greater the discount or premium, the less accurate this formula will be.

For example, if this bond traded at a **50% discount**, the YTM approximation would be far less accurate:

![Approximate YTM - Inaccuracies to the Real Yield to Maturity for a Deep Discount Bond](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201404%20722'%3E%3C/svg%3E "Approximate YTM - Inaccuracies to the Real Yield to Maturity for a Deep Discount Bond")

**Current Yield vs. Yield to Maturity vs. Yield to Call vs. Yield to Worst**
----------------------------------------------------------------------------

These yield metrics all measure the **returns** an investor can expect to receive on a bond, but they do it in different ways.

**–[Current Yield](https://breakingintowallstreet.com/kb/debt-equity/current-yield/)
**: This tells you the percentage investors would earn on a bond if they bought it today and **held it for a year**, factoring in the market price and the coupon rate on the bond.

**–[Yield to Maturity](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
**: This gives the annualized return investors earn if they buy a bond at its current market price and **hold it until maturity**, assuming the company makes all the required payments and the investor reinvests the interest payments at the same rate as the overall return.

**–[Yield to Call](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
**: This is similar to the YTM, but investors hold the bond only until **an earlier call date**, not the maturity date, and also receive some type of penalty fee paid by the company in exchange for this early repayment.

**–[Yield to Worst](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
**: This is the lowest annualized return an investor might receive from buying and holding a bond until _either_ early repayment _or_ maturity, i.e., it is the **minimum** of all the YTCs and the YTM.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Bond Yield - Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Formula-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Bond Yield - Formulas and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Formula.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Yield to Maturity - Calculation Methods (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Example-Calculations.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&mini=true)
[Email](mailto:?subject=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[](https://www.linkedin.com/shareArticle?title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&mini=true)
[](mailto:?subject=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[](https://api.whatsapp.com/send?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Copy](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#)
[Email](mailto:?subject=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&t=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
[Pinterest](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#)
[Print](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[SMS](sms:?&body=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[X](https://x.com/intent/tweet?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-maturity%2F&title=Yield%20to%20Maturity%20%28YTM%29%3A%20Definition%2C%20Calculations%2C%20Meaning%2C%20and%20Excel%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand