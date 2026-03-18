# PIK Interest in LBO Models: Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest

---

Paid-In-Kind (PIK) Interest: Full Tutorial for LBO Models
=========================================================

Unlike normal Interest on Debt, PIK Interest (PIK = “Paid-in-Kind”) accrues to the loan principal rather than being paid in cash, which results in an increasing loan balance and higher interest payments in the future.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#tab-signup)
    

Paid-In-Kind (PIK) Interest: Full Tutorial for LBO Models

> **PIK Interest Definition:** Unlike normal Interest on Debt, PIK Interest (PIK = “Paid-in-Kind”) _accrues to the loan principal_ rather than being paid in cash, which results in an increasing loan balance and higher interest payments in the future.

PIK Interest is most common on “junior Debt” instruments in [leveraged buyouts](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/what-is-an-lbo-model/)
, such as Subordinated Notes, Mezzanine, and Preferred Stock.

These instruments are riskier than Senior Debt (Bank Loans and Revolvers), and, therefore, have higher interest rates and may have some type of equity option as well (please see our [Debt Schedule tutorial](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
 for more).

PIK Interest essentially “kicks the can down the road” by reducing the company’s _cash interest burden but ballooning its future Debt balance_ – so that more needs to be repaid upon maturity or exit.

Therefore, it is **MOST** appropriate for riskier companies with “spotty” cash flows, as it allows them to carry more Debt than they would ordinarily be able to do with cash interest.

PIK Interest on Debt changes the [money-on-money multiple](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
 but **NOT** the [internal rate of return (IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
 for the lenders, assuming full repayment.

This is because the IRR function assumes _full reinvestment of the proceeds at the IRR_, so an 8% compounding balance is equivalent to earning 8% in cash each year on the initial investment (for example).

The private equity firm’s IRR and multiples do not change much due to PIK Interest, but they may **decrease slightly** because of the “ballooning effect,” which results in a higher Debt balance that must be repaid upon exit.

You can use the Excel file below to try different scenarios and see the impact of PIK Interest:

### **Files & Resources:**

[Simple LBO Model – PIK Interest (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-23-PIK-Interest-LBO.xlsx)

[PIK Interest in LBO Models – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-23-PIK-Interest-Slides.pdf)

### **Video Table of Contents:**

**0:00:** Introduction

**4:15:** Part 1: PIK vs. Cash Interest in an LBO

**7:39:** Part 2: The Returns to Lenders

**9:07:** Part 3: Debt Principal Repayments and PIK

**10:35:** Part 4: PIK Interest and Taxes

**12:12:** Recap and Summary

**PIK Interest vs. Cash Interest in a Leveraged Buyout Model**
--------------------------------------------------------------

Suppose you have a “standard” leveraged buyout model for a deal done at 12x [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/)
 with 5x Debt / EBITDA and an 8% cash interest rate on the Debt.

We’ll look at the initial assumptions here and then modify them to use 100% PIK Interest so you can understand the changes:

![Standard LBO Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201204%20822'%3E%3C/svg%3E "Standard LBO Model")

These are standard assumptions for a [cash-free, debt-free](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-free-debt-free-basis/)
 leveraged buyout.

If we now assume **100% PIK Interest**, we need to make the following changes:

### **Step 1: Still Record Interest on the Income Statement, But Note That It Is PIK or Non-Cash**

This interest is still based on the Interest Rate \* Debt Balance; we use the beginning Debt balance in each period to avoid [circular references](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
:

![PIK Interest on the Income Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201210%20940'%3E%3C/svg%3E "PIK Interest on the Income Statement")

### **Step 2: Add Back This PIK Interest on the Cash Flow Statement**

Like Depreciation, PIK Interest is a non-cash expense.

So, just like with Depreciation, we reverse it on the [Cash Flow Statement](https://breakingintowallstreet.com/kb/accounting/cash-flow-statement/)
 or in the cash flow projections:

![PIK Interest Addback on the Cash Flow Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201215%20688'%3E%3C/svg%3E "PIK Interest Addback on the Cash Flow Statement")

### **Step 3: Make This PIK Interest Increase the Debt Balance in Each Period**

To do this, we can modify the Debt formula so that it **adds** the PIK Interest in the period rather than just subtracting the Debt principal repayments:

![PIK Interest Impact on Debt Balance](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201207%20558'%3E%3C/svg%3E "PIK Interest Impact on Debt Balance")

### **Step 4: Make Sure All the Other Formulas Reflect These Changes**

For example, it’s worth checking the final Debt balance in the exit calculations to ensure it has grown due to the PIK Interest.

You should also ensure that the PIK Interest counts as a tax deduction and appropriately reduces Pre-Tax Income and [Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/)
.

Finally, the PIK Interest Expense should **grow over time** because the Debt balance keeps increasing, and there are no principal repayments in this model (so far).

**How Does PIK Interest Affect the Returns?**
---------------------------------------------

In this case, it **reduces the IRR and multiple for the PE firm** because it increases the Debt balance upon exit:

![Cash vs. PIK Interest and Effect on Equity IRR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201148%20618'%3E%3C/svg%3E "Cash vs. PIK Interest and Effect on Equity IRR")

Cash flows are higher because there is no cash interest, **but that doesn’t help because the cash flows are not _distributed_ during the holding period**.

Instead, the improved cash flows accumulate to the Cash balance, but **the final Debt balance increases by more than the final Cash balance**.

As a result, the Net Debt upon exit is higher, which reduces the equity proceeds, the IRR, and the multiple.

**PIK Interest and Its Impact on the Returns to Lenders**
---------------------------------------------------------

Just as the equity investors (the private equity firm) earn a multiple and IRR in a leveraged buyout, so do **the lenders** (the Debt investors).

With PIK Interest rather than Cash Interest, **the lenders’** **multiple changes, but the IRR does not** because of the “reinvest all proceeds _at_ the overall IRR” assumption.

In other words, earning 8% cash interest per year on the initial balance is the same as earning no interest but getting back the Initial Balance \* (1 + 8%) ^ 5 at the end of 5 years – according to the IRR function.

Here’s a comparison of the returns with Cash Interest vs. PIK interest:

![PIK Interest and Returns to Lenders](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201196%20658'%3E%3C/svg%3E "PIK Interest and Returns to Lenders")

**Debt Principal Repayments and PIK Interest**
----------------------------------------------

Allowing for Debt principal repayments **mostly helps the PE firm** because instead of letting the Cash accumulate, the company _uses its Cash_ to do something useful: repay Debt.

However, this is true in all [LBO models](https://mergersandinquisitions.com/lbo-modeling-test/)
 and [Debt Schedules](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/debt-schedule/)
 and is not specifically related to the PIK Interest.

If we modify the model to allow Debt principal repayments, the equity IRR and multiple change as follows:

![Debt Principal Repayments and Impact on Returns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201202%20838'%3E%3C/svg%3E "Debt Principal Repayments and Impact on Returns")

For the **lenders**, once again, the multiple changes – it **decreases** with early principal repayments – but the IRR stays the same because of the reinvestment assumption.

**PIK Interest and Taxes**
--------------------------

In _most cases_, PIK Interest is tax-deductible, just like the Cash Interest Expense.

That is why we show it as a deduction to calculate the Pre-Tax Income above and why the Deferred Tax line item in the cash flow projections is $0.

However, there may be **exceptions** when the PIK Interest is attached to an “equity-like security,” such as [convertible preferred stock](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
 or [convertible notes for a startup](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
.

These rules vary based on your region and the tax treatment of different security types there, so this point is case-by-case.

To assume that PIK Interest is **not** tax-deductible, you can add a Deferred Tax line in the cash flow projections and set it equal to the following in each period:

\= – PIK Interest \* Tax Rate

Here’s an example in this simple model:

![PIK Interest and Tax Effects](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201198%20679'%3E%3C/svg%3E "PIK Interest and Tax Effects")

**PIK Interest: Conclusions**
-----------------------------

In short, PIK Interest is not a “make or break” topic in deals or [financial models](https://mergersandinquisitions.com/financial-modeling/)
; it affects the output, but not enough to shift an investment recommendation from “no” to “yes” (or vice versa).

You should be familiar with this concept for [LBO modeling tests](https://mergersandinquisitions.com/lbo-modeling-test/)
, [private equity case studies](https://mergersandinquisitions.com/private-equity-case-study/)
, and credit case studies, but it’s much less important than understanding how to model Debt repayments, calculate the IRR, and other basic topics.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) PIK Interest in LBO Models - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-23-PIK-Interest-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple LBO Model - PIK Interest (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-23-PIK-Interest-LBO.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&mini=true)
[Email](mailto:?subject=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[](https://www.linkedin.com/shareArticle?title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&mini=true)
[](mailto:?subject=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[](https://api.whatsapp.com/send?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#)
[Email](mailto:?subject=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&t=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[SMS](sms:?&body=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[X](https://x.com/intent/tweet?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fpik-interest%2F&title=Paid-In-Kind%20%28PIK%29%20Interest%3A%20Full%20Tutorial%20for%20LBO%20Models&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand