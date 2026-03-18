# Remove Duplicates Within a Cell in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/remove-duplicates-from-cell-excel

---

[Skip to content](https://trumpexcel.com/remove-duplicates-from-cell-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-duplicates-from-cell-excel/#below-title)

Removing duplicates is a common task for most data workers.

While in most cases, you would be working on removing duplicates from a range of cells, sometimes, you may need to remove duplicates from a cell.

For example, below, I have a dataset with duplicate values in each cell and I want to remove the duplicates and keep only the unique ones.

![Dataset with Duplicates within a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20146'%3E%3C/svg%3E)

This can quickly be done with a simple formula if you have the new version of Excel that includes functions such as UNIQUE and TEXTSPLIT. If you don’t have these functions in your [Excel version](https://trumpexcel.com/excel-version/)
, you can use the VBA method I cover in this article.

Let’s get to these methods now.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-duplicates-from-cell-excel/#)

Formula to Remove Duplicates Within a Cell
------------------------------------------

The [new functions Excel](https://trumpexcel.com/advanced-excel-functions-formulas/)
 has released are amazing and do a lot of heavy lifting.

If you’re using Excel with Microsoft 365, you can use these new functions to remove duplicates from a cell.

Below, I have a dataset where I want to remove the duplicate values (regional name, item name, or person name) from A2:A4.

![Dataset with Duplicates within a cell for formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20896%20146'%3E%3C/svg%3E)

Note that all these items are separated by a comma followed by a space character, and this is something we can use to split all these items and then get rid of the duplicates.

Below is the formula that will work in our case:

\=TEXTJOIN(", ",TRUE,UNIQUE(TEXTSPLIT(A2,,", "))) 

![Formula to remove duplicates from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201095%20199'%3E%3C/svg%3E)

The above formula uses TEXTSPLIT(A2,”, “) to split the content of the cell into separate rows (in a column) using “, ” as the delimiter.

The result of the TEXTSPLIT function is then used within the UNIQUE function to give us only the unique values from the list.

The result of the UNIQUE function is then used within the TEXTJOIN function that combines the result using the specified delimiter (which is “, ” in our example).

In the final result, the duplicates have been removed.

For this formula to work, it is important to ensure that the delimiter is consistent. For example, in our case, all the items in the cells were separated by a comma followed by a space.

If the delimiter is inconsistent, with spaces present in some cases and not present in others, you can use the below formula. It uses the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 to remove leading and trailing spaces.

\=TEXTJOIN(", ",TRUE,UNIQUE(TRIM(TEXTSPLIT(A2,,","))))

![Formula to remove duplicates from a cell with inconsistent delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201146%20202'%3E%3C/svg%3E)

The formula covered in this section is not case-sensitive, so it would consider ‘_US_‘ and ‘_us_‘ as the same and treat them as duplicates.

Also read: [Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)

### Remove Duplicates with Multiple Delimeters

If you have items in a cell separated by more than one type of delimiter, you can still use the above formula with a small tweak.

Below, I have a dataset, and I want to remove duplicate values from within the cell:

![Dataset with inconsistent delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20721%20141'%3E%3C/svg%3E)

As you will notice, this example has four different types of delimiters: _comma, pipe symbol, dash, and semi-colon_.

In this situation, you can use the below formula:

\=TEXTJOIN(", ",TRUE,UNIQUE(TRIM(TEXTSPLIT(A2,,{",","-","|",";"}))))

![Formula to remove duplicates from a cell with inconsistent delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20875%20238'%3E%3C/svg%3E)

The above formula uses all these delimiters within curly brackets inside the TEXTSPLIT function. This way, the formula assesses each cell for all four delimiters, and each of these is used to split the content of the cells.

VBA Custom Function to Remove Duplicates Within a Cell
------------------------------------------------------

If you do not have access to these new functions, you can create your own custom function using VBA. It’s called a User Defined Function (UDF).

Below is the VBA code to create the function:

    Function DeDupCells(Cellref As String, Optional Delimiter As String = ", ") As String
        Dim Item
        With CreateObject("Scripting.Dictionary")
            .CompareMode = vbTextCompare
            For Each Item In Split(Cellref, Delimiter)
                If Trim(Item) <> "" And Not .exists(Trim(Item)) Then .Add Trim(Item), Nothing
        Next
        If .Count > 0 Then DeDupCells = Join(.keys, Delimiter)
       End With
    End Function

To use this VBA function, you will have to put this VBA code in a module in the VB Editor in your Excel file.

### Where to Put the VBA Code?

Here are the steps to do this so you can use this VBA custom function in the worksheet in Excel:

1.  Press Alt + F11 to open the [Visual Basic for Applications editor](https://trumpexcel.com/visual-basic-editor/)
    . You can also click on the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon to open the VB editor.
2.  In the VB editor, go to the menu, click on Insert, and then click on Module. This will create a new module for the Excel file where you can write the code for a custom VBA function.

![Insert a new Module in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20212'%3E%3C/svg%3E)

3.  In the new module window, copy and paste the above VBA code.

![Copy paste the VBA code in module to create function to remove duplicates from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20223'%3E%3C/svg%3E)

4.  Close the VB Editor.

### Using the Custom Function in Worksheet

When you’re done with the above steps, you can now use the custom function we have created as any other regular function within the cells in your worksheet.

I can use the below formula to remove duplicates from the cell:

\=DeDupCells(A2)

![Using Dedupcells formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20925%20217'%3E%3C/svg%3E)

In the VBA code that I have used to create this formula, I have already specified the delimiter as “, “.

In case you want to use any other delimiter, you can use that as the second argument. For example, below, I have a dataset where values are separated by a pipe symbol.

![Dataset with Pipe as the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20106'%3E%3C/svg%3E)

In this case, you can use the below formula:

![VBA custom formula with delimter to remove duplicate from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%20146'%3E%3C/svg%3E)

Note: Since your Excel file now contains a VBA code, you must save it as a macro-enabled file with a .xlsm extension. This will preserve the code in your file, and you can use this function in the future.

In this article, I showed you two methods you can use to remove duplicates within a cell in Excel using formulas. If you’re using a newer version of Excel that has new functions, such as UNIQUE and TEXTSPLIT, you can use the first method that uses a formula with these functions.

If you do not have access to these functions, you can use my second method, in which I showed you how to create your own custom function using VBA.

I hope you found this article helpful.

If you have any feedback or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)
    
*   [Remove Duplicate Values in Excel Using VBA](https://trumpexcel.com/excel-vba/remove-duplicate-values/)
    
*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    
*   [How to Filter Cells that have Duplicate Text Strings (Words) in it](https://trumpexcel.com/duplicate-text-strings/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-duplicates-from-cell-excel/#respond)

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