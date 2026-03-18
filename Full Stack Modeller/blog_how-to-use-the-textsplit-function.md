# The TEXTSPLITFunction

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-textsplit-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTSPLIT%20Function.png)

How to use Excel's TEXTSPLIT Function
=====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 29, 2022 3:40:00 PM

_Splits text out across rows and/or columns  
_

What does Excel's TEXTSPLIT function do?
----------------------------------------

The TEXTSPLIT function is one of Excel's text functions.

The TEXTSPLIT function works in the same way as the text-to-columns functionality in native Excel or split-by functionality in PowerQuery. It allows you to split values from a cell across rows and/or columns based on a delimiter.

The function makes use of Excel' dynamic array functionality to "spill" the results aross rows and columns.

TEXTSPLIT is a great improvement on using other text functions such as LEFT, RIGHT, MIDDLE etc to split text out from a cell.

### Here's a simple example

Let's take a look at a simple example of the TEXTSPLIT function.

We would like to split the three words in cell A1 out across three separate cells, firstly across columns and secondly down rows.  

 ![TEXTSPLIT Columns](https://www.fullstackmodeller.com/hs-fs/hubfs/TEXTSPLIT%20Columns.gif?width=2250&name=TEXTSPLIT%20Columns.gif)

#### \=TEXTSPLIT(A1," ")

![TEXTSPLIT Rows](https://www.fullstackmodeller.com/hs-fs/hubfs/TEXTSPLIT%20Rows.gif?width=2259&name=TEXTSPLIT%20Rows.gif)

#### \=TEXTSPLIT(A1,," ")

#### What does that mean in plain English?

Split the three words in cell A1 out across three separate cells, firstly across columns and secondly down rows.

#### Now lets look at a slightly more complicated example where we want to split by columns and rows  

We would like to split the three words in cell A1 out over both rows and columns. We will split across columns using a space delimiter " " and down rows using the hyphon "-" delimiter.  

![TEXTSPLIT Column and Row](https://www.fullstackmodeller.com/hs-fs/hubfs/TEXTSPLIT%20Column%20and%20Row.gif?width=2226&name=TEXTSPLIT%20Column%20and%20Row.gif)

#### \=TEXTSPLIT(A1," ","-")

#### How do I write a formula using the TEXTSPLIT function?

#### \=TEXTSPLIT(text,col\_delimiter,\[row\_delimiter\],\[ignore\_empty\], \[match\_mode\], \[pad\_with\])

text– The text to be split

col\_delimiter – What to split columns by

\[row\_delimiter\] – What to split rows by (optional)

\[ignore\_empty\] – Ignore empty values. TRUE = ignore, FALSE = preserve (default).

\[match\_mode\] – Case sensitive delimiter. TRUE = yes (default) , FALSE = no

\[pad\_with\] – The  value to pad with

#### What to consider when using the TEXTSPLIT function in your  model

*   The TEXTSPLIT function was introduced in 2019, so be aware of compatibility issues for users of previous Excel versions.

Read more about the TEXTSPLIT function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textsplit-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textsplit-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textsplit-function)
    

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