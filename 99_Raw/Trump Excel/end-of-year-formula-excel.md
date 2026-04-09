# Get End of Year Date in Excel (Easy Formula)

**Source:** https://trumpexcel.com/end-of-year-formula-excel

---

[Skip to content](https://trumpexcel.com/end-of-year-formula-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/end-of-year-formula-excel/#below-title)

In this article, I will show you some simple Excel formulas you can use to get the end-of-year date in Excel.

Now if you’re wondering why you may even want that, and of course the end of the year date is going to always be 31st December of that year, here is the thing:

_**Dates work differently in Excel!**_

Every date in Excel is actually a serial number in the back-end. So when you want to get the date of the last day in a year, you actually need a serial number that represents that date.

In this article, I am going to give you formulas that will return that serial number that you can format to show that as a date.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/end-of-year-formula-excel/#)

Using DATE Function
-------------------

[DATE function](https://trumpexcel.com/excel-date-function/)
 allows you to construct your own dates and then use them in calculations.

Here is how to use it to get the last day of the current year or any specified year.

### Getting Last Day of the Current Year

To get the last day of the current year, you can use the below formula.

\=DATE(YEAR(TODAY()),12,31)

![Getting Last Day of the Current Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201370%20400'%3E%3C/svg%3E)

This formula uses the [TODAY function](https://trumpexcel.com/excel-today-function/)
 to get the current date, which is then used within the YEAR function to fetch the year of the current date.

This is then used within the DATE function which needs the year, month, and day value to construct the date:

*   _Year_ – This comes from YEAR(TODAY()) which will always give you the year value from the current date.
*   _Month_ – hardcoded as 12 as this will never change.
*   _Day_ – hardcoded as 31 as this will never change.

Note: Excel fetches the current date using the TODAY function, which relies on your system’s date and time settings. If your system’s settings are incorrect, then the result of the TODAY function will also be incorrect.

_You may see the actual serial number instead of the date as the result. All you need to do is [format the cell](https://trumpexcel.com/change-date-format-excel/)
 so that is shows the serial number as the date. You can do that by going to the Home tab and and selecting Long or Short date format from the formatting drop-down_

![Format numbers as dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202292%201874'%3E%3C/svg%3E)

### Getting Last Day of the Any Specified Year

If you want the last day of a specific year, say (2026 or 2027), you can use the below formula:

\=DATE(2026,12,31)

![Getting Last Day of the Any Specified Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201163%20420'%3E%3C/svg%3E)

In the above formula, I have hardcoded the year value, but if you have it in a cell reference, you can also use the cell reference. For example, if you have the year value in cell B1, then you can use the below formula.

\=DATE(B1,12,31)

Using the DAY 0 Trick in Formulas
---------------------------------

This is a clever little trick that uses a quirk in how the DATE function works.

If you use 0 for the day argument, Excel understands this as a request to roll back to the last day of the previous month.

You can use this to find the end of the year in two creative ways.

### Formula 1 – Reverting to Previous Year’s Last Day

\=DATE(YEAR(TODAY())+1,1,0)

![Day 0 Trick to get last day of year 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201377%20384'%3E%3C/svg%3E)

This formula is a bit of a mind-bender, but it’s simple when you break it down:

*   _YEAR(TODAY())+1_ gets the integer for next year (e.g., if it’s 2026, this returns 2027).
*   _1_ is for the month (January).
*   _0_ is for the day.

The formula asks Excel for “Day 0 of January of next year.”

Excel calculates this by finding January 1st of next year and then rolling back one day, which lands you on December 31st of the current year.

Also read: [How to Add Years to Date in Excel?](https://trumpexcel.com/add-years-to-date-excel/)

### Formula 2 – Reverting to Previous Months’s Last Day

\=DATE(YEAR(TODAY()),13,0)

![Day 0 Trick to get last day of year 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201345%20404'%3E%3C/svg%3E)

This is another variation of the same trick. The DATE function is smart enough to handle a month value greater than 12.

When you give it 13 for the month, it doesn’t error. It just rolls forward to the 1st month (January) of the next year.

So, just like the formula above, this is also asking for “Day 0 of Month 13” (which is next year’s January).

The result is the same: it rolls back to the last day of the previous month, which is December 31st of the current year.

Using the EOMOTH function
-------------------------

Excel has an EOMONTH function (which stands for End of Month), that returns a serial number of the last day of the month based on a start date and number of months you want to move forward or backward.

But there is no EOYEAR function in Excel.

However, we can tweak the EOMONTH function to give us the last date of the specified year.

Below is the formula that would give you the last day of the year for the current date.

\=EOMONTH(TODAY(), 12 - MONTH(TODAY()))

![EOMONTH to get last day of the year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201222%20443'%3E%3C/svg%3E)

Here is how this works:

*   _TODAY()_ – this gives the current date (which is automatically picked up from your computer date and time settings).
*   _12 – MONTH(TODAY())_ – this first calculates the month value from the current date and then subtracts it from 12, which gives us how many months are left till the end of the year. For example, if the current date is 15th of February, then this would give us 10
*   _\=EOMONTH(TODAY(), 12 – MONTH(TODAY()))_ – the EOM month function starts from the current date and then adds additional months that would take us to December, and then gives us the last date in December for the current year.

If you have a date in a cell that you want to use (instead of using the TODAY function), you can use the below formula (considering that the date is in cell B1).

\=EOMONTH(TODAY(), 12 - MONTH(TODAY()))

In this article I covered how to get the last day of the current year or any specified year using simple formulas.

I hope you found this article helpful.

**Other articles you may also like:**

*   [Calculate Fiscal Year from Date in Excel (Formulas)](https://trumpexcel.com/fiscal-year-excel/)
    
*   [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)
    
*   [Combine Date and Time in Excel (Easy Formula)](https://trumpexcel.com/combine-date-time-excel/)
    
*   [Get Day Name from Date in Excel (Easy Formulas)](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [Convert Month Name to Number in Excel](https://trumpexcel.com/convert-month-name-to-number-excel/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    
*   [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/end-of-year-formula-excel/#respond)

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