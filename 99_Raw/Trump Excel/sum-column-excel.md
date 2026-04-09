# How to Sum a Column in Excel (5 Really Easy Ways)

**Source:** https://trumpexcel.com/sum-column-excel

---

[Skip to content](https://trumpexcel.com/sum-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-column-excel/#below-title)

To get the sum of an entire column is something most of us have to do quite often. For example, if you have the sales data to date, you may want to quickly know the total sum in the column to the sales value till the present day.

You may want to quickly see what the total sum is or you may want is as a formula in a separate cell.

This Excel tutorial will cover a couple of quick and fast methods to sum a column in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-column-excel/#)

Select and Get the SUM of the Column in Status Bar
--------------------------------------------------

Excel has a [status bar](https://trumpexcel.com/status-bar-excel/)
 (at the bottom right of the Excel screen) which displays some useful statistics about the selected data, such as Average, Count, and SUM.

Suppose you have a dataset as shown below and you want to quickly know the sum of the sales for the given weeks.

![Weekly Sales Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20223%20335'%3E%3C/svg%3E)

To do this, [select the entire Column](https://trumpexcel.com/select-entire-column-excel/)
 B (you can do that by clicking on the B alphabet at the top of the column).

![Select the entire column to get the sum of the values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20358'%3E%3C/svg%3E)

As soon as you select the entire column, you will notice that the status bar shows you the SUM of the column.

![Sum value of the selected cells in the satus bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%2050'%3E%3C/svg%3E)

This is a really quick and easy way to get the sum of an entire column.

The good thing about using the status bar to get the sum of the column is that it ignores the cells that have the text and only considers the numbers. In our example, cell B1 has the text title, which is ignored and the sum of the column is displayed in the status bar.

In case you want to get the sum of multiple columns, you can make the selection, and it will show you the total sum value of all the selected columns.

In case you don’t want to select the entire column, you can make a range selection, and the status bar will show the sum of the selected cells only.

One negative of using the status bar to get the sum is that you can not copy this value.

If you want, you can customize the status bar and get more data such as the maximum or the minimum value from the selection. To do this, right-click on the status bar and make the customizations.

Get the SUM of a Column with AutoSum (with a Single-click/Shortcut)
-------------------------------------------------------------------

[Autosum](https://trumpexcel.com/autosum-shortcut-excel/)
 is a really awesome tool that allows you to quickly get the sum of an entire column with a single click.

Suppose you have the dataset as shown below and you want to get the sum of the values in column B.

Below are the steps to get the sum of the column:

1.  Select the cell right below the last cell in the column for which you want the sum![Select the cell where you want the sum](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20233%20373'%3E%3C/svg%3E)
2.  Click the Formula tab![Click the Formulas tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20198'%3E%3C/svg%3E)
3.  In the Function Library group, click on the Autosum option![Click the Autosum option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20198'%3E%3C/svg%3E)

The above steps would instantly give you the sum of the entire column in the selected cell.

You can also use the Auto-sum by selecting the column that has the value and hitting the auto-sum option in the formula tab. As soon as you do this, it will give you the auto-sum in the cell below the selection.

![Get the Sum using Autosum after selecting the column data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20592'%3E%3C/svg%3E)

**Note**: Autosum automatically detects the range and includes all the cells in the SUM formula. If you select the cell which has the sum and look at the formula in it, you will notice that it refers to all the cells above it in the column.

One minor irritant when using Autosum is that it would not identify the correct range in case there are any empty cells in the range or any cell has the text value. In the case of the empty cell (or text value), the auto-sum range would start below this cell.

**Pro Tip**: You can also use the Autosum feature to get the sum of columns as well as rows. In case your data is in a row, simply select the cell after the data (in the same row) and click on the Autosum key.

### AutoSum Keyboard Shortcut

While using the Autosum option in the Formula tab is fast enough, you can make getting the SUM even faster with a keyboard shortcut.

To use the shortcut, select the cell where you want the sum of the column and use the below shortcut:

**ALT =** (hold the ALT key and press the equal to key)

Using the SUM Function to Manually calculate the Sum
----------------------------------------------------

While the auto-sum option is fast and effective, in some cases, you may want to calculate the sum of columns (or rows) manually.

One reason for doing this could be when you don’t want the sum of the entire column, but only of some of the cells in the column.

In such a case, you can use the [SUM function](https://trumpexcel.com/excel-sum-function/)
 and manually specify the range for which you want the sum.

Suppose you have a dataset as shown below and you want the sum of the values in column B:

![Weekly Sales Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20223%20335'%3E%3C/svg%3E)

Below are the steps to use the SUM function manually:

1.  Select the cell where you want to get the sum of the cells/range
2.  Enter the following: =SUM(![Enter the SUM formula manually in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20396'%3E%3C/svg%3E)
3.  Select the cells that you want to sum. You can use the mouse or can use the arrow key (with arrow keys, hold the shift key and then use the arrow keys to select range of cells).![Select the range of cells for the SUM formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20397'%3E%3C/svg%3E)
4.  Hit the Enter key.![SUM formula to sum a column in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20424'%3E%3C/svg%3E)

The above steps would give you the sum of the selected cells in the column.

You can also [create and use named ranges](https://trumpexcel.com/named-ranges-in-excel/)
 in the SUM function to quickly get the sum value. This could be useful when you have data spread on a large spreadsheet and you want to quickly get the sum of a column or range. You would first need to create a named range and then you can use that range name to get the sum.

Below is an example where I have named the range – _Sales_. The below formula also gives me the sum of the sales column:

\=SUM(Sales)

![Sum a column using named range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20436'%3E%3C/svg%3E)

Note that when you use the SUM function to get the sum of a column, it will also include the filtered or hidden cells.

In case you want the hidden cells to not be included when summing a column, you need to use the SUBTOTAL or AGGREGATE function (covered later in this tutorial).

Also read:  [How to Sum Across Multiple Sheets in Excel?](https://trumpexcel.com/sum-across-multiple-sheets-excel/)

Sum Only the Visible Cells in a Column
--------------------------------------

In case you have a dataset where you have filtered cells or hidden cells, you can not use the SUM function.

Below is an example of what can go wrong:

![SUM Function calculates hidden and filtered cells as well](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20272'%3E%3C/svg%3E)

In the above example, when I sum the visible cells, it gives me the result as 2549, **while the actual result of the sum of visible cells would be 2190**.

The reason we get the wrong result is that the SUM function also takes the filtered/hidden cells when calculating the sum of a column.

In case you only want to get the sum of visible cells, you can’t use the SUM function. In this case, you need to use the AGGREGATE or SUBTOTAL function.

If you’re using Excel 2010 or higher versions, you can use the AGGREGATE function. It does everything that the SUBTOTAL function does, and a little more. In case you’re using earlier versions, then you can use the SUBTOTAL function to get the SUM of visible cells only (i.e., it ignores filtered/hidden cells).

Below is the formula you can use to get the sum of only the visible cells in a column:

\=AGGREGATE(9,3,B2:B6)

![Using Aggregate function to get sum of filtered cells in a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20281'%3E%3C/svg%3E)

The Aggregate function takes the following arguments:

*   **function\_num**: This is a number that tells the AGGREGATE function the calculation that needs to be done. In this example, I have used 9 as I want the sum.
*   **options**: In this argument, you can specify what you want to ignore when doing the calculation. In this example, I have used 3, which ‘Ignores hidden row, error values, nested SUBTOTAL, and AGGREGATE functions’. In short, it only uses the visible cells for the calculation.
*   **array**: This is the range of cells for which you want to get the value. In our example, this is B2:B6 (which also has some hidden/filtered rows)

In case you’re using Excel 2007 or prior versions, you can use the following Excel formula:

\=SUBTOTAL(9,B2:B6)

Below is a formula where I show how to sum a column when there are filtered cells (using the SUBTOTAL function)

Convert Tabular Data to Excel Table to Get the Sum of Column
------------------------------------------------------------

When you convert tabular data to an Excel Table, it becomes really easy to get the sum of columns.

I always recommend converting data into an [Excel table](https://trumpexcel.com/excel-table/)
, as it offers a lot of benefits. And with new tools such as Power Query, Power Pivot, and Power BI working so well with tables, it’s one more reason to use it.

To convert your data into an Excel table, follow the below steps:

1.  Select the data that you want to convert to an Excel Table
2.  Click the Insert tab![Click the Insert tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20198'%3E%3C/svg%3E)
3.  Click on the Table icon![Click on the Table icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20304%20199'%3E%3C/svg%3E)
4.  In the Create Table dialog box, make sure the range is correct. Also, check the option ‘My table has headers’ in case you have headers in your data.![Create Table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20185'%3E%3C/svg%3E)
5.  Click Ok.

The above steps would convert your tabular data into an Excel Table.

The keyboard shortcut to convert to a table is Control + T (hold the control key and press the T key)

Once you have the table in place, you can easily get the sum of all the columns.

Below are the steps to get the sum of the columns in an Excel Table:

1.  Select any cell in the Excel table
2.  Click the Design tab. This is a contextual tab that only appears when you select a cell in the Excel table.![Click the Design tab in Table Tools](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20199'%3E%3C/svg%3E)
3.  In the ‘Table Style Options’ group, check the ‘Total Row’ option![Check the Total Row option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20201'%3E%3C/svg%3E)

The above steps would instantly add a totals row at the bottom of the table and give the sum of all the columns.

![Using Table to Get the Sum of columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20252%20406'%3E%3C/svg%3E)

Another thing to know about using an Excel table is that you can easily change the value from the SUM of the column to Average, Count, Min/Max, etc.

To do this, select a cell in the totals rows and use the [drop-down menu](https://trumpexcel.com/excel-drop-down-list/)
 to select the value you want.

![Change from Sum of column to other values such as Average or Count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20278%20627'%3E%3C/svg%3E)

Get the Sum of Column Based on a Criteria
-----------------------------------------

All the methods covered above would give you the sum of the entire column.

In case you want to only get the sum of those values that satisfy a criterion, you can easily do that with a SUMIF or SUMIFS formula.

For example, suppose you have the dataset as shown below and you only want to get the sum of those values that are more than 500.

You can easily do this using the below formula:

\=SUMIF(B2:B11,">500",B2:B11)

![Using SUMIF to conditionally sum the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20493'%3E%3C/svg%3E)

With the [SUMIF formula](https://trumpexcel.com/excel-sumif-function/)
, you can use a numeric condition as well as a text condition.

For example, suppose you have a dataset as shown below and you want to get the SUM of all the sales done by Mark.

In this case, you can use column A as the criteria range and “Mark” as the criteria, and the formula will give you the sum of all the values for Mark.

The below formula will give you the result:

\=SUMIF(A2:A11,"Mark",B2:B10)

![Add all sale values in the column for Mark](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20492'%3E%3C/svg%3E)

Note: Another way to get the sum of a column that meets a criterion could be to filter the column based on the criteria and then use the AGGREGATE or SUBTOTAL formula to get the sum of visible cells only.

**You may also like the following Excel tutorials:**

*   [How to Sum Positive or Negative Numbers in Excel](https://trumpexcel.com/sum-positive-numbers-excel/)
    
*   [How to Apply Formula to the Entire Column in Excel](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    
*   [How to Compare Two Columns in Excel (for matches and differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [How to Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [How to Count Colored Cells In Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [100+ Excel Functions (explained with examples)](https://trumpexcel.com/excel-functions/)
    
*   [5 Easy Ways to Calculate Running Total in Excel (Cumulative Sum)](https://trumpexcel.com/running-total-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-column-excel/#respond)

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