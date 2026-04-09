# Calculate Number of Weeks Between Two Dates (3 Easy Formulas)

**Source:** https://trumpexcel.com/weeks-between-two-dates-excel

---

[Skip to content](https://trumpexcel.com/weeks-between-two-dates-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/weeks-between-two-dates-excel/#below-title)

When working with dates and making project plans in Excel, you may come across a situation where you want to know how many weeks there are between two dates.

While there is no built-in function to do this in Excel, this can easily be done using other simple functions.

In this short article, I will show you how to calculate the number of weeks between two dates in Excel.

**[_Click here to download the example file and follow along_](https://www.dropbox.com/scl/fi/auty675xql7u72a21dyt1/Weeks-Between-Dates.xlsx?rlkey=sxmx6dzkle5fx6fo9xyu1tyjo&dl=1)
**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/weeks-between-two-dates-excel/#)

DAYS Function to Get Weeks Between Two Dates
--------------------------------------------

A week always has seven days, so if we can find the total [number of days between two given dates](https://trumpexcel.com/number-of-days-between-two-dates/)
, we can easily find the total number of weeks by dividing this value by 7.

Below, I have a data set where I have the start date in column A and the End date in column B, and I want to calculate the total number of weeks between these two dates (note that the dates are in dd-mm-yyyy format).

![Dates Dataset to calculate week between dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20336'%3E%3C/svg%3E)

Here is the formula that will do this:

\=DAYS(B2,A2)/7

I entered this formula in cell C2 and then copied it for all the other cells in the column to get the result.

![DAYS formula to get weeks between dates in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20384'%3E%3C/svg%3E)

DAYS function subtracts the start date from the end date to give us the total number of days between these two given dates.

This value is then divided by 7 to get the total number of weeks between the two dates.

In case you see dates in column C instead of numbers, click the Home tab, then in the Number group, click on the Format drop-down and select General.

![Select general as the cell formatting for dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20520'%3E%3C/svg%3E)

As you must have already noticed, some of the results have decimal values (such as 24.142857). In this case, 24 gives us the total number of completed weeks between these two dates, and the decimal portion gives us the additional days after 24 weeks.

In case you only want to get the number of completed weeks, you can use the below formula:

\=INT(DAYS(B2,A2)/7)

This will remove the decimal portion and only give you the [integer part of the result](https://trumpexcel.com/excel-int-function/)
.

In case you want to [round up the value](https://trumpexcel.com/round-to-nearest-integer/)
 and count any decimal part as a complete week, you can use the formula below:

\=ROUNDUP(DAYS(B2,A2)/7,0)

Note: The result you get is not inclusive of both the start date and the end date. For example, if your project starts on 1st January and ends on 11th January, the DAYS function would return 10. If you want the start date and the end date to be included in the counting of days, you need to add 1 to the result of the DAYS function.

Also read: [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)

Subtract Dates to Get Weeks Between Two Dates
---------------------------------------------

Since dates are stored as serial numbers in Excel, you can also [do a simple subtraction](https://trumpexcel.com/subtract-in-excel/)
 to get the number of days between two given dates and then calculate the number of weeks from that.

Below, I have the data set where I have the Start date in column A and the End date in column B, and I want to calculate the number of weeks between these two dates (note that the dates are in dd-mm-yyyy format).

![Dates Dataset to calculate week between dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20336'%3E%3C/svg%3E)

Here is the simple subtraction formula to do this:

\=(B2-A2)/7

Enter this formula in cell C2 and copy it for all the other cells in the column.

![Subtract formula to get weeks between dates in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20352'%3E%3C/svg%3E)

In case you only want to get the number of completed weeks, you can use the below formula:

\=INT((B2-A2)/7)

Note: For this method to work, your dates need to be in a [format that Excel recognizes as a valid date format](https://trumpexcel.com/change-date-format-excel/)
 and it shouldn’t be in the text format. In some cases, when your date is in the text format, this formula may [return a VALUE error](https://trumpexcel.com/fix-value-error-in-excel/)
.

Also read: [Get the Number of Days in a Month in Excel](https://trumpexcel.com/days-in-month-excel/)

WEEKNUM Function to Get Weeks Between Two Dates
-----------------------------------------------

Another smart way to calculate the number of weeks between two dates is by using the WEEKNUM function.

Below, I have the same data set where I have the Start Date in column A and the End Date in column B, and I want to calculate the number of weeks between these two dates (note that the dates are in dd-mm-yyyy format).

![Dates Dataset to calculate week between dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20336'%3E%3C/svg%3E)

Here is the WEEKNUM formula to do this:

\=WEEKNUM(B2-A2)

Enter this formula in cell C2 and copy it for all the other cells in the column.

![WEEKNUM formula to get weeks between dates in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20330'%3E%3C/svg%3E)

WEEKNUM Function works by taking the [serial number of a date](https://trumpexcel.com/convert-date-to-serial-number-excel/)
 as input and giving us the week number of that date in that year.

However, in this example, we are using _B2-A2_ as the date serial number, which makes the formula count the total number of weeks from the beginning of the year till the number of days between the start and end date.

Also, note that this will always give you an integer value that represents the total number of weeks between these two dates. It would automatically round up the result, so if there are 16 days, it would give you three weeks.

**[_Click here to download the example file_](https://www.dropbox.com/scl/fi/auty675xql7u72a21dyt1/Weeks-Between-Dates.xlsx?rlkey=sxmx6dzkle5fx6fo9xyu1tyjo&dl=1)
**

These are some simple formula methods you can use to quickly calculate the number of weeks between two given dates.

I hope you found this article useful. If you know of any other method that can be used to do this, please share with us in the comments section.

**Other Excel articles you may also like:**

*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    
*   [Excel WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    
*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/weeks-between-two-dates-excel/#respond)

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