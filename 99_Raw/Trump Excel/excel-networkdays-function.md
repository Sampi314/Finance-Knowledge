# Excel NETWORKDAYS Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-networkdays-function

---

[Skip to content](https://trumpexcel.com/excel-networkdays-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-networkdays-function/#below-title)

Excel NETWORKDAYS Function (Examples + Video)
---------------------------------------------

![EXCEL NETWORKDAYS FUNCTION](https://trumpexcel.com/wp-content/uploads/2014/03/NETWORKDAYS-FORMULA-EXCEL.png)

### When to use Excel NETWORKDAYS Function

Excel NETWORKDAYS function can be used when you want to get the number of working days between two given dates. It does not count the weekends between the specified dates (by default the weekend is Saturday and Sunday). It can also exclude any specified holidays.

A typical situation where you can use this function is to calculate the benefits accrued to employees overtime.

### What it Returns

It returns a positive integer that represents the total number of working days between two specified dates.

### Syntax

\=NETWORKDAYS(start\_date, end\_date, \[holidays\])

### Input Arguments

*   **start\_date –** a date value that represents the start date.
*   **end\_date** – a date value that represents the end date.
*   **\[holidays\]** – (Optional) It is a range of dates that are excluded from the calculation. For example, these could be national/public holidays. This could be entered as a reference to a range of cells that contains the dates, or could be an array of serial numbers that represent the dates.

### Additional Notes

*   Saturday and Sunday are considered as weekends by default and are not counted. In case you want the weekends to be days other than Saturday and Sunday, use the [NETWORKDAYS.INTL](https://trumpexcel.com/excel-networkdays-intl-function/)
     function.
*   A date can be entered as:
    *   A result from some other function.
    *   A date stored as text.
    *   A date entered as text (in double quotes).
*   NETWORKDAYS function returns the #VALUE! error if any of the arguments is not valid.
*   This function is a part of the Analysis Tool Pack (ATP) and not Excel in-built functions. Hence, in case you get a #NAME! error, it could be due to not having the ATP or it not being loaded properly. Iu such case, try reloading the ATP.

Excel NETWORKDAYS Function – Examples
-------------------------------------

**Example #1: Calculating the number of days between two dates (excluding weekends)**

![Excel Networkdays Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20159'%3E%3C/svg%3E)

In the above example, the Excel NETWORKDAYS function calculates the number of days between 20th December and 10 January. It only excludes the weekends (Saturdays and Sundays) and returns 15 as the result.

In this case, we have specified no holidays, so only weekends are excluded.

**Example #2: Calculating the number of days between two dates (excluding weekends and Holidays)**

![Excel Networkdays Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20711%20159'%3E%3C/svg%3E)

In the above example, the Excel NETWORKDAYS function calculates the number of days between 20th December and 10 January. It excludes the weekends (Saturdays and Sundays) and the specified holidays. The result is 13 days.

In this case, we have specified 2 days as holidays, and these are not counted while calculating the total number of working days. Note that these two holidays occur on a weekday (both 25th Dec 2015 and 01 Jan 2016 occur on a Friday). In case a holiday occurs on a weekend, it is not counted as an exclusion (as weekends are anyway not counted).

In the above example, if you change 01 Jan 2016 (which is a Friday) to 02 Jan 2016 (which is a Saturday), the result would change to 14.

Excel NETWORKDAYS Function – Video
----------------------------------

**Related Useful Excel Functions:**

*   [Using DATE Function in Excel](https://trumpexcel.com/excel-date-function/)
    : Excel DATE function can be used when you want to get the date value using the year, month and, day values as the input arguments. It returns a serial number that represents a specific date in Excel.
*   [Using DATEVALUE Function in Excel](https://trumpexcel.com/excel-datevalue-function/)
    : Excel DATEVALUE function is best suited for situations when a date is stored as text. This function converts the date from text format to a serial number that Excel recognizes as a date.
*   [Using NETWORKDAYS.INTL Function in Excel](https://trumpexcel.com/excel-networkdays-intl-function/)
    : Excel NETWORKDAYS.INTL function can be used when you want to get the number of working days between two given dates. It does not count the weekends and holidays, both of which can be specified by the user. It also enables you to specify the weekend (for example, you can specify Friday and Saturday as the weekend, or only Sunday as the weekend).
*   [Using TODAY Function in Excel](https://trumpexcel.com/excel-today-function/)
    : Excel TODAY function can be used to get the current date. It returns a serial number that represents the current date.
*   [Using WEEKDAY Function in Excel](https://trumpexcel.com/excel-weekday-function/)
    : Excel WEEKDAY function can be used to get the day of the week as a number for the specified date. It returns a number between 1 and 7 that represents the corresponding day of the week.
*   [Using WORKDAY Function in Excel](https://trumpexcel.com/excel-workday-function/)
    : Excel WORKDAY function can be used when you want to get the date after a given number of working days. By default, it takes Saturday and Sunday as the weekend
*   [Using WORKDAY.INTL Function in Excel](https://trumpexcel.com/excel-workdayintl-function/)
    : Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.
*   [Using DATEDIF Function in Excel](https://trumpexcel.com/excel-datedif-function/)
    : Excel DATEDIF function can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating the age.

#### You May Also Like the Following Excel Tutorials_:_

*   [Count the number of workdays between two dates](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [Creating a holiday calendar in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Employee Timesheet Calculator](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Excel Months Between Two Dates](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Business Days Calculator](https://trumpexcel.com/calculator/business-days/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Excel NETWORKDAYS Function | Formula Examples + FREE Video”
--------------------------------------------------------------------------

1.  Is there a 2020 leave trackerr available. Or is there a way that I am able to update 2019 Tracker? Thanks
    
    [Reply](https://trumpexcel.com/excel-networkdays-function/#comment-12720)
    
2.  Could you please correct the video attachment for this tutorial? The video is not for the NETWORKDAYS function
    
    [Reply](https://trumpexcel.com/excel-networkdays-function/#comment-11736)
    
    *   Thanks for letting me know Jordan.. Fixed it!
        
        [Reply](https://trumpexcel.com/excel-networkdays-function/#comment-11737)
        
3.  well explained
    
    [Reply](https://trumpexcel.com/excel-networkdays-function/#comment-9592)
    
    *   RGRH
        
        [Reply](https://trumpexcel.com/excel-networkdays-function/#comment-11480)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-networkdays-function/#respond)

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