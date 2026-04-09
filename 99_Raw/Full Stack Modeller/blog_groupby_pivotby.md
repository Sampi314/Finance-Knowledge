# GROUPBY and PIVOTBY

**Source:** https://www.fullstackmodeller.com/blog/groupby_pivotby

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/2-1.png)

Microsoft announce GROUPBY and PIVOTBY functions
================================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Nov 18, 2023 2:46:01 PM

Two new mind-blowing Excel function are on the way

_Announced by Microsoft on 14th November 2023_

In this latest article in our Future of Excel series, we take a quick look at Excel's new GROUPBY and PIVOTBY functions.  

These two new functions are going to fundamentally change the way that we model in Excel. This is a huge development and will be a staple function in a modeller's toolkit going forward.

GROUPBY  

----------

The GROUPBY function brings the ability to group, or aggregate, data to Excel using formulae alone.

Let's be honest, this isn't exactly a new concept. In fact the ability to group data has been in Excel since 1993 with the arrival of Pivot Tables and has been part of PowerQuery since its launch in 2010.  

This is however the first time that this can be achieved in Excel using just one simple formula.

Here it is in action, grouping the data by category and returning the sales value for each unique category:

![Groupby - Simple](https://www.fullstackmodeller.com/hs-fs/hubfs/Groupby%20-%20Simple.gif?width=2532&height=720&name=Groupby%20-%20Simple.gif)

\[Image courtesy of Microsoft Tech Community\]

Note that the GROUPBY function uses Excel's Dynamic array engine to spill the results, with the formula just entered in one cell (G2).

In order to group your data in Excel using the GROUPBY function you will need three core arguments:

*   **row\_fields:** What to group rows by (eg Category)  
    
*   **values:** the numbers to aggregate (eg Sales)  
    
*   **function:** the function that you want to apply (eg Sum)

There also further optional arguments that enable both sorting and filtering. Here is the full function syntax for GROUPBY:

 GROUPBY(row\_fields,values,function,\[field\_headers\],\[total\_depth\],\[sort\_order\],\[filter\_array\])

 For more detail on the GROUPBY function visit the [Microsoft Tech Community](https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505)
.

**PIVOTBY  
**
--------------

The PIVOTBY function takes the GROUPBY function to another level by adding the ability to also group by column.  

Here it is in action, grouping the data by category and returning the sales value for each unique category but now also with the year across the columns:

![Pivotby - Simple](https://www.fullstackmodeller.com/hs-fs/hubfs/Pivotby%20-%20Simple.gif?width=2532&height=720&name=Pivotby%20-%20Simple.gif)

\[Image courtesy of Microsoft Tech Community\]

In order to group your data in Excel using the GROUPBY function you will need three core arguments:

*   **row\_fields:** What to group rows by (eg Category)  
    
*   **col\_fields:** What to group columns by (eg Year)
*   **values:** the numbers to aggregate (eg Sales)  
    
*   **function:** the function that you want to apply (eg Sum)

Like GROUPBY there also further optional arguments that enable both sorting and filtering. Here is the full function syntax for PIVOTBY:  
  
PIVOTBY(row\_fields,col\_fields,values,function,\[field\_headers\],\[row\_total\_depth\],\[row\_sort\_order\],\[col\_total\_depth\],  
         \[col\_sort\_order\],\[filter\_array\])   

For more detail on the PIVOTBY function visit the [MICROSOFT TECH COMMUNITY](https://support.microsoft.com/en-us/office/pivotby-function-de86516a-90ad-4ced-8522-3a25fac389cf)
.

Functions
---------

Both the GROUPBY and PIVOTBY functions offer these functions:

![Function List](https://www.fullstackmodeller.com/hs-fs/hubfs/Function%20List.png?width=1623&height=813&name=Function%20List.png)

\[Image courtesy of Microsoft Tech Community\]

My thoughts
-----------

Microsoft are really knocking it out of the park at the moment. There just seems to be a constant flow of really useful new features landing in Excel.

GROUPBY and PIVOTBY are likely to fundamentally change the way that we build models in the future. That might sound a bit extreme but there are so many real-life modelling applications for these two new Excel functions.

Could this spell the end of Pivot Tables?.

### Release date

The feature is currently available in the Beta channel version of Excel.

### Our Future of Excel series  

This series of articles focuses on new features recently released or soon to be released in Excel. See the announcement from the [MICROSOFT TECH COMMUNITY](https://techcommunity.microsoft.com/t5/excel-blog/new-aggregation-functions-groupby-and-pivotby/ba-p/3965765)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fgroupby_pivotby)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fgroupby_pivotby)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fgroupby_pivotby)
    

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