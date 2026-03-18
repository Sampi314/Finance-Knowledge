# How to Apply Formula to Entire Column in Excel (5 Easy Ways)

**Source:** https://trumpexcel.com/apply-formula-to-entire-column-excel

---

[Skip to content](https://trumpexcel.com/apply-formula-to-entire-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/apply-formula-to-entire-column-excel/#below-title)

Formulas are the life and blood of Excel spreadsheets. And in most cases, you don’t need the formula in just one cell or a couple of cells.

In most cases, you would need to **apply the formula to an entire column** (or a large range of cells in a column).

And Excel gives you multiple different ways to do this with a few clicks (or a keyboard shortcut).

Let’s have a look at these methods.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/apply-formula-to-entire-column-excel/#)

By Double-Clicking on the AutoFill Handle
-----------------------------------------

One of the easiest ways to apply a formula to an entire column is by using this simple mouse double-click trick.

Suppose you have the dataset as shown below, where want to calculate the commission for each sales rep in Column C (where the commission would be 15% of the sale value in column B).

![Dataset to apply formula to an entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20344'%3E%3C/svg%3E)

The formula for this would be:

\=B2\*15%

Below is the way to apply this formula to the entire column C:

1.  In cell A2, enter the formula: =B2\*15%![Formula to calculate the commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20392'%3E%3C/svg%3E)
2.  With the cell selected, you will see a small green square at the bottom-right part of the selection. ![Fill handle in cell selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20268'%3E%3C/svg%3E)
3.  Place the cursor over the small green square. You will notice that the cursor changes to a plus sign (this is called the [autofill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
    )![Cursor changes to plus icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20206'%3E%3C/svg%3E)
4.  Double click the left mouse key![Double click on apply formula to the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20352'%3E%3C/svg%3E)

The above steps would automatically fill the entire column till the cell where you have the data in the adjacent column. In our example, the formula would be applied till cell C15

For this to work, there shouldn’t be data in the adjacent column and there should not be any blank cells in it. If, for example, there is a blank cell in column B (say cell B6), then this auto-fill double click would only apply the formula till cell C5

![Fill handle stop when it encounters a blank cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20360'%3E%3C/svg%3E)

When you use the autofill handle to apply the formula to the entire column, it’s equivalent to copy-pasting the formula manually. This means that the cell reference in the formula would change accordingly.

For example, if it’s an [absolute reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
, it would remain as is while the formula is applied to the column, add if it’s a relative reference, then it would change as the formula is applied to the cells below.

By Dragging the AutoFill Handle
-------------------------------

One issue with the above double click method is that it would stop as soon as it encountered a blank cell in the adjacent columns.

If you have a small data set, you can also manually drag the fill handle to apply the formula in the column.

Below are the steps to do this:

1.  In cell A2, enter the formula: **\=B2\*15%**
2.  With the cell selected, you will see a small green square at the bottom-right part of the selection
3.  Place the cursor over the small green square. You will notice that the cursor changes to a plus sign![Cursor changes to plus icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20206'%3E%3C/svg%3E)
4.  Hold the left mouse key and drag it to the cell where you want the formula to be applied
5.  Leave the mouse key when done

Using the Fill Down Option (it’s in the ribbon)
-----------------------------------------------

Another way to apply a formula to the entire column is by using the fill down option in the ribbon.

For this method to work, you first need to select the cells in the column where you want to have the formula.

Below are the steps to use the fill down method:

1.  In cell A2, enter the formula: =B2\*15%
2.  Select all the cells in which you want to apply the formula (including cell C2)![Select the entire column or the range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20346'%3E%3C/svg%3E)
3.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20180'%3E%3C/svg%3E)
4.  In the editing group, click on the Fill icon![Click on the Fill icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20144'%3E%3C/svg%3E)
5.  Click on ‘Fill down’![Click on Fill down option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20330%20359'%3E%3C/svg%3E)

The above steps would take the formula from cell C2 and fill it in all the selected cells

### Adding the Fill Down in the Quick Access Toolbar

If you need to use the fill down option often, you can add that to the Quick Access Toolbar, so that you can use it with a single click (and it’s always visible on the screen).

T0 add it to the Quick Access Toolbar (QAT), go to the ‘Fill Down’ option, right-click on it, and then click on ‘Add to the Quick Access Toolbar’

![add to quick access toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20407'%3E%3C/svg%3E)

Now, you will see the ‘Fill Down’ icon appear in the QAT.

![Fill Down added to Quick Access toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20481%20200'%3E%3C/svg%3E)

Using Keyboard Shortcut
-----------------------

If you prefer using the [keyboard shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
, you can also use the below shortcut to achieve the fill down functionality:

CONTROL + D (hold the control key and then press the D key)

Below are the steps to use the keyboard shortcut to fill-down the formula:

1.  In cell A2, enter the formula: =B2\*15%
2.  Select all the cells in which you want to apply the formula (including cell C2)
3.  Hold the Control key and then press the D key

Using Array Formula
-------------------

If you’re using Microsoft 365 and have access to dynamic arrays, you can also use the array formula method to apply a formula to the entire column.

Suppose you have a data set as shown below and you want to calculate the Commission in column C.

Below is the formula that you can use:

\=B2:B15\*15%

![Array formula to apply formula to an entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20488'%3E%3C/svg%3E)

This is an Array formula that would return 14 values in the cell (one each for B2:B15). But since we have dynamic arrays, the result would not be restricted to the single-cell and would spill over to fill the entire column.

Note that you cannot use this formula in every scenario. In this case, because our formula uses the input value from an adjacent column and as the same length of the column in which we want the result (i.e., 14 cells), it works fine here.

But if this is not the case, this may not be the best way to copy a formula to the entire column

By Copy-Pasting the Cell
------------------------

Another quick and well-known method of applying a formula to the entire column (or selected cells in the entire column) is to simply copy the cell that has the formula and paste it over those cells in the column where you need that formula.

Below are the steps to do this:

1.  In cell A2, enter the formula: =B2\*15%
2.  Copy the cell (use the keyboard shortcut Control + C in Windows or Command + C in Mac)
3.  Select all the cells where you want to apply the same formula (excluding cell C2)
4.  Paste the copied cell (Control + V in Windows and Command + V in Mac)

One difference between this copy-paste method and all the methods convert below above this is that with this method you can choose to only paste the formula (and not paste any of the formattings).

For example, if cell C2 has a blue cell color in it, all the methods covered so far (except the array formula method) would not only copy and paste the formula to the entire column but also paste the formatting (such as the cell color, font size, bold/italics)

If you want to only apply the formula and not the formatting, use the steps below:

1.  In cell A2, enter the formula: =B2\*15%
2.  Copy the cell (use the keyboard shortcut Control + C in Windows or Command + C in Mac)
3.  Select all the cells where you want to apply the same formula
4.  Right-click on the Selection
5.  In the options that appear, click on ‘Paste Special’![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20391'%3E%3C/svg%3E)
6.  In the ‘Paste Special’ dialog box, click on the Formulas option![Select formulas in Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20449'%3E%3C/svg%3E)
7.  Click OK

The above steps would make sure that only the formula is copied to the selected cells (and none of the formattings comes over with it).

So these are some of the quick and easy methods that you can use to apply a formula to the entire column in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [5 Ways to Insert New Columns in Excel (including Shortcut & VBA)](https://trumpexcel.com/insert-columns-in-excel/)
    
*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [Lookup and Return Values in an Entire Row/Column in Excel](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/)
    
*   [How to Copy and Paste Columns in Excel?](https://trumpexcel.com/copy-paste-column-excel/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [How to Multiply a Column by a Number in Excel](https://trumpexcel.com/multiply-column-by-number-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/apply-formula-to-entire-column-excel/#respond)

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