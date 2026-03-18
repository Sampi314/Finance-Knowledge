# Absolute, Relative, and Mixed Cell References in Excel

**Source:** https://trumpexcel.com/absolute-relative-mixed-cell-references

---

[Skip to content](https://trumpexcel.com/absolute-relative-mixed-cell-references/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/absolute-relative-mixed-cell-references/#below-title)

A worksheet in Excel is made up of cells. These cells can be referenced by specifying the row value and the column value.

For example, A1 would refer to the first row (specified as 1) and the first column (specified as A). Similarly, B3 would be the third row and second column.

The power of Excel lies in the fact that you can use these cell references in other cells when creating formulas.

Now there are three kinds of cell references that you can use in Excel:

*   Relative Cell References
*   Absolute Cell References
*   Mixed Cell References

Understanding these different types of cell references will help you work with formulas and save time (especially when copy-pasting formulas).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/absolute-relative-mixed-cell-references/#)

What are Relative Cell References in Excel?
-------------------------------------------

Let me take a simple example to explain the concept of relative cell references in Excel.

Suppose I have a data set shown below:

![Relative Cell References in Excel Spreadsheets - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20265'%3E%3C/svg%3E)

To calculate the total for each item, we need to multiply the price of each item with the quantity of that item.

For the first item, the formula in cell D2 would be B2\* C2 (as shown below):

![Relative Cell References in Excel Spreadsheets - Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20310'%3E%3C/svg%3E)

Now, instead of entering the formula for all the cells one by one, you can simply copy cell D2 and paste it into all the other cells (D3:D8). When you do it, you will notice that the cell reference automatically adjusts to refer to the corresponding row. For example, the formula in cell D3 becomes B3\*C3 and the formula in D4 becomes B4\*C4.

![Relative Cell References changes when formulas are copied](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20312'%3E%3C/svg%3E)

These cell references that adjust itself when the cell is copied are called **relative cell references in Excel**.

### **When to Use Relative Cell References in Excel?**

Relative cell references are useful when you have to create a formula for a range of cells and the formula needs to refer to a relative cell reference.

In such cases, you can create the formula for one cell and copy-paste it into all cells.

What are Absolute Cell References in Excel?
-------------------------------------------

Unlike relative cell references, absolute cell references don’t change when you copy the formula to other cells.

For example, suppose you have the data set as shown below where you have to calculate the commission for each item’s total sales.

The commission is 20% and is listed in cell G1.

![Absolute Cell reference in Excel - Dataset blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20266'%3E%3C/svg%3E)

To get the commission amount for each item sale, use the following formula in cell E2 and copy for all cells:

**\=D2\*$G$1**

![Absolute Cell reference in Excel - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20758%20309'%3E%3C/svg%3E)

Note that there are two dollar signs ($) in the cell reference that has the commission – **$**G**$**2.

### **What does the Dollar ($) sign do?**

A dollar symbol, when added in front of the row and column number, makes it absolute (i.e., stops the row and column number from changing when copied to other cells).

For example, in the above case, when I copy the formula from cell E2 to E3, it changes from =D2\*$G$1 to =D3\*$G$1.

Note that while D2 changes to D3, $G$1 doesn’t change.

Since we have added a dollar symbol in front of ‘G’ and ‘1’ in G1, it wouldn’t let the cell reference change when it’s copied.

Hence this makes the cell reference absolute.

### **When to Use Absolute Cell References in Excel?**

Absolute cell references are useful when you don’t want the cell reference to change as you copy formulas. This could be the case when you have a fixed value that you need to use in the formula (such as tax rate, commission rate, number of months, etc.)

While you can also hard code this value in the formula (i.e., use 20% instead of $G$2), having it in a cell and then using the cell reference allows you to change it at a future date.

For example, if your commission structure changes and you’re now paying out 25% instead of 20%, you can simply change the value in cell G2, and all the formulas would automatically update.

What are Mixed Cell References in Excel?
----------------------------------------

Mixed cell references are a bit more tricky than the absolute and relative cell references.

There can be two types of mixed cell references:

*   The row is locked while the column changes when the formula is copied.
*   The column is locked while the row changes when the formula is copied.

Let’s see how it works using an example.

Below is a data set where you need to calculate the three tiers of commission based on the percentage value in cell E2, F2, and G2.

![Mixed Cell References in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20324'%3E%3C/svg%3E)

Now you can use the power of mixed reference to calculate all these commissions with just one formula.

Enter the below formula in cell E4 and copy for all cells.

\=$B4\*$C4\*E$2

![Mixed Cell References in Excel - Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20362'%3E%3C/svg%3E)

The above formula uses both kinds of mixed cell references (one where the row is locked and one where the column is locked).

Let’s analyze each cell reference and understand how it works:

*   **$B4 (and $C4)** –  In this reference, the dollar sign is right before the Column notation but not before the Row number. This means that when you copy the formula to the cells on the right, the reference will remain the same as the column is fixed. For example, if you copy the formula from E4 to F4, this reference would not change. However, when you copy it down, the row number would change as it is not locked.
*   **E$2** – In this reference, the dollar sign is right before the row number, and the Column notation has no dollar sign. This means that when you copy the formula down the cells, the reference will not change as the row number is locked. However, if you copy the formula to the right, the column alphabet would change as it’s not locked.

How to Change the Reference from Relative to Absolute (or Mixed)?
-----------------------------------------------------------------

To change the reference from relative to absolute, you need to add the dollar sign before the column notation and the row number.

For example, A1 is a relative cell reference, and it would become absolute when you make it $A$1.

If you only have a couple of references to change, you may find it easy to change these references manually. So you can go to the formula bar and edit the formula (or select the cell, press F2, and then change it).

However, a faster way to do this is by using the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 – F4.

When you select a cell reference (in the formula bar or in the cell in edit mode) and press F4, it changes the reference.

Suppose you have the reference =A1 in a cell.

Here is what happens when you select the reference and press the F4 key.

*   **Press F4 key once:** The cell reference changes from A1 to $A$1 (becomes ‘absolute’ from ‘relative’).
*   **Press F4 key two times:** The cell reference changes from A1 to A$1 (changes to mixed reference where the row is locked).
*   **Press F4 key three times:** The cell reference changes from A1 to $A1 (changes to mixed reference where the column is locked).
*   **Press F4 key four times:** The cell reference becomes A1 again.

**You May Also Like the Following Excel Tutorials:**

*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [How to Lock Cells in Excel.](https://trumpexcel.com/lock-cells-in-excel/)
    
*   [Excel Freeze Panes: Use it to Lock Row/Column Headers](https://trumpexcel.com/excel-freeze-panes/)
    .
*   [How to Lock Formulas in Excel.](https://trumpexcel.com/lock-formulas-excel/)
    
*   [How to Reference Another Sheet or Workbook in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [How to Find Circular Reference in Excel](https://trumpexcel.com/find-circular-reference-excel/)
    
*   [Using A1 or R1C1 Reference Notation in Excel (& How to Change These)](https://trumpexcel.com/a1-r1c1-reference-notation-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “Absolute, Relative, and Mixed Cell References in Excel”
-----------------------------------------------------------------------

1.  I have these 2 sheets, and I want to copy the exact data from sheet 1 to sheet 2.  
    Note that in sheet 2 it should have those spaces in between before I put the name
    
    Sheet 1 Sheet 2
    
    Name1 Name1  
    Name 2  
    Name 3  
    Name 4 Name 2
    
    Name3
    
    Name 4
    
    In sheet 2 , I will use the formula to copy a cell it will will just have =B7  
    but if I will copy this formula to Sheet2 in the next line which is the position of Name 2 it will give me the  
    value of Name 4 instead because it skips 2 lines from sheet 1, what will I put in the formula so that  
    it will tell just to skip one row at a time when copied to Sheet2.
    
    Thanks for your answer
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-13563)
    
2.  Thank you so much, it helps me a lot
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-12231)
    
3.  Wonderful
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-12198)
    
4.  Really very helpful, you decribe this in a very easiest way.. Thank you!!
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-12122)
    
5.  VERY NICE
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-12070)
    
6.  This tutorial has make understand the three terms better
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-11835)
    
7.  It’s good but would be better if added the differences
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-11820)
    
8.  Very helpful tutorial!
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-11665)
    
9.  Thanks! I’m always looking forward to your tutorials, getting notifications by email is very useful!! Thanks again
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-9648)
    
    *   Thanks for commenting.. Happy to know that you find the tutorials useful 🙂
        
        [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-9685)
        
10.  Very vital and informative in a simple manner. I like flow of the article.
    
    [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-9623)
    
    *   Thanks for commenting.. Glad you liked the tutorial!
        
        [Reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#comment-9684)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/absolute-relative-mixed-cell-references/#respond)

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