# Liquidation Preference: Full Tutorial + Excel Example

**Source:** https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference

---

The Liquidation Preference in Venture Capital: Full Tutorial and Excel Examples
===============================================================================

In venture capital and startup investing, a liquidation preference gives VC investors the option to earn back a fixed multiple of their investment in a company sale or shutdown rather than a percentage of its common equity, which provides downside protection in disappointing outcomes.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#tab-signup)
    

> **Liquidation Preference Definition:** In venture capital and startup investing, a **liquidation preference** gives VC investors the option to earn back a fixed multiple of their investment in a company sale or shutdown rather than a percentage of its common equity, which provides downside protection in disappointing outcomes.

VC investors get this Liquidation Preference because they normally invest in startups via **Preferred Stock**, not Common Stock, and the Preferred Stock carries additional rights and privileges that make it senior to Common Stock.

One of these rights and privileges is the Liquidation Preference, which is easiest to illustrate with a simple numerical example.

Let’s say that a VC-backed startup has two outside investors: The Seed investors, which invested $2 million, and Series A investors, which invested $5 million.

After these funding rounds and several stock and option grants to employees, the Seed investors own 15% of the company, and the Series A investors own 25% according to the [cap table](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
.

If this startup now sells for $100 million, the Seed investors earn 15% \* $100 million = $15 million, and the Series A investors earn $25 million.

The Seed investors earn a 7.5x multiple, the Series A investors earn a 5.0x multiple, and everyone is happy:

![$100 Million Exit Proceeds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201285%20454'%3E%3C/svg%3E "$100 Million Exit Proceeds")

But now imagine that the startup sells for a much lower value, such as $10 million.

_Without_ Liquidation Preferences, the Seed investors earn $1.5 million, and the Series A investors earn $2.5 million, so they both **lose money in the deal:**

![Money Lost in a $10 Million Exit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201286%20652'%3E%3C/svg%3E "Money Lost in a $10 Million Exit")

They lose money because **they invested at** **valuations higher than $10 million**, so they “bought high and sold low.”

If both investor groups had 1x Liquidation Preferences, the Series A investors would earn $5 million, and the Seed investors would earn $2 million:

![Liquidation Preferences in a $10 Million Exit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201288%20687'%3E%3C/svg%3E "Liquidation Preferences in a $10 Million Exit")

When there’s a Liquidation Preference, the investor group has the **option** to earn either a fixed multiple of their initial investment _or_ their Ownership % \* Exit Equity Value.

With the first option, the investor group stays in **Preferred Stock**; with the second, they convert to **Common Stock**.

In this case, the investors would prefer to earn $5 million and $2 million rather than $2.5 million and $1.5 million, so they stay in **Preferred Stock** and take their Liquidation Preferences.

The **concept** of a Liquidation Preference is not complicated, but if you want to implement it in Excel robustly, some of the formulas can be tricky.

### **Files & Resources:**

[Liquidation Preference Guide – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Liquidation-Preference/Liquidation-Preference-Slides.pdf)

[Simple Liquidation Preference Example (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Liquidation-Preference/Liquidation-Preference.xlsx)

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **1:25:** Part 1: Simple 1x Liquidation Preference Example
*   **4:17:** Part 2: What Makes Liquidation Preferences Tricky?
*   **9:13:** Part 3: Pari Passu Liquidation Preferences
*   **12:43:** Part 4: The Liquidation Preference Waterfall
*   **14:47:** Recap and Summary

**What is a Liquidation Preference, and What Makes It Tricky?**
---------------------------------------------------------------

The Liquidation Preference refers to the concept described above: **The option** for the VC investors to earn back a fixed multiple of their investment (1x in most cases) or their Ownership % \* Exit Equity Value.

Writing formulas for the Liquidation Preference in [capitalization tables](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
 is trickier than expected because you may need to **recalculate each group’s ownership percentages**.

For example, if the Series A investors stay in Preferred, but the Seed investors convert to Common, **the Seed Investors now own a higher percentage of the company’s common equity.**

This point explains why one formula in this analysis is simple while the other is far more complicated:

![Liquidation Preference Formulas for the Seed and Series A Investors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201298%20963'%3E%3C/svg%3E "Liquidation Preference Formulas for the Seed and Series A Investors")

The Series A formula is simple:

\= – MIN(MAX(Liquidation Preference, Common Equity Proceeds), Exit Equity Value)

The Series A investors take their Liquidation Preference if it’s bigger or take Ownership % \* Exit Equity Value if that’s bigger.

If the Exit Equity Value is so low that it can’t even cover the Liquidation Preference, they get this Exit Equity Value instead.

The Seed formula is quite a bit more complicated. Written out in words, it’s as follows:

\=IF(– Series A Investor Proceeds <= Series A Liquidation Preference, – MIN(MAX(Seed Liquidation Preference, Seed Ownership % / (Seed Ownership % + Common Shareholder Ownership %) \* Proceeds Remaining for Seed and Common), Proceeds Remaining for Seed and Common), – MIN(MAX(Seed Liquidation Preference, Seed Common Equity Proceeds), Proceeds Remaining for Seed and Common))

You can split this formula into two main cases:

### **Case #1: Series A Investors Stay in Preferred and Earn Their Liquidation Preference (Or Less)**

This is the first part of the IF statement. In this case, the Series A investors take their Liquidation Preference, so we must recalculate the Seed Ownership.

The second part of the formula takes the 15% the Seed investors own and divides it by (15% + 60%) to “gross it up” to **20%**.

Now that the Series A investors are gone, the Seed investors own 20% rather than 15%.

However, this is 20% of a lower number: $5 million rather than $10 million. And 20% \* $5 million = $1 million.

This is a **worse outcome** for the Seed investors than staying in Preferred and getting their $2 million Liquidation Preference, so the MAX(E19 part of the formula makes them do that instead.

The MIN(D26 in the outer part of the formula limits the proceeds to the Seed investors to the amount left over after the Series A investors have been paid.

For example, even if the Liquidation Preference is $2 million, but there are only $500K of proceeds left, the Seed Investors get only $500K:

![Cap on Seed Investor Proceeds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201289%20456'%3E%3C/svg%3E "Cap on Seed Investor Proceeds")

### **Case #2: Series A Investors Convert to Common Shares**

This case is much easier and follows the same idea as the Series A formula above.

If the Series A investors convert to common shares, the Seed investors get the MAX of their Liquidation Preference and their Exit Value If Converted, with a cap based on the Proceeds Remaining.

In this $10 million exit, the Seed investors’ Common Shares are worth $1.5 million, but their Liquidation Preference is $2.0 million. Therefore, they’ll stay in Preferred Stock.

The Proceeds Remaining After Series A Payment are $5.0 million, which is more than enough to cover this.

But if the Proceeds Remaining were only $1.0 million, the Seed investors would receive only this $1.0 million, and the Co-Founders and Employees would get nothing:

![Seed Investors Capped by Exit Equity Value Proceeds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201270%20459'%3E%3C/svg%3E "Seed Investors Capped by Exit Equity Value Proceeds")

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

**2x and 3x Liquidation Preferences**
-------------------------------------

Mechanically, nothing is different when there are 2x, 3x, or even higher Liquidation Preferences.

However, these numbers are less common and are seen more frequently in market downturns and difficult environments, such as the aftermath of the dot-com crash in 2000 – 2002.

They’re more common when startup valuations “reset,” such as in 2022, when central banks aggressively increased interest rates following the high inflation resulting from massive money printing and 0% interest rates during COVID.

These higher liquidation preference multiples are also common in later-stage, [growth-oriented rounds](https://mergersandinquisitions.com/growth-equity/)
, such as Series C, D, and E funding done at high valuations.

They effectively “lock in returns” for the late-stage VCs if the company sells for a low or disappointing valuation.

If an investment has a 2x or 3x Liquidation Preference attached, **it shifts the incentives** and means the Exit Equity Value must be higher for the VCs to convert to common shares.

If the company sells for $50 million in this example, and both investor groups have 3x Liquidation Preferences, the Series A investors will stay in Preferred Stock, but the Seed investors will convert to Common:

![Investor Proceeds with 3x Liquidation Preferences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20462'%3E%3C/svg%3E "Investor Proceeds with 3x Liquidation Preferences")

**Pari Passu Liquidation Preferences**
--------------------------------------

In some deals, certain VC investors have **“pari passu”** terms, which means “on equal footing” in Latin.

In this example, it means that the Series A investors no longer get to make a conversion decision first – instead, the Seed and Series A investors can opt to act together.

In practice, the **pari passu** term comes up most frequently when there’s not enough in Exit Equity Proceeds to cover all the Liquidation Preferences.

If this happens, pari passu means the proceeds will be **split proportionally** based on each group’s percentage of the total Liquidation Preference.

For example, imagine that a startup sells for $5 million.

Without pari passu seniority, the Series A investors would get all $5 million, and the Seed investors would get nothing because the Series A investors have a $5 million Liquidation Preference and are senior to the Seed investors:

![$5 Million Exit with No Pari Passu Terms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201273%20468'%3E%3C/svg%3E "$5 Million Exit with No Pari Passu Terms")

With pari passu, these $5 million in Exit Equity Proceeds are split based on each group’s Liquidation Preference percentage ($2 / $7 = ~29%, and $5 / $7 =~71%).

To set this up, we can add another **condition** to the Series A proceeds formula.

We’ll check if the Exit Equity Value _exceeds_ the Total Liquidation Preferences _or_ if the pari passu option in cell D8 is disabled (i.e., it’s set to 0 rather than 1).

If either one is true, we proceed with the normal formula.

If not – if pari passu is enabled **and** the Exit Equity Value is smaller than the Total Liquidation Preferences – then we split up the Exit Equity Value based on the Liquidation Preference percentages instead:

![$5 Million Exit with Pari Passu Terms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201305%20663'%3E%3C/svg%3E "$5 Million Exit with Pari Passu Terms")

In this case, we do **not** need to modify the Seed Investor formula because the “Proceeds Remaining” are always less than the Seed Liquidation Preference when this happens.

If there were more investor groups, we would need to take a different approach and modify these formulas more extensively.

**The Liquidation Preference Waterfall**
----------------------------------------

On that note, Liquidation Preferences can become very complex in exit scenarios with 5 – 10 VC investor groups, each with different terms and ownership percentages.

With this many groups, writing single formulas to determine whether each group should convert to Common or stay in Preferred Stock becomes **unwieldy**.

It’s easier to **“run a simulation”** and examine all possible combinations of conversion decisions in Excel:

*   Seed converts; Series A stays; Series B stays…
*   Seed converts; Series A converts; Series B stays…
*   Seed converts; Series A converts; Series B converts…

There are 2 ^ 3 = 8 combinations with these 3 investor groups and 2 possible decisions per group.

The number of combinations can grow quickly (e.g., 2 ^ 6 = 64 for 6 investor groups), so we might group investors with similar terms and assume they always act together.

For example, the Seed and Series A investors might always make the same conversion decisions because they both invested in earlier rounds at much lower valuations.

You can see an example below (called a [Flow of Funds](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
), taken from the advanced cap table case study in Module 4 of our [Venture Capital Modeling course](https://breakingintowallstreet.com/venture-capital-modeling/)
:

![Flow of Funds - Conversion Combinations for VC Investor Groups](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201403%201047'%3E%3C/svg%3E "Flow of Funds - Conversion Combinations for VC Investor Groups")

Terms such as Participating Preferred, which give investors not only their Liquidation Preferences but also a percentage of the Common Equity Proceeds, can make these formulas even more complex.

However, the starting point of this Liquidation Preference Waterfall is always the Exit Equity Value, followed by the Liquidation Preferences owned by the most senior VC investors.

The lower-ranked VCs follow, and then you consider the Participating Preferred Proceeds.

After that comes the Common Equity Proceeds for the VC investors that converted to Common Stock and the company’s employees, founders, and managers that have always held Common Stock.

**More Advanced Liquidation Preference Topics**
-----------------------------------------------

This tutorial introduces you to the main concepts behind Liquidation Preferences, but they can always get more complex.

For example:

*   [SAFE Notes](https://breakingintowallstreet.com/kb/venture-capital/safe-notes/)
     and [Convertible Notes](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
     might also offer Liquidation Preferences, but they may work differently depending on the conversion terms.
*   As mentioned above, terms like participating preferred stock and participation caps can change the mechanics.
*   And when there are many different investor groups, you need to set up a “simulation” like the one shown above to determine what happens.

We cover all these (and more) in our full [VC & Growth Equity course](https://breakingintowallstreet.com/venture-capital-modeling/)
, and we may publish a few additional tutorials on them.

[See BIWS Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Liquidation Preference Guide – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Liquidation-Preference/Liquidation-Preference-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Liquidation Preference Example (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Liquidation-Preference/Liquidation-Preference.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&mini=true)
[Email](mailto:?subject=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)

#### Master Cap Tables and Startup Modeling

Learn VC and growth equity financial modeling via 5 short case studies and 4 extended case studies on everything from AI to SaaS to biotech.

[LEARN MORE](https://breakingintowallstreet.com/venture-capital-modeling/)

[](https://x.com/intent/tweet?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&mini=true)
[](mailto:?subject=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[](https://api.whatsapp.com/send?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Copy](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#)
[Email](mailto:?subject=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&t=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
[Pinterest](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#)
[Print](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[SMS](sms:?&body=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[X](https://x.com/intent/tweet?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fliquidation-preference%2F&title=The%20Liquidation%20Preference%20in%20Venture%20Capital%3A%20Full%20Tutorial%20and%20Excel%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand