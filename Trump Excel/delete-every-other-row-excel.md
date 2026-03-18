# How to Delete Every Other Row in Excel (or Every Nth Row)

**Source:** https://trumpexcel.com/delete-every-other-row-excel

---

[Skip to content](https://trumpexcel.com/delete-every-other-row-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/delete-every-other-row-excel/#below-title)

**Watch Video – Delete Every Other Row in Excel**

Sometimes you may have a need to delete every other row (i.e., alternate rows), or every third/fourth/fifth row in Excel.

One use-case of this could be when you have weekly data and you only want the data for even weeks or odd weeks. Another could be when you get a data dump from a database and all the useful data is only in every second or third row.

While you always have the option to manually [select and delete rows](https://trumpexcel.com/delete-rows/)
, this is inefficient in case you have a large dataset.

There are better ways to do this.

In this tutorial, I will show you a couple of ways to delete every other row in Excel using a simple filtering technique. And if you’re cool with using a VBA macro code, I have also given a short VBA code that does it with a single click. The methods are shown in this tutorial work for all the versions of Excel (2007, 2010, 2013, and 2016)

While deleting every other row in Excel can be quite simple, it could be a challenge to delete every other column. This is because you can not filter columns in Excel (the way you can filter rows). In the last section of this tutorial, I will also show you some ways to delete alternate columns (or every Nth column) in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/delete-every-other-row-excel/#)

Delete Every Other Row By Filtering the Dataset (Using Formula)
---------------------------------------------------------------

If you could somehow filter all the even rows or the odd rows, it would be super easy to delete these rows/records.

While there is no inbuilt feature to do this, you can use a helper column to first divide the rows in to odd and even, and then filter based on the helper column value.

Suppose you have a dataset as shown below, which has sales data for each sales rep for two regions (the US and Canada) and you want to delete the data for Canada.

![Dataset where every other row needs to be deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20334'%3E%3C/svg%3E)

Below are the steps to first filter and then delete every other row (which has data for Canada):

1.  In the cell adjacent to the last column header, enter the text **HelperColumn** (or any header text that you want the helper column to have)![Enter HelperColumn header in an adjacent column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20335'%3E%3C/svg%3E)
2.  In the cell below the helper column header, enter the following formula: **\=ISEVEN(ROW())**. Copy this formula for all the cells. This formula returns TRUE for all even rows and FALSE for all ODD rows![Enter ISEVEN formula in the helper column and copy it for all the cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20391'%3E%3C/svg%3E)
3.  Select the entire dataset (including the cells where we entered the formula in the above step).
4.  Click the Data tab![Click on the Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20199'%3E%3C/svg%3E)
5.  Click the Filter icon. This will apply a filter to all the headers in the dataset![Click on the Filter Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20159'%3E%3C/svg%3E)
6.  Click the Filter icon in the HelperColumn cell.![Click on the filter icon the helper column header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20335'%3E%3C/svg%3E)
7.  Deselect the TRUE option (so only the FALSE Option is selected)![Deselect all options and only keep the FALSE option checked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20370'%3E%3C/svg%3E)
8.  Click OK. This will filter the data and only show those records where the HelperColumn value is FALSE.
9.  Select all the filtered cells in the helper column (excluding the header)![Select all the cells in the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20193'%3E%3C/svg%3E)
10.  Right-click on any of the selected cells and click on ‘Delete Row’![Click on the Delete row option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20347'%3E%3C/svg%3E)
11.  In the dialog box that opens, click on OK. This will delete all the visible records and you will only see the header row as of now.![Click on the OK button in the Delete Row dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20145'%3E%3C/svg%3E)
12.  Click the Data tab and then click the Filter icon. This will remove the filter and you will be able to see all the remaining records.

The above steps filter every second row in the dataset and then deletes those rows.

![Resulting Data where every other row has been deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20192'%3E%3C/svg%3E)

**Don’t worry about the helper column values at this stage**. The resulting data has only the rows for the US  and all the Canada rows are deleted. You can delete the helper column now.

In case you want to delete every other row starting from the first row onwards, select the TRUE option in step 7 and deselect the FALSE option.

Note: When you delete the rows in Excel using the above method, it also deletes any data that you may have in the entire (apart from the one in the dataset). When you use this method, make sure you don’t have anything to the left and right of the dataset that you’re deleting.

While the above method is great, it has two drawbacks:

1.  It needs to you add a new column (the **HelperColumn** in our example above)
2.  It can be time-consuming if you have to delete alternate rows do this often

Related tutorial: [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)

Delete Every Nth Row By Filtering the Dataset (Using Formula)
-------------------------------------------------------------

In the above method, I showed you how to delete every other row (alternate row) in Excel.

And you can use the same logic to delete every third or fourth row in Excel as well.

Suppose you have a dataset as shown below and you want to delete all every third row.

![Dataset to delete every third row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20480'%3E%3C/svg%3E)

The steps to delete every third row are almost the same as the one covered in the above section (for deleting alternate rows). The only difference is in the formula used in Step 2.

Below are the steps to do this:

1.  In the cell adjacent to the last column header, enter the text **HelperColumn** (or any header text that you want the helper column to have)
2.  In the cell below the helper column header, enter the following formula: **\=MOD(ROW(),3)=1**. This formula returns TRUE for every third row and FALSE for every other row.![Helper Column MOD formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20534'%3E%3C/svg%3E)
3.  Select the entire dataset (including the cells where we entered the formula in the above step).
4.  Click the Data tab![Click on the Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20199'%3E%3C/svg%3E)
5.  Click the Filter icon. This will apply a filter to all the headers in the dataset![Click on the Filter Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20159'%3E%3C/svg%3E)
6.  Click the Filter icon in the HelperColumn cell.![Click on the filter icon the helper column header - delete every third row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20293'%3E%3C/svg%3E)
7.  Deselect the TRUE option (so only the FALSE Option is selected)![Click TRUE in the Filter option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20476'%3E%3C/svg%3E)
8.  Click OK. This will filter the data and only show those records where the HelperColumn value is FALSE.
9.  Select all the cells in the helper column
10.  Right-click on any of the selected cells and click on Delete Row![Click the Delete row Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20762%20335'%3E%3C/svg%3E)
11.  In the dialog box that opens, click on OK. This will delete all the visible records and you will only see the header row as of now.![Click on the OK button in the Delete Row dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20145'%3E%3C/svg%3E)
12.  Click the Data tab and then click the Filter icon. This will remove the filter and you will be able to see all the remaining records.

The above steps would delete every third row from the dataset and you would get the resulting data as shown below.

![Resulting data after deleting every third row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20335'%3E%3C/svg%3E)

**Don’t worry about the helper column values at this stage**. You can delete the helper column now.

The formula used in Step 2 uses the [MOD function](https://trumpexcel.com/excel-mod-function/)
 – which gives the remainder when one number is divided by the other. Here I have used the [ROW function](https://trumpexcel.com/excel-row-function/)
 to get the row number and it’s divided by 3 (because we want to delete every third row).

Since our dataset starts from the second row onwards (i.e., row #2 contains the first record), I use the following formula:**\=MOD(ROW(),3)=1**

I am equating it to 1 and for every third row, the MOD formula will give the remainder as 1.

You can adjust the formula accordingly. For example, if your dataset’s first record starts from third-row onwards, the formula would be **\=MOD(ROW(),3)=2**

Automatically Delete Every Other Row (or Nth row) using VBA Macro (Quick Method)
--------------------------------------------------------------------------------

If you have to delete every other row (or every nth row) quite often, you can use a [VBA code](https://trumpexcel.com/excel-vba/)
 and have it available in ṭhe Quick Access Toolbar. This will allow you to quickly delete alternate rows with a single click.

Below is the code that first asks you to select the range in which you want to delete alternate rows, and then delete every second row in the selected dataset.

Sub Delete\_Every\_Other\_Row()
Dim Rng As Range
Set Rng = Application.InputBox("Select the Range (Excluding headers)", "Range Selection", Type:=8)
For i = Rng.Rows.Count To 1 Step -2
If i Mod 2 = 0 Then
Rng.Rows(i).Delete
End If
Next i
End Sub

When you run the above code, it will first ask you to select the range of cells. Once you have made the selection, it will go through each row and delete every second row.

If you want to delete every third row instead, you can use the below code:

Sub Delete\_Every\_Third\_Row()
Dim Rng As Range
Set Rng = Application.InputBox("Select the Range (Excluding headers)", "Range Selection", Type:=8)
For i = Rng.Rows.Count To 1 Step -3
If i Mod 3 = 0 Then
Rng.Rows(i).Delete
End If
Next i
End Sub

**Where to put this VBA macro code?**

You need to place this code in a regular module in the VB editor in Excel.

Below are the steps to open the Vb Editor, add a module and place the code in it:

1.  Copy the above VBA code.
2.  Go to the Developer tab.![Developer tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20128'%3E%3C/svg%3E)
3.  Click on Visual Basic.![Click the Visual Basic button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20129'%3E%3C/svg%3E)
4.  In the VB Editor, right-click on any of the workbook objects.
5.  Go to Insert and click on Module.![Insert a module in Excel VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20358'%3E%3C/svg%3E)
6.  In the module, paste the above VBA code.![Copy and Paste the VBA code in code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20201'%3E%3C/svg%3E)
7.  Close the VB Editor.

Once you have the code in the VB Editor, you can use the following methods to run the code:

*   Run a Macro from the VB Editor (by clicking on the green play button in VB Editor toolbar)
*   By placing the cursor on any line in the code and using the F5 key
*   By assigning the macro to a button/shape
*   By adding the macro to the Quick Access toolbar

Here is a detailed tutorial on [how to run a macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
.

If you have to do this often, you can consider adding the VBA code to the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. This way, it will always be available to you for use in all the workbooks.

When you have a VBA code in a workbook, you need to save it as a macro-enabled filed (with the .XLSM extension)

Note: Since any changes made by the VBA code are irreversible, it’s best to first make a back-up copy of the workbook/worksheet and then run this code.

Delete Every Other Column (or Every Nth Column)
-----------------------------------------------

Deleting every alternate row or every third/fourth row is made easy as you can use the filter option. All you have to do is use a formula that identifies alternate rows (or every third/fourth row) and filters these rows.

Unfortunately, this same methodology won’t work with columns – as you can not filter columns the way you filter rows.

So, if you have to delete every other column (or every third/fourth/Nth column), you need to be a little more creative.

In this section, I will show you two methods you can use to delete every other column in Excel (and you can use the same method to delete every third/fourth/Nth column if you want).

### Delete Alternate Columns Using Formulas and Sort Method

Suppose you have a dataset as shown below and you want to delete every other column (excluding the header column A)

![Dataset from which alternate columns need to be deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20336'%3E%3C/svg%3E)

The trick here would be to identify alternate columns using a formula and then sort the columns based on that formula. Once you have the sorted columns together, you can manually select and delete this.

Below are the steps to delete every other column in Excel:

1.  Insert a row above the header row (right-click on any cell in the header, click on Insert and then click on Entire row option)![Insert a row above the header row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20360'%3E%3C/svg%3E)
2.  Enter the following formula in the cell above the left-most column in the dataset and copy for all cells: **\=MOD(COLUMN(),2)![Enter the formula in the inserted row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20594%20410'%3E%3C/svg%3E)**
3.  Convert the formula values to numbers. To do this, copy the cells, right-click and go to Paste Special –> Paste values.
4.  Select the entire dataset (excluding any headers in the column). In this example, I have selected B1:G14 (and **NOT** column A)
5.  Click the Data tab![Click on the Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20199'%3E%3C/svg%3E)
6.  Click on the Sort icon![Click the SORT icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20154'%3E%3C/svg%3E)
7.  In the Sort dialog box, make the following changes:
    *   Click on ‘Options’ button and in the dialog box that opens, click on ‘Sort left to right’ and then Click Ok![Select Sort Left to right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%20333'%3E%3C/svg%3E)
    *   In the Sort by drop-down, select Row 1. This is the row that has the formula results![Select Row1 as the Sort by criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
    *   In the Order drop-down, select Smallest to Largest.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)![Select Smallest to Largest as the sort criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
8.  Click OK

The above steps sort all the columns and bring all the alternate columns together at one place (at the end).

Now you can select all these columns (for which the formula value is 1), and delete these.

Although this is not the best solution, it still gets the work done.

In case you want to delete every third column or every fourth column, you need to adjust the formula accordingly.

Related tutorial: [How to SORT in Excel (by Rows, Columns, Colors, Dates, &#038; Numbers)](https://trumpexcel.com/sort-excel/)

### Delete Alternate Columns Using VBA

Another quick way to delete alternate columns is to use the below VBA code:

Sub Delete\_Every\_Other\_Column()
Dim Rng As Range
Set Rng = Application.InputBox("Select the Range (Excluding headers)", "Range Selection", Type:=8)
For i = Rng.Columns.Count To 1 Step -2
If i Mod 2 = 0 Then
Rng.Columns(i).Delete
End If
Next i
End Sub

The above code asks you to select a range of cells which has the columns. Here you need to select the columns excluding the one which has the header.

Once you have specified the range of cells with the data, it will use a For Loop and delete every other column.

In case you want to delete every third column, you can use the code below (and adjust accordingly to delete the Nth column)

Sub Delete\_Every\_Third\_Column()
Dim Rng As Range
Set Rng = Application.InputBox("Select the Range (Excluding headers)", "Range Selection", Type:=8)
For i = Rng.Columns.Count To 1 Step -3
If i Mod 3 = 0 Then
Rng.Columns(i).Delete
End If
Next i
End Sub

The steps on where to place this VBA code and how to use it covered in the above section titled – _“Automatically Delete Every Other Row (or Nth row) using VBA Macro (Quick Method)”_

Hope you found this Excel tutorial useful.

**You may also like the following Excel tutorials:**

*   [Insert a Blank Row after Every Row in Excel (or Every Nth Row)](https://trumpexcel.com/insert-blank-row-after-every-row/)
    
*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
     (Quick and Easy ways)
*   [Delete Blank Rows in Excel (with and without VBA](https://trumpexcel.com/delete-blank-rows-excel/)
    [)](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [How to Insert Multiple Rows in Excel](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    
*   [Remove Blank Rows in Excel Using a Formula](https://trumpexcel.com/remove-blank-rows-formula/)
    
*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [How to Merge Cells in Excel](https://trumpexcel.com/how-to-merge-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/delete-every-other-row-excel/#respond)

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