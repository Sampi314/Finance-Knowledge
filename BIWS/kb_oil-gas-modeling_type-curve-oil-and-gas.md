# Type Curve Oil and Gas: Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas

---

The Type Curve in Oil and Gas: Financial Modeling Master Key, or Academic Curiosity?
====================================================================================

In oil & gas financial modeling, the “Type Curve” plots the initial production (oil, gas, and natural gas liquids) from a specific type of well in a certain region and shows how that production declines over time; this curve is used to estimate the revenue, expenses, and CapEx associated with a well and its associated IRR and NPV.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#tab-signup)
    

The Type Curve in Oil and Gas: Financial Modeling Master Key, or Academic Curiosity?

> **Type Curve Oil and Gas Definition:** In oil & gas financial modeling, the “Type Curve” plots the initial production (oil, gas, and natural gas liquids) from a specific type of well in a certain region and shows how that production declines over time; this curve is used to estimate the revenue, expenses, and CapEx associated with a well and its associated IRR and NPV.

You can see a real-life example of a **Type Curve** taken from an investor presentation by SilverBow Resources below:

![Eagle Ford Type Curve Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20907%20664'%3E%3C/svg%3E "Eagle Ford Type Curve Example")

Type Curves are important because in [oil & gas modeling](https://breakingintowallstreet.com/oil-gas-modeling/)
, you often set up projections for all the **individual wells** the company currently operates or plans to drill.

Using a Type Curve, you can forecast the production from these wells and aggregate it across all the drilling years with functions such as OFFSET:

![OFFSET to Aggregate Well-Level Production](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202022%20814'%3E%3C/svg%3E "OFFSET to Aggregate Well-Level Production")

So, the Type Curve often forms the basis of an oil & gas company’s **future cash flow growth** (or, more precisely, an exploration & production company’s future growth, since many companies in oil & gas perform non-drilling activities).

Unfortunately, it can be difficult to use Type Curve analysis in real-life [financial models](https://mergersandinquisitions.com/financial-modeling/)
, especially when you are under time pressure to finish the model.

![Oil & Gas Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Dominate Your Investment Banking Interviews With **BIWS Oil & Gas Modeling**

*   #### Learn the 3 major verticals
    
    You’ll learn to build Upstream, Midstream, and Downstream models
    
*   #### Master financial modeling
    
    Learn how to use the NAV Model, new valuation multiples, and O&G-specific nuances for the DCF and DDM
    
*   #### Complete 3 detailed case studies
    
    Model Range Resources, Western Midstream Partners, and Saras S.p.A.
    

[Full Details](https://breakingintowallstreet.com/oil-gas-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Oil-Gas-Modeling-Course-Outline.pdf)

Companies often provide partial or incomplete information or do not fully describe all their wells with Type Curves.

**Also, Type Curves are not particularly useful for all the wells that are ALREADY producing oil/gas/NGLs; for most E&P companies, these wells account for most of the [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
 in the valuation.**

### **Files & Resources:**

*   [Type Curves in Oil and Gas – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Type-Curve-Oil-and-Gas-Slides.pdf)
    
*   [Simple Type Curve Example (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Type-Curve-Oil-and-Gas.xlsx)
    
*   [Type Curve Image – SilverBow Resources (PNG)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Eagle-Ford-Type-Curve.png)
    
*   [Range Resources Investor Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Range-Resources-Investor-Presentation.pdf)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **0:52:** The Short Version
*   **3:18:** Part 1: What is a Type Curve? Key Vocabulary
*   **6:18:** Production Forecasts
*   **8:48:** Part 2: From Type Curves to Models and Cash Flows
*   **17:14:** Part 3: Real-Life Problems with Type Curves
*   **19:16:** Recap and Summary

**What is a Type Curve? Key Vocabulary**
----------------------------------------

To understand Type Curves in oil & gas modeling, you need to know a few key terms first:

*   **D&C Costs or D&C:** “Drilling & Completion”; this is the upfront CapEx required to drill a new well.
*   **EUR:** This is the “Estimated Ultimate Recovery,” or the total amount of oil/gas/NGLs the company believes it can recover over the lifetime of the well in an economically feasible way. It’s normally measured in Billion Cubic Feet Equivalent (Bcfe) for natural gas-dominant wells or Millions of Barrels of Oil Equivalent (MMBOE) for oil/NGL-dominant wells.
*   **IP or IP Rate:** This stands for “Initial Production” and represents the _daily amount_ of oil/gas/NGLs the well produces when it is first drilled. It’s normally measured in Million Cubic Feet Equivalent per Day (Mmcfepd) or Thousands of Barrels of Oil Equivalent per Day (Mboepd) for oil-dominant wells.
*   **B-Factor:** This measures, roughly, the “steepness” of the decline curve after the well’s initial production period. For hyperbolic decline curves, a _higher_ B-Factor means a _shallower_
*   **Terminal Decline:** This represents the _minimum_ decline rate that the production from this well will ever reach, even if a formula predicts lower values.
*   **LOE:** This stands for “Lease Operating Expense” and represents the fixed and variable costs associated with the well once it has been drilled and begins operating.
*   **NPV-10:** The [Net Present Value](https://breakingintowallstreet.com/kb/finance/net-present-value/)
     of the well, including upfront CapEx and future cash flows, at the industry-standard 10% [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
    .
*   **IRR:** This represents the [internal rate of return](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
     on the well, factoring in the upfront CapEx and the future cash flows. Like all IRR metrics, it is roughly “the annualized rate of return,” but it’s often deceptively high in oil & gas because the production is front-loaded.

Once you understand all the parameters, you can use various formulas and equations to forecast production based on Type Curves.

For example, one common formula for the production from a “hyperbolic decline curve” is as follows:

![Hyperbolic Decline Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20210'%3E%3C/svg%3E "Hyperbolic Decline Formula")

You can use this formula to project the Daily Production from the well _at the end of each year_ over the ~40-year period shown here:

![Daily Production Decline Curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20629'%3E%3C/svg%3E "Daily Production Decline Curve")

Determining the “total production” each year based on the Daily Production numbers is tricky because, technically, you should use an integral to calculate **the area under the curve**.

However, if the decline rates are low, you can use simple averages or other numerical approximations and multiply the “average” Daily Rate by 365:

![Simple Average for the Annual Production from a Type Curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20277'%3E%3C/svg%3E "Simple Average for the Annual Production from a Type Curve")

**From Type Curves to Financial Models and Cash Flows**
-------------------------------------------------------

Once you have the production profile, you must **check the cumulative well production against the EUR** and split it into oil, gas, and NGLs.

Since the EUR is 14.25 Bcfe here, a single well can never produce more than that; if cumulative production reaches that level, it should immediately go to 0.

You can enforce this rule with a simple MIN function in Excel:

![Production Constraints Based on the EUR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20339'%3E%3C/svg%3E "Production Constraints Based on the EUR")

In a more robust model, you’d add a “Remainder” row at the bottom to account for the possibility of production continuing past Year 40:

![Remainder Row for Well Production and Cash Flows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20457'%3E%3C/svg%3E "Remainder Row for Well Production and Cash Flows")

The next step is to **forecast the revenue and expenses** associated with the well, typically based on constant gas, NGL, and oil prices, fixed/variable LOE, and variable transportation/processing costs, on either a $ / Mcfe or $ / BOE basis:

![Natural Gas Revenue](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201960%20508'%3E%3C/svg%3E "Natural Gas Revenue")

And the final step is to link in the D&C Costs for the upfront CapEx, calculate the Cash Operating Income, determine the total Pre-Tax Cash Flow, and calculate the IRR and NPV-10:

![IRR and NPV-10 from a Type Curve and Cash Flow Forecast](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20851'%3E%3C/svg%3E "IRR and NPV-10 from a Type Curve and Cash Flow Forecast")

In a full financial model, such as the Net Asset Value (NAV) Model commonly used for E&P companies, this Type Curve is one small component of one schedule.

The next step is to **aggregate production** from all the **new wells drilled** in each year of the model, which you can do with an OFFSET function:

![OFFSET to Aggregate Well-Level Production](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202022%20814'%3E%3C/svg%3E "OFFSET to Aggregate Well-Level Production")

Next, you create a “roll-up” for the revenue, expenses, and cash flows from these wells toward the bottom of the sheet:

![Cash Flow Aggregation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20454'%3E%3C/svg%3E "Cash Flow Aggregation")

In oil & gas, it’s critical to analyze the future cash flows and their Present Value _separately for each region and/or well type_, so it helps to make this as granular as possible.

Other components of this NAV Model might consist of the company’s production or well types in other regions and its cash flows from **existing wells that are already producing** (called “PDP” or “Proved Developed Producing” wells).

**The Problem(s) with Type Curves in Real Life**
------------------------------------------------

Almost every single book and course about oil & gas modeling presents Type Curves as an extremely important topic…

…and it’s true that _interview questions_ about them are quite common, so it helps to know the theory and their use cases.

**But in real life, it is much harder to use Type Curves because not all companies disclose the required information consistently, and even when they do, Type Curves do not “mesh” well with the company’s existing production.**

This example from SilverBow Resources above is unusual because large E&P companies rarely offer this much detail.

Instead, you often see summary production schedules like this one from Range Resources:

![Summary Production by Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202279%20771'%3E%3C/svg%3E "Summary Production by Year")

If you get summary data like this, you can’t use any of the hyperbolic decline curve formulas to project production since you don’t know the B-Factor and other key inputs.

Instead, you must create “rough approximations” based on the percentage of the well’s EUR produced in each year:

![Rough Approximations for the Production Decline Curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20447'%3E%3C/svg%3E "Rough Approximations for the Production Decline Curve")

So, while the Type Curve is nice in theory, you often end up making quick approximations for the production curve in real life.

**Another problem with Type Curves is that they’re only useful for modeling \*new wells\* from the company’s Proved Undeveloped (PUD) Reserves and any Probable (PROB) or Possible (POSS) Reserves, which are far more speculative.**

But most E&P companies’ values come primarily from their _existing, producing wells_, not these new, future wells:

![Pre-Tax Asset Values by Reserve Type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201635%20363'%3E%3C/svg%3E "Pre-Tax Asset Values by Reserve Type")

The Type Curve doesn’t work for modeling this production and these cash flows because you don’t know the “start date” of each well.

If a company has 500 wells, 50 might have been drilled last year, 30 the year before, and 40 the year before that, and you have no idea of each one’s current production level.

And no companies _ever_ disclose this information in their public filings or investor presentations.

You normally make simplifying assumptions for this production, such as a modest decline rate that decreases gradually over time, or even a fixed decline rate that “fits” the company’s expected Reserve Life Ratio (the R / P Ratio, defined as Proved Reserves / Annual Production).

In the NAV Model referenced here, we use a simple Goal Seek to determine a fixed 4-5% decline rate for this entire production segment:

![PDP Decline Rate Approximation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20275'%3E%3C/svg%3E "PDP Decline Rate Approximation")

A purist would dispute this approach and call for something more complicated, but it’s fine if you have limited time or the company does not disclose its information in a useful way.

[Sign Up To BIWS Oil & Gas Modeling](https://breakingintowallstreet.com/oil-gas-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Type Curves in Oil and Gas – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Type-Curve-Oil-and-Gas-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Type Curve Image – SilverBow Resources (PNG)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Eagle-Ford-Type-Curve.png)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Range Resources Investor Presentation (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Range-Resources-Investor-Presentation.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Type Curve Example (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Oil-Gas/Type-Curve/Type-Curve-Oil-and-Gas.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Oil & Gas Modeling](https://breakingintowallstreet.com/oil-gas-modeling/)

Master financial modeling and valuation for the Upstream, Midstream, Downstream, and Oilfield Services verticals via U.S., European, and Asian case studies.

[Learn More](https://breakingintowallstreet.com/oil-gas-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&mini=true)
[Email](mailto:?subject=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)

#### Master Oil & Gas Modeling

Learn financial modeling and valuation for the Upstream, Midstream, and Downstream verticals via U.S. and European case studies.

[LEARN MORE](https://breakingintowallstreet.com/oil-gas-modeling/)

[](https://x.com/intent/tweet?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&mini=true)
[](mailto:?subject=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[](https://api.whatsapp.com/send?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Copy](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#)
[Email](mailto:?subject=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&t=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/)
[Pinterest](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#)
[Print](https://breakingintowallstreet.com/kb/oil-gas-modeling/type-curve-oil-and-gas/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[SMS](sms:?&body=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[X](https://x.com/intent/tweet?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Ftype-curve-oil-and-gas%2F&title=The%20Type%20Curve%20in%20Oil%20and%20Gas%3A%20Financial%20Modeling%20Master%20Key%2C%20or%20Academic%20Curiosity%3F&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand