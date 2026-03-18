# The TEXTAFTER Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-textafter-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTAFTER%20Function.png)

How to use Excel's TEXTAFTER Function
=====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 27, 2022 3:38:00 PM

_Returns text from a cell that occurs after a given delimiter_

What does Excel's TEXTAFTER function do?
----------------------------------------

The TEXTAFTERfunction is one of Excel's text functions.

TEXTAFTER returns the text from a text string that occurs after a given delimiter (character or string).

### Here's a simple example

Let's take a look at a simple example of the TEXTAFTER function.

We would like to return the text that comes after the first space.  

![TEXTAFTER](https://www.fullstackmodeller.com/hs-fs/hubfs/TEXTAFTER.gif?width=2226&name=TEXTAFTER.gif)  

#### \=TEXTAFTER(A1," ")

#### What does that mean in plain English?

Return the text that comes after the first space.

#### How do I write a formula using the TEXTAFTER function?

#### \=TEXTAFTER(text,delimiter,\[instance\_num\], \[match\_mode\], \[match\_end\], \[if\_not\_found\])

text – The text that you want to extract text from  

delimiter – The character that you want to extract text after

\[instance\_num\] – The instance of the delimiter you want to extract after. Defaul is 1. Use a negative number to start from the end.

\[match\_mode\]– Case sensitive delimiter. TRUE = yes (default) , FALSE = no

\[match\_end\]– Treat the end of the text string as the delimiter.

\[if\_not\_found\] – What to return if the delimiter provided is not found. By default, #N/A is returned

#### What to consider when using the TEXTAFTER function in your  model

*   The TEXTAFTER function was introduced in 2019, so be aware of compatibility issues for users of previous Excel versions.
*   Use a negative number in the instance\_num arguement to start from the end.

Read more about the TEXTAFTER function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/textbefore-function-d099c28a-dba8-448e-ac6c-f086d0fa1b29)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textafter-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textafter-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-textafter-function)
    

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