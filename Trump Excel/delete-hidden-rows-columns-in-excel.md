# How to Delete All Hidden Rows and Columns in Excel

**Source:** https://trumpexcel.com/delete-hidden-rows-columns-in-excel

---

[Skip to content](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#below-title)

A lot of Excel users hide rows and columns when they have some data that they don’t need visible.

It’s a way to only keep useful data visible, and at the same time not have to delete the data you don’t need to be visible.

And, if you have lots of such hidden rows/columns, it could be a pain to find and delete these hidden rows and columns (in the case when you don’t need them).

In this tutorial, I’ll show you a couple of ways to easily **delete hidden rows and columns in Excel**.

There is an inbuilt method that allows you to delete all the hidden rows and columns in one go, and you can also use VBA macro codes in case you want to apply this to our selected range of cells.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#)

Delete All Hidden Rows and Columns in Excel
-------------------------------------------

If you want to delete all the hidden rows and columns in an entire workbook in Excel, you can use the method shown here.

Remember that it is going to remove these hidden rows and columns from the entire workbook and not from the active sheet only.

Below are the steps to delete all the hidden rows and columns from the workbook in Excel:

1.  Click the File option![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20349%20199'%3E%3C/svg%3E)
2.  In the options on the left, click on ‘Info’![Click on Info](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20501'%3E%3C/svg%3E)
3.  Click on the ‘Check for Issues’ option![Click on the Check for Issues option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20773%20610'%3E%3C/svg%3E)
4.  Click on the ‘Inspect Document’ option. This will open the Document Inspector dialog box![Click on Inspect Document](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20383'%3E%3C/svg%3E)
5.  In the ‘Document Inspector’ dialog box, click on the ‘Inspect’ button. This will inspect the entire workbook and give you the information about the workbook![Click on the Inspect button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20619'%3E%3C/svg%3E)
6.  Scroll down to the ‘Hidden Rows and Columns’ option. You will see that it shows the total number of hidden rows and columns that it has found in the workbook.![Hidden rows and columns numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20619'%3E%3C/svg%3E)
7.  Click on the ‘Remove All’ button![Click on Remove all to delete the hidden rows and columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20619'%3E%3C/svg%3E)

The above steps would delete all the hidden rows and columns in the workbook.

![Green tick when there are no hidden rows and columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20619'%3E%3C/svg%3E)

Note that you need to save this workbook before running the Document Inspector option. In case the workbook is not saved already, Excel would first force you to save it. Also, it will show you a warning prompt asking to save the file once, as the data changed by these steps can not be recovered.

![Warning Prompt when deleting using inspect option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20131'%3E%3C/svg%3E)

In case there are no hidden rows and columns, you would see a green tick before the Hidden and Rows and Columns option (in the Document Inspector dialog box).

Apart from hidden rows and columns, the Document Inspector dialog box also gives you a lot of other useful information – such as the number of comments, or hidden worksheets, or embedded documents, etc.

Note: You cannot undo the changes made by the Document Inspector. So make sure you have a backup copy of the original data (in case if you may need it in the future)

This is a great method if you want to delete all the hidden columns and rows for the entire workbook.

But in case you only want to delete it in a specific sheet or in a specific range, then you cannot use this option.

In that case, you can use the VBA method covered next.

Also read: [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)

Delete Hidden Rows and Columns using VBA
----------------------------------------

If you only have a few hidden rows and columns, it’s possible to unhide these manually and then delete it.

But if this is something you need to do quite often, or if you have a large data set with a large number of rows/columns that are hidden, it’s best to use VBA macro codes to automate this process.

Let’s look at different scenarios where you can use VBA to delete these hidden rows and columns.

### From an Entire Worksheet (Used Range)

While I can make the VBA code check the entire worksheet starting from the last row number and the last column number in the worksheet, that would be a wastage of resources.

A better method would be to see what’s the used range and then only check that used range for any hidden rows and columns.

Below is the VBA code that would delete all the hidden rows in the used range:

Sub DeleteHiddenRows()
Dim sht As Worksheet
Dim LastRow
Set sht = ActiveSheet
LastRow = sht.UsedRange.Rows(sht.UsedRange.Rows.Count).Row

For i = LastRow To 1 Step -1
If Rows(i).Hidden = True Then Rows(i).EntireRow.Delete
Next

End Sub

The above VBA code first finds out the last row number in the used range and assigns that row number to the variable ‘LastRow’.

This last row number is then used in a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
, where it starts from the last row and checks whether it’s hidden or not.

In case it’s hidden, that entire row is deleted. And in case it’s not hidden, the code leaves that row as is and moves to the row above it. This loop checks for all the rows, and deletes any hidden row that it encounters in the process.

In case you want to delete all the hidden columns in the used range, use the VBA code below:

Sub DeleteHiddenColumns()
Dim sht As Worksheet
Dim LastCol as Integer
Set sht = ActiveSheet
LastCol = sht.UsedRange.Columns(sht.UsedRange.Columns.Count).Column

For i = LastCol To 1 Step -1
If Columns(i).Hidden = True Then Columns(i).EntireColumn.Delete
Next

End Sub

This again works the same way, where instead of rows, we are checking for columns.

So it finds out the last column number in the used range, assigns it to a variable, and then [uses the loop](https://trumpexcel.com/vba-loops/)
 to go from the last column to the first column and delete all the hidden columns in the process.

And in case you want to have a code that would delete all the hidden rows, as well as the hidden columns, use the VBA code below:

Sub DeleteHiddenRowsColumns()
Dim sht As Worksheet
Dim LastRow as Integer
Dim LastCol as Integer
Set sht = ActiveSheet
LastRow = sht.UsedRange.Rows(sht.UsedRange.Rows.Count).Row
LastCol = sht.UsedRange.Columns(sht.UsedRange.Columns.Count).Column

For i = LastRow To 1 Step -1
If Rows(i).Hidden = True Then Rows(i).EntireRow.Delete
Next

For i = LastCol To 1 Step -1
If Columns(i).Hidden = True Then Columns(i).EntireColumn.Delete
Next

End Sub

This is just the combined code for both rows and columns and works the same way.

Instead of one loop, this uses two separate loops, where it first goes through all the rows, and then it goes through all the columns. And in the process, it deletes all the hidden rows and columns that it encounters.

Note that you need to place this VBA code in a regular module in the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
. You can then [run the code](https://trumpexcel.com/run-a-macro-excel/)
 directly from the VB Editor, by using the macro dialog box, or by adding this macro to the quick access toolbar.

If this is something that you need to do quite often, you can also add this code to the [personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
 so that you would have access to it from all the workbooks on your system.

### From a Specific Range of Cells

In case you have a specific range from which you want to remove hidden rows and columns, you need to specify that within the code.

This makes sure that the code only circles through the rows and columns in that specified range and leaves the other areas in the worksheet untouched

Below the VBA code that would do this:

Sub DeleteHiddenRowsColumns()
Dim sht As Worksheet
Dim Rng As Range
Dim LastRow As Integer
Dim RowCount As Integer
Set sht = ActiveSheet
Set Rng = Range("A1:K200")
RowCount = Rng.Rows.Count
LastRow = Rng.Rows(Rng.Rows.Count).Row
ColCount = Rng.Columns.Count
LastCol = Rng.Columns(Rng.Columns.Count).Column

For i = LastRow To LastRow - RowCount Step -1
If Rows(i).Hidden = True Then Rows(i).EntireRow.Delete
Next

For j = LastCol To LastCol - ColCount Step -1
If Columns(j).Hidden = True Then Columns(j).EntireColumn.Delete
Next


End Sub

In the above code, I have specified the range as A1:K200.

This makes the code go through all the rows and columns in the specified range and remove any hidden rows and columns that it encounters.

In case you have hidden rows or columns outside of this range, those would remain unaffected.

So this is how you can delete **hidden rows and columns in Excel**.

If you want to do it across the entire workbook, you can use the Document Inspector option. And in case you need more control, you can use the VBA codes as shown above.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [Delete Blank Columns in Excel](https://trumpexcel.com/delete-blank-columns-excel/)
    
*   [Delete Single or Multiple Rows in Excel](https://trumpexcel.com/delete-rows/)
    
*   [How to Quickly Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [How to Hide a Worksheet in Excel (that can not be unhidden)](https://trumpexcel.com/hide-worksheet/)
    
*   [Hide Zero Values in Excel | Make Cells Blank If the Value is 0](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [How to Hide Formulas in Excel (and Only Display the Value)](https://trumpexcel.com/hide-formulas-excel/)
    
*   [How to Select Entire Column (or Row) in Excel](https://trumpexcel.com/select-entire-column-excel/)
    
*   [How to Group Columns in Excel?](https://trumpexcel.com/group-columns-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Delete All Hidden Rows and Columns in Excel”
------------------------------------------------------------------

1.  Very helpful!
    
    [Reply](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#comment-42659)
    
2.  That is very useful. Thank you.
    
    [Reply](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#comment-14685)
    
3.  I’m interested in your teachings, you are the best, be blessed.
    
    [Reply](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#comment-14676)
    
4.  Thanks a lot  
    Will you please send me the sample file.  
    Best regards,  
    Tehrani
    
    [Reply](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#comment-14674)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/#respond)

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