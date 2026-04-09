# Rename Sheet Using VBA in Excel (Examples)

**Source:** https://trumpexcel.com/excel-vba/rename-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/rename-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/rename-sheet/#below-title)

Renaming sheets in Excel is a common task, and with VBA, you can do this at scale with some very simple code.

While it’s easy to rename one or two worksheets, when you automate it with VBA, it can save you a lot of time.

In this article, I will cover some examples where you can use VBA code to rename sheets in Excel.

So, grab your coffee, sit back, and let’s get started! It’s time to become an Excel pro!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/rename-sheet/#)

Rename Active Sheet
-------------------

Below is the VBA code that will rename the active sheet to “Sales Data”

    Sub RenameActiveSheet()
    
    ' Change Active sheet name
    ActiveSheet.Name = "Sales Data"
    
    End Sub

While this works, it’s not very useful as it will take you less effort to rename the worksheet manually.

However, when we extend this concept, we can do some amazing stuff.

For example, below is the VBA code which would rename the active sheet by using the value in cell A1:

    Sub RenameActiveSheet()
    
    ' Change Active sheet name based on cell value
    ActiveSheet.Name = Range("A1").Value
    
    End Sub

_Note: This code will give you an error in case the cell A1 is empty._

While you may still think this isn’t a big-time save, when we extend this concept further, it becomes useful.

Imagine running a code, and all the sheets in the workbook are renamed using the cell value in the sheet. Now, that’s something you can not you can do faster manually.

So, now that the concept of renaming a sheet is clear, let’s look at more practical examples.

Also read: [How to Rename a Sheet in Excel (Shortcuts)](https://trumpexcel.com/rename-sheet-in-excel/)

Rename the First Sheet (using the Index Number)
-----------------------------------------------

Below is the VBA code that would change sheet name of the first sheet to _Sales Data_”

    Sub RenameFirstSheet()
        
        ' Rename the worksheet
       ThisWorkbook.Sheets(1).Name = "Sales Data"
    
    End Sub
    

In the above VBA code, we have used the sheet index number ThisWorkbook.Sheets(1) to refer to the first sheet.

You can change the number in the parenthesis, and it will refer to the worksheet in that position in the workbook.

Rename All Sheets with Cell Value
---------------------------------

    Sub RenameSheetsCellValue()
    
        ' Declare variables
        Dim ws As Worksheet
    
        Dim cellValue As String
        
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Worksheets
        
            ' Read the value from cell A1 of the current worksheet
            cellValue = ws.Range("A1").Value
            
            ' Check if the cell is not empty
            If cellValue <> "" Then
            
                ' Rename the worksheet with the cell value
                ws.Name = cellValue
                
            End If
            
        ' Move to the next worksheet in the loop
        Next ws
        
    ' End the subroutine
    End Sub

The above code loops through all the sheets in the workbook and renames the sheet using the value in cell A1 of each sheet.

It also uses an IF statement to check whether the cell is empty. If the cell is empty, it leaves that worksheet without renaming it.

Also read: [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)

Rename Sheets To File Name
--------------------------

The below VBA code will change the name of the active sheet to the file name:

    Sub RenameSheetToFileName()
        ' Declare a variable to hold the file name
        Dim fileName As String
        
        ' Extract the file name from the workbook's full path
        fileName = Mid(ThisWorkbook.FullName, InStrRev(ThisWorkbook.FullName, "\") + 1)
        
        ' Remove the file extension from the file name
        fileName = Left(fileName, InStrRev(fileName, ".") - 1)
        
        ' Rename the active sheet to the file name
        ActiveSheet.Name = fileName
    End Sub
    

The above code first extracts the file name from the full file path and then assigns it to a variable called fileName. It then renames the active sheet to the value that the fileName variable holds.

Note: For this code to work, you must have saved your file somewhere. If it’s a new workbook that has never been saved, it will give you an error (Run-time error 5)

Rename Sheets Based On a List
-----------------------------

If you want to rename your sheets based on a list of names you already have in a range, you can easily do that with VBA.

Below, I have some names that I want to use to rename the sheets. So, I want the first sheet to be renamed to _Sales_, the second to _Marketing_, and so on.

![Change Sheet Names by List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20696'%3E%3C/svg%3E)

Here is the VBA code to do this:

    Sub RenameSheetsBasedOnList()
        ' Declare a variables
        Dim ws As Worksheet
        Dim i As Integer
        
        ' Initialize the counter variable to 1
        i = 1
        
        ' Loop through each worksheet in the workbook
        For Each ws In Worksheets
    
            ' If cell is not empty, rename the worksheet using cell value
            If Range("A1").Offset(i - 1, 0) <> "" Then
    
                ws.Name = ActiveSheet.Range("A1").Offset(i - 1, 0)
            End If
            
            ' Increment the counter variable
            i = i + 1
        Next ws
    End Sub

The above code uses two variables – counter (i) and a worksheet variable (was).

It loops through each worksheet in the workbook. Inside the loop, it checks whether the cell at an offset from A1 (using the counter) is empty.

If it’s not empty, the code renames the worksheet (ws.Name) based on the value in that cell.

The counter (i) increments by one after each iteration of the loop, allowing you to go through all worksheets and rename them based on the list starting from cell A1 in the active sheet.

Also read: [Protect and Unprotect Sheet Using VBA](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)

Rename Sheet in an Open Workbook
--------------------------------

Below is the VBA code you can use to rename a sheet in an already open workbook.

    Sub RenameSheetInOpenWorkbook()
    
        ' Declare variable
        Dim targetwb As Workbook
    
        ' Set the workbook variable to the already open workbook
        Set targetwb = Workbooks("OpenWorkbook.xlsx")
    
        
        ' Rename the worksheet
        targetwb.Sheets("Sheet1").Name = "Sales Data"
        
    End Sub

In the above code, I have used a variable _targetwb_ and used it to store the open workbook object in which I want to rename the sheet.

Then, I refer to the sheet that I want to rename (which is _Sheet1_ in this case) and change its name.

Also read: [VBA to Hide or Unhide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)

Rename Sheet in a Closed Workbook
---------------------------------

Below is the VBA code that allows you to rename a worksheet in a closed workbook.

Since VBA cannot work with closed workbooks, the code has to first open the workbook, rename the sheet, and then close it back again.

    Sub RenameSheetInClosedWorkbook()
        ' Declare Workbook and Worksheet variables
        Dim targetwb As Workbook
        Dim targetws As Worksheet
        
        ' Open the workbook that is currently closed
        Set targetwb = Workbooks.Open("C:\Users\sumit\Downloads\Example.xlsx")
        
        ' Reference the worksheet to be renamed
        Set targetws = targetwb.Sheets("Sheet1")
        
        ' Rename the worksheet
        targetws.Name = "New Sheet Name"
        
        ' Save and close the workbook
        targetwb.Close SaveChanges:=True
    End Sub
    

Also read: [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)

Rename Sheet If It Exists
-------------------------

Below is the VBA code that first checks whether the sheet exists in the workbook or not, and if it exists, then it will rename it.

    Sub RenameSheetIfExists()
        ' Declare variables
        Dim wb As Workbook
        Dim ws As Worksheet
        Dim sheetExists As Boolean
        
        ' Set reference to the workbook
        Set wb = ThisWorkbook
        
        ' Initialize the flag as False
        sheetExists = False
        
        ' Loop through each worksheet to check if it exists
        For Each ws In wb.Sheets
            If ws.Name = "OldSheet" Then
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' Rename the sheet if it exists
        If sheetExists Then
            wb.Sheets("OldSheet").Name = "NewSheet"
            MsgBox "Sheet has been renamed"
        Else
            MsgBox "Sheet does not exist."
        End If
    End Sub
    

Using the above code, I want to rename a sheet with the name “OldSheet” to “NewSheet”.

To do this, I’ve [used a loop](https://trumpexcel.com/vba-loops/)
 to go through each sheet and check the name of the sheet. If the name of the sheet is “OldSheet”, it gets renamed to “NewSheet”, and a message is shown saying, “_Sheet has been renamed_“

Rename Active Sheet With Today’s Date/Time
------------------------------------------

Below is the VBA code that will rename the active sheet to the current date

    Sub RenameSheetWithTodaysDate()
        ' Declare a variable to hold the formatted date string
        Dim CurrDate As String
        
        ' Get today's date and format it as YYYY-MM-DD
        CurrDate = Format(Date, "dd-mmm-yyyy")
        
        ' Rename the active sheet to the formatted date string
        ActiveSheet.Name = CurrDate
    End Sub

In the above code, I have used the Date function to get the current date and then used the Format function to format the date in the dd-mmm-yyyy format.

This is to ensure the sheet name will be valid, as Excel sheet names cannot contain certain characters like slashes (/).

Finally, the _ActiveSheet.Name_ property is set to this formatted date string, effectively renaming the active sheet to the current date.

_Note that Excel requires unique names for each sheet, so if a sheet with today’s date already exists, running this macro will result in an error._

If you want to rename the active sheet to the current date as well as time, you can use the code below.

    Sub RenameSheetWithTodaysDateTime()
        ' Declare a variable to hold the formatted date string
        Dim CurrDateTime As String
        
        ' Get today's date and format it as YYYY-MM-DD
        CurrDateTime = Format(Now, "dd-mmm-yyyy_HH-MM-SS")
        
        ' Rename the active sheet to the formatted date string
        ActiveSheet.Name = CurrDateTime
    End Sub

**Note**: You can not use a colon (:) in the sheet name, so here I used the format HH-SS-MM to show the time.

Add Prefix to all Sheets
------------------------

Want to add a specific prefix to all the sheets in the workbook? The below code can do it for you.

    Sub AddPrefixToAllSheets()
        ' Declare variables for the worksheet and the prefix string
        Dim ws As Worksheet
        Dim prefix As String
        
        ' Set the prefix string
        prefix = "Sales_"
        
        ' Loop through all worksheets in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Add prefix to the worksheet name
            ws.Name = prefix & ws.Name
        Next ws
    End Sub

The above code uses a simple For Next loop to go through each sheet and add the prefix text (which I have assigned to a variable called _prefix_).

You can use the same logic to append any suffix after the sheet name for all the sheets in the workbook.

Rules for Naming Sheets in Excel
--------------------------------

Below are some rules you need to keep in mind when renaming sheets in Excel:

*   You can’t use a name that exceeds 31 characters.
*   You can not use any of the following characters in the sheet name **: / \\ ? \* \[ or \]**
*   You can not leave the worksheet name blank
*   You can not use the same name for more than one worksheet.
*   A sheet name cannot start with a space character.
*   Sheet names are not case-sensitive. So, _Sheet1_ and _sheet1_ are considered the same by Excel.

[What is Excel VBA?](https://trumpexcel.com/excel-vba/)

**Other Excel VBA articles you may also like:**

*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [](https://trumpexcel.com/excel-vba/delete-sheet/)
    [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [Create New Sheet Using VBA in Excel (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [Activate Sheet using VBA](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    

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