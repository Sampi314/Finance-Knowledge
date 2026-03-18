# Excel DAY Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-day-function

---

[Skip to content](https://trumpexcel.com/excel-day-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-day-function/#below-title)

Excel DAY Function (Examples + Video)
-------------------------------------

![Excel Day Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20327'%3E%3C/svg%3E)

### When to Use Excel DAY Function

Excel DAY function can be used when you want to get the day value (ranging between 1 to 31) from a specified date.

### What it Returns

It returns a value between 0 and 31 depending on the date used as the input. For example, for the month of February, it will return a day value between 0 and 29.

### Syntax

\=DAY(serial\_number)

### Input Arguments

*   **serial\_number:** It is the serial number of the date for which you want to get the day value. This could be the output from a function, a cell reference that contains a date value, or could be manually entered.

### Additional Notes

*   Apart from serial numbers, the DAY function would also work with dates entered as:
    *   A result of some other function.
        
    *   A date entered as text in the DAY function (in double-quotes).
    *   A date stored as text in a cell.
        
*   Excel can only handle dates starting from January 1, 1900 (for windows) and 1904 (for Mac).

Excel DAY Function – Examples
-----------------------------

Here are four examples of using the Excel DAY function.

### Example 1: Getting the Day value using a serial number

![Excel DAY Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20238'%3E%3C/svg%3E)

In the example above, the Excel DAY function takes 42736 as the input. 42736 is the serial number of the date January 1, 2017. Since it represents the first day of the month, the DATE function returns 1.

### Example 2: Getting the DAY value using Date in a Cell

![Excel DAY Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20227'%3E%3C/svg%3E)

In the above example, the DAY function takes the cell value from a cell and returns the day number of the month of that specified date. Note that if you use a date format that is not recognized by Excel, it returns a #VALUE! error.

### Example 3: Getting the DAY Value of the current date

![Excel DAY Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20432%20195'%3E%3C/svg%3E)

You can easily get the current day value by using the [TODAY function](https://trumpexcel.com/excel-today-function/)
 as the input. The TODAY function returns the current date, and the DAY function can use it to return the day value of that month.

In the example above, the TODAY function returns 11-04-2016 (which is the current date while writing this tutorial). DAY function takes TODAY value as the input as returns 11.

### Example 4: Getting the First Day of the Month

You can use the Excel DAY function to get the first day of the month of the specified date.

![Excel DAY Function - Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20110'%3E%3C/svg%3E)

In the example above, the day value for the date in A2 (15-03-2017) is 15. Since dates are stored as serial numbers in Excel, when we subtract the DAY value from this date and add 1 to it, it returns the first day of the month of the specified date.

Note that the dates in D2 and D3 are formatted as dates. It may happen that when you use this formula, you may get a serial number (for example, 42795 for March 1, 2017). You can then simply format it as a date.

The same logic can also be used to find the last day of the previous month. In that case, you can use the following formula (considering that the date is in cell A2):

\=A2-DAY(A2)

Excel DAY Function – VIDEO
--------------------------

**Other Useful Excel Functions:**

*   [Excel HOUR Function](https://trumpexcel.com/excel-hour-function/)
    : It can be used when you want to get the HOUR integer value from a specified time value. It returns a value between 0 (12:00 A.M.) and 23 (11:00 P.M.) depending on the time value used as the input
*   [Excel MINUTE Function](https://trumpexcel.com/excel-minute-function/)
    : It can be used when you want to get the MINUTE integer value from a specified time value. It returns a value between 0 and 59 depending on the time value used as the input.
*   [Excel NOW Function](https://trumpexcel.com/excel-now-function/)
    : It can be used to get the current date and time value.
*   [Excel SECOND Function](https://trumpexcel.com/excel-second-function/)
    : It can be used want to get the integer value of the seconds from a specified time value. It returns a value between 0 and 59 depending on the time value used as the input.

**You May Also Like the Following Excel Tutorials:**

*   [Creating a holiday calendar in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Calculate the Number of Days Between Two Dates](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [How to Get the First Day of the Month in Excel](https://trumpexcel.com/first-day-of-month-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-day-function/#respond)

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