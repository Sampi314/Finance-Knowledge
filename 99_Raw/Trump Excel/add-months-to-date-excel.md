# How to Add Months to Date in Excel (Easy Formula)

**Source:** https://trumpexcel.com/add-months-to-date-excel

---

[Skip to content](https://trumpexcel.com/add-months-to-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-months-to-date-excel/#below-title)

Sometimes, when working with dates, you may want to know the date after a specific number of months.

For example, you may want to know the date three months after a specific date.

Thankfully, Excel has an [in-built function](https://trumpexcel.com/excel-functions/)
 (**EDATE**) that does exactly this.

In this tutorial, I will show you how to use a simple formula to **add or subtract months to a date in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-months-to-date-excel/#)

Add Months to a Date
--------------------

Suppose you have a dataset as shown below and you want to add the given number of months in column B to the dates in column A.

![Data with Start date and months to add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20561%20247'%3E%3C/svg%3E)

This can be done using the **EDATE** function.

Below is the syntax of the EDATE function:

\=EDATE(start\_date, months)

*   **start\_date** – the date for which you want to get a certain number of months before or after it
*   **months** – the number of months before or after the start date. In case that you want to subtract months, you need to enter a negative number, since the function is by default adding months to a date.

In our example, we want to add 5 months (cell B2) to May 31, 2021 (A2) and get the result in cell C2.

The formula in C2 looks like:

\=EDATE(A2, B2)

![EDATE formula to add months to date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20561%20296'%3E%3C/svg%3E)

The result is **October 31, 2021**, as this is a date 5 months after May 31, 2021.

Note that you can use the same formula to add months as well as subtract months from any given date.

In our example, we have a couple of month values that are negative. When used in the formula, these will give you the date which is the specific number of months ago in the past.

Also, the formula will only consider the integer part of the second argument. So if enter 1.5 as the months to be added to the date, you will still get the date after one month (anything after the decimal is ignored).

_Note: The prerequisite of the function is that columns containing a start date (column B) and a result date (D) are formatted as dates._

Also read: [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)

Add Years to a Date
-------------------

Apart from adding months to a date, you can also use the EDATE function to add years.

Suppose you have a dataset as shown below where you want to add the number of years in column B to the dates in column A

![Data to add years to date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20582%20247'%3E%3C/svg%3E)

Below is the formula that will do this:

**\=EDATE(A2, B2\*12)**

![Formula to add years to date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20580%20302'%3E%3C/svg%3E)

The result in C2 is **May 31, 2022**, which is 1 year after May 31, 2021. As you can see, the parameter months is 12 (1 year \* 12 months).

Also, since we are multiplying the month’s value with 12, you can also use decimal numbers as years and it should still work in most cases. For example, if you want to know the date after 1.5 years, you can do that (as 1.5\*12 is 18, which is an integer).

This way, we can use the EDATE formula to also make the function to add/subtract years from a date.

So this is a simple formula method you can use to add months or years to a date in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [Combine Date and Time in Excel (Easy Formula)](https://trumpexcel.com/combine-date-time-excel/)
    
*   [How to Get Month Name from Date in Excel](https://trumpexcel.com/get-month-name-from-date-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Calculate Quarter from Date in Excel](https://trumpexcel.com/calculate-quarter-from-date-excel/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Calculate Years of Service in Excel (Easy Formulas)](https://trumpexcel.com/calculate-years-of-service-excel/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [How to Add Years to Date in Excel?](https://trumpexcel.com/add-years-to-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Add Months to Date in Excel (Easy Formula)”
----------------------------------------------------------------

1.  I learnt a new function today, thanks.
    
    [Reply](https://trumpexcel.com/add-months-to-date-excel/#comment-43054)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-months-to-date-excel/#respond)

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