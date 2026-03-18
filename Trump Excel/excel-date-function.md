# Excel DATE Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-date-function

---

[Skip to content](https://trumpexcel.com/excel-date-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-date-function/#below-title)

Excel DATE Function Overview
----------------------------

![Excel DATE Function](https://trumpexcel.com/wp-content/uploads/2014/03/DATE-FORMULA-EXCEL.png)

### When to use Excel DATE Function

Excel DATE function can be used when you want to get the date value using the year, month and, day values as the input arguments. The input arguments can be entered manually, as cell reference that contains the dates, or as a result some formula.

### What it Returns

It returns a serial number that represents a specific date in Excel. For example, if it returns 42370, it represents the date: 01 January 2016.

### Syntax

\=DATE(year, month, day)

### Input Arguments

*   **year –** the year to be used for the date.
*   **month** – the month to be used for the date.
*   **day** – the day to be used for the date.

### Additional Notes (boring stuff.. but important to know)

*   The result displayed in the cell would depend on the formatting of that cell. For example:
    *   If the cell is formatted as General, the result is displayed in the date format (remember dates are always stored as serial numbers but can be displayed in various formats).
    *   To get the result as a serial number, change the cell’s formatting to Number.
*   It is recommended to use the four-digit year to avoid unwanted results. If the Year value used is less than 1900, Excel automatically adds 1900 to it. For example, if you use ten as the Year value, Excel makes it 1910.
*   The Month value can be less than 0 or greater than 12. If the Month value is greater than 12, then Excel automatically adds that excess month to the next year. Similarly, if the month value is less than 0, the DATE function would automatically go back that many numbers of months.
    *   For example, DATE(2015,15,1) would return 1 March 2016. Similarly, DATE(2016,-2,1) would return October 1, 2015.
*   Day value could be positive or negative. If the day value is negative, Excel automatically deducts that many days from the [first day of the specified month](https://trumpexcel.com/first-day-of-month-excel/)
    . If it is more than the [number of days in that month](https://trumpexcel.com/days-in-month-excel/)
    , then those extra days are added to the next month value. (example below).

Excel DATE Function – Examples
------------------------------

Here are X example of using the Excel DATE function:

### Example 1: Getting the Date Serial number using Year, Month, and Day values

You can get the serial number of a date when you specify the Year, Month, and Day values.

![Excel DATE Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20713%20189'%3E%3C/svg%3E)

In the example above, the DATE function takes three arguments, 2016 as the year value, 3 as the month value, and 1 as the date value.

It returns 42430 when the cell is formatted as ‘General’, and returns 01-03-2016 when the cell is formatted as ‘Date’.

Note that Excel stores a date or time as a number.

The date format can vary based on your regional settings. For example, the date format in the US is DD-MM-YYYY, while in the UK it’s MM-DD-YYYY.

If you have the Year, Month, and Day values in cells in a worksheet, you can use the cell references as shown below:

![Excel DATE Function - Example 1a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20110'%3E%3C/svg%3E)

Also read: [Number Of Days Between Two Dates Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
 

### Example 2: Using Negative Values for Month or Days

You can use negative values for month and days. When you use a negative value for a month, let’s say -1, it goes back by 1 month return its date.

For example, if you use the formula \=DATE(2017,-1,1), it’ll return the date November 1, 2016, as goes back by one month. Similarly, you can use any negative number in months.

![Excel DATE Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20169'%3E%3C/svg%3E)

The same logic is followed when you use a month value that is more than 12. In that case, it goes to the next year and returns as the date after the months in excess of 12.

For example, if you use the formula \=DATE(2016,14,1), it’ll return the date February 1, 2017.

![Excel DATE Function - Example 2a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20193'%3E%3C/svg%3E)

_Note: The date format shown in the examples above is based on my system’s settings (which is DD-MM-YYYY). It may vary based on your settings._

Similarly, you can also use negative day values or values that are more than 31, and accordingly, Excel DATE function would adjust the date.

Excel DATE Function – VIDEO
---------------------------

**Other Useful Excel Functions:**

*   [DATEVALUE Function](https://trumpexcel.com/excel-datevalue-function/)
    : Excel DATEVALUE function is best suited for situations when a date is stored as text. This function converts the date from text format to a serial number that Excel recognizes as a date.
*   [NETWORKDAYS Function](https://trumpexcel.com/excel-networkdays-function/)
    : Excel NETWORKDAYS function can be used when you want to get the number of working days between two given dates. It does not count the weekends between the specified dates (by default the weekend is Saturday and Sunday). It can also exclude any specified holidays.
*   [NETWORKDAYS.INTL Function:](https://trumpexcel.com/excel-networkdays-intl-function/)
     Excel NETWORKDAYS.INTL function can be used when you want to get the number of working days between two given dates. It does not count the weekends and holidays, both of which can be specified by the user. It also enables you to specify the weekend (for example, you can specify Friday and Saturday as the weekend, or only Sunday as the weekend).
*   [TODAY Function](https://trumpexcel.com/excel-today-function/)
    : Excel TODAY function can be used to get the current date. It returns a serial number that represents the current date.
*   [WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    : Excel WEEKDAY function can be used to get the day of the week as a number for the specified date. It returns a number between 1 and 7 that represents the corresponding day of the week.
*   [WORKDAY Function](https://trumpexcel.com/excel-workday-function/)
    : Excel WORKDAY function can be used when you want to get the date after a given number of working days. By default, it takes Saturday and Sunday as the weekend
*   [WORKDAY.INTL Function](https://trumpexcel.com/excel-workdayintl-function/)
    : Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.
*   [DATEDIF Function](https://trumpexcel.com/excel-datedif-function/)
    : Excel DATEDIF function can be used when you want to calculate the number of years, months, or days between the two specified dates. A good example would be calculating the age.

**You May Also Like the Following Excel Tutorials:**

*   [Creating a holiday calendar in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [How to Calculate Time in Excel](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [Calendar Integrated with a To Do List Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [How to Calculate Age in Excel using the date of birth](https://trumpexcel.com/calculate-age-in-excel/)
    .
*   [How to Convert Date to Text in Excel.](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [MS Excel Functions Help – DATE](https://support.office.com/en-us/article/DATE-function-e36c0c8c-4104-49da-ab83-82328b832349)
    .
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Convert Text to Date in Excel (8 Easy Ways)](https://trumpexcel.com/convert-text-to-date-excel/)
    
*   [Calculate Number Of Months Between Two Dates](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Get End of Year Date in Excel (Formula)](https://trumpexcel.com/end-of-year-formula-excel/)
    
*   [How to Add Years to Date in Excel?](https://trumpexcel.com/add-years-to-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Excel DATE Function | Formula Examples + FREE Video”
------------------------------------------------------------------

1.  sir kindly prepare a excel data base on the line employee id designation name field  
    apar stock, status of apar posting in posting out pending active etc
    
    [Reply](https://trumpexcel.com/excel-date-function/#comment-41415)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-date-function/#respond)

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