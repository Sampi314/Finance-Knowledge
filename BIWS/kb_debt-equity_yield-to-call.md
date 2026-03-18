# Yield to Call: Formula, Meaning, and Excel Examples

**Source:** https://breakingintowallstreet.com/kb/debt-equity/yield-to-call

---

Yield to Call (YTC): Definition, Intuition, and Excel Calculation Examples
==========================================================================

The Yield to Call (YTC) of a bond measures the annualized return an investor receives if they buy the bond at its current market price and hold it until the company “calls” it by repaying the bond early, often with a penalty fee attached.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#tab-signup)
    

Yield to Call (YTC): Definition, Intuition, and Excel Calculation Examples

Yield to Call Definition
------------------------

> The Yield to Call (YTC) of a bond measures the annualized return an investor receives if they buy the bond at its current market price and hold it until the company “calls” it by repaying the bond early, often with a penalty fee attached.

Normally, bond investors (lenders) want companies to _hold their bonds until maturity_, so they receive the full interest payments from the companies over the holding period, such as 5 or 10 years.

In some cases, however, they allow companies to “call” their bonds by repaying them before the maturity date – but they usually charge the companies a penalty fee called a “call premium” to do so.

This penalty fee discourages companies from repaying their bonds early and forces them to consider the trade-offs, i.e., whether it is worth paying the penalty fee just to reduce their interest payments in the future.

This penalty fee and the shorter holding period mean that the Yield to Call (YTC) may differ from the [Yield to Maturity (YTM)](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
, a metric that assumes the investor holds the bond until its official maturity date.

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

If the bond trades at a **discount to par value**, the YTC will be greater than or equal to the YTM.

If the bond trades at a **premium to par value**, the YTC will be less than or equal to the YTM.

The **intuition** is that when the bond trades at a discount, **investors earn a higher annualized return** because they get a discount in the beginning, get repaid more quickly, _and_ get more money back when the company repays them.

For premium bonds, it’s the opposite: Investors pay _extra_ in the beginning rather than receiving a discount, and that extra amount tends to suppress the benefits of the earlier repayment and the penalty fee.

These relationships are critical if you want to understand [bond yields](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
 in depth.

### **Files & Resources:**

[Bond Yields – Formulas and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Formula.xlsx)

[Yield to Call and Yield to Worst – Excel Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Worst-Excel-Example.xlsx)

**Yield To Call (YTC): Simple Calculation and Excel Example**
-------------------------------------------------------------

Suppose that we buy a bond currently trading at a **10% discount to its par value**.

For example, its par value is $1,000, but its current market price is $900.

We buy the bond on December 31, 2023, and it matures in 10 years, on December 31, 2033.

Its coupon rate is 5%, and the company can “call” it by repaying it early, starting on December 31, 2027 (4 years after our purchase).

However, if the company does that, it will pay a **3% penalty fee**, so it will have to pay us $1,000 \* 1.03 = $1,030.

Here are the assumptions entered in Excel:

![Bond Call Premiums](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202116%20634'%3E%3C/svg%3E "Bond Call Premiums")

And here’s the Excel output for this scenario:

![Yield to Call Setup in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201992%20512'%3E%3C/svg%3E "Yield to Call Setup in Excel")

We can calculate the Yield to Call with the function shown below, since YIELD is built into Excel:

![Yield to Call Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201996%20776'%3E%3C/svg%3E "Yield to Call Calculations")

The **key point here** is that the “Bond\_Redemption\_Pct” part must be the **103** shown above, i.e., the 100% principal repayment plus the 3% penalty fee. In Excel bond functions, you always enter these percentages as whole numbers, so the 103% becomes “103” in Excel.

Also, you must use the **early call date** of December 31, 2027, rather than the official maturity date of December 31, 2033.

In this case, the YTC of 8.7% exceeds the YTM of 6.4% because:

**\-It’s a discount bond**, so investors get 10% off the normal price when they purchase it.

**\-There’s a penalty fee** of 3%, so the investors earn back $1,030 rather than $1,000.

**\-The holding period** is 4 years rather than 10 years, so the 10% discount the investors receive on the initial purchase results in a higher _annualized benefit_ over this shorter period.

**The Relationship Between the Yield to Call (YTC) & the Call Premium**
-----------------------------------------------------------------------

The YTC tends to **decrease over time** because the **call premiums** (penalty fees for early repayment) decrease over time.

Early repayments hurt investors more, so the penalty fees are higher – and companies may not be allowed to repay their bonds _at all_ in the first few years.

For example, the call premiums for a 10-year bond might look like this:

**First 3 Years:** A full lockout period (no early repayments) **or** a _very high_ penalty fee, such as the “Make-Whole Price.”

**Next 6 Years:** Steadily decreasing penalty fees, such as Redemption Prices (Call Premiums) of 105%, 104%, 103%, 102%, 101%, and 100% over these 6 years.

**Last Year:** No penalty fee because “early repayment” is irrelevant if there’s less than a year left before maturity.

Here’s a real-life example of call premiums from a Comstock Resources bond:

![Call Premiums for Comstock Resources](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201682%20662'%3E%3C/svg%3E "Call Premiums for Comstock Resources")

To illustrate how this works in Excel, we’ll continue with the example above but assume a **call date** of December 31, 2032 (9-year holding period) and a **call premium of 1%:**

![Yield to Call Calculations on Later Call Dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202012%20886'%3E%3C/svg%3E "Yield to Call Calculations on Later Call Dates")

The YTC is **6.6%**, still higher than the 6.4% YTM, but much lower than the previous YTC of 8.7%.

**As the call date moves later, the Yield to Call decreases because the penalty fees fall, and the benefit of the 10% discount in the beginning is “spread out” over more years.**

A 10% discount is amazing if it’s distributed over 1-2 years, but it’s far less impactful if it’s spread over 9 years.

The YTC would equal the YTM in this case if there were no penalty fee and the “early call date” equaled the maturity date.

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

**For bonds that trade at a discount and that have penalty fees attached to early repayment options:**

\-YTC >= YTM > Current Yield > Coupon Rate

–[YTW](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
 = [YTM](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)

**For bonds that trade at a premium and that have penalty fees attached to early repayment options:**

\-Coupon Rate > Current Yield > YTM >= YTC

–[YTW](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
 < [YTM](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)

**Why Does the Yield to Call Matter in Real Life?**
---------------------------------------------------

In real life, **companies use the Yield to Call to evaluate the trade-offs of refinancing with a new bonds vs. keeping the existing one.**

At a basic level, they might evaluate the financial benefits of getting a lower interest rate on a new issuance vs. the penalty fee they’d have to pay to refinance their current debt.

But they might also look at the **Yield to Call** the current investors would receive in this situation and use it to determine the yield any new issuance would have to offer.

For example, if the YTC is 8%, but the company plans to issue a new bond with a 6% coupon rate to replace their existing issuance, it might have a problem doing so – even if interest rates have fallen.

The issue is that the current investors expect their 8% annualized yield, and both current and new investors might be disappointed if the yield falls to 6% instead.

So, in this situation, the company might have to incentivize the investors by offering something like an [original issue discount (OID)](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
 on this new issuance and allowing them to buy it for less than the par value.

This discount could boost their yield over the 6% stated coupon rate and bring them closer to the 8% yield they’re currently receiving.

This simple example assumes the company’s credit risk profile has stayed the same and nothing else has changed in their financials or the broader macro environment, which may not always be true.

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
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Yield to Call and Yield to Worst - Excel Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Worst-Excel-Example.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&mini=true)
[Email](mailto:?subject=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[](https://www.linkedin.com/shareArticle?title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&mini=true)
[](mailto:?subject=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[](https://api.whatsapp.com/send?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Copy](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#)
[Email](mailto:?subject=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&t=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
[Pinterest](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#)
[Print](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[SMS](sms:?&body=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[X](https://x.com/intent/tweet?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-call%2F&title=Yield%20to%20Call%20%28YTC%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand