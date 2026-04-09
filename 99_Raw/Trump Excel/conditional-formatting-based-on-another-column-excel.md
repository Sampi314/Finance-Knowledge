# Apply Conditional Formatting Based on Another Column in Excel

**Source:** https://trumpexcel.com/conditional-formatting-based-on-another-column-excel

---

[Skip to content](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/#below-title)

[Conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 allows you to apply a format to a cell based on the value in it. in most cases, you will apply conditional formatting to the same cell for which you are analyzing the value.

But in some cases, you may want to apply conditional formatting to a cell or column based on values in another column.

A simple example of this could be when I have the names of students and their scores in two separate columns, and I want to highlight those names where the students have scored less than 35.

![Data with Names highlighted using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20465'%3E%3C/svg%3E)

In this tutorial, I will show you to **apply conditional formatting to one column based on the values in another column or cell**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/#)

Apply Conditional Formatting Based on Another Column
----------------------------------------------------

Below I have a data set with student names and their scores in two separate columns, and I want to highlight the names of those students that have scored less than 35.

![Score and Name Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20465'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the range that has the names

![Select the names you want to highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20466'%3E%3C/svg%3E)

2.  Click the Home tab in the ribbon

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20223'%3E%3C/svg%3E)

3.  Click on the Conditional Formatting icon (in the Styles group)

![Click on Conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20223'%3E%3C/svg%3E)

4.  Click on ‘New Rule’ option

![Click on New Rule option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20267%20629'%3E%3C/svg%3E)

5.  In the New Formatting Rule dialog box, select – “Use a formula to determine which cells to format” option

![Select Use a Formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the following formula in the field: =$B2<35

![Enter the formula based on which to highlight names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button (to specify the formatting in which you want the names to be highlighted)
8.  Select the formatting (I will go with yellow color)

![Select the color to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20597'%3E%3C/svg%3E)

9.  Click OK

The above steps would apply color to those names that have scored less than 35.

![Names are highlighted based on score](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20466'%3E%3C/svg%3E)

Since Conditional Formatting is dynamic, if you change the score in column B, the Conditional Formatting rule will be checked again, and if the score is less than 35 then that name would get highlighted in yellow color.

**How does this work?**

We have used a formula (\=$B2<35) in Conditional Formatting, which is checked for each of the cells in the selected range. In our example, we selected the range A2:A14.

Every cell in this range is checked for the above formula, and if returns TRUE, then the cell with the name gets highlighted in the specified format (yellow color), and if it returns FALSE, no formatting is applied.

*   For the first cell, formula would be \=$B2<35
*   For the second cell, formula would be \=$B3<35
*   For the third cell, formula would be \=$B4<35

You get the idea!

Also read: [Excel Conditional Formatting Based on Another Cell](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/)

Apply Conditional Formatting to Entire Column Based on Value in a Cell
----------------------------------------------------------------------

Another example where you can use the same concept is when you want to highlight all the cells in a range based on the value in one specific cell.

Below I have a data set where I have the names of the Sales Rep in column A, their sales values in column B, and the sales target in cell D2.

![Sales Data with Target in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20421'%3E%3C/svg%3E)

For this to work, I will have to compare the sale value with the sales target, and if the sale value is higher than the Sales target value, then I want to highlight the name of the Sales Rep.

Below are the steps to do this:

1.  Select the cells that have the names
2.  Click the Home tab
3.  Click on the Conditional Formatting icon
4.  Click on New Rule option

![Click on New Rule option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20267%20629'%3E%3C/svg%3E)

5.  In the New Formatting Rule dialog box, select – “Use a formula to determine which cells to format” option
6.  Enter the following formula in the field: =$B2>=$D$2

![Enter formula in Conditional Formatting Rule dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click on the Format button
8.  Specify the formatting in which you want to highlight the names that have more than $25,000 commission
9.  Click OK

The above steps will compare the sales figures for all the Sales Rep with the value in cell D2, and if the sale value is higher than the value in cell D2, it will highlight the names.

![Names with less than value in a cell are highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20421'%3E%3C/svg%3E)

In case you change the value in cell D2, Conditional Formatting will update and highlight names where the sales value is more than the specified value in cell D2.

**Understanding the Formula**

In the above formula, I have compared all the sales values in column B with values in one single cell (D2). For this, I have used $D$2 in the formula.

When you add a dollar sign before the column alphabet or the row number, it makes sure that when the formula is copied to other cells, this value does not change.

For example, when the formula in Conditional Formatting compares the value in cell B2, the formula it assesses is =$B2>=$D$2

For B3, the formula becomes =$B3>=$D$2

For B4, it becomes =$B4>=$D$2

This way, all the sales values in column B are compared with the same value in cell D2.

So this is how you can use a simple formula to apply conditional formatting based on another column or another cell value in Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like**:

*   [How to Select Entire Column (or Row) in Excel – Shortcut](https://trumpexcel.com/select-entire-column-excel/)
    
*   [How to Apply Formula to Entire Column in Excel](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    
*   [How to Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)
    
*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [Highlight EVERY Other ROW in Excel (using Conditional Formatting)](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [Excel Quick Analysis Tool – How to Best Use it?](https://trumpexcel.com/excel-quick-analysis-tool/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/#respond)

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