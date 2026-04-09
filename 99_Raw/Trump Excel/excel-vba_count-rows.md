# Count Rows Using VBA in Excel - Easy Examples

**Source:** https://trumpexcel.com/excel-vba/count-rows

---

[Skip to content](https://trumpexcel.com/excel-vba/count-rows/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/count-rows/#below-title)

It’s common to count the number of rows using VBA, which can then be used for other actions in the code.

For example, if I want to loop through all the rows in the used range, it would be helpful if I could first count the total number of rows.

In this article, I will show you some examples of how you can count rows using VBA in Excel in various situations.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/count-rows/#)

VBA Count Rows in the Selection
-------------------------------

Let’s start with a simple example.

Suppose you have already selected a range in the worksheet, and you want to know how many rows there are in the selection using VBA.

Below is the VBA code to do this:

    Sub CountRowsInSelection()
    
        rowCount = Selection.Rows.Count
    
        MsgBox "Number of rows in the selection: " & rowCount
    
    End Sub

The above code uses the _Rows.Count_ method to count the total number of rows in the selection. This value is then assigned to a variable _rowCount_.

It then shows a [message box](https://trumpexcel.com/vba-msgbox/)
 that tells us the total number of rows.

In VBA, _Rows.Count_ is a property that returns the total number of rows in a worksheet or a range. When used with a range (say _Range(“A1:D12”).Rows.Count_ returns the number of rows in the specified range. In this example, it would return 12.

VBA Count Rows in Used Range
----------------------------

Another common situation where you may want to count the number of rows in the worksheet is in the Used Range.

While the worksheet has a lot of rows, a Used Range only refers to the range that is being used in the worksheet.

Below is the VBA code that would count the total number of rows in the used range and show you the number in a message box.

    Sub CountUsedRows()
    
        Dim CountUsedRows As Integer
        Dim ws As Worksheet
        Set ws = ActiveSheet
        
        CountUsedRows = ws.UsedRange.Rows.Count
        MsgBox "Rows in Used Range: " & CountUsedRows
    End Sub

Note: A Used Range only refers to the cells being used and may not always start from the 1st or the 1st column in the worksheet. For example, if I have my data set in A5:B10 (while the rest of the cells have not been used), then my used range would only have six rows (from 5 to 10)

VBA Count Non-Empty Rows
------------------------

If you want to count the total number of non-empty rows in a worksheet, you can use the below VBA code.

    Sub CountNonEmptyRows()
        Dim ws As Worksheet
        Dim lastRow As Long
        Dim count As Long
        Dim i As Long
        
        ' Set the worksheet you want to count rows in
        Set ws = ThisWorkbook.Sheets("Sheet1") ' Change "Sheet1" to your sheet name
        
        ' Find the last row with data in column A
        lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
        
        ' Initialize count
        count = 0
        
        ' Loop through rows and count non-empty ones
        For i = 1 To lastRow
            If WorksheetFunction.CountA(ws.Rows(i)) > 0 Then
                count = count + 1
            End If
        Next i
        
        ' Display the result
        MsgBox "Number of non-empty rows: " & count
    End Sub

The above code first identifies the last filled row in the worksheet by using _ws.Cells(ws.Rows.Count, “A”).End(xlUp).Row_ and assigns that value to a variable _lastrow_

It then loops through all the rows between the first row and the _lastrow_ value, and uses _[CountA](https://trumpexcel.com/excel-functions/counta-function/)_ function to get the count of non-empty rows.

VBA Count Visible Rows Only (After Filter)
------------------------------------------

If you have applied a filter on a data set or you have some rows that are hidden, and you want to count the total number of visible rows only, then you can use the below VBA code:

    Sub CountVisibleRows()
        Dim rng As Range
        Dim visibleRowCount As Long
        Dim row As Range
        
        ' Set the range you want to count (change as needed)
        Set rng = ActiveSheet.UsedRange
        
        visibleRowCount = 0
        
        ' Loop through each row in the range
        For Each row In rng.Rows
            ' Check if the row is visible (not hidden)
            If Not row.Hidden Then
                visibleRowCount = visibleRowCount + 1
            End If
        Next row
        
        ' Display the result
        MsgBox "Number of visible rows: " & visibleRowCount
    End Sub
    

The above code loops through all the rows in the used range and checks whether the rows are hidden or not using the _row.Hidden_ property.

It only counts in those rows where the row.HIdden property is False, indicating that the row is visible.

Once done, it shows a message box that tells us the total number of visible rows in the used range.

Also read: [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)

VBA Count Rows in Excel Table
-----------------------------

Below is the VBA code that would give you the total number of rows in a table named “Table1”.

    Sub CountRowsInTable1()
        Dim rowCount As Long
        
        ' Attempt to count the rows in Table1
        On Error Resume Next
        rowCount = ActiveSheet.ListObjects("Table1").DataBodyRange.Rows.count
        If Err.Number <> 0 Then
            MsgBox "Error: Table 'Table1' not found.", vbExclamation
            Exit Sub
        End If
        On Error GoTo 0
        
        ' Display the result
        MsgBox "Table1 has " & rowCount & " rows.", vbInformation
    End Sub

Note that, unlike regular range in a worksheet, when you’re working with tables in VBA, you need to use _ListObjects(“Table1”)_ to refer to the table. This is because the table is considered a separate object that needs to be referred to in a different way in VBA.

Also read: [How to Count Colored Cells in Excel?](https://trumpexcel.com/count-colored-cells-in-excel/)

VBA Count Rows With a Specific Value
------------------------------------

If you want to count the total number of rows if any cell in that row contains a specific value, then you can use the below VB code:

    Sub CountRowsWithValueInRange()
        Dim ws As Worksheet
        Dim countValue As Variant
        Dim countRange As Range
        Dim row As Range
        Dim rowCount As Long
        
        ' Set the active worksheet
        Set ws = ActiveSheet
        
        ' Set the range to search (A1:D20)
        Set countRange = ws.Range("A1:D20")
        
        ' Prompt user for the value to count
        countValue = InputBox("Enter the value to count:", "Count Rows")
        
        ' Initialize row count
        rowCount = 0
        
        ' Loop through each row in the range and count rows with matching values
        For Each row In countRange.Rows
            If WorksheetFunction.CountIf(row, countValue) > 0 Then
                rowCount = rowCount + 1
            End If
        Next row
        
        ' Display the result
        MsgBox "Result: " & rowCount, vbInformation, "Count Result"
    End Sub

The above code first shows you a message box that asks you for the term that you want to search for in the specified range (which I have hard-coded as A1:D20 – you can change it as needed).

When you enter the search value in the message box, it goes through each row in the specified range and uses the county function to check if that specified term appears in the row or not.

Once the [For Next loop](https://trumpexcel.com/vba-loops/)
 is completed and it is done by going through all the rows, it shows you the result in a message box.

In this article, I showed you multiple scenarios where you can use simple VBA codes to count the total number of rows in a worksheet in Excel.

I hope you found this article helpful.

If you have any questions or suggestions for me, do let me know in the comments section.

**Other VBA articles you may also like:**

*   [What is VBA in Excel? Learn Excel VBA Programming!](https://trumpexcel.com/excel-vba/)
    
*   [Count Sheets in Excel (using VBA)](https://trumpexcel.com/count-sheets-excel/)
    
*   [Using VLOOKUP in VBA](https://trumpexcel.com/excel-vba/vlookup/)
    
*   [VBA Remove Duplicate Values in Excel](https://trumpexcel.com/excel-vba/remove-duplicate-values/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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