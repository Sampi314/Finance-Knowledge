# The EOMONTH Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-eomonth-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20EOMONTH%20function.png)

How to use Excel's EOMONTH function
===================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

May 27, 2021 11:26:00 AM

_Returns the last day of the month after adding a specified number of months_

What does Excel's EOMONTH function do?
--------------------------------------

The EOMONTH Function is one of Excel's Date/Time functions.

The EOMONTH function returns the date serial number for the last day of the month for the current month plus or minus the number of months you have specified.

In financial modelling the EOMONTH function is often used to switch dates between the start of the month and end of the month and to move from one month to the next.

In data analytics and reporting we often use EOMONTH to tag a row with the period or month end date.

#### Here's a simple example

Let's take a look at a simple example of the EOMONTH function.

We would like to know the date that is the end of the month one month after 22nd January 2020.

#### \=EOMONTH(B1, B2)

![EOMONTH 1](https://www.fullstackmodeller.com/hs-fs/hubfs/EOMONTH%201.png?width=1200&name=EOMONTH%201.png)

#### What does that mean in plain English?

Give me the date of the last day of the month one month from 22/01/2020. Calculated taking 22/01/2020, adding one month and then returning the last day of that month.

#### How do I write a formula using the EOMONTH function?

#### \=EOMONTH(Start Date, Months)

Start Date – The date that you wish to reference.

Months – The number of months before (-ve) or after (+ve) the start date.

#### What to consider when using the EOMONTH function in your financial model

*   Enter a positive month number to increase the months, or negative to decrease the months.
*   Enter 0 in months to return the end of the month selected. 
*   You can increase by a whole year by entering 12 in months.
*   To find the first day of the month enter -1 for months and then add 1 after the function. E.g. EOMONTH(B1,-1) +1 would return 01/01/2020 in our example above.
*   Use EDATE to if you just need to move a date forward or backwards a month without needing the last day of that month.

Read more about the EOMONTH function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-eomonth-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-eomonth-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-eomonth-function)
    

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