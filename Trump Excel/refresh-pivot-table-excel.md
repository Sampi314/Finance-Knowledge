# How to Refresh Pivot Table in Excel (Manually + Auto-Refresh with VBA)

**Source:** https://trumpexcel.com/refresh-pivot-table-excel

---

[Skip to content](https://trumpexcel.com/refresh-pivot-table-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/refresh-pivot-table-excel/#below-title)

Once you have [created a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
, it doesn’t automatically refresh when you add new data or change the existing data.

Since your Pivot Table is created using the [Pivot Cache](https://trumpexcel.com/pivot-cache-excel/)
, when the existing data changes or when you add new rows/columns to the data, the Pivot Cache does not update itself automatically, and hence, the Pivot Table also does not update.

You need to force a refresh every time there are changes. Once you force a refresh, the Pivot Cache gets updated, which is reflected in the Pivot Table.

This tutorial covers a couple of ways to do this.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/refresh-pivot-table-excel/#)

Refresh Pivot Table
-------------------

This option is best suited when there are changes in the existing data source and you want to refresh the pivot table to reflect these changes.

Here are the steps to refresh a Pivot Table:

*   Right-click on any cell in the Pivot Table.
*   Select Refresh.

![Refresh Pivot Table in Excel - Refresh](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20272'%3E%3C/svg%3E)

This will instantly refresh the Pivot Table.

You can also by selecting any cell in the Pivot Table and use the [keyboard shortcut](https://trumpexcel.com/pivot-table-shortcuts/)
 ALT + F5.

**Quick Tip:** It’s a good practice to convert the data source into an [Excel Table](https://trumpexcel.com/excel-table/)
, and use this Excel Table to create the Pivot Table. If you do this, you can also use the refresh technique to update the Pivot Table even when new data (rows/columns) are added to the data source (since an Excel Table automatically accounts for new rows/columns that are added).

Update Pivot Table by Changing the Data Source
----------------------------------------------

If you’ve added new rows/columns to the data source, you need to change the data source to make sure new rows/columns are a part of the dataset.

To do this:

*   Select any cell in the Pivot Table.
*   Go to Analyze –> Data –> Change Data Source. This will select the data source that you have used and will open the ‘Change PivotTable Data Source’ dialog box.![Refresh Pivot Table in Excel - Analyze Change Data Source](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20174'%3E%3C/svg%3E)
*   In the Change PivotTable Data Source dialog box, update the range to include new data.![Refresh Pivot Table in Excel - Change Data Source](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20224'%3E%3C/svg%3E)
*   Click OK.

_Note that if you change the data source into an Excel Table and then use the Excel table to create the Pivot Table, you don’t need to use the change data source option. You can simply refresh the Pivot Table and it’ll account for the new rows/columns._

Autorefresh Pivot Table Using a VBA Macro
-----------------------------------------

While refreshing a Pivot table is as easy as two clicks, you still need to do this every time there is a change.

To make it more efficient and auto-refresh the Pivot Table whenever there is a change in the data source, you can use a simple one-line VBA macro code.

Here is the VBA code:

Private Sub Worksheet\_Change(ByVal Target As Range)
Worksheets("Sheet1").PivotTables("PivotTable1").PivotCache.Refresh
End Sub

**Decoding the Code:** This is a change event which gets triggered whenever there is a change in the sheet that contains the source data. As soon as there is a change, the code refreshes the Pivot Cache of the Pivot Table with the name PivotTable1.

You need to modify this code to make it work for your workbook:

![Refresh Pivot Table in Excel - Macro Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20146'%3E%3C/svg%3E)

*   “Sheet1” – change this part of the code with the [name of the sheet](https://trumpexcel.com/get-sheet-name-excel/)
     that has the Pivot Table.
*   “PivotTable1” – change this to the name of your Pivot Table. To know the name, click anywhere in the Pivot Table and click the Analyze Tab. The name would be visible in the left part of the ribbon under the ‘PivotTable Name’ header.

**Where to put this VBA code:**

*   Press Alt + F11. It will open the VB Editor window.
*   In the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    , there would be Project explorer on the left (that has the names of all the worksheets). If it’s not there, press Control + R to make it visible.![Refresh Pivot Table in Excel - VBA Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20354'%3E%3C/svg%3E)
*   In the Project Explorer, double-click on the sheet name that contains the Pivot Table.
*   In the code window on the right, copy paste the given code.![Refresh Pivot Table in Excel - Autorefresh Code in window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20868%20264'%3E%3C/svg%3E)
*   Close the VB Editor.

Now when you change anything in the data source, the Pivot Table would automatically get refreshed.

**[Click here](https://www.dropbox.com/s/rjjywr6dktiwirf/Pivot-Table-Autorefresh.xlsm?dl=1)
** to download the example file.

Note: Since there is a macro in the workbook, save this with .xls or .xlsm extension.

**You May Also Like the Following Pivot Table Tutorials:**

*   [How to Group Dates in Pivot Tables in Excel.](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    .
*   [How to Filter Data in a Pivot Table in Excel](https://trumpexcel.com/filter-data-pivot-table-excel/)
    .
*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    .
*   [How to Apply Conditional Formatting in a Pivot Table in Excel.](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Field](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    .
*   [Using Slicers in Excel Pivot Table.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [Move Pivot Table to Different Worksheet or Workbook](https://trumpexcel.com/move-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Refresh Pivot Table in Excel (Manually + Auto-Refresh with VBA)”
--------------------------------------------------------------------------------------

1.  Hi,  
    This isnt working.. file is in xlsm format… enabled macros..
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    Worksheets(“Summary”).PivotTables(“PivotTable1”).PivotCache.Refresh  
    End Sub
    
    Summary=name of sheet having pivot table.  
    PivotTable1=Name of pivot table.
    
    [Reply](https://trumpexcel.com/refresh-pivot-table-excel/#comment-47523)
    
2.  Love your Tutorials, learn a lot from you
    
    [Reply](https://trumpexcel.com/refresh-pivot-table-excel/#comment-33182)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/refresh-pivot-table-excel/#respond)

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