# Activate Sheet Using VBA in Excel (Worksheet.Activate)

**Source:** https://trumpexcel.com/excel-vba/activate-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/activate-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/activate-sheet/#below-title)

When you have multiple worksheets in a workbook, you can manually activate a worksheet so that you see the content in that worksheet and can work in it.

The same thing can also be done with VBA using the _Worksheets.Activate_ method.

In this article, I will explain how _Worksheets.Activate_ method works and some examples of using VBA to activate worksheets.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/activate-sheet/#)

Worksheet.Activate Method
-------------------------

_Worksheet.Activate_ is a method that allows you to activate the specified worksheet.

To use this method, you need to refer to the worksheet that you want to activate. This reference can be done by using the sheet name or the sheet number.

### Activate Sheet By Name

Below is the VBA code that will activate Sheet1

    Sub ActivateSheet()
    
        ' This line of code activates the worksheet named "Sheet1".
        Worksheets("Sheet1").Activate
    
    End Sub
    

When you run this code, it will activate Sheet1 of the current workbook.

Note that in this code, I have used Worksheets(“Sheet1”), as Sheet1 is a part of the Worksheets collection. You can also use Sheets(“Sheet1”) as it’s also a part of the Sheets collection.

### Activate Sheet By Number

You can also activate sheets by their index number, which is it’s position in the workbook.

To activate the first sheet in the workbook, you can use the below VBA macro code:

    Sub ActivateSheet()
    
        ' This line of code activates the worksheet named "Sheet1".
        Worksheets(1).Activate
    
    End Sub

In most cases, It is better to use the sheet name instead of the sheet number, as the sheet number can change if you change the position of the worksheet in the workbook.

Activate Sheet Based on Cell Value
----------------------------------

Below is the VBA code that activates the sheet based on the value in cell A1.

    Sub ActivateSheetByCellValue()
    
        ' Activates the worksheet based on the name in cell A1
       Worksheets(Worksheets("Sheet1").Range("A1").Value).Activate
    
    End Sub

The above code first fetches the name that is there in cell a1 in Sheet1 and uses this name in the Worksheets object, and then activates it.

You can simplify the above code by using a variable to store the name in cell A1 and then use it to activate that worksheet (as shown below).

    Sub ActivateSheetByCellValue()
    
        ' Declare the variable
        Dim sheetName As String
        
        ' Store value in cell A1 in the variable
        sheetName = ThisWorkbook.Worksheets("Sheet1").Range("A1").Value
    
        ' This line of code activates the worksheet based on the name in cell A1.
        Worksheets(sheetName).Activate
    
    End Sub

Also read: [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)

Activate Sheet in When Opening the Workbook
-------------------------------------------

If you always want a specific worksheet to be activated whenever you open a workbook, you will have to use the Workbook\_Open event.

This event is going to trigger your VBA code whenever a workbook is open, and within the code, you can specify that it should always activate the specified worksheet.

Below is the VBA code that would always activate the Summary worksheet whenever the workbook (which has this code) is opened.

    Private Sub Workbook_Open()
    
        ' Activates "Summary" worksheet when workbook is opened
        ThisWorkbook.Worksheets("Summary").Activate
    
    End Sub
    

Note that the name of the above subroutine is _Sub Workbook\_Open()_, which makes it a workbook open event and would execute the code in this subroutine whenever the workbook is opened.

An [event code](https://trumpexcel.com/vba-events/)
 is not placed in the standard module. It needs to be placed on the object responsible for that event.

In this example, since we want the code to be run whenever the workbook is opened, we will have to place this code in the [workbook object](https://trumpexcel.com/vba-workbook/)
.

Here are the steps to put this code in the workbook object:

1.  Press ALT + F11 to open the VBA Editor.
2.  In the Project Explorer window on the left, double-click on “_ThisWorkbook_” object under the workbook for which you want this to happen.
3.  In the code window that appears, paste the above code.
4.  Save and close the VBA Editor.

Now, whenever you open the workbook in which we placed the code, it will trigger the _Workbook\_Open_ event and activate the _Summary_ sheet.

Also read: [Protect and Unprotect Sheet Using VBA](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)

Activate Sheet in Another Workbook
----------------------------------

Below is the VBA code that would activate a worksheet named “_Summary_” in the already open _Example.xlsx_ workbook.

    Sub ActivateSheetInAnotherWorkbook()
    
        ' This line of code sets a reference to the workbook named "Example.xlsx".
        Dim Wb As Workbook
        Set Wb = Workbooks("Example.xlsx")
    
        ' This line of code activates the worksheet named "Summary" in the referenced workbook.
        Wb.Sheets("Summary").Activate
    
    End Sub
    

Note that the above code will give you an error if the name of the workbook or the worksheet you want to refer to is incorrect or if the workbook is not already open.

If the workbook is closed, you can open it programmatically by modifying the code by including a line to [open that workbook](https://trumpexcel.com/open-excel-files-using-vba/)
.

VBA Activate Sheet Not Working – Possible Reason
------------------------------------------------

Here are some possible reasons you may be seeing an error when you’re trying to activate a sheet using VBA:

*   **Sheet Does Not Exist**: If you’re trying to activate a sheet that does not exist or if you have misspelled the name of an existing sheet that you’re trying to activate, you will see a [Run time Error 9 – Subscript out of range error](https://trumpexcel.com/excel-vba/run-time-error-9/)
    .
*   **Workbook is Not Open**: If you are trying to activate a sheet in another workbook that is not already open, you will see an error.
*   **Sheet is Hidden or Very Hidden:** If you’re trying to activate a sheet that is hidden or very hidden, you will get an error.
*   **Event Handling**: There might be some event-driven macros (like _Worksheet\_Activate_ or _Workbook\_SheetActivate_) that are overriding or interfering with the sheet activation.

It’s always a good idea to handle potential errors using error handling techniques like _On Error Resume Next_ and _On Error GoTo_, especially when dealing with objects that might not always be present or available. This can provide more graceful feedback to users and help diagnose issues.

Select vs. Activate in VBA
--------------------------

Since we’re talking about activating worksheets using VBA, I think it’s important I also tell you the difference between the _Select_ method and the _Activate_ method in VBA.

While both of these methods may seem to be doing the same thing, here is the difference:

*   You can select more than one object (such as a sheet, range, or chart) using the _Select_ method.
*   You can only activate one object using the _Activate_ method.

**Important Note**: Most of the time, there is no need for you to activate a worksheet to do anything in it using VBA. Almost everything that you need to do can also be done without activating the worksheet. For example, if you want to enter values in a range, clear a range, apply filters, insert a chart, or anything else, you can do that without activating the sheet. Most of the times, activating a sheet is unnecessary, and sometimes even a bad idea.

[What is VBA in Excel? Learn Excel VBA Programming!](https://trumpexcel.com/excel-vba/)

**Other Excel VBA articles you may also like:**

*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Delete Sheet](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)
    
*   [Using Active Cell in VBA in Excel (Examples)](https://trumpexcel.com/active-cell-vba-excel/)
    
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