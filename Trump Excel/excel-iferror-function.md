# Excel IFERROR Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-iferror-function

---

[Skip to content](https://trumpexcel.com/excel-iferror-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-iferror-function/#below-title)

When you work with data and formulas in Excel, you’re bound to encounter errors.

To handle errors, Excel has provided a useful function – the IFERROR function.

Before we get into the mechanics of using the IFERROR function in Excel, let’s first go through the different kinds of errors you can encounter when working with formulas.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-iferror-function/#)

Types of Errors in Excel
------------------------

Knowing the errors in Excel will better equip you to identify the possible reason and the best way to handle these.

Below are the types of errors you might find in Excel.

### #N/A Error

This is called the ‘Value Not Available’ error.

You will see this when you use a lookup formula and it can’t find the value (hence Not Available).

Below is an example where I use the [VLOOKUP formula](https://trumpexcel.com/excel-vlookup-function/)
 to find the price of an item, but it returns an error when it can’t find that item in the table array.

![Excel IFERROR Function - Not Available Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20252'%3E%3C/svg%3E)

### #DIV/0! Error

You’re likely to see this error when a number is divided by 0.

This is called the division error. In the below example, it gives a [#DIV/0! error](https://trumpexcel.com/div-error-in-excel/)
 as the quantity value (the divisor in the formula) is 0.

![Division Error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20311'%3E%3C/svg%3E)

### #VALUE! Error

The [value error](https://trumpexcel.com/fix-value-error-in-excel/)
 occurs when you use an incorrect data type in a formula.

For example, in the below example, when I try to add cells that have numbers and character A, it gives the value error.

This happens as you can only add numeric values, but instead, I tried adding a number with a text character.

![Value Error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20245'%3E%3C/svg%3E)

### #REF! Error

This is called the [reference error](https://trumpexcel.com/ref-error-in-excel/)
 and you will see this when the reference in the formula is no longer valid. This could be the case when the formula refers to a cell reference and that cell reference does not exist (happens when you delete a row/column or worksheet that was referred to in the formula).

In the below example, while the original formula was =A2/B2, when I deleted Column B, all the references to it became #REF! and it also gave the #REF! error as the result of the formula.

![Reference Error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20314'%3E%3C/svg%3E)

### #NAME ERROR

This error is likely to a result of a misspelled function.

For example, if instead of VLOOKUP, you by mistake use VLOKUP, it will give a [name error](https://trumpexcel.com/name-error-excel/)
.

![NAME Error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20253'%3E%3C/svg%3E)

### #NUM ERROR

Num error can occur if you try and calculate a very large value in Excel. For example, \=187^549 will return a number error.

![NUM Error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20129'%3E%3C/svg%3E)

Another situation where you can get the NUM error is when you give a non-valid number argument to a formula. For example, if you’re [calculating the Square Root](https://trumpexcel.com/calculate-square-root-in-excel/)
 if a number and you give a negative number as the argument, it will return a number error.

For example, in the case of Square Root function, if you give a negative number as the argument, it will return a number error (as shown below).

While I have shown only a couple of examples here, there can be many other reasons that can lead to errors in Excel. When you get errors in Excel, you can’t just leave it there. If the data is further used in calculations, you need to make sure the errors are handled the right way.

Excel IFERROR function is a great way to handle all types of errors in Excel.

Excel IFERROR Function – An Overview
------------------------------------

Using the IFERROR function, you can specify what you want the formula to return instead of the error. If the formula does not return an error, then its own result is returned.

![EXCEL IFERROR FUNCTION - What it does! ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20327'%3E%3C/svg%3E)

IFERROR Function Syntax
-----------------------

\=IFERROR(value, value\_if\_error)

**Input Arguments**

*   **value –** this is the argument that is checked for the error. In most cases, it is either a formula or a cell reference.
*   **value\_if\_error** – this is the value that is returned if there is an error. The following error types evaluated: #N/A, #REF!, #DIV/0!, #VALUE!, #NUM!, #NAME?, and #NULL!.

**Additional Notes:**

*   If you use “” as the value\_if\_error argument, the cell displays nothing in case of an error.
*   If the value or value\_if\_error argument refers to an empty cell, it is treated as an empty string value by the Excel IFERROR function.
*   If the value argument is an array formula, IFERROR will return an array of results for each item in the range specified in value.

Excel IFERROR Function – Examples
---------------------------------

Here are three examples of using IFERROR function in Excel.

### Example 1 – Return Blank Cell Instead of Error

If you have functions that may return an error, you can wrap it within the IFERROR function and specify blank as the value to return in case of an error.

In the example shown below, the result in D4 is the #DIV/0! error as the divisor is 0.

![Using Excel IFERROR function to remove error values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20195'%3E%3C/svg%3E)

In this case, you can use the following formula to return blank instead of the ugly DIV error.

\=IFERROR(A1/A2,””)

![Returning a blank using the IFERROR function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20192'%3E%3C/svg%3E)

This IFERROR function would check whether the calculation leads to an error. If it does, it simply returns a blank as specified in the formula.

Here, you can also specify any other string or formula to display instead of the blank.

For example, the below formula would return the text “Error”, instead of the blank cell.

\=IFERROR(A1/A2,”Error”)

![Using Excel Iferror function to return text in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20190'%3E%3C/svg%3E)

Note: If you are using Excel 2003 or a prior version, you will not find the IFERROR function in it. In such cases, you need to use the combination of [IF function](https://trumpexcel.com/excel-if-function/)
 and [ISERROR](https://trumpexcel.com/excel-is-function/)
 function.

### Example 2 – Return ‘Not Found’ when VLOOKUP Can’t Find a Value

When you use the Excel [VLOOKUP Function](https://trumpexcel.com/excel-vlookup-function/)
, and it can’t find the lookup value in the specified range, it would return the #N/A error.

For example, below is a data set of student names and their marks. I have used the VLOOKUP function to fetch the marks of three students (in D2, D3, and D4).

![Using iferror functiont to handle NA error in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20394'%3E%3C/svg%3E)

While the VLOOKUP formula in the above example finds the names of first two students, it can’t find Josh’s name on the list and hence it returns the #N/A error.

Here, we can use the IFERROR function to return a blank or some meaningful text instead of the error.

Below is the formula that will return ‘Not Found’ instead of the error.

\=IFERROR(VLOOKUP(D2,$A$2:$B$12,2,0),”Not Found”)

![excel-iferror-function-vlookup-not-found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20388'%3E%3C/svg%3E)

Note that you can also use IFNA instead of IFERROR with VLOOKUP. While IFERROR would treat all kinds of error values, IFNA would only work on the #N/A errors and wouldn’t work with other errors.

### Example 3 – Return 0 in case of an Error

If you don’t specify the value to return by IFERROR in the case of an error, it would automatically return 0.

For example, if I divide 100 with 0 as shown below, it would return an error.

![excel-iferror-function-error-when-div-by-0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20319%20189'%3E%3C/svg%3E)

However, if I use the below IFERROR function, it would return a 0 instead. Note that you still need to use a comma after the first argument.

![excel-iferror-function-comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20191'%3E%3C/svg%3E)

### Example 4 – Using Nested IFERROR with VLOOKUP

Sometimes when using VLOOKUP, you may have to look through the fragmented table of arrays. For example, suppose you have the sales transaction records in 2 separate worksheets and you want to look-up an item number and see it’s value.

Doing this requires using nested IFERROR with VLOOKUP.

Suppose you have a dataset as shown below:

![Nested IFERROR with VLOOKUP dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20179'%3E%3C/svg%3E)

In this case, to find the score for Grace, you need to use the below nested IFERROR formula:

**\=IFERROR(VLOOKUP(G3,$A$2:$B$5,2,0),IFERROR(VLOOKUP(G3,$D$2:$E$5,2,0),"Not Found"))**

This kind of formula nesting ensure that you get the value from either of the table and any error returned is handled.

Note that in case the tables are on the same worksheet, however, in a real-life example, it likely to be on different worksheets.

Excel IFERROR Function – VIDEO
------------------------------

**Related Excel Functions:**

*   [Excel AND Function](https://trumpexcel.com/excel-and-function/)
    .
*   [Excel OR Function](https://trumpexcel.com/excel-or-function/)
    .
*   [Excel NOT Function](https://trumpexcel.com/excel-not-function/)
    .
*   [Excel IF Function](https://trumpexcel.com/excel-if-function/)
    .
*   [Excel IFS Function](https://trumpexcel.com/excel-ifs-function/)
    .
*   [Excel FALSE Function](https://trumpexcel.com/excel-false-function/)
    .
*   [Excel TRUE Function](https://trumpexcel.com/excel-true-function/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    .
*   [Identify Errors Using Excel Formula Debugging.](https://trumpexcel.com/excel-formula-debugging/)
    
*   [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-iferror-function/#respond)

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