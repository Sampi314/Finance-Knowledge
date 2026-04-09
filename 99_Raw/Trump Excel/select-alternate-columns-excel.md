# Select Every Other Column in Excel

**Source:** https://trumpexcel.com/select-alternate-columns-excel

---

[Skip to content](https://trumpexcel.com/select-alternate-columns-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/select-alternate-columns-excel/#below-title)

Sometimes you may have a large dataset that you are working with in Excel and you want to select alternate columns, or every third or every fourth column in your dataset.

While there is no inbuilt feature to do this in Excel, there are some easy workarounds.

In this article, I’ll show you three ways to select every other column quickly, or every third or every fourth column.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/select-alternate-columns-excel/#)

Manually Select Columns Using Control Key
-----------------------------------------

If you have a small dataset, where you only want to select a couple of alternate columns, the easiest and the fastest way to do this will be to do it manually.

Below I have a dataset where I want to select every other column.

![Dataset to select alternate columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202184%20707'%3E%3C/svg%3E)

Here are the steps to do this.

1.  Select the first column by clicking on the column header.

![Select the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202180%201021'%3E%3C/svg%3E)

2.  Hold the Ctrl key on your keyboard and continue to hold it.
3.  One-by-one select all the columns that you want selected (while continuing to hold the Ctrl key).

![Alternate columns are selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202184%20863'%3E%3C/svg%3E)

4.  Once done with the selection, leave the Ctrl key.

_Pro Tip: If, by mistake, you select a column that you did not want selected, you can click on that column header again and it would [get deselected](https://trumpexcel.com/deselect-cells-in-excel/)
._

If you do not want to select the entire column but a specific range in each column (e.g., the first 10 cells or the first 20 cells), you can still use the same method by holding the Ctrl key and then one-by-one selecting the cells in the columns.

Extract Columns Using TOCOL Function
------------------------------------

If you wish to select every other column so that you can copy them and paste them somewhere else, you can use a formula to do this.

Below I have a dataset where I want to extract every other column and get the result in a separate sheet (or in the same sheet).

![Dataset to select alternate columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202184%20707'%3E%3C/svg%3E)

Here is the formula that will do this:

\=LET(  
rng,B1:M11,  
colgap,2,  
CHOOSECOLS(rng,SEQUENCE(,COLUMNS(rng)/colgap,,colgap)))

![Formula to extract alternate columns in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202190%201687'%3E%3C/svg%3E)

Enter this formula where we want the columns to be extracted.

Select Columns using VBA
------------------------

If you have a large dataset and selecting the columns manually or using a formula is not an option, you can also use a simple VBA code to do this.

Below is the VBA code that would select every Nth column in your dataset (where you can specify the column interval).

'Code by Sumit Bansal from https://trumpexcel.com  
  
Sub SelectColumns()  
    Dim selectedRange As Range  
    Dim intervalInput As String  
    Dim interval As Integer  
    Dim col As Range  
    Dim resultRange As Range  
    Dim i As Integer  
    Dim columnCount As Integer  
      
    ' Ask user to select a range  
    On Error Resume Next  
    Set selectedRange = Application.InputBox("Please select a range:", "Select Range", Type:=8)  
    On Error GoTo 0  
      
    ' Check if user cancelled  
    If selectedRange Is Nothing Then  
        MsgBox "No range selected. Operation cancelled.", vbInformation  
        Exit Sub  
    End If  
      
    ' Ask user for the interval  
    intervalInput = InputBox("Enter the column interval:" & vbCrLf & \_  
                            "2 = every 2nd column (alternate)" & vbCrLf & \_  
                            "3 = every 3rd column, etc.", "Column Interval")  
      
    ' Check if user cancelled  
    If intervalInput = "" Then  
        MsgBox "No interval specified. Operation cancelled.", vbInformation  
        Exit Sub  
    End If  
      
    ' Validate the interval input  
    If Not IsNumeric(intervalInput) Then  
        MsgBox "Please enter a valid number.", vbExclamation  
        Exit Sub  
    End If  
      
    interval = CInt(intervalInput)  
      
    ' Validate interval is positive  
    If interval < 1 Then  
        MsgBox "Interval must be 1 or greater.", vbExclamation  
        Exit Sub  
    End If  
      
    ' Build the range of columns to select  
    i = 1  
    columnCount = 0  
    For Each col In selectedRange.Columns  
        If (i - 1) Mod interval = 0 Then  
            If resultRange Is Nothing Then  
                Set resultRange = col  
            Else  
                Set resultRange = Union(resultRange, col)  
            End If  
            columnCount = columnCount + 1  
        End If  
        i = i + 1  
    Next col  
      
    ' Select the result range  
    If Not resultRange Is Nothing Then  
        resultRange.Select  
        MsgBox "Selected " & columnCount & " column(s) with interval of " & interval, vbInformation  
    Else  
        MsgBox "No columns to select.", vbInformation  
    End If  
End Sub

**How to use this code:**

1.  Press Alt + F11 to open the [VBA Editor](https://trumpexcel.com/visual-basic-editor/)
    
2.  Go to _Insert_ and then click on _Module_ to create a new module
3.  Paste the VBA code above
4.  Close the VBA Editor
5.  Run the macro by pressing Alt + F8, selecting _SelectColumns_ macro, and clicking _Run_

**How this VBA code works:**

*   First, it prompts you to select a range (you will see an input box and then you can select the range in which you want to select the columns)
*   Then it asks you to enter an interval number (2 for alternate, 3 for every third column, etc.)
*   It will select the 1st column, then every nth column after that based on the interval you specify. For example, with interval = 2, it will select every other column, with interval = 3, it will selects every third column.

The VBA code also includes validation to handle cancellations and invalid inputs.

In this article I have covered three ways to select every other column in Excel. You can choose the method that suits your condition the best.

**Other Excel articles you may also like:**

*   [Select Every Other Row in Excel](https://trumpexcel.com/select-every-other-row-excel/)
    
*   [Insert a Blank Row after Every Row in Excel (or Every Nth Row)](https://trumpexcel.com/insert-blank-row-after-every-row/)
    
*   [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)
    
*   [How to Group Columns in Excel?](https://trumpexcel.com/group-columns-excel/)
    
*   [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)
    
*   [How to Select Entire Column (or Row) in Excel – Shortcut](https://trumpexcel.com/select-entire-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/select-alternate-columns-excel/#respond)

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