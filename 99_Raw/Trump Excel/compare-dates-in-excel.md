# How to Compare Dates in Excel (Greater/Less Than, Mismatches)

**Source:** https://trumpexcel.com/compare-dates-in-excel

---

[Skip to content](https://trumpexcel.com/compare-dates-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/compare-dates-in-excel/#below-title)

One area that often troubles Microsoft Excel users is working with dates.

This is mostly because dates can be formatted in many different ways in Excel.

So while you may see two dates in Excel and think those are the same, there is a possibility that these might be different values in the back end (or vice versa, you may think two cells have different dates, and it may be the same).

In this tutorial, I will show you a couple of techniques that you can use to compare dates in Èxcel.

This could be useful when you need to check whether the dates in two cells are the same or not, or if one date is greater than or less than the other date.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/compare-dates-in-excel/#)

How does Excel Stores Dates in the Cells?
-----------------------------------------

Before I get into how you can compare two dates in Excel, let me first explain how date and time values are stored in Excel.

This is important, so if you don’t know this already, don’t skip this section (I will keep it short).

Dates are stored as whole numbers in the backend in Excel, and time values are stored as decimal values.

The dates in Excel start from 01 Jan 1900, which means that the value 1, when formatted as a date, would show you 01-01-1900 as the date in the cell in Excel.

Similarly, 44562, would represent 01 Jan 2022 (which means that 44562 days have passed between 01 Jan 1900 and 01 Jan 2022).

Similarly, time is stored as decimal values, where 0.5 would represent 12 hours and 0.75 would represent 18 hours.

So if I have the value 44562.5 in a cell, this would represent 01 Jan 2022 at 12:00 PM.

In a nutshell, dates and time values are stored as numbers in the backend, that are formatted to show as dates and time. This allows users to use these dates and times in calculations.

This is also the reason that not all date formats are acceptable formats in Excel. For example, if you enter _Jan 01, 2022_ in a cell in Excel, this would be treated as a text string and not as a valid date format.

Comparing Dates in Excel
------------------------

Now that we have a better understanding of dates and time values are handled in the Excel backend, let’s see how to compare two dates in Excel.

### Check Whether the Dates are the Same or Not

Below I have a dataset where I have two sets of dates in two columns, and I want to check whether these dates are the same or not.

![Compare Dates dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20342'%3E%3C/svg%3E)

This can be done using a simple equal-to-operator.

\=A2=B2

![Formula to compare dates in same row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20389'%3E%3C/svg%3E)

The above formula would return TRUE if the compared dates are the same, and FALSE if they are not.

Since dates are stored as numeric values, when we use this formula, Excel simply checks whether the date numeric value is the same or not.

Comparing dates in Excel is just like comparing two numbers.

A few things important things you must know when comparing dates:

*   Dates can be in two different formats and yet be equal, as the backend numeric values of these dates are the same
*   Dates that look exactly the same can be different. In the above example, look at row #5 and #7. The date looks the same, but the result says FALSE. This happens when the date has a time part as well but it’s formatted to only show the date. In this case, the dates in column B also have some time added to it (but it doesn’t show in the cell).
*   In case you have a date entered as a string, you won’t be able to compare these (your dates needs to be in an acceptable date format)

Also read: [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)

### Compare Dates Using IF Formula (Greater Less/Less Than)

While a head-on comparison with an equal-to operator works fine, your comparison could be more meaningful when you use an [IF formula](https://trumpexcel.com/excel-if-function/)
.

Below, I have dates in two different columns, and I want to know whether the dates in column B occurred before or after the dates in column A.

![Dataset to compare dates with IF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20307'%3E%3C/svg%3E)

This will help me identify whether the report was submitted before or after the specified due date.

Below is the formula that will do this:

 =IF(C2<=B2,"In Time","Delayed")

![IF formula to compare dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20357'%3E%3C/svg%3E)

The above formula compares the two dates using the less than or equal to operator, and if the submission date is before the due date, it shows ‘In Time’, else it shows delayed.

You can do more with the IF formula (such as nesting multiple IF statements in the same formula).

Below is the formula that will show the text Delayed’ if the report is submitted 5 days after the due date, and it will show ‘Grace’ if the report is submitted within 5 days of the due date, and return ‘In-time’ if submitted before the due date (or the last day of submission)

\=IF(C2-B2<=0,"In Time",IF(C2-B2<=5,"Grace","Delayed"))

The above formula uses two IF formulas (called nested IF formulas), as we need to check for 3 conditions.

Note that I have subtracted the dates from each other, which is possible as dates are stored as whole numbers in the backend. So when I subtract one date from another, it gives me the total number of days between these two dates.

Also read: [Calculate Number Of Days Between Two Dates Excel](https://trumpexcel.com/number-of-days-between-two-dates/)

Compare Dates That Have Time Values
-----------------------------------

As I mentioned earlier, dates are stored as whole numbers, and time is stored as a decimal number in Excel.

Many times, people format their cells to only show the date and hide the time part.

Below is an example where I have the same values in both columns, but the dates in column B are formatted to only show the date part, so you don’t see the time part in it.

![Compare Dates dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20342'%3E%3C/svg%3E)

This can lead to confusion when comparing dates in Excel. For example, below I have a datset, and when I use the equal-to operator to compare the dates in the two columns, I get unexpected results.

![Formula to compare dates in same row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20389'%3E%3C/svg%3E)

In the above, I get a mismatch in cells C5 and C7, while it appears that the dates are the same.

In such a scenario, you can use the INT formula to make sure you’re comparing only the day part of the date and the time part is ignored.

Below is the formula that will give us the right result:

\=INT(A2)=INT(B2)

![Comparing Dates using the INT formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20391'%3E%3C/svg%3E)

The INT part of the formula makes sure that only the completed days are considered while comparing the dates, and the decimal part is ignored.

While this is an uncommon scenario, it is always a good idea to check the cell format when working with dates. I have often found that downloads from several databases that contain date and time values both have cells formatted to only show the date part.

Operators You Can Use When Comparing Dates in Excel
---------------------------------------------------

And finally, below are some operators you can use when comparing dates in Excel:

*   Equal to (**\=**)
*   Greater Than (**\>**)
*   Less Than (**<**)
*   Greater Than or Equal to (**\>=**)
*   Less Than or Equal to (**<=**)
*   Not Equal to (**<>**)

In this tutorial, I covered how to compare dates in Excel using simple operators and the IF function. I also covered how to handle comparing dates when you have the time value as a part of it.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Compare Two Excel Sheets (for differences)](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Compare Text in Excel (Easy Formulas)](https://trumpexcel.com/compare-text-excel/)
    
*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [Get Day Name from Date in Excel (Easy Formulas)](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Add Months to Date in Excel (Easy Formula)](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [Combine Date and Time in Excel (Easy Formula)](https://trumpexcel.com/combine-date-time-excel/)
    
*   [Highlight Dates Before Today in Excel](https://trumpexcel.com/highlight-dates-before-today-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/compare-dates-in-excel/#respond)

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