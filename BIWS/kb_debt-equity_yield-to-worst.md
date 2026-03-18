# Yield to Worst (YTW): Definition, Intuition, and Excel Calculation Examples

**Source:** https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst

---

Yield to Worst (YTW): Definition, Intuition, and Excel Calculation Examples
===========================================================================

The “Yield to Worst” (YTW) of a bond is the worst-case possible annualized return an investor could earn if they buy the bond at today’s market price and hold it until either maturity or until the company “calls” it by repaying it early; it’s the minimum of the Yield to Call on each possible call date and the Yield to Maturity.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#tab-signup)
    

Yield to Worst (YTW): Definition, Intuition, and Excel Calculation Examples

Yield to Worst Definition
-------------------------

> The “Yield to Worst” (YTW) of a bond is the _worst-case_ possible annualized return an investor could earn if they buy the bond at today’s market price and hold it until either maturity or until the company “calls” it by repaying it early; it’s the minimum of the Yield to Call on each possible call date and the Yield to Maturity.

The true “worst-case scenario” is that the company will **default** on its debt and not be able to pay interest or repay the debt principal on time; the YTW is the “worst-case scenario _assuming interest and principal repayments still happen._”

When a bond trades **at or below par value**, the **Yield to Worst equals the Yield to Maturity**.

In other words, the worst-case outcome for investors in this case is to hold the bond until it matures. If the company “calls it” by repaying the bond early, the investors will earn a **higher annualized return.**

When a bond trades **at a premium to par value**, the **Yield to Worst is less than the Yield to Maturity**.

In other words, if the investors pay a premium for a bond, they _earn more_ if the company waits until the official maturity date to repay the bond rather than repaying it early.

This is because when investors pay a premium, that extra amount is “distributed” over a shorter time frame if the company repays the bond early, which hurts the average annualized returns.

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

The YTW helps investors evaluate the worst-case scenarios and target specific return ranges.

In real life, the Yield to Worst is a common method of **pricing and comparing bonds**.

Metrics such as the [Yield to Call](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
 do not work as well for comparing different bonds because each bond has different call dates and penalty fees for early repayment on those dates.

But the YTW is a **single metric** that factors in every possible YTC and the [YTM](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
 and, therefore, lets you easily compare many different bonds.

### **Files & Resources:**

[Bond Yields – Formulas and Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Maturity-Formula.xlsx)

[Yield to Call and Yield to Worst – Excel Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Debt-Equity/Bond-Yield/Yield-to-Worst-Excel-Example.xlsx)

**Yield to Worst (YTW): Simple Calculation and Excel Example**
--------------------------------------------------------------

Suppose that a bond’s maturity date is June 15th, 2031, and it currently trades at a **5% discount to par value** (market price of $950 vs. par value of $1000). It has a coupon rate of 5%.

The **call premiums** or **penalty fees for early repayment** range from 5.3% in the current year (2024) down to 0% in the final two years (2030 and 2031).

Additionally, the bond is **callable** – meaning the company can repay it early – on June 15th and December 15th of each year.

To calculate the **Yield to Worst** for this bond, you’d start by calculating the **Yield to Call** on each possible call date:

![Yield to Call Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201344%20832'%3E%3C/svg%3E "Yield to Call Calculations")

The Yield to Call is based on the current market price of the bond, the “settlement date” (the purchase date), the coupon rate, the repayment date, and the percentage of the original principal that gets repaid, which reflects the penalty fee.

Once you have all these, you can calculate the Yield to Maturity using the same Excel function, but with a different repayment date and no penalty fee (i.e., the “Redemption Value” should be 100):

![Yield to Maturity](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201593%20560'%3E%3C/svg%3E "Yield to Maturity")

Then, you can take the minimum of all the YTCs and the YTM to calculate the **Yield to Worst.**

Here’s the Excel output for this scenario:

![Yield to Worst Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201253%20724'%3E%3C/svg%3E "Yield to Worst Calculation")

**The Relationship Between the Yield to Worst (YTW) and Bond Discounts and Premiums**
-------------------------------------------------------------------------------------

Since this is a **discount bond**, the YTW equals the YTM. In other words, investors get the **worst deal** if the company waits until the official maturity to repay the bond.

For a **premium bond**, the YTW is **less than** the YTM because in this case, it’s worse for the investors if the company repays the bond early.

Here’s an example of the same scenario, but with a bond that trades at a 5% premium (market price of $1,050 vs. a par value of $1,000):

![Yield to Worst for a Premium Bond](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201174%20590'%3E%3C/svg%3E "Yield to Worst for a Premium Bond")

The YTW can **never** exceed the YTM; it’s always less than or equal to the YTM, depending on the bond’s price:

**Discount Bond:** YTW = YTM

**Par Value Bond:** YTW = YTM

**Premium Bond:** YTW < YTM

**Why Does the Yield to Worst Matter in Real Life?**
----------------------------------------------------

In investment banking groups such as [Leveraged Finance](https://mergersandinquisitions.com/leveraged-finance/)
 and [Debt Capital Markets](https://mergersandinquisitions.com/debt-capital-markets/)
, you often use the **Yield to Worst** as part of the Debt comps (i.e., an analysis of comparable Debt issuances from similar companies) when advising clients on possible refinancings.

For example, the YTW might give a client an approximate idea of what they might pay on a new bond issuance if they want to raise capital.

This YTW _might_ represent the coupon rate on a new bond, but it could also represent the “overall yield” on the bond, which might include a possible [original issue discount (OID)](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
 and call premium as well.

For example, even if the YTW is 8%, it doesn’t necessarily mean the company has to issue a new bond with an 8% coupon rate.

Instead, the company might be able to issue bonds at a 7.0% or 7.5% coupon rate and then **offer investors a discount** on the purchase that results in a yield closer to 8%.

The YTW is almost always included as a key field in these “Comparable Debt Issuances,” as shown below in a case study based on Netflix and its peer media/streaming companies, taken from our [Advanced Financial Modeling course](https://breakingintowallstreet.com/advanced-financial-modeling/)
:

![Yield to Worst in Debt Comparables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20653'%3E%3C/svg%3E "Yield to Worst in Debt Comparables")

![Yield to Worst Summary for Netflix Debt Comps](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20568'%3E%3C/svg%3E "Yield to Worst Summary for Netflix Debt Comps")

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

[X](https://x.com/intent/tweet?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&mini=true)
[Email](mailto:?subject=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[](https://www.linkedin.com/shareArticle?title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&mini=true)
[](mailto:?subject=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[](https://api.whatsapp.com/send?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Copy](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#)
[Email](mailto:?subject=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&t=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
[Pinterest](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#)
[Print](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[SMS](sms:?&body=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[X](https://x.com/intent/tweet?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Fyield-to-worst%2F&title=Yield%20to%20Worst%20%28YTW%29%3A%20Definition%2C%20Intuition%2C%20and%20Excel%20Calculation%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand