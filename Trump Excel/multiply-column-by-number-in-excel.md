# How to Multiply a Column by a Number in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/multiply-column-by-number-in-excel

---

[Skip to content](https://trumpexcel.com/multiply-column-by-number-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/multiply-column-by-number-in-excel/#below-title)

Although Excel is a powerful data analysis tool, many users use it for basic arithmetic operations.

One common requirement is to multiply an entire column by a number (a constant value).

In this tutorial, I will show you two easy ways to **multiple an entire column with a given number**.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/multiply-column-by-number-in-excel/#)

Mulitply Column with a Number Using Formula (Hardcoding the Value in Formula)
-----------------------------------------------------------------------------

Suppose I have a dataset as shown below, where I have the Sales Rep names in Column A and their current sales values in Column B.

![Dataset with new sales target in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20338'%3E%3C/svg%3E)

I want to calculate their Sales target for the next year, which would be 10% higher than their current sales.

This essentially means that I want to increase all the values in column B by 10% (i.e., multiply these values by 1.1 or 110%)

### Hardcoding the Value in the Formula

Below is the formula to multiply 110% with the values in the entire column B2 (use this formula in cell C2):

\=B2\*110%

![Formula to calculate new sales target](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20385'%3E%3C/svg%3E)

The above formula would give you the result of the multiplication of value in cells B2 with 110%.

But we also want to get the result when all the values in column B are multiplied with the same number.

To do this, select cell C2, place the cursor at the bottom right part of the selection, hold the left mouse key and drag down. This will copy the same formula for all the cells in column C.

Alternatively, you can also copy cell C2 and paste it into the cells below it (a simple Control +C and Control + V would work).

![Entire column multiplied with the same value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20379'%3E%3C/svg%3E)

Note that the result of the formula is dynamic. So if you change the values in column B, the result would accordingly update. If you don’t want this to be dynamic, and instead want static values, you can [convert the formula to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

### Multiply Entire Column with a Value in a Cell

In the above example, I hardcoded the value 110% in the formula.

Another option is to have the value, with which I want to multiply the entire column, in a separate cell, and use the cell reference instead of hardcoding the actual value in the formula.

The benefit of this method is that in case I change the value in the cell, the formulas would automatically update.

Below I have the same dataset, and I have the new sales target [percentage](https://trumpexcel.com/calculate-percentages-excel/)
 in cell E2.

![Dataset with new sales target in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20338'%3E%3C/svg%3E)

Below is the formula that will give me the new sales target:

\=B2\*$E$2

![Formula to multiply cell value with entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20381'%3E%3C/svg%3E)

To multiple the entire column, you need to copy the cell with the formula and paste it into all the cells in the column. This will copy the formula as well and give you the right result.

**How does this work?**

The trick in this method is in using the [dollar signs in the reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 of the cell that contains the number with which we want to multiply the entire column ($E$2 in this example).

When you add a dollar sign before the [row number](https://trumpexcel.com/number-rows-in-excel/)
 and the column alphabet, it makes sure that when that formula is copied in other cells, the reference does not change.

In our formula, the $E$2 portion of the formula would not change, while the A2 would become A3 when the formula is copied in cell C3 and it would become A4 when the formula is copied in cell C4, as so on.

Note: In case you’re using Excel for Microsoft 365, where you have access to dynamic arrays, you can simply use the formula =B2:B13\*E2. You don’t need to copy for the entire column, the formula itself would spill the result for the entire range.

Also read: [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)

Mulitple Column with a Number Using Paste Special
-------------------------------------------------

Another method that you can use to quickly multiply an entire column with a given number is by using the [Paste Special technique](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
.

Suppose you have a data set as shown below, where I want to multiply the number in cell E2 with the entire data set in column A.

![Dataset with new sales target in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20338'%3E%3C/svg%3E)

 Below are the steps to do this:

1.  Copy all the values in column B and paste it in column C. We are doing this as the [Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
     multiplication would be applied in column C, and we would also retain the original values in column B.

![Copy column B and paste in column C](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20340'%3E%3C/svg%3E)

2.  Copy cell E2 (you can select it and use Control + C, or you can right-click on it and then click on Copy.

![Copy the cell value with which to multiply](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20344'%3E%3C/svg%3E)

3.  Select all the cell in column A with which you want to multiply the number

![Select cells with which you want to multiply](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20340'%3E%3C/svg%3E)

4.  Right-click on the selected cells and then click on Paste Special option

![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20344'%3E%3C/svg%3E)

5.  In the Paste Special dilaog box that opens, select the Multiply option in Operations

![Select Multiply option in Operation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20429'%3E%3C/svg%3E)

6.  Click OK

That’s it!

The above steps would instantly change all the values in column A and give you the result after it has multiplied these numbers with the value in cell E2.

![Paste Special Multiply result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20614%20336'%3E%3C/svg%3E)

The result you get is static values (as compared to a formula that you get in the method before that)

Once you are done with the multiplication, you can delete the value in cell E2 (if you want).

One important thing to note about using this method is that when you multiply an entire column using the paste special method, it also [copies the formatting](https://trumpexcel.com/excel-format-painter/)
 from cell E2. So if you give a cell color to cell E2 and use this method, all the cells in column A would also have that color copied to it. To avoid this, you can also select the Value option in the Paste Special dialog box in step 4

So these are two simple methods that you can use to multiply an entire column with a number in Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also find helpful:**

*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [How to Apply Formula to Entire Column in Excel (5 Easy Ways)](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    
*   [How to Select Entire Column (or Row) in Excel – Shortcut](https://trumpexcel.com/select-entire-column-excel/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [How to Copy and Paste Column in Excel?](https://trumpexcel.com/copy-paste-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/multiply-column-by-number-in-excel/#respond)

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