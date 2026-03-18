# Convert Columns to Rows in Excel (5 Simple Ways)

**Source:** https://trumpexcel.com/convert-columns-to-rows-excel

---

[Skip to content](https://trumpexcel.com/convert-columns-to-rows-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-columns-to-rows-excel/#below-title)

Most of the time, when working with Excel, you need to restructure your data before you can start any kind of analysis.

One common task many Excel users have to do is convert columns into rows in their existing dataset.

This is usually the case when you get your data set from a database or the web, and you need to [transpose the data](https://trumpexcel.com/transpose-data-excel/)
 so that the columns data is shown in rows and rows data in columns.

In this tutorial, I will show you some easy methods you can use to **convert columns to rows in Excel** quickly. I will be covering the inbuilt functionalities such as paste special, a simple keyboard shortcut, and the TRANSPOSE function to do these.

I will also give you a simple VBA code that you can use to convert columns to rows in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-columns-to-rows-excel/#)

Convert Columns to Rows Using Right-Click Options
-------------------------------------------------

One of the easiest ways to convert columns to rows is by copying the data and then transposing the data and pasting it somewhere else.

The option to paste your data as the transposed version of the original data can be accessed with a simple right-click.

Let me show you how it works.

Below is a data set where I have the Quarterly sales values shown in rows, and the Country sales values are shown in a column.

![Dataset to change columns to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20211'%3E%3C/svg%3E)

I need to transpose this data so that the Quarterly values are shown in a column, and the Country-wise values are shown in a row.

Here are the steps to do this:

1.  Select the entire dataset
2.  Copy the dataset. You can use the keyboard shortcut Control + C or right-click and click the Copy option.

![Click the Copy option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20491'%3E%3C/svg%3E)

3.  Right-click on the cell where you want to transpose and paste this data. In this example, I will paste it into cell A7.
4.  Go to the Paste Special option and hover the cursor over the More Options arrow.

![hover the cursor over the more options arrow.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20588'%3E%3C/svg%3E)

5.  Click on the Transpose Option

![Click on the Transpose option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20565'%3E%3C/svg%3E)

When you click the Transpose option, the copied data will be pasted, but the columns and rows will be interchanged.

![columns converted to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20637%20442'%3E%3C/svg%3E)

Here are a couple of important things to know about this method:

*   The pasted data retains the original [formatting from the copied data](https://trumpexcel.com/data-formatting-in-excel/)
    . In our example, the Country column remains to be in orange color and the Quarter row remains to be in blue.
*   If you have any formulas in the original data, those formulas would also be copied. If there are any [cell references used in those formulas](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
    , those references would be adjusted (if needed) to ensure that the formulas give you the right value.

One minor drawback of this method is that it will always copy everything from the original data and paste it into the transposed data (including the formatting, formulas, [comments](https://trumpexcel.com/insert-delete-comments-excel/)
/notes, and data validation). If you only want to copy the data without the formatting, you can’t do it with this method. But you can use the method I cover next.

Also read: [Text to Columns in Excel](https://trumpexcel.com/excel-text-to-columns-examples/)

Convert Columns to Rows Using Paste Special Dialog Box
------------------------------------------------------

Another quick way to convert columns to rows is by using the in-built Paste Special dialog box.

As you will see, the Paste Special dialog box gives more control over what we can paste.

Below I have the same data set, and I want to convert the columns into rows.

![Dataset to change columns to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20211'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select and copy the entire data (A1:E5 in our example)
2.  Right-click on the cell where you want to paste the copy data, and then click on the Paste Special option. This will open the Paste Special dialog box.

![Click on the Paste Special option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20436'%3E%3C/svg%3E)

3.  In the Paste Special dialog box, click on the **Transpose** option.

![Select the transpose option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20414'%3E%3C/svg%3E)

4.  Click Ok

The above steps would copy the original data and then paste the transposed version of that data (where the columns data have been put in rows and the rows data has been put in columns).

The additional benefit of using the Paste Special dialog box is that it allows you to choose what you want to paste into the transpose data.

For example, you can choose only to paste the values or only paste formulas or only paste the formatting or comments/notes.

To do this, you need to make an additional selection from the Paste options (highlighted below).

![Paste options in paste special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20414'%3E%3C/svg%3E)

While the ‘All’ option is selected by default, you can select the following:

*   **Formulas** – to only paste formulas from the copied data
*   **Value** – to only paste values from the copied data (without any formula or formatting)
*   **Formats** – to only paste the formatting without any data
*   **Comments and Notes** – to only paste the comments or notes in the cells
*   **Validation** – to only paste the validation rules or [drop-down lists](https://trumpexcel.com/excel-drop-down-list/)
    
*   **Values and Number Formats** – to paste the values as well as the number formatting that is applied to those values

**Note**: In case you want to convert columns into rows and paste multiple things such as values as well as comments/notes, you will have to repeat this process two times – i.e., the first time, you only copy the values and the second time, you copy only Comments/Notes

Also read: [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)

Convert Columns to Rows Using Keyboard Shortcut
-----------------------------------------------

If converting columns to rows is something you need to do quite often, I suggest you learn the keyboard shortcut to do it.

Personally, I find the [keyboard shortcut to paste the transposed data](https://trumpexcel.com/excel-paste-special-shortcuts/)
 to be the fastest way to do this.

So let me give you all the shortcuts (they are pretty easy to remember when you get used to them).

### Windows Paste Special Shortcut

Below is the shortcut to copy the data and and paste the transposed version of it (where columns are converted to rows)

ALT + E + S + E + Enter

Here is how to use this shortcut:

1.  Copy the data set that you want to transpose
2.  Go to the destination cell where you want to paste the data
3.  Press the following keys one after the other – **ALT + E + S + E + Enter**

In case you do not want to paste the entire data set and only want to paste the values or formats or comments notes etc., you can use the below shortcuts:

*   ALT + E + S + V + E + Enter – pastes only the values
*   ALT + E + S + F + E + Enter – pastes only the formulas
*   ALT + E + S + T + E + Enter – pastes only the formatting
*   ALT + E + S + C + E + Enter – pastes only the comments and notes
*   ALT + E + S + N + E + Enter – pastes only the data validation

### Mac Paste Special Shortcut

If you’re using a Mac, you can use the below shortcut to open the paste special dialog box.

Control + Command + V

Once the dialog box opens, you can make the needed selection and then click on the OK button.

Also read: [Flip Data in Excel | Reverse Order of Data in Column/Row](https://trumpexcel.com/flip-data-in-excel/)

TRANSPOSE Function to Convert Columns to Rows
---------------------------------------------

Another method you can use to convert columns to rows is by using the TRANSPOSE function in Excel.

Let me explain how it works.

Below is a data set where I want to convert the columns into rows.

![Dataset to change columns to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20211'%3E%3C/svg%3E)

Here is the TRANSPOSE formula I can use to do this:

\=TRANSPOSE(A1:E5)

Enter this formula in the cell where you want to get the transposed data. In my example, I have entered this data in cell A7.

![TRANSPOSE function to convert columns to rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20473'%3E%3C/svg%3E)

When you use the Transpose function, any blank cell in the original data set will return a zero in the resulting data set (as you can see in cell A7).

If you do not want a zero and want a blank instead, then you can use the modified formula mentioned below.

\=IF(TRANSPOSE(A1:E5)=0,"",TRANSPOSE(A1:E5))

![IF and TRANSPOSE function to convert columns to rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20471'%3E%3C/svg%3E)

Here are a couple of things you should know about using the TRANSPOSE formula:

*   The resulting data that you get is an array that is linked to the original data set. So if you make any changes in the original data set, it will automatically be reflected in the resulting data.
*   If you want to delete the original data set, you would first have to [convert the formula result into static values](https://trumpexcel.com/convert-formulas-to-values-excel/)
     so that it is no longer linked to the original data set. If you don’t do this and delete the original data set, you will get 0 in all cells.
*   TRANSPOSE formula would only transpose the values, and the formatting of the original dataset would not be copied.
*   When using the Transpose function, ensure that there are enough empty cells that can accommodate the result of the function. In case any of the cells are already filled, you will get a #SPILL! error

Also read: [Excel Filter Function - Examples + Video](https://trumpexcel.com/filter-function/)

VBA Code to Convert Columns to Rows
-----------------------------------

If you are more of a VBA person, let me give you the code that you can use to convert columns to rows quickly.

Below is the VBA code to do this:

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub ConvertColumnsToRows()
    
        Dim SourceRange As Range
        Dim TargetCell As Range
    
        'Ask the user to select the source range
        On Error Resume Next
        Set SourceRange = Application.InputBox("Select the range to transpose:", Type:=8)
        On Error GoTo 0
    
        'Exit the sub in case no range selected
        If SourceRange Is Nothing Then
            MsgBox "No range selected. Exiting.", vbInformation
            Exit Sub
        End If
    
        'Ask the user to select the destination cell
        On Error Resume Next
        Set TargetCell = Application.InputBox("Select the destination cell:", Type:=8)
        On Error GoTo 0
    
        'If no cell is selected, exit the sub
        If TargetCell Is Nothing Then
            MsgBox "No destination cell selected. Exiting.", vbInformation
            Exit Sub
        End If
    
        'Convert Columns to Rows and give result in destination cell
        SourceRange.Copy
        TargetCell.PasteSpecial Paste:=xlPasteAll, Operation:=xlNone, SkipBlanks:=False, Transpose:=True
    
        'Clean up
        Application.CutCopyMode = False
        Set SourceRange = Nothing
        Set TargetCell = Nothing
    
    End Sub

When you run the above code, it will ask you to select the range of cells that you want to transpose, and then it will ask you to select the destination cell where you should give the result.

Below are the steps to use this code in Excel:

1.  Open the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
    . You can either click on the Visual Basic option in the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
    , or you can use the shortcut ALT + F11 (Where you need to hold the Alt key and then press the F11 key)
2.  In the VB Editor, click on the Insert option and then click on Module. This will insert a new module where we are going to copy and paste the above VBA code.
3.  Copy and paste the code above into the module window.
4.  Close the VBA editor.
5.  Press ALT + F8, select the ‘ConvertColumnsToRows’ macro in the Macro dialog box, and then click ‘Run’. The macro will then guide you to make the selections and give the result in the destination cell.

Here are a couple of things to know when using a VBA code to convert columns to rows in Excel:

*   If you want to reuse the code in the same workbook, save the file as a macro-enabled file (with .XLSM file extension)
*   Changes done by a VBA macro cannot be undone, so it’s always a good idea to create a backup copy before running the macro code.
*   In case you want to use this code in all of your workbooks, then you need to save this in the Personal Macro Workbook. I explain how to do this [in this tutorial here](https://trumpexcel.com/personal-macro-workbook/)
    . Once you have saved the code in your Personal Macro Workbook, you will be able to access it from any workbook on your system.

So these are five methods you can use to quickly convert columns to rows in Excel. The easiest way to do this is by using the Paste Special dialog box, It also exists it also gives you a lot more control over what you want me to be a copy and pasted in the transposed data.

You can also use the in-built TRANSPOSE function or the VBA code to get this done.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Move Rows and Columns in Excel](https://trumpexcel.com/move-rows-columns/)
    
*   [How to Group Columns in Excel?](https://trumpexcel.com/group-columns-excel/)
    
*   [How to Swap Cells in Excel?](https://trumpexcel.com/swap-cells-excel/)
    
*   [Split Text into Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)
    
*   [Row vs Column in Excel – What’s the Difference?](https://trumpexcel.com/row-vs-column-excel/)
    
*   [Delete Blank Columns in Excel](https://trumpexcel.com/delete-blank-columns-excel/)
    
*   [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)
    
*   [Repeat Rows N Times in Excel](https://trumpexcel.com/repeat-rows-excel/)
    
*   [Select Every Other Column in Excel](https://trumpexcel.com/select-alternate-columns-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-columns-to-rows-excel/#respond)

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