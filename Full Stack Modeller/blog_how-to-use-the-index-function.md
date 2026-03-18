# The INDEX Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-index-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20INDEX%20Function.png)

How to use Excel's INDEX Function
=================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Jul 23, 2021 12:20:00 PM

_Returns a value from a range based on the position specified_

What does Excel's INDEX function do?
------------------------------------

The INDEX function is one of Excel's lookup and reference functions.

In financial modelling we use the INDEX function to return a value from a range based on the position specified. In scenario modelling we can use INDEX to pull the values for the selected scenario.

INDEX is often combined with the MATCH function to to map data from one table into another based on a unique reference.

#### Here's a simple example

Let's take a look at a simple example of the INDEX function.

We have a set of numbers in the cell range A2 to F2.

We would like to return the forth item in that range.

We would write the formula using INDEX as follows:

#### \=INDEX(A2:F2,4)

![Excel INDEX function](https://www.fullstackmodeller.com/hs-fs/hubfs/ezgif.com-gif-maker-index.gif?width=2250&name=ezgif.com-gif-maker-index.gif)

#### What does that mean in plain English?

Return the value in the fourth position in the range A2 to F2.

#### How do I write a formula using the INDEX function?

#### \=INDEX(array, row number, \[column number\])

array – The range of cells that you want to analyse.

row number – The number of the row that you want to return a value for. This is the number of the item in a list arranged vertically.

\[column number\] – The number of the column that you want to return a value for. This is the number of the item in a list arranged horizontally.

#### What to consider when using the INDEX function in your financial model

*   Avoid using full column and row references as this is very inefficient.
*   Combine with MATCH for a clear, flexible and efficient lookup formula.
*   INDEX MATCH can often be used instead of complex nested IF functions.
*   The [XLOOKUP](https://www.fullstackmodeller.com/blog/how-to-use-the-xlookup-function)
     function can be used in place of INDEX MATCH

Read more about the INDEX function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-index-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-index-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-index-function)
    

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