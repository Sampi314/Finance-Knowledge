# Islandsbanki

**Source:** https://www.fullstackmodeller.com/blog/islandsbanki-spreadsheet-error

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Islandsbanki%20Under-prices%20Stake%20Sale.png)

Islandsbanki Under-prices Stake Sale
====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Nov 17, 2022 11:02:12 AM

450 million shares were undervalued.  

Error Type: Data formatting

Reported on: November 2022

What happened?
--------------

Iceland bank Islandsbanki sold off 22.5% (450 million) of its shares in March 2022. The National Audit Office discovered that the sales price of 117 kronur per share undervalued the shares based on the actual demand prices recorded.  

What caused the error?
----------------------

Islandsbanki used an Excel based financial model to collate and analyse the demand price data. The National Audit Office found issues with the formatting of some of the demand price data used in the analysis.

They specifically noted that some entries had “foreign commas or amounts defined as text”. These entries were excluded from the calculations by Excel as they would have been interpreted as text rather than numbers.

### How could the error have been avoided?

First up I'd like to be clear - this is not an "Excel error".

The error was caused by data quality issues that were not properly identified and managed by the team performing the analysis.

The good management of the quality of data feeding into any financial model is paramount. As the old adage goes "rubbish in, rubbish out".

Excel's handling of numbers that have been formatted as text is an issue that almost every Excel modeller will have experienced.  Excel has a built-in check for "numbers formatted as text or preceded by an apostrophe". Excel flags any such number with a green mark in the top left of the cell.

Using PowerQuery to process the data could have helped. As part of the ETL (Extract , Transform & Load) process through PowerQuery users are able to specify the format of each data field. The fields loaded into Excel will then be correctly formatted.

Ultimately though you have to ask the question if an Excel-based financial model is the right tool to use for such a business-critical exercise. Indeed the National Audit Office found that:

“A detailed analysis of the data, e.g. with the use of specially designed information systems for managing offers, could have provided a better overview of real demand and laid the foundation for a more accurate assessment of price formation,”

Read the article published by the Bloomberg [here](https://www.bloomberg.com/news/articles/2022-11-14/bungled-excel-sheet-hurts-profits-from-islandsbanki-sale)
.

Full Stack's Financial Modelling Errors Series
----------------------------------------------

See our complete financial modelling error series [here](https://www.fullstackmodeller.com/blog/financial-modelling-errors)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fislandsbanki-spreadsheet-error)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fislandsbanki-spreadsheet-error)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fislandsbanki-spreadsheet-error)
    

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