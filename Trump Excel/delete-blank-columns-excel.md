# Delete Blank Columns in Excel (3 Easy Ways + VBA)

**Source:** https://trumpexcel.com/delete-blank-columns-excel

---

[Skip to content](https://trumpexcel.com/delete-blank-columns-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/delete-blank-columns-excel/#below-title)

When I was working as a data analyst years ago, part of my job was to download data from financial databases and then [clean this data](https://trumpexcel.com/clean-data-in-excel/)
.

And one of the things I had to do while cleaning the data was to delete any blank columns in the data set.

While you can always manually select columns and delete them one by one, doing so in a large data set, where you have tens or hundreds of columns in every data set, would be inefficient and error-prone.

While there is no inbuilt functionality in Excel to date blank columns in one go, this can be achieved by using a combination of different functionalities.

In this tutorial, I will show you **how to delete empty columns in Excel** using a couple of different methods (including a simple VBA code).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/delete-blank-columns-excel/#)

Manually Deleting Blank Columns (Best with Small Datasets)
----------------------------------------------------------

If you have a small data set such as the one shown below, it’s possible to manually select the blank columns, and delete them.

![Dataset with blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20528'%3E%3C/svg%3E)

Below are the steps to delete blank columns manually in the above data set:

1.  Select the blank column that you want to delete by clicking on the column header of that column

![Select one blank column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20693%20535'%3E%3C/svg%3E)

2.  Once the blank column is selected, right-click on the selection
3.  Click on the ‘Delete’ option

![Right click and then click on delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20521'%3E%3C/svg%3E)

The above steps would instantly delete the selected blank column, and shift the remaining data set to the left.

**Pro Tip**: You can also select multiple blank columns in one go by holding the Control key on your keyboard (or the Command key if you’re using a Mac OS), and then manually clicking on the column headers of all the blank columns that you want to select. Once all the blank columns are selected, you can right-click and then click on the Delete option to delete all blank columns in one go

The biggest drawback of this method is that it is manual and inefficient (however, it could be a preferred method with small datasets).

In case you have a large data set with lots of blank columns, it’s better to use the methods covered next

Also read: [Remove Blank Rows in Excel Using a Formula](https://trumpexcel.com/remove-blank-rows-formula/)

Delete Blank Columns Using COUNT Function + Sort/Find and Replace
-----------------------------------------------------------------

Excel has an inbuilt functionality that allows you to quickly select blank cells (using the Go-To special dialog box as we will see later in this tutorial), but there is no way to quickly select only those columns that are empty.

So we will have to use a workaround to first identify those columns that have only blank cells in them and then delete these blank columns.

Below I have a data set where I have the sales figures of different stores for different items. As you can see there are some columns that are completely empty in the below data set.

![Dataset with blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20528'%3E%3C/svg%3E)

Now there are a couple of methods you can use to remove blank columns from the dataset. Let’s have a look at each of these methods in detail.

### Using the COUNTA formula with FIND and Replace

With large datasets, a better way to delete all blank columns is by inserting a helper row at the top and using a COUNTA formula to identify all the columns that are empty.

Once you have done that, you can use this helper row to quickly select all the blank columns and delete them in one go.

Below I have a data set where I have some blank columns that I want to remove.

![Dataset with blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20528'%3E%3C/svg%3E)

Here are the steps to do that using the [COUNTA function](https://trumpexcel.com/excel-functions/counta-function/)
 with a helper row:

1.  Select the first row of your data set by clicking on the row header (it’s the row number in grey on the left)

![Select the entire row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20526'%3E%3C/svg%3E)

2.  With the entire first row selected, right-click and then click on Insert. This will [insert a new row](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
     above the first row of your data set

![Insert a new row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20697%20527'%3E%3C/svg%3E)

3.  Enter the below formula in the first cell of the helper row and copy it for all the cells in the helper row

\=IF(COUNTA(A2:A1048576)=0,"Blank","Not Blank")

![Enter formula in helper row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20397'%3E%3C/svg%3E)

The above formula uses the COUNTA function and calculates the total number of cells that are not empty in the specified range.

This formula is going to return a value greater than zero for all the columns that are not completely empty and zero for any column that is completely empty.

And then I used the [IF function](https://trumpexcel.com/excel-if-function/)
 to return “Blank” in a cell if the entire column below it is empty, and “Not Blank” if it is not empty.

Now that I can identify all the empty columns by looking at the values in the helper row, I’m going to use the Find and Replace dialog box to quickly select all the cells that have the value “Blank”.

Once I have these cells selected, I can delete the entire column in one go.

Below are the steps two now select all the empty columns in one go:

1.  Select all the cells in the helper row (the one where we entered the COUNTA formula)
2.  Hold the Control key on your keyboard and then press the F key. This will open the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
     dialog box. You can also open the Find and Replace dialog box by going to the ‘Home’ tab and then clicking on the ‘Find & Select’ option and then clicking on the ‘Find’ option

![Find and replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

3.  In the Find and Replace dialog box, enter the text ‘Blank’ in the ‘Find what’ field

![Enter blank in Find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

4.  Click the ‘Options’ button

![Click on Options button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

5.  In the ‘Look in’ drop-down, select ‘Values’
6.  Check the option, ‘Match entire cell contents’

![Match entire cell content and look in values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

7.  Click on the Find All button. This will find and return the cell references of all the cells that contain only the text ‘Blank’

![Click on Find all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

8.  Hold the Control key and press the A key. This will select all the cells that were given by the Find and Replace option

![All blank cells are selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20437'%3E%3C/svg%3E)

9.  Right-click on any of the cells that have been selected (which would be any cell that has the text ‘Blank’ in it), and then click on ‘Delete’

![Right click on the blank cell and then click on delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20551'%3E%3C/svg%3E)

10.  In the Delete dialog box, select the ‘Entire Column’ option

![Delete Entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20214%20223'%3E%3C/svg%3E)

11.  Click OK

The above options would instantly delete all the blank columns in your data set.

**Important Notes:**

*   COUNTA function would only return 0 if all the cells in the column are blank. in case there is a header in the column that has no values in it and needs to be removed, you need to adjust the formula so that the header row is not used. For example, you can use the formula =IF(COUNTA(A3:A1048576)=0,”Blank”,”Not Blank”) in case even blank columns have headers
*   For this formula to work, the columns need to actually be blank. For example, if there are space characters in the cells in the blank column, while they might appear to be empty, the COUNTA function would not consider it as blank.

### Using the COUNTA Formula with Sort Option

Let me show you another smart way you can use to quickly delete all the empty columns in Excel.

In this method, we will still be using the COUNTA function to get ‘Blank’ or ‘Not Blank’ in the helper row based on whether the column is empty or not.

But instead of using the Find and Replace dialog box, we will use the Sort option

Below I have the same data set and I want to remove the blank columns.

![Dataset with blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20528'%3E%3C/svg%3E)

Below are the steps to insert a helper row to identify columns that are empty:

1.  Select the first row of your data set by clicking on the row header
2.  Right-click and then click on Insert. This will insert a new row above the first row of your data set
3.  Enter the below formula in the first cell of the helper row and copy it for all the cells in the helper row

\=IF(COUNTA(A2:A1048576)=0,"Blank","Not Blank")

![Enter formula in helper row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20397'%3E%3C/svg%3E)

The above formula would return the text “Blank” in cells where the column below it is empty and “Not Blank” when the column below it is not empty.

Now I can sort the entire data set using the helper row so that I get all the blank columns together and all the non-blank columns together

Below are the steps to do this:

1.  Select the entire data set, including the helper row
2.  Click the **Data** tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20223'%3E%3C/svg%3E)

3.  In the Sort and Filter group, click on the **Sort** icon. This will open the Sort dialog box

![Click the Sort option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20639%20163'%3E%3C/svg%3E)

4.  Click the **Options** button

![Click the Options button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)

5.  In the ‘Sort Options’ dialog box that opens up, click on the ‘**Sort left to right**’ option

![Select Sort left to right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20216'%3E%3C/svg%3E)

6.  Click OK
7.  Click the ‘Sort by’ drop-down and then select the ‘Row 1’ option

![Select Row 1 as Sort by](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)

8.  Keep the Sort Order A to Z (in case it’s not that already)

![Select A to Z as the sort order](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)

9.  Click Ok

The above steps would sort the data based on the helper row and bring all the blank columns together and non-blank columns together (as shown below).

![All blank columns are stacked together](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20551'%3E%3C/svg%3E)

Once you have all the blank columns together, you can select these in one go, and then delete them.

And once you have deleted the blank columns, you can remove the helper row as well.

Delete Blank Columns Using VBA
------------------------------

While the methods covered above work great, they do require a little bit of a setup using a helper row.

In case you are comfortable with VBA, you may find it a little easier to use as compared with the two helper row methods covered above.

Below is the VBA code that will do this for you:

    'Code Developed by Sumit Bansal from https://trumpexcel.com
    
    Sub DeleteBlankColumns()
    
    Dim EntireColumn As Range
    On Error Resume Next
    
    Application.ScreenUpdating = False
    
            For i = Selection.Columns.Count To 1 Step -1
                Set EntireColumn = Selection.Cells(1, i).EntireColumn
                If Application.WorksheetFunction.CountA(EntireColumn) = 0 Then
                    EntireColumn.Delete
                End If
            Next
    
    Application.ScreenUpdating = True
    
    End Sub
    

The above VBA code uses a simple [For-Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each column in the selection, and check whether the COUNTA value for all the cells in that column is zero or not.

In case the COUNTA function value is 0, it means that the column is empty and the VBA macro code deletes that column.

And in case the value of the COUNTA function is more than 0, it means that the column is not empty and it is not removed.

**How to Use the above VBA Macro Code?**

Below are the steps to use the above VBA code to delete empty columns in Excel:

1.  Select the data set that has the blank columns that you want to remove
2.  Click the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     in the ribbon.
3.  Click the Visual Basic icon. This will open the VB editor back end in Excel.

![Click on Visual basic icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20191'%3E%3C/svg%3E)

4.  Click the **Insert** option in the menu and then click on **Module**. This will insert a new module which would be visible in the Project Explorer pane. (In case you do not see the Project Explorer pane, click on the **View** option then click on **Project Explorer**)

![Click on Insert module option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20332'%3E%3C/svg%3E)

5.  Copy and paste the above VBA macro code into the module code window

![Copy and paste the code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20338'%3E%3C/svg%3E)

6.  To run the macro, place the cursor anywhere in the code and then click on the green play icon in the toolbar or use the F5 key on your keyboard

![Click on the run macro icon in the toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20190'%3E%3C/svg%3E)

The above steps would instantly run the code which would remove all the empty columns from the selected data set.

**Caution**: The changes done by the VBA macro code in your worksheet cannot be undone. So it’s always a good idea to create a backup copy of your original data before using the VBA code to delete empty columns

Delete Blank Columns Using Go-To Special
----------------------------------------

One final method that I want to show you to delete empty columns in Excel is by using the Go To Special dialog box.

While this method is the fastest among all the methods covered in this tutorial so far, you need to be extremely cautious when using this method (especially if you’re working with large datasets).

This is because it can be error-prone and can lead to [deleting columns](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
 that are not completely blank.

So while I’m covering this method in this tutorial, I would **not recommend** you use this method, instead use the other methods covered in this tutorial.

If you decide to use this method , you should be absolutely sure that your data set has no blank cells in the columns that are not completely blank

Let’s see how this method works.

Below I have a data set where I have some columns that are empty and I want to remove these columns.

![Dataset with blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20528'%3E%3C/svg%3E)

Here are the steps to do this using go to special dialog box:

1.  Select the entire data set
2.  Press the F5 key on your keyboard. This will open the **Go To dialog box**. You can also get the same thing if you click on the **Home** tab and in the Editing group, click on the **Find & Select** option and then click on the **Go To** option

![Go to special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

3.  In the Go-To dialog box that opens up, click on the **Special** button

![Click the Special button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

4.  In the ‘Go To Special’ dialog box that opens up, click on the **Blanks** option

![Click the blanks option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)

5.  Click OK. The above steps would select all the blank cells in your data set.

![All blank columns are selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20528'%3E%3C/svg%3E)

6.  Once you have these blank cells selected, right-click on any of these blank cells in the empty columns, and then click on the **Delete** option.

![Right click on the blank cell and then click on delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20551'%3E%3C/svg%3E)

7.  This will open the Delete dialog box where you can choose the **Entire column** option and then click on OK

![Delete Entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20214%20223'%3E%3C/svg%3E)

The above steps would delete all the columns where there are blank cells

**The Drawback of this method?**

One big drawback of this method is that in case you have a couple of blank cells in otherwise filled columns, these would also be selected and these non-blank columns would also be deleted.

Below is an example where I have a couple of blank cells in the Printer and Scanner columns, and these were also selected when I use the ‘Go To Special’ dialog box.

![Drawback of go to special method to delete blank columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20693%20526'%3E%3C/svg%3E)

Now if I go ahead with the above ‘Go To Special’ method and delete the empty columns, even the Printer and the Scanner columns would be deleted, which is not what I want.

This is why it is best to avoid this method to delete empty columns as it could also end up deleting some columns just because they had a few blank cells in them.

So these are some of the methods you can use to **delete blank columns in Excel**.

If you have a small data set and you only have a couple of blank columns, it is better to delete them manually.

And in case you have a large data set, you can either use the VBA method (which is fast and efficient), or use the helper row along with the sort feature or the find and replace feature to quickly select blank columns and delete them.

**Note**: The methods I have covered in this tutorial can also be used to delete blank rows in Excel. You would have to adjust the methods and the VBA code accordingly

**Other Excel tutorials you may also like:**

*   [Delete Blank Rows in Excel (with and without VBA)](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [Fill Down Blank Cells Until the Next Value in Excel (3 Easy Ways)](https://trumpexcel.com/fill-down-blank-cells-excel/)
    
*   [Insert a Blank Row after Every Row in Excel (or Every Nth Row)](https://trumpexcel.com/insert-blank-row-after-every-row/)
    
*   [How to Highlight Blank Cells in Excel (in less than 10 seconds)](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/delete-blank-columns-excel/#respond)

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