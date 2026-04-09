# VBA Copy Sheet to New/Existing Workbook

**Source:** https://trumpexcel.com/excel-vba/copy-sheet

---

[Skip to content](https://trumpexcel.com/excel-vba/copy-sheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/copy-sheet/#below-title)

VBA can save you a lot of time when working with worksheets and workbooks in Excel.

One common task that I often had to do was to copy an existing sheet in my current workbook into a new workbook or some other existing workbook.

While you can do this manually, if you have to do this quite often, it would be easier to use VBA.

In this article, I will show you multiple different scenarios where you can use VBA to copy a sheet to another workbook.

_Note: To make it easier for you to understand the code, I have added comments within the code itself_.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/copy-sheet/#)

Copy Sheet to a New Workbook
----------------------------

In this section, I have covered some VBA codes that you can use when you want to copy a sheet to a new workbook (where the new workbook is created and opened by the VBA code itself).

### Copy Sheet to a New Workbook As Is

    Sub CopySheetToNewWorkbook()
    
        ' Declare variable to hold the source worksheet
        Dim sourceWs As Worksheet
        
        ' Set the source worksheet you want to copy from the active workbook
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Copy the source worksheet to a new workbook
        sourceWs.Copy
    End Sub

The above VBA code copies a worksheet named “Sheet1” from the active workbook to a new workbook.

To create a new workbook, the _.Copy_ method is used without any parameters, and Excel takes care of creating a new workbook and then placing the copied sheet in it.

After running this code, you’ll find a new workbook activated on your screen containing the copied sheet. The copied sheet will retain its original name, “Sheet1”.

**Note**: In the above code, I have hardcoded the name “Sheet1” of the sheet that needs to be copied. You can change this accordingly. If you want the active sheet to be copied, you can use the line _Set sourceWs = Activesheet_ instead.

### Copy Sheet to a New Workbook as Values

If you want to copy a sheet from your existing workbook to a new workbook and only want the values (i.e., you don’t want to keep the formulas in the sheet you copied), you can use the code below.

    Sub CopySheetasValues()
    
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim newWb As Workbook
        
        ' Set the source worksheet you want to copy from the active workbook
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Copy the entire source worksheet to a new workbook
        sourceWs.Copy
        Set newWb = ActiveWorkbook
        
        ' Activate the copied worksheet in the new workbook
        newWb.Sheets(1).Activate
        
        ' Copy the used range of the active sheet to clipboard
        ActiveSheet.UsedRange.Copy
        
        ' Paste the copied data as values into the active sheet starting at cell "A1"
        ActiveSheet.Range("A1").PasteSpecial Paste:=xlPasteValues
        
        ' Clear clipboard to remove the dashed line around the copied range
        Application.CutCopyMode = False
    
    End Sub

The above code first copies Sheet1 into a new workbook.

It then copies the used range in the copied sheet and pastes it as values. This effectively means that it removes any formulas while keeping the values.

Note that only [formulas would be removed](https://trumpexcel.com/remove-formulas-keep-data-excel/)
. It won’t remove existing formatting or any objects that are there in the worksheet.

Also read: [Rename Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

### Copy Sheet to a New Workbook and Rename It

Below is the code that will copy the specified worksheet from the active workbook into a new workbook and then rename it using the name you specify in the code.

    Sub CopySheetandRename()
    
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim newWb As Workbook
        Dim wsName As String
        
        ' Set the source worksheet you want to copy
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Set the name for the sheet after copying
        wsName = "CopiedSheet"
        
        ' Copy the source worksheet to a new workbook
        sourceWs.Copy
        
        ' Get a reference to the new workbook
        Set newWb = ActiveWorkbook
        
        ' Rename the copied sheet in the new workbook
        newWb.Sheets(1).Name = wsName
    End Sub

The above VBA code first copies the worksheet named “Sheet1” from the active workbook to a new workbook.

When you copy a worksheet using the _.Copy_ method without any parameters, Excel automatically creates a new workbook to house the copied sheet.

After copying, it renames the copied sheet to “CopiedSheet”.

The new workbook will be active and will have only one sheet—the one that you copied.

Also read: [Clear Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/clear-sheet/)

### Copy Sheet to a New Workbook and Save the Workbook

    Sub CopySheetAndSave()
    
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim newWb As Workbook
        Dim savePath As String
        
        ' Set the source worksheet you want to copy
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Define the save path and filename
        savePath = "C:\Users\sumit\downloads\NewWorkbook.xlsx"
        
        ' Copy the source worksheet to a new workbook
        sourceWs.Copy
        
        ' Get a reference to the new workbook
        Set newWb = ActiveWorkbook
        
        ' Save the new workbook to the specified path
        newWb.SaveAs Filename:=savePath
        
        ' Close the new workbook
        newWb.Close
    End Sub

The above VBA code copies a sheet named “Sheet1” from the active workbook to a new workbook.

It then saves the new workbook to the specified location defined in the _savePath_ variable. You can change the path in the code to the folder where you want to save the workbook.

The ActiveWorkbook refers to the new workbook that was created when the _.Copy_ method was executed.

We then save this new workbook using the _.SaveAs_ method, specifying the path where it should be saved. Finally, the new workbook is closed using the _.Close_ method.

If you do not want this newly created workbook to be closed, you can remove the _newWb.Close_ line from the code.

Make sure that the folder path you specify is correct, else the code will give you a runtime error (Run-time error ‘1004’)

Also read: [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)

### Copy Sheet to a New Workbook and Save it as CSV

    Sub CopySheetandSaveasCSV()
    
        'Declare variables
        Dim sourceWs As Worksheet
        Dim csvPath As String
        
        ' Set the source worksheet you want to copy from the active workbook.
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Optional: Define where you want to save the CSV file.
        csvPath = "C:\Users\sumit\downloads\YourFile.csv"
        
        ' Save the active worksheet as a CSV file.
        sourceWs.SaveAs Filename:=csvPath, FileFormat:=xlCSVUTF8, CreateBackup:=False
        
    End Sub
    

The above VBA code would save the specified sheet (which is Sheet1 in this example) as a CSV file in the specified folder path.

**Note**: You can only save one worksheet as a CSV file (and not the entire workbook). CSV file format doesn’t allow saving a workbook with multiple files as CSV. Also, I have used xlCSVUTF8 in the code as I didn’t want the formatting and the formulas in the sheet to be lost when converted to CSV. If you don’t want to have the formatting and formulas, you can use xlCSV instead of xlCSVUTF8

Also read: [How to Open Excel Files Using VBA](https://trumpexcel.com/open-excel-files-using-vba/)

Copy Sheet to an Already Open Workbook
--------------------------------------

In this section, I’ll cover some scenarios where you can copy a sheet to an already existing workbook (which may or may not be open).

### Copy Sheet to an Already Open Workbook as is

    Sub CopySheetToOpenWorkbook()
        
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim targetWb As Workbook
        
        ' Set the source worksheet you want to copy
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Get a reference to the target workbook, already open
        Set targetWb = Workbooks("TargetWorkbook.xlsx")
        
        ' Copy the sheet to the end of the target workbook
        sourceWs.Copy After:=targetWb.Sheets(targetWb.Sheets.Count)
    End Sub

The above code copies a sheet named “Sheet1” from the active workbook (ThisWorkbook) to another workbook named “TargetWorkbook.xlsx”, which should already be open.

If a sheet with the same name exists in the target workbook, the new sheet’s name would be changed (by adding a numeral in brackets – like (2)).

To use this code, make sure the target workbook (in which you want to copy and put the sheet) is already open, and then run the code from the workbook containing “Sheet1”.

If the target workbook is not open or if it’s name is incorrect in the code, you will get a “_Run-time error 9: Subscript out of range_” error.

Note that we are copying the sheet and not moving the sheet. So, the original sheet would remain in the original workbook, and the copied sheet would be put in the target workbook.

You will have to change the sheet name (I used “Sheet1”), and the target workbook name (I used “TargetWorkbook.xlsx”).

By default, the copied sheet would always be placed at the end of all the sheets in the target workbook

### Copy Sheet to the Beginning of an Already Open Workbook

If you want to copy the sheet at the beginning of the target workbook,  
assuming it’s already open, you can use the code below:

    Sub CopySheetToBeginning()
    
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim targetWb As Workbook
        
        ' Set the source worksheet you want to copy
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Get a reference to the target workbook, already open
        Set targetWb = Workbooks("TargetWorkbook.xlsx")
        
        ' Copy the sheet to the beginning of the target workbook
        sourceWs.Copy Before:=targetWb.Sheets(1)
    End Sub

The above code copies a sheet called “Sheet1” from the active workbook to the beginning of an already open workbook named “TargetWorkbook.xlsx”.

To specify that the copied sheet should be positioned at the beginning, I have used _sourceWs.Copy Before:=targetWb.Sheets(1)_

The copied sheet will retain its original name unless the target workbook already contains a sheet with the same name. In such cases, Excel will automatically rename the copied sheet.

### Copy Sheet to the End of an Already Open Workbook

    Sub CopySheetToEnd()
    
        ' Declare variables
        Dim sourceWs As Worksheet
        Dim targetWb As Workbook
        
        ' Set the source worksheet you want to copy
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Get a reference to the target workbook, already open
        Set targetWb = Workbooks("TargetWorkbook.xlsx")
        
        ' Copy the sheet to the beginning of the target workbook
        sourceWs.Copy After:=targetWb.Sheets(targetWb.Sheets.Count)
    End Sub

The above code counts the total number of sheets in the target workbook and then places the copied sheet after all the sheets.

### Copy All Sheets to Already Open Workbook

    Sub CopyAllSheets()
    
        Dim sourcews As Worksheet
        Dim destinationwb As Workbook
        Dim wbName As String
        
        ' Define the name of the already open workbook you want to copy to
        wbName = "TargetWorkbook.xlsx"
        
        ' Set the destination workbook by checking each open workbook
        For Each wb In Workbooks
            If wb.Name = wbName Then
                Set destinationwb = wb
                Exit For
            End If
        Next wb
        
        ' Check if the destination workbook is set
        If destinationwb Is Nothing Then
            MsgBox "Target workbook not found!"
            Exit Sub
        End If
        
        ' Loop through each worksheet in the current workbook
        For Each sourcews In ThisWorkbook.Worksheets
            ' Copy the worksheet to the destination workbook
            sourcews.Copy After:=destinationwb.Sheets(destinationwb.Sheets.Count)
        Next sourcews
        
    End Sub

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through all the worksheets in the workbook and copy them one by one to the destination workbook.

Copy Sheet Without Opening
--------------------------

When it comes to copying sheet, You won’t be able to do it without opening the workbook that has the shield that you want to copy.

However, what you can do is open the workbook using the code, copy the sheet, and then close the workbook.

We can do this using the below line in the code that does the things in the background without us seeing it happen.

    Application.ScreenUpdating = False 

Once you’re done running the code, you can then turn it back on by using.

    Application.ScreenUpdating = True

Now, let’s see some examples in action.

### Copy Sheet To Another Closed Workbook (Without Opening)

    Sub CopySheetToClosedWorkbook()
    
        Dim sourceWs As Worksheet
        Dim targetWb As Workbook
        Dim targetWs As Worksheet
        Dim targetWbPath As String
        
        ' Set the source worksheet you want to copy from the active workbook
        Set sourceWs = ThisWorkbook.Sheets("Sheet1")
        
        ' Define the path to the target workbook
        targetWbPath = "C:\Users\sumit\Downloads\TargetWorkbook.xlsx"
    
        ' Disbales screen updating
        Application.ScreenUpdating = False
        
        ' Open the target workbook behind the scenes
        Set targetWb = Workbooks.Open(targetWbPath)
        
        ' Copy the worksheet to the target workbook
        sourceWs.Copy After:=targetWb.Sheets(targetWb.Sheets.Count)
        
        ' Save and close the destination workbook
        targetWb.Close SaveChanges:=True
        
        ' Enables screen updating
        Application.ScreenUpdating = True
    
    End Sub

The above code opens the target workbook, then copies the sheet in the current workbook to the target workbook, and then closes it.

Since we used _Application.ScreenUpdating = False_ before opening the workbook, you don’t see it happening on the screen.

### Copy Sheet From Closed Workbook

    Sub CopySheetFromClosedWorkbook()
    
        ' Declare variables
        Dim sourceWorkbook As Workbook
        Dim targetWorkbook As Workbook
        Dim ws As Worksheet
        
        ' Set the destination workbook to the active workbook
        Set targetWorkbook = ThisWorkbook
        
        ' Disbales screen updating
        Application.ScreenUpdating = False
        
        ' Open the source workbook
        Set sourceWorkbook = Workbooks.Open("C:\Users\sumit\Downloads\TargetWorkbook.xlsx")
        
        ' Set the worksheet that you want to copy
        Set ws = sourceWorkbook.Sheets("Old")
        
        ' Copy the worksheet to the destination workbook
        ws.Copy After:=targetWorkbook.Sheets(targetWorkbook.Sheets.Count)
        
        ' Close the source workbook without saving changes
        sourceWorkbook.Close SaveChanges:=False
        
        ' Enables screen updating
        Application.ScreenUpdating = True
        
        ' Release the object variables to free up memory
        Set ws = Nothing
        Set sourceWorkbook = Nothing
        Set targetWorkbook = Nothing
    End Sub
    

The above VB code is quite straightforward.

It goes to the workbook that is closed (from which we want to copy the sheet), opens it, copies the sheet to the destination workbook, and then closes it.

While I have only shown you how to do it with one closed workbook, you can do it with multiple workbooks, which could actually be a big time saver if you want to quickly collate worksheets from different closed workbooks.

**VBA Copy Sheet Type Mismatch Error 13**
-----------------------------------------

If you encounter a “Type Mismatch Error 13” when attempting to copy a sheet using VBA, it’s likely that some of the variables or objects you’re using in the code are not defined correctly.

For example, if I define a variable that can hold worksheets, and I try and assign it to a variable that is defined to hold workbooks, then I would get the “Type Mismatch Error 13” error.

**Other articles you may also like:**

*   [Excel VBA](https://trumpexcel.com/excel-vba/)
    
*   [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [VBA Activate Sheet (Worksheet.Activate)](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [Using Workbook Object in Excel VBA (Open, Close, Save, Set)](https://trumpexcel.com/vba-workbook/)
    
*   [Using VBA FileSystemObject (FSO) in Excel](https://trumpexcel.com/vba-filesystemobject/)
    
*   [Combine Multiple Excel Files into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    
*   [VBA to Hide / Unhide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)
    

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