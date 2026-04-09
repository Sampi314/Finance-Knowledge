# Fannie Mae Spreadsheet Error

**Source:** https://www.fullstackmodeller.com/blog/fannie-mae-spreadsheet-error

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Fannie%20Mae%20$1.2bn%20Restatement.png)

Fannie Mae $1.2bn Restatement
=============================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Mar 17, 2020 12:52:00 PM

Restatement of unrealised gains due to financial modelling errors.

Error Type: Incorrect calculation logic.

Reported on: October 2003

What happened?
--------------

Fannie Mae (the Federal National Mortgage Association) were forced to restate their unrealised gains by $1.2 billion after discovering  “honest mistakes" in one of their spreadsheet-based financial models.

Fannie Mae's share price fell from $73.10 to $2.25 after the spreadsheet error was announced.

### What caused the error?

The errors were caused by a financial modeller using the incorrect logic in a formula in the Excel spreadsheet being used to calculate the changes in the value of commitments the company had made to purchase mortgages or mortgage-backed securities.

The logic error related to "complicated calculations required in the implementation of FAS 149".

These errors were not picked up during the review and test phase of the build of the financial model, or before Fannie Mae issued their earning statement.

The Fannie Mae team did however unearth the mistakes during  their filing process. This lead to the restatement and public announcement of the error.

### How could the error have been avoided?

The error was one of accounting logic rather than a simple formula or input error.

Formula logic errors can be the most difficult to find during testing. The best way to manage formula logic risk is to detail out the logic for all critical formulae within the financial model's guide. This logic can then be more easily validated during the test phase.

This is a great example of where Excel's [LAMBDA](https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambda-turn-excel-formulas-into-custom-functions/ba-p/1925546)
 custom functions could be applied.

Creating a LAMBDA for the calculation in question would have enabled the calculation to be created and tested in isolation and then consistently applied in the financial model.

Read the article published by the New York Times [here](https://www.nytimes.com/2003/10/30/business/fannie-mae-corrects-mistakes-in-results.html)
.

Full Stack's Financial Modelling Errors Series
----------------------------------------------

See our complete financial modelling error series [here](https://www.fullstackmodeller.com/blog/financial-modelling-errors)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffannie-mae-spreadsheet-error)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffannie-mae-spreadsheet-error)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffannie-mae-spreadsheet-error)
    

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