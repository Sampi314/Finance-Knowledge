# Excel WORKDAY Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-workday-function

---

[Skip to content](https://trumpexcel.com/excel-workday-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-workday-function/#below-title)

Excel WORKDAY Function (Examples + Video)
-----------------------------------------

![EXCEL WORKDAY FUNCTION](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20327'%3E%3C/svg%3E)

### When to use Excel WORKDAY Function

Excel WORKDAY function can be used when you want to get the date after a given number of working days. For example, if I start a project today and it will take 20 working days to complete it, then I can use the WORKDAY function to get the completion date. This function is best suited when you want to calculate the [invoice](https://trumpexcel.com/invoice-generator-pdf/)
 due date, project due date, delivery date, etc.

This function, by default, takes Saturday and Sunday as the weekend. If you would like to use days other than Saturday and Sunday as the weekend, use [Excel WORKDAY.INTL function](https://trumpexcel.com/excel-workdayintl-function/)
.

### What it Returns

It returns the serial number of the date that is after or before the specified number of working days (from the specified start date).

### Syntax

\=WORKDAY(start\_date, days, \[holidays\])

### Input Arguments

*   **start\_date –** a date value that represents the start date.
*   **days** – the total number of working days. These exclude weekend (Saturday and Sunday). You can use a positive or a negative value here. A positive value calculates the date which is after the start date, and negative value calculates the date before the start date.
*   **\[holidays\]** – (Optional) It is a range of dates that are excluded from the calculations. For example, these could be national/public holidays. It could be a reference to a range of cells that contains the dates, or could be an array of serial numbers that represent the dates.

### Additional Notes

*   Saturday and Sunday are considered as the weekend and are not counted.
    *   In case the weekends are days other than Saturday and Sunday, use WORKDAYS.INTL function.
*   A date can be entered as:
    *   A result from some other function.
    *   A date stored as text.
    *   A date entered as text (in double quotes).

Excel WORKDAY Function – Examples
---------------------------------

Here are the examples of using the Excel Workday function.

### **#1 Getting the Completion Date after Specified Number of Working Days**

Excel Workday function would return the completion date when you specify the start date and the number of working day. It automatically excludes Saturday and Sunday as weekend (non-working days).

![Excel Workday Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20189'%3E%3C/svg%3E)

In the above example, the start date is 28 Feb 2016, and the result is 15 July 2016, which is after 100 working days (excluding Saturdays and Sundays).

### **#2 Getting the Completion Date after Specified Number of Working Days (excluding Holidays)**

If you want to exclude holidays while calculating the completion date, there is a third argument in the Workday function that lets you specify a list of holidays.

![Excel Workday Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20741%20181'%3E%3C/svg%3E)

In the above example, the start date is 28 Feb 2016, and the result is 20 July 2016, which is after 100 working days. The calculation excludes weekends (Saturdays and Sundays) and the specified holidays in C3:C5. In case, a holiday occurs on a weekend, it is counted only once.

Excel WORKDAY Function – Video Tutorial
---------------------------------------

**Related Excel Functions:**

*   [Excel DATE Function](https://trumpexcel.com/excel-date-function/)
    : Excel DATE function can be used when you want to get the date value using the year, month and, day values as the input arguments. It returns a serial number that represents a specific date in Excel.
*   [Excel DATEVALUE Function](https://trumpexcel.com/excel-datevalue-function/)
    : Excel DATEVALUE function is best suited for situations when a date is stored as text. This function converts the date from text format to a serial number that Excel recognizes as a date.
*   [Excel NETWORKDAYS Function](https://trumpexcel.com/excel-networkdays-function/)
    : Excel NETWORKDAYS function can be used when you want to get the number of working days between two given dates. It does not count the weekends between the specified dates (by default the weekend is Saturday and Sunday). It can also exclude any specified holidays.
*   [Excel NETWORKDAYS.INTL Function](https://trumpexcel.com/excel-networkdays-intl-function/)
    : Excel NETWORKDAYS.INTL function can be used when you want to get the number of working days between two given dates. It does not count the weekends and holidays, both of which can be specified by the user. It also enables you to specify the weekend (for example, you can specify Friday and Saturday as the weekend, or only Sunday as the weekend).
*   [Excel Today Function](https://trumpexcel.com/excel-today-function/)
    : Excel TODAY function can be used to get the current date. It returns a serial number that represents the current date.
*   [Excel WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    : Excel WEEKDAY function can be used to get the day of the week as a number for the specified date. It returns a number between 1 and 7 that represents the corresponding day of the week.
*   [Excel WORKDAY.INTL Function](https://trumpexcel.com/excel-workdayintl-function/)
    : Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.
*   [Excel DATEDIF Function](https://trumpexcel.com/excel-datedif-function/)
    : Excel DATEDIF function can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating the age.

#### You May Also Like the Following Excel Tutorials:

*   [Count the number of workdays between two dates](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [Employee Leave Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-workday-function/#respond)

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