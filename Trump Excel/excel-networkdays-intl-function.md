# Excel NETWORKDAYS.INTL Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-networkdays-intl-function

---

[Skip to content](https://trumpexcel.com/excel-networkdays-intl-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-networkdays-intl-function/#below-title)

Excel NETWORKDAYS.INTL Function (Example + Video)
-------------------------------------------------

![EXCEL NETWORKDAYS.INTL FUNCTION](https://trumpexcel.com/wp-content/uploads/2014/03/NETWORKDAYS.INTL-FORMULA-EXCEL.png)

### When to use Excel NETWORKDAYS.INTL Function

Excel NETWORKDAYS.INTL function can be used when you want to get the number of working days between two given dates. It does not count the weekends and holidays, both of which can be specified by the user.

It can be used when you want to calculate the benefits accrued to employees over time. It also enables you to specify the weekend (for example, you can specify Friday and Saturday as the weekend, or only Sunday as the weekend).

### What it Returns

It returns a positive integer that represents a total number of working days between two specified dates.

### Syntax

\=NETWORKDAYS.INTL(start\_date, end\_date, \[weekend\], \[holidays\])

### Input Arguments

*   **start\_date –** a date value that represents the start date.
*   **end\_date** – a date value that represents the end date.
*   **\[weekend\] –** (Optional) Here you can specify the weekend. If this is omitted, Saturday and Sunday are taken as the weekend.
*   **\[holidays\]** – (Optional) It is a range of dates that are excluded from the calculations. For example, these could be national/public holidays. This could be entered as a reference to a range of cells that contains the dates or could be an array of serial numbers that represent the dates.

### Additional Notes

*   Could be used to calculate benefits accrued to employees over time.
*   A date can be entered as:
    *   A result from some other function
    *   A date stored as text
    *   A date entered as text (in double quotes)
*   Weekend could be any two consecutive days or any single day of the week. When you enter the weekend argument, Excel shows a drop down menu from where you can select the relevant option.
*   In case of part-time jobs or non-consecutive non-working days type the below format in \[weekend\] section
    *   Suppose you only work on Monday and Wednesday, use “0101111” \[0 represents a working day and 1 represents non-working day\]
        *   The first number in this format represents Monday and the last represents Sunday
        *   Use this number in double quotes
        *   With the same logic, “1010111″ indicates that only Tuesday and Thursday are working, and rest 5 days are non-working

Excel NETWORKDAYS.INTL Function – Live Example
----------------------------------------------

Excel NETWORKDAYS.INTL Function – Video Tutorial
------------------------------------------------

**Related Useful Excel Functions:**

*   [Excel DATE Function](https://trumpexcel.com/excel-date-function/)
    : Excel DATE function can be used when you want to get the date value using the year, month and, day values as the input arguments. It returns a serial number that represents a specific date in Excel.
*   [Excel DATEVALUE Function](https://trumpexcel.com/excel-datevalue-function/)
    : Excel DATEVALUE function is best suited for situations when a date is stored as text. This function converts the date from text format to a serial number that Excel recognizes as a date.
*   [Excel NETWORKDAYS Function](https://trumpexcel.com/excel-networkdays-function/)
    : Excel NETWORKDAYS function can be used when you want to get the number of working days between two given dates. It does not count the weekends between the specified dates (by default the weekend is Saturday and Sunday). It can also exclude any specified holidays.
*   [Excel TODAY Function](https://trumpexcel.com/excel-today-function/)
    : Excel TODAY function can be used to get the current date. It returns a serial number that represents the current date.
*   [Excel WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    : Excel WEEKDAY function can be used to get the day of the week as a number for the specified date. It returns a number between 1 and 7 that represents the corresponding day of the week.
*   [Excel WORKDAY Function](https://trumpexcel.com/excel-workday-function/)
    : Excel WORKDAY function can be used when you want to get the date after a given number of working days. By default, it takes Saturday and Sunday as the weekend
*   [Excel WORKDAY.INTL Function](https://trumpexcel.com/excel-workdayintl-function/)
    : Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.
*   [Excel DATEDIF Function](https://trumpexcel.com/excel-datedif-function/)
    : Excel DATEDIF function can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating the age.

#### You May Also Like the Following Tutorials:

*   [Count the number of workdays between two dates](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [Creating a holiday calendar in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Employee Timesheet Calculator](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Business Days Calculator](https://trumpexcel.com/calculator/business-days/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-networkdays-intl-function/#respond)

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