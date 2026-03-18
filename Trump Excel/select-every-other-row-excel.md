# Select Every Other Row in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/select-every-other-row-excel

---

[Skip to content](https://trumpexcel.com/select-every-other-row-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/select-every-other-row-excel/#below-title)

Many times, I have a need to select every other row in Excel so that I can highlight or delete them.

This is commonly the case when I download my data from databases or the web, and it adds an extra row after every useful row that I need to remove.

Another useful situation can be when you want to select every other row and then copy and paste them into some other location in your worksheet.

While there is no inbuilt functionality in Excel that allows you to select every other row, in this tutorial, I am going to show you a couple of workarounds to do this.

Let’s get started with the methods.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/select-every-other-row-excel/#)

**Note**: In many cases, the reason people want to select every other row in Excel is to highlight them. If you are in the same situation, you should know that you do not need to select the row to highlight it. You can use conditional formatting or the inbuilt formatting options in an Excel table to automatically highlight every other row in Excel. [**You can read my detailed tutorial**](https://trumpexcel.com/highlight-every-other-row-excel/)
 on this topic that covers the exact steps you need to take to get this done.

Select Every Other Row Manually
-------------------------------

If you have a small data set, the fastest method to select every other row in Excel would be to do it manually.

To do this, you need to use both your keyboard as well as your mouse/trackpad.

Below, I have a data set where I want to select every other row (i.e., alternate rows).

![data set to select every other row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20337'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Press the Control key on your keyboard and keep holding it
2.  Click on the row header of the row that you want to select (in this example, it would be row number 3, which is the second record in our dataset)

![select the first row manually](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20336'%3E%3C/svg%3E)

3.  Continue to hold the Control key and then click the row header of all the rows that you want to select
4.  Once done with the selection, leave the control key

![all the alternate rows have been manually selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20686%20342'%3E%3C/svg%3E)

This method is suitable only when you have a small data set, and manually selecting every other row won’t be too time-consuming.

Personally, I prefer this method when I have a data set of up to 10 to 12 rows. For anything longer than that, you can use the other methods covered in this article.

Also read: [Keyboard & Mouse Tricks that will Reinvent the Way You Excel](https://trumpexcel.com/keyboard-mouse-tricks/)

Using the Helper Column & Filter Method
---------------------------------------

One simple workaround to select every other row in Excel is by adding a helper column and then using this helper column to filter the data so that only those rows are visible that we need to select.

Let me show you how it works with an example.

Below I have a data set where I want to select every other row.

![data set to select every other row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20337'%3E%3C/svg%3E)

Here are the steps to do this using a helper column and the filter functionality:

1.  Enter the text ‘Helper’ in cell G1. This would become our helper column, and the text ‘Helper’ becomes the header for that column.

![added a helper column on the right of the data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20685%20337'%3E%3C/svg%3E)

2.  In cell G2, enter the below formula

\=ISODD(ROW())

Copy this formula for all the cells in the column.

![ISODD formula in the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20384'%3E%3C/svg%3E)

This formula uses the ISODD function along with the ROW function to give TRUE if the row number is odd and FALSE if the row number is even.

3.  Select any cell in the dataset and then click on the Data tab.

![click the data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20223'%3E%3C/svg%3E)

4.  Click on the Filter icon in the Sort & Filter group. This will add filter icons to all the headers in your data set. You can also use the keyboard shortcut CONTROL + SHIFT + L to apply a filter to the header row.

![click the filter icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20679%20223'%3E%3C/svg%3E)

5.  Click on the filter icon in the helper row column header.

![click on the filter icon in the header of helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20686%20338'%3E%3C/svg%3E)

6.  Uncheck the FALSE option and click OK. This will filter your data set, and you will only see those rows where the value will helper column is TRUE (which is the case for every alternate row)

![uncheck the false option and click OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20607'%3E%3C/svg%3E)

7.  Select the dataset that is visible after filtering.

![only alternate rows are visible that can be selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20205'%3E%3C/svg%3E)

When you select the cells after the data set has been filtered, it only selects the cells that are visible.

So anything you do to this data set would not impact the cells that are not visible.

For example, if you highlight all these visible cells and then you remove the filter, Only the alternate rows would have been highlighted.

Using VBA to Select Every Other Row in Excel
--------------------------------------------

While the above two methods work well, they are a little time-consuming.

If selecting every other row is something you need to do quite often, you should definitely consider trying out the VBA method.

Below is the VBA code that would select every row in your data set that you selected.

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub SelectEveryOtherRow()
    
    Dim MyRange As Range
    Dim RowSelect As Range
    Dim i As Integer
    Set MyRange = Selection
    Set RowSelect = MyRange.Rows(3)
    For i = 3 To MyRange.Rows.Count Step 2
    Set RowSelect = Union(RowSelect, MyRange.Rows(i))
    Next i
    Application.Goto RowSelect
    End Sub

The above VBA code starts from the third row in our dataset. it then uses a simple [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through all the rows and only select every second row, starting from the third row.

Below are the steps to use this VBA code in Excel:

1.  Open the Excel workbook where you want to use this VBA code.
2.  **Select the dataset** where you want to select every alternate row
3.  Click the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon. This will open the [VB editor](https://trumpexcel.com/visual-basic-editor/)
    , where we are going to copy and paste the above code.

![click on visual basic icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20190'%3E%3C/svg%3E)

You can also use the keyboard shortcut **ALT + F11** to open the VB Editor.

4.  Click on the Insert option in the Menu.

![click the insert option in the menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20160'%3E%3C/svg%3E)

5.  In the options that appear, click on the Module option. This will insert a new module in the workbook and open the Module code window.

![click on the module option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20212'%3E%3C/svg%3E)

6.  Copy and Paste the above VBA code into the Module code window.

![copy and paste the VBA code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20303'%3E%3C/svg%3E)

7.  [Run the macro](https://trumpexcel.com/run-a-macro-excel/)
     by clicking the Run Subroutine icon in the toolbar or pressing the F5 key. Make sure that your cursor is within the code before you run the macro. _(Note: This code would only work if you already selected your data in step 2)_

![click on the run macro icon in the toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20121'%3E%3C/svg%3E)

8.  Close or Hide the VB Editor

As soon as you run the above code, you will notice that every other row starting from row #3 has been selected in our data set.

![every other row has been selected with VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20358'%3E%3C/svg%3E)

In case you want to select every other row starting from row number 2, you can modify the code as shown below:

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub SelectEveryOtherRow()
    
    Dim MyRange As Range
    Dim RowSelect As Range
    Dim i As Integer
    Set MyRange = Selection
    Set RowSelect = MyRange.Rows(2)
    For i = 2 To MyRange.Rows.Count Step 2
    Set RowSelect = Union(RowSelect, MyRange.Rows(i))
    Next i
    Application.Goto RowSelect
    End Sub

A few things to know when using this macro code:

*   When you add this VBA code to your workbook, you need to save your workbook as a macro-enabled file (with a .XLSM extension)
*   This code would only work in the workbook where it has been added. In case you want to use this code on all your Excel workbooks, you should save this in your [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
    
*   Once you have added this code in the workbook where you want to use it or in the Personal Macro Workbook, you can also add an icon to run the code with a single click from the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
    .

Add-in to Select Every Other Row in Excel
-----------------------------------------

If selecting every other row is something you need to do quite often, you can also consider investing in third-party Excel add-ins that can make the process very easy for you.

One such add-in you can consider getting is [Dose Excel](https://www.zbrainsoft.com/downloads.html)
, which allows you to specify the interval and the number of rows that can be selected.

For example, you can specify that you need to select one row after every other row (or one row after every two rows).

In this article, I showed you different three different ways you can use to select every other row in Excel. While this is something that is not there as an inbuilt functionality in Excel, it can be done using the filter method that uses a helper column or the VBA method.

And in case you have a small data set, it’s best just to select every alternate row manually.

**Other Excel articles you may also like:**

*   [Select Till End of Data in a Column in Excel (Shortcuts)](https://trumpexcel.com/select-end-of-data-in-column-excel/)
    
*   [How to Select Entire Column (or Row) in Excel – Shortcut](https://trumpexcel.com/select-entire-column-excel/)
    
*   [Select Every Other Column in Excel](https://trumpexcel.com/select-alternate-columns-excel/)
    
*   [7 Easy Ways to Select Multiple Cells in Excel](https://trumpexcel.com/select-multiple-cells-excel/)
    
*   [How to Select Non-adjacent cells in Excel?](https://trumpexcel.com/select-non-adjacent-cells-in-excel/)
    
*   [How to Deselect Cells in Excel](https://trumpexcel.com/deselect-cells-in-excel/)
    
*   [3 Quick Ways to Select Visible Cells in Excel](https://trumpexcel.com/select-visible-cells/)
    
*   [How to Select Every Third Row in Excel (or select every Nth Row)](https://trumpexcel.com/select-every-third-row/)
    
*   [How to Quickly Select Blank Cells in Excel](https://trumpexcel.com/select-blank-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/select-every-other-row-excel/#respond)

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