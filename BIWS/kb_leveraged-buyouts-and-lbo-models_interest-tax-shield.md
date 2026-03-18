# Interest Tax Shield in Valuations and LBO Models

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield

---

The Interest Tax Shield: Valuations, LBO Models, and More
=========================================================

In corporate finance, the “interest tax shield” refers to the tax reduction a company gets by issuing Debt and paying Interest on that Debt; it is roughly equal to the Interest Expense \* Tax Rate, but it may be reduced or limited in certain regions based on the company’s EBIT, EBITDA, or other attributes.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#tab-signup)
    

The Interest Tax Shield: Valuations, LBO Models, and More

> **Interest Tax Shield Definition:** In corporate finance, the “interest tax shield” refers to the tax reduction a company gets by issuing Debt and paying Interest on that Debt; it is roughly equal to the Interest Expense \* Tax Rate, but it may be reduced or limited in certain regions based on the company’s EBIT, EBITDA, or other attributes.

For example, if a company has $1,000 of Debt at a 10% Interest Rate, it pays $100 in Interest Expense per year on the Debt.

Since the interest is tax-deductible, its tax burden is reduced by $100 \* Tax Rate.

In most developed countries, the corporate tax rate is between 20% and 30%, so at a 25% rate, this is a $25 reduction.

As a result, the company spends a “net amount” of $75 rather than $100 due to this tax deduction.

Its after-tax profits ([Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/)
) are still down, but they’re down by $75 rather than $100.

The interest tax shield should be an organic part of any [LBO model](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/what-is-an-lbo-model/)
 and does not require a separate schedule in simple cases.

You can see it on the [Income Statement](https://breakingintowallstreet.com/kb/accounting/income-statement/)
 in the Pre-Tax Income and Net Income area:

![Income Statement - Interest Tax Shield](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2025/04/23100636/01-IS-Interest-Tax-Shield.jpg "Income Statement - Interest Tax Shield")

In more complex cases, the Interest Expense may not be fully deductible (see the full walkthrough below).

So, if we assume that it’s only deductible up to a certain percentage of [Operating Income (EBIT)](https://breakingintowallstreet.com/kb/accounting/ebit-operating-income/)
, the [IRR](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
 (annualized returns) in the deal decreases.

However, since the effect size is small, the IRR remains in a narrow range regardless of the limit:

![Interest Expense - Tax Deduction Limits](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2025/04/23100718/02-Interest-Tax-Deduction-Limits.jpg "Interest Expense - Tax Deduction Limits")

In a DCF-based valuation, the interest tax shield is reflected in the [WACC calculation](https://mergersandinquisitions.com/wacc-formula/)
 because you multiply the company’s Pre-Tax Cost of Debt by (1 – Tax Rate) for use in the standard formula:

![The Tax Shield in the WACC Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20654'%3E%3C/svg%3E "The Tax Shield in the WACC Calculations")

The Interest paid on Debt is tax-deductible, which makes Debt even cheaper than Equity.

Note, however, that the interest tax shield is only part of the explanation; [Debt is cheaper than Equity](https://breakingintowallstreet.com/kb/debt-equity/debt-vs-equity-analysis/)
 mainly because its risks and potential returns are lower.

### **Files & Resources:**

*   [Simple LBO Model – Interest Tax Shield Schedule (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-27-Interest-Tax-Shield-LBO-Model.xlsx)
    
*   [Levered and Unlevered FCF Examples with Tax Calculations (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-28-Levered-Free-Cash-Flow-Simple-DCF.xlsx)
    
*   [Interest Tax Shield Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-27-Interest-Tax-Shield-Slides.pdf)
    

**The Interest Tax Shield in Valuation and DCF Analysis**
---------------------------------------------------------

The main point here was stated above: Always multiply the Pre-Tax Cost of Debt by (1 – Tax Rate) to get the After-Tax Cost of Debt for use in the WACC calculation.

Normally, you estimate a company’s Cost of Debt by calculating the [Yield to Maturity (YTM)](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
 on its existing bonds, but you could also take the [Risk-Free Rate](https://breakingintowallstreet.com/kb/finance/risk-free-rate/)
 and add a Credit Default Spread corresponding to the company’s credit rating.

You could even divide the company’s Interest Expense by its average Debt balance, but this is not ideal since it doesn’t reflect current market rates.

**If you use Unlevered FCF in a traditional DCF, you should NOT factor in any interest tax shield because UFCF is capital structure-neutral. The taxes must be based on the company’s EBIT and ignore the Interest Expense.**

In other words, the Taxes the company pays in the [UFCF calculations](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/)
 stay the same regardless of whether it pays 5%, 10%, or 15% interest on its Debt, and regardless of any deduction limits:

![Unlevered FCF - Tax Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201449%20709'%3E%3C/svg%3E "Unlevered FCF - Tax Calculation")

UFCF is capital structure-neutral, so it is not affected by the company’s Debt vs. Equity mix or the specific terms or interest rates on its capital.

However, the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
 used in a [DCF](https://mergersandinquisitions.com/dcf-model/)
 – whether [the Cost of Equity or WACC](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/wacc-formula/)
 – is _never_ capital structure-neutral.

It changes as the company’s Debt vs. Equity mix, interest rates, and other terms change.

Therefore, the Interest Tax Shield affect the output even in an Unlevered DCF because of its impact on WACC.

It’s just that it makes a much bigger impact in a [Levered DCF](https://breakingintowallstreet.com/kb/valuation/levered-free-cash-flow/)
 since _both_ the Free Cash Flow _and_ the Discount Rate change there.

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

**The Interest Tax Shield in LBO Models and Deduction Limits**
--------------------------------------------------------------

In a simple LBO model, you do not need to do anything “special” or “different” to account for the Interest Tax Shield.

If you have set up your model properly, with standard Pre-Tax Income and Net Income calculations, it happens organically:

![Income Statement - Interest Tax Shield](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2025/04/23100636/01-IS-Interest-Tax-Shield.jpg "Income Statement - Interest Tax Shield")

However, some countries **limit** the amount of Interest Expense a company can deduct.

For example, in the Tax Cuts and Jobs Act (TCJA) passed in the U.S. in 2017, companies could initially deduct Interest Expense only up to 30% \* EBITDA.

After 2022, this rule shifted to 30% \* EBIT, which is much less favorable since [EBIT is lower than EBITDA](https://breakingintowallstreet.com/kb/valuation/ebit-vs-ebitda/)
.

It’s a lower deduction limit, which means reduced tax savings from the Interest Expense.

Some case studies ask candidates to account for these limits, but they’re uncommon in simpler tests, such as [60-minute LBO modeling tests](https://mergersandinquisitions.com/lbo-modeling-test/)
.

As an example, here’s what happens in this [simple LBO model](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/simple-lbo-model-excel/)
 if we allow for Interest Expense deductions up to different percentages of EBIT or EBITDA:

![Interest Expense - Tax Deduction Limits](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201809%20664'%3E%3C/svg%3E "Interest Expense - Tax Deduction Limits")

**Factors That Matter More Than the Interest Tax Shield in LBO Models**
-----------------------------------------------------------------------

Virtually every other assumption matters more than the interest tax shield: The purchase price, the exit multiple, the % debt used, the revenue growth rates, and the operating margins.

The interest rate on Debt, such as 5% or 10%, also makes a bigger impact, though it is still less important than the abovementioned assumptions.

The Interest Tax Shield affects only the Cash Generated and Debt Repaid during the holding period of an LBO, not the Exit Multiple, Exit EBITDA, or EBITDA Growth.

However, in most LBO models, the Cash Generated and Debt Repaid make a small impact next to these other factors:

![LBO Exit Proceeds and Drivers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201790%20467'%3E%3C/svg%3E "LBO Exit Proceeds and Drivers")

Cheaper effective financing improves deal outcomes but is far less significant than the core business growing at different rates.

The Interest Tax Shield makes a larger impact when interest rates are much higher, such as 14% rather than 6%:

![LBO Model - IRR Sensitivities](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201262%20565'%3E%3C/svg%3E "LBO Model - IRR Sensitivities")

However, if a company pays a 14% interest rate on its Debt, it is likely a _very risky company_ with inconsistent cash flows at a higher risk of financial distress.

A company in this category is unlikely to generate much Cash or repay much Debt in the holding period of an LBO model.

Therefore, this example is a bit artificial because this scenario would probably not happen in real life.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Interest Tax Shield Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-27-Interest-Tax-Shield-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple LBO Model - Interest Tax Shield Schedule (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/109-27-Interest-Tax-Shield-LBO-Model.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Levered and Unlevered FCF Examples with Tax Calculations (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/107-28-Levered-Free-Cash-Flow-Simple-DCF.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&mini=true)
[Email](mailto:?subject=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&mini=true)
[](mailto:?subject=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[](https://api.whatsapp.com/send?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#)
[Email](mailto:?subject=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&t=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/interest-tax-shield/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[SMS](sms:?&body=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[X](https://x.com/intent/tweet?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Finterest-tax-shield%2F&title=The%20Interest%20Tax%20Shield%3A%20Valuations%2C%20LBO%20Models%2C%20and%20More&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand