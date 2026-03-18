# Flip Data in Excel | Reverse Order of Data in Column/Row

**Source:** https://trumpexcel.com/flip-data-in-excel

---

[Skip to content](https://trumpexcel.com/flip-data-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/flip-data-in-excel/#below-title)

Sometimes, you may have a need to flip the data in Excel, i.e., to reverse the order of the data upside down in a vertical dataset and left to right in a horizontal dataset.

Now, if you’re thinking that there must be an inbuilt feature to do this in Excel, I’m afraid you’d be disappointed.

While there are multiple ways you can flip the data in Excel, there is no inbuilt feature. But you can easily do this using simple a sorting trick, formulas, or VBA.

In this tutorial, I will show you how to flip the data in rows, columns, and tables in Excel.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/flip-data-in-excel/#)

Flip Data Using SORT and Helper Column
--------------------------------------

One of the easiest ways to reverse the order of the data in Excel would be to use a helper column and then use that helper column to [sort the data](https://trumpexcel.com/sort-excel/)
.

### Flip the Data Vertically (Reverse Order Upside Down)

Suppose you have a data set of names in a column as shown below and you want to flip this data:

![Vertical Dataset to Flip](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20588'%3E%3C/svg%3E)

Below are the steps to flip the data vertically:

1.  In the adjacent column, enter ‘Helper’ as the heading for the column
2.  In the helper column, enter a series of numbers (1,2,3, and so on). You can use the [methods shown here](https://trumpexcel.com/number-rows-in-excel/)
     to do this quickly![Helper column for flipping vertical data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20704%20591'%3E%3C/svg%3E)
3.  Select the entire data set including the helper column
4.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20200'%3E%3C/svg%3E)
5.  Click on the Sort icon![Click the Sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20200'%3E%3C/svg%3E)
6.  In the Sort dialog box, select ‘Helper’ in the ‘Sort by’ dropdown![Select Helper column for sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20338'%3E%3C/svg%3E)
7.  In the Order drop-down, select ‘Largest to Smallest’![Select Largest to Smallest sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20338'%3E%3C/svg%3E)
8.  Click OK

The above steps would sort the data based on the helper column values, which would also lead to reversing the order of the names in the data.

![Data flipped vertically](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20711%20593'%3E%3C/svg%3E)

Once done, feel free to delete the helper column.

_In this example, I’ve shown you how to flip the data when you just have one column, but you can also use the same technique if you have an entire table. Just make sure that you select the entire table and then use the helper column to sort the data in descending order._

Also read: [How to Move Columns in Excel](https://trumpexcel.com/move-rows-columns/)

### Flip the Data Horizontally

You can also follow the same methodology to flip the data horizontally in Excel.

Excel has an option to sort the data horizontally using the Sort dialog box (the ‘Sort left to right’ feature).

Suppose you have a table as shown below and you want to flip this data horizontally.

![Horizontal Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%2062'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In the row below, enter ‘Helper’ as the heading for the row
2.  In the helper row, enter a series of numbers (1,2,3, and so on).![Horizontal Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%2062'%3E%3C/svg%3E)
3.  Select the entire data set including the helper row
4.  Click the Data tab
5.  Click on the Sort icon
6.  In the Sort dialog box, click on the Options button.![Click the Option button in Sort dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20738%20338'%3E%3C/svg%3E)
7.  In the dialog box that opens, click on ‘Sort left to right’![click on Sort left ot right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20225%20222'%3E%3C/svg%3E)
8.  Click OK
9.  In the Sort by drop-down, select Row 3 (or whatever row has your helper column)![Select the helper row number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20738%20338'%3E%3C/svg%3E)
10.  In the Order drop-down, select ‘Largest to Smallest’![Select Largest to Smallest for sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20738%20338'%3E%3C/svg%3E)
11.  Click OK

The above steps would flip the entire table horizontally.

![Horizontal Data flipped](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20778%2087'%3E%3C/svg%3E)

Once done, you can remove the helper row.

Also read: [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)
 

Flip Data Using Formulas
------------------------

Microsoft 365 has got some new formulas that make it really easy to reverse the order of a column or a table in Excel.

In this section, I’ll show you how to do this using the SORTBY formula (if you’re using Microsoft 365), or the [INDEX formula](https://trumpexcel.com/excel-index-function/)
 (if you’re not using Microsoft 365)

### Using the SORTBY function (available in Microsoft 365)

Suppose you have a table as shown below and you want to flip the data in this table:

![Data to be flipped by SORTBY](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20403'%3E%3C/svg%3E)

To do this, first, copy the headers and place them where you would want the flipped table

![Copy the headers in a different place](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20404'%3E%3C/svg%3E)

Now, use the following formula below the cell in the left-most header:

\=SORTBY($A$2:$B$12,ROW(A2:A12),-1)

![SORTBY function to flip the data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20477'%3E%3C/svg%3E)

The above formula sorts the data and by using the result of the [ROW function](https://trumpexcel.com/excel-row-function/)
 as the basis to sort it.

The ROW function in this case would return an array of numbers that represents the row numbers in between the specified range (which in this example would be a series of numbers such as 2, 3, 4, and so on).

And since the third argument of this formula is -1, it would force the formula to sort the data in descending order.

The record that has the highest row number would come at the top and the one which has the lowest rule number would go at the bottom, essentially reversing the order of the data.

Once done, you can [convert the formula to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 to get a static table.

Also read: [How to Swap Cells in Excel?](https://trumpexcel.com/swap-cells-excel/)

### Using the INDEX Function

In case you don’t have access to the SORTBY function, worry not – you can use the amazing INDEX function.

Suppose you have a dataset of names as shown below and you want to flip this data.

![Single column data for index function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20404'%3E%3C/svg%3E)

Below is the formula to do this:

\=INDEX($A$2:$A$12,ROWS(A2:$A$12))

![INDEX function to flip 1 column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20481'%3E%3C/svg%3E)

 **How does this formula work?**

The above formula uses the INDEX function that would return the value from the cell based on the number specified in the second argument.

The real magic happens in the second argument where I have used the ROWS function.

Since I have locked the second part of the reference in the ROWS function, in the first cell, it would return the number of rows between A2 and A12, which would be 11.

But when it goes down the rows, the first reference would change to A3, and then A4, and so on, while the second reference would remain as is because I have [locked it and made it absolute](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
.

As we go down the rows, the result of the [ROWS function](https://trumpexcel.com/excel-rows-function/)
 would decrease by 1, from 11 to 10 to 9, and so on.

And since the INDEX function returns us the value based on the number in the second argument, this would ultimately give us the data in the reverse order.

You can use the same formula even if you have multiple columns in the data set. however, you will have to specify a second argument that would specify the column number from which the data needs to be fetched.

Suppose you have a data set as shown below and you want to reverse the order of the entire table:

![Two data column for index function sort](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20402'%3E%3C/svg%3E)

Below is the formula that will do that for you:

\=INDEX($A$2:$B$12,ROWS(A2:$A$12),COLUMNS($A$2:A2))

![INDEX formula to sort multiple columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20784%20479'%3E%3C/svg%3E)

This is a similar formula where I’ve also added a third argument that specifies the column number from which the value should be fetched.

To make this formula dynamic, I have used the [COLUMNS function](https://trumpexcel.com/excel-columns-function/)
 that would keep on changing the column value from 1 to 2 to 3 as you copy it to the right.

Once done, you can convert the formulas to values to make sure that you have a static result.

Note: When you use a formula to reverse the order of a data set in Excel, it would not retain the original formatting. If you need the original formatting on the sorted data as well, you can either apply it manually or [copy and paste the formatting](https://trumpexcel.com/excel-format-painter/)
 from the original data set to the new sorted dataset

Flip Data Using VBA
-------------------

If flipping the data in Excel is something you have to do quite often, you can also try the VBA method.

With a [VBA macro code](https://trumpexcel.com/excel-macro-examples/)
, you can copy and paste it once within the workbook in the VBA editor, and then reuse it over and over again in the same workbook.

You can also save the code in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
 or as an [Excel add-in](https://trumpexcel.com/excel-add-in/)
 and be able to use it in any workbook on your system.

Below is the VBA code that would flip the selected data vertically in the worksheet.

    Sub FlipVerically()
    
    'Code by Sumit Bansal from trumpexcel.com
    
    Dim TopRow As Variant
    Dim LastRow As Variant
    Dim StartNum As Integer
    Dim EndNum As Integer
    
    Application.ScreenUpdating = False
    
    StartNum = 1
    EndNum = Selection.Rows.Count
    
    Do While StartNum < EndNum
    TopRow = Selection.Rows(StartNum)
    LastRow = Selection.Rows(EndNum)
    Selection.Rows(EndNum) = TopRow
    Selection.Rows(StartNum) = LastRow
    StartNum = StartNum + 1
    EndNum = EndNum - 1
    Loop
    
    Application.ScreenUpdating = True
    End Sub

To use this code, you first need to make the selection of the data set that you want to reverse (excluding the headers), and then run this code.

**How does this code work?**

The above code first counts the total number of rows in the data set and assigns that to the variable EndNum.

It then uses the [Do While loop](https://trumpexcel.com/vba-loops/)
 where the sorting of the data happens.

The way it sorts this data is by taking the first and the last row and swapping these. It then moves to the 2nd row in the second last row and then swaps these. Then it moves to the third row in the third last row and so on.

The loop ends when all the sorting is done.

It also uses the Application.ScreenUpdating property and sets it to FALSE while running the code, and then turn it back to TRUE when the code has completed running.

This ensures that you don’t see the changes happening in real-time on your screen it also speeds up the process.

**How to use the Code?**

Follow the below steps to copy and paste this code in the VB Editor:

1.  Open the Excel file where you want to add the VBA code
2.  Hold the ALT key and press the F-11 key (you can also go to the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and click on the Visual Basic icon)
3.  In the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
     that opens up, there would be a Project Explorer on the left part of the VBA editor. If you don’t see it, click on the ‘View’ tab and then click on ‘Project Explorer’![Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20448'%3E%3C/svg%3E)
4.  Right-click on any of the objects for the workbook in which you want to add the code
5.  Go to the Insert option and then click on Module. This will add a new module to the workbook![Insert a module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20374%20556'%3E%3C/svg%3E)
6.  Double-click on the module icon in the Project Explorer. This will open the code window for that module
7.  Copy and paste the above VBA code into the code window![Copy paste the VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20578'%3E%3C/svg%3E)

To [run the VBA macro code](https://trumpexcel.com/run-a-macro-excel/)
, first select the dataset that you want to flip (excluding the headers).

With the data selected, go to the VB Editor and click on the green play button in the toolbar, or select any line in the code and then hit the F5 key

![Click the Macro run button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20112'%3E%3C/svg%3E)

So these are some of the methods you can use to flip the data in Excel (i.e., reverse the order of the data set).

All the methods that I have covered in this tutorial (formulas, SORT feature, and VBA), can be used to flip the data vertically and horizontally (you’ll have to adjust the formula and VBA code accordingly for horizontal data flipping).

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Sort by the Last Name in Excel (Easy Guide)](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [How to Sort By Color in Excel (in less than 10 seconds)](https://trumpexcel.com/sort-by-color/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [How to do a Multiple Level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Flip Data in Excel | Reverse Order of Data in Column/Row”
------------------------------------------------------------------------

1.  How do i set the range without having to select it again? I have the same couple ranges that I need it done for and they dont change
    
    [Reply](https://trumpexcel.com/flip-data-in-excel/#comment-37961)
    
2.  Please note that a typing mistake causes the macro not work  
    The following is the corrected code please  
    Sub FlipVerically()
    
    ‘Code by Sumit Bansal from trumpexcel.com  
    ‘Below is the VBA code that would flip the selected data vertically in the worksheet.  
    ‘https://trumpexcel.com/flip-data-in-excel/
    
    Dim TopRow As Variant  
    Dim LastRow As Variant  
    Dim StartNum As Integer  
    Dim EndNum As Integer
    
    Application.ScreenUpdating = False
    
    StartNum = 1  
    EndNum = Selection.Rows.Count
    
    Do While StartNum < EndNum  
    TopRow = Selection.Rows(StartNum)  
    LastRow = Selection.Rows(EndNum)  
    Selection.Rows(EndNum) = TopRow  
    'Selection.Rows(StartNum) = LastRowStartNum = StartNum + 1  
    Selection.Rows(StartNum) = LastRow  
    StartNum = StartNum + 1  
    EndNum = EndNum – 1  
    Loop
    
    Application.ScreenUpdating = True  
    End Sub
    
    [Reply](https://trumpexcel.com/flip-data-in-excel/#comment-36905)
    
    *   Thanks for letting me know. Copy pasting the code from VBA to WordPress messed it up. I have fixed it now
        
        [Reply](https://trumpexcel.com/flip-data-in-excel/#comment-36917)
        
3.  The conversion of data from top to bottom in excel is very nice. Thank you
    
    [Reply](https://trumpexcel.com/flip-data-in-excel/#comment-33414)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/flip-data-in-excel/#respond)

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