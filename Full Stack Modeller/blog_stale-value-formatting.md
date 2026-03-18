# Excel Stale Value Formatting

**Source:** https://www.fullstackmodeller.com/blog/stale-value-formatting

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Excel%20Stale%20Value%20Formatting.png)

Excel Stale Value Formatting
============================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Aug 9, 2023 4:52:00 PM

Microsoft announce new Stale Value Formatting for Excel

_Announced by Microsoft on 8th August 2023_

In this latest article in our Future of Excel series, we look at Excel's new Stale Value Formatting functionality.

### Manual or automatic calculation  

In Excel there are two main calculation options: manual calculation and automatic calculation. The default setting is automatic. This means that Excel will automatically recalculate all formulae whose input values (or "ingredients") have changed.

For most Excel users the default automatic calculation setting works just fine.

Financial Modellers, however, tend to use the manual calculation setting. This is because Financial Modellers like to see the impact of their changes on key outputs like profit, net assets, IRR or debt ratios. By switching the calculation setting to manual the modeller has total control over the moment the calculation happens, and they can ensure they are looking at their key outputs when they trigger the change.

Another reason for using the manual setting is to deal with bloated models that take a long time to calculate. Users can turn the calculation to manual and only trigger calculations when they are ready. I've seen many situations when the modeller triggers the calculation and then goes off to make a cup of coffee! ☕  

**How to change the calculation setting in Excel**

You can change the calculation setting in the Calculation Options area in the Formulas tab on the Excel Ribbon:

![Disable Stale Value](https://www.fullstackmodeller.com/hs-fs/hubfs/Disable%20Stale%20Value.png?width=1020&height=783&name=Disable%20Stale%20Value.png)

**How to trigger calculations manually in Excel**

There are four shortcuts for triggering a manual calculation in Excel:

**Shift + F9 -** This only calculates the sheet that you are on (the active sheet)

**F9 -** This calculates the cells that have changed since you last recalculated

**Ctrl + Alt + F9 -** This is a full recalculation - Recommended

**Shift + Ctrl + Alt + F9 -** This is also a full recalculation but in addition it forces a complete bebuild of the calculations in the background of Excel

**A few things to consider when using manual calculation**

The first time I found out about manual calculations was when my own models suddenly stopped calculating. Luckily I spotted it pretty quickly!

The reason for this is that the calculation mode is not set at the workbook level. It is at the application level. This means that if you change the setting from automatic to manual then all open workbooks will switch to manual.

Sounds okay, right? That is under your control after all.

It would be, however there are two further aspects of manual calculation that we need to consider: 1) when you save a workbook the calculation setting at the time that you save is held within the workbook; and 2) the calculation mode is changed based on the calculation setting of the first workbook that you open.

So what does that mean?

Let me talk you through what happened to me. A colleague shared a workbook with me that was saved with the calculation mode set to manual. I opened this workbook as my first workbook and then opened two of my own models. I then saved all three models and closed Excel. Both my models were now set to manual. When I opened one of them first they set the calculation mode to manual. Any subsequent model I opened was then switched to manual. Almost like a virus of manual settings spreading through my files! 🦠 😲

It was lucky that I spotted that the calculations weren't happening automatically. It's not obvious to spot.

Until now....

### Introducing Stale Value Formatting  

Not the greatest name in the world, but it's a welcome addition to Excel, and one that we have been waiting for for decades.  

With this new Stale Value Formatting change in Excel, cells whose input values have changed but have not been updated (because the model is in manual calculation mode) will now be formatted with a strikethrough:

![Updated vs Stale](https://www.fullstackmodeller.com/hs-fs/hubfs/Updated%20vs%20Stale.png?width=906&height=312&name=Updated%20vs%20Stale.png)

The setting can be managed through the Calculation Options area in the Formulas tab on the Ribbon:

![Disable Stale Value](https://www.fullstackmodeller.com/hs-fs/hubfs/Disable%20Stale%20Value.png?width=1020&height=783&name=Disable%20Stale%20Value.png)

Let's see it in action:

![Stale Formatting HiRes](https://www.fullstackmodeller.com/hs-fs/hubfs/Stale%20Formatting%20HiRes.gif?width=2340&height=1578&name=Stale%20Formatting%20HiRes.gif)

\[All images courtesy of Microsoft Tech Community\]

### My thoughts

This is a great addition from Microsoft. It is incredibly helpful to be able to see which cells have not recalculated. This new feature will undoubtedly reduce some of the risk of using the manual calculation setting in Excel.

My only reservation is the fact that the formatting being applied is a strikethrough and that it is not customisable by the user. It would be great to have this as style option linked to the workbook style.

It would also be helpful to be able to see a log of cells not calculated in the navigation pane for example, or in the Formula Auditing section.

I'd love to see Stale Value Formatting built into the GoTo Special functionality.

### Release date

The feature is currently available in the Beta channel version of Excel.

### Our Future of Excel series  

This series of articles focuses on new features recently released or soon to be released in Excel. See the announcement from the [Microsoft Tech Community](https://techcommunity.microsoft.com/t5/excel-blog/stale-value-formatting/ba-p/3887098)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fstale-value-formatting)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fstale-value-formatting)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fstale-value-formatting)
    

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