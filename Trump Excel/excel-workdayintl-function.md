# Excel WORKDAY.INTL Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-workdayintl-function

---

[Skip to content](https://trumpexcel.com/excel-workdayintl-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-workdayintl-function/#below-title)

Excel WORKDAY.INTL Function (Example + Video)
---------------------------------------------

![ EXCEL WORKDAY.INTL Function](https://trumpexcel.com/wp-content/uploads/2014/05/WORKDAY.INTL-FORMULA-EXCEL.png)

### When to use Excel WORKDAY.INTL Function

Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days.

For example, if I start a project today and it will take 20 working days to complete, then I can use WORKDAY function to get the completion date.

This function is best used when you want to calculate the [invoice](https://trumpexcel.com/invoice-generator-pdf/)
 due date, project due date, delivery date, etc.

This function differs from [Excel WORKDAY function](https://trumpexcel.com/excel-workday-function/)
, as here you can specify the weekend to be days other than Saturday and Sunday.

### What it Returns

It returns the serial number of the date that is after or before the specified number of working days (from the specified start date)

### Syntax

\=WORKDAY.INTL(start\_date, days, \[weekend\], \[holidays\])

### Input Arguments

*   **start\_date –** a date value that represents the start date.
*   **days** – the total number of working days. These exclude the weekend. You can use a positive or a negative value here. A positive value calculates the date which is after the start date, and negative value calculates the date before the start date.
*   **\[weekend\]** – (Optional) It specifies the day of the weeks that are considered as the weekend. It is a number that maps to various combinations of weekends.
*   **\[holidays\]** – (Optional) It is a range of dates that are excluded from the calculations. For example, these could be national/public holidays. It could be a reference to the range of cells that contains the dates, or could be an array of serial numbers that represent the dates.

### Additional Notes

*   A Date can be entered as:
    *   A result from some other function
    *   A date stored as text
    *   A date entered as text (In double quotes)
*   A Weekend could be any two consecutive days or any single day of the week.
*   In case of part-time jobs or non-consecutive non-working days, type the below format in \[weekend\] section.
    *   Suppose you only work on Monday and Wednesday, use “0101111” \[0 represents a working day and 1 represents non-working day\].
        *   The first number in this format represents Monday and the last represents Sunday.
        *   Use this number in double quotes.
        *   With the same logic, “1010111” indicates that only Tuesday and Thursday are working, and rest 5 days are non-working.

Excel WORKDAY.INTL Function – Live Example
------------------------------------------

Excel WORKDAY.INTL Function – Video Tutorial
--------------------------------------------

**Related Useful Excel Functions:**

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
*   [Excel WORKDAY Function](https://trumpexcel.com/excel-workday-function/)
    : Excel WORKDAY function can be used when you want to get the date after a given number of working days. By default, it takes Saturday and Sunday as the weekend.
*   [Excel DATEDIF Function](https://trumpexcel.com/excel-datedif-function/)
    : Excel DATEDIF function can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating the age.
*   [Excel SEQUENCE Function](https://trumpexcel.com/excel-functions/sequence/)
    

#### You May Also Like the Following Tutorials:

*   [Count the Number of Working Days in a part-time job](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-workdayintl-function/#respond)

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