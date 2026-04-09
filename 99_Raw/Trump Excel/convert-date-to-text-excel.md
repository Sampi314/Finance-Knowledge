# Convert Date to Text in Excel - Explained with Examples

**Source:** https://trumpexcel.com/convert-date-to-text-excel

---

[Skip to content](https://trumpexcel.com/convert-date-to-text-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-date-to-text-excel/#below-title)

**Watch video – Convert Date to Text in Excel**

Date and Time in Excel are stored as numbers. This enables a user to use these dates and [time in calculations](https://trumpexcel.com/calculate-time-in-excel/)
. For example, you can add a specific number of days or hours to a given date.

However, sometimes you may want these dates to behave like text. In such cases, you need to know how to convert the date to text.

Below is an example where dates are combined with text. You can see that the dates don’t retain their format and show up as numbers in the combined text.

![Convert Date to Text - Problem Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20213'%3E%3C/svg%3E)

In such situations, it’s required to convert a date into text.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-date-to-text-excel/#)

Convert Date to Text in Excel
-----------------------------

In this tutorial, you’ll learn three ways to convert the date to text in Excel:

*   Using the Text Function
*   Using the Text to Column feature
*   Using the Copy-Paste method

### Convert Date to Text using Text Function

[TEXT function](https://trumpexcel.com/excel-text-function/)
 is best used when you want to display a value in a specific format. In this case, it would be to display the date (which is a number) in the [date format](https://trumpexcel.com/change-date-format-excel/)
.

Let’s first see how the text function works.

Here is the syntax:

\=TEXT(value, format\_text)

It takes two arguments:

*   **value** –  the number that you want to convert into text. This can be a number, a cell reference that contains a number, or a formula result that returns a number.
*   **format\_text** – the format in which you want to display the number. The format needs to be specified within double quotes.

Using the Text function requires a basic understanding of the formats that you can use in it.

In the case of dates, there are four parts to the format:

*   day format
*   month format
*   year format
*   separator

Here are the formats you can use for each part:

*   **Day Format:**
    *   **d** – it shows the day number without a leading zero. So 2 will be shown as 2 and 12 will be shown as 12.
    *   **dd** – it shows the day number with a leading zero. So 2 will be shown as 02, and 12 will be shown as 12
    *   **ddd** – it shows the [day name](https://trumpexcel.com/get-day-name-from-date-excel/)
         as a three letter abbreviation of the day. For example, if the day is a Monday, it will show Mon.
    *   **dddd** – it shows the full name of the day. For example, if it’s Monday, it will be shown as Monday.
*   **Month Format:**
    *   **m** – it shows the month number without a leading zero. So 2 will be shown as 2 and 12 will be shown as 12.
    *   **mm** – it shows the month number with a leading zero. So 2 will be shown as 02, and 12 will be shown as 12
    *   **mmm** – it shows the month name as a three letter abbreviation of the day. For example, if the month is August, it will show Aug.
    *   **mmmm** – it shows the [full name of the month](https://trumpexcel.com/get-month-name-from-date-excel/)
        . For example, if the month is August, it will show August.
*   **Year Format:**
    *   **yy** – it shows the two digit year number. For example, if it is 2016, it will show 16.
    *   **yyyy** – it shows the four digit year number. For example, if it is 2016, it will show 2016.
*   **Separator:**
    *   **/ (forward slash)**: A forward slash can be used to separate the day, month, and year part of a date. For example, if you specify “dd/mmm/yyyy” as the format, it would return a date with the following format: 31/12/2016.
    *   **– (dash)**: A dash can be used to separate the day, month, and year part of a date. For example, if you specify “dd-mmm-yyyy” as the format, it would return a date with the following format: 31-12-2016.
    *   **Space and comma**: You can also combine space and comma to create a format such as “dd mmm, yyyy”. This would show the date in the following format: 31 Mar, 2016.

Let’s see a few examples of how to use the TEXT function to convert date to text in Excel.

#### Example 1: Converting a Specified Date to Text

Let’s again take the example of the date of joining:

![Convert Date to Text - Problem Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20213'%3E%3C/svg%3E)

Here’s the formula that will give you the right result:

\=A2&"'s joining date is "&TEXT(B2,"dd-mm-yyyy")

![Convert Date to Text - Joining date example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20199'%3E%3C/svg%3E)

Note that instead of using the cell reference that has the date, we have used the TEXT function to convert it into text using the specified format.

Below are some variations of different formats that you can use:

![Convert Date to Text - sample formats](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20210'%3E%3C/svg%3E)

You can experiment with other formats as well and create your own combinations.

Also read: [How to Convert Text to Date in Excel (8 Easy Ways)](https://trumpexcel.com/convert-text-to-date-excel/)

#### Example 2: Converting Current Date to Text

To convert the current date into text, you can use the [TODAY function](https://trumpexcel.com/excel-today-function/)
 along with the TEXT function.

Here is a formula that will do it:

\="Today is "&TEXT(TODAY(),"dd/mm/yyyy")

This could be useful in dashboards/reports, where as soon as the file is opened (or any changes are made), the date refreshes to show the current date.

![Convert Date to Text - current date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20103'%3E%3C/svg%3E)

### Convert Date to Text using Text to Column

If you’re not a fan of [Excel formulas](https://trumpexcel.com/excel-functions/)
, there is another cool way to quickly convert date to text in Excel – the Text to Column feature.

Suppose you have a dataset as shown below and you want to convert these dates into text format:

![Convert Date to Text - text to column 1a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20345%20165'%3E%3C/svg%3E)

Here are the steps to do this:

*   Select all the cells that contain dates that you want to convert to text.
*   Go to Data –> Data Tools –> Text to Column.![Convert Date to Text - text to column 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20138'%3E%3C/svg%3E)
*   In the Text to Column Wizard, make the following selections:
    *   Step 1 of 3: Make sure Delimited is selected and click on Next.![Convert Date to Text - text to column 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20420'%3E%3C/svg%3E)
    *   Step 2 of 3: In the delimiter options, make sure none of the options is selected. Deselect the one which is selected by default and click on Next.![Convert Date to Text - text to column 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20419'%3E%3C/svg%3E)
    *   Step 3 of 3: Select Text in the ‘Column data format’ options and specify the destination cell (B2 in this example) and click on Finish.![Convert Date to Text - text to column 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20421'%3E%3C/svg%3E)

This would instantly convert the dates into text format.

![Convert Date to Text - text to column 6](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20347%20168'%3E%3C/svg%3E)

Note: There is a difference in the format of the dates in the two columns. While the original format had dd mmm, yyyy format, the result is dd-mm-yyyy. Remember that the Text to Column feature will always convert dates to the default short date format (which is dd-mm-yyyy as per my systems regional settings. It could be different for yours).

Also read: [How to Convert Serial Numbers to Dates in Excel (2 Easy Ways)](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)

If you want the date in other formats, use the formula method, or the copy-paste method shown below.

### Convert Date to Text using the Copy-Paste Method

This is the fastest way to convert date to text.

Here are the steps:

*   Select the cells that have dates that you want to convert and copy it.![Convert Date to Text - copy paste 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20202'%3E%3C/svg%3E)
*   Open a Notepad and paste it there. As soon as you paste the dates in the notepad, it automatically gets converted into text.![Convert Date to Text - copy paste 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20359%20232'%3E%3C/svg%3E)
*   Now switch back to the Excel and select the cells where you want to paste these dates.
*   With the cells selected, go to Home –> Number and select the Text format (from the drop down).![Convert Date to Text - copy paste 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20185%20407'%3E%3C/svg%3E)
*   Now go back to the notepad, copy the dates and paste it in Excel. You’ll see that the dates have been converted into text.

![Convert Date to Text - copy paste 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20170'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [Convert Text to Numbers in Excel – A Step By Step Tutorial](https://trumpexcel.com/convert-text-to-numbers-excel/)
    .
*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   [How to Quickly Transpose Data in Excel](https://trumpexcel.com/transpose-data-excel/)
    .
*   [\[Quick Tip\] How to Split Cells in Excel](https://trumpexcel.com/split-cells-in-excel/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [How to Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [How to Remove Time from Date in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Convert Date to Text in Excel – Explained with Examples”
----------------------------------------------------------------------

1.  Thank you for straight forward solution!!!
    
    [Reply](https://trumpexcel.com/convert-date-to-text-excel/#comment-12284)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-date-to-text-excel/#respond)

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