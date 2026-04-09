# The SUMIFS Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-sumifs-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20SUMIFS%20Function.png)

How to use Excel's SUMIFS Function
==================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Oct 22, 2021 12:26:00 PM

_Sum rows that meet specifc criteria_

What does Excel's SUMIFS function do?
-------------------------------------

The SUMIFS function is one of Excel's maths and trig functions.

The SUMIFS function returns the total value for rows in a dataset that meet the criteria that have been defined.

SUMIFS is an extremely useful function for obtaining the values to use in your reports.

### Here's a simple example

Let's take a look at a simple example of the SUMIFS function.

We would like to sum up the total quanity sold for three different sets of criteria:

![Excel SUMIFS function](https://www.fullstackmodeller.com/hs-fs/hubfs/ezgif.com-gif-maker.gif?width=2250&name=ezgif.com-gif-maker.gif)

### What does that mean in plain English?

1.  Sum up the quantity sold for any row that has “Chicken Pies” in the product range.
2.  Sum up the quantity sold for any row that has “January” in the month range.
3.  Sum up the quantity sold for any row that has “Chicken Pies” in the product range and has “January” in the month range.

### How do I write a formula using the SUMIFS function?

###### \=SUMIFS(sum range, criteria range 1, criteria 1, criteria range 2, criteria 2, ... )

*   sum range – What to sum up.
*   criteria range 1– The first range to look in.
*   criteria 1 – What to look for in criteria range 1.

### What to consider when using the SUMIFS function in your financial model

*   You can specify up to 127 criteria pairs.
*   The criteria range must contain the same number of rows as the sum range.
*   Use absolute cell references if you plan to copy the formula to other cells.
*   SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?).
*   Consider using Pivot Tables if you are performing one-off analysis.
*   There are also COUNTIFS, AVERAGEIFS, MAXIFS and MINIFS functions.

Read more about the SUMIFS function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b?ns=excel&version=90&syslcid=1033&uilcid=1033&appver=zxl900&helpid=xlmain11.chm60530&ui=en-us&rs=en-us&ad=us)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-sumifs-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-sumifs-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-sumifs-function)
    

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