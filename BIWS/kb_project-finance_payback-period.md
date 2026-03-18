# Payback Period in Project Finance, Biotech, and More

**Source:** https://breakingintowallstreet.com/kb/project-finance/payback-period

---

The Payback Period in Project Finance and Asset-Level Modeling: A More Objective Measure of Risk and Growth?
============================================================================================================

In finance, the “Payback Period” refers to the time required to recoup the cost of a development or acquisition with the cash flows from the asset; it is most useful in asset-level financial modeling, such as in fields like Project Finance, but it may be relevant in other contexts as well.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/project-finance/payback-period/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/project-finance/payback-period/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/project-finance/payback-period/#tab-signup)
    

The Payback Period in Project Finance and Asset-Level Modeling: A More Objective Measure of Risk and Growth?

> **Payback Period Definition:** In finance, the “Payback Period” refers to the time required to recoup the cost of a development or acquisition with the cash flows from the asset; it is most useful in asset-level financial modeling, such as in fields like Project Finance, but it may be relevant in other contexts as well.

![Payback Period Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201270%20173'%3E%3C/svg%3E "Payback Period Formula")

**Shorter Payback Periods** are better than longer Payback Periods because they mean that the investors earn back their initial funds more quickly, which reduces their risk.

**However, a shorter Payback Period does not necessarily mean they earn higher returns – in fact, it sometimes means the opposite! (see below)**

The Payback Period must also pass the “sniff test”: For example, no one would believe that the Payback Period on a medium-sized solar plant is 2 years because solar assets do not have high enough cash-flow yields for that math to work.

If an asset’s cash flows are **constant**, the Payback Period formula is simpler than the one above:

![Simple Payback Period Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20824%20166'%3E%3C/svg%3E "Simple Payback Period Formula")

For example, if you buy a property for $1,000, and it generates $100 in cash flow each year, the **Payback Period** is $1,000 / $100 = 10.0 years.

**This is very low for real estate** because a 10% yield is far above what most properties offer, so we might be skeptical of this estimate.

**Payback Periods are most useful for modeling assets that lack [Terminal Values](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
 or Exit Values, as investors need significant cash flows during the holding period to realize a solid return on investment.**

The Payback Period helps quantify the overall risk of “waiting and holding the asset.”

It also tells you something about the **growth potential** of the asset: If the cash flow grows more quickly, you might expect a shorter Payback Period.

You would not use the Payback Period as a key metric in a traditional [leveraged buyout model](https://mergersandinquisitions.com/lbo-modeling-test/)
 or a [DCF analysis of an entire company](https://mergersandinquisitions.com/dcf-model/)
 because **most of the value comes from the Exit Value or Terminal Value.**

However, you might use it as _a part_ of this model to analyze the effectiveness of the company’s growth strategy as it opens new stores or factories (for example).

### **Files & Resources:**

*   [Simple Payback Period Formulas in Project Finance (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-06/PF-06-Payback-Period.xlsm)
    
*   [Payback Period – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-06/PF-06-Payback-Period-Slides.pdf)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **0:43:** The Short Version
*   **5:17:** Part 1: Levered and Unlevered Payback Periods
*   **9:35:** Part 2: Payback Period vs. IRR and Multiples
*   **12:29:** Part 3: Biotech Payback Period Example
*   **15:14:** Recap and Summary

**Why Use the Payback Period Rather Than the IRR and NPV?**
-----------------------------------------------------------

The [Internal Rate of Return (IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
, [Net Present Value (NPV)](https://breakingintowallstreet.com/kb/finance/net-present-value/)
, and Payback Period are all common investment analyses, but they measure different things.

The **IRR** is a rough proxy for the “annualized rate of return” on an asset or investment.

The **NPV** tells you whether an investment is “worth” more than its upfront cost, i.e., whether the rate of return on it exceeds your targeted returns.

So, the IRR and NPV are more about **measuring returns**, while the Payback Period is more about **measuring risk and growth potential.**

The Payback Period is useful for the same reason a [SaaS metric](https://breakingintowallstreet.com/kb/venture-capital/saas-metrics/)
 like the Customer Acquisition Cost (CAC) Payback Period is useful: It eliminates the judgment calls around assumptions like the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
 and **makes it 100% about costs and cash flows.**

But that also means it’s arguably less useful for “real-world” investment decisions, as the [time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
 is always important there.

**The Payback Period in Project Finance: Simple Example**
---------------------------------------------------------

To demonstrate the Payback Period in Excel, we’ll walk through a simple example based on the [simplified Project Finance model for the acquisition of a solar plant](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-06/PF-06-Payback-Period.xlsm)
.

To set this up, you’ll need to track the **Upfront Investor Equity**, the **Unrecovered Equity** each year, the **Breakeven Point**, and the **Year Fraction** when the breakeven point is finally reached.

First, link in the Upfront Investor Equity, which might be the amount used to fund the project’s development or the Equity spent to acquire it.

Then, calculate the “Unrecovered Equity” in each period based on this Upfront Equity minus the cumulative Cash Flows to Equity so far:

![Unrecovered Equity in the Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20943%20232'%3E%3C/svg%3E "Unrecovered Equity in the Payback Period")

In each period, do a check to see if you’ve hit the “Breakeven Point,” which happens when the Unrecovered Equity goes from a positive number to 0:

![Breakeven Point in the Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201111%20232'%3E%3C/svg%3E "Breakeven Point in the Payback Period")

Then, calculate the “Year Fraction” when this Breakeven Point is reached.

You can do this by taking the cash flow in the year and dividing it by the Unrecovered Equity at the start of the year to estimate the **year** **fraction** required to recover the remaining Equity:

![Year Fraction in the Breakeven Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201083%20233'%3E%3C/svg%3E "Year Fraction in the Breakeven Period")

Finally, **count** the number of years required to reach the Breakeven Point and add this final fractional year to get the Payback Period:

![Payback Period Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201084%20361'%3E%3C/svg%3E "Payback Period Formula")

You can also calculate the Payback Period on an **unlevered basis**, like the difference between [Unlevered FCF](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/)
 and [Levered FCF](https://breakingintowallstreet.com/kb/valuation/levered-free-cash-flow/)
 and the Unlevered vs. Levered IRR.

If you do it this way, you use Unlevered Cash Flow instead of Cash Flow to Equity and the entire Upfront Capital, not just the Upfront Equity, in the “Unrecovered” calculations.

**(NOTE:** “Unlevered Cash Flow” in a Project Finance context is slightly different from Unlevered Free Cash Flow – yes, sorry, it’s confusing, and you should look at the [CFADS tutorial](https://breakingintowallstreet.com/kb/project-finance/cash-flow-available-for-debt-service-cfads/)
 to learn more.)

![Unlevered Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201080%20290'%3E%3C/svg%3E "Unlevered Payback Period")

![Project Finance & Infrastructure Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Project Finance Modeling for Energy, Transportation, and Mining Assets

*   #### Evaluate infrastructure deals like a pro
    
    You’ll evaluate the risks and rewards and make investment recommendations
    
*   #### Master financial modeling
    
    Model solar, wind, gas, nuclear, toll road, airport, and mining assets
    
*   #### Complete 8 case studies
    
    Build 4 shorter “crash course” models and 4 detailed “on the job” ones
    

[Full Details](https://breakingintowallstreet.com/project-finance-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Project-Finance-Modeling-Course-Outline.pdf)

**Why the Payback Period and IRR Often Tell Different Stories**
---------------------------------------------------------------

If you look at the Payback Periods, IRRs, and Cash-on-Cash Multiples here, you’ll see that **the returns are better in the “Levered” case, but the Payback Period is worse**:

![Levered vs. Unlevered Returns and Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20948%20604'%3E%3C/svg%3E "Levered vs. Unlevered Returns and Payback Period")

This is because the Cash Flow to Equity is much lower over the first 10 years, so it takes several extra years to recoup the Upfront Equity.

On an unlevered basis, the cash flows are significantly higher, more than offsetting the additional capital required initially.

**But the returns are worse because the unlevered calculations assume nearly twice as much capital invested in the beginning, which is worse in terms of the time value of money.**

However, the lower Payback Period tells us that the unlevered option is “less risky” due to the faster recoupment and the lack of Debt to potentially default on.

**What is a “Good” Payback Period?**
------------------------------------

There’s no universally “good” Payback Period, as it depends on the industry, asset type, and typical holding period.

It’s most useful as a way to **compare similar assets** in the same industry.

For example, if one solar plant has a Payback Period of 11.0 years, and another plant’s is 9.0 years, that helps you quantify the risk.

But you would never compare the Payback Period of an oil & gas well to a normal company acquired in a leveraged buyout.

As a _very rough guideline_, you could take the Upfront Price / Year 1 Cash Flow and use that for your “Expected Payback Period.”

If the Actual Payback Period is **lower**, it’s positive because it means the asset’s cash flow **grows** during the holding period.

If the Actual Payback Period is **higher**, that’s negative because it points to shrinking cash flows.

It’s positive when there’s a bigger “gap” between the Expected and Actual Payback Periods since it indicates more growth potential:

![Expected vs. Actual Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201051%20343'%3E%3C/svg%3E "Expected vs. Actual Payback Period")

**The Payback Period in Biotech Financial Modeling for Individual Drugs**
-------------------------------------------------------------------------

The Payback Period in biotech/biopharma modeling works differently because:

*   The **capital** is contributed over many years since the drug development and clinical trials take far longer than the construction of simple solar assets.
*   The **cash flows** from this drug or medical device must be probability-adjusted to reflect the chances of failure (not passing clinical trials or failing to launch commercially).

You can see some of the differences in a modified example taken from our [Biotech Valuation course](http://breakingintowallstreet.com/biotech-valuation/)
 below:

![Biotech Payback Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201073%20303'%3E%3C/svg%3E "Biotech Payback Period")

In biotech, the Breakeven Point tends to occur shortly after the drug launches, but this depends on when the investment is made as well.

Investors who fund the company earlier in the period, such as before the Phase I trials, will see longer Payback Periods.

Those who join in Phases II or III tend to experience shorter Payback Periods.

Drug sales tend to start at a certain level, take several years to “ramp,” and then reach a “peak sales” number before declining, as generic competitors enter the market and push down prices.

Therefore, a biotech company has only a small window in which to recoup the initial investment.

**Therefore, the Payback Period in biotech measures the product development and regulatory approval time _and_ the upfront costs _and_ the early sales potential of the drug.**

It still measures risk, but it’s more of a “combined” metric that factors in the development time and capital, _plus_ the sales potential _and_ the success probability at different stages.

[Sign Up for Project Finance Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Payback Period – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-06/PF-06-Payback-Period-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Payback Period Formulas in Project Finance (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/PF/PF-06/PF-06-Payback-Period.xlsm)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Project Finance & Infrastructure Modeling](https://breakingintowallstreet.com/project-finance-modeling/)

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[Learn More](https://breakingintowallstreet.com/project-finance-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Project Finance Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/2uXiVPKF/checkout)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with project finance and infrastructure modeling case studies. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/2uXiVPKF/checkout)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&mini=true)
[Email](mailto:?subject=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)

#### Project Finance & Infrastructure Modeling

Learn cash flow modeling for energy and transportation assets (toll roads, solar, wind, and gas), debt sculpting, and debt and equity analysis.

[LEARN MORE](https://breakingintowallstreet.com/project-finance-modeling/)

[](https://x.com/intent/tweet?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&mini=true)
[](mailto:?subject=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[](https://api.whatsapp.com/send?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Copy](https://breakingintowallstreet.com/kb/project-finance/payback-period/#)
[Email](mailto:?subject=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&t=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/project-finance/payback-period/)
[Pinterest](https://breakingintowallstreet.com/kb/project-finance/payback-period/#)
[Print](https://breakingintowallstreet.com/kb/project-finance/payback-period/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[SMS](sms:?&body=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[X](https://x.com/intent/tweet?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fproject-finance%2Fpayback-period%2F&title=The%20Payback%20Period%20in%20Project%20Finance%20and%20Asset-Level%20Modeling%3A%20A%20More%20Objective%20Measure%20of%20Risk%20and%20Growth%3F&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand