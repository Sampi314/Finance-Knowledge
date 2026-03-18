# Transpose Multiple Rows into One Column (4 Easy Ways)

**Source:** https://trumpexcel.com/transpose-multiple-rows-into-one-column

---

[Skip to content](https://trumpexcel.com/transpose-multiple-rows-into-one-column/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/transpose-multiple-rows-into-one-column/#below-title)

Recently, I was working on a project where I had data in multiple rows, and I needed to combine the multiple rows and get the result in one single column.

There are multiple ways to do this in Excel.

If you’re using Excel with Microsoft 365, there is a dedicated formula to do this, and if you’re using an older version of Excel, you can do this using a combination of functions, Power Query or VBA.

Let’s see how to do this.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/4jq22vl4um9wv6f4uelmd/Transpose-Multiple-Rows-into-One-Column.xlsm?rlkey=o31y7upwbybx5de1qre07xamh&dl=1)
_**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/transpose-multiple-rows-into-one-column/#)

Using TOCOL Function
--------------------

Below, I have a data set where I have some names in multiple rows, and I want to combine all these names and then [transpose them](https://trumpexcel.com/transpose-data-excel/)
 to get all the data in one column (as shown in column E).

![Transpose multiple rows into one column example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20363'%3E%3C/svg%3E)

Excel’s **TCOL function** is perfect for this kind of scenario. It’s only available for Excel with Microsoft 365, though.

Below is the formula that would do this:

\=TOCOL(A1:C4)

![TOCOL formula to get rows in a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20506%20413'%3E%3C/svg%3E)

The above function takes the array as the input, combines all the rows, and gives the result in one single column.

And there is more you can do with this function.

If you want to combine this data by columns (instead of rows as we did above), you can use the below formula:

\=TOCOL(A1:C4,,TRUE)

By specifying the third argument as TRUE, I force the function to combine the data by columns instead of rows. If I omit this argument, by default, it becomes FALSE, and data is combined by rows.

And wait… there is more.

In case there are blanks or errors in your data set, and you do not want them to be part of your result, you can use the second argument.

*   0 – This is the default value, and it ignores nothing
*   1 – ignores blank cells
*   2 – ignores cells with errors
*   3 – ignores cells with errors and blanks

So, if you have a data set that can have blank cells or errors, you can use the below formula:

\=TOCOL(A1:C4,3)

I love these new [Excel functions](https://trumpexcel.com/excel-functions/)
. It makes life so much easier.

Excel also has a TOROW function that combines different columns and gives you the result in one single row.

Also read: [Split Text into Multiple Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)

Using INDEX with INT, COLUMNS, and MOD
--------------------------------------

If you’re not using Excel with Microsoft 365 (which you totally should be), you will have to use a much more complicated formula to transpose multiple rows into one column.

Below, I have a data set with names in three rows. I want to combine and transpose these multiple rows and get the result in one column.

![Transpose multiple rows into one column dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20141'%3E%3C/svg%3E)

Below is the formula to do this:

\=[INDEX](https://trumpexcel.com/excel-index-function/)
($A$1:$C$4,1+INT((ROW(A1)-1)/COLUMNS($A$1:$C$4)),MOD(ROW(A1)-1+COLUMNS($A$1:$C$4),COLUMNS($A$1:$C$4))+1)

Enter this formula in a cell where you want the result and then drag it down to get all the names in the column.

![Index formula to get multiple rows in a column as transposed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20361'%3E%3C/svg%3E)

In case there are [blank cells](https://trumpexcel.com/select-blank-cells-in-excel/)
 or errors in the selected data set, you will have to adjust the formula to handle those.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/4jq22vl4um9wv6f4uelmd/Transpose-Multiple-Rows-into-One-Column.xlsm?rlkey=o31y7upwbybx5de1qre07xamh&dl=1)
_**

Using Power Query Unpivot Feature
---------------------------------

This is also the perfect use case for the [unpivot feature in Power Query](https://trumpexcel.com/unpivot-data/)
.

Even if you do not have the latest version of Microsoft Excel, there’s a good chance you already have Power Query baked into your system. If you’re using Excel 2010 or 2013, you can download it as an add-in.

Below, I have a data set with names in three rows. I want to combine and transpose these multiple rows and get the result in one column.

![Transpose multiple rows into one column dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20141'%3E%3C/svg%3E)

Here are the steps to do this using Power Query:

1.  Select the names data set
2.  Click the Data tab

![Click the data tab in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20223'%3E%3C/svg%3E)

3.  In the Get & Transform Data group, click on the _From Table/Range_ icon.

![Click on from table or range icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20223'%3E%3C/svg%3E)

4.  If your data is not already in an [Excel table](https://trumpexcel.com/excel-table/)
    , this will open the Create Table dialog box. Check the range and click Ok. If your data has headers, check the My table has headers option.

![Create table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20161'%3E%3C/svg%3E)

5.  In the Power Query editor that opens, select all the columns
6.  Click on the _Transform_ tab

![Click on the transform tab in power query editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20172'%3E%3C/svg%3E)

7.  Click on the _Unpivot Columns_ option. As soon as you click on it, your data will transform, and you will now have two columns: _Attribute_ and _Value_.

![Click on unpivot columns option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20140'%3E%3C/svg%3E)

8.  Delete the Attribute column (right click and then click on Remove).
9.  Rename the Values column to Names.

![Rename the column to names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20441'%3E%3C/svg%3E)

10.  Click on the File tab and then click on _Close and Load to_ option

![Click on close and load to](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20388'%3E%3C/svg%3E)

11.  In the _Import_ dialog box, select the _Existing Worksheet_ option and then select the cell where you want to get the result. In this case, I am going to select cell E1.

![Select a cell in the existing worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20351'%3E%3C/svg%3E)

12.  Click OK

The above steps combine the data from multiple rows, then transpose it and give you the result in one column.

![multiple rows transformed into one column with pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20396'%3E%3C/svg%3E)

Also read: [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)

Using VBA Code
--------------

Another way to do this is by using a VBA subroutine that does all the heavy lifting in the back end and gives you the result right away.

Below is the VBA code to do this:

    'Code developed by Sumit Bansal from https://trumpexcel.com
    
    Sub CombineMultipleRowsToColumn()
        Dim inputRange As Range
        Dim outputCell As Range
        Dim result() As Variant
        Dim cell As Range
        Dim i As Long
        
        ' Prompt user to select the input range
        On Error Resume Next
        Set inputRange = Application.InputBox("Please select the range with data in multiple rows:", "Select Range", Type:=8)
        On Error GoTo 0
        
        ' Check if user cancelled the selection
        If inputRange Is Nothing Then
            MsgBox "Operation cancelled.", vbInformation
            Exit Sub
        End If
        
        ' Resize the result array based on the input range size
        ReDim result(1 To inputRange.Cells.Count)
        
        ' Loop through each cell in the input range
        i = 1
        For Each cell In inputRange.Cells
            If cell.Value <> "" Then
                result(i) = cell.Value
                i = i + 1
            End If
        Next cell
        
        ' Resize the array to remove any empty elements
        ReDim Preserve result(1 To i - 1)
        
        ' Transpose the result
        result = WorksheetFunction.Transpose(result)
        
        ' Prompt user to select the output cell
        On Error Resume Next
        Set outputCell = Application.InputBox("Please select the cell where you want to output the result:", "Select Output Cell", Type:=8)
        On Error GoTo 0
        
        ' Check if user cancelled the selection
        If outputCell Is Nothing Then
            MsgBox "Operation cancelled.", vbInformation
            Exit Sub
        End If
        
        ' Output the result to the selected cell
        outputCell.Resize(UBound(result), 1).Value = result
        
        MsgBox "Data has been combined and transposed successfully!", vbInformation
    End Sub

Here are the steps to use this code by putting it in the VB editor:

1.  Hold the Alt key and then press the F11 key. This will open the VB editor. Alternatively, you can click on the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon.
2.  In the VB editor, click on the Insert option in the menu.
3.  Click on the Module option. This will insert a new module for the active workbook.
4.  Copy and paste the above VBA subroutine code into the Module code window.
5.  Place the cursor anywhere in the code and then press the F5 on your keyboard or click on the Run Sub/Userform icon in the toolbar.

When you run the above VBA code, it will first ask you to select the range that has the names, and then it will ask you to select the cell where you want to get the result.

When the VBA code is done, you’ll see a [message box](https://trumpexcel.com/vba-msgbox/)
 saying _Data has been completed and transposed successfully_!

![Message box after vba has completed transposing multiple rows into single column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20208'%3E%3C/svg%3E)

Note: If you want to keep the VBA code in the workbook so that you can reuse it later, you need to save the Excel file as a macro-enabled file (with .xlsm extension)

In this article, I showed you how to transpose data from multiple rows into one column in Excel using built-in functions, Power Query, and VBA.

While it’s super easy to do with the new version of Excel (with M365) that has the TOCOL function, if you do not have this function, you can easily use the Power Query or the VBA method.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [Text to Columns in Excel](https://trumpexcel.com/excel-text-to-columns-examples/)
    
*   [Copy Paste Formulas without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [Flip Data in Excel](https://trumpexcel.com/flip-data-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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