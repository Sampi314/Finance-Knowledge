# VBA Check IF Cell is Empty (using ISEMPTY Function)

**Source:** https://trumpexcel.com/excel-vba/check-if-cell-empty

---

[Skip to content](https://trumpexcel.com/excel-vba/check-if-cell-empty/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/check-if-cell-empty/#below-title)

It’s a useful check to know whether there are any empty cells in a dataset or not.

With VBA, you can easily do this using the ISEMPTY function.

In this article, I will show you some simple VBA codes you can use to check if a cell is empty or not.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/check-if-cell-empty/#)

Check if a Specific Cell is Empty
---------------------------------

There are two ways you can check whether a cell is empty or not:

*   Using the ISEMPTY function
*   Using the equal-to comparison to a blank string

Let’s look at both of these methods

### Using ISMPTY Function

Below is the VBA code that checks whether cell A1 is empty or not.

If it is, it shows a [message box](https://trumpexcel.com/vba-msgbox/)
 saying “Cell is Empty”; else, it shows a message box saying “Cell is not Empty”.

    Sub CheckIfCellIsEmpty()
        Dim targetCell As Range
        Dim ws As Worksheet
        
        'Set the worksheet and target cell
        Set ws = ThisWorkbook.Sheets("Sheet1")
        Set targetCell = ws.Range("A1")
        
        'Using IsEmpty function
        If IsEmpty(targetCell.Value) Then
            MsgBox "Cell is Empty"
        Else
            MsgBox "Cell is not Empty"
        End If
        
    End Sub

The above VBA code uses the _IsEmpty_ function to check whether cell A1 in Sheet1 is empty or not. If it’s empty, it shows a message box as shown below:

![Cell is empty message box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20186'%3E%3C/svg%3E)

**Note**: In the above example code, I have hardcoded “Sheet1” as the worksheet to check. You can change this or use _Activesheet_ if you want to check in the currently active sheet

### Using Comparison Operator

While using the ISEMPTY function is a perfectly fine way to do this, let me also show you another way to check whether a cell is empty or not using VBA.

Below is the VBA code that compares the value in the target cell with an empty string.

If the cell is blank, it shows a message box saying “Cell is Empty”; else, it shows a message box saying “Cell is not Empty”.

    Sub CheckIfCellIsEmpty()
        Dim targetCell As Range
        Dim ws As Worksheet
        
        'Set the worksheet and target cell
        Set ws = ThisWorkbook.Sheets("Sheet1")
        Set targetCell = ws.Range("A1")
    
        'Comparing with an empty string
        If targetCell.Value = "" Then
            MsgBox "Cell is Blank"
        Else
            MsgBox "Cell is not Blank"
        End If
    
    End Sub

Check If Any Cell is Empty in the Specified Range
-------------------------------------------------

If you want to check whether there is any empty cell in the specified range you can use the below VBA code:

    Sub CheckIfEmptyInRange()
        Dim targetRange As Range
        Dim cell As Range
        Dim ws As Worksheet
        Dim isEmptyFound As Boolean
        
        'Set the worksheet and target range
        Set ws = ThisWorkbook.Sheets("Sheet1")
        Set targetRange = ws.Range("A1:D10")
        
        'Initialize isEmptyFound as False
        isEmptyFound = False
        
        'Loop through each cell in the target range
        For Each cell In targetRange
            If isEmpty(cell.Value) Then
                isEmptyFound = True
                Exit For
            End If
        Next cell
        
        ' Display message based on whether an empty cell was found
        If isEmptyFound Then
            MsgBox "Found Empty Cells in the Range"
        Else
            MsgBox "No Empty Cells in the Range"
        End If
    End Sub

In the above code, I have hard-coded the sheet name (Sheet1) and the range (A1:D10). You can change these accordingly based on your requirements.

The above code uses a [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each cell in the specified range and then check whether it is empty or not using the ISEMPTY function.

As soon as it finds an empty cell, it exits the loop and shows the message box as shown below:

![VBA Check IF Cell is Empty found cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20254%20186'%3E%3C/svg%3E)

Also read: [Using VLOOKUP in VBA](https://trumpexcel.com/excel-vba/vlookup/)

Check If Any Cell is Empty in Selection
---------------------------------------

If you want to check for blank cells in the already selected range in your worksheet, you can use the VBA code below.

    Sub CheckIfEmptyinSelection()
        Dim cell As Range
        Dim cellempty As Boolean
    
        'Initialize isEmpty to False
        cellempty = False
    
        'Loop through each cell in the selection range
        For Each cell In Selection
            'Use IsEmpty function to check if the cell is empty
            If isEmpty(cell.Value) Then
                cellempty = True
                Exit For
            End If
        Next cell
    
        'Display a message box based on the isEmpty value
        If cellempty Then
            MsgBox "Empty Cells Found in Selection"
        Else
            MsgBox "All cells are filled"
        End If
    End Sub
    

The above code uses a [For Next loop](https://trumpexcel.com/vba-loops/)
 to go through each cell in the selection and check whether the cell is empty or not using the ISEMPTY function.

Get a Count of Blank Cells in Selection
---------------------------------------

Along with checking for blank cells in the selection, if you also want to know how many cells are blank, then you can use the below VBA code.

    Sub CountBlankCells()
        Dim cell As Range
        Dim selectionRange As Range
        Dim blankCount As Long
    
        ' Initialize blankCount to 0
        blankCount = 0
    
        ' Set the selectionRange to the currently selected cells
        Set selectionRange = Selection
    
        ' Loop through each cell in the selection range
        For Each cell In selectionRange
            ' Use IsEmpty function to check if the cell is empty
            If IsEmpty(cell.Value) Then
                blankCount = blankCount + 1
            End If
        Next cell
    
        ' Display a message box with the count of blank cells
        MsgBox "Number of blank cells: " & blankCount
    End Sub

The above VBA code goes through all the cells in the selection and then shows you a message box that shows the total number of blank cells (as shown below):

![Message box showing the number of empty cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20206%20186'%3E%3C/svg%3E)

These are some of the macro codes that can be used to check if a cell is empty using VBA.

**Other articles you may also like:**

*   [What is VBA in Excel? Learn Excel VBA Programming!](https://trumpexcel.com/excel-vba/)
    
*   [Check IF Sheet Exists in Excel Using VBA](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [How to Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)
    
*   [How to Filter Cells with Bold Font Formatting in Excel](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [Using Active Cell in VBA in Excel](https://trumpexcel.com/active-cell-vba-excel/)
    

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