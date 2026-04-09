# #REF! Error in Excel - How to Fix the Reference Error!

**Source:** https://trumpexcel.com/ref-error-in-excel

---

[Skip to content](https://trumpexcel.com/ref-error-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/ref-error-in-excel/#below-title)

If you have worked with formulas in Excel for some time, I am sure you have already met the #**REF! Error (reference error).**

Since this is quite common, I thought of writing a tutorial just to tackle the #REF! error.

In this Excel tutorial, I will cover what is the #REF! error, what causes it, and how to fix it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/ref-error-in-excel/#)

What is #REF! Error (Reference Error) in Excel?
-----------------------------------------------

A reference error is something you get when your formula doesn’t know what cell/range to refer to or when the reference is not valid.

The most common reason you may end up with the reference error is when you have a formula that refers to a cell/row/column, and you delete that cell/row/column.

Now, since the formula (that was referring to the range before it got deleted) has no clue where to point to, that earlier reference in the formula changes to #REF!.

This, in turn. makes the formula return the #REF! error for the formula result.

Example of the #REF! Error
--------------------------

Let me show you a simple example where we end up getting the reference error, and later I will cover how to find and fix it.

Below is a dataset where I want to add the four cells, and I use simple arithmetic using the addition operator.

![Formula to calculate the sum of cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20458%20363'%3E%3C/svg%3E)

So far, so good!

Now, if I delete one of the columns, the formula will not have the reference for the deleted cell, so it’s going to give me a #REF! error (as shown below)

![Formula that returns the REF error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20319'%3E%3C/svg%3E)

In the above example, since I [deleted the fourth row](https://trumpexcel.com/delete-rows/)
 (that had the cell with the value 3), the formula doesn’t know what to refer to and returns a reference error.

Reference errors are quite common, and you may want to do a quick check before you use a dataset in the calculation (that has the possibility of having the #REF! error).

So, let me show you two ways to quickly find cells that have the reference error and some possible fixes.

_Related tutorial:_ [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)

Find #REF! Error using Find and Replace
---------------------------------------

Suppose you have a dataset as shown below where you have a couple of reference errors.

![KPI Data with errors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20508'%3E%3C/svg%3E)

Below are the steps to find and select all the cells that have the ‘reference errors’:

1.  Select the entire dataset where you want to check
2.  Hold the Control key and press the F key (or Command + F if you’re using a Mac). This will open the Find and Replace dialog box
3.  In the ‘Find what’ field, enter **#REF!![Enter REF in Find All field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20251'%3E%3C/svg%3E)**
4.  Click on the ‘Find All’ button. This will find all the cells that have the #REF! error![Click on the Find All button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20251'%3E%3C/svg%3E)
5.  Hold the Control key and press the A key (or Command + A if you’re using Mac). This would select all the cells that have the reference error.![All the selected cell in Find and Replace that have the !REF# error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20447'%3E%3C/svg%3E)
6.  Close the Find and Replace dialog box.

The above steps would find and then select all the cells that have the #REF! error and select these.

Once you have all these cells selected that has the error, you can choose what to do with it.

Let’s have a look at some of the possible ways you can handle the reference error.

### Ways to Fix the #REF! error

Once you have all the cells with the reference error selected, you can choose to do any of the following:

*   **Delete the error**: Simply hit the delete key and it will remove these error and you’ll have blank cells instead
*   **Replace with a value or text**: You can choose to replace the error with 0 or dash or any other meaningful text. To do this, simply type what you want to replace the error with, hold the Control key and then press the Enter key. This will enter the text you entered in all the selected cells.
*   **Highlight these cells** using the cell color option in the Home tab in the ribbon

Note: When you use the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 method, it will only find the cells that have the #REF! error, as that’s what we searched for in the ‘Find what’ field. In case there are other errors (such as #NA or #DIV! error), these will not be found (unless you repeat the same steps for these errors as well.

In case you want to find all the errors (including the #REF! error), use the method covered next.

Find Errors using Go To Special Option
--------------------------------------

Another method to quickly find #REF! errors **which are a result of a formula** is by using the Paste Special method.

The good part about this method is that it will find and select all the cells that have any type of error (including the reference errors). But the downside with this method is that it will only find and select cells where the error is because of formula. In case the error is there as text, this method will not be able to find it.

Suppose you have a dataset as shown below and you want to find and select all the cells that have errors in it.

![KPI Data with errors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20508'%3E%3C/svg%3E)

Below are the steps to use Go To Special option to find and select all the errors:

1.  Select the entire dataset where you want to check for errors
2.  Click the Home tab
3.  In the Editing group, click on the ‘Find & Select’ option.
4.  In the options that show up, click on the ‘Go-To Special’ option![Click on the Go To Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20510'%3E%3C/svg%3E)
5.  In the Go To Special dialog box, click on the Formulas option
6.  In the options within Formulas, uncheck everything except the Error checkbox.![Select formula with errors option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20431'%3E%3C/svg%3E)
7.  Click OK

The above steps would instantly select all the cells that have formulas that return an error.

Once you have these cells selected, you can choose to delete these, highlight it, or replace it with 0 or dash or some other meaningful text.

Note: One limitation of this method is that it will only find and select those cells where the error is a result of a formula. In case you have got a data dump where the errors are within the cells as the value itself and not as aa result of a formula, this method will not select those cells.

So these are two quick methods you can use to find and fix the #REF error (reference error) in Excel.

Hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [How to Quickly Find Hyperlinks in Excel](https://trumpexcel.com/find-hyperlinks-in-excel/)
    
*   [How to Find Hyperlinks in Excel](https://trumpexcel.com/find-hyperlinks-in-excel/)
    
*   [Identify Errors Using Excel Formula Debugging](https://trumpexcel.com/excel-formula-debugging/)
    
*   [Excel IFERROR Function](https://trumpexcel.com/excel-iferror-function/)
    
*   [#NAME Error in Excel – What Causes it and How to Fix it!](https://trumpexcel.com/name-error-excel/)
    
*   [How to Get Rid of #DIV/0! Error in Excel?](https://trumpexcel.com/div-error-in-excel/)
    
*   [How to Fix #VALUE Error in Excel?](https://trumpexcel.com/fix-value-error-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/ref-error-in-excel/#respond)

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