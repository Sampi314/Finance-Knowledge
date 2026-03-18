# How to Sort Worksheets in Excel using VBA (alphabetically)

**Source:** https://trumpexcel.com/sort-worksheets

---

[Skip to content](https://trumpexcel.com/sort-worksheets/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-worksheets/#below-title)

If you work with a lot of worksheets in Excel, you would know that management of it can become an issue.

Once you have more than a couple of worksheets, you need to manually arrange these.

How easy would it be had there been a way to quickly sort the worksheets alphabetically in Excel.

While there is no inbuilt feature way to do this, it can be done (easily) using VBA.

In this tutorial, I will give you the code and the exact steps you need to follow to sort worksheets in Excel.

You can tweak the code to sort the worksheets in an ascending or descending order.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-worksheets/#)

VBA code to Sort Worksheets in Excel (Alphabetically)
-----------------------------------------------------

Below is the code that will sort the worksheets in alphabetical order as soon as you run it.

Sub SortWorksheetsTabs()
Application.ScreenUpdating = False
Dim ShCount As Integer, i As Integer, j As Integer
ShCount = Sheets.Count

For i = 1 To ShCount - 1
    For j = i + 1 To ShCount
        If UCase(Sheets(j).Name) < UCase(Sheets(i).Name) Then
            Sheets(j).Move before:=Sheets(i)
        End If
    Next j
Next i

Application.ScreenUpdating = True
End Sub

The above is a simple code that uses to [For Next loops](https://trumpexcel.com/for-next-loop-excel-vba/)
 to analyze each worksheet against all the worksheets.

It compares the name of a worksheet against all the worksheets and moves it based on its name in alphabetical order.

It then moves on to the next worksheet and then checks it against all the worksheets.

This process is repeated for all the worksheets and the final result is an order of worksheets sorted in alphabetical order.

![Sort Worksheets in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20360'%3E%3C/svg%3E)

**A few important things to know about this code:**

1.  [UCase function](https://trumpexcel.com/vba-ucase/)
     is used to make sure that the lowercase and uppercase are not treated differently.
2.  The value of Application.ScreenUpdating is set to False at the beginning of the code and changed to True at the end of the code. This ensures that while the code is running, you don’t see it happening on the screen. This also helps speed up the code execution.

Sort Worksheets in Descending Order
-----------------------------------

If you want to sort worksheets in descending order, you only need to change the < (less than) sign with the > (greater than) sign.

The below code would sort the worksheets in descending order:

'This code will sort the worksheets alphabetically
Sub SortWorksheetsTabs()
Application.ScreenUpdating = False
Dim ShCount As Integer, i As Integer, j As Integer
ShCount = Sheets.Count
For i = 1 To ShCount - 1
    For j = i + 1 To ShCount
        If UCase(Sheets(j).Name) > UCase(Sheets(i).Name) Then
            Sheets(j).Move before:=Sheets(i)
        End If
    Next j
Next i
Application.ScreenUpdating = True
End Sub

Sort Worksheets in Ascending/Descending Order Based on User Input
-----------------------------------------------------------------

You can also give the user the option to choose whether he/she wants to sort in ascending/descending order.

The below code would show a [message box](https://trumpexcel.com/vba-msgbox/)
 and the user can select the order to sort.

Sub SortWorksheetsTabs()
Application.ScreenUpdating = False
Dim ShCount As Integer, i As Integer, j As Integer
Dim SortOrder As VbMsgBoxResult
SortOrder = MsgBox("Select Yes for Ascending Order and No for Descending Order", vbYesNoCancel)
ShCount = Sheets.Count
For i = 1 To ShCount - 1
For j = i + 1 To ShCount
If SortOrder = vbYes Then
    If UCase(Sheets(j).Name) < UCase(Sheets(i).Name) Then
        Sheets(j).Move before:=Sheets(i)
    End If
ElseIf SortOrder = vbNo Then
    If UCase(Sheets(j).Name) > UCase(Sheets(i).Name) Then
    Sheets(j).Move before:=Sheets(i)
    End If
End If
Next j
Next i
Application.ScreenUpdating = True
End Sub

The above code when executed shows a message as shown below. It sorts based on the selection (Yes for Ascending and No for Descending).

In case you click Cancel, the code stops and nothing happens.

![Message box when sorting worksheets in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20186'%3E%3C/svg%3E)

**Note**: The sorting cannot be undone. In case you want to keep the original order as well, make a copy of the workbook.

**A word of caution**: The above code works in most cases. One area where it will give you the wrong result is when you have tab names such as Q1 2018, Q2 2018, Q1 2019, and Q2 2019. Ideally, you would want all the tabs for the same years to be together, but it won’t be done as Q1 2019 will be placed before Q2 2018.

Where to Put the VBA Code
-------------------------

Excel has a VBA backend called the VBA editor.

You need to copy and paste the VBA code into the VB Editor module code window.

Here are the steps to do this:

1.  Click the ‘Developer’ tab. (Can’t see the developer tab? [Click here](https://trumpexcel.com/excel-developer-tab/)
     to learn how to get it).![Sort Worksheets in Excel - Developer Tab in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on Visual Basic option. This will open the VB editor in the backend.![Click on Visual Basic to open the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. (If you don’t see the Project Explorer go to the ‘View’ tab and click on ‘Project Explorer’.)
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![Insert a Module in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20497%20491'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.![Copy and Paste the code to sort worksheet tabs in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20753%20466'%3E%3C/svg%3E)

How to Run the VBA Code
-----------------------

In Excel, there are various ways to run the VBA code.

You can run the code right from the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
 (also called the VB Editor).

You can insert a button or a shape in the worksheet and assign the macro to it. When you click on the button, it will run the macro instantly.

You can also add the macro to the Quick Access Toolbar (QAT). Now whenever you have to sort the worksheet tabs, you can just click on the macro code icon in the QAT.

You can read all about running the macro here - [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
 (or watch the video below).

**You May Also Like the Following Excel/VBA Tutorials:**

*   [How to Sort Data in Excel using VBA.](https://trumpexcel.com/sort-data-vba/)
    
*   [How to Get the Sheet Name in Excel?](https://trumpexcel.com/get-sheet-name-excel/)
    
*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    .
*   [How to do a Multiple Level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    .
*   [An Introduction to Excel Data Sorting Options](https://trumpexcel.com/sort-excel/)
    .
*   [Excel VBA Autofilter: A Complete Guide with Examples](https://trumpexcel.com/vba-autofilter/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [How to Flip Data in Excel](https://trumpexcel.com/flip-data-in-excel/)
    
*   [VBA Protect and Unprotect Sheets](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [Sort Dates By Month in Excel](https://trumpexcel.com/sort-dates-by-month-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Sort Worksheets in Excel using VBA (alphabetically)”
--------------------------------------------------------------------------

1.  In both modules I get the following error message “Runtime Error ‘9’ Subscript out of range” at  
    If UCase(Sheets(j).Name) < UCase(Sheets(i).Name) Then  
    Sheets(j).Move before:=Sheets(i)  
    Can you explain, please
    
    [Reply](https://trumpexcel.com/sort-worksheets/#comment-12394)
    
2.  tank you very good
    
    [Reply](https://trumpexcel.com/sort-worksheets/#comment-10644)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-worksheets/#respond)

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