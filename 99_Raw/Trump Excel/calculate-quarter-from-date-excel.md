# Calculate Quarter from Date in Excel (Easy Formula)

**Source:** https://trumpexcel.com/calculate-quarter-from-date-excel

---

[Skip to content](https://trumpexcel.com/calculate-quarter-from-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-quarter-from-date-excel/#below-title)

I was recently working on a project where I had dates in Excel and I had to find out what quarter of the year it was based on the date.

For the purpose of this tutorial, let’s consider the following:

*   Quarter 1 – Jan, Feb, and Mar
*   Quarter 2 – Apr, May, and Jun
*   Quarter 3 – July, Aug, and Sep
*   Quarter 4 – Oct, Nov, and Dec

In case you’re working with financial data where the quarter starts from April, then you can adjust the formulas accordingly (also covered later in this tutorial).

Now let’s see how to use simple formulas to find out the quarter from the date.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-quarter-from-date-excel/#)

Find Quarter From Date in Excel (Calendar Year)
-----------------------------------------------

Suppose you have the data set as shown below and you want to calculate the Quarter number for each date.

![Data with dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20284'%3E%3C/svg%3E)

Below is the formula to do that:

\=ROUNDUP(MONTH(A2)/3,0)

![Calculate quarter value from date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20506'%3E%3C/svg%3E)

The above formula uses the MONTH function to get the month value for each date. The result of this would be 1 for January, 2 for February, 3 for March, and so on.

This month number is divided by 3 so that for all the months in Quarter 1, we get a value less than or equal to 1, and for all the months in Quarter 2, we get a value that is greater than 1 and less than or equal to 2, and so no.

And then ROUNDUP function is used so that we get the same quarter value for all the months in that quarter.

Quite straightforward!

Find Quarter From Date in Excel (Financial/Accounting Year)
-----------------------------------------------------------

In accounting and financial analysis, Quarter 1 begins and April and Quarter 4 ends in March.

In such a case, we need to adjust our formula to get the correct result.

Below is the formula that will give the correct quarter value for dates in a financial year:

\=IF(ROUNDUP(MONTH(A2)/3,0)-1=0,4,ROUNDUP(MONTH(A2)/3,0)-1)

![Calculate quarter value from date in a fiscal year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20506'%3E%3C/svg%3E)

In this formula, I have used the same ROUNDUP function (that I used in the previous example to calculate the quarter for a calendar year), and subtracted 1 from it.

It gives the right result for all the quarters except quarter 4 (where it would give 0 instead of 4).

And to fix this simple issue I use the [IF formula](https://trumpexcel.com/excel-if-function/)
 to check if the quarter value is 0 or not, and if it is 0, then I simply make the formula return 4 instead.

You can use the same logic to get the quarter value from the date in case your quarter starts from July or October.

So this is how you can use a simple formula to get the quarter value from a date in Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [Calculate Fiscal Year from Date in Excel](https://trumpexcel.com/fiscal-year-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-quarter-from-date-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK