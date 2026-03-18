# How to Get the First Day of the Month in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/first-day-of-month-excel

---

[Skip to content](https://trumpexcel.com/first-day-of-month-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/first-day-of-month-excel/#below-title)

Sometimes, you may need to know what’s the first day of the month based on a given date.

When there is no dedicated function to get the first day of a given month, you can easily use a workaround to find it.

In this Excel tutorial, I’ll show you some really simple formula that you can use to **get the first day of a month in Excel** based on a given date.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/first-day-of-month-excel/#)

Get the First Day of the Month Using EOMONTH
--------------------------------------------

EOMONTH Function gives you the last day of the month for a given date (hence called the end-of-month function).

But we don’t want the last day of the month – we want the first day.

To get the first of the month you need to tweak your EOMONTH formula a little.

Suppose you have a data set as shown below where you want to find the first day of the month for each of these given dates in column A.

![Dates Dataset to get the first day of the month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20278'%3E%3C/svg%3E)

_Note that these dates are in the MM/DD/YYYY format (the date format followed in the US). These may look different in your system based on your regional date setting._

Below is the formula to do that:

\=EOMONTH(A2,-1)+1

![EOMONTH formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20327'%3E%3C/svg%3E)

The above EOMONTH formula uses two arguments:

*   **Start Date**: the date from which Excel uses the month value and calculates the first day of the month
*   **Months**: The number of months before or after the start date. If I use 0, EOMONTH will give me the last day of the given month, and if I use 1, it will give me the last day of the next month.

Since I’ve used -1 as the second argument in the EOMONTH formula, it gives me the last day of the previous month (based on the date in cell A2).

And since I want the first day of the month (from the given date), I can simply add 1 to the EOMONTH result.

You can also use the same logic if you want the 10th day or any other day of the month. Just add that value instead of 1 in the formula.

Note that the EOMONTH function is available for Excel 2007 and later versions only.

Get the First Day of the Month Using DATE/DAY formula
-----------------------------------------------------

Dates are stored as numbers in Excel, which allows us to easily use it in calculations (such as addition/subtraction).

Now, if you want to get the first day of the month from a given date, you just need to use the day value in the date and bring it back to 1.

For example, if I have the date as 15th October 2020, to get the first day off this month, I need to subtract 14 days from this date.

Now let’s see how to translate this logic into an Excel formula.

Suppose I have a data set as shown below where I have the dates in column A and I want to get the first day of the month for each of these dates.

![Dates Dataset to get the first day of the month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20278'%3E%3C/svg%3E)

Below is the formula that will do that:

\=A2-DAY(A2)+1

![DAY formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20329'%3E%3C/svg%3E)

The above formula uses the date in cell A2 (which is stored as a serial number in the back and in Excel) and subtracts the day value of the same date (which is given by the [DAY formula](https://trumpexcel.com/excel-day-function/)
).

The above formula gives us the last day of the previous month, so 1 is added because we want the first day of the month from the given date.

Also read: [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)

Get the First Monday of the Month
---------------------------------

It’s fairly straightforward to get the first day of the month, it’s likely tricky to get the first Monday of the month (or any other first weekday of the month).

While we know that this would be somewhere at the beginning of the month, to get the exact date, we need to find out what day it is on the first day of the month and then use it to get the first Monday.

The purpose of this tutorial I will consider Monday to be the first weekday (that you can use the method shown here to find out the first occurrence of any day of the week)

Let me take an example of September 2020 where the first day of the month is a Tuesday in the first Monday is on 8 September 2020.

Below is the formula that will give me the first Monday in September 2020

\=(EOMONTH(DATE(2020,7,1),-1)+1)+(MOD(8-WEEKDAY(EOMONTH(DATE(2020,7,1),-1)+1,2),7))

Note that I have hardcoded the date using the [DATE function](https://trumpexcel.com/excel-date-function/)
. You can also use a cell reference that has a date in this case. So instead of DATE(2020,7,1), you can use the cell reference (such as A2) that has the date.

Now let me explain how this formula works!

The first part of the formula (which is the EOMONTH formula) gives us the first day of the month for the given date.

The second part of the formula uses the [WEEKDAY function](https://trumpexcel.com/excel-weekday-function/)
 to analyze this first day of the month. If it is already a Monday, then the entire MOD formula returns 0 and we would be left with the first day itself.

But if the first day of the month is not a Monday, then the [MOD formula](https://trumpexcel.com/excel-mod-function/)
 would give us the total number of days that we should add to this date to get the first Monday of the month.

For example, for September 2020, the first day of the month is a Tuesday. In this case, the MOD function gives us 6, which when we add to the EOMONTH result gives us 7th September 2020 as the first Monday of the month.

In this example, I have shown you how to find the first Monday of any month, but you can use the same formula to find any day.

For example, if you want to find the first Saturday of any month you can tweak the formula as shown below:

\=(EOMONTH(DATE(2020,9,1),-1)+1)+(MOD(8-WEEKDAY(EOMONTH(DATE(2020,9,1),-1)+1,16),7))

The only change I have made is the second argument of the WEEKDAY formula.

So this is how you can use formulas in excel to find out the first day of the month or the first Monday (or any other weekday) of the month.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How to Get Month Name from Date in Excel](https://trumpexcel.com/get-month-name-from-date-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/first-day-of-month-excel/#respond)

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