# Convertible Notes for Startups: Full Guide + Excel File

**Source:** https://breakingintowallstreet.com/kb/venture-capital/convertible-notes

---

Convertible Notes for Startups Explained: Definition, Calculations, Excel Examples, and Comparison to SAFE Notes
================================================================================================================

With Convertible Notes, startup investors contribute capital but do not receive direct ownership in the startup right away; instead, they earn interest and receive their shares later based on a conversion of the loan principal into equity when the company raises a “priced round” based on a specific valuation.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#tab-signup)
    

Convertible Notes for Startups Explained: Definition, Calculations, Excel Examples, and Comparison to SAFE Notes

> **Convertible Notes Definition:** With Convertible Notes, startup investors contribute capital but do not receive direct ownership in the startup right away; instead, they earn interest and receive their shares later based on a conversion of the loan principal into equity when the company raises a “priced round” based on a specific valuation.

Just like SAFE Notes, in theory, Convertible Notes are **faster and cheaper** than traditional equity rounds, such as Seed or Series A funding linked to agreed-upon valuations. They are quite different from [Convertible Preferred Stock](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/convertible-preferred-stock/)
, which is typically used by larger public companies.

Valuation discussions and share grants are deferred until these priced rounds take place – though other conversion/trigger mechanisms may be defined for Convertible Notes.

Unlike [SAFE Notes](https://breakingintowallstreet.com/kb/venture-capital/safe-notes/)
, Convertible Notes are **clearly Debt** and have a well-defined space in the seniority and capital structure.

As a result, they avoid some of the problems that SAFE Notes create and tend to be more favorable for **investors**.

For startups, however, Convertible Notes potentially create **more dilution** because the interest often accrues to the loan principal – meaning that the investors get more shares upon conversion due to this higher principal:

![Convertible Note Dilution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201157%20634'%3E%3C/svg%3E "Convertible Note Dilution")

You can get our simple Convertible Notes Excel model and presentation and read this entire tutorial in written format below:

[Convertible Notes vs. SAFE Notes – Excel Model (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Convertible-Notes/Convertible-Notes-vs-Safe-Notes.xlsx)

[Convertible Notes – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Convertible-Notes/Convertible-Notes-Slides.pdf)

### **Video Table of Contents:**

**5:19:** Part 1: Convertible Notes in a Seed Round

**6:01:** Part 2: Conversions in the Series A with an Options Pool

**10:47:** Dollars Invested Method

**11:41:** Part 3: Side-by-Side: Convertible Note vs. SAFE

**12:35:** Part 4: Should a Startup Use Either One of These?

**13:32:** Recap and Summary

**Part 1: Convertible Notes in a Seed Round**
---------------------------------------------

If a startup raises capital via Convertible Notes in a Seed Round, **nothing changes** in the [capitalization table (“cap table”)](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
 because the investors do not receive direct ownership.

So, if a Seed Investor invests $2 million via Convertible Notes, and the co-founders own 90% with the employees owning 10%, the ownership percentages remain 90% and 10% before and after the deal:

![Convertible Note Terms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201336%20770'%3E%3C/svg%3E "Convertible Note Terms")

There are terms associated with these Convertible Notes – namely the **valuation cap** and **conversion discount** – but these only take effect in the next **priced round** when the startup raises capital at a specific valuation.

_Unlike_ the SAFE Notes, an **interest rate and maturity date** are also attached to these Convertible Notes.

Here, we assume 2 years between the Seed Round and Series A round, but in real life, you would model this based on the dates of the maturity and the next priced round.

**Part 2: Convertible Note Conversions in a Series A Round (Valuation Caps and Conversion Discounts) with an Options Pool**
---------------------------------------------------------------------------------------------------------------------------

We’ll assume here that this startup plans to raise **$5 million at a $10 million pre-money valuation.**

That means the post-money valuation is $5 + $10 = $15 million, so the VC firm _expects_ to own ~33% of the company:

![Series A Ownership with a Convertible Note](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201357%20202'%3E%3C/svg%3E "Series A Ownership with a Convertible Note")

**But in reality, the VC firm investing $5 million in this Series A round will own less than 33% because of the shares that go to the Convertible Note investors**.

Here’s the step-by-step process to set up the cap table:

### **Step 1: Calculate the “Price per Share” in the Series A Round**

This is based on the pre-money valuation divided by the Pre-Money Share Count (the shares that existed _before_ the Series A):

![Series A Share Price](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201209%20338'%3E%3C/svg%3E "Series A Share Price")

It’s $7.50 here, which means the Series A investors pay $7.50 for each new share they purchase in this round.

### **Step 2: Determine the “Price per Share” for the Convertible Note Investors**

This is where the **conversion discount**, **valuation cap**, and **accrued interest** come into play.

First, you must calculate the **Convertible Note principal** factoring in the 10% accrued interest over 2 years, which equals $2.42 million here:

![Convertible Note Accrued Interest Effect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201304%20584'%3E%3C/svg%3E "Convertible Note Accrued Interest Effect")

If there’s a **conversion discount**, the Convertible Note investors get their shares at a discount to the $7.50 the Series A investors pay (a 20% discount in this case, which means $6.00 per share).

If there’s a **valuation cap**, the Convertible Note investors get their shares at a price equal to the Valuation Cap / Pre-Money Shares, or $10 million / 1.333 million = $7.50 here.

### **Step 3: Grant Shares to the New Investors in the Round**

In a case like this with **both** a discount and a cap, we take the _best possible share price_ for the Convertible Note investors and use that to calculate the shares granted:

![Shares from the Convertible Note Conversion](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201620%20460'%3E%3C/svg%3E "Shares from the Convertible Note Conversion")

The Series A investors get their 666,667 new shares from the $7.50 per share they pay.

The **valuations** are based on the $7.50 Series A share price times each group’s share count.

![Venture Capital & Growth Equity Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Model and Value Startups, Understand Cap Tables, and Prepare for VC Interviews

*   #### Evaluate companies and deals like a pro
    
    You’ll understand cap tables, startup/growth valuations, and exits
    
*   #### Master financial modeling
    
    You’ll build forecasts and analyze metrics for tech and biotech startups
    
*   #### Complete 9 case studies
    
    You’ll learn the numbers and how to make investment recommendations
    

[Full Details](https://breakingintowallstreet.com/venture-capital-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Venture-Capital-Modeling-Course-Outline.pdf)

### **Step 4: Build in Dilution from the Options Pool**

The **employee** **options pool** is usually **upsized or re-sized** in a priced round, which creates additional complications because now the employees effectively get “free shares.”

To calculate the impact, start with the **total non-option shares** after the Convertible Note conversions and Series A funding, which in this case are 1.070 million + 1.333 million = 2.270 million.

Then, divide this by **1 – Options Pool %**, where “Options Pool %” is the total percentage of the company shares that employees should own:

![Options Pool Post-Conversion](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201270%20220'%3E%3C/svg%3E "Options Pool Post-Conversion")

The employees should have 20% \* 2,837,500 = 567,500 shares after this round, and they already have 133,333 options.

Therefore, they receive 567,500 – 133,333 = 434,167 additional options in this round, which count as “free shares.”

This further dilutes the Series A investors down to **~24% ownership:**

![Series A Ownership Dilution After the Convertible Note Shares](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201314%20492'%3E%3C/svg%3E "Series A Ownership Dilution After the Convertible Note Shares")

### **Step 5: Link in the Post-Series A Cap Table and Calculate the Ownership Percentages**

Based on these new share counts, we can calculate each group’s ownership and share value (shown above).

The Series A investors own **less than 33%** because the Seed Investors got their shares “for free” in this round based on their previous investment.

Therefore, the “true” Pre-Money Valuation was higher.

Because of this issue, people have developed different ways to determine the number of shares that Convertible Notes convert into.

For example, they might use the “Dollars Invested” method, a weighted average of the share prices, or another method to find a middle ground between the investor groups.

You can see an example of the “Dollars Invested” method below:

![Dollars Invested Method for the Convertible Note Shares](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201150%20722'%3E%3C/svg%3E "Dollars Invested Method for the Convertible Note Shares")

Effectively, it produces a **lower “true” pre-money valuation** by subtracting some of the Convertible Note.

As a result, both the Convertible Note and Series A investors end up with higher ownership and the Co-Founders get more heavily diluted:

![Ownership with the Dollars Invested Method](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201424%20552'%3E%3C/svg%3E "Ownership with the Dollars Invested Method")

**Part 3: Convertible Notes and SAFE Notes Side-by-Side**
---------------------------------------------------------

The most obvious difference is that Convertible Notes create more dilution due to the accrued interest:

![Dilution from the Convertible Note vs. SAFE Note](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201411%20341'%3E%3C/svg%3E "Dilution from the Convertible Note vs. SAFE Note")

But this doesn’t tell the whole story, as the Convertible Notes also have advantages in a shutdown or company liquidation.

Their place in the capital structure is very clear (they are senior to the Preferred and Common Equity Investors), and they have the first claim to the company’s assets.

Therefore, while Convertible Note investors are unlikely to recover much in a liquidation, they _might_ recover some of their principal, while the SAFE Note and priced equity investors would get nothing.

Also, Convertible Notes, similar to [Venture Debt](https://breakingintowallstreet.com/kb/ma-and-merger-models/divestitures/)
, can sometimes act as “mini-bridge loans” between priced rounds, which is rare for SAFE Notes.

Here’s a full comparison table:

![Convertible Note vs. SAFE Note Comparison Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202422%201206'%3E%3C/svg%3E "Convertible Note vs. SAFE Note Comparison Table")

**Part 4: Are Convertible Notes or SAFE Notes _Ever_ Worth It?**
----------------------------------------------------------------

In short, **no**, not really.

Both instruments had advantages in past years (SAFE Notes were introduced in 2013), but most of these advantages have diminished over time.

Priced equity rounds have become simpler and cheaper to execute, and they don’t create messy cap tables, unclear valuations, or accrued interest with higher dilution in the same way these “deferred” instruments do.

**Convertible Notes** are more favorable to investors due to the maturity and full repayment, varied conversion triggers, accrued interest, and seniority.

From the co-founders’ perspective, however, Convertible Notes usually mean more dilution and don’t necessarily provide a big benefit unless the company shuts down.

So, priced equity rounds are still superior in most cases, and if a startup needs a bridge loan, Venture Debt could work quite well.

Convertible Notes and SAFE Notes should be in the “Interesting and good to know, but not necessarily a top priority” category when you’re considering startup funding options.

[Sign up to BIWS VC & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Convertible Notes – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Convertible-Notes/Convertible-Notes-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Convertible Notes vs. SAFE Notes – Excel Model (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Convertible-Notes/Convertible-Notes-vs-Safe-Notes.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

Master cap tables, exit analysis, flow of funds, startup valuation, and growth-stage modeling - and win job offers at venture capital and growth equity firms.

[Learn More](https://breakingintowallstreet.com/venture-capital-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[VC Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/FrakNsSE)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with cap tables, exit analysis, startup valuation, and other VC-related topics. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/FrakNsSE)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&mini=true)
[Email](mailto:?subject=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)

#### Master Cap Tables and Startup Modeling

Learn VC and growth equity financial modeling via 5 short case studies and 4 extended case studies on everything from AI to SaaS to biotech.

[LEARN MORE](https://breakingintowallstreet.com/venture-capital-modeling/)

[](https://x.com/intent/tweet?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[](https://www.linkedin.com/shareArticle?title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&mini=true)
[](mailto:?subject=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[](https://api.whatsapp.com/send?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Copy](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#)
[Email](mailto:?subject=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&t=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
[Pinterest](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#)
[Print](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[SMS](sms:?&body=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[X](https://x.com/intent/tweet?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fconvertible-notes%2F&title=Convertible%20Notes%20for%20Startups%20Explained%3A%20Definition%2C%20Calculations%2C%20Excel%20Examples%2C%20and%20Comparison%20to%20SAFE%20Notes&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand