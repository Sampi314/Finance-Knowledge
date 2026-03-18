# How to Copy Conditional Formatting to Another Cell in Excel

**Source:** https://trumpexcel.com/copy-conditional-formatting-another-cell-excel

---

[Skip to content](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#below-title)

Conditional Formatting in Excel enables you to quickly format a cell (or range of cells) based on the value or the text in it.

For example, below I have an example where I have student’s scores and I have used conditional formatting to highlight all the scores that are above 80.

If you’re interested in learning all the amazing things you can do with conditional formatting, check out this tutorial where I show some useful [conditional formatting examples](https://trumpexcel.com/excel-conditional-formatting/)
.

Once you have set the conditional formatting rules for a cell or range of cells, you can easily copy it to other cells on the same sheet or other sheets.

In this tutorial, I will show you **how to copy conditional formatting from one cell to another cell in Excel**. I will cover multiple ways to do this – such as simple copy-paste, copy and paste conditional formatting only, and using the format painter.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#)

Copy Conditional Formatting Using Paste Special
-----------------------------------------------

Just like you can copy and paste cells in the same sheet or even across sheets or workbooks, you can also copy and paste the conditional formatting from one cell to another.

Note that you can not just copy and paste the cell. You have to make sure that you copy a cell but only paste the conditional formatting rules in that cell (and not everything else such as the value or the formula).

And to make sure you only copy and paste the conditional formatting, you need to use Paste Special.

Suppose you have a dataset as shown below where I have conditional formatting applied to column B (the Math score) so that all the cells that have the value more than 80 get highlighted.

![Data set from which to copy conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20289'%3E%3C/svg%3E)

Now, what if I want to apply the same conditional formatting rule to the second column (for Physics score) os that all the cells above 80 are highlighted in green.

This can easily be done!

Below are the steps to copy conditional formatting from one cell to another:

1.  Select cell B2
2.  Right-click and copy it (or use the keyboard shortcut Control + C)![right-click and copy cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20361'%3E%3C/svg%3E)
3.  Select the entire range where you want to copy the conditional formatting (C2:C11 in this example)
4.  Right-click anywhere in the selection
5.  Click on the Paste Special option. This will open the Paste Special dialog box.![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20335'%3E%3C/svg%3E)
6.  In the Paste Special dialog box, select Formats![Click Format in the Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20449'%3E%3C/svg%3E)
7.  Click on OK

The above steps would copy the conditional formatting from column B and apply it to the selected cells in column C.

![Resulting data where conditional formatting has been copied and pasted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20288'%3E%3C/svg%3E)

One thing to remember when using Paste Special to copy conditional formatting is that it will copy all the formatting. So if there is any border in the cells or if the text has been made bold, etc., that would also be copied.

Note: The same steps shown above would also work when copying and pasting conditional formatting to cells in another sheet or even another workbook.

Also read: [Excel Conditional Formatting Based on Another Cell](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/)

Copy Conditional Formatting Using Format Painter
------------------------------------------------

Format painter is a tool that allows you to copy the format from a cell (or range of cells) and paste it.

And since conditional formatting is also a part of the formatting, you can also use format painter to copy and then paste it.

Suppose you have a dataset as shown below where I have conditional formatting applied to the Math score column so that all the cells that have the value more than 80 get highlighted.

Below are the steps to use format painter to copy conditional formatting from the Math score column and apply it to the Physics score column:

1.  Select the cell (or range of cells) from which you want to copy the conditional formatting
2.  Click the Home tab
3.  In the Clipboard group, click on the Format Painter icon![Click on Format Painter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20203'%3E%3C/svg%3E)
4.  Select all the cells where you want the copied conditional formatting to be applied

![Format Painter to copy conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20508'%3E%3C/svg%3E)

Pro tip: In case you want to copy the conditional formatting and paste it on multiple cells or ranges (that you can not select at one go), click on the Format painter icon twice. That will keep the format painter active and you can paste the formatting multiple times (unless you hit the Escape key).

Once you have the format painter activated, you can use it on the same sheet, on some other sheet in the same workbook, and even on the other workbook.

Again, just like with Paste Special, Format painter also copies all the formatting (including the conditional formatting).

Also read: [Conditional Formatting Not Working in Excel](https://trumpexcel.com/conditional-formatting-not-working/)

Issue when Copying Conditional Formatting
-----------------------------------------

In most cases, you will have no problems copying and pasting conditional formatting from one cell to another.

But you may face issues if you have used a custom formula to determine which cells to format.

This option allows you to create your own formula and formatting is applied in the formula returns TRUE for a cell and not applied when the formula returns FALSE.

If you have used a formula in conditional formatting that uses [absolute or mixed references](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
, then it may not work as expected when copied.

For example, in the below example, I have used the formula =$B2>=80 to highlight all cells in column B that have a value higher than 80.

![Conditional Formatting with a custom formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20287'%3E%3C/svg%3E)

But when I copy this conditional formatting to column C, it still references the B column and I get the wrong result (as shown below).

![Issue with copying Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20288'%3E%3C/svg%3E)

So, if you copy conditional formatting from one cell to another and don’t get the expected result, it’s best to check the formula used and adjust the references.

For example, in this case, I can change the formula to =B2>=80 and it should work fine.

If you’re wondering where the formula goes, click on the Home tab and then on Conditional Formatting.

In the options that appear, click on ‘New Rule’. In the New Formatting Rule dialog box, click on the option – Use a formula to determine which cells to format.

This will show you the field where you can enter the formula for the selected range. If this formula returns TRUE for the cell, it will get formatted and if it returns FALSE, it will not.

![Formula to enter in New Formatting rule dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20458'%3E%3C/svg%3E)

So these are two simple ways you can use to copy conditional formatting from one cell to another in Excel – using Paste Special and Format Painter.

And in case you see issues with it, check the custom formula used in it.

Hope you found this tutorial useful!

**Other Excel tutorials you may find useful:**

*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [Highlight EVERY Other ROW in Excel (using Conditional Formatting)](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [How to Remove Table Formatting in Excel](https://trumpexcel.com/remove-table-formatting-excel/)
    
*   [Search and Highlight Data Using Conditional Formatting](https://trumpexcel.com/search-highlight-using-conditional-formatting/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [Highlight the Active Row and Column in a Data Range in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [Copy and Paste Multiple Cells in Excel (Adjacent & Non-Adjacent)](https://trumpexcel.com/copy-paste-multiple-cells-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Copy Conditional Formatting to Another Cell in Excel”
---------------------------------------------------------------------------

1.  This doesn’t work.
    
    Irrespective of how I paste the call with the conditional formatting into the other cells, Excel
    
    Retains the same row for ALL other cells, instead of adjusting the condition to align with the new cells’ rows (e.g. copy conditional formatting from row 16 =(B16)=TODAY() to row 17 should yield the rule =(B17)=TODAY(). Instead, it yields the condition =(B16)=TODAY(), rendering it useless.
    
    and
    
    changes the “Apply to Range”
    
    I’ll specify the “Apply to” range to be, for example, H4; when I copy and paste the conditional formatting, Excel changes the Apply to Range to multiple cells in column H (e.g. $H4..$H5). Oh, and it always changes my relative cell references to absolute.
    
    Is anyone else experiencing this behavior?
    
    [Reply](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#comment-37762)
    
2.  i have an issue.  
    My formula is looking for none blank cells within the row B, when a non blank cell is TRUE in B i want the attached row to highlight, which I’ve done by selecting the row that highlights, but i cannot remove the $ signs which would usually allow me to copy it to all rows, how do i overcome this issue?
    
    [Reply](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#comment-15705)
    
3.  This is a helpful article. (I didn’t know the way to keep Format Painter active.) I am still looking for a way around the issue you pointed out with copying and pasting conditional formatting: All formatting from the source is applied. This is a problem for me since the number formatting from the source is applied to the destination with undesirable results.
    
    [Reply](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#comment-14746)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/#respond)

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