# How to Use Excel DATEDIF Function (with Examples)

**Source:** https://trumpexcel.com/excel-datedif-function

---

[Skip to content](https://trumpexcel.com/excel-datedif-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-datedif-function/#below-title)

Excel DATEDIF Function (Examples + Video)
-----------------------------------------

###### ![Excel DATEDIF function - Overview](https://trumpexcel.com/wp-content/uploads/2016/03/Excel-DATEDIF-function-Overview.png)

Excel DATEDIF is one of the few undocumented functions (the other ones I know are EVALUATE, [FILES](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
, and [GET.CELL](https://trumpexcel.com/count-colored-cells-in-excel/)
).

Being undocumented means that you will not find it in the formula list or as a part of the IntelliSense (the prompt that shows up when you type a formula name to show you the names of the matching functions).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-datedif-function/#)

### When to use Excel DATEDIF Function

Excel DATEDIF function can be used when you want to [calculate the number of years, months](https://trumpexcel.com/calculate-months-between-two-dates/)
, or days between the two specified dates. A good example would be calculating the age.

### What it Returns

It returns a numerical value that denotes the number of Years/Months/Days between the two specified dates.  Whether it would be the number of Years, or Months, or Days is determined by the user input (see Input Arguments below).

### Syntax

\=DATEDIF(start\_date,end\_date,unit)

### Input Arguments

*   start\_date: It’s a date that represents the starting date value of the period. It can be entered as text strings in double quotes, as serial number, or as a result of some other function, such as [DATE](https://trumpexcel.com/excel-networkdays-function/)
    ().
*   end\_date: It’s a date that represents the end date value of the period. It can be entered as text strings in double quotes, as serial number, or as a result of some other function, such as DATE().
*   unit: This would determine what type of result you get from this function. There are six different outputs that you can get from the DATEDIF function, based on what unit you use. Here are the units that you can use:
    *   “Y” – returns the number of completed years in the specified period.
    *   “M” – returns the number of completed months in the specified period.
    *   “D” – returns the number of completed days in the specified period.
    *   “MD” – returns the number of days in the period, but doesn’t count the ones in the Years and Months that have been completed.
    *   “YM” – returns the number of months in the period, but doesn’t count the ones in the years that have been completed.
    *   “YD” – returns the number of days in the period, but doesn’t count the ones in the years that have been completed.

### Additional Notes

*   Excel DATEDIF function is provided for compatibility with Lotus 1-2-3.
*   While typing this function in a cell in Excel, it would NOT show the IntelliSense. It’ll not even show the function’s name as you enter it in a cell. However, it works in all versions of Excel. You need to know the arguments and how to use it.![Excel DATEDIF Function does not appear in the intellisense](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20162'%3E%3C/svg%3E)
*   Dates can be entered as text strings within double quotes (for example, “2016/1/15”), as serial numbers (for example, 42384, which represents January 15, 2016, if you’re using the 1900 date system), or as the results of other formulas/functions (for example, [DATEVALUE](https://trumpexcel.com/excel-datevalue-function/)
    (“2016/1/15”)).

Excel DATEDIF Function – Live Examples
--------------------------------------

Here are three examples of using the Excel DATEDIF Function.

### #1 Calculating the Number of Years Completed between two dates.

![Excel DATEDIF Function - Calculating number of years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20162'%3E%3C/svg%3E)

In the above example, Excel DATEDIF function returns the number of years completed between 01 January 1990 and the current date (which is 14 March 2016 in this example). It returns 26, which is the total number of years completed and ignores the additional months and days after it.

A common use of this could be calculating the age in years.

### #2 Calculating the Number of Months Completed between two dates.

![Excel DATEDIF Function - calculating number of months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20162'%3E%3C/svg%3E)

In the above example, Excel DATEDIF function returns the number of months completed between 01 January 1990 and the current date (which is 14 March 2016 in this example).

It returns 314, which is the total number of months completed and ignores the additional days after it.

A good use of this could be calculating the number of months between the start and end dates of projects.

In the above example, it gives the total number of months. But if you want to know the number of months after the total number of completed years, then you need to use YM as the unit argument.

For example, while [calculating age in Excel](https://trumpexcel.com/calculate-age-in-excel/)
, if you want to know how many years and how many months have elapsed till date, then you can use YM to get the number of months in addition to the years (as shown below).

![Excel DATEDIF Function - result of months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20165'%3E%3C/svg%3E)

### #3 Calculating the Number of Days Completed between two dates.

![Excel DATEDIF Function - calculating number of days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20166'%3E%3C/svg%3E)

In the above example, Excel DATEDIF function returns the total number of days completed between 01 January 1990 and the current date (which is 14 March 2016 in this example). It returns 9569, which is the total number of days between the two dates.

If you want to get the number of days between the two dates while excluding the ones from the years that have already completed, you need to use YD as the third argument (as shown in the pic below):

![Excel DATEDIF Function - number of days result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20164'%3E%3C/svg%3E)

In the above example, it returns 72, which is the total number of days after 26 complete years.

If you want to get the number of days between the two dates while excluding the ones from the years and months that have already completed, you need to use MD as the third argument (as shown in the pic below):

![Excel DATEDIF Function - Example 9](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20166'%3E%3C/svg%3E)

In the example above, it returns 13, which is the number of days in addition to 26 years and 3 months.

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
*   [Excel WORKDAY.INTL Function](https://trumpexcel.com/excel-workdayintl-function/)
    : Excel WORKDAY.INTL function can be used when you want to get the date after a given number of working days. In this function, you can specify the weekend to be days other than Saturday and Sunday.

**You May Also Like the Following Excel Tutorials:**

*   [Creating a holiday calendar in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [Undocumented Function in Excel](http://chandoo.org/wp/2011/05/16/lost-excel-functions/)
    .
*   [How to SUM values between two dates in Excel](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Calculate Years of Service in Excel](https://trumpexcel.com/calculate-years-of-service-excel/)
    
*   [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-datedif-function/#respond)

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