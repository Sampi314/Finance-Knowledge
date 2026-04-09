# Flow of Funds: Detailed Guide + Excel Examples and Video

**Source:** https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds

---

The Flow of Funds (Cap Table Waterfall) in Venture Capital, M&A, and More
=========================================================================

In venture capital and M&A modeling, the “Flow of Funds” refers to a model that calculates the exit proceeds in a deal to each investor group and determines the proper conversion decisions for all the investors; it is relevant primarily for acquired private companies because public company shareholders rarely have complex terms attached to their ownership.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#tab-signup)
    

> **Flow of Funds Definition:** In venture capital and M&A modeling, the “Flow of Funds” refers to a model that calculates the exit proceeds in a deal to each investor group and determines the proper conversion decisions for all the investors; it is relevant primarily for acquired private companies because public company shareholders rarely have complex terms attached to their ownership.

“Flow of Funds” can refer to many concepts in finance, from macro indicators about the banking system to the closing documents and wire transfers in a deal.

But in this article, we focus on the schedule that shows **how much each investor group earns when a venture capital-backed startup sells**, which is also known as a “Cap Table Waterfall”:

![Flow of Funds Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20447'%3E%3C/svg%3E "Flow of Funds Summary")

This schedule is relevant mostly in M&A exits because in [IPOs](https://mergersandinquisitions.com/ipo-process/)
, VC-held preferred shares normally convert to common shares and lose their special terms, such as [Liquidation Preferences](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
.

Also, in M&A deals, each group’s **conversion decision** (i.e., stay in preferred or convert to common) affects the optimal decisions of the other groups, which requires a specialized approach.

If the company has only 1 – 2 investor groups, we can easily write formulas to determine the optimal decision for each group:

![Simple Conversion Decision Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20470'%3E%3C/svg%3E "Simple Conversion Decision Formula")

But this becomes unwieldy as more groups invest and VC investment terms become more complex.

In theory, we could write a formula to handle a case with 5 VC groups and different investment terms, but it would be very difficult to audit and understand.

So, we normally approach this task by analyzing **all possible conversion decisions** and picking the set that maximizes overall proceeds to the VC investors.

To illustrate, we’ll walk through an example with 3 VC investor groups, company founders with common shares, and employees with an options pool:

### **Files & Resources:**

*   [Flow of Funds – Simple Example (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Startups-VC/Flow-of-Funds/Flow-of-Funds.xlsx)
     \[You must enable circular references in Options à Formulas à Iterative Calculations for this file to handle the employee options properly.\]
*   [Flow of Funds – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Startups-VC/Flow-of-Funds/Flow-of-Funds-Slides.pdf)
    

### **Video Table of Contents:**

*   **1:59:** Part 1: Flow of Funds: The Short Version
*   **3:34:** Part 2: Cap Table Data, Exit Price, and Conversion Combos
*   **5:08:** Part 3: Liquidation Preferences
*   **6:56:** Part 4: Participating Preferred Logic
*   **9:35:** Part 5: Common Share Counts and Options
*   **13:43:** Part 6: Net Proceeds and Multiples
*   **15:38:** Advanced Features
*   **17:10:** Recap and Summary

**Flow of Funds M&A Example for a VC-Backed Startup**
-----------------------------------------------------

This VC-backed startup has done well, but it has not been a gargantuan success (i.e., not on par with Google, Facebook, etc.).

So, the early-stage VC investors will do well, but the later-stage ones will earn less impressive multiples.

**Flow of Funds, Step 1: Set Up the Model (Exit Price, Cap Table Data, and Conversion Combinations)**
-----------------------------------------------------------------------------------------------------

At the time of the exit, this company has $400 million in revenue. Based on the [comparable public companies](https://breakingintowallstreet.com/kb/valuation/comparable-company-analysis-cca/)
, the VCs expect it to sell for 4x revenue.

It has $400 million of Net Debt, so its Exit Enterprise Value will be $1.6 billion, and its Exit Equity Value will be $1.2 billion.

This $1.2 billion is available for distribution to all the shareholders in the company:

![Flow of Funds - Exit Price Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20354'%3E%3C/svg%3E "Flow of Funds - Exit Price Calculation")

To proceed, we need information on the [capitalization table](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
. For example:

*   How many common shares does each group own? If they own preferred stock or options, what are their common share equivalents?
*   How much did each VC group invest, what are their liquidation preferences, and do any have participation preferred? If so, are there participation caps?
*   For the employees with options, what are the exercise prices? Are the options vested, unvested, or exercisable? How will the acquirer treat them in the deal?

Here’s our simplified summary for this startup:

![Flow of Funds - Cap Table Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20156'%3E%3C/svg%3E "Flow of Funds - Cap Table Summary")

The next step is to set up a table at the top of the sheet with 1’s and 0’s representing all possible conversion decisions the VC investors could make.

For example, the Series A, B, and C investors could all stay in preferred stock, which we represent with three 0’s at the top.

Or the Series C and B investors could stay in preferred, but the Series A investors could convert into common stock, which we represent with two 0’s and one 1:

![Flow of Funds - Conversion Combinations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20163'%3E%3C/svg%3E "Flow of Funds - Conversion Combinations")

There will be 2^n columns, where n = the number of different investor groups.

There are 3 groups here, so this is only 2^3 = 8 columns and is manageable.

**Flow of Funds, Step 2: Set Up the Liquidation Preference Logic**
------------------------------------------------------------------

In this step, we link in the Exit Equity Value at the top (called the “Equity Purchase Price” here from the acquirer’s perspective).

Then, we **ignore** the options proceeds for now and start setting up the liquidation preferences.

In each level, if the investors in this column stay in preferred, they get the lesser of their liquidation preference and the remaining available proceeds:

![Flow of Funds - Liquidation Preferences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20528'%3E%3C/svg%3E "Flow of Funds - Liquidation Preferences")

We then subtract this amount and calculate the “Remaining Proceeds” after each deduction.

**Flow of Funds, Step 3: Factor in Participating Preferred**
------------------------------------------------------------

The Liquidation Preferences always take top priority in this Flow of Funds schedule.

After that come the **Participating Preferred** proceeds.

Participating Preferred means that if an investor group stays in preferred stock and collects its Liquidation Preference, it can “double dip” and _also_ get a percentage of the remaining proceeds.

This percentage is normally linked to the group’s ownership of the common share equivalents.

So, Step 1 is to check whether this group stays in preferred _and_ if it has this “Participating Preferred” term attached.

However, Participating Preferred is also subject to **participation caps** in most cases; without these caps, it would unfairly favor the VC investors.

If there is a cap, we limit the total proceeds, including the liquidation preference, to that cap.

This cap is normally based on the group’s **Liquidation Preference**, not the total amount they’ve invested so far.

Here’s the formula:

![Flow of Funds - Participating Preferred](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202319%201008'%3E%3C/svg%3E "Flow of Funds - Participating Preferred")

For example, if the Series C investors have a $400 million Liquidation Preference and a $700 million Participation Cap, they can earn a maximum of $300 million from this Participating Preferred term (assuming there’s enough in proceeds to fund everything).

So, if their Ownership % \* Remaining Proceeds equals $500 or $600 million, it is reduced to $300 million instead.

On the other hand, if their Ownership % \* Remaining Proceeds equals $250 million, that’s fine because $250 + $400 = $650 million, which is below the $700 million total.

Nothing gets adjusted or limited in this case, and they receive the full $650 million in total proceeds.

**Flow of Funds, Step 4: Calculate the Common Share Counts and Account for Options and Warrants**
-------------------------------------------------------------------------------------------------

Next, we multiply each investor group’s conversion decision (1 or 0) by its common share equivalents to determine the number of common shares each group owns after all decisions are made.

For the true common shareholders (founders, some employees, etc.), there’s no multiplication since they’ve owned common shares from the start and cannot “convert” anything.

We **ignore** options, warrants, and anything else with an exercise price for now.

At the bottom, we take the Remaining Proceeds after all Liquidation Preferences and Participating Preferred distributions and divide by the Total Common Shares to get the Share Price:

![Flow of Funds - Share Price Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20591'%3E%3C/svg%3E "Flow of Funds - Share Price Calculation")

The “Common Equity Proceeds” above are based on each group’s ownership of the common shares in the “Share Counts Following Conversion” area times the Remaining Proceeds in row 41.

At this stage, we must finally address the option holders and the potential proceeds from exercising these options.

If the Implied Common Share Price is above the Exercise Price, the options are in-the-money, so the employees exercise them and receive shares.

If not, the options are out-of-the-money, so the employees do nothing and receive nothing in the exit.

This sounds simple, but it creates a [circular reference](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
 because the Implied Share Price depends on their exercise decision, but their exercise decision also depends on the Implied Share Price.

Why?

**Because if the employees exercise their options, the amounts they pay to the company _add_ to the total proceeds in the exit, which affects the proceeds to all the other groups and, therefore, the Implied Share Price at the end:**

![Flow of Funds - Circular References](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20750'%3E%3C/svg%3E "Flow of Funds - Circular References")

If a financial model contains circular references, there should always be a way to disable them, so we build that in here:

![Circular Reference Check for Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20568'%3E%3C/svg%3E "Circular Reference Check for Options")

At the top of the Cap Table Waterfall, the Options Exercise Proceeds are based on this common share count at the bottom times the Exercise Price (as shown above).

These calculations change the proceeds for everyone else because the option holders _contribute_ something, but also _withdraw_ something from this Flow of Funds.

**Flow of Funds, Step 5: Calculate the Net Proceeds and Multiples**
-------------------------------------------------------------------

Next, we add up the **net proceeds** for each investor group.

“Net” means that for the option holders, we **subtract** the amount they paid to exercise their options.

Then, we add up all the proceeds to all the VC investors and use an IF check with the MAX function to determine the optimal set of conversion decisions:

![Flow of Funds - Maximum Proceeds Check](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20436'%3E%3C/svg%3E "Flow of Funds - Maximum Proceeds Check")

After we copy and paste all the formulas across, we can get an actual answer (Conversion Decision Set #4 is optimal), and we can calculate the amount that goes to each group and the respective [Multiples of Invested Capital (MOICs)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
:

![Flow of Funds - Optimal Decisions and Multiples of Invested Capital](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20431'%3E%3C/svg%3E "Flow of Funds - Optimal Decisions and Multiples of Invested Capital")

This analysis assumes that the VC investors will collaborate to get the best overall outcome, which isn’t necessarily true in practice.

**Flow of Funds: Added Complexities**
-------------------------------------

Looking at this example, you might think the Flow of Funds schedule is easy.

However, this is a greatly simplified example that ignores many complexities that arise in real deals:

*   **Option Types:** Employee options might be unvested, vested, exercisable, or non-exercisable, and the acquirer often treats these categories differently (i.e., cancellation vs. assumption vs. cashed out in the deal).
*   **True Purchase Price:** Many M&A deals for VC-backed startups have [Earnouts](https://breakingintowallstreet.com/kb/ma-and-merger-models/earnout-accounting/)
     and other contingent consideration attached, and terms such as escrows and [Working Capital adjustments](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/working-capital-adjustment/)
     may alter the true amount available to the shareholders.
*   **Investor Priority and Seniority:** Do the Series C investors “rank” ahead of the Series B and Seed/Series A ones? Or do they have “pari passu” (equal ranking) or something else? The order of operations changes based on this.
*   **More Complex Securities:** Does the startup have [convertible notes](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
    , a [SAFE](https://breakingintowallstreet.com/kb/venture-capital/safe-notes/)
    , [venture debt](https://breakingintowallstreet.com/kb/venture-capital/venture-debt/)
    , or venture loans? What about an investment with a cumulative participating preferred term? These securities and terms alter the conversion decisions and share counts.
*   **Too Many Combinations:** What if there are 10 investor groups? Will you create 2^10 = 1,024 columns in Excel? At this level of complexity, you would normally change the approach and use VBA or another coding/automation tool to “run the simulations” and make the correct decisions.

We cover some of these more advanced features for VC-backed startups in our full [Venture Capital & Growth Equity course](https://breakingintowallstreet.com/venture-capital-modeling/)
.

[See BIWS Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Flow of Funds - Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Startups-VC/Flow-of-Funds/Flow-of-Funds-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Flow of Funds - Simple Example (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Startups-VC/Flow-of-Funds/Flow-of-Funds.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&mini=true)
[Email](mailto:?subject=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)

#### Master Cap Tables and Startup Modeling

Learn VC and growth equity financial modeling via 5 short case studies and 4 extended case studies on everything from AI to SaaS to biotech.

[LEARN MORE](https://breakingintowallstreet.com/venture-capital-modeling/)

[](https://x.com/intent/tweet?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&mini=true)
[](mailto:?subject=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[](https://api.whatsapp.com/send?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Copy](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#)
[Email](mailto:?subject=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&t=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
[Pinterest](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#)
[Print](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[SMS](sms:?&body=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[X](https://x.com/intent/tweet?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fflow-of-funds%2F&title=The%20Flow%20of%20Funds%20%28Cap%20Table%20Waterfall%29%20in%20Venture%20Capital%2C%20M%26A%2C%20and%20More&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand