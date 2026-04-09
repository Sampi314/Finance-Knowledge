# Excel MINUTE Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-minute-function

---

[Skip to content](https://trumpexcel.com/excel-minute-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-minute-function/#below-title)

Excel MINUTE Function – Overview
--------------------------------

Excel MINUTE function can be used when you want to get the MINUTE integer value from a specified time value.

### What it Returns

It returns a value between 0 and 59 depending on the time value used as the input.

### Syntax

\=MINUTE(serial\_number)

*   **serial\_number** – The value that contains the time that needs to be determined.

Excel Minute Function – Examples
--------------------------------

Here are some practical examples of using the Excel MINUTE function.

### Example #1 – Entering Time as Text

Excel MINUTE function can take time in double quotes as text. Based on the time you have used, it will return the minutes values of that time (between 0 and 59).

![Excel Minute function Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20179'%3E%3C/svg%3E)

For this to work, the time has to be in a format that Excel interprets as time.

If you enter the time without AM/PM (as shown in A2 in the above example) Excel will consider it as the time in the 24-hour format.

Make sure you enter time in a format that is recognized by Excel. For example, “12:43 Noon” wouldn’t count as a valid format, and would return a #VALUE! error.

### Example #2 – Enter Cell Reference that has the Time

![Excel Minute function Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%20177'%3E%3C/svg%3E)

You can also use the cell reference of a cell that has the time value. In the above example, the MINUTE function returns the minute value for each time.

Also, the time needs to be in a format that Excel understands. If it’s not, you’ll get an error.

In case you don’t specify the AM/PM, the time would be taken in the 24-hour format.

### Example #3 – Using Numerical Values in Exel Hour Function

![Minute Function in Excel - example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%20178'%3E%3C/svg%3E)

In Excel, date and time are stored as numbers. So this means, 43368.215 represents a date and time – which is **25 September 2018 05:09:36.**

You can use the MINUTE function to get the minute value from this date value (or time value).

### Example #4 – Using the Result of Excel HOUR function in Calculations

![Excel Minute function Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20140'%3E%3C/svg%3E)

The result of the MINUTE formula is an integer. So you can use this integer in further calculations.

For example, you can add/subtract minutes to the resulting value (as shown in the example above).

Useful Notes
------------

The arguments can be provided in different formats:

*   **As serial number**: The integer part of the serial number represents the date and the decimal portion represents time (remember excel stores date and time as serial numbers). If you provide 41640.78125 as the serial number, it would return 45 (as the decimal portion 0.78125 represents 18 hours and 45 minutes).
    
*   **As text**: =MINUTE(“41640.78125”) would return 45.
    
*   **As a result of some other formula**: For example, =MINUTE(TIMEVALUE(“6:45 PM”)) would return 45.

#### Related Excel Functions:

*   [Excel DAY Function](https://trumpexcel.com/excel-day-function/)
    : Excel DAY function can be used when you want to get the day value (ranging from 1 to 31) on a specified date. It returns a value between 0 and 31 depending on the date used as the input.
*   [Excel NOW Function](https://trumpexcel.com/excel-now-function/)
    : It can be used to get the current date and time value.
*   [Excel Hour Function](https://trumpexcel.com/excel-hour-function/)
    : Excel HOUR function can be used when you want to get the HOUR integer value from a specified time value. It returns a value between 0 (12:00 A.M.) and 23 (11:00 P.M.) depending on the time value used as the input.
*   [Excel SECOND Function](https://trumpexcel.com/excel-second-function/)
    : It can be used want to get the integer value of the seconds from a specified time value. It returns a value between 0 and 59 depending on the time value used as the input.

**You May Also Like the Following Excel Tutorials:** 

*   [Excel Timesheet Calculator Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [How to Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Excel Timesheet Calculator template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [Convert Time to Decimal Number in Excel](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Convert Seconds to Minutes in Excel (Easy Formula)](https://trumpexcel.com/convert-seconds-to-minutes-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-minute-function/#respond)

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