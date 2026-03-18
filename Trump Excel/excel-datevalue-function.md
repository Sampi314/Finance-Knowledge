# Excel DATEVALUE Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-datevalue-function

---

[Skip to content](https://trumpexcel.com/excel-datevalue-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-datevalue-function/#below-title)

Excel DATEVALUE Function – An Overview
--------------------------------------

![Excel DATEVALUE Function](https://trumpexcel.com/wp-content/uploads/2014/03/DATEVALUE-FORMULA-EXCEL.png)

### When to use Excel DATEVALUE Function

Excel DATEVALUE function is best suited for situations when a date is stored as text. This function converts the date from text format to a serial number that Excel recognizes as a date.

### What it Returns

It returns a serial number for a date. For example, if we use the function DATEVALUE(“1/1/2016”), it would return 42370 which is the serial number for 01-01-2016.

### Syntax

\=DATEVALUE(“date\_text”)

### Input Arguments

*   **date\_text**: this argument could be a date in text format (entered manually) or a cell reference that contains the date in text format.
    *   If date\_text is manually entered in the DATEVALUE function, it should be in double quotes.
    *   If date\_text is a cell reference, it should be in text format.

### Additional Notes

*   DATEVALUE function returns a serial number.
    *   For example: =DATEVALUE(“1/1/2014”) returns 41640 (which is the serial number for this date).
    *   If you do not use the day argument, and only use the month and year arguments, it returns the serial number for the [first day of that month](https://trumpexcel.com/first-day-of-month-excel/)
        .
        *   For example, DATEVALUE(“1/2014”) would return the serial number 41640 (which represents the first day of the first month of 2014).
    *   If the Year argument is not used, excel automatically takes the current year (based on computer systems clock settings).
*   The serial number returned by the DATEVALUE function can vary depending on the computer’s system date settings.
    *   For example, 01/03/2016 would be January 3rd in the US and 1st March in the UK.

Excel DATEVALUE Function – Examples
-----------------------------------

Here are examples of using the Excel DATEVALUE function.

### Example 1: Getting the Serial Number of a Date Entered as Text

![Excel DateValue Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20242'%3E%3C/svg%3E)

In the above example, the DATEVALUE function returns the serial number of the date entered within quotes. The date entered needs to be in a format that is recognized by Excel as a valid date format (else it returns a #VALUE! error.

Note that the value returned by the DATEVALUE function depends on your system’s clock setting. If it DD-MM-YYYY then “01-06-2016” would mean June 1, 2016, but for MM-DD-YYYY it would be January 6, 2016.

### Example 2: Using Cell References Where Dates are Entered as Text

![Excel DateValue Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20554%20191'%3E%3C/svg%3E)

When dates are entered as text in a cell, you can use the DATEVALUE function to get the serial number of the date it represents. Note that the date needs to be in a format that is recognized by Excel as a valid date format.

In the above example, the DATEVALUE function converts 1-6-16 and 1-June-16 to its date value.

Excel DATEVALUE function can be useful when you have dates in a text format that you want to filter, sort, or format as dates, or use in date calculations. In the text format, you won’t be able to sort the dates as Excel would consider it as text and not numbers.

### Example 3: When the Year is Not Specified

![Excel DateValue Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20554%20218'%3E%3C/svg%3E)

When the Year is not specified, DATEVALUE uses the current year to return the date value (current year is 2016 in this case).

### Example 4: When the Day is Not Specified

![Excel DateValue Example 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20216'%3E%3C/svg%3E)

When the Day is not specified, DATEVALUE uses the first day of the month to return the date value.

In the examples above, when 6-16 is used in the DATEVALUE function, it returns 42522, which is the date value for 1 June 2016.

**Note:** If the ‘year’ value is greater than 12, then the DATEVALUE function would consider it as a case of ‘missing month’ and use the first day of the specified month. But if the year is less than or equal to 12 (let’s say 2011 or 2012), then the DATEVALUE function would consider it as a case of the missing year, and use the current year to return the date value.

### Excel DATEVALUE Function – VIDEO

**Other Useful Excel Functions:**

*   [Excel DATE Function in Excel](https://trumpexcel.com/excel-date-function/)
    : It can be used when you want to get the date value using the year, month and, day values as the input arguments. It returns a serial number that represents a specific date in Excel.
*   [Excel NETWORKDAYS Function](https://trumpexcel.com/excel-networkdays-function/)
    : It can be used when you want to get the number of working days between two given dates. It does not count the weekends between the specified dates (by default the weekend is Saturday and Sunday). It can also exclude any specified holidays.
*   [Excel NETWORKDAYS.INTL Function](https://trumpexcel.com/excel-networkdays-intl-function/)
    : It’s similar to the NETWORKDAYS function with one added functionality. It enables you to specify the weekend (for example, you can specify Friday and Saturday as the weekend, or only Sunday as the weekend).
*   [Excel TODAY Function](https://trumpexcel.com/excel-today-function/)
    : It can be used to get the current date. It returns a serial number that represents the current date.
*   [Excel WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    : It can be used to get the day of the week as a number for the specified date. It returns a number between 1 and 7 that represents the corresponding day of the week.
*   [Excel WORKDAY Function](https://trumpexcel.com/excel-workday-function/)
    : It can be used when you want to get the date after a given number of working days. By default, it takes Saturday and Sunday as the weekend
*   [Excel WORKDAY.INTL Function](https://trumpexcel.com/excel-workdayintl-function/)
    : It can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.
*   [Excel DATEDIF Function](https://trumpexcel.com/excel-datedif-function/)
    : It can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating age.

**You May Also Like the Following Excel Tutorials:**

*   [Calculate Age in Excel using Date of Birth](https://trumpexcel.com/calculate-age-in-excel/)
    .
*   [How to Remove Time from Date in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    
*   [How to Convert Text to Date in Excel](https://trumpexcel.com/convert-text-to-date-excel/)
    
*   [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)
    
*   [Calculate Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-datevalue-function/#respond)

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