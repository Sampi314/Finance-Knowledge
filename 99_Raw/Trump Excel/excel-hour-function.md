# Excel HOUR Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-hour-function

---

[Skip to content](https://trumpexcel.com/excel-hour-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-hour-function/#below-title)

Excel HOUR Function (Example + Video)
-------------------------------------

![EXCEL HOUR FUNCTION](https://trumpexcel.com/wp-content/uploads/2014/03/HOUR-FORMULA-EXCEL.png)

### When to Use Excel HOUR Function

Excel HOUR function can be used when you want to get the HOUR integer value from a specified time value.

### What it Returns

It returns a value between 0 (12:00 A.M.) and 23 (11:00 P.M.) depending on the time value used as the input.

### Syntax

\=HOUR(serial\_number)

### Input Arguments

*   **serial\_number:** the time value that contains the hour that needs to be determined.

### Additional Notes

*   The argument can be provided in different formats:
    
    *   As a serial number: The integer part of the serial number represents the date and the decimal portion represents time. For example, if you are using 41640.5 as the serial number, it would return 12 (as the decimal portion 0.5 represents 12:00 PM, which is half of a full day)
        
    *   As text: =HOUR(“12:00 PM”) would return 12.
        
    *   As a result of some other formula. For example, =TIMEVALUE(“6:45 PM”)
*   Excel stores dates and time as serial numbers.

Excel HOUR Function – Examples
------------------------------

Here are five practical examples of using the Excel HOUR function.

### Example #1 – Entering Time as Text

![Excel Hour Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20417%20248'%3E%3C/svg%3E)

Excel Hour function can take the time within double quotes as the input. It then returns the integer between 0 and 23 based the time. For this to work, the time has to be in a format that Excel interprets as time.

If you enter the time without AM/PM (as shown in A2 in the above example) Excel will consider it as the time in the 24-hour format.

Make sure you enter time in a format that is recognized by Excel. For example, “12 Noon” wouldn’t count as a valid format, and would return a #VALUE! error.

### Example #2 – Enter Cell Reference that has the Time

![Excel Hour Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20237'%3E%3C/svg%3E)

As shown in the examples above, you can use the cell reference that contains the time value. Note that if you don’t use AM/PM, the HOUR function would take it in the 24 Hour format.

### Example #3 – Using Numerical Values in Exel Hour Function

![Excel Hour Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20232'%3E%3C/svg%3E)

If you use a numeric value within Excel HOUR Function, it will use the decimal portion of it to return the HOUR value. For example, if I use 41699.125 as the input in HOUR function, it will discard the 41699 part and use .125 part to return the time. The answer would be 3 as .125 represents three hours.

### Example #4 – Using the Result of Excel HOUR function in Calculations

![Excel Hour Function - Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20192'%3E%3C/svg%3E)

The output of the Excel HOUR function is an integer which can be used in formulas/calculations. For example, you can add/subtract values from the result of the HOUR function as shown above.

Excel HOUR Function – Video
---------------------------

**Other Useful Excel Functions:**

*   [Excel DAY Function](https://trumpexcel.com/excel-day-function/)
    : Excel DAY function can be used when you want to get the day value (ranging between 1 to 31) from a specified date. It returns a value between 0 and 31 depending on the date used as the input.
*   [Excel MINUTE Function](https://trumpexcel.com/excel-minute-function/)
    : It can be used when you want to get the MINUTE integer value from a specified time value. It returns a value between 0 and 59 depending on the time value used as the input.
*   [Excel NOW Function](https://trumpexcel.com/excel-now-function/)
    : It can be used to get the current date and time value.
*   [Excel SECOND Function](https://trumpexcel.com/excel-second-function/)
    : It can be used want to get the integer value of the seconds from a specified time value. It returns a value between 0 and 59 depending on the time value used as the input.

**You May Also Like the Following Tutorials:**

*   [Excel Timesheet Calculator Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [How to Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Excel Timesheet Calculator template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [Convert Time to Decimal Number in Excel](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Calculate Time in Excel](https://trumpexcel.com/calculate-time-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-hour-function/#respond)

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