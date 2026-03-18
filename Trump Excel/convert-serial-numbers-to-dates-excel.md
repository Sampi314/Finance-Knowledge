# Convert Serial Numbers to Dates in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/convert-serial-numbers-to-dates-excel

---

[Skip to content](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/#below-title)

Excel stores date and time values as serial numbers in the back end.

This means that while you may see a date such as “10 January 2020” or “01/10/2020” in a cell, in the back-end, Excel is storing that as a number. This is useful as it also allows users to easily add/subtract date and time in Excel.

In Microsoft Excel for Windows, “01 Jan 1900” is stored as 1, “02 Jan 1900” is stored as 2, and so on.

Below, both columns have the same numbers, but Column A shows numbers and Column B shows the date that’s represented by that number.

![Same numeric value as number and as date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20292'%3E%3C/svg%3E)

This is also the reason that sometimes you may expect a date in a cell but end up seeing a number. I see this happening all the time when I download data from databases or web-based tools.

It happens when the cell format is set to show a number as a number instead of a date.

So how can we **convert these serial numbers into dates**?

That’s what this tutorial is all about.

In this tutorial, I would show you two really easy ways to convert serial numbers into dates in Excel

_Note: Excel for Windows uses the 1900 date system (which means that 1 would represent 01 Jan 1900, while Excel for Mac uses the 1904 date system (which men’s that 1 would represent 01 Jan 1904 in Excel in Mac)_

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/#)

Convert Serial Numbers to Dates Using Number Formatting
-------------------------------------------------------

The easiest way to convert a date serial number into a date is by changing the formatting of the cells that have these numbers.

You can find some of the commonly used date formats in the Home tab in the ribbon

Let me show you how to do this.

### Using the In-Built Date Format Options in the Ribbon

Suppose you have a data set as shown below, and you want to convert all these numbers in column A into the corresponding date that it represents.

![Dataset that has the numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20510'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells that have the number that you want to convert into a date![Select the cells that have the numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20315%20457'%3E%3C/svg%3E)
2.  Click the ‘Home’ tab![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20205'%3E%3C/svg%3E)
3.  In the ‘Number’ group, click on the Number Formatting drop-down![Click on the number formatting drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20200'%3E%3C/svg%3E)
4.  In the drop-down, select ‘Long Date’ or Short Date’ option (based on what format would you want these numbers to be in)![Select the long date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20397%20729'%3E%3C/svg%3E)

That’s it!

The above steps would convert the numbers into the selected date format.

![Serial numbers converted to dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20306%20448'%3E%3C/svg%3E)

The above steps have not changed the value in the cell, only the way it’s being displayed.

Note that Excel picks up the short date formatting based on your system’s regional setting. For example, if you’re in the US, then the [date format](https://trumpexcel.com/change-date-format-excel/)
 would be MM/DD/YYYY, and if you are in the UK, then the date format would be DD/MM/YYYY.

While this is a quick method to convert serial numbers into dates, it has a couple of limitations:

*   There are only two date formats – short date and long date (and that too in a specific format). So, if you want to only get the month and the year and not the day, you won’t be able to do that using these options.
*   You cannot show date as well as time using the formatting options in the drop-down. You can either choose to display the date or the time but not both.

So, if you need more flexibility in the way you want to show dates in Excel, you need to use the Custom Number Formatting option (covered next in this tutorial).

Sometimes when you convert a number into a date in Excel, instead of the date you may see some hash signs (something like #####). this happens when the column width is not enough to accommodate the entire date. In such a case, just [increase the width of the column](https://trumpexcel.com/autofit-excel/)
.

Also read: [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)

### Creating a Custom Date Format Using Number Formatting Dialog Box

Suppose you have a data set as shown below and you want to convert the serial numbers in column A into dates in the following format – 01.01.2020

![Dataset that has the numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20510'%3E%3C/svg%3E)

Note that this option is not available by default in the ribbon method that we covered earlier.

Below are the steps to do this:

1.  Select the cells that have the number that you want to convert into a date
2.  Click the ‘Home’ tab
3.  In the Numbers group, click on the dialog box launcher icon (it’s a small tilted arrow at the bottom right of the group)![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20204'%3E%3C/svg%3E)
4.  In the ‘Format Cells’ dialog box that opens up, make sure the ‘Number’ tab selected![Make sure numnber tab is selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
5.  In the ‘Category’ options on the left, select ‘Date’![Select date from the category list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
6.  Select the desired formatting from the ‘Type’ box.![Select the format in which you want the dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
7.  Click OK

The above steps would convert the numbers into the selected date format.

![Final result with the desired date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20451'%3E%3C/svg%3E)

As you can see, there are more date formatting options in this case (as compared with the short and long date we got with the ribbon).

And in case you do not find the format you are looking for, you can also create your own date format.

For example, let’s say that I want to show the date in the following format – 01/01/2020 (which is not already an option in the format cells dialog box).

Here is how I can do this:

1.  Select the cells that have the numbers that you want to convert into a date
2.  Click the Home tab
3.  In the Numbers group, click on the dialog box launcher icon (it’s a small tilt arrow at the bottom right of the group)
4.  In the ‘Format Cells’ dialog box that opens up, make sure the ‘Number’ tab selected
5.  In the ‘Category’ options on the left, select ‘Custom’![Select custom in the format cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
6.  In the field on the right, enter
    
    mm/dd/yyyy
    
    ![Enter mmddyyyy format in the type field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
    
7.  Click OK

The above steps would change all the numbers into the specified number format.

![Result in the specified date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20457'%3E%3C/svg%3E)

With custom format, you get full control and it allows you to show the date in whatever format you want. You can also create a format where it shows the date as well time in the same cell.

For example, in the same example, if you want to show date as well as time, you can use the below format:

mm/dd/yyyy hh:mm AM/PM

Below is the table that shows the date format codes you can use:

|     |     |
| --- | --- |
| **Date Formatting Code** | **How it Formats the Date** |
| m   | Shows the Month as a number from 1–12 |
| mm  | Show the months as two-digit numbers from 01–12 |
| mmm | Shows the Month as three-letter as in Jan–Dec |
| mmmm | Shows the [Months full name](https://trumpexcel.com/get-month-name-from-date-excel/)<br> as in January–December |
| mmmmm | Shows the Month name first alphabet as in J-D |
| d   | Shows Days as 1–31 |
| dd  | Shows Days as 01–31 |
| ddd | Shows Days as Sun–Sat |
| dddd | Shows Days as Sunday–Saturday |
| yy  | Shows Years as 00–99 |
| yyyy | Shows Years as 1900–9999 |

Also read: [How to Convert Text to Date in Excel (Easy Formulas)](https://trumpexcel.com/convert-text-to-date-excel/)

Convert Serial Numbers to Dates Using TEXT Formula
--------------------------------------------------

The methods covered above work by changing the formatting of the cells that have the numbers.

But in some cases, you may not be able to use these methods.

For example, below I have a data set where the numbers have a leading apostrophe – which converts these numbers into text.

![Numbers with apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20480'%3E%3C/svg%3E)

If you try and using the inbuilt options to change the formatting of the cells with this data set, it would not do anything. This is because Excel does not consider these as numbers, and since dates for numbers, Excel refuses your wish to format these.

In such a case, you can either [convert these text to numbers](https://trumpexcel.com/convert-text-to-numbers-excel/)
 and then use the above-covered formatting methods, or use another technique to convert serial numbers into dates – **using the [TEXT function](https://trumpexcel.com/excel-text-function/)
**.

The TEXT function takes two arguments – the number that needs to be formatted, and the format code.

Suppose you have a data set as shown below, and you want to convert all the numbers and column A into dates.

![Dataset to convert numbers to dates using the TEXT formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20438'%3E%3C/svg%3E)

Below the formula that could do that:

\=TEXT(A2,"MM/DD/YYYY")

![TEXT formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20480'%3E%3C/svg%3E)

Note that in the formula I have specified the date formatting to be in the MM/DD/YYYY format. If you need to use any other formatting, you can specify the code for it as the second argument of the TEXT formula.

You can also use this formula to show the date as well as the time.

For example, if you want the final result to be in the format – 01/01/2020 12:00 AM, use the below formula:

\=TEXT(A2,"mm/dd/yyyy hh:mm AM/PM")

In the above formula, I have added the time format as well so if there are decimal parts in the numbers, it would be shown as the time in hours and minutes.

If you only want the date (and not the underlying formula), [convert the formulas into static values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 by using [paste special](https://trumpexcel.com/excel-paste-special-shortcuts/)
.

One big advantage of using the TEXT function to convert serial numbers into dates is that you can [combine the TEXT formula result](https://trumpexcel.com/convert-date-to-text-excel/)
 with other formulas. For example, you can combine the resulting date with the text and show something such as – _The Due Date is 01-Jan-2020_ or _The Deadline is 01-Jan-2020_

_Note: Remember dates and time are stored as numbers, where every integer number would represent one full day and the decimal part would represent that much part of the day. So 1 would mean 1 full day and  0.5 would mean half-a-day or 12 hours._

So these are two simple ways you can use to convert serial numbers to dates in Microsoft Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Excel DATEVALUE Function – Convert Date in Text into Serial Date Formats](https://trumpexcel.com/excel-datevalue-function/)
    
*   [How to Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [Convert Scientific Notation to Number or Text in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    
*   [How to Format Phone Numbers in Excel?](https://trumpexcel.com/format-phone-numbers-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Convert Serial Numbers to Dates in Excel”
--------------------------------------------------------------

1.  your website is amazing  
    really helped me alot,reduced my anxiety of deadlines.  
    thank you very much.  
    keep doing all good work.
    
    I am from south africa.
    
    [Reply](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/#comment-36160)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/#respond)

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