# Check IF Sheet Exists Using VBA in Excel

**Source:** https://trumpexcel.com/excel-vba/check-if-sheet-exists

---

[Skip to content](https://trumpexcel.com/excel-vba/check-if-sheet-exists/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/check-if-sheet-exists/#below-title)

With VBA, you can easily check whether a sheet exists or not in a given workbook by going through all the sheets and checking their names.

In this article, I am going to show you a few scenarios where you can use VBA to check if a sheet exists or not in the current workbook, in some other open workbook, or even in a closed workbook.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/check-if-sheet-exists/#)

Check If the Sheet Exists and Show a Message
--------------------------------------------

Below is the VBA code that checks whether the sheet with the name sales exists in the current book or not.

    Sub CheckIfSheetExists()
        Dim ws As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        
        ' Assign the name of the sheet you're looking for to sheetName
        sheetName = "Sales"
        
        ' Initialize sheetExists to False
        sheetExists = False
        
        ' Loop through all worksheets in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Check if the worksheet name matches sheetName
            If ws.Name = sheetName Then
                ' Set sheetExists to True and exit the loop
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' Display a message box to indicate whether the sheet exists
        If sheetExists Then
            MsgBox "Yes, the sheet exists."
        Else
            MsgBox "No, the sheet does not exist."
        End If
    End Sub

The above code uses a For Next loop to go through each worksheet in the current workbook and check its name.

If the name of the worksheet is “Sales”, it exits the for loop and shows a message, as shown below.

![Message box when the sheet exists in the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20182%20186'%3E%3C/svg%3E)

And if it cannot find the worksheet with the name ‘Sales’, it will show another message, as shown below.

![Prompt when the sheet does not exist in workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20186'%3E%3C/svg%3E)

Note that in the above code, I’ve hard-coded the name of the sheet that I need to check for.

Also read: [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)

Ask the Sheet Name from the User and Check If It Exists
-------------------------------------------------------

If you want to ask the user for the sheet name and then [run the code](https://trumpexcel.com/run-a-macro-excel/)
 to check for it, you can use the below code.

    Sub CheckIfSheetExists()
        Dim ws As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        
        ' Prompt the user for the name of the sheet to look for
        sheetName = InputBox("Enter the name of the sheet you want to check:")
        
        ' Initialize sheetExists to False
        sheetExists = False
        
        ' Loop through all worksheets in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Check if the worksheet name matches sheetName
            If ws.Name = sheetName Then
                ' Set sheetExists to True and exit the loop
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' Display a message box to indicate whether the sheet exists
        If sheetExists Then
            MsgBox "Yes, the sheet exists."
        Else
            MsgBox "No, the sheet does not exist."
        End If
    End Sub
    

It first shows an input box asking for the sheet name from the user and then checks for it in the workbook.

Also read: [Create New Sheet Using VBA in Excel (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)

Check If the Sheet Exists (if Not, Create It)
---------------------------------------------

Below is the VBA code asks the user for the sheet name that needs to be checked for existence.

It then goes through all the worksheets and checks whether the sheet exists or not. If the sheet exists, it shows a message stating that, and if the sheet does not exist, it creates a new one with the same name.

    Sub CheckSheetExists()
        Dim ws As Worksheet
        Dim NewWs As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        
        ' Prompt the user for the name of the sheet to look for
        sheetName = InputBox("Enter the name of the sheet you want to check:")
        
        ' Initialize sheetExists to False
        sheetExists = False
        
        ' Loop through all worksheets in the workbook
        For Each ws In ThisWorkbook.Worksheets
            ' Check if the worksheet name matches sheetName
            If ws.Name = sheetName Then
                ' Set sheetExists to True and exit the loop
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' Display a message box to indicate whether the sheet exists
        If sheetExists Then
            MsgBox "The sheet exists."
        Else
            Set NewWs = Worksheets.Add
            NewWs.Name = sheetName
            MsgBox "The sheet did not exist. A new sheet with the name " & sheetName & " has been created"
        End If
    End Sub
    

Also read: [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)

Check If the Sheet Exists in Another Open Workbook
--------------------------------------------------

If you already have another workbook open and you want to check whether a sheet exists in that open workbook or not, you can use the below code.

    Sub CheckSheetInWorkbook()
        Dim ws As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        Dim targetWorkbook As Workbook
        
        ' Prompt the user for the name of the sheet to look for
        sheetName = InputBox("Enter the name of the sheet you want to check:")
        
        ' Prompt the user for the name of the workbook to check in
        Set targetWorkbook = Workbooks("Example.xlsx")
    
            
            ' Loop through all worksheets in the target workbook
            For Each ws In targetWorkbook.Worksheets
                ' Check if the worksheet name matches sheetName
                If ws.Name = sheetName Then
                    ' Set sheetExists to True and exit the loop
                    sheetExists = True
                    Exit For
                End If
            Next ws
            
            ' Display a message box to indicate whether the sheet exists
            If sheetExists Then
                MsgBox "The sheet exists in the open workbook."
            Else
                MsgBox "The sheet does not exist in the open workbook."
            End If
    
    End Sub

When you run the above code, it is going to ask you for the sheet name and then go through all the sheets in the specified workbook. In this example, I have used Example.xlsx as the workbook where I am checking the sheet.

You can change the workbook name in the code, or you can use an input box to ask the user for the workbook name.

Also read: [Rename Sheet Using VBA in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

Check If the Sheet Exists in a Closed Workbook
----------------------------------------------

If you need to check whether a sheet exists or not in a closed workbook, you can use the below VBA code.

    Sub CheckSheetInClosedWorkbook()
        Dim ws As Worksheet
        Dim sheetName As String
        Dim sheetExists As Boolean
        Dim workbookPath As String
        Dim targetWorkbook As Workbook
        
        ' Prompt the user for the name of the sheet to look for
        sheetName = InputBox("Enter the name of the sheet you want to check:")
        
        ' Show the Open dialog to allow the user to select the workbook
        workbookPath = Application.GetOpenFilename(Title:="Select the workbook", FileFilter:="Excel Files *.xls* (*.xls*),")
        
        ' Exit if the user cancels the Open dialog
        If workbookPath = "False" Then Exit Sub
        
        ' Open the workbook in the background
        Application.ScreenUpdating = False
        Set targetWorkbook = Workbooks.Open(workbookPath, ReadOnly:=True, UpdateLinks:=False)
        
        ' Initialize sheetExists to False
        sheetExists = False
        
        ' Loop through all worksheets in the target workbook
        For Each ws In targetWorkbook.Worksheets
            If ws.Name = sheetName Then
                sheetExists = True
                Exit For
            End If
        Next ws
        
        ' Close the workbook
        targetWorkbook.Close False
        Application.ScreenUpdating = True
        
        ' Display a message box to indicate whether the sheet exists
        If sheetExists Then
            MsgBox "Yes, the sheet exists"
        Else
            MsgBox "No, the sheet does not exist"
        End If
    End Sub
    

The above code first asks for the sheet name that you want to check and then shows the Open File dialog box so that you can select the file in which you want to check for the existence of the sheet.

Once this is done, Excel opens the workbook in the background and then goes through all the worksheets in that workbook. If it finds the worksheet with the specified name, it shows you a message box, as shown below.

![Message box when the sheet exists in the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20182%20186'%3E%3C/svg%3E)

And if it isn’t able to find the worksheet, it shows you a message box that’s shown below.

![Prompt when the sheet does not exist in workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20186'%3E%3C/svg%3E)

It also closes the workbook in the back end once it’s done looking for the sheet.

Also read: [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)

**Other articles you may also like:**

*   [Delete Sheet in Excel Using VBA](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Activate Sheet](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [Hide or Unhide Sheets Using VBA](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)
    
*   [Run Time Error 9 (Subscript Out of Range)](https://trumpexcel.com/excel-vba/run-time-error-9/)
    

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