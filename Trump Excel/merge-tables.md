# Merge Tables in Excel Using Power Query (Step-by-Step Guide)

**Source:** https://trumpexcel.com/merge-tables

---

[Skip to content](https://trumpexcel.com/merge-tables/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/merge-tables/#below-title)

With Power Query, working with data dispersed across worksheets or even workbooks has become easier.

One of the things where [Power Query](https://trumpexcel.com/power-query-course/)
 can save you a lot of time is when you have to merge tables with different sizes and columns based on a matching column.

Below is a video where I show exactly how to merge tables in Excel using Power Query.

In case you prefer reading the text over watching a video, below are the written instructions.

Suppose you have a table as shown below:

![Merge Tables in Excel using Power Query - Table 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20465'%3E%3C/svg%3E)

This table has the data I want to use, but it’s still missing two important columns – the ‘Product Id’ and the ‘Region’ where the sales rep operates.

This information is provided as separate tables as shown below:

![Merge Tables using Power Query - Table 2 & 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20252'%3E%3C/svg%3E)

To get all this information into a single table, you will have to merge these three tables so that you can then [create a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
 and analyze it, or use it for other [reporting/dashboarding purposes](https://trumpexcel.com/creating-excel-dashboard/)
.

And by merging, I don’t mean a simple copy paste.

You’ll have to map the relevant records from Table 1 with data from Table 2 and 3.

Now you can rely on [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 or INDEX/MATCH to do this.

Or if you’re a [VBA whiz](https://trumpexcel.com/excel-vba/)
, you can write a code to do this.

But these options are time-consuming and complicated as compared with Power Query.

In this tutorial, I will show you how to merge these three Excel tables into one.

For this technique to work, you need to have connecting columns. For example, in Table 1 and Table 2, the common column is ‘Item’, and in Table 1 and Table 3, the common column is ‘Sales Rep’. Also, note that there should be no repetition in these connecting columns.

Note: Power Query can be used as an add-in in Excel 2010 and 2013, and is an inbuilt feature from Excel 2016 onwards. Based on your version, some images may look different (image captures used in this tutorial are from Excel 2016).

Merge Tables Using Power Query
------------------------------

I have named these tables as shown below:

1.  Tabel 1 – **Sales\_Data**
2.  Table 2 – **Pdt\_Id**
3.  Table 3 – **Region**

It isn’t mandatory to rename these tables, but it’s better to give names that describe what the table is about.

At one go, you can merge only two tables in Power Query.

So we will first have to merge Table 1 and Table 2 and then merge Table 3 into it in the next step.

### Merging Table 1 and Table 2

To merge tables, you first need to convert these tables into connections in Power Query. Once you have the connections, you can easily merge these.

Here are the steps to save an Excel table as a connection in Power Query:

1.  Select any cell in Sales\_Data table.
2.  Click the Data tab.![Merge Tables using Power Query - Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20193'%3E%3C/svg%3E)
3.  In the Get & Transform group, click on ‘From Table/Range’. This will open the Query editor.![Merge Tables using Power Query - from table range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20193'%3E%3C/svg%3E)
4.  In the Query editor, click the ‘File’ tab.![Merge Tables using Power Query - File tab in qury editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20172'%3E%3C/svg%3E)
5.  Click on ‘Close and Load To’ option.![Merge Tables using Power Query - Close and Load to](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20215%20266'%3E%3C/svg%3E)
6.  In the ‘Import Data’ dialog box, select ‘Only Create Connection’.![Merge Tables using Power Query - only create connection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20351'%3E%3C/svg%3E)
7.  Click OK.

The above steps would create a connection with the name Sales\_Data (or any name that you have given to the Excel Table).

**Repeat the above steps for Table 2 and Table 3.**

So when you’re done, you will have three connections (with the name Sales\_Data, Pdt\_Id, and Region).

![Merge table columns in Excel using Power Query - three queries](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20343'%3E%3C/svg%3E)

Now let’s see how to merge the Sales\_Data and Pdt\_Id table.

1.  Click on the Data tab.![Merge Tables using Power Query - Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20193'%3E%3C/svg%3E)
2.  In the Get & Transform Data group, click on Get Data. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20193'%3E%3C/svg%3E)
3.  In the drop-down, click on Combine Queries.
4.  Click on Merge. This will open the Merge dialog box.![Merge Tables using Power Query - Combine queries merge queries options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20471%20522'%3E%3C/svg%3E)
5.  In the Merge dialog box, select ‘Sales\_Data’ from the first drop down.![Select Sales Data in the Merge Dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20669'%3E%3C/svg%3E)
6.  Select ‘Pdt\_Id’ from the second drop down.![Select Product Id in Merge dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20669'%3E%3C/svg%3E)
7.  In ‘Sales\_Data’ preview, click on the ‘Item’ column. Doing this will [select the entire column](https://trumpexcel.com/select-entire-column-excel/)
    .
8.  In ‘Pdt\_Id’ preview, click on the ‘Item’ column. Doing this will select the entire column.![Select Columns that are common - merge tables in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20669'%3E%3C/svg%3E)
9.  In the ‘Join Kind’ drop-down, select ‘Left Outer (all from first, matching from second)’.![Merge Tables in Excel using Power Query Join drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20669'%3E%3C/svg%3E)
10.  Click OK.

The above steps would open the Query editor and show you the data from the Sales\_Data with one additional column (of Pdt\_Id).

![Merge Tables using Power Query - Extra column when combining data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20803%20247'%3E%3C/svg%3E)

### Merging the Excel Tables (Table 1 & 2)

Now the process of merging the tables will happen within the Query editor with the following steps:

1.  In the additional column (Pdt\_Id), click on the double pointed arrow in the header.![Click on double pointed arrow in Product Id column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20238'%3E%3C/svg%3E)
2.  From the options box that opens, uncheck all the column names and only select Item. This is because we already have the product name column in the existing table, and we only want the product ID for each product.
3.  Uncheck the option ‘Use original column name as prefix’.
4.  Click Ok.

This would give you the resulting table that has every record from Sales\_Data table and an additional column that has product ids as well (from the Pdt\_Id table).

![Merge tables with the extra column in sales data result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20803%20221'%3E%3C/svg%3E)

Now if you only want to combine two tables, you can load this Excel you’re done.

But we have three tables to merge, so there is more work to be done.

You need to save this resulting table as a connection (so that we can use it to merge it with Table 3).

Here are the steps to save this merged table (with data from Sales\_Data and Pdt\_Id table) as a connection:

1.  Click the File tab
2.  Click on ‘Close and Load to’ option.
3.  In the ‘Import Data’ dialog box, select ‘Only Create Connection’.
4.  Click OK.

This will save the newly merged data as a connection. You can rename this connection if you want.

![Merge1 table in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20390'%3E%3C/svg%3E)

### Merging Table 3 with the Resulting Table

The process of merging the third table with the resultant table (that we got by merging Table 1 and Table 2) is exactly the same.

Here are the steps to merge these tables:

1.  Click on the Data tab.
2.  In the Get & Transform Data group, click on ‘Get Data’.
3.  In the drop-down, click on ‘Combine Queries.
4.  Click on ‘Merge’. This will open the Merge dialog box.
5.  In the Merge dialog box, Select ‘Merge1’ from the first drop down.
6.  Select ‘Region’ from the second drop down.
7.  In ‘Merge1’ preview, click on the ‘Sales Rep’ column. Doing this will select the entire column.
8.  In Region preview, click on the ‘Sales Rep’ column. Doing this will select the entire column.
9.  In the ‘Join Kind’ drop-down, select Left Outer (all from first, matching from second).
10.  Click OK.

The above steps would open the Query editor and show you the data from Merge1 with one additional column (Region).

Now the process of merging the tables will happen within the Query editor with the following steps:

1.  In the additional column (Region), click on the double pointed arrow in the header.
2.  From the options box that opens, uncheck all the column names and only select Region.
3.  Uncheck the option ‘Use original column name as prefix’.
4.  Click Ok.

The above steps would give you a table that has all the three tables merged (Sales\_Data table with one column for Pdt\_Id and one for Region).

Here are the steps to load this table in Excel:

1.  Click the File tab.
2.  Click on ‘Close and Load to’.
3.  In the ‘Import Data’ dialog box, select Table and New Worksheets options.
4.  Click OK.

This would give you the resulting merged table in a new worksheet.

One of the best things about Power Query is that you can easily accommodate any changes in the underlying data (Table 1, 2 and 3) by simply refreshing it.

For example, suppose Laura gets transferred to Asia and you get new data for the next month. Now you don’t have to repeat the above steps again. All you need to do is refresh the table and it will do everything it all over again for you.

Within seconds you’ll have the new merged table.

**You May Also Like the Following Power Query Tutorials:**

*   [Combine Data from Multiple Workbooks in Excel (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    .
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel.](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [How To Copy Excel Table Into Word](https://trumpexcel.com/copy-excel-table-to-word/)
    
*   [How to Unpivot Data in Excel using Power Query (aka Get & Transform)](https://trumpexcel.com/unpivot-data/)
    
*   [Get a List of File Names from Folders & Sub-folders (using Power Query)](https://trumpexcel.com/list-file-names-power-query/)
    
*   [Combine CSV Files With Inconsistent Column Headers](https://trumpexcel.com/power-query/combine-csv-inconsistent-headers/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “Merge Tables in Excel Using Power Query”
--------------------------------------------------------

1.  This has been super helpful. Thanks bunches
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-33456)
    
2.  Nice, detailed instructions, but I need to merge data from three tables into one, not create a table with matched entries. i.e. three tables with identical column headers which I need to merge into one table dynamically without having to cut/paste the three into one every time I modify one. Is there a way to do that?
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-31268)
    
    *   There is a way to do that. Instead of Merge, you should use Append (step 4).
        
        [Reply](https://trumpexcel.com/merge-tables/#comment-33336)
        
3.  This functionality does not exist in Excel 2013. MISLEADING
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-14895)
    
4.  Very useful and neat!  
    شكرا جزيلا
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-13856)
    
5.  This was very helpful!! Thank you!!
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-13615)
    
6.  Hi! I am trying to merge tables from a web source that the number of tables varies from day to day. When i import the data connection and use the append in power query, i get the following:
    
    \= Table.Combine({#”Table 0″, #”Table 1″, #”Table 10″, #”Table 11″, #”Table 12″, #”Table 13″, #”Table 2″, #”Table 3″, #”Table 4″, #”Table 5″, #”Table 6″, #”Table 7″, #”Table 8″, #”Table 9″})
    
    is there a way to make this dynamic so that it looks for \*any\* table instead of this static list of tables? Sometimes i have 4 tables, sometimes i have 20… the file name it is reading from is the same but the table count is variable depending on the data… how can i do this?
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-13459)
    
7.  Thank you for this video, but I can’t get the merge to work, because after creating the connection, in Merge dialog, there is NO Join Kind dropdown. Any suggestions why that might be? Thank you.
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-13398)
    
8.  Muchas gracias, no tenía ni idea que Excel tuviera esta herramienta.
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-13045)
    
9.  This is exactly what I needed. Thank you so much!!
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-12882)
    
10.  amazing ! thank you very much for your valuable contents and learning
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-12755)
    
11.  Wonderful tutorial! Please can you give the link to the data you used for both write-ups and youtube?
    
    [Reply](https://trumpexcel.com/merge-tables/#comment-10194)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/merge-tables/#respond)

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