# How to Sum Across Multiple Sheets in Excel? (3D SUM Formula)

**Source:** https://trumpexcel.com/sum-across-multiple-sheets-excel

---

[Skip to content](https://trumpexcel.com/sum-across-multiple-sheets-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-across-multiple-sheets-excel/#below-title)

If you need to get the sum across multiple worksheets, you can use one of the less-known Excel feature called **3D referencing**.

With 3D referencing, you can refer to the same cell in multiple worksheets, and can also use this in formulas such as the SUM or AVERAGE, or COUNT.

In this short tutorial, I will show you how to quickly **sum across multiple worksheets using this 3D reference feature**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-across-multiple-sheets-excel/#)

Sum Across Multiple Sheets in Excel – Single Cell
-------------------------------------------------

Below I have a dataset with quarter-wise sales for 10 stores.

![Quarter1 Sales Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20721'%3E%3C/svg%3E)

In the screenshot above, you can see the sales data for Quarter 1 in the sheet named Q1, and I have similar data for the other three quarters (Q2, Q3, and Q4) in three separate worksheets.

![Other quarter sheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20721'%3E%3C/svg%3E)

And I want to get the sum of each store from all four quarters and get it in the Summary tab (where I have a table as shown below).

![Summary Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20721'%3E%3C/svg%3E)

Now if I do this the regular way, I would first have to enter the equal to sign in the Summary sheet (in cell B2, then go to each worksheet, then select cell B2 in that worksheet, then add a [plus sign](https://trumpexcel.com/add-plus-sign-before-numbers-excel/)
, and then do the same for all the other worksheets.

This will give me a formula as shown below:

\='Q1 Sales'!B2+'Q2 Sales'!B2+'Q3 Sales'!B2+'Q4 Sales'!B2

While this works, this is inefficient and error-prone.

Also, note that I only have 4 worksheets in this case, but in case you have many more (say 12 worksheets for each month), then doing this would take even more time.

Let me show you a better method to do this.

Below are the steps to get the sum across multiple worksheets using 3D referencing:

1.  In the cell where you want the sum value, enter

\=SUM(

![Enter SUM formula in summary sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20356'%3E%3C/svg%3E)

2.  Select the first worksheet (Q1 in this example)
3.  Hold the SHIFT key and click on the last worksheet tab name (Q4 in this example)
4.  Now in the active sheet, the one that’s visible, click on cell B2

![Select cell B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20545'%3E%3C/svg%3E)

5.  Hit the Enter key

The above steps would give you the below formula in cell B2 in the Summary sheet:

\=SUM('Q1 Sales:Q4 Sales'!B2)

![3D Sum value in summary sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20397'%3E%3C/svg%3E)

You can drag this down for all the cells in column B in the [summary worksheet](https://trumpexcel.com/create-summary-worksheet-in-excel/)
.

![Drag the formula to sum across worksheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20340'%3E%3C/svg%3E)

In the above formula, when you followed the steps I’ve mentioned above, it automatically created a 3D reference – _‘Q1 Sales:Q4 Sales’!B2_

This reference refers to all the B2 cells in the sheets between Q1 Sales and Q4 Sales.

As you can see, this 3D formula is shorter and a lot easier to manage than going to each worksheet and selecting the cell that you want to add.

_Note: If you enter the same formula manually in a cell, you would still get the same result._

Sum Across Multiple Sheets in Excel – Range of Cells
----------------------------------------------------

In the above example, I showed you how to get the sum across multiple sheets when I only wanted to add one cell from each worksheet.

But what if I want to add a range of cells from each worksheet and then get the result in the Summary sheet?

For example, below I have the sales data of multiple products in the Q1 sheet, and I have a similar construct across worksheets or other Quarters as well.

![Sales data for multiple products](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20458'%3E%3C/svg%3E)

Now, I want to get the sum of all the products in each quarter in the summary sheet.

Below are the steps to do this:

1.  In the cell where you want the sum value, enter

\=SUM(

2.  Select the first worksheet (Q1 in this example)
3.  Hold the SHIFT key and click on the last worksheet tab name (Q4 in this example)
4.  Now in the active sheet, select B2:D2
5.  Hit the Enter key

This will give you the following formula:

\=SUM('Q1 Sales:Q4 Sales'!B2:D2)

![Fomrula to sum range of cells across multiple sheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20534'%3E%3C/svg%3E)

As you can see, instead of adding one cell from each sheet, we have used a formula to add three cells across four different worksheets.

So this is how you can easily get the sum of values across multiple worksheets using the 3D reference formula.

You can also use the same method with other formulas such as [COUNT](https://trumpexcel.com/excel-count-function/)
 or [AVERAGE](https://trumpexcel.com/excel-average-function/)
.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Sum by Color in Excel (Formula & VBA)](https://trumpexcel.com/sum-by-color-excel/)
    
*   [How to Sum Only Positive or Negative Numbers in Excel (Easy Formula)](https://trumpexcel.com/sum-positive-numbers-excel/)
    
*   [How to Sum a Column in Excel (5 Really Easy Ways)](https://trumpexcel.com/sum-column-excel/)
    
*   [How to SUM values between two dates (using the SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Get the Sheet Name in Excel?](https://trumpexcel.com/get-sheet-name-excel/)
    
*   [Using A1 or R1C1 Reference Notation in Excel (& How to Change These)](https://trumpexcel.com/a1-r1c1-reference-notation-excel/)
    
*   [How to Reference Another Sheet or Workbook in Excel (with Examples)](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [AutoSum in Excel (Shortcut)](https://trumpexcel.com/autosum-shortcut-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Sum Across Multiple Sheets in Excel? (3D SUM Formula)”
----------------------------------------------------------------------------

1.  Sumit!
    
    You’re the man! I just wanted you to know. Thank you for posting this. This was very helpful to me.
    
    Anthony
    
    [Reply](https://trumpexcel.com/sum-across-multiple-sheets-excel/#comment-41475)
    
    *   Thanks Anthony… Glad you found the article helpful!
        
        [Reply](https://trumpexcel.com/sum-across-multiple-sheets-excel/#comment-41621)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-across-multiple-sheets-excel/#respond)

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