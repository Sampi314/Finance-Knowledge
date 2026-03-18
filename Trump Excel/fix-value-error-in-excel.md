# How to Fix #VALUE Error in Excel?

**Source:** https://trumpexcel.com/fix-value-error-in-excel

---

[Skip to content](https://trumpexcel.com/fix-value-error-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/fix-value-error-in-excel/#below-title)

When you’re working formulas in Excel, many times you will encounter the #VALUE error.

While the error is quite generic and doesn’t tell you what the problem is, in most cases, this happens when you give a formula a data type that is not expected (explained with examples below).

For example, if you have a few numbers that you’re adding in Excel, and you also try and add a text value in the same formula, Excel will give you an error. This is because Excel expects only numbers to be used in addition or subtraction.

While the easiest way to tackle the #VALUE error would be to make sure that the [data types](https://trumpexcel.com/vba-data-types-variables-constants/)
 are correct in the formulas, it may not always be possible.

In this tutorial, I will show you a couple of methods you can use to **get rid of the value error in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/fix-value-error-in-excel/#)

Value Error Becuase of Text String in Formulas
----------------------------------------------

Some formulas are designed to only work with numbers.

And when there are non-numbers (such as [text strings](https://trumpexcel.com/count-cells-that-contain-text/)
) used in the formula, you may see a value error.

In the image below is a very simple example where I need to add the scores of a student in different subjects.

While I have the numbers for all the subjects, I don’t have them for Math (and there is NA written instead of the score value).

If I use a simple arithmetic equation to get the sum of all the scores, I will get a value as shown below.

![VALUE error when adding scores](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20146'%3E%3C/svg%3E)

This is because the formula expects the only add numbers and I’m referencing a cell that has a text string instead.

**How to tackle this?**

In such simple addition subtraction formulas, one way to get rid of the error would be to remove the text string so that only numbers are left that can be added.

In our above example, if I remove the text ‘NA’ from the cell, the formula would work just fine.

Another way you can tackle this VALUE error is by using in-built functions instead of using the arithmetic equation.

Many of the commonly used Excel formulas are built in a way where they ignore any unexpected data type that is not supported by the formula.

For example, in this case, you can use the [SUM formula](https://trumpexcel.com/excel-sum-function/)
, which would ignore all the text strings and only add the numbers.

![SUM formula ignored text strings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20147'%3E%3C/svg%3E)

Another possible reason that can give you a value error is when you have a space character in a cell that you have referenced in a formula. While most of the formulas are designed to ignore empty cells with space characters, in case you are using a simple arithmetic equation to add or subtract values, having a space character in a cell could give you a value error (as a space character is considered a text string).

Also read: [Excel Formulas Not Working](https://trumpexcel.com/excel-formulas-not-working/)

Value Error Because of Incorrect Argument Type in Formulas
----------------------------------------------------------

If you’re using a formula that gives you a value error, there’s a good chance you have used an argument that is not the expected data type in the formula.

Let me give you an example and explain.

Below I have the year, month, and day value in three separate cells.

If I use this data in the [DATE formula](https://trumpexcel.com/excel-date-function/)
 to get the serial number of this date, it is going to give me a value error.

![DATE formula giving a VALUE error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20174'%3E%3C/svg%3E)

This is because the date formula expects only numeric values as arguments, and in this formula, I have the [month name](https://trumpexcel.com/get-month-name-from-date-excel/)
 which is a text string.

**How to tackle this?**

Check and double-check the formula to make sure that the argument types are correct.

It’s possible that you may be using formulas that you’re not very well versed with.

In such cases, it’s a good idea to check the help for each formula and make sure that the argument type is correct.

**Pro Tip**: Sometimes, the formulas can get large and complex and it could be difficult to find out what’s causing the error. A good technique in such cases to [debug the formula](https://trumpexcel.com/excel-formula-debugging/)
 would be to select a portion of the formula in the formula bar and hit the F9 key. The F9 key computes and gives you the result of the selected portion of the formula. This allows you to debug the Formula part-by-part.

Value Errors Due to Incorrect Date Format
-----------------------------------------

Excel has multiple in-built date formats that it can recognize.

But in some cases, you may have a date in a format that Excel does not recognize as a date.

In such a scenario, Excel would treat those dates as text strings.

Now, if you try and use these dates in formulas that are built to handle date values, you will get a value error.

Let me explain with an example.

Below I have a date in cell A1, but this is not in the format that Excel recognizes as a proper date format.

If I try and use this date in the EOMONTH formula (which requires a date as one of the arguments). it will give me the value error.

![VALUE error because of wring date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20435'%3E%3C/svg%3E)

**How to tackle this?**

The only way to tackle this issue is to make sure that the date is in the right format.

**Pro tip**: A quick trip to make sure that the date is in the right format is to go to an empty cell and add 1 to the date value. For example, if you have the date in cell A1, then you go to an empty cell and enter =A1+1. If you get a result, then the date is in the right format, and if you get an error, then it needs to be corrected

Removing #VALUE Error Using IF or IFERROR Functions
---------------------------------------------------

Excel has some built-in error handling formulas that can help you tackle the value error.

This can be done using the [IFERROR formula](https://trumpexcel.com/excel-iferror-function/)
 (or a combination of IF and ISERROR).

Below I have a data set where I have the dates in column A and the number of days that I want to add to these dates in column B.

![Dataset to add days to date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20541%20385'%3E%3C/svg%3E)

In column C, I use the below formula to get the date after the specified number of days for each date:

\=A2+B2

![Adding dates in wring format gives value error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20425'%3E%3C/svg%3E)

As you can see, some of the results show the value error as the dates are not in the right format (i.e., these are in a format that Excel doesn’t recognize as a date, hence these are considered as text strings).

You can use the below formula to get a more meaningful text instead of the value error.

\=IFERROR(A2+B2,"Check the date")

![Value error replaces by more meaningful text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20435'%3E%3C/svg%3E)

The above IFERROR formula would return the result of the first argument, and in case that results is an error, then it would return the second argument.

You can also achieve the same thing by using the below combination of IF and ISERROR formula

\=IF(ISERROR(A2+B2),"Check the Date",A2+B2)

The above first checks whether the result of the calculation is an error or not. If it’s an error, it returns the second argument, else the third argument.

_Note that if you’re using excel 2003 or versions prior to that, you would not have access to the IFERROR formula (as it was introduced from Excel 2007 onwards)_

One drawback of using the IFERROR formula is that it is going to catch all the different types of error (be it #N/A or #DIV/0 #VALUE, #REF, etc.). So no matter what’s causing the error, IFERROR formula would bucket everything as an error and give you the specified second argument

Find All Cells with the #VALUE Error
------------------------------------

If you’re auditing someone else’s work, it may be useful to know how to quickly find out all the cells that have the value error in them.

This can be done using a simple Find operation in Excel.

Below are the steps to quickly find out all the cells that contain the value error in a worksheet:

1.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20223'%3E%3C/svg%3E)

2.  In the Editing group, click on Find and Select

![Click on Find and Select](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20166'%3E%3C/svg%3E)

3.  In the options from the drop-down, click on Find. This will open the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
     dialog box
4.  Click on the Options button. This will make available some additional options

![Click on Options button in Find and Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20225'%3E%3C/svg%3E)

5.  In the Find and Replace dialog box, make the following changes:
    1.  In the ‘Find what’ field, enter VALUE!
    2.  From the ‘Within’ drop-down, select Workbook (or keep in Worksheet if you only want to find the error in the active worksheet)
    3.  In the ‘Look in’ drop-down, select Values

![Enter Value! in Find what field and select Values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

6.  Click on Find All

![Click on the Find All option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

The above steps would scan your entire worksheet (or workbook if you selected that) and give you a list of all the cells that contain the value error.

You should see the list of cells as shown below.

![All Cells with Value error are found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20393'%3E%3C/svg%3E)

Now you can go through each of these cells one by one and handle these, or if you want to delete these or highlight these in one go, you can do that as well.

To select all the cells that have the value error, click on any of the listed cells in the Find and Replace dialog box, and then use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 Control + A (hold the Control key and press the A key). If you’re using Mac, use Command + A instead.

That’s all that you need to know about the value error in Microsoft Excel.

In this tutorial, I covered the possible reasons that can cause the Value error and how to tackle these, some inbuilt error-handling formulas that you can use in case you get the value error, and how to quickly find and select all the cells that contain the value error in the worksheet or the workbook.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [NAME Error in Excel (#NAME?)- What Causes it and How to Fix it!](https://trumpexcel.com/name-error-excel/)
    
*   [#REF! Error in Excel – How to Fix the Reference Error!](https://trumpexcel.com/ref-error-in-excel/)
    
*   [How to Get Rid of #DIV/0! Error in Excel? Easy Formulas!](https://trumpexcel.com/div-error-in-excel/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [Identify Errors Using Excel Formula Debugging (2 Methods)](https://trumpexcel.com/excel-formula-debugging/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/fix-value-error-in-excel/#respond)

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