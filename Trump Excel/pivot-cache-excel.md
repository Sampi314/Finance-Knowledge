# Pivot Cache in Excel - What Is It and How to Best Use It

**Source:** https://trumpexcel.com/pivot-cache-excel

---

[Skip to content](https://trumpexcel.com/pivot-cache-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/pivot-cache-excel/#below-title)

If you work with Excel Pivot Tables, Pivot Cache is something you should definitely know about.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/pivot-cache-excel/#)

What is Pivot Cache?
--------------------

Pivot Cache is something that automatically gets generated when you [create a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
.

It is an object that holds a replica of the data source. While you can’t see it, it is a part of the workbook and is connected to the Pivot Table. When you make any changes in the Pivot Table, it does not use the data source, rather it uses the Pivot Cache.

![Pivot Cache in Pivot Table - Flow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20220'%3E%3C/svg%3E)The reason a pivot cache gets generated is to optimize the pivot table functioning. Even when you have thousands of rows of data, a pivot table is super fast in summarizing it. You can drag and drop items in the rows/columns/values/filters boxes and it will instantly update the results.

Pivot Cache enables this fast functioning of a pivot table.

While you think that you are directly linked to the source data, in reality, you access the pivot cache (and not the source data) when you make changes in the pivot table.

This is also the reason you need to refresh the pivot table to reflect any changes made in the data set.

Pivot Cache Side Effects
------------------------

One downside of pivot cache is that it increases the size of your workbook.

Since it’s a replica of the source data, when you create a pivot table, a copy of that data gets stored in the Pivot Cache.

When you use large data sets to create a pivot table, the workbook file size increases significantly.

Sharing the Pivot Cache
-----------------------

From Excel 2007 onwards, if you already have a pivot table, and you create an additional pivot table using the same source data, Excel automatically shares the pivot cache (which means that both the pivot tables use the same pivot cache). This is helpful as it avoids pivot cache duplication and in turn, results in less memory usage and [reduced file size](https://trumpexcel.com/reduce-excel-file-size/)
.

**Limitations of Shared Pivot Cache**

While a shared pivot cache improves pivot table functioning and memory usage, it suffers from the following limitations:

*   When you refresh one pivot table, all the pivot tables linked to the same cache gets refreshed.
*   When you group fields in one of the pivot tables, it is applied to all the pivot tables using the same pivot cache. For example, if you group dates by months, this change will be reflected in all the pivot tables.
*   When you insert a calculated field/item in one of the Pivot Table, it shows up in all the pivot tables that are sharing the pivot cache.

The way around these limitations is to force Excel to create separate pivot cache for different pivot tables (while using the same data source).

_Note: If you are using different data sources for different pivot tables, Excel would automatically generate separate Pivot Caches for it._

Creating Duplicate Pivot Cache (with the same Data Source)
----------------------------------------------------------

Here are 3 ways to create duplicate pivot cache while creating pivot tables from the same data source:

**#1 Using Different Table Names**

*   Click anywhere in the data source and go to Insert –> Table _(or you can use the keyboard shortcut – Control + T)_.![Pivot Cache in Pivot Table Excel - Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20126'%3E%3C/svg%3E)
*   In the Create Table dialogue box, click OK. It will create a Table with the name Table1_._![Pivot Cache in Pivot Table Excel - Create Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20239%20156'%3E%3C/svg%3E)
*   With any cell selected in the table, Go to Insert –> Pivot Table.![Pivot Cache in Pivot Table Excel - Insert Pivot](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20224%20126'%3E%3C/svg%3E)
*   In the Create Pivot Table dialogue box, you would notice that in the Table/Range field has the name of the table. Click OK.
    *   This will create the first pivot table.![Pivot Cache in Pivot Table Excel - Table1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20335'%3E%3C/svg%3E)
*   Go to the data source (table), select any cell and Go to Table Tools Design –> Tools –> Convert to Range. It will show a prompt asking if you want to convert Table to Normal Range. Click on Yes. This will convert the table into regular tabular data.![Pivot Cache in Pivot Table Excel - Convert to Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20639%2099'%3E%3C/svg%3E)

Now repeat the steps above, and just change the Table Name (from Table1 to Table2 or whatever you want). You can change it by entering the name in the field below Table Name in the Table Tools Design tab.

![Pivot Cache in Pivot Table Excel - Change Table Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%2099'%3E%3C/svg%3E)

Although both the tables (Table1 and Table2) refer to the same data source, this method ensures that two separate pivot caches are generated for each table.

**#2 Using Old Pivot Table Wizard**

Use these steps when you want to create an additional pivot table with a separate pivot cache while using the same data source.

*   Select any cell in the data and press ALT + D + P.
    *   This will open the Pivot Table and Pivot Chart Wizard.
*   In Step 1 of 3, click on Next.![Pivot Cache in Pivot Table Excel - Wizard 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20256'%3E%3C/svg%3E)
*   In Step 2 of 3, make sure that the data range is correct and click on Next.![Pivot Cache in Pivot Table Excel - Wizard 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20125'%3E%3C/svg%3E)
*   Excel shows a prompt that essentially says click on Yes to create a shared pivot cache and No to create a separate pivot cache.![Pivot Cache in Pivot Table Excel - Wizrd Prompt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20798%20171'%3E%3C/svg%3E)
*   Click No.
*   In Step 3 of the Wizard, select if you want the Pivot table in a new worksheet or the same worksheet and then click on Finish.![Pivot Cache in Pivot Table Excel - Step 3 Wizard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20246'%3E%3C/svg%3E)

_Note: Make sure the data is not an Excel table._

Count the Number of Pivot Caches
--------------------------------

You may want to count the number of pivot caches just to avoid multiple pivot caches from the same data source.

Here is a quick way to count it:

*   Press ALT + F11 to open the VB Editor (or go to [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     –> Visual Basic).![Pivot Cache in Pivot Table Excel - VB](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20125'%3E%3C/svg%3E)
*   In the Visual Basic Editor Menu, click on View and select [Immediate Window](https://trumpexcel.com/vba-immediate-window/)
     (_or press Control + G_). This will make the Immediate Window visible.![Pivot Cache in Pivot Table Excel - Immediate Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20245'%3E%3C/svg%3E)
*    In the Immediate Window, paste the following code and press Enter:
    
    ?ActiveWorkbook.PivotCaches.Count![Pivot Cache in Pivot Table Excel - Immediate Window Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20174'%3E%3C/svg%3E)
    

It will instantly show the number of Pivot Caches in the workbook.

Improving Performance while Working with Pivot Tables
-----------------------------------------------------

There are a couple of things you can do to improve the performance of workbooks (file size and memory usage) while you work with Pivot Tables:

**#1 Delete the Source Data**

You can delete the source data and use the Pivot Cache only. You will still be able to do everything using the pivot cache as it holds a snapshot of the original data. But since you have deleted the source data, your workbook file size would reduce.

![Pivot Cache in Pivot Table - Size Difference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20602%2097'%3E%3C/svg%3E)

In case you want to get back the source data, simply double-click on the intersection of Grand Totals for that pivot table. It will create a new worksheet and show all the data used to create that pivot table.

![Pivot Cache in Pivot Table - Double Click on Intersection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20236'%3E%3C/svg%3E)

**#2 Don’t Save the Data in Pivot Cache**

When you save a file with a pivot table and source data, it also saves the pivot cache that has a copy of the source data. This means that you are saving the source data in two places: in the worksheet that has the data and in the pivot cache.

There is an option to not save the data in the cache and close it. This will lead a lower file size.

To do this:

*   Select any cell in the Pivot Table.
*   Go to Analyze –> Pivot Table –> Options.![Pivot Cache in Pivot Table Excel - Analyze Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20649%20100'%3E%3C/svg%3E)
*   In the Pivot Table Options dialogue box, go to the Data Tab.![Pivot Cache in Pivot Table Excel - Data Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20310'%3E%3C/svg%3E)
*   Uncheck the Option – Save Source Data with File.![Pivot Cache in Pivot Table Excel - Data Uncheck Save](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20296'%3E%3C/svg%3E)
*   Check the option – Refresh Data when opening the file.
    *   If you do not check this option, when you open the Excel Workbook, it will not refresh the data and you will not be able to use the Pivot Table functionalities. To make it work, you will have to manually refresh the pivot table.![Pivot Cache in Pivot Table Excel - Check Refresh](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20305'%3E%3C/svg%3E)

When you do this, Excel will not save the data in the pivot cache, but it will refresh it when you open the Excel workbook the next time. Your data can be in the same workbook, some other workbook, or an external database. When you open the file, it refreshes the data and Pivot Cache is recreated.

While this may lead to lower file size, it can take a bit longer to open the file (as Excel recreates the cache).

**See Also**: [Saving Source Data with Pivot Table](http://www.pivot-table.com/2015/01/28/saving-source-data-with-pivot-table-file/)
.

_Note: If you use this option, make sure you have the data source intact. If you delete the source data (from the workbook or any external data source), then you will not be able to recreate the pivot cache._

**#3 Sharing the Pivot Cache for better performance**

If by accident (or intentionally) you end up in a situation when you have duplicate pivot cache and you want to delete the duplicate and share the pivot cache, here are the steps to do it:

*   [Delete one of the Pivot Tables](https://trumpexcel.com/delete-pivot-table/)
     for which you want to delete the cache. To do this, Select the pivot table and go to Home –> Clear –> Clear All.![Pivot Cache in Pivot Table Excel - Clear All](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20280'%3E%3C/svg%3E)
*   Now simply copy the Pivot Table that you want to duplicate and paste it (either in the same worksheet or in a separate worksheet).
    *   It is recommended to paste it in separate worksheets so that it does not overlap with the other pivot table when you expand it. Although, I sometimes copy it side by side to compare different views. This copy pasting of the pivot table makes sure that the pivot cache is shared.![Pivot Cache in Pivot Table - Copy Pivot Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20152'%3E%3C/svg%3E)

**Related Readings:**

*   [Microsoft Help – Unshare a data cache between PivotTable reports](https://support.office.com/en-in/article/Unshare-a-data-cache-between-PivotTable-reports-87188806-0c24-4d17-b2f7-9e3a4a05542b)
    .

**Other Pivot Table Tutorials You May Like:**

*   [Preparing Source Data For Pivot Table.](https://trumpexcel.com/source-data-for-pivot-table/)
    
*   [How to Group Dates in Pivot Tables in Excel.](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    .
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    .
*   [Using Slicers in Excel Pivot Table.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Field](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [How to Apply Conditional Formatting in a Pivot Table in Excel.](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [Connect a Single Slicer to Multiple Pivot Tables in Excel](https://trumpexcel.com/connect-slicer-to-multiple-pivot-tables/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Pivot Cache in Excel – What Is It and How to Best Use It”
------------------------------------------------------------------------

1.  awsome explanation..
    
    [Reply](https://trumpexcel.com/pivot-cache-excel/#comment-14701)
    
2.  EXCELLENT CONTENT!!  
    The author has good communication skills as well!!  
    Deserves big CLAP.
    
    [Reply](https://trumpexcel.com/pivot-cache-excel/#comment-14060)
    
3.  Why is it that sometimes excel will allow me to break the pivot cache when I do the Alt D P, and other times there is no pop up asking me?
    
    [Reply](https://trumpexcel.com/pivot-cache-excel/#comment-10406)
    
4.  Instead of doing all of that to have another pivot table use the same pivot cache, couldn’t you just add a whole new pivot from the source data and do “#2 Don’t Save the Data in Pivot Cache”? The would effectively get rid of both pivot caches, right?
    
    [Reply](https://trumpexcel.com/pivot-cache-excel/#comment-10096)
    
5.  Hi,  
    Amazing tutorial by far I could find in the internet.  
    By the way, I’m wondering if is possible to do an interactive graph depending on the group I choose?
    
    [Reply](https://trumpexcel.com/pivot-cache-excel/#comment-3307)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/pivot-cache-excel/#respond)

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