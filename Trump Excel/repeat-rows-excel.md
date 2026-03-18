# Repeat Rows N Times in Excel

**Source:** https://trumpexcel.com/repeat-rows-excel

---

[Skip to content](https://trumpexcel.com/repeat-rows-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/repeat-rows-excel/#below-title)

If you want to repeat rows in your dataset N number of times (say 5 or 7 times), or based on a value in a column, Power Query is the easiest way to do that.

In this article, I’ll walk you through two methods to repeating all rows the same number of times, and repeating rows based on different values that are given in a column.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/repeat-rows-excel/#)

1\. Repeat All Cells / Rows _N_ Times
-------------------------------------

Below I have a dataset of all-time top grossing movies as of writing this article. And I want to repeat each row in this data five times.

![Dataset to repeat each row n times](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20372'%3E%3C/svg%3E)

Note: While I’m going to show you how to repeat rows in a data set, you can use the same process to also repeat cells in a column

Here are the steps to do this using [Power Query](https://trumpexcel.com/power-query-course/)
.

### Step 1: Convert Your Data to an Excel Table

If your data is already in an [Excel table](https://trumpexcel.com/excel-table/)
, you can leave this step. But if it’s not, you can use the below steps to first convert you data into an Excel Table.

1.  Select any cell within your data
2.  Hold the Ctrl key and press the T key
3.  In the Create Table dialog box that opens, verify that range is correct (it usually is)
4.  Ensure “My table has headers” is checked (if your data includes headers)

![Create Table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20162'%3E%3C/svg%3E)

5.  Click OK

Now your data has been converted into an Excel Table.

_Optional_: For the sake of simplicity and clarity, it best to rename your Excel Table and give it a descriptive name. In this case, I will name it _RepeatRows_

### Step 2: Open Power Query

Now let’s open this table in Power Query Editor.

1.  Select any cell in the Excel Table.
2.  Go to the Data tab in the Excel ribbon and click on the “From Table/Range” icon

![Click on the From Table Range icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20223'%3E%3C/svg%3E)

This will open your data in the Power Query Editor.

![Data opens in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20826%20533'%3E%3C/svg%3E)

_Note that the name of the query will be the same as the name of your table._

### Step 3: Create a List Using a Custom Column

Now we will insert a new column that will be used in the next step to make the rows repeat.

To do this:

1.  In the Power Query Editor, click the “Add Column” tab

![Click on the Add Column tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20170'%3E%3C/svg%3E)

2.  Click on “Custom Column” option

![Click on Custom Column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20169'%3E%3C/svg%3E)

3.  In the “New column name” field, enter any name you prefer. I will leave it as _Custom_
4.  In the formula field, type: **{1..5}** (This creates a list of numbers from 1 to 5 and every cell in the newly added column will get this list)

![Enter the list formula in custom column dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20876%20549'%3E%3C/svg%3E)

5.  Click OK

Once done, you will see that the new column displays a “List” value in each cell (as shown below).

![Custom column with list in each cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20353'%3E%3C/svg%3E)

This might look strange if you’re new to Power Query! What’s happening is that Power Query has created a small container (called a list) for each row, and inside each container are five numbers: 1, 2, 3, 4, and 5.

If you click on any “List” value in this new column, you’ll see these numbers appear in the preview window at the bottom of your screen.

![Custom column with list in each cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20353'%3E%3C/svg%3E)

This is different from regular Excel where a cell typically holds just one value. In Power Query, a cell can hold multiple values in a list, which is exactly what we need to repeat our rows in the next step.

### Step 4: Expand the List to Rows

Now that we have the list in each cell in the newly added column, let expand it so it gives the repeated rows.

1.  Click the expand icon (two diagonal arrows) on your new custom column
2.  Select “Expand to New Rows”

![Expand to new rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20356'%3E%3C/svg%3E)

And Voila!

You can see we are very close to what we wanted. Every row in the dataset has been repeated five times.

![each row repeated n times](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20650'%3E%3C/svg%3E)

### Step 5: Remove the Custom Column

Now let’s remove the column we inserted:

1.  Right-click on the custom column header
2.  Select “Remove”

![Remove the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20815%20668'%3E%3C/svg%3E)

As this point, we have the data we want, but it’s in Power Query editor. So we need to get this data into Excel now.

### Step 6: Load the Data to Excel

1.  Go to File tab
2.  Click on Close & Load

![Click on Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20416'%3E%3C/svg%3E)

This will insert a new sheet into your Excel workbook and the resulting data from Step 5 will be inserted as an Excel Table.

_**Power Query Magic**_: The real Power Query Magic happens when there are changes and you want to redo this result. Insetad of repeating all these steps again, just right click on any cell in the resulting table and click on Refresh. Since we have already created the query, all the steps would repeat in the backend and your results would be refreshed (almost instantly)

Also read: [Create All Possible Combinations from Lists in Excel](https://trumpexcel.com/create-all-combinations-from-lists-excel/)

2\. Repeat All Cells / Rows Based on Different Values
-----------------------------------------------------

What if you don’t want to repeat each row the same number of times? Maybe you want the first row to repeat 2 times, the second row 5 times, the third row 4 times, and so on?

Below I have a dataset where I have a column named ‘Rept’ that specifies how many times I want each row to be repeated.

![Data to repeat rows based on cell value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20372'%3E%3C/svg%3E)

Here are the steps to do this using Power Query.

### Step 1: Convert Your Data to an Excel Table

If your data is already in an Excel table, you can skip this step. But if it’s not, you can use the below steps to first convert your data into an Excel Table.

1.  Select any cell within your data
2.  Hold the Ctrl key and press the T key
3.  In the Create Table dialog box that opens, verify that range is correct (it usually is)
4.  Ensure “My table has headers” is checked (if your data includes headers)

![Make sure the range is right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20162'%3E%3C/svg%3E)

5.  Click OK

Now your data has been converted into an Excel Table.

**Optional**: For the sake of simplicity and clarity, it’s best to rename your Excel Table and give it a descriptive name. In this case, I will name it _RepeatRowsCustom_

### Step 2: Open Power Query

Now let’s open this table in Power Query Editor.

1.  Select any cell in the Excel Table
2.  Go to the Data tab in the Excel ribbon and click on the “From Table/Range” icon

![Click on the From Table Range icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20223'%3E%3C/svg%3E)

This will open your data in the Power Query Editor.

_Note that the name of the query will be the same as the name of your table._

### Step 3: Create a Dynamic List Using a Custom Column

Now we will add a new column that will be used in the next step to repeat each row the specified number of times.

To do this:

1.  In the Power Query Editor, click the “Add Column” tab
2.  Click on “Custom Column” option

![Click on Custom column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20170'%3E%3C/svg%3E)

3.  In the “New column name” field, enter any name you prefer. I will leave it as _Custom_
4.  In the formula field, type: **{1..\[Rept\]}** (where “\[Rept\]” is the name of your column that contains the repeat count)

_Tip: You can either type this manually or simply double-click on the column name in the “Available columns” list to insert it._

![Enter the formula with column name in Custom Column dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20876%20549'%3E%3C/svg%3E)

5.  Click OK

Once done, you will see that the new column displays a “List” value in each cell (as shown below).

![Custom column with list with custom number is added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20875%20352'%3E%3C/svg%3E)

If you click on the first row’s list, you will see it contains \[1, 2\] because the Rept column value for that row was 2.

![List with values in first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20870%20527'%3E%3C/svg%3E)

The second row will show \[1, 2, 3, 4, 5\] because its Rept column value for that row was 5, and so on.

![List with values in second cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20873%20595'%3E%3C/svg%3E)

What’s happening is that Power Query is creating a custom-sized list for each row based on the values in your Rept column. Pretty neat, right?

### Step 4: Expand the List to Rows

Now let’s expand these dynamic lists:

1.  Click the expand icon (two diagonal arrows) on your new custom column
2.  Select “Expand to New Rows”

![Select the Expand to new rows option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20874%20351'%3E%3C/svg%3E)

And just like that, the magic happens! Each row has been repeated exactly the number of times specified in the Rept column.

![Rows repeated based on the REPT column values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20867%20630'%3E%3C/svg%3E)

Pretty Neat… isn’t it!

### Step 5: Remove Unnecessary Columns

Now let’s clean up our data:

1.  Right-click on the custom column header and select “Remove”
2.  If you also want to remove the original Rept column (the one that specified the repeat count), right-click on it and select “Remove”

![Click on remove columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20990%20613'%3E%3C/svg%3E)

Now we have the result that we wanted. The only step left now is to get this data in Excel.

### Step 6: Load the Data to Excel

Follow the steps below to get the data in Excel as a Table:

1.  Go to the File tab
2.  Click on Close & Load

![Click on close and load option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20398'%3E%3C/svg%3E)

This will insert a new sheet into your Excel workbook, and the resulting data will be inserted as an Excel Table.

And just like the previous method, if you make any changes in the original table, you can get the updated result by simply refreshing the query result. To do that, right-click on any cell in the result table and click on Refresh

So this is how you can use Power Query to repeat rows in Excel N times or based on a value in a column.

Repeat Rows Using a Formula
---------------------------

If you want to repeat rows in Excel using a formula, you can use the method covered in the video below:

I hope you found this article helpful.

**Other Excel articles you may also like:**

*   [How to Print the Top Row on Every Page in Excel (Repeat Row/Column Headers)](https://trumpexcel.com/print-top-row-on-every-page-excel/)
    
*   [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)
    
*   [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)
    
*   [How to Move Rows and Columns in Excel](https://trumpexcel.com/move-rows-columns/)
    
*   [Repeat Lists Using SEQUENCE Function](https://trumpexcel.com/excel-functions/sequence/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/repeat-rows-excel/#respond)

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