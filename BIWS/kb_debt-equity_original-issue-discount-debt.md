# Original Issue Discount Debt (OID) on Bonds - Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt

---

Original Issue Discount Debt (OID) Tutorial (12:43)
===================================================

Original Issue Discount refers to when a company issues Debt at a discount to par value. For example, a bond is worth $100 (the “face value” that the company pays interest on), but the company issues it for $90, which lets investors buy the bonds at a 10% discount and still earn interest based on the $100.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/#tab-signup)
    

Original Issue Discount Debt (OID) Tutorial

**What is Original Issue Discount Debt (OID)?**
-----------------------------------------------

> **Original Issue Discount Definition:** Original Issue Discount refers to when a company issues Debt at _a discount to par value_. For example, a bond is worth $100 (the “face value” that the company pays interest on), but the company issues it for $90, which lets investors buy the bonds at a 10% discount and still earn interest based on the $100.

A company might do this, or have to do this, because:

**1) The bond’s coupon rate (interest rate) is below the rates of other, similar bonds**, and the company needs to incentivize investors to buy it even though the investors could earn higher interest elsewhere. In other words, it’s a way to boost the [bond yield](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
 or [Yield to Maturity](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
.

**2) Investors have doubts about the company’s credit quality** and ability to eventually repay the bond upon maturity (or to refinance and replace it with another bond).

When a company issues a bond at a discount to par value, **the company amortizes this discount on the financial statements** and increases the Book Value of Debt on the Balance Sheet until it reaches Par Value upon maturity.

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

[Simple Example of Original Issue Discount (OID) on the Financial Statements (XL)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Original-Issue-Discount.xlsx)

[Original Issue Discount (OID): What It Means and How It Works on the Financial Statements (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Original-Issue-Discount-Slides.pdf)

### **Video Table of Contents:**

**0:51:** The Short, Simple Answer

**4:04:** The Longer Answer – OID on Debt with Principal Repayments

**10:28:** Recap and Summary

**Walkthrough of Original Issue Discount (OID) Amortization**
-------------------------------------------------------------

In the example above, for Debt with a Face Value of $100, a 10% Coupon Rate (i.e., a fixed interest rate of 10%), a 5-year maturity, no principal repayments until maturity, and an Original Issue Discount of $10:

**Cash Interest per Year** = $100 \* 10% = $10 (based on Face Value \* Coupon Rate)

**OID Amortization** = $10 / 5 = $2 (based on Original Issue Discount / Maturity)

On the Balance Sheet, the company initially records Debt of $90 (its Book Value, which equals Face Value – Original Issue Discount), and it increases this number by $2 per year as the OID amortizes.

The Face Value of the Debt remains the same, at $100, **because discounts, premiums, and issuance fees never affect the Face Value of Debt.**

The company still pays Interest based on this $100 Face Value, so the Cash Interest stays the same each year because the Face Value and Coupon Rate are both fixed.

On the [Income Statement](https://breakingintowallstreet.com/kb/accounting/income-statement/)
, both the Interest Expense and Amortization of OID appear under the “Interest Expense” category ($12 in total), which reduces Pre-Tax Income, Taxes, and Net Income.

Here it is in Excel:

![Original Issue Discount - Simple Example on the Income Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20952%20814'%3E%3C/svg%3E "Original Issue Discount - Simple Example on the Income Statement")

On the Cash Flow Statement, Net Income is slightly lower as a result of the Amortization of OID, but since it is a non-cash expense, similar to Depreciation, we add it back in Cash Flow from Operations:

![OID - Cash Flow Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20247'%3E%3C/svg%3E "OID - Cash Flow Statement")

If this company had issued the Debt at a Book Value of $100 – no OID – rather than $90 – here’s how Free Cash Flow would have changed:

![OID - Cash Flow Statement with Discount Included](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20831%2093'%3E%3C/svg%3E "OID - Cash Flow Statement with Discount Included")

**More Advanced Walkthrough: Original Issue Discount with Debt Principal Repayments**
-------------------------------------------------------------------------------------

 If there are Mandatory or Optional Repayments on the Debt, you must amortize the OID more rapidly, which is slightly more complicated to model.

Companies call this “Extra Amortization” something like “Loss on Unamortized OID on Repayment,” and it’s based on % Debt Principal repaid in the current year \* OID balance after OID Amortization in the current year.

So, for example, if we assume the following:

**Beginning OID Balance:** $10

**OID Amortization:** $2

**Principal Repayment:** $20

Then the “Loss on Unamortized OID on Repayment” will be: ($20 / $100) \* $8 = 20% \* $8 = $1.6.

Here’s what it looks like in Excel if we assume the same OID Discount of $10, Annual Amortization of 20%, a 5-year maturity, and a Fixed Coupon Rate of 10%:

![Original Issue Discount with Debt Principal Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20602'%3E%3C/svg%3E "Original Issue Discount with Debt Principal Repayments")

The Amortization of Original Issue Discount itself also changes in this scenario.

To calculate it, you take the minimum between the OID Beginning Balance and OID Beginning Balance / Years Remaining in Amortization Period:

![OID Calculations with Debt Principal Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20843%20407'%3E%3C/svg%3E)

So, with OID of $10 and a 5-year period, this will initially be $10 / 5 = $2. But it will fall to less than $2 by the end because the OID Balance and OID Amortization Period keep decreasing.

As a result, the OID Balance itself decreases by a total of $3.6, then $2.8, then $2.0, then $1.2, and then $0.4 in the final year – not the constant changes we saw before.

On the financial statements, the “Loss on Unamortized OID on Repayment” counts as another expense on the Income Statement.

Cash Interest, OID Amortization, and the Loss on Unamortized OID on Repayment all reduce the company’s Pre-Tax Income, Taxes, and Net Income:

![Original Issue Discount on the Income Statement with Debt Principal Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20303'%3E%3C/svg%3E "Original Issue Discount on the Income Statement with Debt Principal Repayments")

On the Cash Flow Statement, Net Income is lower, and you add back the Amortization of OID and the Loss on Unamortized OID on Repayment since they’re both non-cash expenses:

![OID on the Cash Flow Statement with Debt Principal Repayments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20232'%3E%3C/svg%3E "OID on the Cash Flow Statement with Debt Principal Repayments")

These items **boost** the company’s [Free Cash Flow](https://breakingintowallstreet.com/kb/financial-statement-analysis/free-cash-flow-example/)
 because they’re non-cash items that reduce the company’s taxes, similar to Depreciation.

**Advanced Note:** In reality, these items may not _actually_ boost FCF with everything factored in because they may not be deductible for cash-tax purposes.

In that case, there will be a negative adjusting line item for Deferred Taxes that reduces the company’s FCF and eliminates the tax savings from these items shown on the Income Statement.

However, this is an advanced point that we don’t recommend bringing up in an interview context unless you want to go down the “rabbit hole” of tax-related questions.

Does Original Issue Discount (OID) Truly Matter?
------------------------------------------------

In most cases, no, not really.

Most Debt is **not** issued at a huge discount to par value; the 1-3% range is typical in normal markets.

The company may save a **tiny** amount on taxes as a result, especially in countries with relatively low corporate tax rates (15% – 25%) …and it takes **_a lot_** of extra work to set up these OID calculations, especially if there are many tranches of Debt.

It does not factor into financial statement analysis or metrics such as [Return on Invested Capital](https://breakingintowallstreet.com/kb/financial-statement-analysis/roic-return-on-invested-capital/)
, and it does not contribute to items like the [Change in Working Capital](https://breakingintowallstreet.com/kb/financial-statement-analysis/change-in-working-capital/)
.

So, be familiar with OID, but don’t obsess over it. You could easily simplify or ignore it in case studies and modeling tests and be fine.

Recap and Summary
-----------------

Here’s the TL;DR version of everything covered above:

**Original Issue Discount (OID):** This occurs when the Face Value of a bond is $100, but the company issues it for some amount less than $100, such as $90, because its Coupon Rate is lower than market rates on similar bonds, or because there are doubts about the company’s credit quality.

**No Principal Repayments:** Amortize the OID / # Years to Maturity each year. Show this expense on the Income Statement under Interest Expense, and add it back on the Cash Flow Statement as a non-cash expense. The Book Value of Debt on the Balance Sheet will increase by this amount each year, but the company still pays Cash Interest each year based on the $100 Face Value of the bond.

**Principal Repayments:** Accelerate the OID Amortization based on (OID _after_ Normal Annual Amortization) \* % Principal Repayment in the Year, and record this item as a “Loss on Unamortized OID on Repayment.” The normal OID Amortization starts higher and declines each year, so the OID Balance declines by less and less each year until it reaches 0. You add back both the OID Amortization and the Loss on Unamortized OID on Repayment as non-cash adjustments on the CFS. The Face Value changes based only on the Principal Repayments each year.

**Impact:** OID at modest levels barely makes an impact on models and valuations. It’s good to know, but it won’t make a “no” investment recommendation turn into a “yes” in most cases. Exceptions apply for distressed companies and others that issue Debt at very high discounts.

Finally, if you can’t fall asleep and you need the equivalent of a sleeping pill, check out the [IRS guide to OID instruments for more details](https://www.irs.gov/publications/p1212)
.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Original Issue Discount (OID): What It Means and How It Works on the Financial Statements (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Original-Issue-Discount-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Example of Original Issue Discount (OID) on the Financial Statements (XLS)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Original-Issue-Discount.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&mini=true)
[Email](mailto:?subject=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[](https://www.linkedin.com/shareArticle?title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&mini=true)
[](mailto:?subject=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[](https://api.whatsapp.com/send?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Copy](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/#)
[Email](mailto:?subject=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&t=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/11/19075616/kb-original-issue-discount-debt.jpg&description=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[Print](https://breakingintowallstreet.com/kb/debt-equity/original-issue-discount-debt/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[SMS](sms:?&body=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[X](https://x.com/intent/tweet?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdebt-equity%2Foriginal-issue-discount-debt%2F&title=Original%20Issue%20Discount%20Debt%20%28OID%29%20Tutorial%20%2812%3A43%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/11/19075616/kb-original-issue-discount-debt.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand