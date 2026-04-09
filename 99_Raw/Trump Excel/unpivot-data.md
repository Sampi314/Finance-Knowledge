# How to Unpivot Data in Excel using Power Query (aka Get & Transform)

**Source:** https://trumpexcel.com/unpivot-data

---

[Skip to content](https://trumpexcel.com/unpivot-data/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/unpivot-data/#below-title)

**Watch Video – Fastest Way to Unpivot Data in Excel**

Pivot Tables are great when you want to analyze a huge amount of data in seconds. It also allows you to quickly create different views of data by simply dragging and dropping.

And to [create a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
, you need to have the data in a specific Pivot Table ready format.

In many cases, you’re likely to get the [data in formats that are not Pivot Table ready](https://trumpexcel.com/source-data-for-pivot-table/)
.

This often is the case when someone manually collects data and creates a format that is more readable by humans (not Pivot Tables).

Something as shown below:

![Unpivot Data in Excel Using Power Query - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20131'%3E%3C/svg%3E)

The above data format is something you expect to get as an output of a Pivot Table analysis.

Now, what if you want to analyze this same data, and see what were the total sales by each region or by each month.

While this can easily be done using Pivot Tables, unfortunately, you can’t feed the above data into a Pivot Table.

So you need to unpivot data and make it Pivot Table friendly.

![Result when you Unpivot Data using Power Query transformation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%20609'%3E%3C/svg%3E)

While there are some ways to do this using [Excel formula](https://trumpexcel.com/excel-functions/)
 or [VBA](https://trumpexcel.com/excel-vba/)
, Power Query (Get & Transform in Excel 2016) is the best tool to unpivot data.

Unpivot Data Using Power Query
------------------------------

Here are the steps to unpivot data using [Power Query](https://trumpexcel.com/power-query-course/)
:

(If your data is already in an [Excel Table](https://trumpexcel.com/excel-table/)
, start from step 6 onwards)

1.  Select any cell in the dataset.
2.  Go to the Insert Tab.![Insert Tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20294%20159'%3E%3C/svg%3E)
3.  Click on the Table icon.![Click on the Table Icon to create an Excel table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20294%20159'%3E%3C/svg%3E)
4.  In the ‘Create Table’ dialog box, make sure the range is correct. You can modify the range if needed.
5.  Click OK. This will convert your tabular data into an Excel table.![Create Table dialog box in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20185'%3E%3C/svg%3E)
6.  With any cell selected in the Excel Table, click on the Data tab.![Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20479%20154'%3E%3C/svg%3E)
7.  In the Get & Transform data group, click on the ‘From Table/Range’ icon.![click on from table range to create a power query to unpivot data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20479%20154'%3E%3C/svg%3E)
8.  In the Create Table dialog box that opens (if it opens), click on OK. This will open the Query Editor using the Excel Table data.
9.  In the Query editor, right-click on the Region column.![Right click on Region column Power Query to Unpivot Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20827%20191'%3E%3C/svg%3E)
10.  Click on ‘Unpivot Other Columns’ option. This will instantly unpivot your data.![Click on Unpivot Other Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20520'%3E%3C/svg%3E)
11.  Change the name of the ‘Attribute’ column to a more meaningful name, such as ‘Months’.
12.  Once you have the Unpivoted data, it’s a good practice to make sure the data types are all correct. In this example, click on one cell for each column and see the data type in the Transform tab. If needed, you can change the data type as well.![Data Type in the Transform tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20333'%3E%3C/svg%3E)
13.  (Optional) Change the name of your query to ‘Sales’.![Change the name of the query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20329%20318'%3E%3C/svg%3E)
14.  Go to the Home tab (in the query editor).![Home tab in Power Query Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20299%20181'%3E%3C/svg%3E)
15.  Click on Close and Load.![Close and Load Power Query - Load Unpivot Data in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20299%20181'%3E%3C/svg%3E)

The above steps would unpivot your data set using Power Query and put in back in Excel as a Table in a new worksheet.

Now you can use this data to create different views using a Pivot table. For example, you can check the total sale value by month or by region.

Also read: [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)

Refreshing the Query When New Data is Added
-------------------------------------------

This all works fine.

But what happens when new data is added to our original data set.

Let’s say you get data for July which is in the same format as the one with which we started.

Do I need to repeat all the steps again to include this data in my unpivoted dataset?

The answer is NO.

And that is what is so awesome about Power Query. You can continue to add new data (or modify existing data), and Power Query would update it instantly as soon as you refresh it.

Let me show you how.

Suppose below is the new dataset that I get (which has additional data for July):

![July Data to Unpivot in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20659%20136'%3E%3C/svg%3E)

Here are the steps to refresh the already created query and unpivot this data:

1.  Add this new data to your original data that you used to create the query.
2.  Since you’re adding data to the adjacent column of an Excel table, the Excel Table will expand to include this data in it. If it doesn’t by any chance, do it manually by dragging the small inverted ‘L’ icon at the bottom-right of the Excel Table.
3.   Go to the Data tab and click on Queries & Connections. This will show a pane with all the existing queries in it.![Queries and Connections in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20164'%3E%3C/svg%3E)
4.  Right-click on the Sales query in the Queries pane.![Queries Pane that has all the queries at one place](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20204'%3E%3C/svg%3E)
5.  Click on Refresh.![Refresh Power Query to Unpivot Data in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20315'%3E%3C/svg%3E)

That’s it! Your new data is instantly unpivoted and added to the existing data.

You would notice that the number of rows shown in the Query updates to show you the new numbers. In this example, it was 24 before the refresh and became 28 after the refresh.

This also means that if you have created any Pivot Tables using the data you got from Power Query, those Pivot Tables would also refresh to show you the updated results.

**You May Also Like the Following Excel Tutorials:**

*   [Combine Data from Multiple Workbooks in Excel (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel.](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [Get a List of File Names from Folders & Sub-folders (using Power Query)](https://trumpexcel.com/list-file-names-power-query/)
    .
*   [Merge Tables in Excel Using Power Query.](https://trumpexcel.com/merge-tables/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Field](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Unpivot Data in Excel using Power Query (aka Get & Transform)”
------------------------------------------------------------------------------------

1.  Thank you but what if i want to remove one column in the base table?
    
    [Reply](https://trumpexcel.com/unpivot-data/#comment-13376)
    
2.  Great
    
    [Reply](https://trumpexcel.com/unpivot-data/#comment-12535)
    
3.  Awesome!
    
    [Reply](https://trumpexcel.com/unpivot-data/#comment-12279)
    
4.  Brilliant!
    
    [Reply](https://trumpexcel.com/unpivot-data/#comment-12001)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/unpivot-data/#respond)

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