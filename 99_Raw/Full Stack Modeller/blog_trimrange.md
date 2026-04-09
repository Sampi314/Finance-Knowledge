# TRIMRANGE

**Source:** https://www.fullstackmodeller.com/blog/trimrange

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/2-1.png)

Microsoft announce TRIMRANGE function
=====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 2, 2024 2:00:11 PM

A new Excel function designed to remove empty rows or columns from a selected range.

_Announced by Microsoft on 28th August 2024  
_

In this latest article in our Future of Excel series, I take a quick look at Excel's new TRIMRANGE function.  

Please note that this new function is currently only available to Beta Channel users running Version 2409 (Build 18020.2000) or later.

TRIMRANGE  

------------

The TRIMRANGE function removes empty rows from a selected range.  

In the example below from the Microsoft team, the TRIMRANGE function is being used to filter the  rows being considered in a full-column reference to only those that aren't empty. (in this case column A).

![TRIMRANGE function in Excel](https://www.fullstackmodeller.com/hs-fs/hubfs/gif1-v4.gif?width=1332&height=933&name=gif1-v4.gif)

\[Image courtesy of Microsoft Tech Community\]

The initial formula =LEN(A:A) is a full-column reference with the LEN function making use of the dynamic array engine to return results for all rows.

By inserting a TRIMRANGE after the LEN function the range of cells being considered and therefore returned has been limited to those that are not empty.

\=LEN(TRIMRANGE(A:A).

The Syntax of TRIMRANGE
-----------------------

**\=TRIMRANGE(range,\[trim\_rows\],\[trim\_cols\])**   

TRIMRANGE has three arguments, two of which are optional:

*   **range:** The range to be trimmed
*   **\[trim\_rows\]:** Which rows to be trimmed (default is to trim both leading and trailing blank rows)
*   **\[trim\_cols\]:** Which columns to be trimmed (default is to trim both leading and trailing blank columns)

Both the trim\_rows and trim\_cols arguments have the following options:

*   0 - None  
      
    1 - Trims leading blanks  
      
    2 - Trims trailing blanks  
      
    3 - Trims both leading and trailing blanks (default) 

TRIM References
---------------

Interestingly the Microsoft Excel team have also developed something that they are calling "TRIM References".

TRIM References are a syntax shortcut to call the range trimming functionality without having to write the TRIMRANGE function within your formula.

The table below from Microsoft explains how these TRIM References can be used in the place of a full TRIMRANGE function:

![TRIM References in Excel](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-1.png?width=1971&height=600&name=image-png-1.png)

\[Image courtesy of Microsoft Tech Community\]

In the example below =LEN(A:.A) is used to trim trailing blank rows from the whole column.

![gif2-v5](https://www.fullstackmodeller.com/hs-fs/hubfs/gif2-v5.gif?width=1332&height=933&name=gif2-v5.gif)

\[Image courtesy of Microsoft Tech Community\]

My thoughts
-----------

On initial view, it appears that the TRIMRANGE function has been brought out to address the performance issues that come with full-column references in Excel.

This new functionality will enable users to select a whole column as long as they pass it through TRIMRANGE first.

This seems like a crazy approach to me.

Just stop using full-column references!

Holding your data in Excel Tables is a much neater solution to this problem, and has so many other benefits too. [Find out more about Excel Tables in my article here](https://www.fullstackmodeller.com/blog/use-excel-tables)
.

I'm also a little concerned about the introduction of full stops within a function next to the colon.

All-in-all, the TRIMRANGE function seems like a solution to a problem that no one has (or shouldn't have if they don't use full-column references).

Application within LAMBDAs
--------------------------

According to Joe McDaid, Principle PM Manager at Microsoft, "TRIMRANGE is also a great new tool for optimizing the performance of lambda functions that operate on ranges. It allows lambda authors to more tightly scope ranges, which can reduce the number of necessary computations."

So maybe this is where the real magic of TRIMRANGE will lie. I look forward to seeing how this usage of the function evolves once it comes out in the main Excel versions.

### Release date

The feature is currently available in the Beta channel version of Excel.

### Our Future of Excel series  

This series of articles focuses on new features recently released or soon to be released in Excel. See the announcement from the [MICROSOFT TECH COMMUNITY](https://techcommunity.microsoft.com/t5/excel-blog/announcing-trimrange-and-accompanying-trim-references/ba-p/4230202)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ftrimrange)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ftrimrange)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ftrimrange)
    

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