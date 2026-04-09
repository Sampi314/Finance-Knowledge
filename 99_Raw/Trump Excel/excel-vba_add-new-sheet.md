# Create New Sheet Using VBA in Excel (Sheets.Add)

**Source:** https://trumpexcel.com/excel-vba/add-new-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/add-new-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/add-new-sheet/#below-title)

A common Excel task when automating tasks in Excel using VBA is to add new sheets.

In VBA, this can easily be done using the _Sheets.Add_ method.

In this article, I will cover various scenarios where you can use VBA to create a new sheet in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/add-new-sheet/#)

Sheets.Add Method
-----------------

_Sheets.Add_ is a method that adds a new sheet. You can use this to add a regular worksheet, a chart sheet, or a macro sheet.

When a new sheet is added, it automatically becomes the active sheet.

Below is the syntax of the _Sheets.Add_ method:

Sheets.Add (Before, After, Count, Type)

Where:

*   **Before**: Specify the sheet before which you want the new sheet to be added
*   **After**: Specify the sheet after which you want the new sheet to be added
*   **Count**: Specify the number of sheets you want to add
*   **Type**: Specify what type of sheet you want to add (worksheet, chart sheet, or macro sheet). If not specified, it would add a worksheet.

Note that all of these arguments are optional, and if you just use _Sheets.Add_, it would create one new worksheet before the active sheet.

Now that you know about the ‘_Sheets.Add_‘ method, let’s see it in action in some practical examples.

Create One New Sheet
--------------------

Below is the VBA code that will add one new sheet in the current workbook (in which you are running the code)

    Sub CreateNewSheet()
        ' Create a new worksheet
        Sheets.Add
    End Sub

The new worksheet is always added to the left of the active sheet.

In the above code, I have used _Sheets.Add_ method. You can also use _Worksheets.Add_

Create Multiple New Sheet
-------------------------

If you want to insert multiple new sheets, you can use the Sheets.Add method multiple times.

Below is the VBA code that will add three new sheets to the workbook.

    Sub AddMultipleSheets()
    
        ' Create a new worksheet
        Sheets.Add
        
        ' Create the second new worksheet
        Sheets.Add
        
        ' Create the third new worksheet
        Sheets.Add
    
    End Sub

In the above, I have used the _Sheets.Add_ method three times, so this adds three new worksheets.

You can also use a loop to add multiple new sheets, as shown below in the code that adds five new sheets.

    Sub AddMultipleSheets()
    
        ' For loop to add five new sheets
        For i = 1 To 5
            Sheets.Add
        Next i
    
    End Sub

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to add five new sheets. In case you want to run the loop any other number of times, you can change the value in the code.

Also read: [How to Insert New Worksheet in Excel (Shortcuts)](https://trumpexcel.com/insert-new-worksheet-excel/)

Create a Sheet with a Specific Name
-----------------------------------

    Sub CreateSheetWithSpecificName()
    
        ' Declare a variable to hold the new worksheet
        Dim ws As Worksheet
        
        ' Create a new sheet and assing it to the variable
        Set ws = Worksheets.Add
    
        ' Assign the name to the newly created sheet
        ws.Name = "NewName"
    
    End Sub

The above code first adds a new worksheet and assigns it to a variable called _ws_.

It then [renames the sheet](https://trumpexcel.com/excel-vba/rename-sheet/)
 to “NewName”.

Add a New Sheet at the Beginning
--------------------------------

Below is the VBA code that will add a new sheet at the beginning (so that it becomes the first sheet in the workbook)

    Sub AddSheetAtBeginning()
    
        ' Create a new worksheet at the beginning of existing worksheets
        Sheets.Add Before:=Sheets(1)
        
    End Sub
    

In the above code, I have used the Before parameter of the Add method. I have used _Before:=Sheets(1),_ so it adds the new sheet before the first sheet.

You can also tweak the code so that it adds a new sheet at the beginning and also renames it, using the name you specify in the code.

Below is the code that does this:

    Sub AddSheetAtBeginning()
    
        ' Create a new worksheet at the beginning and rename it
        Sheets.Add(Before:=Sheets(1)).Name = "FirstSheet"
    
    End Sub
    

Running the code again will generate another sheet at the start, but Excel will automatically adjust the name (like “FirstSheet (2)”) to avoid any naming conflicts.

Also read: [Clear Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/clear-sheet/)

Add a New Sheet at the End (After the Last Sheet)
-------------------------------------------------

Below is the VBA code that will add a new sheet at the end of all sheets in the workbook.

    Sub AddSheetAtEnd()
    
        ' Create a new worksheet at the end of existing worksheets
        Sheets.Add After:=Sheets(Sheets.Count)
    
    End Sub

The above code uses _Sheets.Count_ to get the count of all the worksheets in the workbook. It then uses this count number to add the sheet after this last worksheet.

You can also use the below (slightly modified) code to add the sheet at the end and give it the specified name.

    Sub AddSheetAtEnd()
    
        ' Create a new worksheet at the end and rename it
        Sheets.Add(After:=Sheets(Sheets.Count)).Name = "LastSheet"
    
    End Sub

If you run the code more than once, Excel will automatically rename subsequent sheets (e.g., “LastSheet (2)”, “LastSheet (3)”, and so on) to prevent any naming conflicts.

Also read: [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)

Create a Sheet With the Name from a Cell
----------------------------------------

Below is the VBA code that creates a worksheets and names it using the value in cell A1 of the active sheet.

    Sub CreateSheetWithNameFromCell()
    
        ' Declare a variable to hold the sheet name
        Dim sheetName As String
    
        ' Get the sheet name from cell A1
        sheetName = ActiveSheet.Range("A1").Value
        
        ' Check if the cell is empty or not
        If sheetName = "" Then
            MsgBox "Cell A1 is empty. Please provide a name for the sheet.", vbExclamation
            Exit Sub
        End If
        
        ' Try to create a new worksheet with the specified name
        On Error Resume Next
        Worksheets.Add(After:=Worksheets(Worksheets.Count)).Name = sheetName
        If Err.Number <> 0 Then
            MsgBox "Error creating sheet. It might be because the name already exists or it's an invalid name.", vbExclamation
        End If
        On Error GoTo 0
    
    End Sub

In the above code, I have used the variable _sheetname_ to store the value in cell A1. This variable is then used to assign the name to the newly added sheet.

I have also placed some checks and balances in place in this code to handle potential errors.

In case the cell is empty or it has a name that can’t be used for a worsheet, the code will show an error and stop.

Also read: [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)

Add Sheet Before Or After a Specific Sheet
------------------------------------------

Below is the VBA code that adds a new sheet named “Summary” before the sheet named “Sales”

    Sub AddSheetBeforeSpecificSheet()
            Worksheets.Add(Before:=Worksheets("Sales")).Name = "Summary"
    End Sub

While this code works, it doesn’t check whether the ‘Sales’ sheet exists or not.

Below is a more robust code that checks for the sheet’s existence first and then adds a new sheet after the Sales sheet.

    Sub AddSheetBeforeSpecificSheet()
    
        ' Declare a variable to hold the target sheet name
        Dim targetSheetName As String
        targetSheetName = "Sales"
        
        ' Check if the target sheet exists
        Dim sheetExists As Boolean
        sheetExists = False
        Dim ws As Worksheet
        
        For Each ws In ThisWorkbook.Worksheets
            If ws.Name = targetSheetName Then
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' If the target sheet exists, add a new sheet before it
        If sheetExists Then
            Worksheets.Add(Before:=Worksheets(targetSheetName)).Name = "Summary"
        Else
            MsgBox targetSheetName & " not found. Please check the sheet name.", vbExclamation
        End If
    
    End Sub

Add Sheets from Values in a List/Range
--------------------------------------

Sometimes, you may want to add new sheets in bulk and assign them names based on the values in a list in the worksheet.

Below, I have some values in the range A1:A10, and I want to insert ten new sheets where the names should be taken from this range.

![Add Sheets from Values in a List Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20488'%3E%3C/svg%3E)

Below is the VBA code that would do this.

    Sub AddSheetsFromList()
    
        ' Declare variables
        Dim rng As Range
        Dim cell As Range
        Dim sheetName As String
        
        ' Set the range containing the list of sheet names
        Set rng = ActiveSheet.Range("A1:A10")
        
        ' Loop through each cell in the range
        For Each cell In rng
            sheetName = Trim(cell.Value)
            
            ' Check if the cell is not empty and a sheet with the same name doesn't exist
            If sheetName <> "" Then
                ' Add the new worksheet with the specified name
                Worksheets.Add(After:=Worksheets(Worksheets.Count)).Name = sheetName
            End If
        Next cell
    
    End Sub

The above code [loops through each cell](https://trumpexcel.com/vba-loops/)
 in the range and then adds a new sheet for each of these names at the end. If you have a blank cell in the specified range, it will be ignored.

Add a Chart Sheet
-----------------

So far, we have been talking about worksheets in Excel. _Sheets.Add_ method, by default, adds a worksheet.

But you can also use it to add a chart sheet (which is a sheet dedicated to holding and displaying a single chart/graph).

Below is the VBA code to add a chart sheet.

    Sub AddChartSheet()
    
        ' This line creates a new chart sheet
        Sheets.Add Type:=xlChart
    
    End Sub

Create a New Sheet and Copy Data from Another Sheet
---------------------------------------------------

The below VBA code will add a new sheet, copy all the cells from a specified sheet (Sheet1), and then paste it into the newly added sheet.

    Sub CreateSheetAndCopyData()
    
        Dim newWs As Worksheet
    
        ' Create a new worksheet and assign to varaible
        Set newWs = ThisWorkbook.Sheets.Add
        
        ' Give the new worksheet a name
        newWs.Name = "NewSheet"
        
        ' Copy data from existing worksheet named "SourceSheet" to the new worksheet
        ThisWorkbook.Sheets("SourceSheet").Cells.Copy Destination:=newWs.Cells(1, 1)
    
    End Sub

When using this code, ensure you have a sheet named “SourceSheet” in the workbook, or replace “SourceSheet” in the code with the name of your source sheet.

Also read: [VBA to Hide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)

Create a New Sheet in Another Workbook
--------------------------------------

You can also add new sheets to other workbooks that are open already. In case you want to create a new sheet in a closed workbook, then you need to first open that closed workbook and then add a new sheet to it.

Let’s see both of these examples.

### VBA Code to Create Sheet in Already Open Workbook

Below is the code that will create a new sheet in an open workbook named Example.xlsx, and give this new worksheet a name (NewSheet)

    Sub CreateSheetInOpenWorkbook()
    
        ' Declare the variables
        Dim targetWbName As String
        Dim newWs As Worksheet
    
        ' Set vairable to hold the name of the open workbook
        targetWbName = "Example.xlsx"
    
        ' Set tragetWb variable to the open workbook object
        Set targetWb = Workbooks(targetWbName)
    
        ' Add new sheet and assign it to the newWs vairable
        Set newWs = targetWb.Sheets.Add
    
        ' Give a Name to the new worksheet
        newWs.Name = "NewSheet"
    
    End Sub

This is the basic code you can use and then modify accordingly. For example, you can put some checks to make sure that the workbook is open and the sheet with the same name does not exists.

### VBA Code to Create Sheet in a Closed Workbook

Below VBA code will open the workbook named Example.xlsx, add a new sheet to it, and then close it.

While this alone may not be useful in practical scenario, you can extend this code and use this to open a closed workbook, add a new sheet, and then copy data from some other sheet to this newly created sheet, and then close it. This would certainly be immensely helpful for some people.

    Sub CreateSheetInClosedWorkbook()
    
        ' Declare the variables
        Dim targetWbPath As String
        Dim targetWb As Workbook
        Dim newWs As Worksheet
    
        ' Set variable to hold the path of the closed workbook
        targetWbPath = "C:\Users\sumit\Downloads\Example.xlsx" 'Replace with the path to your closed workbook
    
        ' Open the target workbook and set targetWb variable to the workbook object
        Set targetWb = Workbooks.Open(targetWbPath)
    
        ' Add new sheet and assign it to the newWs variable
        Set newWs = targetWb.Sheets.Add
    
        ' Give a Name to the new worksheet
        newWs.Name = "NewSheet"
    
        ' Save and close the workbook
        targetWb.Save
        targetWb.Close
    
    End Sub

While this code as is may not be useful in practical scenario, you can extend this code and use this to open a closed workbook, add a new sheet, and then copy data from some other sheet to this newly created sheet, and then close it.

This would certainly be immensely helpful for some people.

Remember to change the workbook name and the file path based on your requirements.

Create a New Sheet from Template
--------------------------------

If you’re trying to create a new sheet in the same workbook using a template sheet (an existing sheet within that workbook acting as the template), you can do this with the code below:

    Sub CreateSheetFromTemplate()
    
        ' Declare the Workbook and Worksheet variables
        Dim Wb As Workbook
        Dim Ws As Worksheet
    
        ' Set the current workbook to Wb
        Set Wb = ThisWorkbook
    
        ' Check if a template sheet named "Template" exists
        On Error Resume Next
        Set Ws = Wb.Worksheets("Template")
        On Error GoTo 0
    
        ' If the template does not exist, exit the subroutine
        If Ws Is Nothing Then
            MsgBox "Template sheet not found!", vbExclamation
            Exit Sub
        End If
    
        ' Copy the template sheet to the end and rename it
        Ws.Copy After:=Wb.Sheets(Wb.Sheets.Count)
        Wb.Worksheets(Wb.Sheets.Count).Name = "NewSheet"
    
    End Sub

This code starts by checking if there’s a worksheet named “Template” in the current workbook.

If it finds one, it creates a copy of that template and places it at the end of all worksheets.

It then renames this new sheet to “NewSheet”. If the template does not exist, a message box pops up notifying the user.

You can change the sheet name in the code accordingly,

Create a New Sheet if It Doesn’t Exist
--------------------------------------

Here’s a VBA code that will ask the user for a sheet name and then [check if that sheet already exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
 in the workbook. If it does not exist, it will add one with the given name, else it will [show you a message box](https://trumpexcel.com/vba-msgbox/)
.

    Sub CreateSheetIfNotExists()
    
        ' Declare the Workbook and Worksheet variables
        Dim Wb As Workbook
        Dim Ws As Worksheet
        Dim SheetName As String
    
        ' Set the current workbook to Wb
        Set Wb = ThisWorkbook
    
        ' Ask the user to input the desired name for the new sheet
        SheetName = InputBox("Enter the desired name for the new sheet:")
    
        ' If the input is empty, exit the subroutine
        If SheetName = "" Then Exit Sub
    
        ' Check if the specified sheet name already exists
        On Error Resume Next
        Set Ws = Wb.Worksheets(SheetName)
        On Error GoTo 0
    
        ' If the sheet doesn't exist, create a new one with the specified name
        If Ws Is Nothing Then
            Wb.Worksheets.Add(After:=Wb.Worksheets(Wb.Worksheets.Count)).Name = SheetName
        Else
            MsgBox "A sheet with the name '" & SheetName & "' already exists!", vbExclamation
        End If
    
    End Sub

Remember that the changes done by VBA can not be reversed. So it’s essential to ensure you don’t accidentally overwrite or duplicate sheets, especially in workbooks with many sheets.

This VBA code helps prevent such mishaps by checking for the existence of a sheet before trying to create one with the same name.

[What is VBA in Excel?](https://trumpexcel.com/excel-vba/)

**Other Excel VBA articles you may also like:**

*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [](https://trumpexcel.com/excel-vba/delete-sheet/)
    [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [Activate Sheet using VBA](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [VBA Protect and Unprotect Sheets](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    

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