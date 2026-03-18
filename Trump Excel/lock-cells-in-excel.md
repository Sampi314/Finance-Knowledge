# How to Lock Cells in Excel (Step-by-Step Tutorial + Video)

**Source:** https://trumpexcel.com/lock-cells-in-excel

---

[Skip to content](https://trumpexcel.com/lock-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/lock-cells-in-excel/#below-title)

**Watch Video – How to Lock Cells in Excel**

Sometimes you may want to lock cells in Excel so that other people can’t make changes to it.

It could be to avoid tampering of critical data or prevent people from making changes in the formulas.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/lock-cells-in-excel/#)

How to Lock Cells in Excel
--------------------------

Before we learn how to lock cells in Excel, you need to understand how it works on a conceptual level.

All cells in Excel are locked by default.

But…

It doesn’t work until you also protect these cells.

Only when you have a combination of cells that are **locked** and **protected** can you truly prevent people from making changes.

In this tutorial, you’ll learn:

*   How to lock all the cells in a worksheet in Excel.
*   How to lock some specific cells in Excel.
*   How to [hide formula](https://trumpexcel.com/hide-formulas-excel/)
     from the locked cell.

So let’s get started.

### Lock all the Cells in a Worksheet in Excel

This essentially means that you want to lock the entire worksheet.

Now, since we already know that all the cells are locked by default, all we need to do is to protect the entire worksheet.

Here are the steps to lock all the cells in a worksheet.

*   Click the Review tab.
*   In the Changes group, click on Protect Sheet.![How to Lock Cells in Excel - Protect Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20135'%3E%3C/svg%3E)
*   In the Protect Sheet dialog box:
    *   Make sure that you’ve checked the box ‘Protect worksheet and contents of locked cells’ (it’s checked by default).![Protect Sheet dialog box - selected locked cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20320'%3E%3C/svg%3E)
    *   Enter a password (if you want to password protect the sheet).![Lock Cells in Excel - Protect Sheet dialog box enter password](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20321'%3E%3C/svg%3E)
    *   Specify what a user is allowed to do. By default, the first two boxes are checked that allows a user to select locked and unlocked cells. You can allow other options as well such as formatting or inserting rows/columns.![How to Lock Cells in Excel - Protect Sheet dialog box3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)
    *   Click OK.![How to Lock Cells in Excel - Protect Sheet dialog box4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)

If you have used a password, it will ask you to reconfirm the password.

Once locked, you’ll notice that most of the options in the ribbon are unavailable, and if someone tries to change anything in the worksheet, it shows a prompt (as shown below):

![Error when you try to edit locked cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20803%20125'%3E%3C/svg%3E)

To unlock the worksheet, go to Review –> Changes –> Protect Sheet. If you had used a password to lock the worksheet, it will ask you to enter that password to unlock it.

Also read: [Freeze Columns in Excel](https://trumpexcel.com/freeze-multiple-columns-excel/)

### Lock Some Specific Cells in Excel

Sometimes, you may want to lock some specific cells that contain crucial data points or formulas.

In this case, you need to simply protect the cells that you want to lock and leave the rest as is.

Now, since all the cells are locked by default, if you protect the sheet, all the cells would get locked. Hence you need to first make sure only the cells that you want to protect are locked, and then protect the worksheet.

Here is a simple example where I want to lock B2 and B3, and these contain values that are not to be changed.

![How to Lock Cells in Excel - PMT Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20309%20146'%3E%3C/svg%3E)

Here are the steps to lock these cells:

*   Select the entire sheet, and click on the dialog box launcher in the Alignment group in the Home tab (you can also use the keyboard shortcut Control + 1).![Dialog box launcher to Open format cells dialog box ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20140'%3E%3C/svg%3E)
*   In the Format Cells dialog box, in the Protection tab, uncheck the box for Locked.![How to Lock Cells in Excel - locked unchecked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20258'%3E%3C/svg%3E)
*   Click OK.
*   Select the cells that you want to lock (in this case, B2 and B3).
*   Again click on the dialog box launcher in the Alignment group within the Home tab (or use the keyboard shortcut Control + 1).
*   In the Format Cells dialog box, in the Protection tab, check the box for Locked. The steps so far would unlock all the cells in the worksheet except the ones that you want to lock (B2 and B3 in this case).![How to Lock Cells in Excel - locking cell B2 and B3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20241'%3E%3C/svg%3E)
*   Go to the Review tab.
*   In the Changes group, click on Protect Sheet.
*   In the Protect Sheet dialog box:
    *   Make sure you’ve checked the box ‘Protect worksheet and contents of locked cells’ (it’s checked by default).![Protect Sheet dialog box - checked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20320'%3E%3C/svg%3E)
    *   Enter a password (if you want to password protect the sheet).![Protect Sheet dialog box2 when locking cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20321'%3E%3C/svg%3E)
    *   Specify what all a user is allowed to do. By default the first two boxes are checked that allows a user select locked and unlocked cells. You can allow other options as well such as formatting or inserting rows/columns.![How to Lock Cells in Excel - Protect Sheet dialog box3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)
    *   Click OK.![How to Lock Cells in Excel - Protect Sheet dialog box4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)

If you have used a password, it will ask you to reconfirm the password.

Also read: [Unprotect Excel Sheets Without Password](https://trumpexcel.com/unprotect-excel-sheets-without-password/)

### Protect the Entire Sheet (except a few cells)

If you want to protect the entire worksheet, but keep some cell unlocked, you can do that as well.

This can be the case when you have interactive features (such as a [drop-down](https://trumpexcel.com/excel-drop-down-list/)
 list) that you want to keep functioning even in a protected worksheet.

Here are the steps to do this:

1.  Select the cell(s) that you want to keep unlocked.
2.  Press Control + 1 (hold the control key and then press 1).
3.  In the Format Cells box that opens, click on the ‘Protection’ tab.
4.   Uncheck the Locked option.![Format Cells Dialog box when protecting a worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20220'%3E%3C/svg%3E)
5.  Click OK.

Now when you protect the entire worksheet, these cells would continue to work as normal. So if you have a drop-down list in it, you can continue to use it (even when the rest of the sheet is locked).

Here are the steps to now protect the entire sheet (except the selected cells):

*   Click the Review tab.
*   In the Changes group, click on Protect Sheet.![Protect Sheet option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20135'%3E%3C/svg%3E)
*   In the Protect Sheet dialog box:
    *   Make sure that you’ve checked the box ‘Protect worksheet and contents of locked cells’ (it’s checked by default).![Protect Sheet dialog box - selected locked cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20320'%3E%3C/svg%3E)
    *   Enter a password (if you want to password protect the sheet).![Lock Cells in Excel - Protect Sheet dialog box enter password](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20321'%3E%3C/svg%3E)
    *   Specify what a user is allowed to do. By default, the first two boxes are checked that allows a user to select locked and unlocked cells. You can allow other options as well such as formatting or inserting rows/columns.![How to Lock Cells in Excel - Protect Sheet dialog box3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)
    *   Click OK.![How to Lock Cells in Excel - Protect Sheet dialog box4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20319'%3E%3C/svg%3E)

If you have used a password, it will ask you to reconfirm the password.

### Hide Formula When the Cells are Locked

Once you lock a cell in Excel, and that cell contains a formula, it’s visible in the formula bar when the cell is selected.

If you don’t want the formula to be visible, here are the steps:

*   Select the cells that you want to lock and also hide the formula from being displayed in the formula bar.
*   Click on the dialog box launcher in the Alignment group in the Home tab (or use the keyboard shortcut Control + 1).
*   In the Format Cells dialog box, in the Protection tab, check the Hidden box.![How to Lock Cells in Excel - hide formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20268'%3E%3C/svg%3E)

Now when you protect the cells, the formula in it wouldn’t be visible in the formula bar.

TIP: Another way to hide the formula from getting displayed is by disabling the selection of the cell. Since the user can’t select the cell, it’s content wouldn’t get displayed in the formula bar.

So these are some of the ways you can lock cells in Excel. You can lock the entire sheet or only specific cells.

A lot of people ask me if there is a shortcut to lock cells in Excel. While there is no inbuilt one, I am sure you can create one using VBA.

I hope you found this tutorial useful!

**You May Also Like the Following Excel Tutorials:**

*   [How to Lock Formulas in Excel.](https://trumpexcel.com/lock-formulas-excel/)
    
*   [How to Use Excel Freeze Panes](https://trumpexcel.com/excel-freeze-panes/)
    .
*   [Excel VLOOKUP Function Examples](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [How to Insert and Use a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Using Track Changes in Excel.](https://trumpexcel.com/track-changes-in-excel/)
    
*   [Unhide Columns in Excel](https://trumpexcel.com/unhide-columns/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “How to Lock Cells in Excel”
------------------------------------------

1.  Too good this tutorial,,
    
    [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-12729)
    
2.  Thank you Sumit! My students will find it very simple to understand along with the snapshots provided.
    
    [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-11843)
    
3.  Thanks Mr. Sumit. Its realy helpful.
    
    [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3356)
    
    *   Thanks for commenting Khairul.. I am glad you’re finding the tutorial helpful!
        
        [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3570)
        
4.  Hi Sumit, thanks for the excellent post. These tips and tricks keep me in my day job as the resident excel guru. Thanks a million.
    
    [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3334)
    
    *   Thanks for the kind words.. I am glad these tutorials are helping you in your day job!
        
        [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3571)
        
5.  Very nicely written. Thanks for sharing, Sumit. Is there any way to protect the sheet and still have a Table auto-expand? I have some calculated columns in table and would like the auto-expand functionality but lock the formulas in calculated columns. Is it possible? Thanks in advance for your time.
    
    [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3326)
    
    *   I can’t think of doing it any way except VBA
        
        [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3572)
        
        *   Thanks, Sumit. If you know of any articles that will help me write that code, please provide links. Thank you.
            
            [Reply](https://trumpexcel.com/lock-cells-in-excel/#comment-3576)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/lock-cells-in-excel/#respond)

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