# COVID-19 Results Lost

**Source:** https://www.fullstackmodeller.com/blog/covid19-results-lost-excel

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/COVID-19%20Results%20Lost%20Due%20to%20Using%20Excel.png)

COVID-19 Results Lost Due to Using Excel
========================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Oct 6, 2020 11:38:00 AM

Nearly 16,000 Coronavirus cases went unreported in England.

Error Type: Data error; incorrect use of Excel.

Reported on: 5th October 2020

What happened?
--------------

Public Health England (PHE) misreported COVID-19 cases in England. Over a period of eight days 15,841 positive cases of COVID-19 were not reported or passed into the contact-tracing process.  

### What caused the error?

Public Health England chose Excel as the tool to collate csv files containing the results from the companies carrying out the COVID tests. The process was designed to pull the csv files automatically into Excel, collate them and then upload them into the central system.

Now, whilst it does seem pretty crazy to choose Excel to do this for such a vital process, anyone who has worked in data will know just how common this is.

The real problem came about because the developers chose to use the .xls file format rather than the newer .xlsx file format. The old (pre 2007) .xls Excel format is limited to 65,000 rows, whilst the more recent .xlsx format can handle over a million.

The consequence of this is that as the csv files were collated they capped out at 65,000 rows, with any rows in excess of this being lost into the ether.

#### How could the error have been avoided?

When designing any process, and even more so for a process of national importance, developers should assess the tools available to them a choose the right software for the job.

In this case its fair to say Excel was the wrong choice, and certainly the pre 2007 version.

Read the article published by the BBC [here](https://www.bbc.co.uk/news/technology-54423988)
.

Full Stack's Financial Modelling Errors Series
----------------------------------------------

See our complete financial modelling error series [here](https://www.fullstackmodeller.com/blog/financial-modelling-errors)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcovid19-results-lost-excel)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcovid19-results-lost-excel)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcovid19-results-lost-excel)
    

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