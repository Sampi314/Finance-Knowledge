# How To Convert Date To Serial Number In Excel? 3 Easy Ways!

**Source:** https://trumpexcel.com/convert-date-to-serial-number-excel

---

[Skip to content](https://trumpexcel.com/convert-date-to-serial-number-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-date-to-serial-number-excel/#below-title)

There are multiple ways you can display a number in a cell in Excel. And one of the ways you can format a number is to show it as a date (for that corresponding serial number)

When you see a date in a cell in Excel, in the back end it is still stored as a number.

In some cases, you may not want to show the date and instead show the serial number it represents. For example, instead of showing 31 Dec 2022 in a cell, you may want to show its numerical value, which is 44926.

In this tutorial, I will show you some simple ways you can use to convert a date into a serial number in Excel. I will also show you the method that would work in case you have the dates in the text format.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-date-to-serial-number-excel/#)

How To Convert Date To Serial Number In Excel?
----------------------------------------------

As I mentioned, dates are stored as numbers in the back-end in Excel.

So if you have a date in a cell and you want to show the serial number instead, all you need to do is change the format so that the serial number is displayed.

You can either use the option in the ribbon to quickly convert any date into a serial number, or you can use the custom formatting dialog box that gives you a lot more control.

Let me show you both of these methods here.

### Using the Format Drop-down in the Ribbon (Quick Method)

Below I have some dates in column A that I want to convert into numbers.

![Dates in a column in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20363'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select all the dates in Column A
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20391%20221'%3E%3C/svg%3E)

3.  In the Number group, click on the Format drop-down
4.  Select General

![Select the General option in the format drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20529%20560'%3E%3C/svg%3E)

The above steps would instantly convert the format of all the cells from Date to General.

![Dates converted to serial numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20361'%3E%3C/svg%3E)

A general format is where no specific formatting has been applied, so a number would be shown as a number (and if there are dates in the selected cells, these would be converted back to its serial numbers).

Note that this method will only work if the date in the cell is in a format that Excel recognizes as a date. For example, if you have a date as ‘Dec 31 2022′ or ’12 31 2022’, these will not be converted into their serial number, because Excel does not recognize these as a valid date format.

Below I have some commonly used valid date formats in Excel.

| Valid Date Formats in Excel |
| --- |
| 12-31-2022 |
| 31 Dec 2022 |
| 31 December 2022 |
| 31-12-22 |
| 31.12.2022 |

Also read: [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)

### Using the Format Cells Dialog Box (Gives More Control)

Another great way to show dates as numbers would be by using the Format Cells dialog box.

While it also works by changing the cell formatting from a date to a number, when compared with the above method where we used the Format drop-down and chose the General option, this method gives you a little more control.

Assuming I have the same data set where I have dates in column a comma below are the steps to convert these dates into serial numbers:

![Dates in a column in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20363'%3E%3C/svg%3E)

Below are the steps to do this using the ‘Format Cells’ dialog box:

1.  Select all the dates in Column A
2.  Click the Home tab
3.  In the Number group, click on the small dialog box launcher (the tilted arrow as shown below)

![Click on dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20391%20167'%3E%3C/svg%3E)

4.  In the Format Cells dialog box, make sure the Number tab is selected

![Make sure number tab is selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the Category options, select the Number option

![Select the Number category](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20363'%3E%3C/svg%3E)

6.  \[Optional\] If you need the number to have decimal places as well, specify how many decimal places you need. In this example, I will make this 0 (as I don’t want any decimal numbers)

![Specify the decimal places](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20350'%3E%3C/svg%3E)

7.  \[Optional\] If you want the number to have a thousand separator, you can check the ‘Use 1000 Separator option’

![Use thousand separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

8.  Click OK

The above steps would also give you the same result, where the date will now be shown as its serial number.

![Dates converted to serial numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20365'%3E%3C/svg%3E)

While this may look like a longer way to convert dates to numbers, you can see that you get a lot more control when using the Format Cells dialog box. You can specify whether you need 1000 separators or decimal places.

Apart from this, it also shows you the option where you can select if you want to show negative numbers in red (with or without a negative sign). Of course, this is not quite useful as a date can never be negative in Excel.

Again, this method is only going to work for dates that are considered a valid date format by Excel. If a cell has a date that’s not recognized as a valid date format, and you use the above method to convert it into a serial number, nothing would happen.

Also read: [How to Convert Text to Date in Excel](https://trumpexcel.com/convert-text-to-date-excel/)

Change Date in Text Format to Serial Number (Using DATEVALUE)
-------------------------------------------------------------

If you have the dates in a proper format, which means that they are numbers in the back end, then you can simply change the cell format to show the serial number instead of the date (using any of the two methods shown above).

But in many cases, you may get a column full of dates that are text strings and not numbers in the back end.

In my experience, this often happens when you download your data from a database or from the web. It recently happened when I downloaded my bank statement as an Excel file, and the date column had text strings.

And many times, people add an apostrophe before the date to make a text string.

In such cases, changing the cell format is not going to give you the serial number for that date.

But there is a workaround – the [DATEVALUE function](https://trumpexcel.com/excel-datevalue-function/)
.

The DATEVALUE function is made specifically for this use case, where it takes the date in the text format as the input and gives you the serial number for that date.

Below I have a column where I have dates in text format for which I want to get the serial number.

![Date in Text Format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20362%20400'%3E%3C/svg%3E)

And below is the formula that will do this for me:

\=DATEVALUE(A2)

![Datevalue function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20433'%3E%3C/svg%3E)

One useful use case of this function is when you have dates in the text format, and you want to convert these into proper date format.

While you cannot do that when the dates are in the text format, you can first use the DATEVALUE function to convert it into the corresponding serial number, and then change the formatting of the dates

Note that the DATEVALUE function only works with text data. So if you have cells that have dates in proper format (that are stored as numbers in the back end), this formula would give you a value error.

Convert Date to Number in the MMDDYYYY or DDMMYYY Format
--------------------------------------------------------

In some, not-so-common, situations users may want to convert a date into an 8-digit number in the DDMMYYYY or the MMDDYYY format.

For example, 31 Dec 2022 would be 31122022 in the DDMMYYYY format and 12312022 in the MMDDYYYY format.

While it may look like a complex problem to solve, the fact that you can specify you’re own custom formatting in Excel makes it an easy task.

Below I have some dates in column E that I want to show in the 8-digit MMDDYYYY format.

![Dates in a column in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20363'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select all the cells that contain the dates
2.  Hold the Control key and press the 1 key. This will open the Format Cells dialog box. if you’re using a Mac use the Command key instead of the Control key
3.  In the format cells dialog box, make sure ‘Number’ tab is selected
4.  In the Category options, select ‘Custom’

![Select the custom option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the Type field, enter **mmddyyyy**

![Enter mmddyyyy in the format field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20350'%3E%3C/svg%3E)

6.  Click on OK

The above steps would change the format of the selected cells and make sure that any number is shown in the MMDDYYYY format.

![Dates in 8 digit format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20357'%3E%3C/svg%3E)

Note that this would only work if you have numerical values in the cells. In case you have text values, all numbers that have been formatted as text, this wouldn’t work.

In case you want to show the dates in the DDMMYYYY format, use ddmmyyyy in step 5.

In this tutorial, I showed you **how to convert dates into serial numbers in Excel**. If you have the dates in the proper format (i.e., these are numbers in the back end), you can get the serial number by changing the cell format using the Format Cells dialog box (or the General option in the Ribbon).

In case you have dates that are in the text format, you need to use the DATEVALUE function to convert these dates into the corresponding serial numbers.

I also covered how to convert dates into the 8-digit format – MMDDYYYY or DDMMYYYY.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [Convert Scientific Notation to Number or Text in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)
    
*   [Combine Date and Time in Excel](https://trumpexcel.com/combine-date-time-excel/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-date-to-serial-number-excel/#respond)

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