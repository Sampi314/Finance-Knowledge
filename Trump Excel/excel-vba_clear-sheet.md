# Clear Sheet Using VBA in Excel

**Source:** https://trumpexcel.com/excel-vba/clear-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/clear-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/clear-sheet/#below-title)

With VBA, you can quickly clear part of the worksheet or the entire worksheet in Excel using the **_Cells.Clear method_**.

It also gives you the flexibility to choose whether you want to clear everything or specific things such as the formatting or the content, etc.

Let’s see a couple of simple VBA code examples to clear a sheet in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/clear-sheet/#)

Clear the Entire Active Sheet
-----------------------------

    Sub ClearActiveSheet()
    
        ' Clear everything from the active sheet
        ActiveSheet.Cells.Clear
    
    End Sub

The Cells property in the above code refers to all the cells in the sheet, and the Clear method effectively removes everything from these cells, leaving you with a completely blank sheet.

It clears all the data, formatting, and formulas from the sheet that is currently active when you run the macro.

Now, let me show you how to clear specific things from the worksheet (such as only the content formatting or comments) using VBA.

### Clear Only the Content

    Sub ClearActiveSheetContent()
    
        ActiveSheet.Cells.ClearContents
    
    End Sub

The above VBA code will remove any data or formulas in these cells in the entire sheet without affecting the cell formatting.

This macro is helpful when you need to reset the data in a sheet but want to preserve the existing formatting, like cell colors, borders, or number formats.

### Clear Only the Format

    Sub ClearActiveSheetFormats()
    
        ActiveSheet.Cells.ClearFormats
    
    End Sub

The above VBA macro code would remove the formatting while leaving everything else intact, including the content and formulas in the cells.

This macro is particularly useful when you need to reset the visual appearance of a sheet without losing the data or calculations it contains.

### Clear Only the Comments / Notes

Excel has notes as well as comments.

Notes (which earlier used to be called Comments are the non-threaded single notes, as shown below.

![Example of a note in Excel -  - VBA Clear Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20481%20243'%3E%3C/svg%3E)

Comment is a threaded discussion where you can add a comment, and other people can reply in the same thread (as shown below).

![Example of a comment in Excel - VBA Clear Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20291'%3E%3C/svg%3E)

If you want to clear all notes as well as comments from the entire sheet, you can use the below code:

    Sub ClearActiveSheetComments()
    
        ActiveSheet.Cells.ClearComments
    
    End Sub

Note: You can also use ClearNotes instead of ClearComments and it would work the same way

Also read: [Comments in Excel VBA (Add, Remove, Block Commenting)](https://trumpexcel.com/comments-excel-vba/)

### Clear Only the Hyperlinks

If you have [hyperlinks in your worksheet](https://trumpexcel.com/hyperlinks/)
 and you want to clear all the hyperlinks in one go, you can use the below code.

    Sub ClearActiveSheetHyperlinks()
    
        ActiveSheet.Cells.ClearHyperlinks
    
    End Sub

Note that this is not going to remove the content of the cell or even change the formatting, but it would remove the hyperlink property of the cell, which means that the cell would no longer be clickable.

Also read: [VBA to Remove Duplicate Values in Excel](https://trumpexcel.com/excel-vba/remove-duplicate-values/)

### Clear Only the Outline

If you have used the Group feature or the Auto Outline feature in Excel to create outlines, you can use the below code to clear the outline from the entire worksheet:

    Sub ClearActiveSheetHyperlinks()
    
        ActiveSheet.Cells.ClearOutline
    
    End Sub

**Note**: In all the codes covered so far, I’ve shown you how to clear the entire active sheet by using the expression _ActiveSheet.Cells_. If you want to clear a specific range or any specific worksheet, all you need to do is specify that range instead of _ActiveSheet.Cells_ and use the rest of the code as is. I have covered some examples of this in the below sections

Also read: [VBA Delete Sheet](https://trumpexcel.com/excel-vba/delete-sheet/)

Clear UsedRange in the Active Sheet
-----------------------------------

    Sub ClearUsedRange()
    
        ActiveSheet.UsedRange.Clear
    
    End Sub

This VBA code clears all content and formatting from the ‘UsedRange’ in the currently active worksheet of the active workbook.

_‘UseRange’ refers to any part of the worksheet that has been used or altered in some way, such as cells containing data, formatting, or formulas._

Also read: [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)

Clear Sheet By Name
-------------------

Below is the code to clear a sheet by using its name:

    Sub ClearUsedRange()
    
        Worksheets("Sheet1").Cells.Clear
    
    End Sub

In the above code, I have specified Sheet1 as the name of the worksheet, and then all the cells in this worksheet are cleared.

This approach is useful when you know the name of the sheet you want to clear and you don’t necessarily want it to be the active or currently selected sheet.

Also read: [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

Clear All the Sheets in the Workbook
------------------------------------

Below is the VBA code that would clear all the sheets in the workbook in which the code is run:

    Sub ClearAllSheets()
    
        Dim ws As Worksheet
    
        ' Loop through each worksheet and clear all cells
        For Each ws In ThisWorkbook.Worksheets
            ws.Cells.Clear
        Next ws
    
    End Sub
    

The above macro uses the [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each worksheet in _ThisWorkbook_ object and clear all the cells in each worksheet.

It is useful when you need to reset an entire workbook, clearing all sheets at once. It’s efficient and saves time compared to clearing each sheet individually.

Also read: [VBA Protect / Unprotect Sheet](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)

Clear Sheets That Contains a Specific Word in the Name
------------------------------------------------------

Below is the VBA macro code that would clear only those worksheets that have the word ‘Sales’ in their name.

    Sub ClearSheetsContainingSales()
    
        Dim ws As Worksheet
    
        ' Loop through each worksheet in the workbook
        For Each ws In ThisWorkbook.Worksheets
    
            ' If sheet name contains the word "Sales", clear it
            If InStr(1, ws.Name, "Sales", vbTextCompare) > 0 Then
                ws.Cells.Clear
            End If
    
        Next ws
    
    End Sub

The above code uses a For Next [VBA loop](https://trumpexcel.com/vba-loops/)
 to go through each worksheet in the workbook.

Inside the loop, the [InStr function](https://trumpexcel.com/excel-vba-instr/)
 checks if the word “Sales” is part of the worksheet’s name (_ws.Name_). The _vbTextCompare_ argument makes the comparison case-insensitive.

If the worksheet has the word ‘Sales’ in its name, _ws.Cells.Clear_ method clears all the cells in it.

Clear a Protected Sheet
-----------------------

In the below code, I clear a protected sheet named ‘Sales’

    Sub ClearProtectedSheet()
    
        Dim ws As Worksheet
        Set ws = ThisWorkbook.Sheets("Sales")  
    
        ' Unprotect the sheet (if it has a password, include it in the parentheses)
        ws.Unprotect "ThePassword" 
    
        ' Clear everything from the sheet
        ws.Cells.Clear
    
    End Sub

The above code clears all contents from a protected worksheet named “Sales” in the active workbook.

It first unprotects this sheet using the provided password (“_ThePassword_“). Once unprotected, it uses the _Cells.Clear_ method to remove all data and formatting from every cell in the worksheet.

**Other Excel VBA articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [VBA Activate Sheet (Worksheet.Activate)](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    

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