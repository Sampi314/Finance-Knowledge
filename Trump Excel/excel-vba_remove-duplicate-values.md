# Remove Duplicate Values in Excel Using VBA

**Source:** https://trumpexcel.com/excel-vba/remove-duplicate-values

---

[Skip to content](https://trumpexcel.com/excel-vba/remove-duplicate-values/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/remove-duplicate-values/#below-title)

Dealing with duplicates is a regular task for people working with data in Excel.

While there is already an in-built [Remove Duplicate functionality in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
, you can also do the same using VBA.

This could be useful if you’re already working with VBA and want to remove duplicates using your code or automate the process.

In this article, I will explain how to remove duplicate values using VBA and then cover some examples of VBA codes you can use in various scenarios.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/remove-duplicate-values/#)

Range.RemoveDuplicates Method in VBA
------------------------------------

Let’s first understand the _Range.RemoveDuplicates_ method, which allows us to remove duplicates in VBA.

Below is the syntax of _Range.RemoveDuplicates_ method:

Range("YourRange").RemoveDuplicates Columns:=Array(1,2), Header:=xlYes

Here:

*   _“YourRange”_ is the range you’re working with
*   _Columns:=Array(1,2)_ specifies which columns to check for duplicates (in this case, columns 1 and 2). This is a mandatory argument, and RemoveDuplicates won’t work if you don’t provide this.
*   _Header:=xlYes_ indicates whether the first row contains headers. This is an optional argument, and if you don’t provide it, Excel will consider that your dataset doesn’t have a header.

The _RemoveDuplicates_ method compares rows within the selected range.

If a row has the same values as another row in the specified columns, Excel will consider it a duplicate and remove it. The first occurrence of a unique combination is kept, while subsequent duplicates are deleted.

VBA to Remove Duplicate Values in Excel
---------------------------------------

Now, let’s look at some examples of how to use VBA to remove duplicate values in Excel in various scenarios.

### Remove Duplicates From One Column

Below, I have a dataset where I have names in column A, and I want to remove any duplicate occurrence of the name and only keep the unique ones.

![Dataset to remove duplicates from one column VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20446'%3E%3C/svg%3E)

Here is the VBA code that would do this:

    Sub RemoveDuplicatesFromColumn()
    
        Sheets("Sheet1").Range("A1:A11").RemoveDuplicates Columns:=1, Header:=xlYes
    
    End Sub

The above VBA code removes duplicate values from the range A1:A11 in the worksheet named “Sheet1”.

The RemoveDuplicates method is used on the range, specifying Columns:=1 to indicate that the operation should consider the first column within the specified range.

The Header:=xlYes argument indicates that the first row in the range (A1) is treated as a header row and not part of the data to be de-duplicated.

In the above example, I specified the range From which I wanted to remove the duplicate values. You can use the VBA code below to do the same from an already selected range of cells.

    Sub RemoveDuplicatesFromColumn()
        Selection.RemoveDuplicates Columns:=1, Header:=xlYes
    End Sub

### Remove Duplicates Based on One Column

Below, I have a data set where I have names in column, their state in column B, and their city in column C, and I want to remove any duplicate instance of the name.

This means that I want to remove any record where the name repeats, irrespective of whether the state and city names are the same or not.

![Remove duplicates based on one column VBA Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20341'%3E%3C/svg%3E)

The VBA code below would do this:

    Sub RemoveDuplicatesFromColumn()
    
        Sheets("Sheet1").Range("A1:C11").RemoveDuplicates Columns:=1, Header:=xlYes
    
    End Sub

The above code considers the entire range A1:C11 but only uses column 1 to check for duplicates.

So when it encounters a repeat instance of a name, that entire record is deleted.

Also read: [Select Ranges using VBA](https://trumpexcel.com/vba-ranges/)

### Remove Duplicates Based on Multiple Columns

Below, I have a data set where I have names in column, their state in column B, and their city in column C, and I want to remove any duplicate instances where the name and the state name are the same.

![Remove duplicates based on multiple columns VBA Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20340'%3E%3C/svg%3E)

The VBA code below would do this:

    Sub RemoveDuplicatesFromColumn()
    
        Sheets("Sheet1").Range("A1:C11").RemoveDuplicates Columns:=Array(1,2), Header:=xlYes
    
    End Sub

The above code considers the entire range A1:C11 and then checks columns 1 and 2 to assess the duplicate records.

When it encounters the same instance of the name and state, it considers that record as duplicate and removes it (irrespective of what the city name is)

### Remove Duplicates Rows

If you want to remove the entire duplicate row, you can do that by specifying all the column numbers in the VBA code.

Below is a data set from which I want to remove all the duplicate rows (where a duplicate row would be where all the values in the row are the same as that of some other row).

![Remove duplicate rows using VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20337'%3E%3C/svg%3E)

The VBA code below would do this:

    Sub RemoveDuplicatesFromColumn()
    
        Sheets("Sheet1").Range("A1:C11").RemoveDuplicates Columns:=Array(1,2,3), Header:=xlYes
    
    End Sub

Since there are three columns in my data set, I have used _Columns:=Array(1,2,3)._ You can adjust this parameter accordingly if your data has more columns.

Also read: [Count Rows Using VBA](https://trumpexcel.com/excel-vba/count-rows/)

### Remove Duplicates Across Multiple Sheets

VBA can be useful when you want to remove duplicates across multiple sheets in one go.

Now, there can be two situations:

*   Your data set is in the same range in all the sheets, and you want to remove duplicates from it.
*   All the sheets have data sets of different sizes, and you need to use VBA first to determine the size and then remove the duplicate records from it.

#### Remove Duplicates From the Same Range Across Multiple Sheets

Let’s say you have a workbook with multiple worksheets, and all these worksheets have data in the same range (say A1:D40)

Below is the VBA code that would remove duplicates from multiple sheets in this scenario:

    Sub RemoveDuplicatesAcrossSheets()
        Dim ws As Worksheet
        Dim targetRange As String
        Dim columnsArray As Variant
    
        ' Specify the range to remove duplicates from
        targetRange = "A1:D40"
    
        ' Specify the columns array to check for duplicates
        columnsArray = Array(1, 2, 3, 4)
    
        ' Loop through each worksheet and remove duplicates
        For Each ws In ThisWorkbook.Worksheets
            ws.Range(targetRange).RemoveDuplicates Columns:=columnsArray, Header:=xlYes
        Next ws
    
    End Sub
    

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each sheet and then uses the _RemoveDuplicates_ method to remove duplicate records from the specified range (which is A1:D40).

This was a pretty straightforward VBA code since we had to remove duplicates from the same range in each worksheet.

However, in most practical scenarios, your range is likely to be of varying length. So, let’s say how to remove duplicates from each sheet where the ranges are of different sizes.

#### Remove Duplicates From Varying Ranges Across Multiple Sheets

Below is the VBA code that would go through each worksheet in the given workbook, determine the range size, and then remove duplicates from it.

    Sub RemoveDuplicatesFromMultipleSheets()
    
        Dim ws As Worksheet
        Dim lastRow As Long
        Dim lastCol As Integer
        Dim i As Integer
        Dim columnsArray() As Integer
    
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Find the last row and column with data
            lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
            lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
    
            ' Check if there's more than one row of data and at least one column
            If lastRow > 1 And lastCol > 0 Then
                ' Redimension the columnsArray based on the number of columns
                ReDim columnsArray(1 To lastCol)
                For i = 1 To lastCol
                    columnsArray(i) = i
                Next i
    
                ' Apply RemoveDuplicates method on the entire used range of each sheet
                ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol)).RemoveDuplicates Columns:=columnsArray, Header:=xlYes
            End If
        Next ws
    
    End Sub

The above VBA code removes duplicate rows from all worksheets in a workbook based on the entire range of used columns.

It [loops through each worksheet](https://trumpexcel.com/vba-loops/)
, then identifies the last row and column containing data, and then checks if there is a valid range (more than one row and at least one column).

The subroutine then dynamically creates an array (_columnsArray_) based on the number of columns and uses this array to specify the columns for the _RemoveDuplicates_ method.

This method is applied to the entire Used range of each worksheet, considering all the columns for duplicate identification.

### Remove Duplicate from Table

    Sub RemoveDuplicatesFromTable()
        Dim tbl As ListObject
        Dim columnsArray As Variant
    
        ' Set the table from which to remove duplicates
        Set tbl = ThisWorkbook.Sheets("Table").ListObjects("MyTable")
    
        ' Specify the columns array to check for duplicates (e.g., Array(1, 2) for the first two columns)
        columnsArray = Array(1, 2) 
    
        ' Remove duplicates from the table
        tbl.Range.RemoveDuplicates Columns:=Array(1, 2), Header:=xlYes
    
    End Sub
    

The above VBA macro removes duplicate rows from a specified table named “_MyTable_” in a worksheet named “_Table_“.

It uses a predefined array (columnsArray) containing column indexes (in this case, columns 1 and 2) to identify duplicates.

The _RemoveDuplicates_ method is applied to the entire range of the table, considering the specified columns for duplicate detection.

The _Header:=xlYes_ parameter indicates that the table has headers, which are excluded from the duplicate check.

VBA Remove Duplicates not Working – Possible Reasons!
-----------------------------------------------------

If you’re encountering issues with the _RemoveDuplicates_ method in VBA for Excel, there could be several reasons why it’s not working as expected.

Here are some potential causes:

**Incorrect Range Selection:**

Ensure that the range you’ve selected for the _RemoveDuplicates_ method is correct. If the range is not properly defined, it may not include all the columns you intend to duplicate.

**Column Indexes:**

When specifying columns in the RemoveDuplicates method, ensure you are using the correct column indexes. Remember, column indexing starts from 1 and not 0.

**Data Types Mismatch:**

Sometimes, data that looks identical may have [different data types](https://trumpexcel.com/vba-data-types-variables-constants/)
 (e.g., text vs. numeric). Ensure that the data types are consistent across each column.

**Hidden Rows or Columns:**

If there are hidden rows or columns, they might be causing unexpected results. Make sure to account for or unhide them before running the duplicate removal.

**Leading or Trailing Spaces:**

Check for leading or trailing spaces in your data. These can cause entries that look identical to be treated as different. You might want to use the Trim function to [remove extra spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
.

**Case Sensitivity:**

The RemoveDuplicates method is not case-sensitive. Therefore, entries with different cases (e.g., “Excel” vs. “excel”) will be considered duplicates.

**Merge Cells:**

If your range includes [merged cells](https://trumpexcel.com/find-merged-cells/)
, it might cause the RemoveDuplicates method to behave unexpectedly. Ensure that cells are not merged in the range you are working with.

**Incorrect Use of Method Parameters:**

Double-check the syntax and parameters of the _RemoveDuplicates_ method. Incorrect parameters can lead to unexpected results.

**Macro Security Settings:**

Sometimes, high macro security settings can prevent VBA scripts from running correctly. Check your macro security settings to ensure they’re not too restrictive.

**Other Excel articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [How to Delete Entire Row in Excel Using VBA](https://trumpexcel.com/vba-delete-row-excel/)
    
*   [VBA Protect / Unprotect Sheet](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)
    
*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    

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