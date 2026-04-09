# Volatile Formulas Detected in Excel - Keep Your Distance

**Source:** https://trumpexcel.com/excel-volatile-formulas

---

[Skip to content](https://trumpexcel.com/excel-volatile-formulas/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-volatile-formulas/#below-title)

Last week, I came across an Excel problem in a forum.

I immediately sprung into action and created a long formula that started with [OFFSET()](https://trumpexcel.com/excel-offset-function/)
.

Within a few hours, it was shot down by other Excel experts as it contained volatile formulas.

_I immediately recognized the cardinal sin I had committed._

So with this confession, let me share what I have learned about volatile functions in Excel.

In plain simple terms, it is a function that will make your Excel [spreadsheet slow](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
, as it recalculates the formula repeatedly.

Several actions can trigger this (described later in this article).

A very simple example of a volatile function is the NOW() function (to get the current date and time in a cell). Whenever you edit any cell in a worksheet, it gets recalculated. 

This is fine if you have a small data set and less number of formulas, but when you have large spreadsheets, this could significantly slow down the processing.

Here is a list of some common volatile functions which should be avoided:

Higghly Volatile Formulas:
--------------------------

*   [RAND()](https://trumpexcel.com/excel-rand-function/)
    
*   [NOW()](https://trumpexcel.com/excel-now-function/)
    
*   [TODAY()](https://trumpexcel.com/excel-today-function/)
    

Almost Volatile Formulas:
-------------------------

*   [OFFSET()](https://trumpexcel.com/excel-offset-function/)
    
*   CELL()
*   [INDIRECT()](https://trumpexcel.com/excel-indirect-function/)
    
*   INFO()

The good news is my favorite [INDEX()](https://trumpexcel.com/excel-index-function/)
, [ROWS()](https://trumpexcel.com/excel-rows-function/)
, and [COLUMNS()](https://trumpexcel.com/excel-columns-function/)
 don’t exhibit volatility.

The bad news is that [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 is volatile.

Also, ensure that you do not have these functions inside non-volatile functions, such as IF(), LARGE(), SUMIFS(), and COUNTIFS(), as this would eventually make the entire formula volatile.

For example, suppose you have a formula =If(A1>B1, “Trump Excel”,RAND()). Now, if A1 is greater than B1, it returns Trump Excel, but if it is not, then it returns RAND(), which is a volatile function.

Also read: [Excel Formulas Not Working](https://trumpexcel.com/excel-formulas-not-working/)

Triggers that Recalculate Volatile Formulas in Excel
----------------------------------------------------

*   Entering new data (if Excel is in Automatic recalculation mode).
*   Explicitly instructing Excel to recalculate all or part of a workbook.
*   Deleting or inserting a row or column.
*   Saving a workbook while the _‘Recalculate before save’_ option is set (it’s in File–> Options–> Formula).
*   Performing certain Autofilter actions.
*   Double-clicking a row or column divider (in Automatic calculation mode).
*   Adding, editing, or deleting a defined name.
*   Renaming a worksheet.
*   Changing the position of a worksheet in relation to other worksheets.
*   Hiding or unhiding rows, but not columns.

If you have a lot of formulas in your worksheet that are making it slow, I suggest you switch to Manual Calculation Mode.

This stops automatic recalculation and gives you the power to tell Excel when to calculate (by clicking ‘Calculate Now’ or pressing F9).

This option is available in Formulas –> Calculation Options.

![Volatile Formulas - Manual Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20183'%3E%3C/svg%3E)

###### **Related Excel Tutorials**:

*   [10 Super Neat Ways to Clean Data in Excel Spreadsheets](https://trumpexcel.com/clean-data-in-excel/)
    .
*   [10 Excel Data Entry Tips You Can’t Afford to Miss](https://trumpexcel.com/excel-data-entry-tips/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Volatile Formulas Detected in Excel – Keep Your Distance”
------------------------------------------------------------------------

1.  I try to avoid this problem in my Excel environment, but this blog illustrates that “errors” can sometimes be useful when used intelligently. Thank you!
    
    [Reply](https://trumpexcel.com/excel-volatile-formulas/#comment-14468)
    
2.  I have a very complex workbook that contained multiple NOW() and TODAY() references and as it grew in size through the year the macro that ran transaction posting begin to take longer and longer.
    
    1\. I replaced all references to NOW() and TODAY() with a pointer to a cell in my TBL worksheet named NVDate (Non-Volatile Date).
    
    2\. Then I added the following code to the ThisWorkbook object:
    
    Private Sub Workbook\_Open()  
    ‘Seed NVDate to eliminae volatile Today() and Now() functions  
    TBL.Range(“NVDate”).Value = Date  
    End Sub
    
    The gain in speed was astounding. A transaction that had been taking 9 seconds to post was now running in less than a second.
    
    [Reply](https://trumpexcel.com/excel-volatile-formulas/#comment-12536)
    
    *   Thanks for this code. Very helpful, but FOLLOWING DETAIL might be helpful to some.
        
        Private Sub Workbook\_Open()  
        ‘Seed NVDate to eliminae volatile Today() and Now() functions  
        Worksheets(“TBL”).Range(“NVDate”).Value = Date  
        End Sub
        
        [Reply](https://trumpexcel.com/excel-volatile-formulas/#comment-13712)
        
3.  vlookup() is volatile as well afaik
    
    [Reply](https://trumpexcel.com/excel-volatile-formulas/#comment-12494)
    
4.  Nice
    
    [Reply](https://trumpexcel.com/excel-volatile-formulas/#comment-41)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-volatile-formulas/#respond)

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