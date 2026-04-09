# New Text and Array Functions

**Source:** https://www.fullstackmodeller.com/blog/new-text-array-functions

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/New%20Text%20and%20Array%20Functions.png)

New Text and Array Functions
============================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Mar 17, 2022 1:00:00 PM

Microsoft announce new Text and Array functions for Excel

_Announced by Microsoft on 16th March 2022_

In this latest article in our Future of Excel series we look at the new Text and Array functions announced for Microsoft Excel.

An exciting day for all us Excel users as Microsoft announce 14 new functions. And some of them look like they are going to be really useful, simplifying the way we tackle data analysis and financial modelling challenges.

#### TEXTBEFORE

TEXTBEFORE returns text from a text string that occurs before a given character or string.

\=TEXTBEFORE(text,delimiter,\[instance\_num\], \[match\_mode\], \[match\_end\], \[if\_not\_found\])

For example: =TEXTBEFORE("New Excel function"," function") returns "New Excel"

####   
TEXTAFTER

TEXTAFTER returns text from a text string that occurs after a given character or string.

\=TEXTAFTER(text,delimiter,\[instance\_num\], \[match\_mode\], \[match\_end\], \[if\_not\_found\])

For example: =TEXTAFTER("New Excel function","New ") returns "Excel function"

####   
TEXTSPLIT

TEXTSPLIT splits a text string by using column and row delimiters. The TEXTSPLIT function works the same as text to column, but in a formula rather than through a wizard. It allows you to split across columns or down by rows.

\=TEXTSPLIT(text,col\_delimiter,\[row\_delimiter\],\[ignore\_empty\], \[match\_mode\], \[pad\_with\])

The ability to split text by formula across rows and columns is incredibly useful.

####   
VSTACK

VSTACK appends (combines) arrays vertically and in sequence to return a larger array.

\=VSTACK(array1,\[array2\],...)

####   
HSTACK

VSTACK appends (combines) arrays vertically and in sequence to return a larger array.

\=HSTACK(array1,\[array2\],...)

#### TOROW

TOROW returns the array (range of cell) in a single row.

\=TOROW(array, \[ignore\], \[scan\_by\_column\])

####   
TOCOL

TOCOL returns the array (range of cell) in a single column.

\=TOCOL(array, \[ignore\], \[scan\_by\_column\])

####   
WRAPROWS

WRAPROWS wraps the provided row or column of values by rows after a specified number of elements to form a new array.

\=WRAPROWS(vector, wrap\_count, \[pad\_with\])

####   
WRAPCOLS

WRAPCOLS wraps the provided row or column of values by columns after a specified number of elements to form a new array.

\=WRAPCOLS(vector, wrap\_count, \[pad\_with\])

####   
My thoughts

These are a great set of new Excel functions and a really useful addition to any data analyst's or financial modeller's toolkit.

The stand outs for me are TEXTSPLIT, TOROW and TOCOL. I can't wait for these functions to be in general Excel usage.

See more about these new Excel functions on the Microsoft Excel Tech blog [here](https://techcommunity.microsoft.com/t5/excel-blog/announcing-new-text-and-array-functions/ba-p/3186066)
.

### Release date

These functions are currently available to users running Beta Channel, Version 2203 (Build 15104.20004) or later on Windows and Version 16.60 (Build 22030400) or later on Mac.

They will be tested by the insider team and then released to all Excel users once finalised.

  

Our Future of Excel series  

-----------------------------

This series of articles focuses on new features soon to be released on Excel. This is based on announcements by the [Microsoft Office Insider](https://insider.office.com/en-gb/)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fnew-text-array-functions)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fnew-text-array-functions)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fnew-text-array-functions)
    

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