# Using Workbook Object in Excel VBA (Open, Close, Save, Set)

**Source:** https://trumpexcel.com/vba-workbook

---

[Skip to content](https://trumpexcel.com/vba-workbook/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-workbook/#below-title)

In this tutorial, I will cover the how to work with workbooks in Excel using VBA.

In Excel, a ‘Workbook’ is an object that is a part of the ‘Workbooks’ collection. Within a workbook, you have different objects such as [worksheets](https://trumpexcel.com/vba-worksheets/)
, chart sheets, [cells and ranges](https://trumpexcel.com/vba-ranges/)
, chart objects, shapes, etc.

With VBA, you can do a lot of stuff with a workbook object – such as open a specific workbook, save and close workbooks, create new workbooks, change the workbook properties, etc.

So let’s get started.

All the codes I mention in this tutorial need to be placed in the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
. Go to the ‘[Where to Put the VBA Code](https://trumpexcel.com/vba-workbook/#Where_to_Put_the_VBA_Code)
‘ section to know how it works.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-workbook/#)

Referencing a Workbook using VBA
--------------------------------

There are different ways to refer to a Workbook object in VBA.

The method you choose would depend on what you want to get done.

In this section, I will cover the different ways to refer to a workbook along with some example codes.

### Using Workbook Names

If you have the exact name of the workbook that you want to refer to, you can use the name in the code.

Let’s begin with a simple example.

If you have two workbooks open, and you want to activate the workbook with the name – Examples.xlsx, you can use the below code:

Sub ActivateWorkbook()
Workbooks("Examples.xlsx").Activate
End Sub

Note that you need to use the file name along with the extension if the file has been saved. If it hasn’t been saved, then you can use the name without the file extension.

If you’re not sure what name to use, take help from the Project Explorer.

![Worksheets Object in Excel VBA - file name in project explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20272'%3E%3C/svg%3E)

If you want to activate a workbook and select a specific cell in a worksheet in that workbook, you need to give the entire address of the cell (including the Workbook and the Worksheet name).

Sub ActivateWorkbook()
Workbooks("Examples.xlsx").Worksheets("Sheet1").Activate
Range("A1").Select
End Sub

The above code first activates Sheet1 in the Examples.xlsx workbook and then selects cell A1 in the sheet.

You will often see a code where a reference to a worksheet or a cell/range is made without referring to the workbook. This happens when you’re referring to the worksheet/ranges in the same workbook that has the code in it and is also the active workbook. However, in some cases, you do need to specify the workbook to make sure the code works (more on this in the ThisWorkbook section).

### Using Index Numbers

You can also refer to the workbooks based on their index number.

For example, if you have three workbooks open, the following code would show you the names of the three workbooks in a message box (one at a time).

Sub WorkbookName()
MsgBox Workbooks(1).Name
MsgBox Workbooks(2).Name
MsgBox Workbooks(3).Name
End Sub

The above code uses MsgBox – which is a function that shows a message box with the specified text/value (which is the workbook name in this case).

One of the troubles I often have with using index numbers with Workbooks is that you never know which one is the first workbook and which one is the second and so on. To be sure, you would have to run the code as shown above or something similar to loop through the open workbooks and know their index number.

Excel treats the workbook opened first to have the index number as 1, and the next one as 2 and so on.

Despite this drawback, using index numbers can come in handy.

For example, if you want to loop through all the open workbooks and save all, you can use the index numbers.

In this case, since you want this to happen to all the workbooks, you’re not concerned about their individual index numbers.

The below code would loop through all the open workbooks and close all except the workbook that has this VBA code.

Sub CloseWorkbooks()
Dim WbCount As Integer
WbCount = Workbooks.Count
For i = WbCount To 1 Step -1
If Workbooks(i).Name <> ThisWorkbook.Name Then
Workbooks(i).Close
End If
Next i
End Sub

The above code counts the number of open workbooks and then goes through all the workbooks using the [For Each loop](https://trumpexcel.com/vba-loops/)
.

It uses the [IF condition](https://trumpexcel.com/if-then-else-vba/)
 to check if the name of the workbook is the same as that of the workbook where the code is being run.

If it’s not a match, it closes the workbook and moves to the next one.

Note that we have run the loop from WbCount to 1 with a Step of -1. This is done as with each loop, the number of open workbooks is decreasing.

ThisWorkbook is covered in detail in the later section.

Also read: [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)

### Using ActiveWorkbook

ActiveWorkbook, as the name suggests, refers to the workbook that is active.

The below code would show you the name of the active workbook.

Sub ActiveWorkbookName()
MsgBox ActiveWorkbook.Name
End Sub

When you use VBA to activate another workbook, the ActiveWorkbook part in the VBA after that would start referring to the activated workbook.

Here is an example of this.

If you have a workbook active and you insert the following code into it and run it, it would first show the name of the workbook that has the code and then the name of Examples.xlsx (which gets activated by the code).

Sub ActiveWorkbookName()
MsgBox ActiveWorkbook.Name
Workbooks("Examples.xlsx").Activate
MsgBox ActiveWorkbook.Name
End Sub

Note that when you create a new workbook using VBA, that newly created workbook automatically becomes the active workbook.

### Using ThisWorkbook

ThisWorkbook refers to the workbook where the code is being executed.

Every workbook would have a ThisWorkbook object as a part of it (visible in the Project Explorer).

![Workbook Object in VBA - ThisWorkbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20296%20321'%3E%3C/svg%3E)

‘ThisWorkbook’ can store regular macros (similar to the ones that we add-in modules) as well as event procedures. An [event procedure](https://trumpexcel.com/vba-events/)
 is something that is triggered based on an event – such as double-clicking on a cell, or saving a workbook or activating a worksheet.

Any event procedure that you save in this ‘ThisWorkbook’ would be available in the entire workbook, as compared to the sheet level events which are restricted to the specific sheets only.

For example, if you double-click on the ThisWorkbook object in the Project Explorer and copy-paste the below code in it, it will show the cell address whenever you double-click on any of the cells in the entire workbook.

Private Sub Workbook\_SheetBeforeDoubleClick(ByVal Sh As Object, ByVal Target As Range, Cancel As Boolean)
MsgBox Target.Address
End Sub

While ThisWorkbook’s main role is to store event procedure, you can also use it to refer to the workbook where the code is being executed.

The below code would return the name of the workbook in which the code is being executed.

Sub ThisWorkbookName()
MsgBox ThisWorkbook.Name
End Sub

The benefit of using ThisWorkbook (over ActiveWorkbook) is that it would refer to the same workbook (the one that has the code in it) in all the cases. So if you use a VBA code to add a new workbook, the ActiveWorkbook would change, but ThisWorkbook would still refer to the one that has the code.

Creating a New Workbook Object
------------------------------

The following code will create a new workbook.

Sub CreateNewWorkbook()
Workbooks.Add
End Sub

When you add a new workbook, it becomes the active workbook.

The following code will add a new workbook and then show you the name of that workbook (which would be the default Book1 type name).

Sub CreateNewWorkbook()
Workbooks.Add
MsgBox ActiveWorkbook.Name
End Sub

Open a Workbook using VBA
-------------------------

You can use VBA to open a specific workbook when you know the file path of the workbook.

The below code will open the workbook – Examples.xlsx which is in the Documents folder on my system.

Sub OpenWorkbook()
Workbooks.Open ("C:\\Users\\sumit\\Documents\\Examples.xlsx")
End Sub

In case the file exists in the default folder, which is the folder where VBA saves new files by default, then you can just specify the workbook name – without the entire path.

Sub OpenWorkbook()
Workbooks.Open ("Examples.xlsx")
End Sub

In case the workbook that you’re trying to open doesn’t exist, you’ll see an error.

To avoid this error, you can add a few lines to your code to first check whether the file exists or not and if it exists then try to open it.

The below code would check the file location and if it doesn’t exist, it will show a custom message (not the error message):

Sub OpenWorkbook()  
If Dir("C:\\Users\\sumit\\Documents\\Examples.xlsx") <> "" Then  
Workbooks.Open ("C:\\Users\\sumit\\Documents\\Examples.xlsx")  
Else  
MsgBox "The file doesn't exist"  
End If  
End Sub

You can also use the Open dialog box to select the file that you want to open.

Sub OpenWorkbook()  
If Dir("C:\\Users\\sumit\\Documents\\Examples.xlsx") <> "" Then  
Workbooks.Open ("C:\\Users\\sumit\\Documents\\Examples.xlsx")  
Else  
MsgBox "The file doesn't exist"  
End If  
End Sub

The above code opens the Open dialog box. When you select a file that you want to open, it assigns the file path to the FilePath variable. Workbooks.Open then uses the file path to open the file.

In case the user doesn’t open a file and clicks on Cancel button, FilePath becomes False. To avoid getting an error in this case, we have used the ‘On Error Resume Next’ statement.

**Related**: [Learn All about Error Handling in Excel VBA](https://trumpexcel.com/vba-error-handling/)

Saving a Workbook
-----------------

To save the active workbook, use the code below:

Sub SaveWorkbook()
ActiveWorkbook.Save
End Sub

This code works for the workbooks that have already been saved earlier. Also, since the workbook contains the above macro, if it hasn’t been saved as a .xlsm (or .xls) file, you will lose the macro when you open it next.

If you’re saving the workbook for the first time, it will show you a prompt as shown below:

![Workbook Object in VBA - Warning when saving Workbook for the first time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20704%20226'%3E%3C/svg%3E)

When saving for the first time, it’s better to use the ‘Saveas’ option.

The below code would save the active workbook as a .xlsm file in the default location (which is the document folder in my system).

Sub SaveWorkbook()
ActiveWorkbook.SaveAs Filename:="Test.xlsm", FileFormat:=xlOpenXMLWorkbookMacroEnabled
End Sub

If you want the file to be saved in a specific location, you need to mention that in the Filename value. The below code saves the file on my desktop.

Sub SaveWorkbook()
ActiveWorkbook.SaveAs Filename:="C:\\Users\\sumit\\Desktop\\Test.xlsm", FileFormat:=xlOpenXMLWorkbookMacroEnabled
End Sub

If you want the user to get the option to select the location to save the file, you can use call the Saveas dialog box. The below code shows the Saveas dialog box and allows the user to select the location where the file should be saved.

Sub SaveWorkbook()
Dim FilePath As String
FilePath = Application.GetSaveAsFilename
ActiveWorkbook.SaveAs Filename:=FilePath & ".xlsm", FileFormat:=xlOpenXMLWorkbookMacroEnabled
End Sub

Note that instead of using FileFormat:=xlOpenXMLWorkbookMacroEnabled, you can also use FileFormat:=52, where 52 is the code xlOpenXMLWorkbookMacroEnabled.

Also read: [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)

Saving All Open Workbooks
-------------------------

If you have more than one workbook open and you want to save all the workbooks, you can use the code below:

Sub SaveAllWorkbooks()
Dim wb As Workbook
For Each wb In Workbooks
wb.Save
Next wb
End Sub

The above saves all the workbooks, including the ones that have never been saved. The workbooks that have not been saved previously would get saved in the default location.

If you only want to save those workbooks that have previously been saved, you can use the below code:

Sub SaveAllWorkbooks()
Dim wb As Workbook
For Each wb In Workbooks
If wb.Path <> "" Then
wb.Save
End If
Next wb
End Sub

Saving and Closing All Workbooks
--------------------------------

If you want to close all the workbooks, except the workbook that has the current code in it, you can use the code below:

Sub CloseandSaveWorkbooks()
Dim wb As Workbook
For Each wb In Workbooks
If wb.Name <> ThisWorkbook.Name Then
wb.Close SaveChanges:=True
End If
Next wb
End Sub

The above code would close all the workbooks (except the workbook that has the code – ThisWorkbook). In case there are changes in these workbooks, the changes would be saved. In case there is a workbook that has never been saved, it will show the save as dialog box.

Save a Copy of the Workbook (with Timestamp)
--------------------------------------------

When I am working with complex data and dashboard in Excel workbooks, I often create different versions of my workbooks. This is helpful in case something goes wrong with my current workbook. I would at least have a copy of it saved with a different name (and I would only lose the work I did after creating a copy).

Here is the VBA code that will create a copy of your workbook and save it in the specified location.

Sub CreateaCopyofWorkbook()
ThisWorkbook.SaveCopyAs Filename:="C:\\Users\\sumit\\Desktop\\BackupCopy.xlsm"
End Sub

The above code would save a copy of your workbook every time you run this macro.

While this works great, I would feel more comfortable if I had different copies saved whenever I run this code. The reason this is important is that if I make an inadvertent mistake and run this macro, it will save the work with the mistakes. And I wouldn’t have access to the work before I made the mistake.

To handle such situations, you can use the below code that saves a new copy of the work each time you save it. And it also adds a date and timestamp as a part of the workbook name. This can help you track any mistake you did as you never lose any of the previously created backups.

Private Sub Workbook\_BeforeSave(ByVal SaveAsUI As Boolean, Cancel As Boolean)
ThisWorkbook.SaveCopyAs Filename:="C:\\Users\\sumit\\Desktop\\BackupCopy" & Format(Now(), "dd-mm-yy-hh-mm-ss-AMPM") & ".xlsm"
End Sub

The above code would create a copy every time you [run this macro](https://trumpexcel.com/run-a-macro-excel/)
 and [add a date/time stamp](https://trumpexcel.com/date-timestamp-excel/)
 to the workbook name.

Create a New Workbook for Each Worksheet
----------------------------------------

In some cases, you may have a workbook that has multiple worksheets, and you want to create a workbook for each worksheet.

This could be the case when you have monthly/quarterly reports in a single workbook and you want to split these into one workbook for each worksheet.

Or, if you have department wise reports and you want to split these into individual workbooks so that you can send these individual workbooks to the department heads.

Here is the code that will create a workbook for each worksheet, give it the same name as that of the worksheet, and save it in the specified folder.

Sub CreateWorkbookforWorksheets()
Dim ws As Worksheet
Dim wb As Workbook
For Each ws In ThisWorkbook.Worksheets
Set wb = Workbooks.Add
ws.Copy Before:=wb.Sheets(1)
Application.DisplayAlerts = False
wb.Sheets(2).Delete
Application.DisplayAlerts = True
wb.SaveAs "C:\\Users\\sumit\\Desktop\\Test\\" & ws.Name & ".xlsx"
wb.Close
Next ws
End Sub

In the above code, we have used two variable ‘ws’ and ‘wb’.

The code goes through each worksheet (using the [For Each Next loop](https://trumpexcel.com/vba-loops/)
) and creates a workbook for it. It also uses the copy method of the worksheet object to create a copy of the worksheet in the new workbook.

Note that I have used the SET statement to assign the ‘wb’ variable to any new workbook that is created by the code.

You can use this technique to assign a workbook object to a variable. This is covered in the next section.

Assign Workbook Object to a Variable
------------------------------------

In VBA, you can assign an object to a variable, and then use the variable to refer to that object.

For example, in the below code, I use VBA to add a new workbook and then assign that workbook to the variable wb. To do this, I need to use the SET statement.

Once I have assigned the workbook to the variable, all the properties of the workbook are made available to the variable as well.

Sub AssigntoVariable()
Dim wb As Workbook
Set wb = Workbooks.Add
wb.SaveAs Filename:="C:\\Users\\sumit\\Desktop\\Examples.xlsx"
End Sub

Note that the first step in the code is to declare ‘wb’ as a workbook type variable. This tells VBA that this variable can hold the workbook object.

The next statement uses SET to assign the variable to the new workbook that we are adding. Once this assignment is done, we can use the wb variable to save the workbook (or do anything else with it).

Looping through Open Workbooks
------------------------------

We have already seen a few examples codes above that used looping in the code.

In this section, I will explain different ways to loop through open workbooks using VBA.

Suppose you want to save and close all the open workbooks, except the one with the code in it, then you can use the below code:

Sub CloseandSaveWorkbooks()
Dim wb As Workbook
For Each wb In Workbooks
If wb.Name <> ThisWorkbook.Name Then
wb.Close SaveChanges:=True
End If
Next wb
End Sub

The above code uses the For Each loop to go through each workbook in the Workbooks collection. To do this, we first need to declare ‘wb’ as the workbook type variable.

In every loop cycle, each workbook name is analyzed and if it doesn’t match the name of the workbook that has the code, it’s closed after saving its content.

The same can also be achieved with a different loop as shown below:

Sub CloseWorkbooks()
Dim WbCount As Integer
WbCount = Workbooks.Count
For i = WbCount To 1 Step -1
If Workbooks(i).Name <> ThisWorkbook.Name Then
Workbooks(i).Close SaveChanges:=True
End If
Next i
End Sub

The above code uses the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to close all the workbooks except the one that has the code in it. In this case, we don’t need to declare a workbook variable, but instead, we need to count the total number of open workbooks. When we have the count, we use the For Next loop to go through each workbook. Also, we use the index number to refer to the workbooks in this case.

Note that in the above code, we are looping from WbCount to 1 with Step -1. This is needed as with each loop, the workbook gets closed and the number of workbooks gets decreased by 1.

Error while Working with the Workbook Object (Run-time error ‘9’)
-----------------------------------------------------------------

One of the most common error you may encounter when working with workbooks is – [Run-time Error ‘9’ – Subscript out of range](https://trumpexcel.com/excel-vba/run-time-error-9/)
.

![Workbook Object in VBA - Runtime Error 9 Subscript Out of Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20255'%3E%3C/svg%3E)

Generally, VBA errors are not very informative and often leave it to you to figure out what went wrong.

Here are some of the possible reasons that may lead to this error:

*    The workbook that you’re trying to access does not exist. For example, if I am trying to access the fifth workbook using Workbooks(5), and there are only 4 workbooks open, then I will get this error.
*   If you’re using a wrong name to refer to the workbook. For example, if your workbook name is Examples.xlsx and you use Example.xlsx. then it will show you this error.
*   If you haven’t saved a workbook, and you use the extension, then you get this error. For example, if your workbook name is Book1, and you use the name Book1.xlsx without saving it, you will get this error.
*   The workbook you’re trying to access is closed.

Get a List of All Open Workbooks
--------------------------------

If you want to get a list of all the open workbooks in the current workbook (the workbook where you’re running the code), you can use the below code:

Sub GetWorkbookNames()
Dim wbcount As Integer
wbcount = Workbooks.Count
ThisWorkbook.Worksheets.Add
ActiveSheet.Range("A1").Activate
For i = 1 To wbcount
Range("A1").Offset(i - 1, 0).Value = Workbooks(i).Name
Next i
End Sub

The above code [adds a new worksheet](https://trumpexcel.com/insert-new-worksheet-excel/)
 and then lists the name of all the open workbooks.

If you want to get their file path as well, you can use the below code:

Sub GetWorkbookNames()
Dim wbcount As Integer
wbcount = Workbooks.Count
ThisWorkbook.Worksheets.Add
ActiveSheet.Range("A1").Activate
For i = 1 To wbcount
Range("A1").Offset(i - 1, 0).Value = Workbooks(i).Path & "\\" & Workbooks(i).Name
Next i
End Sub

Open the Specified Workbook by Double-clicking on the Cell
----------------------------------------------------------

If you have a list of file paths for Excel workbooks, you can use the below code to simply double-click on the cell with the file path and it will open that workbook.

Private Sub Workbook\_SheetBeforeDoubleClick(ByVal Sh As Object, ByVal Target As Range, Cancel As Boolean)
Workbooks.Open Target.Value
End Sub

This code would be placed in the ThisWorkbook code window.

To do this:

*   Double click on the ThisWorkbook object in the project explorer. Note that the ThisWorkbook object should be in the workbook where you want this functionality.
*   Copy and paste the above code.

Now, if you have the exact path of the files that you want to open, you can do that by simply double-clicking on the file path and VBA would instantly open that workbook.

Where to Put the VBA Code
-------------------------

Wondering where the VBA code goes in your Excel workbook?

Excel has a VBA backend called the VBA editor. You need to copy and paste the code into the VB Editor module code window.

Here are the steps to do this:

1.  Go to the Developer tab.![Using Workbooks in Excel VBA - Developer Tab in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on the Visual Basic option. This will open the VB editor in the backend.![Click on Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. If you don’t see the Project Explorer go to the View tab and click on Project Explorer.
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![Using Workbooks in Excel VBA - inserting module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20363'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.![Using Workbooks in Excel VBA - inserting module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20363'%3E%3C/svg%3E)

**You May Also Like the Following Excel VBA Tutorials:**

*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    .
*   [Creating a User Defined Function in Excel](https://trumpexcel.com/user-defined-function-vba/)
    .
*   [How to Create and Use Add-in in Excel](https://trumpexcel.com/excel-add-in/)
    .
*   [How to Resue Macros by placing it in the Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
    .
*   [Get the List of File Names from a Folder in Excel (with and without VBA)](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
    .
*   [How to Use Excel VBA InStr Function (with practical EXAMPLES)](https://trumpexcel.com/excel-vba-instr/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Using Workbook Object in Excel VBA (Open, Close, Save, Set)”
---------------------------------------------------------------------------

1.  In the section “Open a Workbook using VBA” you have the same code repeated twice. The second version is supposed to show the code needed to use a dialog box to open a workbook. However, it just repeats the hard-coded version. Just thought you would want to know, since it is a critical feature that some would be interested in.
    
    [Reply](https://trumpexcel.com/vba-workbook/#comment-33356)
    
2.  Hi, I am using copy/move option to copy some sheets to a new workbook using VBA. I am running into an issue where the new workbook name is named as Book1 or Book2 and so on depending how many new workbooks I have opened previously. Is there a solution where Book1/Book2 isn’t hard coded? Thanks, RM
    
    [Reply](https://trumpexcel.com/vba-workbook/#comment-13589)
    
3.  How to Send Email Automatically with attach Excel
    
    [Reply](https://trumpexcel.com/vba-workbook/#comment-11185)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-workbook/#respond)

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