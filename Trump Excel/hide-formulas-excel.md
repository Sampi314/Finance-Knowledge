# How to Hide Formulas in Excel (and Only Display the Value)

**Source:** https://trumpexcel.com/hide-formulas-excel

---

[Skip to content](https://trumpexcel.com/hide-formulas-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/hide-formulas-excel/#below-title)

When you share a normal Excel file with others, they are able to see and edit everything that the Excel file has.

If you don’t want them to change anything, you have the option to either protect the entire worksheet/workbook or protect certain cells that have important data (that you don’t want the user to mess up).

But even when you protect the worksheet, the end-user can still click on a cell and see the formula that’s used for calculations.

If you want to hide the formula so that the users cannot see those, you can do that as well.

In this exact tutorial, I will show you how to **hide formulas in Excel in a protected worksheet** (so that’s it’s not visible to the user).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/hide-formulas-excel/#)

How to Hide All Formulas in Excel
---------------------------------

When you have a formula in a cell, a user can see the formula in two ways:

1.  By double-clicking on the cells and getting into the edit mode
2.  By selecting the cell and seeing the formula in the formula bar

When you hide the formulas (as we’ll soon see how), the users won’t be able to edit the cell as well as not be able to see the formula in the formula bar.

Suppose you have a data set as shown below where you have the formula in column D.

![Formula that you need to hide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20338'%3E%3C/svg%3E)

Below are the steps to hide all the formulas in column D:

1.  Select the cells in column D that have the formula that you want to hide![Select the cells from which you want to hide the formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20287'%3E%3C/svg%3E)
2.  Click the ‘Home’ tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20478%20200'%3E%3C/svg%3E)
3.  In the ‘Number’ group, click on the dialog box launcher (it’s the small tilted arrow icon at the bottom right of the group)![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20479%20213'%3E%3C/svg%3E)
4.  In the ‘Format Cells’ dialog box that opens up, click the ‘Protection’ tab![Click on the Protection tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20288'%3E%3C/svg%3E)
5.  Check the Hidden option![Check the hidden option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20216'%3E%3C/svg%3E)
6.  Click OK
7.  Click the Review tab in the ribbon![Click the Review tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20637%20200'%3E%3C/svg%3E)
8.  In the Protect group, click on the Protect Sheet option![Click on Protect Sheet option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20200'%3E%3C/svg%3E)
9.  In the Protection dialog box, enter the password that would be needed if you want to unlock the worksheet (in case you don’t want to apply a password, you can leave this blank)![Enter the password in the Protect Sheet dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20398'%3E%3C/svg%3E)
10.  Click OK

The above steps would protect the entire worksheet in such a way that if you click on a cell that has a value you would see the value in the formula bar, but if you click on a cell that has a formula, no formula would be shown in the formula bar.

![Formula hidden in the formula bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20535'%3E%3C/svg%3E)

And since the worksheet is protected, you would not be able to double-click on the cell and get into the edit mode (so the formula is hidden that way as well).

While this method works fine, you need to know that the sheets/cells that are protected in Excel can easily be unlocked by the user.

Any tech-savvy user can easily break into your protected workbooks (a simple Google search will give them multiple ways to break the protected worksheet). It’s not straight-forward, but it’s not too hard.

But if you’re working with less tech-savvy users, adding a password should be enough.

Also read: [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)

How to Only Hide Formulas in Excel (And Keep Rest of the Cells Editable)
------------------------------------------------------------------------

In the above method, I showed you how to protect the entire worksheet (including the cells that have don’t have a formula in it).

But what if you don’t want to protect the entire worksheet? What if you only want to protect the cells that have formulas and hide these formulas from the user.

This could be the case when you want the users to input data (such as in a [data entry form](https://trumpexcel.com/data-entry-form/)
) but not be able to edit the formula or see it.

This can easily be done as well.

Unlike the previous method, where we protected all the cells in the worksheet, in this method we would only select the cells that have the formulas and protect these cells.

The remaining of the worksheet would remain open for the user to edit.

Suppose you have a data set as shown below where you only want to protect the formulas in column D (which has formulas).

![Formula that you need to hide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20338'%3E%3C/svg%3E)

For a cell to be protected, it needs to have the ‘Locked’ property enabled, as well as the protection enabled from the ribbon. Only when both of these happen does a cell truly becomes locked (i.e., can’t be edited).

This also means that if you disable the lock property for a few cells, these could still be edited after you protect the worksheet.

We will use this concept where we will disable the locked property for all the cells except the ones that have formulas in it.

Let’s see how to do this.

### Step 1 – Disable the Lock Property for all the Cells

So, we first need to disable the Locked property for all the cells (so that these can’t be protected)

Below are the steps to do this:

1.  Select all the cells in the worksheet (you can do this by clicking on the gray triangle at the top left part of the sheet).![Click on the gray triangle](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20462'%3E%3C/svg%3E)
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20478%20200'%3E%3C/svg%3E)
3.  In the Number group, click on the dialog box launcher![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20479%20213'%3E%3C/svg%3E)
4.  In the Format cells dialog box, click on the ‘Protection’ tab![Click on the Protection tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20288'%3E%3C/svg%3E)
5.  Uncheck the Locked option![Uncheck the locked option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20255'%3E%3C/svg%3E)
6.  Click Ok

The above steps have disabled the locked property for all the cells in the worksheet.

Now, even if I go and protect the sheet using the option in the ribbon (Review >> Protect Sheet), the cells would not be completely locked and you can still edit the cells.

### Step 2 – Enable the Locked and Hidden Property only for Cells with Formulas

To hide the formula from all the cells in the worksheet, I now need to somehow identify the cells that have the formula and then lock these cells.

And while locking these cells, I would make sure that the formula is hidden from the formula bar as well.

Below are the steps to hide formulas:

1.  Select all the cells in the worksheet (you can do this by clicking on the gray triangle at the top left part of the sheet).
2.  Click the Home tab
3.  In the editing group, click on the Find & Select option![Click on Find and Select](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20171'%3E%3C/svg%3E)
4.  Click on the ‘Go-To Special’ option.![Click on Go To Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20562'%3E%3C/svg%3E)
5.  In the Go To Special dialog box, click on the Formulas option. This will select all the cells that have a formula in it![Select the Formulas option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20364%20451'%3E%3C/svg%3E)
6.  With the cells with formulas selected, hold the Control key and then press the 1 key (or the Command key and the 1 key if using Mac). This will open the Number Format dialog box
7.  Click on the ‘Protection’ tab
8.  Make sure ‘Locked’ and ‘Hidden’ options are checked![Check the Locked and Hidden option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20250'%3E%3C/svg%3E)
9.  Click Ok

Also read: [Highlight Cells With Formulas in Excel](https://trumpexcel.com/highlight-cells-with-formulas-excel/)

### Step 3 – Protecting the Worksheet

In the process so far, the Locked property is disabled for all the cells except the ones that have a formula in it.

So now, if I protect the entire worksheet, only those cells would be protected that have a formula (as you need the Locked property to be enabled to truly lock a cell).

Here are the steps to do this:

1.  Click the Review tab![Click the Review tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20637%20200'%3E%3C/svg%3E)
2.  In the Protect group, click on the ‘Protect Sheet’ option![Click on Protect Sheet option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20200'%3E%3C/svg%3E)
3.  In the Protect Sheet dialog box, enter the password (optional)![Enter the password in the Protect Sheet dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20398'%3E%3C/svg%3E)
4.  Click Ok

The above steps would lock only those cells that have a formula in it and at the same time hide the formula from the users.

The users won’t be able to double-click and get into the edit mode as well as see the formula in the formula bar.

Also read: [Excel Formulas Not Working](https://trumpexcel.com/excel-formulas-not-working/)

How to Hide Formulas Without Protecting the Worksheet
-----------------------------------------------------

If you’re wondering whether you can hide the formulas in Excel without protecting the sheet, unfortunately, **you can’t**.

While you can get this done by using a complex VBA code, it would be unreliable and can lead to other issues. Here is an article that [shares such a code](https://www.extendoffice.com/documents/excel/4787-excel-hide-formula-without-protecting-sheet.html)
 (use it if you really really can’t do without it)

As of now, the only way to hide the formulas in Excel is to protect the sheet and also make sure that the hidden properties enabled for the cells that have the formula.

I hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    
*   [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)
    
*   [How to Hide a Worksheet in Excel (that can not be unhidden)](https://trumpexcel.com/hide-worksheet/)
    
*   [How to Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [How to Unhide Sheets in Excel](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Hide or Show Formula Bar in Excel?](https://trumpexcel.com/show-hide-formula-bar-excel/)
    
*   [Excel Showing Formula Instead of Result](https://trumpexcel.com/excel-showing-formula-instead-of-result/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Hide Formulas in Excel (and Only Display the Value)”
--------------------------------------------------------------------------

1.  thank you very much it is helpful for me
    
    [Reply](https://trumpexcel.com/hide-formulas-excel/#comment-36912)
    
2.  Thank you! This worked and was helpful.
    
    [Reply](https://trumpexcel.com/hide-formulas-excel/#comment-35713)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/hide-formulas-excel/#respond)

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