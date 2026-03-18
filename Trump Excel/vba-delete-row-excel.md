# How to Delete Entire Row in Excel Using VBA (Examples)

**Source:** https://trumpexcel.com/vba-delete-row-excel

---

[Skip to content](https://trumpexcel.com/vba-delete-row-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-delete-row-excel/#below-title)

Adding and deleting rows is part of everyday common tasks when working with Excel.

While you can do this easily from the worksheet itself, sometimes you may want to use the VBA route to delete rows in Excel. These could be deleting a specific row, multiple rows in the selection, deleting alternate rows or those that have a specific value in it.

In this tutorial, I will show you how to delete rows in Excel using VBA (multiple scenarios).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-delete-row-excel/#)

Delete an Entire Row using VBA
------------------------------

To delete an entire row in Excel using VBA, you need to use the EntireRow.Delete method.

For example, if you want to delete the entire first row in a worksheet, you can use the below code:

Sub DeleteEntireRow()
Rows(1).EntireRow.Delete
End Sub

The above code first specifies the row that needs to be deleted (which is done by specifying the number in bracket) and then uses the EntireRow.Delete method to delete it.

You can also delete multiple rows by specifying these rows in the code.

For example, the below code will delete row number 1, 5 and 9 in the worksheet:

Sub DeleteEntireRow()
Rows(9).EntireRow.Delete
Rows(5).EntireRow.Delete
Rows(1).EntireRow.Delete
End Sub

The above code uses the same logic, where it specifies the row numbers and Excel will delete these rows one by one.

IMPORTANT: When you’re deleting rows with something similar to the above code, remember to start deleting from the bottom and then go up. For example, in case you start at the top and delete row 1 first, all the rows below it would be shifted one row up and the numbering would be off (as row 5 would become row 4 and so on)

Also read: [How to Delete Rows in Excel (Single or Multiple)?](https://trumpexcel.com/delete-rows/)

Delete All Rows in the Selection
--------------------------------

In case you want to delete all the rows in a selected range of cells, you can use the VBA macro code below:

Sub DeleteEntireRow()
Selection.EntireRow.Delete
End Sub

The above code applies to the _EntireRow.Delete_ method to the entire selection.

Also read: [Remove Duplicate Values in Excel Using VBA](https://trumpexcel.com/excel-vba/remove-duplicate-values/)

Delete Alternate rows (or Delete Every Third/Fourth/Nth Row)
------------------------------------------------------------

Sometimes, you may get a data dump where every second row (or third, fourth or Nth rows) is useless and needs to be deleted.

I used to work with financial data where every second row was empty and had to be deleted.

This is the type of scenario where VBA really shines.

Below is the VBA code that will go through all the rows in the selection and delete every second row:

Sub DeleteAlternateRows()
RCount = Selection.Rows.Count
For i = RCount To 1 Step -2
    Selection.Rows(i).EntireRow.Delete
Next i
End Sub

Let me explain how this VBA code works.

First, I have used a variable _RCount_ to get the total number of rows in the selection.

Then I have used a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to run this as many times as many rows are there. For example, if there are 12 rows, this loop will run from 12 to 1 (i.e., 12 times). It’s important to run this from the last row in the selection to the first as we don’t want the row numbers to change when a row is deleted.

Also, Step -2 is used since we need to [delete every other row](https://trumpexcel.com/delete-every-other-row-excel/)
 (from bottom to top). In case you want to delete every third row, you can use -3.

Within the [VBA loop](https://trumpexcel.com/vba-loops/)
, I have used the Selection.Rows(i).EntireRow.Delete method to delete every alternate row.

Delete Blank Rows with VBA
--------------------------

You can also use the EntireRow.Delete method to [delete all blank rows](https://trumpexcel.com/delete-blank-rows-excel/)
.

Below is the VBA code that will select blank cells in the selected dataset and delete the entire row.

Sub DeleteBlankRows()
Selection.SpecialCells(xlCellTypeBlanks).EntireRow.Delete
End Sub

The above code uses the SpecialCells property to select and delete all the cells that are blank. This is the same method that also allows us to use ‘Go To Special’ dialog box to select all blank cells.

Once these blank cells are identified using SpecialCell, these are then deleted using the EntireRow.Delete method.

Note: This method selects cells that are blank and don’t check whether the entire row is blank or not. So if anyone cell is empty in a row, this would still delete the entire row.

Delete Rows with a Specific Word/Value
--------------------------------------

You can also use a simple VBA code to go through each cell in the selected range and delete all the rows where a cell contains a specific text or value.

For example, suppose you have a dataset and I want to delete all cells that have the text Printer in column 2 of the selection.

![Dataset from where delete entire row with specific value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20308'%3E%3C/svg%3E)

Below is the code that will do this:

Sub DeleteRowswithSpecificValue()
For i = Selection.Rows.Count To 1 Step -1
If Cells(i, 2).Value = "Printer" Then
Cells(i, 2).EntireRow.Delete
End If
Next i
End Sub

The above code first counts the total number of rows in the selection. This will make sure the loop is run only these many times. It then uses the ‘For Next loop’ to go through all the cells in Column 2.

The [IF THEN ELSE statement](https://trumpexcel.com/if-then-else-vba/)
 is then used to check the value in each cell in column 2. And in case the value/text matches the specified text (which is ‘Printer’ in this example).

In this example, I have checked whether the text matches a specific string or not. You can also do this with values. For example, you can delete all rows where the sale value is less than 1000 or more than 1000.

Note: An important thing to note here is that the loop runs from _Selection.Rows.Count To 1_ to make sure when a row is deleted, it doesn’t impact the rows above it.

How to Use This VBA Code
------------------------

Now let me show you how to use all the codes mentioned in this tutorial to delete the entire row.

You need to copy and paste these codes in a module in Excel VB Editor. Once you have these codes copied, you can then run the macro codes.

Below are the steps to copy and paste these VBA codes in a module:

1.  Hold the ALT key and press the F11 key (or Function + Option + F11 in Mac). This will open the VB Editor
2.  In the VB Editor, you will have the project explorer on the left. If you don’t see it, go to the View option and then click on Project Explorer.![Click on Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20353%20479'%3E%3C/svg%3E)
3.  Right-click on any object in the Project Explorer (for the workbook in which you want to run the code).![Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20514'%3E%3C/svg%3E)
4.  Go to Insert and then click on Module. This will insert a new Module for the workbook![Copy and paste to delete entire row in the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20278'%3E%3C/svg%3E)
5.  Copy and Paste the above codes in the module.

And to run these codes, you can place the cursor anywhere in the code (that you want to run) and hit the F5 key (or click on the green triangle in the VBA toolbar).

I have also written a detailed tutorial on [different ways to run VBA macro codes in Excel](https://trumpexcel.com/run-a-macro-excel/)
.

In case you need to use any of these codes quite often, you can also consider adding these to the Personal Macro Workbook and then to the QAT. This way, the code will be available to you in any of your workbooks with a single click.

So these were some VBA codes that you can use to delete entire rows in Excel (in different scenarios). The same logic can also be applied in case you want to delete columns instead of rows (with the corresponding adjustment in the code examples).

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [Excel VBA Autofilter: A Complete Guide with Examples](https://trumpexcel.com/vba-autofilter/)
    
*   [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [Insert a Blank Row after Every Row in Excel (or Every Nth](https://trumpexcel.com/insert-blank-row-after-every-row/)
     [Row)](https://trumpexcel.com/insert-blank-row-after-every-row/)
    
*   [How to Quickly Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Delete Entire Row in Excel Using VBA (Examples)”
---------------------------------------------------------------------

1.  Hello Sumit Bansal, very helpful blog. Can you tweek the ‘Delete Rows with a Specific Word/Value’ VBA code to del rows beyond row 99 ie I want to keep only the first 99 rows of many csv files. thanks
    
    [Reply](https://trumpexcel.com/vba-delete-row-excel/#comment-14513)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-delete-row-excel/#respond)

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