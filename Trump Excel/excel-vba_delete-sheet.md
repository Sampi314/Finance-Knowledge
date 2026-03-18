# Delete Sheet in Excel Using VBA

**Source:** https://trumpexcel.com/excel-vba/delete-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/delete-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/delete-sheet/#below-title)

Managing worksheets is a common task for Excel users, and VBA can simplify this process.

In this article, I will show you different ways you can use VBA codes to delete sheets in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/delete-sheet/#)

Delete a Specific Sheet by Name
-------------------------------

    Sub DeleteSheetByName()
    
        ' Deletes the workheet with the name Sheet1
        ThisWorkbook.Worksheets("Sheet1").Delete
    
    End Sub

In the above code, we have used the line ThisWorkbook.Worksheets(“Sheet1”).Delete where:

*   _ThisWorkbook_ – refers to the workbook in which the code is run.
*   _Worksheets(“Sheet1”)_ – refers to the worksheet you want to delete (Sheet1 in this case)
*   _.Delete_ – The delete method of the worksheet object is used to delete the sheet

When you run the above code, Excel will show you a warning before deleting the sheet (as shown below).

![Excel prompt before deleting the sheet permanently](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20221'%3E%3C/svg%3E)

If you click on the delete button, the sheet will be deleted. If you click the Cancel button, the sheet will not be deleted.

There should always be at least one sheet in the workbook. If you try to delete the last sheet in the workbook, it will give you a Run time error (1004)

### Sheet vs. Worksheet (Important Note)

In VBA, the terms “Sheet” and “Worksheet” are often used interchangeably, but they are not the same.

*   **Worksheet:** A worksheet refers to what we commonly understand as an Excel sheet with rows and columns where we can manipulate data. When we say “Worksheet” in VBA, we are exclusively talking about these types of sheets. The “Worksheet” object in VBA belongs to the Worksheets collection.
*   **Sheet:** A “Sheet” can refer to any type of sheet in an Excel workbook, which includes Worksheets, Chart Sheets, and other types of specialty sheets (like Excel 4.0 Macro sheets). The “Sheet” object in VBA belongs to the Sheets collection and is more generic.

In most cases, it’s alright to use the terms Sheet and Worksheet interchangeably, as most Excel users only work with worksheets. But it’s important to know the difference.

Also read: [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)

Delete Sheet by Index Number
----------------------------

Apart from using the worksheet name, you can also delete a sheet using VBA by specifying its index number. The index number refers to the position of the sheet in the workbook.

For example, ThisWorkbook.Worksheets(1) refers to the first worksheet in the workbook where the code is run. ThisWorkbook.Worksheets(2) refers to the second workbook and so on.

Below is the VBA code that would delete the first worksheet in the workbook:

    Sub DeleteSheetByName()
    
        ' Deletes the first worksheet in the worksbook
        ThisWorkbook.Worksheets(1).Delete
    
    End Sub

Delete Sheet without Prompt / Warning
-------------------------------------

If you use any of the above VBA codes, it is going to show you a warning prompt before deleting the sheet.

This is because deleting a sheet is a big task, and Excel doesn’t want VBA to delete a sheet without giving you a chance to review it first.

In case you don’t want to see that prompt when trying to delete a sheet using the VBA code, you can use the code below:

    Sub DeleteSheetWithoutPrompt()
    
        ' Set the display alerts to False, so no prompts are shown
        Application.DisplayAlerts = False
        
        ' Deletes the workheet with the name Sheet1
        ThisWorkbook.Worksheets("Sheet1").Delete
        
        ' Set the display alerts back to to True
        Application.DisplayAlerts = True
    
    End Sub

In the above code, I used the line Application.DisplayAlerts = False before deleting the sheet.

This ensures that I don’t see any prompt or warning while the sheet is being deleted. Once the sheet deletion is done, I set the Application.DisplayAlerts value back to True (which is the default setting).

_Remember that the change is done by a VBA code or irreversible. So, if you delete a sheet, you can’t undo it later. So, make sure to have a backup before running this code._

Delete All Sheets Except the Active Sheet
-----------------------------------------

    Sub DeleteAllSheetsExceptActive()
        Dim ws As Worksheet
        Dim activeWsName As String
        
        ' Store the name of the active sheet in variable
        activeWsName = ActiveSheet.Name
        
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Sheets
    
            ' Check if worksheet name is different that active worksheet name
            If ws.Name <> activeWsName Then
    
                ' Delete the worksheet without displaying a confirmation message
                Application.DisplayAlerts = False
                ws.Delete
                Application.DisplayAlerts = True
    
            End If
        Next ws
    End Sub
    

In the above code, we first save the name of the active worksheet in a variable _activeWsName_.

It then loops through all the worksheets in the workbook and checks the name of each worksheet. If the name of the worksheet is not the same as that stored in the variable, it is deleted.

Also read: [Rename Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

Delete Sheets If Names Contains Specific Text
---------------------------------------------

When managing workbooks that contain a lot of worksheets, you may sometimes want to delete all the sheets that contain a specific text or string in its name.

Below is the VBA code that would delete all the worksheets that have the term “Sales” in its name:

    Sub DeleteSheetsContainingText()
        Dim ws As Worksheet
        Dim wsName As String
        
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Sheets
    
            ' Check if the worksheet name contains the word "sales"
            If InStr(1, ws.Name, "sales", vbTextCompare) > 0 Then
            
                ' Delete the worksheet without displaying a confirmation message
                Application.DisplayAlerts = False
                ws.Delete
                Application.DisplayAlerts = True
                
            End If
        Next ws
    End Sub

The above code goes through each worksheet in the workbook and checks whether it contains the text “Sales” or not. This is done using the [VBA INSTR function](https://trumpexcel.com/excel-vba-instr/)
.

If the name contains the word “Sales”, that worksheet is deleted.

Remember that Excel would not allow you to delete all the worksheets in a workbook. So if all the sheets contain the text ‘sales’, you will see an error before the last one is deleted.

Also read: [VBA to Hide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)

Delete Sheets Based on Cell Value
---------------------------------

    Sub DeleteSheetIfCellContains()
        Dim ws As Worksheet
        
        ' Loop through each worksheet in the workbook
        For Each ws In Worksheets
    
            ' Check if the value in cell A1 in the sheet is Sales
            If ws.Range("A1").Value = "Sales" Then
            
                ' Delete the worksheet without displaying a confirmation message
                Application.DisplayAlerts = False
                ws.Delete
                Application.DisplayAlerts = True
                
            End If
        Next ws
    End Sub

In the above code, we look through all the worksheets and check the value in cell A1 for each sheet. If the value in cell A1 is “Sales”, that sheet is deleted, else nothing happens.

Delete Every Other Sheet (Delete Alternate Sheets)
--------------------------------------------------

    Sub DeleteAlternateSheets()
        Dim i As Integer
        
        ' Loop through worksheets in reverse order using step 2 for alternates
        For i = ThisWorkbook.Sheets.Count To 1 Step -2
            ' Delete the worksheet without displaying a confirmation message
            Application.DisplayAlerts = False
            ThisWorkbook.Sheets(i).Delete
            Application.DisplayAlerts = True
        Next i
    End Sub
    

The above VBA code loops through all the worksheets in the workbook in reverse order, stepping by 2 to select alternate sheets.

Each selected sheet is then deleted without displaying a confirmation message.

Delete the Sheet if it Exists
-----------------------------

    Sub DeleteSheetIfExists()
        Dim ws As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        
        ' Set sheetName variable to the sheet name
         sheetName = "Sheet1"
    
        ' Initialize variable to false
        sheetExists = False
        
        ' Loop through each worksheet to check if the sheet exists
        For Each ws In ThisWorkbook.Sheets
            If ws.Name = sheetName Then
                
                Application.DisplayAlerts = False
                ThisWorkbook.Sheets(sheetName).Delete
                Application.DisplayAlerts = True
    
                Exit For
            End If
        Next ws
    
    End Sub
    

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to check whether the sheet with the given name exists or not.

As soon as it finds the sheet that has the name, it gets deleted.

Note: In case the workbook does not contain the sheet with the specified name, the above code goes through the loop and ends without any prompt. If you want, you can use a message box to show a prompt in case the sheet is not found

Delete Sheet After or Before a Specific Sheet
---------------------------------------------

    Sub DeleteSheetAfterSales()
        Dim i As Integer
        Dim sheetIndex As Integer
        Dim sheetExists As Boolean
        
        ' Initialize variable to false
        sheetExists = False
        
        ' Loop through worksheets to find the index of the sheet named "Sales"
        For i = 1 To ThisWorkbook.Sheets.Count
            If ThisWorkbook.Sheets(i).Name = "Sales" Then
                sheetExists = True
                sheetIndex = i
                Exit For
            End If
        Next i
        
        ' If "Sales" sheet exists and is not the last sheet, delete the sheet after it
        If sheetExists And sheetIndex < ThisWorkbook.Sheets.Count Then
            Application.DisplayAlerts = False
            ThisWorkbook.Sheets(sheetIndex + 1).Delete
            Application.DisplayAlerts = True
            MsgBox "Deleted Sheet with name: " & Sheets(i).Name
        End If
    End Sub

The above VBA subroutine looks for a sheet named “Sales” in the workbook.

If it finds the sheet and if it’s not the last sheet in the workbook, the subroutine deletes the sheet immediately following “Sales” without any confirmation. It also shows a message box showing the name of the sheet it deleted.

So if you don’t see the message box, you can assume that it either didn’t find the sheet or the Sales sheet was the last sheet, so it could not have deleted the sheet after that.

You can modify the code to delete a sheet before a specific sheet.

Delete All Hidden Sheets
------------------------

    Sub DeleteAllHiddenSheets()
        Dim ws As Worksheet
        
        ' Loop through each worksheet in the workbook using a backward loop
        For Each ws In Worksheets
            
            ' Check if the worksheet is hidden
            If ws.Visible <> xlSheetVisible Then
                ' Delete the worksheet without displaying a confirmation message
                Application.DisplayAlerts = False
                ws.Delete
                Application.DisplayAlerts = True
            End If
        Next ws
    End Sub

The above code [loops through all the worksheets](https://trumpexcel.com/vba-loops/)
 in the workbook and checks the visible property of the sheet.

If the visible property value is not equal to _xlSheetVisible_, it means that the sheet is hidden and is deleted.

Also read: [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)

Delete All Chart Sheets
-----------------------

As I mentioned earlier in this article, a workbook can contain worksheets as well as other sheet objects such as a Chart sheet or a Macro 4 worksheet.

Below is the VBA code that would delete all the chart sheets in your workbook (without doing anything to the worksheets).

    Sub DeleteAllChartSheets()
        Dim i As Integer
        
        ' Loop through each sheet in the workbook using a backward loop
        For i = ThisWorkbook.Sheets.Count To 1 Step -1
            ' Check if the sheet is a chart sheet
            If TypeName(ThisWorkbook.Sheets(i)) = "Chart" Then
                ' Delete the chart sheet without displaying a confirmation message
                Application.DisplayAlerts = False
                ThisWorkbook.Sheets(i).Delete
                Application.DisplayAlerts = True
            End If
        Next i
    End Sub
    

This code loops through all chart sheets in the workbook in reverse order. We do this to avoid issues with changing indices as sheets are deleted.

The code checks the type of the sheet using the TYPENAME function. If the sheet type is Chart, it is deleted.

**Other articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Count Sheets](https://trumpexcel.com/count-sheets-excel/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [How to Activate Sheet using VBA](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [How to Insert New Worksheet in Excel (Easy Shortcuts)](https://trumpexcel.com/insert-new-worksheet-excel/)
    
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