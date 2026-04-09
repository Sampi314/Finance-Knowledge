# How to Calculate Age in Excel using Formulas + FREE Calculator Template

**Source:** https://trumpexcel.com/calculate-age-in-excel

---

[Skip to content](https://trumpexcel.com/calculate-age-in-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-age-in-excel/#below-title)

**Watch Video – How to Calculate Age in Excel (in Years, Months, and Days)**

Using a combination of [Excel functions](https://trumpexcel.com/excel-functions/)
 and the date of birth, you can easily calculate age in Excel. You can either calculate the age till the current date or between the specified period of time.

The technique shown here can also be used in other situations such as calculating the duration of a project or the [tenure of the service](https://trumpexcel.com/calculate-years-of-service-excel/)
.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-age-in-excel/#)

How to Calculate Age in Excel
-----------------------------

In this tutorial, you’ll learn how to calculate age in Excel in:

*   The number of years elapsed till the specified date.
*   The number of Years, Months, and Days elapsed till the specified date.

You can also download the **[Excel Age Calculator Template](https://trumpexcel.com/wp-content/uploads/2016/03/Age-Calculator-Template.xlsx)
**.

### Calculate Age in Excel – Years Only

Suppose you have the date of birth in cell B1, and you want to calculate how many years have elapsed since that date, here is the formula that’ll give you the result:

\=DATEDIF(B1,TODAY(),"Y")

![How to Calculate Age in Excel - Datedif years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20177'%3E%3C/svg%3E)

If you have the current date (or the end date) in a cell, you can use the reference instead of the [TODAY](https://trumpexcel.com/excel-today-function/)
 function. For example, if you have the current date in cell B2, you can use the formula:

\=DATEDIF(B1,B2,"Y")

[DATEDIF function](https://trumpexcel.com/excel-datedif-function/)
 is provided for the compatibility with Lotus 1-2-3.

One of the things that you’ll notice when you use this function is that there is no IntelliSense available for this function. No tooltip appears when you use this function.

![How to Calculate Age in Excel - Datedif](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20162'%3E%3C/svg%3E)

This means that while you can use this function in Excel, you need to know the syntax and how many arguments this function takes.

If you’re interested in knowing more about DATEDIF function, read the content of the box below. If not, you can skip this and move to the next section.

Syntax of DATEDIF function:

\=DATEDIF(start\_date, end\_date, unit)

It takes 3 arguments:

*   _start\_date_: It’s a date that represents the starting date value of the period. It can be entered as text strings in double-quotes, as serial numbers, or as a result of some other function, such as DATE().
*   _end\_date_: It’s a date that represents the end date value of the period. It can be entered as text strings in double-quotes, as serial numbers, or as a result of some other function, such as DATE().
*   _unit_: This would determine what type of result you get from this function. There are six different output that you can get from the DATEDIF function, based on what unit you use. Here are the units that you can use:
    *   “Y” – returns the number of completed years in the specified time period.
    *   “M” – returns the number of completed months in the specified time period.
    *   “D” – returns the number of completed days in the specified period.
    *   “MD” – returns the number of days in the period, but doesn’t count the ones in the Years and Months that have been completed.
    *   “YM” – returns the number of months in the period, but doesn’t count the ones in the years that have been completed.
    *   “YD” – returns the number of days in the period, but doesn’t count the ones in the years that have been completed. 

You can also use the YEARFRAC function to calculate the age in Excel (in years) in the specified date range.

Here is the formula:

\=INT(YEARFRAC(B1,TODAY()))

![How to Calculate Age in Excel - YEARFRAC years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20579%20174'%3E%3C/svg%3E)

The YEARFRAC function returns the number of years between the two specified dates and then the [INT function](https://trumpexcel.com/excel-int-function/)
 returns only the integer part of the value.

_NOTE:_ It’s a good practice to use the DATE function to get the date value. It avoids any erroneous results that may occur when entering the date as text or any other format (which is not an acceptable date format).

Also read: [How To Calculate Time In Excel](https://trumpexcel.com/calculate-time-in-excel/)

### Calculate Age in Excel – Years, Months, & Days

Suppose you have the date of birth in cell A1, here are the formulas:

To get the year value:

\=DATEDIF(B1,TODAY(),"Y")

![How to Calculate Age in Excel - Datedif Year Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20219'%3E%3C/svg%3E)

To get the month value:

\=DATEDIF(B1,TODAY(),"YM")

![How to Calculate Age in Excel - Datedif Month Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20218'%3E%3C/svg%3E)

To get the day value:

\=DATEDIF(B1,TODAY(),"MD")

![How to Calculate Age in Excel - Datedif Day Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20218'%3E%3C/svg%3E)

Now that you know how to calculate the years, months and days, you can combine these three to get a text that says 26 Years, 2 Months, and 13 Days. Here is the formula that will get this done:

\=DATEDIF(B1,TODAY(),"Y")&" Years "&DATEDIF(B1,TODAY(),"YM")&" Months "&DATEDIF(B1,TODAY(),"MD")&" Days"

![How to Calculate Age in Excel - combined](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20147'%3E%3C/svg%3E)

Note that the TODAY function is [volatile](https://trumpexcel.com/excel-volatile-formulas/)
 and its value would change every day whenever you open the workbook or there is a change in it. If you want to keep the result as is, convert the [formula result to a static value](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

_**Download the Excel Age Calculator Template**_  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/03/Age-Calculator-Template.xlsx)

**Excel Functions Used:**

Here is a list of functions used in this tutorial:

*   DATEDIF() – This function calculates the number of days, months, and years between two specified dates.
*   TODAY() – It gives the current date value.
*   YEARFRAC() – It takes the start date and the end date and gives you the number of years that have passed between the two dates. For example, if someone’s date of birth is 01-01-1990, and the current date is 15-06-2016, the formula would return 26.455. Here the integer part represents the number of years completed, and the decimal part represents additional days that have passed after 26 years.
*   [DATE()](https://trumpexcel.com/excel-networkdays-function/)
     – It returns the date value when you specify the Year, Month, and Day value arguments.
*   [INT](https://trumpexcel.com/excel-int-function/)
    () – This returns the integer part of a value.

**You May Also Like the Following Excel Tutorials:**

*   [Free Excel Holiday Calendar Template](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Calculating Working Days between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Calculate Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to SUM values between two dates in Excel](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [Free Age Calculator](https://trumpexcel.com/calculator/age-years-months-days/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Calculate Age in Excel using Formulas + FREE Calculator Template”
---------------------------------------------------------------------------------------

1.  This is the first time I saw this calculator and stop watch in MS Excel.  
    Thank You
    
    [Reply](https://trumpexcel.com/calculate-age-in-excel/#comment-16000)
    
2.  thanks
    
    [Reply](https://trumpexcel.com/calculate-age-in-excel/#comment-12790)
    
3.  how to calculate number of months between two dates
    
    [Reply](https://trumpexcel.com/calculate-age-in-excel/#comment-10060)
    
4.  I have created video tutorial as well. [http://talkproductivity.xyz/datedif-function-to-calculate-age/](http://talkproductivity.xyz/datedif-function-to-calculate-age/)
      
    It’s the easiest way to calculate age or difference between two dates.
    
    [Reply](https://trumpexcel.com/calculate-age-in-excel/#comment-3251)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-age-in-excel/#respond)

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