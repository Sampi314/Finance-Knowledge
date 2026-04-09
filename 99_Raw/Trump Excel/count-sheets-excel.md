# Count Sheets in Excel (using VBA)

**Source:** https://trumpexcel.com/count-sheets-excel

---

[Skip to content](https://trumpexcel.com/count-sheets-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-sheets-excel/#below-title)

There are some simple things that are not possible for you to do with in-built functions and functionalities in Excel, but can easily be done using VBA.

**Counting the total number of sheets** in the active workbook or any other workbook on your system is an example of such a task.

In this tutorial, I’ll show you some simple VBA code that you can use to count the total number of sheets in an Excel workbook.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-sheets-excel/#)

Count All Sheets in the Workbook
--------------------------------

There are multiple ways I can use VBA to give me the total count of sheets in a workbook.

In the following sections, I will show you three different methods, and you can choose which one to use:

1.  Using the VBA code in a module (to get sheet count as a message box)
2.  Using Immediate window
3.  Using a Custom Formula (which will give you the sheet count in a cell in the worksheet)

### VBA Code to Show Sheet Count in a Message Box

Below is the VBA code to get the total number of sheets in the current workbook shown in a message box:

Sub SheetCount()
MsgBox ThisWorkbook.Sheets.Count
End Sub

_In the above code, I have used Sheets, which will count all the sheets (be it worksheets or chart sheets). In case you only want to count the total number of worksheets, use Worksheets instead of Sheets. In most cases, people only use worksheets, using Sheets works fine. In layman terms, Sheets = Worksheets + Chart Sheets_

Below are the steps to put this code in the VBA Backend:

1.  Click the Develope tab in the ribbon (don’t see the Developer tab – [click here](https://trumpexcel.com/excel-developer-tab/)
     to know how to get it)

![Click the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20178'%3E%3C/svg%3E)

2.  Click on Visual Basic icon

![Click on Visual Basic icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20178'%3E%3C/svg%3E)

3.  In the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
     that opens, click on ‘Insert’ option in the menu
4.  Click on Module. This will insert a new module for the workbook

![Insert a module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20335'%3E%3C/svg%3E)

5.  Copy and Paste the above VBA code in the code window of the module

![Copy and Paste the code to the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20318'%3E%3C/svg%3E)

6.  Place the cursor anywhere in the code and press the F5 key (or click the green play button in the toolbar)

![Run the macro - click on green play button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20206'%3E%3C/svg%3E)

The above steps would run the code and you will see a [message box](https://trumpexcel.com/vba-msgbox/)
 that shows the total number of worksheets in the workbook.

![Message Box showing sheet count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20186'%3E%3C/svg%3E)

Note: If you want to keep this code and reuse it in the future in the same workbook, you need to save the Excel file as a macro-enabled file (with a .XLSM extension). You will see this option when you try to save this file.

### Getting Sheet Count Result in Immediate Window

The [Immediate window](https://trumpexcel.com/vba-immediate-window/)
 gives you the result right there with a single line of code.

Below are the steps to get the count of sheets in the workbook using the immediate window:

1.  Click the Develope tab in the ribbon (don’t see the Developer tab – [click here](https://trumpexcel.com/excel-developer-tab/)
     to know how to get it)
2.  Click on Visual Basic icon

![Click on Visual Basic icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20178'%3E%3C/svg%3E)

3.  In the VB Editor that opens, you might see the Immediate Window already. If you don’t, click the ‘View’ option in the menu and then click on Immediate Window (or use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     – Control + G)

![Click on Immediate Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20389%20492'%3E%3C/svg%3E)

4.  Copy and paste the following line of code: _? ThisWorkbook.Sheets.Count_

![Code in the immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20155'%3E%3C/svg%3E)

5.  Place the cursor at the end of the code line and hit enter.

When you hit enter in Step 5, it executes the code and you get the result in the next line in the immediate window itself.

![Result in immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20369%20140'%3E%3C/svg%3E)

The number in the second line means there are three sheets in the workbook

### Formula to Get Sheet Count in the Worksheet

If you want to get the sheet count in a cell in any worksheet, using the formula method is the best way.

In this method, I will [create a custom formula](https://trumpexcel.com/user-defined-function-vba/)
 that will give me the total number of sheets in the workbook.

Below is the code that will do this:

Function SheetCount()  
SheetCount = ThisWorkbook.Sheets.Count  
End Function

You need to place this code in the module (just like the way I showed in the ” _VBA Code to Show Sheet Count in a Message Box_” section)

Once you have the code in the module, you can get the sheet count by using the below formula in any cell in the workbook:

\=SheetCount()

![Sheet count formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20190'%3E%3C/svg%3E)

Pro Tip: If you need to get the sheet count value often, I would recommend copying and pasting this formula VBA code in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. When you save a VBA code in the Personal Macro Workbook, it can be used on any Excel file on your system. In short, VBA codes in PMW are always available to you on your system.

_Also read: [Count Rows Using VBA](https://trumpexcel.com/excel-vba/count-rows/)
_

Count All Sheets in Another Workbook (Open or Closed)
-----------------------------------------------------

In the above example, I showed you how to count the number of sheets in the active workbook (the one where you’re working and where you added the VBA codes).

You can also tweak the code a little to get the sheet count in other workbooks (whether open or closed).

### Sheet Count in Another Open Workbook

Suppose I want to know the sheet count of an already open workbook – Example.xlsx

The below VBA code with do this:

Sub SheetCount()
MsgBox Workbooks("Example.xlsx").Sheets.Count
End Sub

And in case you want to get the result in the immediate window, you can use the below code.

? Workbooks("Example.xlsx").Sheets.Count

### Sheet Count from a Closed Workbook

In case you need to get the sheet count of a file that’s closed, you either need to open it and then use the above codes, or you can use VBA to first open the file, then count the sheets in it, and then close it.

The first step would be to get the full file location of the Excel file. In this example, my file location is “C:\\Users\\sumit\\OneDrive\\Desktop\\Test\\Example File.xlsx”

_You can get the full file path by right-clicking on the file and then clicking on the Copy Path option (or click on the Properties option)._

Below are the VBA codes to get the sheet count from the closed workbook:

Sub SheetCount()  
Application.DisplayAlerts = False  
Set wb = Workbooks.Open("C:\\Users\\sumit\\OneDrive\\Desktop\\Test\\Example File.xlsx")  
ShCount = wb.Sheets.Count  
wb.Close SaveChanges:=True  
Application.DisplayAlerts = True  
MsgBox ShCount  
End Sub

The above code first opens the workbook, then counts the total number of sheets in it, and then closes the workbook.

Since the code needs to do some additional tasks (apart from counting the sheets), it has some extra lines of code in it.

_The Application.DisplayAlerts = False_ part of the code makes sure that the process of opening a file, counting the sheets, and then closing the file is not visible to the user. This line stops the alerts of the Excel application. And at the end of the code, we set it back to True, so things get back to normal and we see the alerts from thereon.

Count All Sheets that Have a Specific Word In It
------------------------------------------------

One useful scenario of counting sheets would be when you have a lot of sheets in a workbook, and you only want to count the number of sheets that have a specific word in them.

For example, suppose you have a large workbook that has sheets for multiple departments in your company, and you only want to know the sheet count of the sales department sheets.

Below is the VBA code that will only give you the number of sheets that have the word ‘Sales’ in it

Sub SheetCount()  
Dim shCount As Long  
For Each sh In ThisWorkbook.Worksheets  
If InStr(1, sh.Name, "Sales", vbBinaryCompare) > 0 Then  
shCount = shCount + 1  
End If  
Next sh  
MsgBox shCount  
End Sub

Note that the code is case-sensitive, so ‘Sales’ and ‘sales’ would be considered different words.

The above uses an [IF condition](https://trumpexcel.com/if-then-else-vba/)
 to check the name of each sheet, and if the name of the sheet contains the specified word (which is checked using the [INSTR function](https://trumpexcel.com/excel-vba-instr/)
), it counts it, else it doesn’t.

So these are some simple VBA codes that you can use to quickly get a count of sheets in any workbook.

I hope you found this tutorial useful!

**Other Excel tutorials you may also find useful:**

*   [How to Insert New Worksheet in Excel (Easy Shortcuts)](https://trumpexcel.com/insert-new-worksheet-excel/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [How to Get the Sheet Name in Excel? Easy Formula](https://trumpexcel.com/get-sheet-name-excel/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [How to Delete Sheets in Excel (Shortcuts + VBA)](https://trumpexcel.com/delete-sheets-excel/)
    
*   [How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [Excel Tabs/Sheets Not Showing – How to Fix?](https://trumpexcel.com/excel-tabs-sheets-not-showing/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-sheets-excel/#respond)

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