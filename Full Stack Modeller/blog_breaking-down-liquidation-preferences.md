# Breaking Down Liquidation Preferences

**Source:** https://www.fullstackmodeller.com/blog/breaking-down-liquidation-preferences

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Breaking%20Down%20Liquidation%20Preferences-1.png)

Breaking Down Liquidation Preferences
=====================================

Published [by Marcus Lertkomolsuk](https://www.fullstackmodeller.com/blog/author/marcus-lertkomolsuk)

Mar 2, 2023 10:39:00 AM

In this post, we'll cover the main components of a liquidation preference  

**![3a30ef_97c2acbc57b44f2bbf3c852406ba77e9_mv2](https://www.fullstackmodeller.com/hs-fs/hubfs/3a30ef_97c2acbc57b44f2bbf3c852406ba77e9_mv2.png?width=3072&height=3072&name=3a30ef_97c2acbc57b44f2bbf3c852406ba77e9_mv2.png)**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**What is Liquidation Preference?**
-----------------------------------

A liquidation preference is an important mechanism in venture capital that ensures investors receive their money back before any of the common shareholders, such as employees and founders. It is designed to protect the interests of preferred shareholders and mitigate the risks associated with early-stage investing. Before going into the details, it's important to understand the use cases and limitations of liquidation preferences.

Liquidation preferences are only attached to preferred shares, which are typically issued to investors during financing rounds. This means that a liquidation preference is only significant when a company exits via a merger or acquisition, or if its assets are sold during bankruptcy or recapitalization. It's worth noting that liquidation preferences are not relevant to public exits, as an initial public offering typically auto-converts all preferred shareholders into common shareholders. 

While liquidation preferences offer an added layer of protection for investors, they can also create complications and reduce the value of common shares. Founders and employees may have less incentive to work towards maximizing the value of the company if they are unlikely to receive a significant payout in the event of a sale or liquidation.

The Structure 
--------------

### Preference Stack

Getting liquidation preferences right during fundraising is crucial for both startups and investors. The first step is to negotiate the preference stack structure, which defines the order in which preferred stockholders get paid out during an exit. The three most common preference stack structures are Standard, Pari Passu, and Tiered. 

### Standard

Investors are paid in order from the latest to the earliest rounds. This means that investors who invested in the latest funding round receive their investment back first, followed by earlier rounds. Series A and seed investors face the risk of receiving back less than they put in or nothing at all. 

### Pari Passu

With a pari passu preference, investors from all funding rounds receive proceeds pro rata to their committed capital, and all have the same level of seniority status. This means that if the startup exits for less than its valuation or amount invested, every investor receives part of the proceeds. 

### Tiered

Some payout orders are determined by grouping seniority levels into tiers. Within each tier, investors follow the pari passu payout. 

### Liquidation Multiple

The second step is to negotiate the liquidation multiple, which specifies the amount of the investment that the preferred stockholders are entitled to before common shareholders receive any proceeds. 

Let's say a VC invested USD 2m in your startup with a 2x liquidation preference. This means that in the event of a liquidation or sale of the company, the VC is entitled to receive two times its initial investment of USD 2m before any other shareholders receive anything. 

If the company is sold for USD 7m, the VC would receive USD 4m, and the remaining USD 3m will be distributed among other shareholders in proportion to their ownership. 

However, if the company is sold for USD 3m, the VC is still entitled to receive USD 4m. In this scenario, the VC would receive all of the USD 3m with nothing remaining to be distributed among other shareholders. 

High multiple liquidation preferences can create problems for future funding rounds and negatively impact the ability of future Investors and common shareholders and employees to see a return in the future. 

The liquidation multiple in any given investment can vary widely depending on a number of factors. These include the performance of the underlying company, the nature of the exit event, and the preferences of other investors and stakeholders involved in the deal. This means that there is no one standard liquidation multiple that applies across the board in venture capital and startup investing. However, for Angel and Seed investors it's not uncommon to see 1-2x liquidation multiple for the risks involved at such an early stage. 

### Participation Rights

The third step is to negotiate the participation rights, which determine whether the preferred stockholders participate in the distribution of any remaining proceeds beyond their liquidation preference. The two main types of liquidation participation are Non-Participating and Participating. 

### Non-Participating

Non-participating preference (also known as “straight preferred”) stockholders have the option to either receive an amount equal to the liquidation preference multiple or convert their preferred shares into common stock and participate in the liquidity event as though they were common shareholders. 

Suppose a VC invests USD 2m in your startup with a 2x non-participating liquidation preference, in exchange for a 25% ownership stake in your company. This means that in the event of a sale, the VC has the option to either exercise its liquidation preference to receive a guaranteed payout of USD 4m, or to convert its preferred shares into common equity to have proceeds distributed. 

If the company is sold for USD 6m, the VC can either exercise its liquidation preference and receive USD 4m, or convert its preferred shares into common equity and receive 25% of the USD 6m, which is USD 1.5m. In this case, the VC would likely exercise this liquidation preference, as it provides a higher payout than converting its preferred shares. 

However, if the company was sold for USD 16m, the investor would be indifferent between exercising the liquidation preference and converting the preferred shares since both options provide a payout of USD 4m. This is called the _**Conversion Threshold -- remember this word as it will be important later on**._ 

### Participating

In contrast to non-participating liquidation preferences, participating liquidation preferences allow investors to receive additional payouts after their liquidation preference has been satisfied, in proportion to their ownership. Double dipping. 

For example, suppose the VC invests USD 2m in your startup with a 2x participating liquidation preference, in exchange for a 30% ownership stake. If the company is sold for USD 6m, the VC is guaranteed to receive USD 4m as liquidation preference, and then an additional 30% of the remaining proceeds, which is USD 600k. This generates a total payout of USD 4.6m.

Since participating preferred holders are entitled to their liquidation preference payout and a proportional share of the remaining proceeds, they will always have a higher value per share than common shareholders. This can create misaligned incentives and result in smaller exit values for founders.

While participating liquidation preferences are less common than non-participating liquidation preferences, they can significantly impact the overall payout for investors and founders alike.

#### Participation Cap

Liquidation preferences were initially intended to protect investors, however, it can create unfair outcomes for entrepreneurs. To mitigate this, caps were introduced on the amount of committed capital to safeguard the entrepreneur's interests.

For example, if a VC commits USD 2m with a 1x participating liquidation preference on a 2x cap, it is entitled to a maximum payout of USD 4m (USD 2m liquidation preference + USD 2m in participation) if they don't convert. 

If the investor wants to receive a payout higher than the cap, they must convert fully to common shares. Remember that one word, **Conversion Threshold?** This introduces a conversion threshold for participating preferred shareholders that wouldn't otherwise exist.

The cap serves as a safeguard to ensure that participating liquidation preferences don't unfairly reduce the value of the common shares or incentivize investors to prioritize their own interests over those of the entrepreneur.

By setting a limit on the maximum payout, the cap ensures that the interests of investors and entrepreneurs remain more closely aligned. 

Overall, it's crucial to understand the implications of different liquidation preference structures because it impacts the overall payout for investors and entrepreneurs. By carefully modelling out the scenario and weighing the potential benefits and drawbacks of different payout options, investors and entrepreneurs can make more informed decisions.

This article was written and published by one of our Full Stack Modeller community members, [Marcus Lertkomolsuk](https://www.linkedin.com/in/marcuslertkomolsuk/)
.  

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fbreaking-down-liquidation-preferences)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fbreaking-down-liquidation-preferences)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fbreaking-down-liquidation-preferences)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter