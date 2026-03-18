# Convert Month Name to Number in Excel

**Source:** https://trumpexcel.com/convert-month-name-to-number-excel

---

[Skip to content](https://trumpexcel.com/convert-month-name-to-number-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-month-name-to-number-excel/#below-title)

In some situations, you may have the month name that you want to convert into the month number so that it can be used further in calculations.

While there is no built-in function to do this in Excel, it’s pretty easy with simple formula workarounds.

In this article, I will show you a couple of methods for converting month names to numbers in Excel.

So, let’s see how to do this!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-month-name-to-number-excel/#)

Using the MONTH Function
------------------------

Below, I have a data set where I have month names in column A, and I want to get their month number in column B.

![Data set to find month number from name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20407'%3E%3C/svg%3E)

Here is the formula to do this:

\=MONTH("1"&A2)

![MONTH formula to get month number from name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20453'%3E%3C/svg%3E)

The above formula converts the month name into a more recognizable date format for Excel. So January is converted to _1January_.

Now, when I use the MONTH function to fetch the month name from this date, it correctly identifies this as January and gives me the month number as 1.

For this to work correctly, you need to ensure that your month name is in a format that Excel can recognize as a date, such as January or Jan.

Also read: [How to Get Month Name from Date in Excel](https://trumpexcel.com/get-month-name-from-date-excel/)

Using MATCH Function
--------------------

Another way to convert the month name to the month number is by using the MATCH function.

In this method, you manually enter all the month names, and then the match function can find the name and give you the corresponding position.

Below, I have a dataset where I have month names in column A, and I want to get their month number in column B:

![Data set to find month number from name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20407'%3E%3C/svg%3E)

Below is the formula that will do this:

\=MATCH(A2,{"January","February","March","April","May","June","July","August","September","October","November","December"},0)

One benefit of this method is that it allows you to rearrange the month names if you want.

For example, if I’m working with the data set where my financial year is from April to March, and I want April to be month 1 and May to be month 2, and so on, I can modify the formula as shown below:

\=MATCH(A2,{"April","May","June","July","August","September","October","November","December","January","February","March"},0)

Using VLOOKUP Function
----------------------

If you need to convert the month name into the corresponding number often in the same workbook, it would be more efficient to create a table with the month name in one column and the number in another column and then use VLOOKUP to fetch the value.

Below, I have month names in column A, and I want to get their month number in column B. I have also created a table (named Table1) that lists all the months and the numbers, as shown below:

![Dataset with table with month name and number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20407'%3E%3C/svg%3E)

Below is the VLOOKUP formula I can use to fetch the month number based on the month’s name:

\=VLOOKUP(A2,Table1,2,0)

![VLOOKUP formula to convert month name to number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20449'%3E%3C/svg%3E)

or, if you have the [XLOOKUP function](https://trumpexcel.com/xlookup-function/)
, then you can use the below formula as well:

\=XLOOKUP(A2,Table1\[Name\],Table1\[Number\],"",0)

_Also read: [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)
_

VBA Custom Function to Convert Month Name to Number
---------------------------------------------------

Another way to do this is by [creating your own custom function using VBA](https://trumpexcel.com/user-defined-function-vba/)
, and then use that function wherever you want to convert month name into number.

Below is the VBA code that would create a custom function that takes the month name as the input and converts it into the corresponding number.

    Function MonthNameToNumber(monthName As String) As Integer
        Select Case LCase(monthName)
            Case "january": MonthNameToNumber = 1
            Case "february": MonthNameToNumber = 2
            Case "march": MonthNameToNumber = 3
            Case "april": MonthNameToNumber = 4
            Case "may": MonthNameToNumber = 5
            Case "june": MonthNameToNumber = 6
            Case "july": MonthNameToNumber = 7
            Case "august": MonthNameToNumber = 8
            Case "september": MonthNameToNumber = 9
            Case "october": MonthNameToNumber = 10
            Case "november": MonthNameToNumber = 11
            Case "december": MonthNameToNumber = 12
            Case Else: MonthNameToNumber = 0 ' Invalid month name
        End Select
    End Function

Below are the steps to use this VBA code in your Excel file:

1.  Hold the ALT key and press the F11 key to open the VB editor. Alternatively, you can also click on the Developer tab and then click on the Visual Basic icon to [open the VB editor](https://trumpexcel.com/visual-basic-editor/)
    .
2.  In the VB editor, click on the Insert option in the menu and then click on Module.
3.  In the module code window, copy and paste the above VBA macro code.
4.  Click on the save icon in the VB editor and close it.

Now, you can use _MonthNameToNumber_ as any other regular worksheet function in your workbook.

\=MonthNameToNumber(A2)

![VBA Custom function to get month number from name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20456'%3E%3C/svg%3E)

These are some of the methods you can use to quickly convert a month’s name into its corresponding month number in Excel.

While the easiest would be to use the MONTH name function, the other methods I’ve covered offer you a little more flexibility if you’re dealing with inconsistent data sets.

I hope you found this article helpful. In case you have any questions or suggestions, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Sort Dates By Month in Excel](https://trumpexcel.com/sort-dates-by-month-excel/)
    
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Get the First Day of the Month in Excel](https://trumpexcel.com/first-day-of-month-excel/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Calculate Number of Days Between Two Dates](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)
    
*   [Last Date of the Year in Excel (Formula)](https://trumpexcel.com/end-of-year-formula-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-month-name-to-number-excel/#respond)

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