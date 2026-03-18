# Excel Formulas Not Working (Not Calculating) - Fix!

**Source:** https://trumpexcel.com/excel-formulas-not-working

---

[Skip to content](https://trumpexcel.com/excel-formulas-not-working/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-formulas-not-working/#below-title)

If you work with [formulas in Excel](https://trumpexcel.com/excel-functions/)
, sooner or later, you will encounter the problem where Excel formulas don’t calculate and give the result (or give the wrong result).

It would have been great had there been only a few possible reasons for malfunctioning formulas.

Unfortunately, there are too many things that can go wrong (and often do).

But since we live in a world that follows the [Pareto principle](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
, if you check for some common issues, it’s likely to solve 80% (or maybe even 90% or 95% of the issues where formulas are not working in Excel).

In this article, I will highlight those common issues that are likely the cause of your **Excel formulas not working**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-formulas-not-working/#)

Incorrect Syntax of the Function
--------------------------------

Let me start by pointing out the obvious.

Every function in Excel has a specific syntax – such as the number of arguments it can take or the type of arguments it can accept.

And in many cases, the reason your Excel formulas are not working or gives the wrong result could be an incorrect argument (or missing arguments).

For example, the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 takes three mandatory arguments and one optional argument.

If you provide a wrong argument or don’t specify the optional argument (where it’s needed for the formula to work), it’s going to give you a wrong result.

For example, suppose you have a dataset as shown below where you need to know the score of Mark in Exam 2 (in cell F2).

![Formula not working Dataset to get score](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20246'%3E%3C/svg%3E)

If I use the below formula, I will get the wrong result, because I am using the wrong value in the third argument (one that asks for Column Index number).

\=VLOOKUP(A2,A2:C6,2,FALSE)

![VLOOKUP function giving wrong result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20243'%3E%3C/svg%3E)

In this case, the formula calculates (as it returns a value), but the result is incorrect (instead of score in Exam 2, it gives the score in Exam 1).

Another example where you need to be cautious about the arguments is when using VLOOKUP with the approximate match.

Since you need to use an optional argument to specify where you want VLOOKUP to do an exact match or an approximate match, not specifying this (or using the wrong argument) can cause issues.

Below is an example where I have the marks data for some students and I want to extract marks in Exam 1 for the students in the table on the right.

![Dataset for VLOOKUP exact match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20203'%3E%3C/svg%3E)

When I use the below VLOOKUP formula it gives me an error for some names.

\=VLOOKUP(E2,$A$2:$C$6,2)

![Wrong formula result due to missing argument](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20578%20248'%3E%3C/svg%3E)

This happens as I have not specified the last argument (which is used to determine whether to do an exact match or approximate match). When you don’t specify the last argument, it automatically does an approximate match by default.

Since we needed to do an exact match in this case, the formula returns an error for some names.

While I have taken the example of the VLOOKUP function, in this case, this is something that can be applicable for many Excel formulas that have optional arguments as well.

Also read: [Identify Errors Using Excel Formula Debugging](https://trumpexcel.com/excel-formula-debugging/)

Extra Spaces Causing Unexpected Results
---------------------------------------

Leading, trailing spaces are hard to find out and can cause issues when you use a cell that has these in formulas.

For example, in the below example, if I try to use VLOOKUP to fetch the score for Mark, it gives me the #N/A error (the not available error).

![Formula giving a NA error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20245'%3E%3C/svg%3E)

While I can see that the formula is correct and the name ‘Mark’ is clearly there is the list, what I can not see is that there is a trailing space in the cell that has the name (in cell D2).

![Extra Space in the lookup value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20245'%3E%3C/svg%3E)

Excel doesn’t consider the content of these two cells the same and therefore it considers it a mismatch when fetching the value using VLOOKUP (or it could be any other lookup formula).

To fix this issue, you need to [remove these extra space](https://trumpexcel.com/excel-trim-function/)
 characters.

You can do this by using any of the following methods:

1.  Clean the cell and [remove any leading/trailing spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
     before using it in formulas
2.  Use the TRIM function within the formula to make sure any leading/trailing/double spaces are ignored.

In the above example, you can use the below formula instead to make sure it works.

\=VLOOKUP(TRIM(D2),$A$2:$B$6,2,0)

While I have taken the VLOOKUP example, this is also a common issue when working with TEXT functions.

For example, if I use the [LEN function](https://trumpexcel.com/excel-len-function/)
 to count the total number of characters in a cell, if there are leading or trailing spaces, these would also be counted and give the wrong result.

**Take away / How to Fix**: If possible, [clean your data](https://trumpexcel.com/clean-data-in-excel/)
 by removing any leading/trailing or double spaces before using these in formulas. If you can not change the original data, use the TRIM function in formulas to take care of this.

Also read: [Excel Showing Formula Instead of Result](https://trumpexcel.com/excel-showing-formula-instead-of-result/)

Using Manual Calculation Instead of Automatic
---------------------------------------------

This one setting can drive you crazy (if you don’t know it’s what’s causing all the issues).

Excel has two calculation modes – **Automatic** and **Manual.**

By default, the automatic mode is enabled, which means that in case I use a formula or make any changes in the existing formulas, it automatically (and instantly) makes the calculation and gives me the result.

This is the setting we are all used to.

In the automatic setting, whenever you make any change in the worksheet (such as entering a new formula to even some text in a cell), Excel automatically recalculates everything (yes, **everything**).

But in some cases, people enable the manual calculation setting.

This is mostly done when you have a heavy Excel file with a lot of data and formulas. In such cases, you may not want Excel to recalculate everything when you make small changes (as it may take a few seconds or even minutes) for this recalculation to complete.

If you enable manual calculation, Excel will not calculate unless you force it to.

And this may make you think that your formula is not calculating.

All you need to do in this case is either set the calculation back to automatic or force a recalculation by hitting the F9 key.

Below are the steps to change the calculation from manual to automatic:

1.  Click the Formula tab![Formulas tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20201'%3E%3C/svg%3E)
2.  Click on Calculation Options
3.  Select Automatic![Set the calculation to automatic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20254'%3E%3C/svg%3E)

Important: In case you’re changing the calculation from manual to automatic, it’s a good idea to create a backup of your workbook (just in case this makes your workbook hang or makes Excel crash)

**Take away / How to Fix**: If you notice that your formulas are not giving the expected result, try something simple in any cell (such as adding 1 to an existing formula. Once you identify the issue as the one where calculation mode needs to be changed, do a force calculation by using F9.

Deleting Rows/Column/Cells Leading to #REF! Error
-------------------------------------------------

One of the things that can have a devastating effect on your existing formulas in Excel is when you delete any row/column which has been used in calculations.

When this happens, sometimes, Excel adjusts the reference itself and makes sure that the formulas are working fine.

And sometimes… **it can not**.

Thankfully, one clear indication that you get when formulas break on deleting cells/rows/columns is the #REF! error in the cells. This is a [reference error](https://trumpexcel.com/ref-error-in-excel/)
 that tells you that there is some issue with the references in the formula.

Let me show you what I mean by using an example.

Below I have used the SUM formula to add the cells A2:A6.

![Formula to add cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20369'%3E%3C/svg%3E)

Now, if I delete any of these cells/rows, the SUM formula will return a #REF! error. This happens because when I [deleted the row](https://trumpexcel.com/delete-rows/)
, the formula doesn’t know what to reference now.

![Ref error when a row is deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20338'%3E%3C/svg%3E)

You can see that the third argument in the formula has become #REF! (which earlier referred to the cell that we deleted).

**Take away / How to Fix**: Before you delete any data that is being used in formulas, make sure there are no errors after the deletion. It’s also recommended that you create a backup of your work regularly to make sure you always have something to fall back on.

Incorrect Placement of Parenthesis (BODMAS)
-------------------------------------------

As your formulas start to get bigger and more complex, it’s a good idea to use parenthesis to be absolutely clear of what part belongs together.

In some cases, you may have the parenthesis at the wrong place, which can either give you a wrong result or an error.

And in some cases, it’s recommended to uses parenthesis to make sure the formula understands what needs to be grouped and calculated first.

For example, suppose you have the following formula:

\=5+10\*50

In the above formula, the result is 505 as Excel first does the multiplication and then the addition (as there is an order of precedence when it comes to operators).

If you want it to first do the addition and then the multiplication, you need to use the below formula:

\=(5+10)\*50

In some cases, the order of precedence may work for you, but it’s still recommended that you use the parenthesis to avoid any confusion.

Also, in case you’re interested, below is the order of precedence for various operators often used in formulas:

|     |     |     |
| --- | --- | --- |
| **Operator** | **Description** | **Order of Precedence** |
| : (colon) | Range | 1   |
| (single space) | Intersection | 2   |
| , (comma) | union | 3   |
| –   | Negation (as in –1) | 4   |
| %   | Percentage | 5   |
| ^   | Exponentiation | 6   |
| \* and / | Multiplication & division | 7   |
| \+ and – | Addition & [subtraction](https://trumpexcel.com/subtract-in-excel/) | 8   |
| &   | Concatnenation | 9   |
| \= < > <= >= <> | Comparison | 10  |

**Take away / How to Fix**: Always use parenthesis to avoid any confusion, even if you know the order of precedence and are using it correctly. Having parenthesis makes it easier to audit formulas.

Incorrect Use of Absolute/Relative Cell References
--------------------------------------------------

When you copy and paste formulas in Excel, it automatically adjusts the references. Sometimes, this is exactly what you want (mostly when you’re copy-pasting formulas down the column), and sometimes you don’t want this to happen.

An absolute reference is when you fix a cell reference (or range reference) so that it doesn’t change when you copy and paste formulas, and a relative reference is one that changes.

_You can read more about [absolute, relative, and mixed references here](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
._

You may get an incorrect result in case you forget to change the reference to an absolute one (or vice versa). This is something that happens quite often to me when I am using lookup formulas.

Let me show you an example.

Below I have a dataset where I want to fetch the score in Exam 1 for the names in column E (a simple VLOOKUP use case)

![Dataset for incorrect references](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20249'%3E%3C/svg%3E)

Below is the formula that I use in cell F2 and then copies to all the cells below it:

\=VLOOKUP(E2,A2:B6,2,0)

![Formula giving erorr because references are not locked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20624%20246'%3E%3C/svg%3E)

As you can see that this formula gives an error in some cases.

This happens because I haven’t locked the table array argument – it’s **A2:B6** in cell F2, while it should have been **$A$2:$B$6**

By having these dollar signs before the row number and column alphabet in a cell reference, I am forcing  Excel to keep these cell references fixed. So, even when I copy this formula down, the table array will continue to refer to A2:B6

**Pro Tip**: To convert a relative reference to an absolute one, select that cell reference within the cell, and press the F4 key. You would notice that it changes by adding the dollar signs. You can continue to press F4 until you get the reference you want.

Incorrect Reference to Sheet / Workbook Names
---------------------------------------------

When you refer to other sheets or workbooks in a formula, you need to follow a specific format. And in case the format is incorrect, you will get an error.

For example, if I want to refer to cell A1 in Sheet2, the reference would be **\=Sheet2!A1** (where there is an exclamation sign after the sheet name)

And in case there are multiple words in the sheet name (let’s say it’s Example Data), the reference would be **\=’Example Data’!A1** (where the name is enclosed in single quotes followed by an exclamation sign).

In case you’re referring to an external workbook (let’s say you’re referring to cell A1 in ‘Example Sheet’ in the workbook named ‘Example Workbook’), the reference will be as shown below:

\='\[Example Workbook.xlsx\]Example Sheet'!$A$1

And in case you close the workbook, the reference would change to include the entire path of the workbook (as shown below):

\='C:\\Users\\sumit\\Desktop\\\[Example Workbook.xlsx\]Example Sheet'!$A$1

In case you end up changing the name of the workbook or the worksheet to which the formula refers to, it’s going to give you a #REF! error.

Also read: [How to Find External Links and References in Excel](https://trumpexcel.com/find-external-links-excel/)

Circular References
-------------------

A [circular reference](https://trumpexcel.com/find-circular-reference-excel/)
 is when you refer (directly or indirectly) to the same cell where the formula is being calculated.

Below is a simple example, where I use the SUM formula in cell A4 while using it in the calculation itself.

\=SUM(A1:A4)

Although Excel shows you a prompt letting you know about the circular reference, it will not do it for every instance. And this may give you the wrong result (without any warning).

In case you suspect circular reference in play, you can check which cells have it.

To do this, click the Formula tab and in the ‘Formula Auditing’ group, click on the Error Checking drop-down icon (the small downward pointing arrow).

Hover the cursor over the Circular reference option and it will show you the cell that has the circular reference issue.

![finding circular reference error in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20232'%3E%3C/svg%3E)

Cells Formatted as Text
-----------------------

If you find yourself in a situation where as soon as you type the formula as hit enter, you [see the formula instead of the value](https://trumpexcel.com/show-formulas-in-excel/)
, it’s a clear case of the cell being formatted as text.

![Cell formatted as text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20277'%3E%3C/svg%3E)

When a cell is formatted as text, it considers the formula as a text string and shows it as is.

It doesn’t force it to calculate and give the result.

And it has an easy fix.

1.  Change the format to ‘General’ from ‘Text’ (it’s in Home tab in the Numbers group)
2.  Go to the cell that has the formula, get into the edit mode (use F2 or double click on the cell) and hit Enter

In case the above steps don’t solve the problem, another thing to check is whether the cell has an apostrophe at the beginning. A lot of people add an apostrophe to convert formulas and numbers to text.

If there is an apostrophe, you can simply remove it.

Text Automatically Getting Converted into Dates
-----------------------------------------------

Excel has this bad habit of converting that looks like a date into an actual date. For example, if you enter 1/1, Excel would convert it to 01-Jan of the current year.

In some cases, this may be exactly what you want, and in some cases, this may work against you.

And since Excel stores date and time values as numbers, as soon as you enter 1/1, it converts it into a number representing the January 1 of the current year. In my case, when I do this, it converts it into the number 43831 (for 01-01-2020).

This could mess with your formulas if you’re using these cells as an argument in a formula.

How to fix this?

Again, we don’t want Excel to automatically pick the format for us, so we need to clearly specify the format ourselves.

Below are the steps to change the format to text so that it doesn’t automatically [convert text to dates:](https://trumpexcel.com/convert-date-to-text-excel/)

1.  Select the cells/range where you want to change the format
2.  Click on the Home tab![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20200'%3E%3C/svg%3E)
3.  In the Number group, click on the Format drop-down
4.  Click on Text![Select text as the formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20732'%3E%3C/svg%3E)

Now, whenever you enter anything in the selected cells, it would be considered as text, and not changed automatically.

Note: The above steps would only work for data entered after the formatting has been changed. It will not change any text that has been converted to date before you made this formatting change.

Another example where this can be really frustrating is when you enter a text/number that has [leading zeros](https://trumpexcel.com/add-leading-zeroes-excel/)
. Excel automatically [removes these leading zeros](https://trumpexcel.com/remove-leading-zeros-excel/)
 as it considers these useless. For example, if you enter 0001 in a cell, Excel will change it to 1. In case you want to keep these leading zeros, use the steps above.

Also read: [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)

Hidden Rows/Columns Can Give Unexpected Results
-----------------------------------------------

This is not a case of formula giving you the wrong result but of using the wrong formula.

For example, suppose you have a dataset as shown below and I want to get the sum of all the visible cells in column C.

![Dataset for formulas not working](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20279'%3E%3C/svg%3E)

In cell C12, I have used the [SUM function](https://trumpexcel.com/excel-sum-function/)
 to get the total sale value for all these given records.

![SUM formula to get the sum of the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20372'%3E%3C/svg%3E)

So far so good!

Now, I apply a filter to the item column to only show the records for Printer sales.

![Same SUM value even after the filer is applied](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20255'%3E%3C/svg%3E)

And here is the problem – the formula in cell C12 still shows the same result – i.e., the sum of all the records.

As I said, the formula is not giving the wrong result. In fact, the SUM function is working just fine.

The issue is that we have used the wrong formula here.

SUM function can not account for the filtered data and give you the result for all the cells (hidden or visible). If you only want to get the sum/count/average of visible cells, use SUBTOTAL or AGGREGATE functions.

_**Key takeaway** – Understand the correct use and limitations of a function in Excel._

These are some of the common causes that I have seen where your **Excel formulas may not work or give unexpected or wrong results**. I am sure there are many more reasons for an Excel formula to not work or update.

In case you know of any other reason (maybe something that irks you often), let me know in the comments section.

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    
*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [Show Formulas in Excel Instead of the Values](https://trumpexcel.com/show-formulas-in-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [Microsoft Excel Won’t Open; How to Fix it!](https://trumpexcel.com/microsoft-excel-wont-open/)
    
*   [Conditional Formatting Not Working in Excel](https://trumpexcel.com/conditional-formatting-not-working/)
    
*   [Arrow Keys not Working in Excel | Moving Pages Instead of Cells](https://trumpexcel.com/arrow-keys-not-working-excel/)
    
*   [20 Advanced Excel Functions and Formulas](https://trumpexcel.com/advanced-excel-functions-formulas/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Excel Formulas Not Working (Not Calculating)”
------------------------------------------------------------

1.  Hi Sumit,  
    I recognize these problems and have to deal with this a lot when I receive files or questions from other people. In most cases I can find the solution.  
    But I still have one very nasty problem, maybe you have a solution for this. I often have to use files with EAN-codes in it.  
    With use of the correct barcode fonts I can make these codes readable for scanners.  
    But the EAN-codes are automaticly transposed to Exponential values. Example: 8714632069985 is shown as 8,71463E+12 or 8,715E+12 in a smaller column.  
    I can change the cell properties to value without decimals or text but I hope there is a way I don’t have to change the cell properties because a lot of these files are imported from csv-files.
    
    [Reply](https://trumpexcel.com/excel-formulas-not-working/#comment-14584)
    
2.  Very useful and interesting.  
    Thank you Summit.
    
    [Reply](https://trumpexcel.com/excel-formulas-not-working/#comment-14575)
    
3.  Sumit,  
    Regarding your #REF! section, I have several hundred Excel files sent to me by others that may have #REF! errors due to cut/paste operations (which I have advised against) and the users don’t necessarily know it. I know I can find them in the opened file, but do you know how I can identify the “bad” files without opening them one at a time? Apparently, Windows File Explorer doesn’t recognize the #REF! text in the Excel file.  
    Thank you for the great tutorials,  
    Willie
    
    [Reply](https://trumpexcel.com/excel-formulas-not-working/#comment-14568)
    
4.  When I format a cell with a custom format ;;; to make it unseen, the cell still counts as containing text, but when it is in a table, the filter drop down doesn’t show it. I have a column of check boxes that I would like to filter TRUE or FALSE without seeing the text, just the checked boxes. Making the text color match the background color works but is problematic with striped rows. Any suggestions?
    
    [Reply](https://trumpexcel.com/excel-formulas-not-working/#comment-14567)
    
5.  never got it
    
    [Reply](https://trumpexcel.com/excel-formulas-not-working/#comment-14563)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-formulas-not-working/#respond)

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