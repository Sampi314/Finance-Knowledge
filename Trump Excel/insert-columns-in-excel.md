# 5 Ways to Insert New Columns in Excel (including Shortcut & VBA)

**Source:** https://trumpexcel.com/insert-columns-in-excel

---

[Skip to content](https://trumpexcel.com/insert-columns-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-columns-in-excel/#below-title)

Adding or removing columns in Excel in a common task when you’re working with data in Excel.

And just like every other thing in Excel, there are multiple ways to insert columns as well. You can insert one or more single columns (to the right/left of a selected one), multiple columns (adjacent or non-adjacent), or a column after every other column in a dataset.

Each of these situations would need a different method to insert a column.

Note: All the methods shown in this tutorial will also work in case you want to insert new rows

This Tutorial Covers:

[Toggle](https://trumpexcel.com/insert-columns-in-excel/#)

Insert New Columns in Excel
---------------------------

In this tutorial, I will cover the following methods/scenarios to insert new columns in Excel:

1.  Insert one new column (using keyboard shortcut or options in the ribbon)
2.  Add multiple new columns
3.  Add non-adjacent columns at one go
4.  Insert new columns after every other column
5.  Insert a New Column in an Excel Table

### Insert a New Column (Keyboard Shortcut)

Suppose you have a dataset as shown below and you want to add a new column to the left of column B.

Below is the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 to insert a column in Excel:

**Control** **Shift** **\+** (hold the Control and Shift keys and press the plus key)

_Command + I if you’re using Mac_

Below are the steps to use this keyboard shortcut to add a column to the left of the selected column:

1.  Select a cell in the column to the left of which you want to add a new column
2.  Use the keyboard shortcut **Control Shift +**
3.  In the Insert dialog box that opens, click the Entire Column option (or hit the C key)![Check the Entire Column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20262%20231'%3E%3C/svg%3E)
4.  Click OK (or hit the Enter key).

The above steps would instantly add a new column to the left of the selected column.

Another way to add a new column is to first select an entire column and then use the above steps. When you select an entire column, using the **Control Shift +** shortcut will not show the insert dialog box.

It will just add the new column right away.

Below is the keyboard shortcut to [select the entire column](https://trumpexcel.com/select-entire-column-excel/)
 (once you select a cell in the column):

**Control + Spacebar** (hold the Control key and press the space bar key)

Once you have the column selected, you can use **Control Shift +** to add a new column.

If you’re not a fan of [keyboard shortcuts](https://www.youtube.com/watch?v=TWYXcNm1I-Q)
, you can also use the right-click method to insert a new column. Simply right-click on any cell in a column, right-click and then click on Insert. This will open the Insert dialog box where you can select ‘Entire Column’.

![Right-click and then click on Insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20442'%3E%3C/svg%3E)

This would insert a column to the left of the column where you selected the cell.

### Add Multiple New Columns (Adjacent)

In case you need to insert multiple adjacent columns, you can either insert one column and time and just [repeat the same process (you can use the F4 key to repeat the last action), or you can insert all these columns at one go](https://trumpexcel.com/repeat-last-action-excel/)
.

Suppose you have a dataset as shown below and you want to add two columns to the left of column B.

Below are the steps to do this:

1.  Select two columns (starting with the one on the left of which you want to insert the columns)
2.  Right-click anywhere in the selection
3.  Click on Insert

![To insert multiple columns right click and then click on Insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20473'%3E%3C/svg%3E)

The above steps would instantly insert two columns to the left of Column B.

In case you want to insert any other number of columns (say 3 or 4 or  5 columns), you select that many to begin with.

### Add Multiple New Columns (Non-Adjacent)

The above example is quick and fast when you want to add new adjacent columns (i.e., a block of 3 adjacent columns as shown above).

But what if you want to insert columns but these are non-adjacent.

For example, suppose you have a dataset as shown below, and you want to insert one column before Column B and one before Column D.

![Dataset to insert mulitple columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20435'%3E%3C/svg%3E)

While you can choose to do this one by one, there is a better way.

Below are the steps to add multiple non-adjacent columns in Excel:

1.  Select the columns where you want to insert a new column.
2.  Right-click anywhere in the selection
3.  Click on Insert.

![Select non contiguous columns and then click on Insert columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20475'%3E%3C/svg%3E)

The above steps would instantly insert a column to the left of the selected columns.

![Inserted two columns at one go](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20765%20435'%3E%3C/svg%3E)

### Insert New Columns After Every Other Column (Using VBA)

Sometimes, you may want to add a new column after every other column in your existing dataset.

While you can do this manually, if you’re working with a large dataset, this can take some time.

The faster way of doing this would be to use a simple VBA code to simply insert a column after every column in your dataset.

Sub InsertColumn()
'Code created by Sumit Bansal from trumpexcel.com

Dim ColCount As Integer
Dim i As Integer

StartCol = Selection.Columns.Count + Selection.Columns(1).Column
EndCol = Selection.Columns(1).Column

For i = StartCol To EndCol Step -1
    Cells(1, i).EntireColumn.Insert
Next i

End Sub

The above code will go through each column in the selection and insert a column to the right of the selected columns.

You can add this code to a regular module and then [run this macro from there](https://trumpexcel.com/run-a-macro-excel/)
.

Or, if you have to use this functionality regularly, you can also consider adding it to Personal Macro Workbook and then adding it to the Quick Access Toolbar. This way, you will always have access to this code and can run it with a single click.

Note: The above code also works when you have the data formatted as an [Excel table](https://trumpexcel.com/excel-table/)
.

### Add a Column in an Excel Table

When you convert a dataset into an Excel Table, you lose some of the flexibility that you have with regular data when it comes to inserting columns.

For example, you can not select non-contiguous columns and insert columns next to it at one go. You will have to do this one by one.

Suppose you have an Excel Table as shown below.

To insert a column to the left of column B, select any cell in the column, right-click, go to the Insert option and click on ‘Table Columns to the left’.

![Insert column in Excel table - Table column to the left](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20438'%3E%3C/svg%3E)

This will insert a column to the left of the selected cell.

In case you select a cell in Column B and one in Column D, you will notice that the ‘Table Columns to the left’ option is grayed out. In this case, you will have to insert columns one by one only.

What’s surprising is that this works when you select non-contiguous rows, but not with columns.

So these are some of the methods you can use to insert new columns in Excel. All the methods covered in this tutorial will also work if you want to insert new rows (the VBA code would need some modification though).

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [How to Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [How to Move Rows and Columns in Excel](https://trumpexcel.com/move-rows-columns/)
    
*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [How to Freeze Multiple Columns in Excel?](https://trumpexcel.com/freeze-multiple-columns-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-columns-in-excel/#respond)

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