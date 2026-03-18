# The TEXTJOIN Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-textjoin-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTJOIN%20Function.png)

How to use Excel's TEXTJOIN Function
====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 26, 2022 3:37:00 PM

_Concatenates values together from cells or ranges of cells  
_

What does Excel's TEXTJOIN function do?
---------------------------------------

The TEXTJOIN function is one of Excel's text functions.

The TEXTJOIN function concatenates (or joins) values together from cells or ranges of cell. 

This function is a great improvement on the CONCAT and CONCATENATE functions as it allows you to include a delimiter and to choose whether or not to ignore empty cells.

### Here's a simple example

Let's take a look at a simple example of the TEXTJOIN function.

We would like to concatenate the three words "Full", "Stack" and "Modeller" together from the range of cells A1 to A3 and insert a space delimiter between each word.  

![TEXTJOIN](https://www.fullstackmodeller.com/hs-fs/hubfs/TEXTJOIN.gif?width=2004&name=TEXTJOIN.gif)

#### \=TEXTJOIN(" ",,A1:A3)

#### What does that mean in plain English?

Join the three words "Full", "Stack" and "Modeller" together from the range of cells A1 to A3 and insert a space (delimiter) between each word. Ignore empty cells.

Note that the second arguement "ignore\_empty" is left blank. As the function defaults ot TRUE this will ignore any empty cells. The function could also have been written as: =TEXTJOIN(" ",TRUE,A1:A3)

#### How do I write a formula using the TEXTJOIN function?

#### \=TEXTJOIN(delimiter, ignore\_empty, text1, \[text2\], ...)

Delimiter – Seperator between each value (space, comma, hyphon)

Ignore empty – Ignore empty cells or not (default is to ignore)

text1 – The first value or range of values to join

#### What to consider when using the TEXTJOIN function in your  model

*   The TEXTJOIN function was introduced in 2019, so be aware of compatibility issues for users of previous Excel versions.

Read more about the TEXTJOIN function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textjoin-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textjoin-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textjoin-function)
    

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