# DROP Function in Excel

**Source:** https://trumpexcel.com/excel-functions/drop-function

---

[Skip to content](https://trumpexcel.com/excel-functions/drop-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/drop-function/#below-title)

DROP is a new [Excel function](https://trumpexcel.com/excel-functions/)
 that allows you to get all the records from a data set after you have dropped the specified number of rows or columns.

_DROP function is available in Excel for Microsoft 365, Excel for the web, and Excel for Microsoft 365 for Mac._ It was released along with the [TAKE function](https://trumpexcel.com/excel-functions/take-function/)
 (which is the opposite of the DROP function)

In this article, I will show you a couple of examples of how to use the DROP function in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/drop-function/#)

DROP Function Syntax in Excel
-----------------------------

Below is the syntax of the Excel DROP function:

\=DROP(array, rows,\[columns\])

Where:

*   _array_ – This is the array from which you want to drop rows and columns
*   _rows_ – This is a number that specifies the number of rows that you want to drop. If the number is positive, that many number of rows are dropped from the beginning of the data set, and if the number is negative, that many number of rows are dropped from the bottom of the data set.
*   _\[columns\]_ – This is a number that specifies the number of columns that you want to drop. If the number is positive, that many number of columns are dropped from the beginning of the data set, and if the number is negative, that many number of columns are dropped from the end of the data set.

Let’s now look at a couple of examples of using the DROP function in Excel.

Example 1 – Dropping Rows from the Beginning or End
---------------------------------------------------

Below, I have data in a Table with Name, Region, and Sales values, and I want to get all the records after dropping the first three records.

![Data set to use for the drop function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20365'%3E%3C/svg%3E)

Here is the formula to do this:

\=DROP(Data,3)

![DROP function to drop first three records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20415'%3E%3C/svg%3E)

Note that the table is named Data in this example.

And if you want to drop the last three records, you can use the below formula:

\=DROP(Data,-3)

![DROP function to drop last three records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20414'%3E%3C/svg%3E)

Since the result of the DROP formula is an array, make sure that the cells that are supposed to occupy the result of the drop function are empty. If they’re not empty, you will see a SPILL error.

Example 2 – Dropping Columns from Beginning or End
--------------------------------------------------

Just like rows, you can also drop columns from a dataset using the DROP function.

Below, I have data in a Table with Name, Region, and Sales values, and I want to get only the sales column from this data set.

![Data set to use for the drop function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20365'%3E%3C/svg%3E)

You can do this using the formula below:

\=DROP(Data,,2)

![DROP function to drop first two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20410'%3E%3C/svg%3E)

If you want to drop columns from the beginning, you can use a negative number as the column number argument.

For example, I can use the below formula only to get the names column from the data set:

\=DROP(Data,,-2)

![DROP function to drop last two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%20410'%3E%3C/svg%3E)

Example 3 – Dropping Rows and Columns both
------------------------------------------

You can also drop both rows and columns from a data set by specifying the row number as well as the column number in the formula.

Below, I have a data set from which I want to get only the names column, and even from that column, I want to drop the last five names.

![Data set to use for the drop function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20365'%3E%3C/svg%3E)

Here is the formula that will do this:

\=DROP(Data,-5,-2)

![DROP function to drop last two columns and last five rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20410'%3E%3C/svg%3E)

Example 4 – Using DROP with SORT
--------------------------------

DROP function becomes more useful when you start using it with other functions, such as SORT or FILTER.

Below, I have a data set with the names, regions, and sales values. I want to get only the names column, which should be sorted based on the sales values.

![Data set to use for the drop function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20365'%3E%3C/svg%3E)

You can do this using the below formula:

\=DROP(SORT(Data,3,-1),,-2)

![DROP with SORT Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20414'%3E%3C/svg%3E)

The above formula first uses the SORT(Data,3,-1) formula to sort our data set based on the sales value (which is in column 3 of the dataset). I have used -1 as the third argument here, as I wanted the data to be sorted in descending order.

The result of this SORT formula is then fed into the DROP function, Which drops the last two columns to give us only the names.

Example 5 – Using DROP with FILTER
----------------------------------

With the [FILTER function](https://trumpexcel.com/filter-function/)
, you can filter your larger data set to get the required array and then feed that into the DROP function to extract the relevant rows or columns.

Below, I have a data set with names, regions, and sales values columns. I want to extract all the records for the US region and then only get the top records after removing the bottom three records.

![Data set to use for the drop function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20365'%3E%3C/svg%3E)

Here is the formula to do that:

\=DROP(FILTER(Data,Data\[Region\]="US"),-3)

![DROP with FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20856%20418'%3E%3C/svg%3E)

The above formula first uses the FILTER function to extract all the records where the region is US. This result is then fed into the drop function, which gives us all the records after dropping the last three records.

You can further refine this formula to first filter the records, then sort them based on the sales values, and then use the DROP function to extract all the records after dropping the last three records.

Here is the formula to do that:

\=DROP(SORT(FILTER(Data,Data\[Region\]="US"),3,-1),-3)

![DROP with FILTER and SORT Functions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20811%20414'%3E%3C/svg%3E)

The above formula first filters the data to only get the records for US, then sorts this filtered data based on the sales values, and then DROP function is used over it to get all the records except the last three.

I hope all the examples I’ve covered here have helped you get a better understanding of how to best use the DROP function in Excel.

If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also find useful:**

*   [SWITCH Function in Excel](https://trumpexcel.com/excel-functions/switch-function/)
    
*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [INDEX & MATCH Functions Combo in Excel (Examples)](https://trumpexcel.com/index-match/)
    
*   [Excel HLOOKUP Function](https://trumpexcel.com/excel-hlookup-function/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [](https://trumpexcel.com/excel-functions/switch-function/)
    [Find the Closest Match in Excel (using Formulas)](https://trumpexcel.com/find-closest-match-in-excel/)
    
*   [Excel REDUCE Function](https://trumpexcel.com/excel-functions/reduce-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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