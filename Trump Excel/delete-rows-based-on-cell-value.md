# Delete Rows Based on a Cell Value (or Condition) in Excel [Easy Guide]

**Source:** https://trumpexcel.com/delete-rows-based-on-cell-value

---

[Skip to content](https://trumpexcel.com/delete-rows-based-on-cell-value/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/delete-rows-based-on-cell-value/#below-title)

When working with large data sets, you may have the need to quickly delete rows based on the cell values in it (or based on a condition).

For example, consider the following examples:

1.  You have sales rep data and you want to delete all the records for a specific region or product.
2.  You want to delete all the records where the sale value is less than 100.
3.  You want to delete all rows where there is a blank cell.

There are multiple ways to skin this data cat in Excel.

The method you choose to delete the rows will depend on how your data is structured and what’s the cell value or condition based on which you want to delete these rows.

In this tutorial, I will show you multiple ways to delete rows in Excel based on a cell value or a condition.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/delete-rows-based-on-cell-value/#)

Filter Rows based on Value/Condition and Then Delete it
-------------------------------------------------------

One of the fastest ways to delete rows that contain a specific value or fulfill a given condition is to filter these. Once you have the filtered data, you can delete all these rows (while the remaining rows remain intact).

Excel filter is quite versatile and you can filter based on many criteria (such as text, numbers, dates, and colors)

Let’s see two examples where you can filter the rows and delete them.

### Delete Rows that contain a specific text

Suppose you have a data set as shown below and you want to delete all the rows where the region is Mid-west (in Column B).

![Sales Dataset with US regions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20480'%3E%3C/svg%3E)

While in this small dataset you can choose to do delete these rows manually, often your datasets are going to be huge where deleting rows manually won’t be an option.

In that case, you can filter all the records where the region is Mid-West and then delete all these rows (while keeping the other rows intact).

Below are the steps to delete rows based on the value (all Mid-West records):

1.  Select any cell in the data set from which you want to delete the rows
2.  Click on the Data tab ![Click the Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20199'%3E%3C/svg%3E)
3.  In the ‘Sort & Filter’ group, click on the Filter icon. This will apply filters to all the headers cells in the dataset![Click on the Filter icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%20198'%3E%3C/svg%3E)
4.  Click on the Filter icon in the Region header cell (this is a small downward-pointing triangle icon at the top-right of the cell)![Click the Filter icon in the header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20408'%3E%3C/svg%3E)
5.  Deselect all the other options except the Mid-West option (a quick way to do this is by clicking on the Select All option and then clicking on the Mid-West option). This will filter the dataset and only show you records for Mid-West region.![Filter option to get only those rows that you want to delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20548'%3E%3C/svg%3E)
6.  Select all the filtered records
7.  Right-click on any of the selected cells and click on ‘Delete Row’![Click on Delete Row Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20426'%3E%3C/svg%3E)
8.  In the dialog box that opens, click on OK. At this point, you will see no records in the dataset.![Click OK to delete rows based on the value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20145'%3E%3C/svg%3E)
9.  Click the Data tab and click on the Filter icon. This will remove the filter and you will see all the records except the deleted ones.

The above steps first filter the data based on a cell value (or can be other condition such as after/before a date or greater/less than a number). Once you have the records, you simply delete these.

Some useful shortcuts to know to speed up the process:

1.  **Control + Shift + L** to apply or remove the filter
2.  **Control + –** (hold the control key and press the minus key) to delete the selected cells/rows

In the above example, I had only four distinct regions and I could manually select and deselect it from the Filter list (in steps 5 above).

In case you have a lot of categories/regions, you can type the name in the field right above the box (that has these region names), and Excel will show you only those records that match entered text (as shown below). Once you have the text based on which you want to filter, hit the Enter key.

![Enter text in filter filed to get matching records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20546'%3E%3C/svg%3E)

Note that when you delete a row, anything that you may have in other cells in these rows will be lost. One way to get around this is to create a copy of the data in another worksheet and delete the rows in the copied data. Once done, copy it back in place of the original data.

Or

You can use the methods shown later in this tutorial (using the Sort method or the Find All Method)

Also read: [Delete Single or Multiple Rows in Excel](https://trumpexcel.com/delete-rows/)

### Delete Rows Based on a Numeric Condition

Just as I used the filter method to delete all the rows that contain the text Mid-West, you can also use a number condition (or a date condition).

For example, suppose I have the below dataset and I want to delete all the rows where the sale value is less than 200.

Below are the steps to do this:

1.  Select any cell in the data
2.  Click on the Data tab
3.  In the ‘Sort & Filter’ group, click on the Filter icon. This will apply filters to all the headers cells in the dataset![Click on the Filter icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%20198'%3E%3C/svg%3E)
4.  Click on the Filter icon in the Sales header cell (this is a small downward-pointing triangle icon at the top-right of the cell)![Click the filter icon for sales column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20410'%3E%3C/svg%3E)
5.  Hover the cursor over the Number Filters option. This will show you all the number related filter options in Excel.
6.  Click on the ‘Less than’ option.![Click on Less then option in number filters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20527'%3E%3C/svg%3E)
7.  In the ‘Custom Autofilter’ dialog box that opens, enter the value ‘200’ in the field![Enter the number filter value in the dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20225'%3E%3C/svg%3E)
8.  Click OK. This will filter and show only those records where the sales value is less than 200
9.  Select all the filtered records
10.  Right-click on any of the cells and click on Delete Row![Click on Delete Row Option for filtered row based on numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20367'%3E%3C/svg%3E)
11.  In the dialog box that opens, click on OK. At this point, you will see no records in the dataset.![Click OK to delete rows based on the value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20145'%3E%3C/svg%3E)
12.  Click the Data tab and click on the Filter icon. This will remove the filter and you will see all the records except the deleted ones.

There are many number filters that you can use in Excel – such as less than/greater than, equal/does not equal, between, top 10, above or below average, etc.

Note: You can use multiple filters as well. For example, you can delete all the rows where the sales value is greater than 200 but less than 500. In this case, you need to use two filter conditions. The Custom Autofilter dialog box allows having two filter criteria (AND as well as OR).

Just like the number filters, you can also filter the records based on the date. For example, if you want to remove all the records of the first quarter, you can do that by using the same steps above. When you’re working with Date filters, Excel automatically shows you relevant filters (as shown below).

![Date Filter in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20749'%3E%3C/svg%3E)

While filtering is a great way to quickly delete rows based on a value or a condition, it has one drawback – it deletes the entire row. For example, in the below case, it would delete all the data which is to the right of the filtered dataset.

What if I only want to delete records from the dataset, but want to keep the remaining data intact.

You can’t do that with filtering, but you can do that with sorting.

Sort the Dataset and Then Delete the Rows
-----------------------------------------

Although [sorting](https://trumpexcel.com/sort-excel/)
 is another way to delete rows based on value, but in most cases, you’re better off using the filter method covered above.

This sorting technique is recommended only when you want to delete the cells with the values and not the entire rows.

Suppose you have a dataset as shown below and you want to delete all the records where the region is Mid-west.

Below are the steps to do this using sorting:

1.  Select any cell in the data
2.  Click on the Data tab
3.  In the Sort & Filter group, click on the Sort icon.![Click the Sort Icon in the data tab in Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20155'%3E%3C/svg%3E)
4.  In the Sort dialog box that opens, select Region in the sort by column.![Select Region as the basis to sort and delete rows1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
5.  In the Sort on option, make sure Cell Values is selected![Make Sure Cells Values is selected as the basis to sort the data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
6.  In Order option, select A to Z (or Z to A, doesn’t really matter).
7.  Click OK. This will give you the sorted data set as shown below (sorted by column B).![Data After Sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20408'%3E%3C/svg%3E)
8.  Select all the records with the region Mid-West (**all the cells in the rows, not just the region column**)
9.  Once selected, right-click and then click on Delete. This will open the Delete dialog box.![Right and click on Delete after selecting all the cells of the records you want to delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20408'%3E%3C/svg%3E)
10.  Make sure the ‘Shift cells up’ option is selected.![Click on Shift Cells Up option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20230'%3E%3C/svg%3E)
11.  Click OK.

The above steps would delete all the records where the region was Mid-West, but it doesn’t delete the entire row. So, if you have any data on the right or left of your dataset, it will remain unharmed.

In the above example, I have sorted the data based on the cell value, but you can also use the same steps to sort based on numbers, dates, cell color or font color, etc.

Here is a detailed guide on [how to sort data in Excel](https://trumpexcel.com/sort-excel/)

In case you want to keep the original data set order but remove the records based on criteria, you need to have a way to sort the data back to the original one. To do this, add a column with serial numbers before sorting the data. Once you’re done with deleting the rows/records, simply sort based using this extra column you added.

Find and Select the Cells Based on Cell Value and Then Delete the Rows
----------------------------------------------------------------------

Excel has a Find and Replace functionality that can be great when you want to find and select cells with a specific value.

Once you have selected these cells, you can easily delete the rows.

Suppose you have the dataset as shown below and you want to delete all the rows where the region is Mid-West.

Below are the steps to do this:

1.  Select the entire dataset
2.  Click the Home tab![Click the Home Tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20198'%3E%3C/svg%3E)
3.  In the Editing group, click on the ‘Find & Select’ option and then click on Find (you can also use the keyboard shortcut Control + F).![Click on FIND](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20224%20286'%3E%3C/svg%3E)
4.  In the Find and Replace dialog box, enter the text ‘Mid-West’ in the ‘Find what:’ field.![Enter the region in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
5.  Click on Find All. This will instantly show you all the instances of the text Mid-West that Excel was able to find.![Click on Find All](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
6.  Use the keyboard shortcut Control + A to select all the cells that Excel found. You will also be able to see all the selected cells in the dataset.![Select all the records where the search term is found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20445'%3E%3C/svg%3E)
7.  Right-click on any of the selected cells and click on Delete. This will open the Delete dialog box.![Delete all the rows based on the term that was searched for](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20478'%3E%3C/svg%3E)
8.  Select the ‘Entire row’ option![Click on Entire row to delete all selected rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20230'%3E%3C/svg%3E)
9.  Click OK.

The above steps would delete all the cells where the region value is Mid-west.

Note: Since Find and Replace can handle [wild card characters](https://trumpexcel.com/excel-wildcard-characters/)
, you can use these when finding data in Excel. For example, if you want to delete all the rows where the region is either Mid-West or South-West, you can use ‘**\*West**‘ as the text to find in the Find and Replace dialog box. This will give you all the cells where the text ends with the word West.

Delete All Rows With a Blank Cell
---------------------------------

In case you want to delete all the rows where there are blank cells, you can easily do this with an inbuilt functionality in Excel.

It’s the **Go-To Special Cells** option – which allows you to quickly select all the blank cells. And once you have selected all the blank cells, deleting these is super simple.

Suppose you have the dataset as shown below and I want to delete all the rows where I don’t have the sale value.

Below are the steps to do this:

1.  Select the entire dataset (A1:D16 in this case).
2.  Press the **F5** key. This will open the ‘Go To’ dialog box (You can also get this dialog box from Home –> Editing –> Find and Select –> Go To).
3.  In the ‘Go To’ dialog box, click on the Special button. This will open the ‘Go To Special’ dialog box![Click on Special button in Go To dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20347'%3E%3C/svg%3E)
4.  In the Go To Special dialog box, select ‘Blanks’.![Select Blanks option to select all blank cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)
5.  Click OK.

The above steps would select all the cells that are blank in the dataset.

Once you have the blank cells selected, right-click on any of the cells and click on Delete.

![Click on delete to remove all rows with blank cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20773%20476'%3E%3C/svg%3E)

In the Delete dialog box, select the ‘Entire row’ option and click OK. This will delete all rows that have blank cells in it.

![Click on Entire row to delete all selected rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20230'%3E%3C/svg%3E)

If you’re interested in learning more about this technique, I wrote a detailed tutorial on [how to delete rows with blank cells](https://trumpexcel.com/delete-blank-rows-excel/)
. It includes the ‘Go To Special’ method as well as a VBA method to delete rows with blank cells.

Filter and Delete Rows Based On Cell Value (using VBA)
------------------------------------------------------

The last method that I am going to show you include a little bit of VBA.

You can use this method if you often need to delete rows based on a specific value in a column. You can add the VBA code once and add it your [Personal Macro workbook](https://trumpexcel.com/personal-macro-workbook/)
. This way it will be available for use in all of your Excel workbooks.

This code works the same way as the Filter method covered above (except the fact that this does all the steps in the backend and save you some clicks).

Suppose you have the dataset as shown below and you want to delete all the rows where the region is Mid-West.

Below is the VBA code that will do this.

Sub DeleteRowsWithSpecificText()
'Source:https://trumpexcel.com/delete-rows-based-on-cell-value/
ActiveCell.AutoFilter Field:=2, Criteria1:="Mid-West"
ActiveSheet.AutoFilter.Range.Offset(1, 0).Rows.SpecialCells(xlCellTypeVisible).Delete
End Sub

The above code uses the [VBA Autofilter](https://trumpexcel.com/vba-autofilter/)
 method to first filter the rows based on the specified criteria (which is ‘Mid-West’), then select all the filtered rows and delete it.

Note that I have used Offset in the above code to make sure my header row is not deleted.

The above code doesn’t work if your data is in an [Excel Table](https://trumpexcel.com/excel-table/)
. The reason for this is that Excel considers an Excel Table as a list object. So if you want to delete rows that are in a Table, you need to modify the code a bit (covered later in this tutorial).

Before deleting the rows, it will show you a prompt as shown below. I find this useful as it allows me to double-check the filtered row before deleting.

Remember that when you delete rows using VBA, you can’t undo this change. So use this only when you’re sure that this works the way you want. Also, it’s a good idea to keep a backup copy of the data just in case anything goes wrong.

In case your data is in an Excel Table, use the below code to delete rows with a specific value in it:

Sub DeleteRowsinTables()
'Source:https://trumpexcel.com/delete-rows-based-on-cell-value/
Dim Tbl As ListObject
Set Tbl = ActiveSheet.ListObjects(1)
ActiveCell.AutoFilter Field:=2, Criteria1:="Mid-West"
Tbl.DataBodyRange.SpecialCells(xlCellTypeVisible).Delete
End Sub

Since VBA considers Excel Table as a List object (and not a range), I had to change the code accordingly.

**Where to Put the VBA code?**

This code needs to be placed in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
 backend in a module.

Below are the steps that will show you how to do this:

1.  Open the workbook in which you want to add this code.
2.  Use the keyboard shortcut ALT + F11 to open the VBA Editor window.
3.  In this VBA Editor window, on the left, there is a ‘Project Explorer’ pane (which lists all the workbooks and worksheets objects). Right-click on any object in the workbook (in which you want this code to work), hover the cursor over ‘Insert’ and then click on ‘Module’. This will add the Module object to the Workbook and also open the Module code window on the right
4.  In the module window (that will appear on the right), copy and paste the above code.

Once you have the code in the VB Editor, you can run the code by using any of the below methods (make sure you have the selected any cell in the dataset on which you want to run this code):

1.  Select any line within the code and hit the F5 key.
2.  Click on the Run button in the toolbar in the VB Editor
3.  Assign the macro to a button or a shape and run it by clicking on it in the worksheet itself
4.  Add it to the Quick Access Toolbar and run the code with a single click.

You can read all about [how to run the macro code in Excel](https://trumpexcel.com/run-a-macro-excel/)
 in this article.

Note: Since the workbook contains a VBA macro code, you need to save it in the macro-enabled format (xlsm).

**You may also like the following Excel tutorials:**

*   [How to Delete Every Other Row in Excel](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [How to Delete a Pivot Table in Excel](https://trumpexcel.com/delete-pivot-table/)
    
*   [How to Delete Every Other Row in Excel](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [How to Move Rows and Columns in Excel (The Best and Fastest Way)](https://trumpexcel.com/move-rows-columns/)
    
*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Insert Multiple Rows in Excel](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    
*   [Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
    
*   [Remove Empty Rows Using a Formula](https://trumpexcel.com/remove-blank-rows-formula/)
    
*   [How to Quickly Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [Hide Zero Values in Excel](https://trumpexcel.com/hide-zero-values-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “Delete Rows Based on a Cell Value (or Condition) in Excel \[Easy Guide\]”
----------------------------------------------------------------------------------------

1.  I was unsuccessful in getting the code to work for me using VBA for the code provided. I’m not sure where my error is, but it doesn’t delete anything and it also doesn’t show anything for the Module when I entered it and saved it. Please help.
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-14874)
    
2.  Thank you, you’ve helped me save time.
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-14820)
    
3.  Thanks for this. This is very useful to me. I have been looking for something like this without using a userform. I added this last line to clear the filter – ActiveSheet.ListObjects(“Table1”).Range.AutoFilter Field:=2
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-14585)
    
4.  Hello Sumit,  
    It’s really nice to learn from the site as usual.  
    I am working on data where i have angle in column, i need to keep angle in multiples of 0.1,0.2,.3 i. e. in increment of 0.1 deg only & delete other rows in between. I am not getting which conditional formatting options I should use.  
    Please help me to resolve it.
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-14295)
    
5.  While not a big deal, how do you keep from deleting the header row. Unless I’m missing something using the filter keeps the header visible then when you select only visible cells, the header row is also selected and then deleted along with the data? I’m using Office 365 on Windows 10 Enterprise.
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-13465)
    
6.  Side note: the ads on your well-done website use “ad.doubleclick.net” and this company plants a file that constantly shows up for users to download. It’s called “f.txt”. You should be aware of this and not support ads from this company!!!
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-12246)
    
7.  I have found (from bitter experience) that when working with a largish dataset (>10000 rows), deleting a non-contiguous filtered set of cells can take a very long time (many minutes)  
    Sorting the data first (so that the rows to be deleted are contiguous) is, by comparison, almost instantaneous
    
    [Reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#comment-12244)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/delete-rows-based-on-cell-value/#respond)

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