# Capitalization Table: Full Tutorial + Excel Example

**Source:** https://breakingintowallstreet.com/kb/venture-capital/capitalization-table

---

The Capitalization Table (Cap Table): Full Guide + Excel Examples
=================================================================

The capitalization table (“cap table”) for a startup or venture capital-backed business lists the shares owned by each individual or entity, their percentage ownership, the current value of this ownership, and any special terms associated with each group, such as liquidation preferences.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#tab-signup)
    

The Capitalization Table (Cap Table): Full Guide + Excel Examples

> **What is a Cap Table?:** The “cap table” for a startup or venture capital-backed business lists the shares owned by each individual or entity, their percentage ownership, the current value of this ownership, and any special terms associated with each group, such as liquidation preferences.

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

Here’s an example cap table taken from our [Venture Capital & Growth Equity Modeling course](https://breakingintowallstreet.com/venture-capital-modeling/)
:

![Example Cap Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202016%20724'%3E%3C/svg%3E "Example Cap Table")

This table lists the co-founders’ and executives’ shares, employees’ options, and the shares owned by the investors over 5 investment rounds (Seed through Series D).

When the startup sells, the cap table tells you **how much in proceeds each group earns,** factoring in their shares and special terms.

For large public companies, “cap tables” are pointless because these companies mostly have **common shares** with a small number of employee-owned options, restricted stock units (RSUs), and other dilutive securities.

There’s no need for a full table because if one investor owns 100 shares, they have the same ownership and economic value as 100 shares owned by any other investor.

(Some exceptions exist, such as companies with multiple share classes, separate voting/control shares, etc., but these are not common.)

**However, for startups, certain investors have special terms and privileges, so 100 shares owned by one group could be quite different from 100 shares owned by someone else.**

For example, venture capital (VC) firms often invest using **preferred stock**, which gives them more **downside protection** if the startup fails or sells for a low price.

Cap tables are also important because, with startups, **you need to track the share counts and ownership over time**.

This is a bit of an afterthought for public companies, but startups need to understand each investor group independently because they likely invested at different times and valuations.

Here’s a simple cap table Excel example and instructions for the key calculations:

### **Files & Resources:**

[Cap Table Guide – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Capitalization-Table/Capitalization-Table-Slides.pdf)

[Cap Table Example (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Capitalization-Table/Example-Cap-Table.xlsx)

### **Video Table of Contents:**

*   **1:07:** Part 1: Cap Tables: The Short Version
*   **2:30:** Part 2: Ownership and Investment Sizes
*   **3:47:** Part 3: Options and Liquidation Preferences
*   **6:09:** Part 4: New Shares and Options in the Round
*   **9:17:** Part 5: Share Price in Each Round
*   **10:27:** Part 6: Exit Calculations
*   **13:27:** Recap and Summary

**Cap Table Setup: Ownership and Investment Sizes**
---------------------------------------------------

At the minimum, you need to know **how much is invested in each funding round**, the pre- and post-money valuations, and any special terms attached to the funding.

Also, if the startup’s employees receive options in the round or its co-founders/managers get “free shares” in the round, you need this information.

In this example, the three co-founders each owned 33% of the company before they raised outside capital:

![Cap Table Pre-Investment (Company Founding)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201328%20508'%3E%3C/svg%3E "Cap Table Pre-Investment (Company Founding)")

Next, the company raised a $2 million Seed round at a $6 million pre-money valuation.

“Pre-money” means “The [Equity Value](https://mergersandinquisitions.com/enterprise-value-vs-equity-value/)
 _before_ the additional capital came in.”

The **post-money valuation** equals the pre-money valuation + the investment size, so it is $8 million here.

“Post-money” means “The Equity Value _after_ the additional capital,” so it should always be higher than the pre-money valuation.

The **investors’ ownership** in this round equals the Investment Size / Post-Money Valuation.

In other words, they invested $2 million into a company that is now worth $8 million, so they own $2 million / $8 million = 25%.

You can see this setup below:

![Cap Table - Seed Round Ownership](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201072%20260'%3E%3C/svg%3E "Cap Table - Seed Round Ownership")

**Cap Table Setup: Options and Liquidation Preferences**
--------------------------------------------------------

Venture capital investors typically invest using **preferred stock** rather than common shares.

They may convert their preferred stock into common shares at any time, but they typically keep them until the exit because doing so gives them special rights and privileges – such as [liquidation preferences](https://breakingintowallstreet.com/kb/venture-capital/liquidation-preference/)
.

In this $2 million Seed Round, the investors get a 1x “liquidation preference,” which equals $2 million \* 1x = $2 million.

This means that if the company sells for a very low valuation that would result in the Seed investors earning _less than $2 million_, they get the $2 million as a minimum return.

If the available proceeds are less than $2 million, they just get the available proceeds.

The liquidation preferences are not shown directly in the cap table until the exit calculations (see below), but you should enter and track them in each round:

![Cap Table - Liquidation Preferences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201174%20412'%3E%3C/svg%3E "Cap Table - Liquidation Preferences")

Another issue is that in each funding round, the startup normally grants **options to employees** to incentivize them to stay and work at the company.

These options become more valuable if the company performs well, and if the employees stay for several years, they can pay a small amount to “exercise” their options and get shares in the company (assuming the company’s value has increased).

If they do this, they can sell their shares for a solid profit since the share price should be much higher than the options’ original exercise price.

Options may be granted _before_ the funding round, _at the same time as_ the funding round, or _after_ the round.

If we assume the options are issued _before_ this funding round and represent 10% of the company, we can calculate the options granted to employees with:

\= Shares Before Round / (1 – Ownership) \* Ownership

\= 1.2 million / (1 – 10%) \* 10% = 133,333

We want them to own 10% _afterward,_ so we must “gross up” the share count, as 133,333 is 10% of 1.333 million shares:

![Cap Table - Options Pool](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201390%20896'%3E%3C/svg%3E "Cap Table - Options Pool")

Because we calculate the employee options _before_ the funding round, they end up owning _less than 10%_ after the funding round, as the VCs purchase 25% of the company:

![Cap Table - Options Pool Dilution Following Seed Round VC Funding](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201457%20386'%3E%3C/svg%3E "Cap Table - Options Pool Dilution Following Seed Round VC Funding")

This is quite unusual and not the intended result of a standard options pool, so we’ll look at a more traditional method in the next section.

**Cap Table Calculations: New Shares and Options in the Round**
---------------------------------------------------------------

While it’s critical to calculate the ownership and pre- and post-money valuation in each round, that’s **not enough** because you also want to track the _number of_ shares or options owned by each group and the effective share price.

In other words, if the Series A investors invest $5 million, how many shares do they get, and what price do they pay for each share?

This sounds simple, but it can get complicated because in addition to the VC investors that pay for shares, some groups **may get shares or options for free**.

For example, let’s say the Series A round VCs invest $5 million at a $15 million pre-money valuation, and the employee options pool is also upsized to 20% total ownership.

To calculate the **new shares** for each group in this round, we start by adding up the groups whose ownership does NOT change.

We have new Series A investors, and the employees get more options, but the Co-Founders and Seed investors do not get any new shares.

The employees will own 20% afterward, and the VCs are investing $5 million at a $15 million pre-money valuation, so they’ll own $5 / ($15 + $5) = 25%.

Therefore, these **“new/changed investors”** will own 20% + 25% = 45%, and the investors that stay the same will own 100% – 45% = 55%.

We then “gross up” the share count by taking the 1.778 million shares from before the round and dividing by this 55% ownership:

![Cap Table - Post-Investment Share Count Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201376%20972'%3E%3C/svg%3E "Cap Table - Post-Investment Share Count Calculations")

So, there will be approximately ~3.0 million total shares after the round, which means ~1.2 million new shares will be created.

We know the employees should own 20% \* 3.0 million of these, or ~598K. They already own 133K, so they’ll get 598K – 133K = 465K in the round:

![Cap Table - Employee Options Pool Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201390%20982'%3E%3C/svg%3E "Cap Table - Employee Options Pool Calculations")

Therefore, the remaining 1.2 million – 465K = 747K goes to the Series A investors, and they end up owning the 25% they initially targeted:

![Cap Table - Series A VC Ownership After Funding Round](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202392%20702'%3E%3C/svg%3E "Cap Table - Series A VC Ownership After Funding Round")

**The Cap Table: The Share Price in Each Round**
------------------------------------------------

Calculating the share price in each round is also useful because you may need this information when dealing with employee options and their exercise prices (or to assess the startup’s per-share value in an [IPO](https://mergersandinquisitions.com/ipo-process/)
 or M&A exit).

You can use one of two methods to calculate it:

1.  **Investment Size / Shares Purchased** – For example, in this Series A round, it’s $5 million / 747K shares = $6.69
2.  **Pre-Money Valuation / (Pre-Money Shares + “Free” Shares and Options Granted in Round)** – For example, here it’s $15 million / (1.8 million + 465K) =$6.69.

More advanced features, such as anti-dilution provisions, [SAFE notes](https://breakingintowallstreet.com/kb/venture-capital/safe-notes/)
, [convertible notes](https://breakingintowallstreet.com/kb/venture-capital/convertible-notes/)
, [venture debt](https://breakingintowallstreet.com/kb/venture-capital/venture-debt/)
, warrants, or follow-on investments can complicate these calculations, but the basic idea is simple:

![Share Price Calculations in a Capitalization Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201886%201006'%3E%3C/svg%3E "Share Price Calculations in a Capitalization Table")

**Cap Table Use in Real Life: Exit Calculations with a Liquidation Preference**
-------------------------------------------------------------------------------

One of the **main points** of a cap table is to determine the **exit proceeds** to each group if the startup sells or goes public.

We’ll focus on the “startup sells” case here and assume a **$100 million exit** (i.e., the Exit Equity Value is $100 million, so these are the total proceeds available to the shareholders).

To determine the exit proceeds, we multiply each group’s ownership percentage by the $100 million:

![Capitalization Table Exit Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201724%20378'%3E%3C/svg%3E "Capitalization Table Exit Calculations")

However, this assumes that none of these investors **take their liquidation preferences** and instead convert to common shares, which offer ownership in an exit.

By contrast, if the investors stay in preferred, they would simply earn their liquidation preferences in an exit.

In this case, all the investors would convert to common shares because it’s better to earn $25 million rather than $5 million or $15 million rather than $2 million.

However, if the company sells for a much lower price, such as an $18 million Exit Equity Value, things change dramatically:

![Capitalization Table - Exit with Liquidation Preferences Included](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201726%20570'%3E%3C/svg%3E "Capitalization Table - Exit with Liquidation Preferences Included")

In this case, the Series A investors’ stake is worth only $18 million \* 25% = $4.5 million, so they’ll take their $5 million liquidation preference instead.

Since they’ve taken their liquidation preference, **the Seed investors now own more of the company**.

Instead of just 14.9%, they own 14.9% / (14.9% + 60.1%) = 19.8%.

The remaining proceeds are only $13 million now, since $18 million – $5 million = $13 million, so the Seed investors earn 19.8% \* $13 million = $2.6 million.

This amount exceeds their liquidation preference of $2 million, so they choose to convert into common shares and get the $2.6 million.

This is why it’s so important to use a real cap table for startup modeling: These details would be lost if you only tracked the shares owned by each group, and you’d get incorrect results in “low exit value” cases.

**More Advanced Cap Table Topics**
----------------------------------

This tutorial scratches the surface of capitalization tables.

Other, more advanced topics include:

*   [SAFE Notes](https://breakingintowallstreet.com/kb/venture-capital/safe-notes/)
    , Convertible Notes, and other forms of investing in “unpriced” rounds without a defined pre- or post-money valuation.
*   Venture debt, venture loans, and warrants associated with these.
*   “Down rounds” and terms such as anti-dilution provisions that protect earlier investors.
*   Participating preferred stock with participation caps.
*   Flow of Funds analysis that presents multiple exit scenarios and includes circular calculations for employees’ exercise of options.

We cover all these (and more) in our full [VC & Growth Equity course](https://breakingintowallstreet.com/venture-capital-modeling/)
, and we may publish a few additional tutorials on them.

If you want a short preview of some of these topics, please see the sections below:

Cap Table Management: Excel vs. Dedicated Software
--------------------------------------------------

As with many other tasks in finance, companies can manage their cap tables “the manual way” (i.e., with Excel) or by using dedicated software/services, such as Carta, which automates much of the process.

The trade-offs are the same as any other manual vs. automated approach: Excel is cheaper, flexible, and fine for simple scenarios, but tends not to work well beyond a certain complexity level.

So, once a VC-backed startup goes beyond a few early-stage funding rounds, it often switches to something like Carta to manage its cap tables, investors, ownership, and options pools.

However, it is more expensive to implement, and it doesn’t offer the full control that a customized Excel model does, which can make it tricky to handle one-off and “random” scenarios.

Our courses focus on cap tables in Excel because not everyone has Carta access, while Excel is universally available.

Cap Table Waterfall Analysis: Modeling Exit Proceeds
----------------------------------------------------

The exit examples and liquidation preference calculations above are quite simple because there are only a few investor groups and only one group of founders/employees.

In real life, it gets considerably more complicated as the startup grows because many additional investor groups tend to join the cap table by investing in later funding rounds.

Because each investor group has a different priority and different terms attached to their capital, it becomes unwieldy to write a single formula that determines whether the VC investors will convert their preferred shares into common.

Instead, you normally take more of a “simulation” approach and examine all the possibilities.

For example, maybe Group A stays in preferred stock, but Groups B and C convert to common, or all three groups convert to common.

You examine all the possible combinations and calculate the proceeds to each investor group in a “waterfall analysis,” also known as a “[Flow of Funds](https://breakingintowallstreet.com/kb/venture-capital/flow-of-funds/)
” analysis.

Investors who stay in preferred always get paid first via their liquidation preferences.

Participating preferred payouts come after that, and payments to the common equity investors come last (both founders/employees and VCs that converted to common):

![Flow of Funds - Participating Preferred Proceeds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201425%20907'%3E%3C/svg%3E "Flow of Funds - Participating Preferred Proceeds")

You normally run all these scenarios and take the maximum of the total investor exit proceeds to determine which conversion decisions are optimal for the group as a whole.

Pre-Emptive Rights and Pro-Rata Participation
---------------------------------------------

Continuing with the example above, suppose that instead of exiting, the VC-backed startup decides to raise a Series B funding round.

Its goal is to raise $20 million at a $100 million post-money valuation, so the Series B VCs will own 20% of the company.

When this happens, the Seed Investors and Series A investors will get **diluted** because they will not receive any new shares or even have the option to invest in this round.

Dilution always happens as VC-backed startups grow because there’s no way to fully prevent it: Different investors invest at different stages and for different amounts of capital.

Therefore, even if the Seed and Series A investors love a company, they can’t necessarily keep investing in the Series B, C, and D rounds because they don’t have the capital to do so.

However, they can **limit the damage** in these later rounds by taking advantage of pre-emptive rights, also known as pro-rata rights.

These give earlier investors the ability to invest an amount in later rounds that maintains their ownership (but this does not last forever – much later rounds tend to reduce this right).

So, for example, the Series A investors shown above with 25% ownership might have the chance to invest up to $X in the Series B round, which would maintain their 25% ownership.

These pro-rata features make cap tables tricky because you need to consider the dilutive impact on all parties in the deal and determine the correct investment amounts and shares to create.

Frequently Asked Questions (FAQ)
--------------------------------

### How do I create a cap table?

Start by listing all the shareholders and option holders in the company, their share/option counts, and the ownership percentages these imply on a fully diluted basis (i.e., by assuming all the options convert into common shares 1:1).

Then, you start adding funding rounds and additional investments as well as new and upsized option pools to the mix.

It’s also useful to add some type of “exit scenario” at the bottom to illustrate the proceeds that go to different groups if the company sells.

### Do all companies have cap tables?

All companies have shares, so all companies have cap tables.

However, only VC-backed startups typically _create_ and _track_ their cap tables using the methods above.

True small businesses rarely do this because there is typically just one owner (or a small group of owners), and large public companies also do not do this because everyone has common shares, options, or RSUs, with none of the complexity seen with standard VC investments.

### How do I calculate a cap table?

You don’t “calculate” a cap table.

You calculate _elements_ of a cap table, such as the ownership, by taking each group’s _fully diluted shares_ and dividing by the entire _fully diluted share count_ of the company as a whole.

Each group’s share value is based on their ownership \* the company’s current Equity Value, as determined in its most recent funding round.

### Is a cap table legally binding?

No. Cap tables are used as reference/record documents, but they are not part of the articles of incorporation or shareholder agreements or signed documents required to close funding rounds.

### Is a cap table a financial statement?

No. It does not track revenue, expenses, cash flows, assets, or liabilities, so it is not a financial statement.

Note also that it is _not_ the same as the Statement of Shareholders’ Equity – despite the similar name, the Statement of Shareholders’ Equity is used for different purposes (namely, tracking changes that affect the company’s Equity, not just its ownership).

### Why do startups need cap tables?

They need cap tables because “1 share” owned by one group is not necessarily the same as “1 share” owned by another group.

VC investments into startups often have idiosyncratic terms and privileges and different conversion rights, so you must track the common shares that each investor could potentially own, and any special terms attached, such as liquidation preferences.

### What information does the cap table keep track of?

It tracks each VC/investor group, the founders/employees, and their share/option counts, ownership, exercise prices for the options, and any other special terms attached, such as liquidation preferences, pro-rata rights, and more.

Over time, the cap table also demonstrates how the company’s ownership changes as it raises additional funding rounds.

### Are cap tables public information?

No, but if/when a startup finally goes public, it may disclose partial cap table information in its S-1 IPO filing, such as the number of common shares owned by different investor groups.

Before that happens, cap tables are private and normally shared only with founders, early employees, investors, and advisors.

### Who manages the cap table?

In the earliest stages of a startup, the CFO or “Business Person” manages it. Eventually, that responsibility shifts to the finance/legal teams.

Even if the startup begins using specialized software to manage it, someone on those teams still takes responsibility for updating and checking it.

### What is a fully diluted cap table?

“Fully diluted” means that you assume that all dilutive securities, such as options, warrants, and convertible bonds, are converted into common shares _even if they could not necessarily be converted right now._

For example, if an employee owns 100 options that each represent 1 share, you would record 100 common shares for that employee in the cap table, even if the employee has not exercised their options yet.

For options and warrants, you do **not** assume any proceeds/cash inflows from the exercise of these securities. You simply show the common share counts they represent.

You **do** factor in the exercise proceeds in the “Waterfall” or “Flow of Funds” to calculate the exact cash that gets distributed to each group in a company sale.

[See BIWS Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Cap Table Tutorial – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Capitalization-Table/Capitalization-Table-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Example Cap Table – Excel Model (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/Capitalization-Table/Example-Cap-Table.xlsx)
    

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

[X](https://x.com/intent/tweet?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&mini=true)
[Email](mailto:?subject=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)

#### Master Cap Tables and Startup Modeling

Learn VC and growth equity financial modeling via 5 short case studies and 4 extended case studies on everything from AI to SaaS to biotech.

[LEARN MORE](https://breakingintowallstreet.com/venture-capital-modeling/)

[](https://x.com/intent/tweet?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&mini=true)
[](mailto:?subject=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[](https://api.whatsapp.com/send?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Copy](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#)
[Email](mailto:?subject=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&t=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/)
[Pinterest](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#)
[Print](https://breakingintowallstreet.com/kb/venture-capital/capitalization-table/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[SMS](sms:?&body=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[X](https://x.com/intent/tweet?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fcapitalization-table%2F&title=The%20Capitalization%20Table%20%28Cap%20Table%29%3A%20Full%20Guide%20%2B%20Excel%20Examples&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand