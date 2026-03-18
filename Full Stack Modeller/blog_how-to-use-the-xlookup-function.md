# The XLOOKUP Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-xlookup-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20XLOOKUP%20Function.png)

How to use Excel's XLOOKUP Function
===================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Jul 30, 2021 12:34:00 PM

_Looks up values from another table_

What does Excel's XLOOKUP function do?
--------------------------------------

The XLOOKUP function is one of Excel's lookup and reference functions.

In modelling we use the XLOOKUP function to map data from one table into another based on a unique reference.

XLOOKUP is a much improved version of existing lookup methods such as VLOOKUP, HLOOKUP and INDEX MATCH.

The function includes an optional argument of what to return if no match is found. This removes the need for separate error management functions.

### Here's a simple example

Let's take a look at a simple example of the XLOOKUP function.

We have a table of products and their prices.

In cell B7 we would like to return the price of the product that is entered in cell A7.

We would write the formula using XLOOKUP as follows:

#### \=XLOOKUP(A7, A2:A5, B2:B5, "Not Found")

![Excel XLOOKUP function](https://www.fullstackmodeller.com/hs-fs/hubfs/ezgif.com-gif-maker-xlookup.gif?width=2250&name=ezgif.com-gif-maker-xlookup.gif)

### What does that mean in plain English?

Return the price of Lamb Pies from the product table.

Let's take a closer look at the structure of the arguments in the formula:

  

**lookup** - We want to find the price for Lamb Pie. 

**lookup array** - We are looking for Lamb Pie in the range A2 to A5.

**return array** - The range B2 to B5 contains the product prices we want to choose from.

\[not found\] - Return the text "Not Found" if the lookup cannot be found in the lookup array

### How do I write a formula using the XLOOKUP function?

#### \= XLOOKUP (lookup, lookup\_array, return\_array, \[not\_found\], \[match\_mode\], \[search\_mode\])

lookup - The value that you want to match.

lookup\_array - The range of cells being searched through for the match value.

return\_array - The range of cells that you want to return a value from.

\[not\_found\] - Value to return if no match is found.

\[match\_mode\] - Defines how the match should be performed:1 for next lower, -1 for next higher, 0 for exact match and 2 for a wildcard match.

\[search\_mode\] - 1 for search from first (default), -1 for search from last,2 for binary search ascending, -2 for binary search descending.

### What to consider when using the XLOOKUP function in your financial model

*   The function includes an optional argument of what to return if no match is found. This removes the need for separate error management functions.
*   As with other reference functions, we are able to choose an exact or approximate match using the match mode argument.
*   XLOOKUP also includes the additional feature of defining whether the search is performed top to bottom or bottom to top using the search mode argument.
*   The function can take advantage of the dynamic array engine, returning multiple entries for one formula.
*   The XLOOKUP function only works for Office 365 users. This raises a significant compatibility risk.

Read more about the XLOOKUP function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-xlookup-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-xlookup-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-xlookup-function)
    

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