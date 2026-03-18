# 24 Useful Excel Macro Examples for VBA Beginners (Ready-to-use)

**Source:** https://trumpexcel.com/excel-macro-examples

---

[Skip to content](https://trumpexcel.com/excel-macro-examples/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-macro-examples/#below-title)

Using Excel Macros can speed up work and save you a lot of time.

One way of getting the VBA code is to [record the macro](https://trumpexcel.com/record-macro-vba/)
 and take the code it generates. However, that code by macro recorder is often full of code that is not really needed. Also macro recorder has some limitations.

So it pays to have a collection of useful VBA macro codes that you can have in your back pocket and use it when needed.

While writing an Excel VBA macro code may take some time initially, once it’s done, you can keep it available as a reference and use it whenever you need it next.

In this massive article, I am going to list some useful Excel macro examples that I need often and keep stashed away in my private vault.

I will keep updating this tutorial with more macro examples. If you think something should be on the list, just leave a comment.

You can bookmark this page for future reference.

Now before I get into the Macro Example and give you the VBA code, let me first show you how to use these example codes.

Using the Code from Excel Macro Examples
----------------------------------------

Here are the steps you need to follow to use the code from any of the examples:

*   Open the Workbook in which you want to use the macro.
*   Hold the ALT key and press F11. This opens the [VB Editor](http://Visual Basic Editor (Complete Overview))
    .
*   Right-click on any of the objects in the project explorer.
*   Go to Insert –> Module.
*   Copy and Paste the code in the Module Code Window.

In case the example says that you need to paste the code in the worksheet code window, double click on the worksheet object and copy paste the code in the code window.

Once you have inserted the code in a workbook, you need to save it with a .XLSM or .XLS extension.

How to Run the Macro
--------------------

Once you have copied the code in the VB Editor, here are the steps to run the macro:

*   Go to the Developer tab.
*   Click on Macros.

![VBA Excel Macro Examples - Developer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20133'%3E%3C/svg%3E "VBA Excel Macro Examples - Developer")

*   In the Macro dialog box, select the macro you want to run.
*   Click on Run button.

![VBA Excel Macro Examples - Run the Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20363'%3E%3C/svg%3E "VBA Excel Macro Examples - Run the Macro")

In case you can’t find the developer tab in the ribbon, [read this tutorial](https://trumpexcel.com/excel-developer-tab/)
 to learn how to get it.

_Related Tutorial: [Different ways to run a macro in Excel.](https://trumpexcel.com/run-a-macro-excel/)
_

In case the code is pasted in the worksheet code window, you don’t need to worry about running the code. It will automatically run when the specified action occurs.

Now, let’s get into the useful macro examples that can help you automate work and save time.

_Note: You will find many instances of an apostrophe (‘) followed by a line or two. These are comments that are ignored while running the code and are placed as notes for self/reader._

_In case you find any error in the article or the code, please be awesome and let me know._

![Excel Macro Examples for Beginners Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20500'%3E%3C/svg%3E "Excel Macro Examples for Beginners Blog")

Excel Macro Examples
--------------------

Below macro examples are covered in this article:

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-macro-examples/#)

### Unhide All Worksheets at One Go

If you are working in a workbook that has multiple hidden sheets, you need to unhide these sheets one by one. This could take some time in case there are many hidden sheets.

Here is the code that will unhide all the worksheets in the workbook.

'This code will unhide all sheets in the workbook
Sub UnhideAllWoksheets()
Dim ws As Worksheet
For Each ws In ActiveWorkbook.Worksheets
ws.Visible = xlSheetVisible
Next ws
End Sub

The above code uses a [VBA loop](https://trumpexcel.com/vba-loops/)
 (For Each) to go through each worksheets in the workbook. It then changes the visible property of the worksheet to visible.

Here is a detailed tutorial on how to use various methods to [unhide sheets in Excel](https://trumpexcel.com/unhide-sheets-excel/)
.

### Hide All Worksheets Except the Active Sheet

If you’re working on a report or [dashboard](https://trumpexcel.com/creating-excel-dashboard/)
 and you want to hide all the worksheet except the one that has the report/dashboard, you can use this macro code.

'This macro will hide all the worksheet except the active sheet
Sub HideAllExceptActiveSheet()
Dim ws As Worksheet
For Each ws In ThisWorkbook.Worksheets
If ws.Name <> ActiveSheet.Name Then ws.Visible = xlSheetHidden
Next ws
End Sub

### Sort Worksheets Alphabetically Using VBA

If you have a workbook with many worksheets and you want to sort these alphabetically, this macro code can come in really handy. This could be the case if you have sheet names as years or employee names or product names.

'This code will sort the worksheets alphabetically
Sub SortSheetsTabName()
Application.ScreenUpdating = False
Dim ShCount As Integer, i As Integer, j As Integer
ShCount = Sheets.Count
For i = 1 To ShCount - 1
For j = i + 1 To ShCount
If Sheets(j).Name < Sheets(i).Name Then
Sheets(j).Move before:=Sheets(i)
End If
Next j
Next i
Application.ScreenUpdating = True
End Sub

### Protect All Worksheets At One Go

If you have a lot of worksheets in a workbook and you want to protect all the sheets, you can use this macro code.

It allows you to specify the password within the code. You will need this password to unprotect the worksheet.

'This code will protect all the sheets at one go
Sub ProtectAllSheets()
Dim ws As Worksheet
Dim password As String
password = "Test123" 'replace Test123 with the password you want
For Each ws In Worksheets
   ws.Protect password:=password
Next ws
End Sub

Also read: [Remove Password from VBA Project in Excel](https://trumpexcel.com/excel-vba/remove-password/)

### Unprotect All Worksheets At One Go

If you have some or all of the worksheets protected, you can just use a slight modification of the code used to protect sheets to unprotect it.

'This code will protect all the sheets at one go
Sub ProtectAllSheets()
Dim ws As Worksheet
Dim password As String
password = "Test123" 'replace Test123 with the password you want
For Each ws In Worksheets
ws.Unprotect password:=password
Next ws
End Sub

Note that the password needs to the same that has been used to lock the worksheets. If it’s not, you will see an error.

### Unhide All Rows and Columns

This macro code will unhide all the hidden rows and columns.

This could be really helpful if you get a file from someone else and want to be sure there are no [hidden rows/columns](https://trumpexcel.com/unhide-columns/)
.

'This code will unhide all the rows and columns in the Worksheet
Sub UnhideRowsColumns()
Columns.EntireColumn.Hidden = False
Rows.EntireRow.Hidden = False
End Sub

### Unmerge All Merged Cells

It’s a common practice to merge cells to make it one. While it does the work, when cells are merged you will not be able to sort the data.

In case you are working with a worksheet with merged cells, use the code below to [unmerge all the merged cells](https://trumpexcel.com/unmerge-cells-excel/)
 at one go.

'This code will unmerge all the merged cells
Sub UnmergeAllCells()
ActiveSheet.Cells.UnMerge
End Sub

Note that instead of Merge and Center, I recommend using the [Centre Across Selection](https://trumpexcel.com/how-to-merge-cells-in-excel/)
 option.

### Save Workbook With TimeStamp in Its Name

A lot of time, you may need to create versions of your work. These are quite helpful in long projects where you work with a file over time.

A good practice is to save the file with timestamps.

Using timestamps will allow you to go back to a certain file to see what changes were made or what data was used.

Here is the code that will automatically save the workbook in the specified folder and add a timestamp whenever it’s saved.

'This code will Save the File With a Timestamp in its name
Sub SaveWorkbookWithTimeStamp()
Dim timestamp As String
timestamp = Format(Date, "dd-mm-yyyy") & "\_" & Format(Time, "hh-ss")
ThisWorkbook.SaveAs "C:UsersUsernameDesktopWorkbookName" & timestamp
End Sub

You need to specify the folder location and the file name.

In the above code, “C:UsersUsernameDesktop is the folder location I have used. You need to specify the folder location where you want to save the file. Also, I have used a generic name “WorkbookName” as the filename prefix. You can specify something related to your project or company.

### Save Each Worksheet as a Separate PDF

If you work with data for different years or divisions or products, you may have the need to save different worksheets as PDF files.

While it could be a time-consuming process if done manually, VBA can really speed it up.

Here is a VBA code that will save each worksheet as a separate PDF.

'This code will save each worsheet as a separate PDF
Sub SaveWorkshetAsPDF()
Dim ws As Worksheet
For Each ws In Worksheets
ws.ExportAsFixedFormat xlTypePDF, "C:UsersSumitDesktopTest" & ws.Name & ".pdf"
Next ws
End Sub

In the above code, I have specified the address of the folder location in which I want to save the PDFs. Also, each PDF will get the same name as that of the worksheet. You will have to modify this folder location (unless your name is also Sumit and you’re saving it in a test folder on the desktop).

Note that this code works for worksheets only (and not chart sheets).

### Save Each Worksheet as a Separate PDF

Here is the code that will save your entire workbook as a PDF in the specified folder.

'This code will save the entire workbook as PDF
Sub SaveWorkshetAsPDF()
ThisWorkbook.ExportAsFixedFormat xlTypePDF, "C:UsersSumitDesktopTest" & ThisWorkbook.Name & ".pdf"
End Sub

You will have to change the folder location to use this code.

### Convert All Formulas into Values

Use this code when you have a worksheet that contains a lot of formulas and you want to [convert these formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

'This code will convert all formulas into values
Sub ConvertToValues()
With ActiveSheet.UsedRange
.Value = .Value
End With
End Sub

This code automatically identifies cells are used and convert it into values.

### Protect/Lock Cells with Formulas

You may want to [lock cells with formulas](https://trumpexcel.com/lock-formulas-excel/)
 when you have a lot of calculations and you don’t want to accidentally delete it or change it.

Here is the code that will lock all the cells that have formulas, while all the other cells are not locked.

'This macro code will lock all the cells with formulas
Sub LockCellsWithFormulas()
With ActiveSheet
   .Unprotect
   .Cells.Locked = False
   .Cells.SpecialCells(xlCellTypeFormulas).Locked = True
   .Protect AllowDeletingRows:=True
End With
End Sub

Related Tutorial: [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
.

### Protect All Worksheets in the Workbook

Use the below code to protect all the worksheets in a workbook at one go.

'This code will protect all sheets in the workbook
Sub ProtectAllSheets()
Dim ws As Worksheet
For Each ws In Worksheets
ws.Protect
Next ws
End Sub

This code will go through all the worksheets one by one and protect it.

In case you want to unprotect all the worksheets, use ws.Unprotect instead of ws.Protect in the code.

### Insert A Row After Every Other Row in the Selection

Use this code when you want to insert a blank row after every row in the selected range.

'This code will insert a row after every row in the selection
Sub InsertAlternateRows()
Dim rng As Range
Dim CountRow As Integer
Dim i As Integer
Set rng = Selection
CountRow = rng.EntireRow.Count
For i = 1 To CountRow
ActiveCell.EntireRow.Insert
ActiveCell.Offset(2, 0).Select
Next i
End Sub

Similarly, you can modify this code to insert a blank column after every column in the selected range.

### Automatically Insert Date & Timestamp in the Adjacent Cell

A timestamp is something you use when you want to track activities.

For example, you may want to track activities such as when was a particular expense incurred, what time did the sale [invoice](https://trumpexcel.com/invoice-generator-pdf/)
 was created, when was the data entry done in a cell, when was the report last updated, etc.

Use this code to insert a date and time stamp in the adjacent cell when an entry is made or the existing contents are edited.

'This code will insert a timestamp in the adjacent cell
Private Sub Worksheet\_Change(ByVal Target As Range)
On Error GoTo Handler
If Target.Column = 1 And Target.Value <> "" Then
Application.EnableEvents = False
Target.Offset(0, 1) = Format(Now(), "dd-mm-yyyy hh:mm:ss")
Application.EnableEvents = True
End If
Handler:
End Sub

Note that you need to insert this code in the worksheet code window (and not the in module code window as we have done in other Excel macro examples so far). To do this, in the VB Editor, double click on the sheet name on which you want this functionality. Then copy and paste this code in that sheet’s code window.

Also, this code is made to work when the data entry is done in Column A (note that the code has the line Target.Column = 1). You can change this accordingly.

### Highlight Alternate Rows in the Selection

[Highlighting alternate rows](https://trumpexcel.com/highlight-every-other-row-excel/)
 can increase the readability of your data tremendously. This can be useful when you need to take a print out and go through the data.

Here is a code that will instantly highlight alternate rows in the selection.

'This code would highlight alternate rows in the selection
Sub HighlightAlternateRows()
Dim Myrange As Range
Dim Myrow As Range
Set Myrange = Selection
For Each Myrow In Myrange.Rows
   If Myrow.Row Mod 2 = 1 Then
      Myrow.Interior.Color = vbCyan
   End If
Next Myrow
End Sub

Note that I have specified the color as vbCyan in the code. You can specify other colors as well (such as vbRed, vbGreen, vbBlue).

### Highlight Cells with Misspelled Words

Excel doesn’t have a [spell check](https://trumpexcel.com/using-spell-check-in-excel/)
 as it has in Word or PowerPoint. While you can run the spell check by hitting the F7 key, there is no visual cue when there is a spelling mistake.

Use this code to instantly highlight all the cells that have a spelling mistake in it.

'This code will highlight the cells that have misspelled words
Sub HighlightMisspelledCells()
Dim cl As Range
For Each cl In ActiveSheet.UsedRange
If Not Application.CheckSpelling(word:=cl.Text) Then
cl.Interior.Color = vbRed
End If
Next cl
End Sub

Note that the cells that are highlighted are those that have text that Excel considers as a spelling error. In many cases, it would also highlight names or brand terms that it doesn’t understand.

### Refresh All Pivot Tables in the Workbook

If you have more than one [Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
 in the workbook, you can use this code to refresh all these Pivot tables at once.

'This code will refresh all the Pivot Table in the Workbook
Sub RefreshAllPivotTables()
Dim PT As PivotTable
For Each PT In ActiveSheet.PivotTables
PT.RefreshTable
Next PT
End Sub

You can read more about [refreshing Pivot Tables](https://trumpexcel.com/refresh-pivot-table-excel/)
 here.

### Change the Letter Case of Selected Cells to Upper Case

While Excel has the [formulas](https://trumpexcel.com/excel-functions/)
 to change the letter case of the text, it makes you do that in another set of cells.

Use this code to instantly change the letter case of the text in the selected text.

'This code will change the Selection to Upper Case
Sub ChangeCase()
Dim Rng As Range
For Each Rng In Selection.Cells
If Rng.HasFormula = False Then
Rng.Value = UCase(Rng.Value)
End If
Next Rng
End Sub

Note that in this case, I have used UCase to make the text case Upper. You can use [LCase for lower case](https://trumpexcel.com/vba-lcase/)
.

### Highlight All Cells With Comments

Use the below code to highlight all the cells that have comments in it.

'This code will highlight cells that have comments\`
Sub HighlightCellsWithComments()
ActiveSheet.Cells.SpecialCells(xlCellTypeComments).Interior.Color = vbBlue
End Sub

In this case, I have used vbBlue to give a blue color to the cells. You can change this to other colors if you want.

### Highlight Blank Cells With VBA

While you can [highlight blank cell](https://trumpexcel.com/highlight-blank-cells-in-excel/)
 with conditional formatting or using the Go to Special dialog box, if you have to do it quite often, it’s better to use a macro.

Once created, you can have this macro in the Quick Access Toolbar or save it in your [personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
.

Here is the VBA macro code:

'This code will highlight all the blank cells in the dataset
Sub HighlightBlankCells()
Dim Dataset as Range
Set Dataset = Selection
Dataset.SpecialCells(xlCellTypeBlanks).Interior.Color = vbRed
End Sub

In this code, I have specified the blank cells to be highlighted in the red color. You can choose other colors such as blue, yellow, cyan, etc.

### How to Sort Data by Single Column

You can use the below code to sort data by the specified column.

Sub SortDataHeader()
Range("DataRange").Sort Key1:=Range("A1"), Order1:=xlAscending, Header:=xlYes
End Sub

Note that the I have created a named range with the name ‘DataRange’ and have used it instead of the cell references.

Also there are three key parameters that are used here:

*   Key1 – This is the on which you want to sort the data set. In the above example code, the data will be sorted based on the values in column A.
*   Order- Here you need to specify whether you want to sort the data in ascending or descending order.
*   Header – Here you need to specify whether your data has headers or not.

Read more on how to [sort data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
.

### How to Sort Data by Multiple Columns

Suppose you have a dataset as shown below:

![Dataset to sort data using VBA in Excel - Macro Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20366'%3E%3C/svg%3E "Dataset to sort data using VBA in Excel")

Below is the code that will sort the data based on multiple columns:

Sub SortMultipleColumns()
With ActiveSheet.Sort
 .SortFields.Add Key:=Range("A1"), Order:=xlAscending
 .SortFields.Add Key:=Range("B1"), Order:=xlAscending
 .SetRange Range("A1:C13")
 .Header = xlYes
 .Apply
End With
End Sub

Note that here I have specified to first sort based on column A and then based on column B.

The output would be something as shown below:

![Sort Data Using VBA - Multiple Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20365'%3E%3C/svg%3E "Sort Data Using VBA - Multiple Columns")![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20366'%3E%3C/svg%3E "Sort Data Using VBA - Multiple Columns")

### How to Get Only the Numeric Part from a String in Excel

If you want to [extract only the numeric part or only the text part from a string](https://trumpexcel.com/extract-numbers-from-string-excel/)
, you can create a custom function in VBA.

You can then use this VBA function in the worksheet (just like regular Excel functions) and it will extract only the numeric or text part from the string.

Something as shown below:

![Dataset to get the numeric or the text part in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20594%20158'%3E%3C/svg%3E "Dataset to get the numeric or the text part in Excel")

Below is the VBA code that will create a function to extract numeric part from a string:

'This VBA code will create a function to get the numeric part from a string
Function GetNumeric(CellRef As String)
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If IsNumeric(Mid(CellRef, i, 1)) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetNumeric = Result
End Function

You need place in code in a module, and then you can use the function =GetNumeric in the worksheet.

This function will take only one argument, which is the cell reference of the cell from which you want to get the numeric part.

Similarly, below is the function that will get you only the text part from a string in Excel:

'This VBA code will create a function to get the text part from a string
Function GetText(CellRef As String)
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If Not (IsNumeric(Mid(CellRef, i, 1))) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetText = Result
End Function

So these are some of the useful Excel macro codes that you can use in your day-to-day work to automate tasks and be a lot more productive.

**Other Excel tutorials you may like:**

*   [How to Delete Macros in Excel](https://trumpexcel.com/remove-macros-from-excel/)
    
*   [How to Enable Macros in Excel?](https://trumpexcel.com/enable-macros-in-excel/)
    
*   [How to Describe Excel Skills in a Resume?](https://trumpexcel.com/excel-skills/resume/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

47 thoughts on “24 Useful Excel Macro Examples for VBA Beginners”
-----------------------------------------------------------------

1.  Hello, thank you for your sharing. May I ask for the code if I want to print all attachments/objects (such as Excel file, PDF doc, word doc) embedded within an Excel workbook?
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14340)
    
    *   CALL ME
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14551)
        
2.  How do we enter 2<x<5 in VBA codd
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13765)
    
    *   HI
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14550)
        
3.  There is a problem in this page  
    24 Useful Excel Macro Examples for VBA Beginners (Ready-to-use)
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13488)
    
4.  This is very cool! If I may ask a more specific question: lets say I want to save a variety of worksheets to PDFs however, I only want to convert worksheets that titles that begin with “D\_”. Is this possible?
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13451)
    
5.  hello, what if i have 2 sets of numeric part from a string and i wanted to separate them both
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13292)
    
6.  Hello,  
    I am working on an excel database of vinyl records.  
    Row G shows if the track is an ‘a’ or ‘b’ side.  
    What I want to do, is when ‘a’ is typed into any cell in this Column, the corresponding cell in which shows the track title will turn to light green.  
    If ‘b’ is entered, the cell will remain white.  
    Thank you for your help.
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13210)
    
    *   use conditional formating
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13453)
        
7.  Hi  
    I would like to know how can i saved my code that i have and use it several times again in different workbook, and i have a problem for running the code again in different workbook or if i changed the cell no . the functions have been created by macro are acceptable for another orders fro excel?
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13092)
    
    *   look up personal macro workbook
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14004)
        
8.  At a quick glance the macros look interesting.  
    I can see a use for some of them with modification.
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-13089)
    
9.  Thats really some fantastic codin,  
    Thank you so much for sharing!
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12972)
    
10.  if we protect the worksheets using macro then anyone can see the password from the coding and it will defeat the purpose of protecting. How to stop such situation?
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12963)
    
    *   You can password protect your Macros also.
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14005)
        
11.  i want to a Excel vba programming file for road cross section and Long Section Make In excel And send To autocad . automation vba program.
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12426)
    
12.  Your comment is awaiting moderation.
    
    i want to hyperlink my image with website url plz help me for hyperling my image! and i want to send it to outlook
    
    Sub Send\_email\_fromexcel()  
    Dim edress As String  
    Dim subj As String  
    Dim message As String  
    Dim filename, fname2 As String  
    Dim outlookapp As Object  
    Dim outlookmailitem As Object  
    Dim myAttachments As Object  
    Dim path As String  
    Dim lastrow As Integer  
    Dim attachment As String  
    Dim x As Integer
    
    x = 2
    
    Set outlookapp = CreateObject(“Outlook.Application”)  
    Set outlookmailitem = outlookapp.createitem(0)  
    Set myAttachments = outlookmailitem.Attachments  
    path = “C:UsersUserDesktopstatements”
    
    edress = Sheet1.Cells(x, 1)
    
    subj = Sheet1.Cells(x, 2)  
    filename = Sheet1.Cells(x, 3)  
    fname2 = “Weddingplz-Safe-Gold.jpg”
    
    attachment = path + filename
    
    outlookmailitem.to = edress  
    outlookmailitem.cc = “”  
    outlookmailitem.bcc = “”  
    outlookmailitem.Subject = subj  
    outlookmailitem.Attachments.Add path & fname2, 1
    
    outlookmailitem.htmlBody = “Thank you for your contract” \_  
    & “nicely done this work” \_  
    & “”  
    outlookmailitem.htmlBody = “” & outlookmailitem.htmlBody & “”
    
    ‘outlookmailitem.body = “Please find your statement attached” & vbCrLf & “Best Regards”
    
    outlookmailitem.display  
    ‘outlookmailitem.send
    
    lastrow = lastrow + 1  
    edress = “”  
    x = x + 1
    
    Set outlookapp = Nothing  
    Set outlookmailitem = Nothing
    
    End Sub
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12402)
    
13.  Nice
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12381)
    
14.  Hello good day 🙂 i want to learn how to open the item that is listed in the listbox like for example 3 item in listbox and every item has a corresponding worksheet. after i select the item it opens a new workbook and show the data 🙂
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12294)
    
15.  I tried the macro for protecting only cells with formulas. It worked well for the sheet that was active at the time but could not protect any cell with a formula in the next sheet, even when I tried to run it while opening that next sheet. What can I do to use it in more than one sheet.
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12276)
    
    *   WANT JOB IN ACCOUNTS
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14552)
        
16.  how to separate dollar sign and number on different columns. Thanks
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12237)
    
    *   u can just use “Text to column” in DATA tab..cut the separate column
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12805)
        
17.  Hi,  
    I work for a Finance company, i need an solution where, multiple sets of data values gets pasted to resultant sheets and also calculates the values against them, under conditions.?
    
    Please can you help me out with a suggestion?
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11981)
    
18.  I work in a finance-related field, yet no one understands the value of (or knows how to build) models to do a lot of the work for us rather than inputting everything manually. At the moment, I’m trying to convert a bank reconciliation that takes 5 or 6 separate spreadsheets into a maximum of 3… preferably 1, but that’s ambitious. I came from another company that already had complex models created, but now I’m in the position of knowing how valuable they are without the extensive enough excel knowledge to build them how they should be built (I can do simple models).
    
    I’m not sure if VLOOKUPS or Macros or a combination of both are my best solution. What I do know is that a series of sums and manual entries won’t do the trick.
    
    Anyone able to help??
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11802)
    
    *   Check out the group execl for freelancers on Facebook. Invaluable
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12087)
        
        *   PLZ FIND JOB FOR ME
            
            [Reply](https://trumpexcel.com/excel-macro-examples/#comment-14553)
            
19.  I would like to take copy of cells in an invoice, eg. customer name, address, amount due etc. These are in a contiguous state on invoice and I want to transfer VBA to sheet 2 to make a data base.
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11652)
    
20.  How can I run macro by changing cell value….  
    Cell value is trigger for macro ??
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11531)
    
21.  Hi, I need a macro code to copy the an adjustant cell reference of the trace present of a particular cell.
    
    Eg. I have 3 sheet , I two sheet there are identical text and adjusted numeric value in another column. But in 3rd sheet the text name is little different so I can’t use vlookup here . So I want to for copy the text from 1st sheet cell and search that in 2nd sheet and go to its trace precedants and copy that cell and past at 1 sheet
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11280)
    
22.  Thank you
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-11242)
    
23.  Private Sub CommandButton1\_Click()
    
    If Txtl = “” Or Txtb = “” Or Txtc = “” Or Txtr = “” Or Txtlpa = “” Or Txtd = “” Or Txtp = “” Or Txta = “” Or Txte = “” Or Txtw = “” Or Txtq = “” Or Txtdl = “” Or Txtehm = “” Or Txtco = “” Or Txtbo = “” Or Txtcurr = “” Or Txtwritten = “” Then
    
    MsgBox “PLEASE FILL ALL THE DETAILS”
    
    Txtl = “”  
    Txtb = “”  
    Txtc = “”  
    Txtr = “”  
    Txtlpa = “”  
    Txtd = “”  
    Txtp = “”  
    Txta = “”  
    Txte = “”  
    Txtw = “”  
    Txtq = “”  
    Txtdl = “”  
    Txtehm = “”  
    Txtco = “”  
    Txtbo = “”  
    Txtcurr = “”  
    Txtwritten = “”
    
    Cancle = True
    
    Exit Sub
    
    End If
    
    If Range(“A2”).Value = “” Then
    
    Sheets(“output”).Select  
    Range(“A2”).Value = Txtl  
    Range(“B2”).Value = Txtb  
    Range(“C2”).Value = Txtc  
    Range(“D2”).Value = Format(Txtr, “mm/dd/yyyy”)  
    Range(“E2”).Value = Txtlpa  
    If IsNumeric(Txtd) Then  
    Range(“F2”).Value = Format(Txtd, “mm/dd/yyyy”)  
    Else  
    Range(“F2”).Value = Txtd  
    End If  
    If IsNumeric(Txtp) Then  
    Range(“G2”).Value = Format(Txtp, “mm/dd/yyyy”)  
    Else  
    Range(“G2”).Value = Txtp  
    End If  
    If IsNumeric(Txta) Then  
    Range(“H2”).Value = Format(Txta, “mm/dd/yyyy”)  
    Else  
    Range(“H2”).Value = Txta  
    End If  
    If IsNumeric(Txte) Then  
    Range(“I2”).Value = Format(Txte, “mm/dd/yyyy”)  
    Else  
    Range(“I2”).Value = Txte  
    End If  
    If IsNumeric(Txtw) Then  
    Range(“J2”).Value = Format(Txtw, “mm/dd/yyyy”)  
    Else  
    Range(“J2”).Value = Txtw  
    End If  
    If IsNumeric(Txtq) Then  
    Range(“K2”).Value = Format(Txtq, “mm/dd/yyyy”)  
    Else  
    Range(“K2”).Value = Txtq  
    End If  
    If IsNumeric(Txtdl) Then  
    Range(“L2”).Value = Format(Txtdl, “mm/dd/yyyy”)  
    Else  
    Range(“L2”).Value = Txtdl  
    End If  
    If IsNumeric(Txtehm) Then  
    Range(“M2”).Value = Format(Txtehm, “mm/dd/yyyy”)  
    Else  
    Range(“M2”).Value = Txtehm  
    End If  
    Range(“N2”).Value = Txtco  
    Range(“P2”).Value = Txtbo  
    Range(“O2”).Value = Txtcurr  
    Range(“Q2”).Value = Txtwritten
    
    Else:
    
    lr = Sheets(“output”).Range(“A” & Rows.Count).End(xlUp).Row
    
    Range(“A” & lr).Offset(1, 0).Value = Txtl  
    Range(“B” & lr).Offset(1, 0).Value = Txtb  
    Range(“C” & lr).Offset(1, 0).Value = Txtc  
    Range(“D” & lr).Offset(1, 0).Value = Format(Txtr, “mm/dd/yyyy”)  
    Range(“E” & lr).Offset(1, 0).Value = Txtlpa  
    If IsNumeric(Txtd) Then  
    Range(“F” & lr).Offset(1, 0).Value = Format(Txtd, “mm/dd/yyyy”)  
    Else  
    Range(“F” & lr).Offset(1, 0).Value = Txtd  
    End If  
    If IsNumeric(Txtp) Then  
    Range(“G” & lr).Offset(1, 0).Value = Format(Txtp, “mm/dd/yyyy”)  
    Else  
    Range(“G” & lr).Offset(1, 0).Value = Txtp  
    End If  
    If IsNumeric(Txta) Then  
    Range(“H” & lr).Offset(1, 0).Value = Format(Txta, “mm/dd/yyyy”)  
    Else  
    Range(“H” & lr).Offset(1, 0).Value = Txta  
    End If  
    If IsNumeric(Txte) Then  
    Range(“I” & lr).Offset(1, 0).Value = Format(Txte, “mm/dd/yyyy”)  
    Else  
    Range(“I” & lr).Offset(1, 0).Value = Txte  
    End If  
    If IsNumeric(Txtw) Then  
    Range(“J” & lr).Offset(1, 0).Value = Format(Txtw, “mm/dd/yyyy”)  
    Else  
    Range(“J” & lr).Offset(1, 0).Value = Txtw  
    End If  
    If IsNumeric(Txtq) Then  
    Range(“K” & lr).Offset(1, 0).Value = Format(Txtq, “mm/dd/yyyy”)  
    Else  
    Range(“K” & lr).Offset(1, 0).Value = Txtq  
    End If  
    If IsNumeric(Txtdl) Then  
    Range(“L” & lr).Offset(1, 0).Value = Format(Txtdl, “mm/dd/yyyy”)  
    Else  
    Range(“L” & lr).Offset(1, 0).Value = Txtdl  
    End If  
    If IsNumeric(Txtehm) Then  
    Range(“M” & lr).Offset(1, 0).Value = Format(Txtehm, “mm/dd/yyyy”)  
    Else  
    Range(“M” & lr).Offset(1, 0).Value = Txtehm  
    End If  
    Range(“N” & lr).Offset(1, 0).Value = Txtco  
    Range(“O” & lr).Offset(1, 0).Value = Txtbo  
    Range(“P” & lr).Offset(1, 0).Value = Txtcurr  
    Range(“Q” & lr).Offset(1, 0).Value = Txtwritten
    
    End If
    
    Txtl = “”  
    Txtb = “”  
    Txtc = “”  
    Txtr = “”  
    Txtlpa = “”  
    Txtd = “”  
    Txtp = “”  
    Txta = “”  
    Txte = “”  
    Txtw = “”  
    Txtq = “”  
    Txtdl = “”  
    Txtehm = “”  
    Txtco = “”  
    Txtbo = “”  
    Txtcurr = “”  
    Txtwritten = “”
    
    End Sub
    
    Private Sub Txtb\_BeforeUpdate(ByVal Cancel As MSForms.ReturnBoolean)  
    If IsNumeric(Txtn) > 50 Then  
    MsgBox “pls fill text only”  
    Txtn = “”  
    Cancel = True  
    End If
    
    End Sub
    
    Private Sub Txtb\_Change()
    
    End Sub
    
    Private Sub Txtl\_BeforeUpdate(ByVal Cancel As MSForms.ReturnBoolean)  
    If Len(Txtl) > 8 Then  
    Txtl = “”  
    MsgBox “please 8 chr numric only ”  
    Cancel = True  
    End If
    
    If Not IsNumeric(Txtl) Then  
    Txtl = “”  
    MsgBox “please numeric values”  
    Cancel = True  
    End If  
    End Sub
    
    Private Sub Txtl\_Change()
    
    End Sub
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-10970)
    
24.  COOL!
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-10915)
    
25.  Very useful
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-10861)
    
26.  Tooo useful..for bignner thanks a lot…
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-10508)
    
    *   Oh shush. Read some stuff and get over it
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-12088)
        
27.  Hi Bro,
    
    How can i take to address in outlook way VBA.
    
    Regards,  
    Moorthy P
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-10077)
    
28.  Hi guys,
    
    I need some help with my excel database.  
    I’ve made a Form which holds two groups of two radiobuttons.  
    The form works nice except for the outcome of these radiobuttons.  
    I want them to say “Afslag” and “Opbod+Afslag” instead of TRUE and FALSE.
    
    How can I make it happen?
    
    Like to hear from you guys, tnx a lot.
    
    Roel
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9433)
    
    *   Figured it out 😉
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9434)
        
29.  pls i want a code that will automatically protect cell when values are entered in
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9427)
    
30.  Just a few thoughts on the saving a copy of the workbook with a timestamp in the name.
    
    I do this (manually) all the time and it’s saved me a lot of trouble having those backups. I use the format “yyyymmdd\_hhmm” though because that way I can sort Alphabetically in File Explorer. I might add your function to my library so that I can hot-key it, because there have been times when I’ve been too absorbed in development to remember to save the timestamped copies resulting in the loss of hours of work! Thanks for the tip.
    
    If users do prefer, I guess, a more intuitive date format then rather than “dd-mm-yyyy”, a more general coding suited to folk in the US etc would be format(Date,”short date”) which will automatically use the local format (mm-dd-yyyy for our US friends).
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9389)
    
31.  Thanks for sharing!
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9386)
    
32.  refresh all pivots?  
    I use Ctrl+Alt+F5 to Refresh All (maybe there’s a good reason why not but I don’t have one)
    
    great idea to have all these potentially useful snippets in one place
    
    useful macros in my Personal.xlsb army include:  
    • Toggle centre across cells (merging really is the devil’s spawn)  
    • Clear user-defined styles (I’ve had spreadsheets bloated with over 3000)  
    • Unprotect worksheets (for when you don’t have the password)  
    • Toggle the status bar (to give that one extra line of display)  
    • Cycle case between UPPER, lower, Sentence and Title Case – the latter with selected exceptions (a, the, it, AA, RAC, pH etc)
    
    [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9383)
    
    *   Thanks for sharing Jim.. I will try and add some of these to this list of useful macro examples.
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9384)
        
    *   may i have your workbook as i want unprotect one worksheet pls
        
        [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9394)
        
        *   Hi Carl, copy and paste the following:
            
            Sub Pwd()  
            On Error Resume Next  
            For i = 65 To 66: For j = 65 To 66: For k = 65 To 66: For l = 65 To 66: For m = 65 To 66: For n = 65 To 66: For o = 65 To 66: For p = 65 To 66: For q = 65 To 66: For r = 65 To 66: For S = 65 To 66: For t = 32 To 126  
            ActiveSheet.Unprotect Chr(i) & Chr(j) & Chr(k) & Chr(l) & Chr(m) & Chr(n) & Chr(o) & Chr(p) & Chr(q) & Chr(r) & Chr(S) & Chr(t)  
            If ActiveSheet.ProtectContents = False Then  
            MsgBox “Worksheet unlocked, relock with: ” & Chr(i) & Chr(j) & Chr(k) & Chr(l) & ” ” & Chr(m) & Chr(n) & Chr(o) & Chr(p) & ” ” & Chr(q) & Chr(r) & Chr(S) & Chr(t)  
            Exit Sub  
            End If  
            Next: Next: Next: Next: Next: Next: Next: Next: Next: Next: Next: Next  
            End Sub
            
            enjoy
            
            NB the password found is not THE password, just one that will work and, if used to re-lock will still allow the original password to work  
            This only works for worksheets, not workbooks – though you may find the same password has been used
            
            jim
            
            [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9396)
            
            *   thz for help
                
                [Reply](https://trumpexcel.com/excel-macro-examples/#comment-9405)
                

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-macro-examples/#respond)

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