# Protect and Unprotect Sheet Using VBA

**Source:** https://trumpexcel.com/excel-vba/protect-unprotect-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/#below-title)

It’s common for people to protect their work in Excel by locking the sheet (also called protecting the sheet) in a workbook.

A common example is when you have created a dashboard or report that has multiple sheets with calculations, and you don’t want the user or your manager/colleague to accidentally mess up with the formulas.

In such a case, it’s a good idea to protect some or all the sheets.

Similarly, you may receive a workbook with protected sheets that you want to unprotect.

While you can protect or unprotect sheets manually, VBA allows you to do this at scale.

In this article, I will cover various scenarios where you can protect and unprotect sheets in Excel using VBA.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/#)

Worksheet.Protect Syntax in VBA
-------------------------------

Below is the syntax you need to use to protect a sheet using VBA:

ws.Protect

Here, ws is a variable that represents the worksheet that you want to protect.

For example, if you want to protect Sheet1, you can use the below code.

    Sub ProtectSheet()
    Worksheets("Sheet1").Protect
    End Sub

Here, I have qualified the sheet I want to protect by using _Worksheets(“Sheet1”)_.

Alternatively, you can first assign the sheet to a variable and then protect it as shown below in the code:

    Sub ProtectSheet()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    ws.Protect
    End Sub

Here, I have first set the variable ws to the sheet I want to protect and then used _ws.Unprotect_

When you just use the Protect method, as shown above, it will protect the entire sheet (and you won’t be able to make any changes).

However, the Protect method does allow a number of optional arguments that allow you to select what not to protect while protecting/locking the entire sheet.

Below is the full syntax of the [Worksheet.Protect method](https://learn.microsoft.com/en-us/office/vba/api/excel.worksheet.protect)
:

ws.Protect (Password, DrawingObjects, Contents, Scenarios, UserInterfaceOnly, AllowFormattingCells, AllowFormattingColumns, AllowFormattingRows, AllowInsertingColumns, AllowInsertingRows, AllowInsertingHyperlinks, AllowDeletingColumns, AllowDeletingRows, AllowSorting, AllowFiltering, AllowUsingPivotTables)

All these arguments are optional, but you can use them to change how the protection should be done on your sheets (I will cover more examples of these later in this article)

Here is a short explanation of each of these options:

*   **Password**: This lets you specify a case-sensitive password for your sheet or book. If you don’t set one, you won’t need a password to unprotect it. It’s a good idea to use a strong password, like Y6dh!et5, and remember, if you forget it, Microsoft can’t help you get it back. Make sure to keep it stored safely!
*   **DrawingObjects**: This setting protects your shapes, and it’s set to True by default.
*   **Contents**: Keeps the chart or locked cells in your worksheet safe; it’s automatically set to True.
*   **Scenarios**: This one is for protecting scenarios on your worksheet. It’s set to True right off the bat and is only relevant for worksheets.
*   **UserInterfaceOnly**: When set to True, it protects the user interface but leaves macros alone. If you skip this, it’ll protect both macros and the UI.
*   **AllowFormattingCells**: It lets you format any cell on a protected worksheet when set to True, though it’s False by default.
*   **AllowFormattingColumns**: This allows you to format any column on a protected worksheet. This is set to True, but the default setting is False.
*   **AllowFormattingRows**: This enables you to format any row on a protected worksheet. It’s set to True, but normally it’s False.
*   **AllowInsertingColumns**: It lets you add columns on a protected worksheet if you set it to True, but usually, this is set to False.
*   **AllowInsertingRows**: This allows you to insert rows on a protected worksheet. By default, this is set to False.
*   **AllowInsertingHyperlinks**: This enables you to add hyperlinks on a protected worksheet. By default, this is set to False.
*   **AllowDeletingColumns**: This lets you delete columns on a protected worksheet, provided all cells in the column are unlocked. The default setting for this is False.
*   **AllowDeletingRows**: This option allows you to remove rows on a protected worksheet as long as every cell in the row is unlocked, with the default being False.
*   **AllowSorting**: This enables you to [sort data](https://trumpexcel.com/sort-data-vba/)
     on a protected worksheet, but only if every cell in the sort range is unlocked. Normally, this is set to False.
*   **AllowFiltering**: This one lets you set filters on a protected worksheet. You can change filter criteria, but you can’t turn an auto filter on or off. The default setting here is False.
*   **AllowUsingPivotTables**: Permits you to use PivotTable reports on a protected worksheet. It’s set to False by default.

Worksheet.Unprotect Syntax in VBA
---------------------------------

The syntax to unprotect sheets in VBA is straightforward:

_worksheet.Unprotect (Password)_

If the worksheet has been Protected using a password, then you need to supply the password to unprotect it. If no password was used for protection, you can simply use ‘_worksheet.Unprotect_‘ to unlock the sheet.

Also read: [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)

VBA Code Examples to Protect Sheets in Excel
--------------------------------------------

Now, let’s look at some practical scenarios where you can use VBA to protect worksheets in Excel.

### Protect Sheet by Name

Below is the VBA code that would protect the sheet named “Final Report” in the workbook in which the code is run.

    Sub ProtectSheetByName()
    
        ThisWorkbook.Sheets("Final Report").Protect
    
    End Sub

The above code would protect the sheet named ‘Final Report’, without using any password.

As a best practice, it’s a good idea to assign the sheet name to an object variable, as it allows you to use that variable instead of the entire sheet name everywhere else in the code.

Below is the same code where we first assign the sheet to a variable _ws_, and then used _ws.protect_ to protect the sheet.

    Sub ProtectSheetByName()
    
        Dim ws As Worksheet
        Set ws = ThisWorkbook.Sheets("Final Report")
        ws.Protect
    
    End Sub

### Protect a Sheet With a Password

Below is the VBA code that would protect the sheet (named Final Report) with a password.

    Sub ProtectFinalReport()
    
        Dim ws As Worksheet
    
        ' Set "Final Report" sheet to a variable
        Set ws = ThisWorkbook.Sheets("Final Report")
    
        ' Protect the worksheet with a password
        ws.Protect Password:="Excel123"
    
    End Sub

The above code protects the worksheet using the _ws.Protect_ method, and at the same time, it also uses the Password argument to assign a password to it.

Now, when you want to unprotect this sheet manually through the Excel interface or using VBA, you will have to provide this password.

### Protect Sheet by Index Number

    Sub ProtectSheetByIndex()
    
        Dim sheetIndex As Integer
    
        ' Protect the first worksheet
        Worksheets(1).Protect
    
    End Sub

This macro applies the _.Protect_ method to the first worksheet in your workbook (worksheets are indexed starting from 1)

In case you want to protect using a password, you can use the password argument as shown in the below code:

    Sub ProtectSheetByIndex()
    
        Dim sheetIndex As Integer
    
        ' Protect the first worksheet
        Worksheets(1).Protect Password:="Excel123"
    
    End Sub

**Note**: In most cases, it’s better to refer to sheets using their name instead of the index number. There could be chances of error in case you end up changing the position of the worksheets in the workbook, which would also impact the index number (as the left-most sheet is always index number 1, followed by 2, 3, and so on). So, if you change the position of these worksheets, their index number also changes.

### Protect the Active Sheet

To protect the active sheet in an Excel workbook using VBA, you will use the _ActiveSheet_ property.

This property refers to the worksheet that is currently selected or active in Excel at the [time the macro runs](https://trumpexcel.com/run-a-macro-excel/)
.

Below is the VBA code to protect the active sheet:

    Sub ProtectActiveSheet()
       
        ActiveSheet.Protect
    
    End Sub

### Protect All Sheets

To protect all sheets in an Excel workbook with VBA, you need to loop through each sheet in the workbook and then apply the _Protect_ method to each sheet.

Below is the VBA code to protect all the sheets in a workbook:

    Sub ProtectAllSheets()
        
    Dim sh As Object
    
        ' Loop through each sheet and protect it
        For Each sh In ThisWorkbook.Sheets
            sh.Protect
        Next sh
    
    
    End Sub

The above code uses the [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to cycle through all the sheets in the workbook and then protect them one by one.

**Note**: In the above code, I’m looping through all the sheets (and not worksheets). In Excel, a sheet can be a worksheet or a chart sheet, and the above code is going to go through all the sheets irrespective of their type and protect them. In case you only want to protect the worksheets, you can use Worksheets instead of Sheets in the above code.

### Protect All Sheets Except the Active Sheets

Below is the VBA code that would protect all the sheets in the workbook except the active sheet:

    Sub ProtectAllExceptActive()
    
        Dim sh As Worksheet
    
        ' Loop through each worksheet in the workbook
        For Each sh In ThisWorkbook.Worksheets
    
            ' Check if the sheet is not the active sheet
            If sh.Name <> ActiveSheet.Name Then
    
                ' Protect the sheet with a password
                sh.Protect
    
            End If
    
        Next sh
    
    End Sub

The above code loops through each sheet in the workbook and checks whether the name of the sheet is the same as that of the active sheet.

If the name is different, it is protected, else it moves on to the next sheet.

Also read: [VBA to Unhide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)

### Protect Sheet But Allow Filtering and Sorting

Below is the VBA code that would protect the specified worksheet (named Report) but allow sorting and filtering.

    Sub ProtectSheetAllowFilterSort()
    
        Dim ws As Worksheet
    
        ' Set worksheet variable to the sheet you want to protect
        Set ws = ThisWorkbook.Sheets("Report")
    
        ' Protect the worksheet and allow sorting and filtering
        ws.Protect , AllowSorting:="True", AllowFiltering:="True"
        
    End Sub

In the above code, I have made use of the arguments _AllowSorting_ and _AllowFiltering_ and set them to True. This allows us to sort and filter data while the worksheet remains protected.

**Note**: This would only allow you to filter a dataset where a filter has already been applied to a data set. In case you already do not have the filter, you won’t be able to enable it after protecting the sheet.

### Protect Sheet But Allow Formatting

The VBA code below would protect the specified sheet but allow formatting of cells, rows, and columns.

    Sub ProtectSheetAllowFormatting()
        
        Dim ws As Worksheet
    
        ' Set worksheet variable to the sheet you want to protect
        Set ws = ThisWorkbook.Sheets("Report")
    
        ' Protect the worksheet and allow formatting
        ws.Protect AllowFormattingCells:="True", AllowFormattingColumns:="True", AllowFormattingRows:="True"
    
    End Sub

### Protect Sheet When Workbook is Opened

If you want to automatically protect a sheet when the workbook is opened, you can do that using the _Workbook\_Open_ event in VBA.

This event is triggered whenever the workbook is opened, and you can write a macro within this [VBA event](https://trumpexcel.com/vba-events/)
 to protect a specific sheet.

Below is the VBA code to do this:

    Private Sub Workbook_Open()
        
    Dim ws As Worksheet
    
        ' Set the variable to specific sheet to protect
        Set ws = ThisWorkbook.Sheets("Report") 
    
        ' Protect the worksheet with a password
        ws.Protect
    
    End Sub

You need to put this code in the ThisWorkbook object in the VB Editor. Below are the steps to do this:

1.  Press Alt + F11 in Excel to open the [VBA Editor](https://trumpexcel.com/visual-basic-editor/)
    
2.  In the VBA Editor, double-click on the “ThisWorkbook” object in the Project Explorer window. If you don’t see the Project Explorer, you can enable it by using the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Ctrl + R.
3.  Copy and paste the above VBA code in the code window that opens when you double-click on the ThisWorkbook object.
4.  Close the VB Editor

Now, whenever you open this workbook, it triggers the _Workbook\_Open_ event and runs the code to protect the ‘Report’ worksheet.

This method is useful when you’re working in shared environments where multiple users might be accessing the same workbook, and you don’t want them to make any changes.

Also read: [Unprotect Excel Sheets Without Password](https://trumpexcel.com/unprotect-excel-sheets-without-password/)

### Automatically Protect All Sheets When Saving the Workbook

This is another example where you would need to use VBA events to protect the sheet whenever a workbook is saved or closed.

Below is the VBA code that would protect all the worksheets when you save the workbook:

    Private Sub Workbook_BeforeSave(ByVal SaveAsUI As Boolean, Cancel As Boolean)
    
        Dim ws As Worksheet
    
        ' Loop through and protect each worksheet
        For Each ws In ThisWorkbook.Worksheets
            ws.Protect 
        Next ws
    
    End Sub

You need to put this code in the ThisWorkbook object in the VB Editor. Below are the steps to do this:

1.  Press Alt + F11 in Excel to open the VBA Editor.
2.  Double-click on the “ThisWorkbook” object in the Project Explorer window (use the keyboard shortcut Ctrl + R if you don’t see the Project Explorer).
3.  Copy and paste the above VBA code in the ThisWorkbook object code window.
4.  Close the VB Editor.

Now, whenever you save the workbook, it is going to trigger the _Workbook\_BeforeSave_ event and protect all the worksheets.

### Automatically Protect All Sheets When Closing the Workbook

Below is the VBA code that would protect all the worksheets when you close the workbook. This uses the _Workbook\_BeforeClose_ event to do this.

    Private Sub Workbook_BeforeClose(Cancel As Boolean)
        Dim ws As Worksheet
    
        ' Loop through each worksheet and protect it
        For Each ws In ThisWorkbook.Worksheets
            ws.Protect
        Next ws
        
    End Sub

Also read: [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)

VBA Code to Unprotect Sheets in Excel
-------------------------------------

Now, let’s have a look at some examples of how you can use VBA to unprotect sheets in Excel.

### UnProtect Sheet by Name

To unprotect a sheet by name (say “Final Report”), you can use the below code (if no password was used):

    Sub ProtectSheetByName()
    
        ThisWorkbook.Sheets("Final Report").UnProtect
    
    End Sub

In case a password was used to protect it, you need to give the password as shown below (replace the string _PasswordYouUsed_ with the actual password that was used to lock the sheet):

    Sub ProtectSheetByName()
    
        ThisWorkbook.Sheets("Final Report").UnProtect Password:="PasswordYouUsed"
    
    End Sub

In case you supply an incorrect password, you will see an error message as shown below:

![Error when wrong password is used to unprotect our sheet VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20255'%3E%3C/svg%3E)

### Unprotect Active Sheet

    Sub UnprotectActiveSheet()
    
        ' Unprotect the active worksheet without a password
        ActiveSheet.Unprotect
    
    End Sub

This macro is straightforward and effective for quickly removing protection from the sheet you are currently working on.

However, if the sheet was protected with a password, you would need to modify the Unprotect method to include the correct password, like ActiveSheet.Unprotect Password:=”YourPassword”

### Unprotect All Sheets

Below is the VBA code that would loop through all the worksheets in a workbook and unprotect all the worksheets one by one.

    Sub UnprotectAllWorkSheets()
    
        Dim ws As Worksheet
    
        ' Loop through each worksheet and Unprotect it
        For Each ws In ThisWorkbook.Worksheets
                ws.Unprotect
        Next ws
    
    End Sub

In case you also have charge sheets in your workbook, then you can use the below code, which uses the sheet object instead of the [worksheet object](https://trumpexcel.com/vba-worksheets/)
.

    Sub UnprotectAllSheets()
    
        Dim sh As Sheet
    
        ' Loop through each sheet and Unprotect it
        For Each sh In ThisWorkbook.Sheets
                sh.Unprotect
        Next ws
    
    End Sub

**Note**: This code is handy when you have multiple sheets in a workbook, and you want to quickly remove protection from all of them in one go. Remember, if the sheets are protected with a password, you’ll need to modify the _ws.Unprotect_ line to include the password, like _ws.Unprotect Password:=”ThePassword”_.

### Unprotect All Sheets When the Workbook is Opened

Below is the VBA code that you can use to unprotect/unlock all the worksheets as soon as the workbook is opened.

    Private Sub Workbook_Open()
    
        Dim ws As Worksheet
    
        ' Loop through each worksheet and unprotect it
        For Each ws In ThisWorkbook.Worksheets
                ws.Unprotect
        Next ws
    
    End Sub

This is an event code, which means this needs to execute only when _Workbook\_Open_ event is triggered.

Below are the steps to place this code in the ThisWorkbook object so it runs every time the workbook is opened.

*   Open the workbook in which you want to put this code.
*   Press Alt + F11 to open the VBA editor.
*   In the Project Explorer window, double-click on ‘ThisWorkbook’ to open its code module.
*   Paste the code into the ThisWorkbook module.
*   Close the VB Editor

Now, whenever you open this workbook, all the worksheets in that workbook will automatically be unprotected.

In this article, I have covered various scenarios where you can use simple VBA code to protect and unprotect worksheets in Excel.

I hope you found this article useful. In case you have any questions, do leave a comment below.

**Other Excel articles you may also like:**

*   [What is VBA in Excel? Learn Excel VBA Programming!](https://trumpexcel.com/excel-vba/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)
    
*   [Remove Password from VBA Project in Excel](https://trumpexcel.com/excel-vba/remove-password/)
    
*   [VBA Activate Sheet (Worksheet.Activate)](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [Unhide Sheets in Excel](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [Clear Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/clear-sheet/)
    

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