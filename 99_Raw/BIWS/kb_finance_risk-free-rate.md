# Risk-Free Rate: Full Tutorial and Examples

**Source:** https://breakingintowallstreet.com/kb/finance/risk-free-rate

---

The Risk-Free Rate: Full Definition and Excel Examples
======================================================

The Risk-Free Rate (RFR) represents the annualized return you could earn on assets that are free of default risk, such as “safe” government bonds that will almost certainly be repaid; it is a central part of the Discount Rate calculation and all corporate valuation.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#tab-signup)
    

The Risk-Free Rate: Full Definition and Excel Examples

> **Risk-Free Rate Definition:** The Risk-Free Rate (RFR) represents the annualized return you could earn on assets that are free of _default risk_, such as “safe” government bonds that will almost certainly be repaid; it is a central part of the Discount Rate calculation and all corporate valuation.

In most analyses, such as the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
 or WACC calculation, the Risk-Free Rate equals the [yield to maturity (YTM)](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
 on 10-year government bonds denominated in the same currency as this company’s financial statements.

For example, if the company operates globally but reports its financials in British pounds (GBP), you use the 10-year U.K. government bond yield (“Gilt bonds”) for the Risk-Free Rate, [which you can easily find online](https://tradingeconomics.com/united-kingdom/government-bond-yield)
.

If the company reports in U.S. Dollars, you use the 10-year U.S. Treasury yield, [which you can also find online](https://www.cnbc.com/quotes/US10Y)
.

Government bonds in countries like the U.S. and U.K. are considered “safe” because the chance of government default is nearly 0 (although “soft defaults” can still happen).

This is because these countries control their own currencies and their own money supplies, so if push came to shove, they could simply print more money to repay looming debt maturities (at the cost of increasing inflation).

If you’re analyzing a company in an emerging market without good data for 10-year government bond yields, you could calculate the Risk-Free Rate by taking the U.S. Risk-Free Rate and adding the **country default spread**, [which Aswath Damodaran tracks here](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
.

This Risk-Free Rate is used to calculate the Cost of Equity in the WACC formula in corporate valuation and may even be used to calculate the Cost of Debt in some cases.

Since the RFR _directly_ influences the required or expected returns (i.e., the Discount Rate), it is therefore central to all corporate and asset valuation.

### **Files & Resources:**

*   [Risk-Free Rate – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/Risk-Free-Rate/Risk-Free-Rate-Slides.pdf)
    
*   [Risk-Free Rate – Simple Demonstration File (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/Risk-Free-Rate/Risk-Free-Rate-Reference.xlsx)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **3:58:** What is the Risk-Free Rate?
*   **5:53:** Interest-Rate Risk
*   **13:39:** Currency Risk
*   **16:51:** Inflation Risk
*   **19:44:** Recap and Summary

**Why the Risk-Free Rate Does Not Actually Mean “Risk Free”**
-------------------------------------------------------------

Before moving on, we must emphasize one point: **Government bonds are not _free of risk_ – they are simply assumed to be _free of_ _default risk_.**

They have many other risks attached, such as the inflation risk, currency risk, and interest-rate risk.

**It is 100% possible to invest in U.S. government bonds and _lose money_ even though they appear to be “risk-free.”**

For example, the Vanguard Long-Term U.S. Treasury Fund declined by ~23% between early 2022 and early 2023, as the Federal Reserve aggressively raised interest rates to fight inflation:

![Vanguard Long-Term U.S. Treasuries Performance](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20404'%3E%3C/svg%3E "Vanguard Long-Term U.S. Treasuries Performance")

How could this happen?

As prevailing interest rates rise, the prices of **existing bonds** fall because most of these existing bonds were issued when interest rates were much lower.

If a bond has a coupon rate of 2% when interest rates are at 0%, it looks quite appealing – but if the central bank raises interest rates to 4%, a 2% rate is considerably less appealing.

Why buy this bond and earn 2% interest when you could buy _new_ government bonds and earn 4% interest or more?

This is exactly what happened between early 2022 and early 2023, which is why long-term U.S. Treasuries declined in value.

**NOTE:** In this scenario, you would have lost money only if you had _sold_ your U.S. Treasuries early (i.e., in 2023 rather than waiting until maturity).

If you had purchased them and held them to maturity in 10 years, you would have earned interest and recovered your full principal – but that full principal would have been worth less in real terms after 10 years due to inflation.

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

**How to Use the Risk-Free Rate in Valuation: WACC and the Cost of Equity**
---------------------------------------------------------------------------

In the Capital Asset Pricing Model (CAPM), the Cost of Equity – the expected or targeted annualized return that you could earn by investing in a company’s stock – is based directly on the Risk-Free Rate.

The formula is:

**Cost of Equity = Risk-Free Rate + Equity Risk Premium \* Levered Beta.**

The intuition is that the RFR is the baseline rate of return that you could earn by investing in “safe” government bonds and holding them until maturity.

However, the stock market as a whole and individual stocks are much riskier than government bonds because specific companies could fail, go bankrupt, shut down, or otherwise see their stock prices plummet by 90%+.

Since the stock market is riskier than government bonds, it must offer **higher potential returns** to compensate for this risk.

These higher potential returns are represented by the **Equity Risk Premium (ERP)**, which is calculated as the expected annualized return of the stock market _minus_ the Risk-Free Rate.

So, for example, if the stock market is expected to return 10% per year over the long term, on average, and the RFR is currently 4%, the ERP is 6%.

However, the ERP is for _the stock market as a whole_.

We need to adjust it for the specific company we are analyzing, which is where the “Levered Beta” term factors in.

You can find this “Levered Beta” on sources like Bloomberg, Capital IQ, FinViz, or Yahoo Finance, and it represents the company’s overall volatility relative to the entire stock market.

For example, if Levered Beta is 1.5 and the stock market goes up by 10%, the company’s stock price should go up by 15%; if the market goes down by 10%, the company’s stock price should go down by 15%.

You can see an example of these calculations below in the valuation of Steel Dynamics in our [Core Financial Modeling Course](https://breakingintowallstreet.com/core-financial-modeling/)
:

*   **Cost of Equity (Current Capital Structure)** = 1.20% + 5.50% \* 1.52 = 9.55%
*   **Cost of Equity (Optimal Capital Structure)** = 1.20% + 5.50% \* 1.68 = 10.45%

![Steel Dynamics - Risk-Free Rate, the Cost of Equity, and WACC](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20713'%3E%3C/svg%3E "Steel Dynamics - Risk-Free Rate, the Cost of Equity, and WACC")

The next step here is to calculate the Cost of Debt and Cost of Preferred Stock (if applicable) and use them and the capital structure percentages to estimate the overall [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
, or [WACC](https://mergersandinquisitions.com/wacc-formula/)
, for the company.

Then, we use this Discount Rate in a [DCF model](https://mergersandinquisitions.com/dcf-model/)
 to estimate the [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
 of the company’s future cash flows and determine whether it is valued appropriately based on its current stock price.

**How to Use the Risk-Free Rate in Valuation: The Cost of Debt**
----------------------------------------------------------------

When calculating the Cost of Debt for use in this WACC formula, we could simply use the yield to maturity (YTM) of the company’s bonds or even their simple interest rate.

But there is another alternative: We could take the Risk-Free Rate and then add the company’s _credit default spread_ based on its current credit rating, which is normally linked to credit metrics such as Debt / EBITDA and EBITDA / Interest.

Again, [Aswath Damodaran from NYU tracks this data each year](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html)
.

For example, if the current Risk-Free Rate is 4%, and the company’s Interest Coverage Ratio (EBITDA / Interest or a close variation) is between 2.00x and 2.50x, its credit default spread is approximately 2%.

Therefore, its Cost of Debt based on this method is 4% + 2% = 6%, and we could use this in the WACC formula.

**Interview Questions: What Happens If the Risk-Free Rate Changes?**
--------------------------------------------------------------------

In [investment banking interviews](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/)
, questions about **components** of WACC, the Cost of Equity, and the Cost of Debt are common.

A higher Risk-Free Rate **increases** both the Cost of Debt and the Cost of Equity and, therefore, increases WACC.

This is because when the Risk-Free Rate is higher, investors can earn higher annualized returns by investing in government bonds – so they need higher potential returns to invest in **risk assets**, such as corporate bonds or stocks.

As a result, **companies’ valuations fall when the Risk-Free Rate rises** – because government bonds are now relatively more appealing to investors.

When the Risk-Free Rate is lower, the opposite happens: The Cost of Equity and Cost of Debt both fall, WACC falls, and companies’ implied values from a DCF analysis increase.

Since government bonds now yield less, investors are more incentivized to take risks by investing in companies rather than sticking to the “safe” assets.

Some people argue that these rules are not necessarily true because when the Risk-Free Rate changes, the **Equity Risk Premium** might also change.

There is some truth to that, so these changes are less predictable in real life.

For _interview purposes_, however, it’s helpful to keep in mind this summary of factors that affect WACC:

![How the Risk-Free Rate and WACC Affect the DCF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201354%20865'%3E%3C/svg%3E "How the Risk-Free Rate and WACC Affect the DCF")

**The Risk-Free Rate and Bond Prices**
--------------------------------------

Bond pricing is very similar to company valuation: It’s based on the Present Value of future cash flows.

The differences are that a bond’s cash flows are much more predictable, and the bond’s maturity date is always known, so there are no debates about the forecasts or the cash-flow numbers to use.

When the Risk-Free Rate increases, the **Discount Rate** used to value the bond increases, so the bond’s price falls.

It’s the same as the idea discussed above: If a government bond yields 4% when similar bonds yield 3%, it’s quite appealing.

But if the central bank now raises rates so that new, similar bonds offer 5%, the 4% bond is less appealing.

So, its price falls such that the _yield to maturity_ on this bond now equals the 5% that newly issued bonds in this environment offer.

If the Risk-Free Rate decreases, the opposite happens, and the bond’s price increases because it is now comparatively more appealing.

[Sign Up for Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Risk-Free Rate – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/Risk-Free-Rate/Risk-Free-Rate-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Risk-Free Rate – Simple Demonstration File (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/Risk-Free-Rate/Risk-Free-Rate-Reference.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&mini=true)
[Email](mailto:?subject=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&mini=true)
[](mailto:?subject=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[](https://api.whatsapp.com/send?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Copy](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#)
[Email](mailto:?subject=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&t=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
[Pinterest](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#)
[Print](https://breakingintowallstreet.com/kb/finance/risk-free-rate/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[SMS](sms:?&body=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[X](https://x.com/intent/tweet?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Frisk-free-rate%2F&title=The%20Risk-Free%20Rate%3A%20Full%20Definition%20and%20Excel%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand