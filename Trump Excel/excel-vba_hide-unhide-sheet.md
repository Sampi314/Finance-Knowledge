# Hide or Unhide Sheets Using VBA

**Source:** https://trumpexcel.com/excel-vba/hide-unhide-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/hide-unhide-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/hide-unhide-sheet/#below-title)

When working with large workbooks with many worksheets, it’s common to hide some worksheets to make the workbook more manageable.

With VBA, you can easily hide or unhide worksheets in bulk. This can also be useful when you want to quickly hide or unhide specific worksheets without having to find and locate them from a long list.

In this article, I will show you some simple VBA codes to hide or unhide sheets in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/hide-unhide-sheet/#)

Sheet.Visible Property in VBA
-----------------------------

VBA has the _Sheet.Visible_ property (or _Worksheet.Visible_ property) that determines whether it would be visible or hidden for the user in the workbook.

Below is the line of code that would hide the sheet named ‘Example’ in the workbook in which the code is run:

Worksheets("Example").Visible = False

And here is the code that would unhide it (in case it is hidden):

Worksheets("Example").Visible = True

In this example, I have used Worksheets(“Example”), but you can use any sheet name, the active sheet, or even the Sheet object stored in a variable.

You can also use _xlSheetHidden_ instead of _True_ and _xlSheetVisible_ instead of _False_. For example, the following code would also hide the sheet named Example _Worksheets(“Example”).Visible = xlSheetHidden_.

Note: You need to have at least one sheet visible in the workbook. If you try to hide the last visible sheet, VBA will give you the Runtime 1004 error.

VBA Codes to Hide Sheets
------------------------

Below, I have some [examples of VBA codes](https://trumpexcel.com/excel-macro-examples/)
 for hiding sheets in different situations.

### Hide the Active Sheet

The below code will hide the active sheet:

    Sub HideActiveSheet()
    
        ' Hide the currently active sheet
        ActiveSheet.Visible = False
    
    End Sub

Remember that you always need to have one visible sheet in the workbook. So, if the active sheet is the only sheet in the workbook, this code will throw an error.

Also read: [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)

### Hide All Sheets Except the Active Sheet

Below is the code that will hide all the sheets except the active sheet.

    Sub HideSheetsExceptActive()
        
    Dim ws As Worksheet
    
        For Each ws In ThisWorkbook.Worksheets
            If ws.Name <> ActiveSheet.Name Then
                ws.Visible = False
            End If
        Next ws
    
    End Sub

The above code uses a [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each sheet, and then it checks the name of the sheet.

If the name of the sheet is not the same as that of the active sheet, it gets hidden.

### Hide Sheets by Name

If you want to hide sheets by their names, you can do that using a VBA code as shown below:

    Sub HideSheetByName()
    
        Sheets("Sheet1").Visible = False
        Sheets("Sheet2").Visible = False
        Sheets("Sheet3").Visible = False
    
    End Sub

In the above code, I specified the sheet name in double quotes and then used the _Visible_ property of the sheet to set it to _False_ to hide it.

In this case, I have hidden three sheets, and you can modify the code to hide more/less number of sheets.

### Hide Sheets with a Specific Word in the Name

Below is the VBA code that hides only those sheets that have the word ‘Sales’ in the name:

    Sub HideSheetswithSpecificWord()
    
        Dim ws As Worksheet
    
        For Each ws In ThisWorkbook.Worksheets
            If InStr(1, ws.Name, "Sales", vbTextCompare) > 0 Then
                ws.Visible = False
            End If
        Next ws
    
    End Sub

The above VBA macro [loops through each worksheet](https://trumpexcel.com/vba-loops/)
 in the workbook and checks whether the name contains the word Sales or not. This is done using the [VBA INSTR function](https://trumpexcel.com/excel-vba-instr/)
.

If the word _Sales_ appears anywhere in the name of the sheet, that sheet would be hidden.

### Hide Sheets Based on Cell Value

Below, the VBA code hides any sheet that has the text “Hide” in cell A1 of the sheet.

    Sub HideSheetsBasedOnCellValue()
    
        Dim ws As Worksheet
        
        ' Loop through each worksheet and hide if cell A1 has "Hide" in it
        For Each ws In ThisWorkbook.Worksheets
    
            If ws.Range("A1").Value = "Hide" Then
                ws.Visible = False
            End If
        Next ws
    
    End Sub

The above code loops through each worksheet in the workbook and then checks the value in cell A1 of each sheet.

If the text in cell A1 is “Hide”, then it will hide that sheet by setting the _visible_ property of the sheet to _False_.

### Hide Sheets Based on Tab Color

When I’m working with a large workbook, I often give color to my worksheet tabs to [group similar sheets](https://trumpexcel.com/group-worksheets-in-excel/)
 and to make them more manageable.

This is also easier for me when I’m presenting my work on calls, as I can direct them to a specific tab by mentioning the tab color.

Below is the VBA code you can use to hide all the sheets that have a [specific tab color](https://trumpexcel.com/change-color-of-sheet-tab-excel/)
 (where you need to specify the tab color):

    Sub HideSheetsBasedOnTabColor()
    
        Dim ws As Worksheet
        Dim colorCriteria As Long
    
        ' Specify the RGB color to match. Example: RGB(255, 0, 0) for red
        colorCriteria = RGB(255, 0, 0)
    
        ' Loop through each worksheet, check color and hide
        For Each ws In ThisWorkbook.Worksheets
            If ws.Tab.Color = colorCriteria Then
                ws.Visible = False
            End If
        Next ws
    
    End Sub

In the above code, I have specified the color criteria as _RGB(255, 0, 0)_, which refers to the red color.

The above code then loops through each worksheet in the workbook and checks the tab color. If the existing color of the worksheet matches the criteria in our code, then that sheet gets hidden.

If you want to hide all the sheets except the one that has a specific color, you can use a code similar to what I have below here:

    Sub HideSheetsBasedOnTabColor()
    
        Dim ws As Worksheet
        Dim colorCriteria As Long
    
        ' Specify the RGB color to match. Example: RGB(255, 0, 0) for red
        colorCriteria = RGB(255, 0, 0)
    
        ' Loop through each worksheet, check color and hide
        For Each ws In ThisWorkbook.Worksheets
            If ws.Tab.Color <> colorCriteria Then
                ws.Visible = False
            Else
                ws.Visible = True
            End If
        Next ws
    
    End Sub

The above code goes through each worksheet in the workbook and checks the tab color.

It then uses an [If Then Else statement](https://trumpexcel.com/if-then-else-vba/)
 to check the tab color. If the tab color is not red (RGB(255, 0, 0)), then the _Visible_ property is set to False (thus hiding it); else, it is set to True (making the sheet visible).

Also read: [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)

### Make the Sheet Very Hidden (Cannot Be Unhidden by User)

VBA in Excel also allows you to [make a sheet Very Hidden](https://trumpexcel.com/hide-worksheet/)
 so that it cannot be unhidden by a user using the regular Excel interface.

This means that when you right-click on the sheet tab and then click on Unhide, you will not see the sheet name, and hence, you won’t be able to unhide it.

Below is the VB code that makes the sheet named _Data_ very hidden:

    Sub MakeSheetVeryHidden()
    
        ThisWorkbook.Sheets("Data").Visible = xlSheetVeryHidden
    
    End Sub

The above code sets the _Visible_ property of the sheet to _xlSheetVeryHidden_.

This is different than all the other codes where we have been setting the visible property to _False_ or _xlSheetHidden_.

When you make the sheet ‘very hidden’, you will have to use a VBA code or an option in the [VB editor](https://trumpexcel.com/visual-basic-editor/)
 interface to unhide it (covered later in this article).

Also read: [VBA Protect / Unprotect Sheet](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)

### Check If the Worksheet is Hidden

Before using VBA code to make changes to a worksheet, it might be useful to first check whether the worksheet is hidden or not.

Below is the VBA code that checks the visible property of the worksheet and shows a message box with a numeric value (corresponding to the sheet’s visible property):

    Sub CheckIfWorksheetHidden()
    
        MsgBox Worksheets("Data").Visible
    
    End Sub

This would show a message box with one of three values:

*   **\-1**: The worksheet is visible.
*   **0**: The worksheet is hidden but can be unhidden via the Excel interface.
*   **2**: The worksheet is very hidden and cannot be unhidden via the Excel interface (only through VBA).

You can modify the code above to give you more meaningful text instead of numbers or use it as part of a larger code where the output of this line could then be used to decide what to do.

Also read: [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

VBA Codes to Unhide Sheets
--------------------------

And here are some example codes for unhiding sheets in different situations.

### Unhide Sheets By Names

If you already know the name of the sheet that you want to unhide, you can use a code as shown below:

    Sub UnhideSheetByName()
    
        Sheets("Data").Visible = True
        Sheets("Summary").Visible = True
        Sheets("Table").Visible = True
    
    End Sub

In the above code, I used the sheet name and set the _Visible_ property of that sheet to True to make it visible.

You can also use the code below, where instead of _True_, I use _xlSheetVisible_

    Sub UnhideSheetByName()
    
        Sheets("Data").Visible = xlSheetVisible
        Sheets("Summary").Visible = xlSheetVisible
        Sheets("Table").Visible = xlSheetVisible
    
    End Sub

### Unhide All Hidden Sheets

The below VBA code goes through all the sheets in the workbook and makes them visible:

    Sub UnhideAllSheets()
    
        Dim ws As Worksheet
    
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Unhide the sheet
            ws.Visible = True
        Next ws
    
    End Sub

### Unhide Sheets With Specific Words in the Name

Below, the VBA code would unhide all the sheets that have the word ‘Data’ in their name.

    Sub UnhideSheetsContainingSpecificWord()
    
        Dim ws As Worksheet
        Dim wordCriteria As String
    
        ' Specify the word to look for in the sheet names
        wordCriteria = "Data"
    
        For Each ws In ThisWorkbook.Worksheets
            If InStr(1, ws.Name, wordCriteria, vbTextCompare) > 0 Then
                ws.Visible = xlSheetVisible
            End If
        Next ws
    
    End Sub

In the above code, I have used a variable _wordCriteria_ to store the word that I am checking for in each sheet’s name.

It then goes through each worksheet and then uses the INSTR function to check whether the sheet name contains the word stored in the _wordCriteria_ variable or not.

If it finds the name, it makes the sheet visible.

In this article, I’ve covered the concept of hiding and unhiding sheets in Excel using VBA and provided some simple code examples that you can use in various situations.

I hope you found this article useful. Please let me know your thoughts in the comments section below.

**Other Excel articles you may also like:**

*   [What is VBA Programming in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Activate Sheet (Worksheet.Activate)](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)
    
*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    

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