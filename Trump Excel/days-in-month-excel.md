# Get Total Number of Days in Month in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/days-in-month-excel

---

[Skip to content](https://trumpexcel.com/days-in-month-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/days-in-month-excel/#below-title)

When working with dates, sometimes you may need to know the total number of days in a given month.

This could be useful when working on project scheduling or payroll calculation, or even travel planning.

While you can easily figure out the total days in a given month, when doing it for a larger dataset, it would be best to use some simple Excel formulas that would give you the result instantly.

In this short tutorial, I will show you some easy formulas you can use to **calculate the total number of days in any given month** in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/days-in-month-excel/#)

Get Total Days In a Month Using EOMONTH & DAY Functions
-------------------------------------------------------

The easiest way to get the total number of days in a month is by using a combination of the DAY and EOMONTH functions.

Let me first show you how it works, and then I’ll explain the formula.

Below I have a data set where I have some dates in column A, and I want to find out the number of days in the month to which that date belongs.

![dataset to calculate days in month in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20310'%3E%3C/svg%3E)

Here is the formula that will give me the total number of days in each month.

\=DAY(EOMONTH(A2,0))

Enter this formula in cell B2 and copy it for all the remaining cells in the column.

![EOMONTH and DAY functions to calculate total days in month in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20357'%3E%3C/svg%3E)

Now let me quickly explain how this formula works.

The EOMONTH function (where EO stands for End Of) takes the date in the cell as the input and then gives the last day of that month. Note that the second argument in the EOMONTH function needs to be 0 as we need the [last day date](https://trumpexcel.com/end-of-year-formula-excel/)
 for the same month.

For example, when the date is 17-Jun-2024, the EOMONTH function would give us 30-Jun-2024 (which is the last day of June 2024).

The [DAY function](https://trumpexcel.com/excel-day-function/)
 then gives us the day value of the last date of the month, which would essentially be the total number of days in the month.

**Note**: In case you want to get the total number of days in the previous month or the next month, you can change the second argument of the EOMONTH function (use -1 for the previous month and 1 for the next month)

Also read: [How to Get the First Day of the Month in Excel](https://trumpexcel.com/first-day-of-month-excel/)

Get Total Days In a Month Using EOMONTH Function
------------------------------------------------

Another fast way to get the total number of days In a month is by using two EOMONTH functions with the subtraction operator.

In this case, we calculate the last day of the month for the given month and the previous month and then simply subtract the two values.

This works as date values are stored as numeric values in the back end.

Let me demonstrate how it works by using an example.

Below I have a data set where I have the dates in column A, and I want to get the total number of days in each month.

![dataset to calculate days in month in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20310'%3E%3C/svg%3E)

Here is the formula to do this:

\=EOMONTH(A2,0)-EOMONTH(A2,-1)

Enter this formula in cell B2 and copy it for all the remaining cells in the column.

![EOMONTH formula to get total days in a month in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20372'%3E%3C/svg%3E)

The above formula uses two EOMONTH functions. The first EOMONTh function uses 0 as the second argument, which gives us the date of the last day of the same month as the date in cell A2.

And the second EOMONTH function uses -1 as the second argument, which gives us the date of the last day of the previous month.

And since the dates are stored as serial numbers in the back end, when we subtract these two EOMONTH function results, we get the total number of days in the month.

Also read: [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)

Get Total Days In the Current Month
-----------------------------------

In the above examples, I had a set of dates in a column, and I wanted to calculate the total number of days for the month for each date.

Now let me show you a formula that would give you the total number of days in the current month (where the current month value would be automatically picked up from your system settings)

Here is the formula:

\=DAY(EOMONTH(TODAY(),0))

![Formula for Total days in current month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20142'%3E%3C/svg%3E)

This formula uses the [TODAY function](https://trumpexcel.com/excel-today-function/)
 to get the current date, and then the EOMONTH function is used to get the last date of the current month.

The result of the EOMONTH function is then used by the DAY function to get the total number of days in the current month.

Note that the TODAY [function is volatile](https://trumpexcel.com/excel-volatile-formulas/)
 and would automatically recalculate to show the current date. This formula would dynamically update based on the current date value.

Also read: [Calculate Fiscal Year from Date in Excel](https://trumpexcel.com/fiscal-year-excel/)

Get Total Days When You Have Month Name Only
--------------------------------------------

In this section, I will show you how to calculate the total number of days in the month when you only have the month’s name.

Below I have the data set where I have the month name in column A, and I want to know how many days are there in each month.

![Month names to get total days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20311'%3E%3C/svg%3E)

Since the month name is a [text string](https://trumpexcel.com/count-cells-that-contain-text/)
, we will first have to construct a date out of it so that we can get the serial number for the date, and then use that date serial number to calculate the total number of days in that month.

Below is the formula that will do this:

\=DAY(EOMONTH(DATEVALUE("01-"&A2&"-"&YEAR(TODAY())),0))

![Formula to get total days in month using month name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20385'%3E%3C/svg%3E)

Let me quickly explain how this formula works.

Since we only have the month name, we have used “01-“&A2&”-“&YEAR(TODAY())) to first construct a [date in a format](https://trumpexcel.com/change-date-format-excel/)
 that Excel recognizes as a proper date.

In our example, this part of the formula would give us “01-January-2023” in cell B2.

Since this is still a text string, I have used the [DATEVALUE function](https://trumpexcel.com/excel-datevalue-function/)
 to get the corresponding serial number for this date.

Once I have the serial number, I used EOMONTH to get the last day of the month and then the DAY function to get the total number of days in that month.

Also read: [How to Get Month Name from Date in Excel](https://trumpexcel.com/get-month-name-from-date-excel/)

Total Days Left in the Month
----------------------------

In all the examples above, I have shown you how to get the total number of days in the month for each date.

But what if you want to know the total number of days left in the month after the given date? This can easily be done using the [DATEDIF function](https://trumpexcel.com/excel-datedif-function/)
.

Below I have a data set where I have some dates in column A, and I want to know the total number of remaining days in that month.

![Dataset to calculate days left in the month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20365'%3E%3C/svg%3E)

Here is the formula that will do this:

\=DATEDIF(A2,EOMONTH(A2,0),"d")

Enter this formula in cell B2 and copy it for all the remaining cells in the column.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20660%20425'%3E%3C/svg%3E)

DATEDIF function takes three arguments:

*   the start date – which is the date in column A
*   the end date – which we have calculated using the EOMONTH function so that it is the last day of the month
*   “d” – this is the code that tells the function to give us the total number of remaining days between the start and the end date.

So these are some of the formula methods you can use to quickly calculate the total number of days in any given month in Excel.

**Other Excel articles you may also like:**

*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [Calculate Number of Weeks Between Two Dates in Excel](https://trumpexcel.com/weeks-between-two-dates-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    
*   [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)
    
*   [Business Days Calculator](https://trumpexcel.com/calculator/business-days/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/days-in-month-excel/#respond)

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