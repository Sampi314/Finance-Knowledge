# Excel | IMPORTTEXT IMPORTCSV

**Source:** https://www.fullstackmodeller.com/blog/excel-importtext-importcsv

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Microsoft%20Copilot.png)

New Import Functions
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Jan 15, 2026 5:00:00 PM

Today Microsoft announced two new import functions for Excel

Microsoft have just announced the [IMPORTTEXT and IMPORTCSV](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613)
 functions for Excel.  

In this article, I'll take a look at what these functions are and how I think we will be able to use them once they are released into the current channel.

**IMPORTTEXT**
--------------

The IMPORTTEXT function lets you import data from.txt, .csv, and .tsv files directly into a dynamic array in Excel.

The syntax is: =IMPORTTEXT(path,\[delimiter\],\[skip rows\],\[take rows\],\[encoding\],\[locale\])

![IMPORTTEXT New Demo](https://www.fullstackmodeller.com/hs-fs/hubfs/IMPORTTEXT%20New%20Demo.gif?width=1692&height=1269&name=IMPORTTEXT%20New%20Demo.gif)

Video from [Microsoft Insider Blog](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613)

**IMPORTCSV**
-------------

IMPORTCSV is a version of IMPORTTEXT, designed specifically for importing data from .csv files.

The syntax is: =IMPORTCSV(path,\[skip rows\],\[take rows\],\[encoding\],\[locale\])

![IMPORTCSV New Demo](https://www.fullstackmodeller.com/hs-fs/hubfs/IMPORTCSV%20New%20Demo.gif?width=1752&height=1314&name=IMPORTCSV%20New%20Demo.gif)

Video from [Microsoft Insider Blog](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-data-into-excel-with-the-new-import-functions/4485613)

How can we use these two new import functions in practice
---------------------------------------------------------

These two import functions will provide a new way to bring data into Excel. Being dynamic array functions, they will bring the data directly into the grid and spill the results.

We will then be able to use the skip rows and take rows parameters, along with other Excel functions like TAKE, DROP, CHOOSECOLS, CHOOSEROWS and FILTER to perform the required transformations. This will naturally result in fairly complex, nested formulas.

As a modeller you should always consider the balance of functionality, complexity and risk. The balance you strike will depend on the nature of the data that you are working with, the skill set of the users and your risk appetite.

How do these new import functions compare to PowerQuery?
--------------------------------------------------------

PowerQuery is a comprehensive ETL (Extract, Transform & Load) tool built into Excel. As such, it can work with a wide range of data sources and can perform powerful transformations. The final dataset can be loaded into an Excel Table, into a Pivot Table or can be added into the Data Model.

IMPORTTEXT and IMPORTCSV are much simpler tools, and being dynamic array functions, they will not be able to be imported into an Excel Table.

I am a strong advocate of modellers using both Excel Tables and PowerQuery to source, transform and store their data. I don't see these two functions changing that any time soon.

That said, I am looking forward to having a play to see if/how I can use them in my modelling in the future.

**When will IMPORTTEXT and IMPORTCSV be released?**
---------------------------------------------------

IMPORTTEXT and IMPORTCSV are currently in the Beta Channel (Build 18604.20002) or later. Microsoft haven't yet announced when they will come to the current channel.

The Future of Excel Series
--------------------------

This series of articles focuses on new features soon to be released on Excel. This is based on announcements by the [Microsoft Office Insider](https://insider.office.com/en-gb/)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-importtext-importcsv)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-importtext-importcsv)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-importtext-importcsv)
    

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