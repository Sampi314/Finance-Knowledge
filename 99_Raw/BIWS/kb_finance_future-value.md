# Future Value (FV): Definitions and Examples

**Source:** https://breakingintowallstreet.com/kb/finance/future-value

---

Future Value: Meaning, Examples, and How It Relates to Present Value
====================================================================

Future Value is the opposite of Present Value and measures what an investment today is worth in the future based on the Discount Rate, or the targeted/expected annualized return on this investment.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/finance/future-value/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/finance/future-value/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/finance/future-value/#tab-signup)
    

Future Value: Meaning, Examples, and How It Relates to Present Value

> **Future Value Definition:** Future Value is the _opposite_ of Present Value and measures _what an investment today is worth in the future_ based on the Discount Rate, or the targeted/expected annualized return on this investment.

Future Value goes back to the concept of [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
: Money earned _in the future_ is worth less than money today because you could invest money today and earn more with it in the future ([the time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
).

People often cite inflation or interest rates as the explanation for why future money is worth less than “current money,” and while these do play a role, **they are not the real reason why money is worth less today.**

The real reason is the ability to invest today and earn more over time.

The Present Value formula takes a value in the future and divides it by (1 + Discount Rate) ^ # Years to determine what it is worth today.

The Future Value formula takes _a value today_ and _multiplies it_ by (1 + Discount Rate) ^ # Years to determine what it _will be worth_ on a future date.

So, if you invest $1,000 today and earn 10% on it per year (compounded), its Future Value in 5 years I $1,000 \* (1 + 10%) ^ 5 = $1,610.5.

In Excel, you can use the **FV** function to estimate this value, but it’s not strictly necessary because the numbers are so easy to calculate.

Investors often use Future Value to make “quick estimates” for deals and compare potential outcomes across their portfolios.

Estimating the “future value” of a company is also a critical part of analyses such as the [DCF](https://mergersandinquisitions.com/dcf-model/)
 and [LBO model](https://mergersandinquisitions.com/lbo-modeling-test/)
, but in those, it’s normally based on a [valuation multiple](https://breakingintowallstreet.com/kb/valuation/valuation-multiples/)
, such as Enterprise Value / EBITDA, rather than a simple function.

### **Files & Resources:**

*   [Simple Template for Future Value (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/BIWS-Future-Value-Template.xlsx)
    

**The Future Value Formula**
----------------------------

The formula looks like this:

**_FV = CV \* (1 + i) ^ n_**

*   CV = Current Value or Initial Investment Amount
*   i = Expected or Targeted Annualized Return (i.e., the Discount Rate)
*   n = Number of Years in Holding Period

Note that the “Expected or Targeted Annualized Return” here is _not_ the interest rate; it’s normally the [Weighted Average Cost of Capital (WACC)](https://mergersandinquisitions.com/wacc-formula/)
 or the Cost of Equity.

If we were working with a bond and calculating [bond yields](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
, for example, this Future Value formula would not make sense unless the interest paid accrued to the bond principal (as with [PIK Interest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
).

But interest on bonds and loans is normally paid in cash during the holding period, which means that the investors get back their initial principal at the end and earn a cash percentage on this number each year.

The concept of Future Value makes sense only if the _investment itself grows in value_ during the holding period, such as what happens with companies that perform well or with real estate assets that increase in price.

It is possible to calculate Future Value using an assumption for **simple interest** rather than **compounded interest**, but this is a slightly different issue because with either one, the investment itself still grows.

**Simple Interest vs. Compound Interest in Future Value**
---------------------------------------------------------

For example, let’s say that we invest $1,000 today and earn 10% on it per year for 5 years.

If we assume **compound interest**, the Future Value is $1,000 \* (1 + 10%) ^ 5 = $1,610.5, following the formula above.

This is because we earn $100, or 10% \* $1,000, in the first year, and add this $100 to the $1,000 balance.

Then, in Year 2, we earn 10% of this new $1,100 balance, so 10% \* $1,100 = $110, and we add this $110 to the $1,100 to get $1,210.

It keeps going like that until we reach Year 5.

However, with simple interest, the **annual gains are calculated based on just the original principal**, which remains constant through the holding period.

So, in this example, we would earn $1,000 \* 10% = $100 in Year 1, another $100 in Year 2, and so on, and we’d reach $1,500 by Year 5.

Compounding produces a much higher Future Value, and it makes a bigger difference over longer time frames.

**The Future Value Function in Excel**
--------------------------------------

One reason to use the built-in FV function in Excel to calculate the Future Value is that it lets you **vary the compounding frequency and periods**.

You can do this manually as well, but the FV function makes it much easier.

For example, let’s say you’re evaluating a potential investment that will cost you $5,000 in today’s dollars, and you expect annualized returns of ~8% per year over 8 years.

You want these to compound **semiannually**, or **twice per year**, which is easy to implement with the FV function in Excel.

Here’s the required setup and the output:

![Future Value - Excel Setup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201784%20826'%3E%3C/svg%3E "Future Value - Excel Setup")

The Excel formula here is as follows:

\=FV(RATE, NPER, PMT, -CURRENT VALUE)

\=FV(8% / 2, 16, 0, -5000)

We are using 8% / 2 rather than 8% because this is **semiannual compounding**, so we need to divide the annualized return by 2 to get the 4% that compounds in each half-year period.

The **16** is because we expect to hold this investment for 8 years, and 2 half-year periods in each year means there are 8 \* 2 = 16 total periods.

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

**Future Value Function in Real Estate**
----------------------------------------

If you purchase a property and expect that prices will appreciate each year, you can use the Future Value formula to estimate what the property might be worth in several years.

For example, if you buy a property for $1 million today, and its price increases by 8% per year, it will be worth almost $1.5 million in 5 years, as shown below:

![Future Value - Simple Example for a Property](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20856%20378'%3E%3C/svg%3E "Future Value - Simple Example for a Property")

**Future Value vs. Present Value and Net Present Value**
--------------------------------------------------------

All the concepts are based on the **time value of money**.

*   [**Future Value**](https://breakingintowallstreet.com/kb/finance/future-value/)
     takes the current value of an investment and projects what it will be worth in the future based on a targeted or expected annualized return (the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
    ).
*   **Present Value** takes the future value of an investment or cash flow and **discounts** it to what it is worth today based on the Discount Rate.
*   [**Net Present Value**](https://breakingintowallstreet.com/kb/finance/net-present-value/)
     equals the [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
     of an investment, i.e., the sum of its discounted future cash flows, minus the “Asking Price” – what you pay upfront for the investment.

**NPV** is _not_ directly comparable to Future Value because they measure different things: [NPV](https://breakingintowallstreet.com/kb/finance/net-present-value/)
 is about determining whether _you will make money on an investment_, while Future Value simply estimates what an investment might be worth in the future.

It is possible to get a favorable Future Value for an investment but still get a negative NPV.

This normally happens if the “asking price” is far too high and produces an annualized return below the one you are seeking.

For example, let’s say that you could invest $1,000 today and earn 10% per year on it, so that it’s worth $1,611 in 5 years.

If you discount this $1,611 back 5 years to its Present Value today at this 10% Discount Rate, its Present Value is $1,000.

**However, the “asking price” is $1,200.**

So, the owner of this asset will not sell it for $1,000 – they want $1,200.

In this scenario, the [Net Present Value](https://breakingintowallstreet.com/kb/finance/net-present-value/)
 is negative because $1,000 – $1,200 = ($200).

**The problem is that your expectations for the annualized returns do not align with the seller’s.**

For the NPV to be 0%, the Discount Rate would have to be closer to ~6%, which is far below the 10% annualized return you are targeting.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Template for Future Value (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/BIWS-Future-Value-Template.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&mini=true)
[Email](mailto:?subject=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[](https://www.linkedin.com/shareArticle?title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&mini=true)
[](mailto:?subject=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[](https://api.whatsapp.com/send?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Copy](https://breakingintowallstreet.com/kb/finance/future-value/#)
[Email](mailto:?subject=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&t=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/future-value/)
[Pinterest](https://breakingintowallstreet.com/kb/finance/future-value/#)
[Print](https://breakingintowallstreet.com/kb/finance/future-value/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[SMS](sms:?&body=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[X](https://x.com/intent/tweet?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Ffuture-value%2F&title=Future%20Value%3A%20Meaning%2C%20Examples%2C%20and%20How%20It%20Relates%20to%20Present%20Value&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand