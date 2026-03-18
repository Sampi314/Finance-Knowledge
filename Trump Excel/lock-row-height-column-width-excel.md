# How to Lock Row Height & Column Width in Excel (Easy Trick)

**Source:** https://trumpexcel.com/lock-row-height-column-width-excel

---

[Skip to content](https://trumpexcel.com/lock-row-height-column-width-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/lock-row-height-column-width-excel/#below-title)

It’s quite easy to change a cell’s height and width in Excel.

The more you work with Excel, the more you would find yourself adjusting the row height and column width.

But in some cases, you may want to lock the cell height and width so that a user cannot make any changes to it.

One scenario where this may be needed could be when you have a fixed [template](https://trumpexcel.com/free-excel-templates/)
 that you share with other people and you don’t want them to mess up the formatting by changing the cell height/width.

In this tutorial, I will show you **how to lock the row height and column width in Excel** by making a simple change.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/lock-row-height-column-width-excel/#)

How to Lock Row Height and Column Width in Excel (Easy Trick)
-------------------------------------------------------------

When you protect a worksheet in Excel, also locks the row height and column width so that no one can change it.

But with sheet protection, all the cells are also locked and you cannot make any changes to it (i.e, you can not get into the edit mode or enter formulas).

While we want to lock the column width and the row height, we don’t want to [lock the cells](https://trumpexcel.com/lock-cells-in-excel/)
 completely.

And thankfully, you can do that in Excel.

For this to work, you need to do two things:

1.  Disable the ‘Locked’ property for all the cells
2.  Protect the worksheet so that row height and column width for each cell is locked

### Disabling the Lock Property for all Cells

Below are the steps to disable the lock property for all the cells, after which we can lock the row height and the column width:

1.  Select all the cells in the worksheet by clicking on the gray triangle at the top-left part of the worksheet.![Click on the gray triangle to select all cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20376'%3E%3C/svg%3E)
2.  Click the ‘Home’ tab![Click Home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20201'%3E%3C/svg%3E)
3.  In the Number group, click on the dialog box launcher icon (the small tilted arrow icon at the bottom right of the group)![Click the dialog box launcher in the Number group](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20201'%3E%3C/svg%3E)
4.  In the Format cells dialog box that opens up, click on the ‘Protection’ tab![Click the protection tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)
5.  Uncheck the Locked option![Disable the locked property](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)
6.  Click OK

By doing this we have ensured that even if we protect the entire worksheet the cells would still remain editable.

When you protect a worksheet in Excel, the cells would be completely locked (i.e., the user won’t be able to edit the cells and enter anything into it). But this happens only when the Locked property is enabled. If you disable the Locked property, the cells would remain editable even after protecting the worksheet.

Now, let’s move to the second step, which is to protect the entire sheet.

### Protecting the Entire Worksheet

Now let’s see how to quickly protect the entire worksheet.

1.  Click the ‘Review’ tab![Click the Review tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20201'%3E%3C/svg%3E)
2.  In the Protect group, click on the ‘Protect Sheet’ option![Click on Protect Sheet icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20201'%3E%3C/svg%3E)
3.  In the Protect Sheet dialog box that opens up, enter the password (optional)![Enter the password in Protect Sheet dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20334%20387'%3E%3C/svg%3E)
4.  Check all the options in the Protect Sheet dialog box (except the ‘Format Columns’ and ‘Format Rows’ options).![Row height and column options grayed out](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20334%20387'%3E%3C/svg%3E)
5.  Click OK

The above steps would protect the worksheet, but at the same time allow the user to do all the regular stuff such as formatting the cells or deleting/adding rows and columns.

Since we have disabled the format columns and format rows option (in the Protect Sheet dialog box), these will still remain locked for the user.

This means that the user won’t be able to change the row height or column width in this worksheet.

If you go to any a row header or column header and put your cursor at the edge of the header, you would see that your icon would not change (which earlier used to change into a double-pointed arrow and allow you to change the row height or column it by clicking and dragging the cursor)

Similarly, if you select any cell in the worksheet, click the Home tab, and then click on the Format option, you would see that the Row Height and Column Width options are now grayed out.

![Row height and column options grayed out](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20577'%3E%3C/svg%3E)

So, this is how you can lock the row height and column width in Excel.

Note that since we have protected the worksheet and only enabled certain options, there are some things that you won’t be able to do when you lock the row height and the column width using the above method. For example, if you want to insert new cells in a column/row or hide the rows and columns, you won’t be able to do that (as we have completely disabled the option to format rows and options in any manner)

I hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [Excel AUTOFIT: Make Rows/Columns Fit the Text Automatically](https://trumpexcel.com/autofit-excel/)
    
*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    
*   [Freeze Columns in Excel](https://trumpexcel.com/freeze-multiple-columns-excel/)
    
*   [Remove Password from VBA Project in Excel](https://trumpexcel.com/excel-vba/remove-password/)
    
*   [Excel Freeze Panes: Use it to Lock Row/Column Headers](https://trumpexcel.com/excel-freeze-panes/)
    
*   [How to Copy Column Widths in Excel (Shortcut)](https://trumpexcel.com/copy-column-width-excel/)
    
*   [Make Cells Bigger in Excel](https://trumpexcel.com/make-cells-bigger-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Lock Row Height & Column Width in Excel (Easy Trick)”
--------------------------------------------------------------------------

1.  Hi  
    you Have Very good Site
    
    [Reply](https://trumpexcel.com/lock-row-height-column-width-excel/#comment-44142)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/lock-row-height-column-width-excel/#respond)

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