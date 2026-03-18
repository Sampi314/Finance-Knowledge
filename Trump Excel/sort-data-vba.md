# How to Sort Data in Excel using VBA (Range/Columns)

**Source:** https://trumpexcel.com/sort-data-vba

---

[Skip to content](https://trumpexcel.com/sort-data-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-data-vba/#below-title)

Excel already has a couple of ways to [sort data](https://trumpexcel.com/sort-excel/)
 quickly.

You can easily sort a data set by using the sort icons in the ribbon or the sort dialog box.

![Sort Data options in the ribbon](https://trumpexcel.com/wp-content/uploads/2017/09/Sort-Data-options-in-the-ribbon.png)

Then why do you need to know how to do this using VBA?

Knowing how to sort data using VBA can be helpful when included as a part of your code. For example, suppose you get a data set daily/weekly that you need to format and sort in a specific order.

You can create a macro to do all this for you with a single click. That will save you a lot of time and effort every time you do it.

Also, if you [create Excel dashboards](https://trumpexcel.com/creating-excel-dashboard/)
, you can take Excel sorting capability to a new level by allowing the user to sort the data just by double-clicking on the header (as shown below).

![Sort Data Using VBA - Double Click Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20412'%3E%3C/svg%3E)

I will cover how to create this later in this tutorial. Let’s first quickly get the basics straight.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-data-vba/#)

Understanding the Range.Sort Method in Excel VBA
------------------------------------------------

When sorting using VBA, you need to use the Range.Sort method in your code.

The ‘Range’ would be the data that you’re trying to sort. For example, if you’re sorting the data in A1:A10, then ‘Range’ would be Range(“A1:A10”).

You can also create a [named range](https://trumpexcel.com/named-ranges-in-excel/)
 and use it instead of the cell references. For example, if I create a named range ‘DataRange’ for the cells A1:A10, then I can also use Range(“DataRange”)

With the sort method, you need to provide some additional information through parameters. Below are the key parameters you need to know:

*   **Key** – here you need to specify the column that you want to sort. For example, if you want to sort column A, you need to use key:=Range(“A1”)
*   **Order** – here you specify whether you want the sorting in an ascending order or the descending order. For example, if you want the sorting in ascending order, you will use Order:=xlAscending
*   **Header** – here you specify whether your data set has headers or not. If it has headers, the sorting starts from the second row of the data set, else it starts from the first row. To specify that your data has headers, you will use Header:=xlYes

While these three suffices in most of the cases, you can read more about the parameters [in this article](https://msdn.microsoft.com/en-us/vba/excel-vba/articles/range-sort-method-excel)
.

Now let’s see how to use the Range.Sort method in VBA to sort data in Excel.

Sorting a Single Column Without Header
--------------------------------------

Suppose you have a single column without header (as shown below).

![Data for sorting with VBA - without headers single column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20123%20343'%3E%3C/svg%3E)

You can use the below code to sort it in ascending order.

Sub SortDataWithoutHeader()
Range("A1:A12").Sort Key1:=Range("A1"), Order1:=xlAscending, Header:=xlNo
End Sub

Note that I have specified the data range manually as Range(“A1:A12”).

In case there might be changes in the data and values might be added/deleted, you can use the below code that automatically adjusts based on the filled cells in the dataset.

Sub SortDataWithoutHeader()
Range("A1", Range("A1").End(xlDown)).Sort Key1:=Range("A1"), Order1:=xlAscending, Header:=xlNo
End Sub

Note that instead of Range(“A1:A12”), I have used, Range(“A1”, Range(“A1”).End(xlDown)).

This will check the last consecutively filled cell in the column and include it in sorting. In case there are blanks, it will only consider data till the first blank cell.

You can also create a named range and use that named range instead of the cell references. For example, if the named range is DataSet, your code would now be as shown below.

Sub SortDataWithoutHeader()
Range("DataRange").Sort Key1:=Range("A1"), Order1:=xlAscending, Header:=xlNo
End Sub

Now let me quickly explain the parameters used in the above examples:

*   Key1:=Range(“A1”) – Specified A1 so that the code would know which column to sort.
*   Order1:=xlAscending – Specified the order as xlAscending. If you want it to be in the descending order, use xlDescending.
*   Header:= xlNo – Specified that there are no headers. This is also the default value. So even if you omit this, your data will be sorted considering it has no headers.

Wondering where to put this VBA code and how to run the macro? [Read this tutorial](https://trumpexcel.com/run-a-macro-excel/)
!

Sorting a Single Column With Header
-----------------------------------

In the previous example, the data set did not have a header.

When your data has headers, you need to specify that in the code so that the sorting can start from the second row of the dataset.

Suppose you have a dataset as shown below:

![Dataset to sort data using VBA in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20366'%3E%3C/svg%3E)

Below is the code that will sort the data in descending order based on the sales of the stores.

Sub SortDataWithHeader()
Range("DataRange").Sort Key1:=Range("C1"), Order1:=xlDescending
End Sub

Note that I have created a named range – ‘DataRange’, and used this named range in the code.

Sorting Multiple Columns With Headers
-------------------------------------

So far in this tutorial, we have seen how to sort a single column (with and without headers).

Now, what if you want to sort based on multiple columns.

For example, in the below data set, what if I want to first sort by the state code, and then by the store.

![Dataset to sort data using VBA in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20366'%3E%3C/svg%3E)

Here is the code that will sort multiple columns at one go.

Sub SortMultipleColumns()
With ActiveSheet.Sort
     .SortFields.Add Key:=Range("A1"), Order:=xlAscending
     .SortFields.Add Key:=Range("B1"), Order:=xlAscending
     .SetRange Range("A1:C13")
     .Header = xlYes
     .Apply
End With
End Sub

Below is the result that you will get.

![Sorting Multiple Columns Using VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20290%20367'%3E%3C/svg%3E)

In the above example, the data is first sorted by the state code (column A). Then within the state code data, it is again sorted by the Store (Column B). This order is determined by the code in which you mention it.

Sorting Data Using Double Click on Header
-----------------------------------------

If you’re creating a dashboard or want more ease of use in your reports, you can write a VBA code that will sort the data when you double click on the headers.

Something as shown below:

![Sort Data with VBA in Excel Using Double Click](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20292%20376'%3E%3C/svg%3E)

Below is the code that will allow you to do this:

Private Sub Worksheet\_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
Dim KeyRange As Range
Dim ColumnCount As Integer
ColumnCount = Range("DataRange").Columns.Count
Cancel = False
If Target.Row = 1 And Target.Column <= ColumnCount Then
Cancel = True
Set KeyRange = Range(Target.Address)
Range("DataRange").Sort Key1:=KeyRange, Header:=xlYes
End If
End Sub

Note that I have created a named range (“DataRange”) and have used it in the code instead of using the cell references.

As soon as you double-click on any of the headers, the code disables the usual double-click functionality (which is to get into the edit mode) and uses that cell as the key while sorting the data.

Also note that as of now, this code will sort all the columns in ascending order only.

Note that double-click is a trigger allows Excel to run the specified code. These triggers such as double-click, opening a workbook, [adding a new worksheet](https://trumpexcel.com/insert-new-worksheet-excel/)
, changing a cell, etc. are called events and can be used to run macros in Excel. You can read more about [Excel VBA events here](https://trumpexcel.com/vba-events/)
.

**Where to put this code?**

You need to paste this code into the code window of the sheet in which you want this double click sort functionality.

To do this:

*   Right-click on the sheet tab.
*   Click on View Code.
*   Paste the code in the code window of the sheet in which your data resides.

Now what if you want to sort the first two columns (‘State’ and ‘Store’) in ascending order, but ‘Sales’ column in descending order.

Here is the code that will do it:

Private Sub Worksheet\_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
Dim KeyRange As Range
Dim ColumnCount As Integer
ColumnCount = Range("DataRange").Columns.Count
Cancel = False
If Target.Row = 1 And Target.Column <= ColumnCount Then
Cancel = True
Set KeyRange = Range(Target.Address)
If Target.Value = "Sales" Then
SortOrder = xlDescending
Else
SortOrder = xlAscending
End If
Range("DataRange").Sort Key1:=KeyRange, Header:=xlYes, Order1:=SortOrder
End If
End Sub

In the above code, it checks if the cell that is double-clicked is the Sales header or not. If yes, then it assigns the xlDescending value to the variable SortOrder, else it makes it xlAscending.

Now let’s take this a notch further and show a visual Marker (arrow and colored cell) in the header when it is sorted.

Something as shown below:

![Sort Data Using VBA - Double Click Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20412'%3E%3C/svg%3E)

To get this, I have added a new worksheet and made the following changes in it (you can [download the example file](https://www.dropbox.com/s/zotao0kzk9lljgw/Sort-Data-Using-VBA.xlsm?dl=1)
 and follow along):

*   Changed the name of the new sheet to ‘BackEnd’.
*   In cell B2, entered an arrow symbol (to do this, go to Insert and click on ‘Symbol’ option).
*   Copy and paste the headers from the data set to cell A3:C3 in the ‘Backend’ sheet.
*   Use the following function in cell A4:AC4:
    
    \=[IF](https://trumpexcel.com/excel-if-function/)
    (A3=$C$1,A3&" "&$B$1,A3)
    
*   Rest of the cells will automatically get filled by the VBA code when you double click on the headers to sort the column.

Your backend sheet would look something as shown below:

![Sort Data using VBA - Backend for double click with arrow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20233'%3E%3C/svg%3E)

Now you can use the below code to sort the data by double-clicking on the headers. When you double-click on a header, it will automatically get the arrow in the header text. Note that I have also used [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to highlight the cell as well.

Private Sub Worksheet\_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
Dim KeyRange As Range
Dim ColumnCount As Integer
ColumnCount = Range("DataRange").Columns.Count
Cancel = False
If Target.Row = 1 And Target.Column <= ColumnCount Then
Cancel = True
Worksheets("Backend").Range("C1") = Target.Value
Set KeyRange = Range(Target.Address)
Range("DataRange").Sort Key1:=KeyRange, Header:=xlYes
Worksheets("BackEnd").Range("A1") = Target.Column
For i = 1 To ColumnCount
Range("DataRange").Cells(1, i).Value = Worksheets("Backend").Range("A4").Offset(0, i - 1).Value
Next i
End If
End Sub

Note that this code works well for the way my data and workbook is constructed. If you change the structure of the data, you will have to modify the code accordingly.

[**Download the Example File**](https://www.dropbox.com/s/zotao0kzk9lljgw/Sort-Data-Using-VBA.xlsm?dl=1)

**You May Also Like the Following Excel Tutorials:**

*   [Sort Worksheets in Excel](https://trumpexcel.com/sort-worksheets/)
     (Alphabetically)
*   [How to Filter Data in a Pivot Table in Excel](https://trumpexcel.com/filter-data-pivot-table-excel/)
    .
*   [Dynamic Excel Filter Search Box – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [How to do a Multi-level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    .
*   [Excel Advanced Filter – A Complete Guide with Examples](https://trumpexcel.com/excel-advanced-filter/)
    .
*   [24 Useful Excel Macro Examples for VBA Beginners.](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Use Excel VBA InStr Function (with practical EXAMPLES).](https://trumpexcel.com/excel-vba-instr/)
    
*   [Excel VBA Autofilter](https://trumpexcel.com/vba-autofilter/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

21 thoughts on “How to Sort Data in Excel using VBA (Range/Columns)”
--------------------------------------------------------------------

1.  Is there any possibility of converting excel VBA to google sheet. Thank you.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-14691)
    
2.  If you want to protect the sheet is it possible or does this not work with protected sheets? can I add the password to the code?
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-14595)
    
3.  Sorting Multiple Columns With Headers  
    I copied this code and table, but it does not work. Is there a problem with the code?
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-14051)
    
4.  This post helped me a lot, thank you very much!
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-13530)
    
5.  Hi  
    How to Auto sort when file open…?
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-13504)
    
6.  Very helpful post. I suggest to add a ‘SortFields.Clear’ if you want to run it more than once.
    
    Sub SortMultipleColumns()  
    With ActiveSheet.Sort  
    .SortFields.Clear ‘<— \*\*\*HERE\*\*\*  
    .SortFields.Add Key:=Range("A1"), Order:=xlAscending  
    .SortFields.Add Key:=Range("B1"), Order:=xlAscending  
    .SetRange Range("A1:C13")  
    .Header = xlYes  
    .Apply  
    End With  
    End Sub
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-13485)
    
7.  Is there a way to sort a portion of a single row over multiple columns, without having to specify a Sort by column?
    
    I have individual words in several columns, and I want to sort the columns alphabetically, regardless of which column the words are in.
    
    For example, each column from M to W has a single word. I want to sort that portion of the row so that the words are rearranged in the columns alphabetically, lowest in M, highest in W.
    
    Thank you.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-12981)
    
8.  Great explanation. Very Clear. Using your example of sorting the 3 column data set by column “A”, my need is to sort A1:C20 then move to column E and sort E1:E20 and repeat “X” number of times (where X is variable) moving to the right 4 columns each time.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-12923)
    
    *   This is John R. Forget my request. Just figured it out thanks to your wonderful explanation. The code is as follows for anyone else interested.  
        Enter the number of times you want to move to the right and sort a new data set in Cell “A4”. Put cursor on first cell of data set you want to start with and macro will sort that data set, move 4 cells to the right (ActiveCell.Offset line) and repeat sort.
        
        Sub SortDataWithoutHeader()  
        ActiveCell.Range(“A1:C30”).Select  
        Dim i As Long  
        For i = 1 To Range(A4).Value  
        Selection.Sort  
        Key1:=ActiveCell.Range(“A1”), Order1:=xlAscending, Header:=xlNo  
        ActiveCell.Offset(0, 4).Range(“A1”).Select  
        Next i  
        End Sub
        
        [Reply](https://trumpexcel.com/sort-data-vba/#comment-12924)
        
9.  Very Nice! Clear and to the point. Many thanks
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-12545)
    
10.  Getting Method ‘Range’ of object ‘\_Worksheet’ failed on this line:
    
    ColumnCount = Range(“DataRange”).Columns.Count
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-12210)
    
    *   Because Writer use “DateRange” as variable for range, please use your own data range / table range for getting desired result.
        
        [Reply](https://trumpexcel.com/sort-data-vba/#comment-12349)
        
11.  Very helpful indeed!!!!
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-11774)
    
12.  Re:  
    Sub SortMultipleColumns()  
    With ActiveSheet.Sort  
    .SortFields.Add Key:=Range(“A1”), Order:=xlAscending  
    .SortFields.Add Key:=Range(“B1”), Order:=xlAscending  
    .SetRange Range(“A1:C13”)  
    .Header = xlYes  
    .Apply  
    End With  
    End Sub
    
    I use .SetRange Columns(“A:B”)  
    This gets all the data in the column(s)
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-11520)
    
    *   Quite sure that if your data is in four columns you will need to change the Range from A1:C?? to A1:D??.  
        I would recommend that you set the range first and assign it to a variable and then use that variable name in the sort code.
        
        [Reply](https://trumpexcel.com/sort-data-vba/#comment-11775)
        
13.  Sub SortMultipleColumns()  
    With ActiveSheet.Sort  
    .SortFields.Add Key:=Range(“A1”), Order:=xlAscending  
    .SortFields.Add Key:=Range(“B1”), Order:=xlAscending  
    .SetRange Range(“A1:C13”)  
    .Header = xlYes  
    .Apply  
    End With  
    End Sub
    
    this isn’t working for 4 columns. It sorts my data for the first 2 columns I specify, but not after that.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-11383)
    
14.  I could not download the example files.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-11145)
    
15.  Interesting. Is there an approach that would allow sorting as described here but a) contents of cells to be protected. b) some visible data columns to be excluded as sorting by options? i.e. double clicking on some headers does nothing because we don’t want the user to break the data set, but they do need to be able to see it. Thanks.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-10774)
    
16.  How to sort excel data on basis of Color of cell?
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-10455)
    
17.  very helpful. Thank you. I had found some older macro code with “key1:” but that doesn’t appear to work anymore so it was helpful to see “add key” in your code.
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-10427)
    
18.  Hi,  
    My profile is RTA in a bpo and I need your help. Hope you don’t mind.
    
    Question – We do have Forecast volume from client and actual volume is refreshed every 5 second and is updated in excel. Based on that I can judge in which span the number of calls / chats were high/low.  
    According to that I have to send an e-mail… for ex:-  
    Low volume observed in Pay&Go  
    High volume observed in Business, Sales Skills.
    
    I have used the formulas which will filter both of the values (greater than 10% as high volume and less than -10% as low volume.  
    I need to send an e-mail which will filter and write automatically as mentioned above.
    
    Pls let me know how this can be done
    
    [Reply](https://trumpexcel.com/sort-data-vba/#comment-9869)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-data-vba/#respond)

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