# TAKE Function in Excel - Useful Examples!

**Source:** https://trumpexcel.com/excel-functions/take-function

---

[Skip to content](https://trumpexcel.com/excel-functions/take-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/take-function/#below-title)

TAKE Is a new Excel function that allows you to extract records from the top or bottom of an array.

_TAKE function is available in Excel for Microsoft 365, Excel for the web, and Excel for Microsoft 365 for Mac._ _It was released along with the [DROP function](https://trumpexcel.com/excel-functions/drop-function/)
 (which is the opposite of the TAKE function)_

While it’s useful when you want to extract records from the top or bottom of an array, its real usefulness comes in when you use it with other functions such as FILTER and SORT.

In this article, I will first explain to you how the take function works and then show you some useful examples that can really help you in your day-to-day work.

**_[Click here to download the example file and follow along](https://www.dropbox.com/scl/fi/f9gn45wqxbrf9o85tbsxy/Take-Function-in-Excel.xlsx?rlkey=xa3bynh9277isowgt4thvimkq&dl=1)
_**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/take-function/#)

TAKE Function Syntax in Excel
-----------------------------

Below is the syntax of the Excel TAKE function:

\=TAKE(array, rows,\[columns\])

Where:

*   **array** – This is the array from which you want to extract/take the rows or columns from the beginning or the end
*   **rows** – This argument tells the TAKE function to extract the specified number of rows from the beginning (if the number is positive) and from the end (if the number is negative)
*   **\[columns\]** – This argument tells the TAKE function to extract the specified number of columns from the beginning (if the number is positive) and from the end (if the number is negative)

Now let me show you a couple of examples where you can use take function in your day-to-day work.

Also read: [Excel XLOOKUP Function (10 Examples)](https://trumpexcel.com/xlookup-function/)

Example 1 – Extract Records from the Top or Bottom
--------------------------------------------------

Let’s start with a simple example where I want the take function to give me rows from an array.

Below is a table (named Data) from which I want to extract the top 3 rows.

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Here is the formula to get the top three rows from this table.

\=TAKE(Data,3)

When I use this formula in a cell and hit Enter, it will return the top three records, as shown below.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20820%20513'%3E%3C/svg%3E)

Note that the result is an array that will spill and occupy the cells based on the resulting array’s size. If any of those cells that are supposed to be occupied by the result of the take function are already filled out, you will get the SPILL error.

If I want to get the results from the bottom, I can use the below formula that would give me the last three records from the table:

\=TAKE(Data,-3)

![TAKE function to get bottom three rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20825%20482'%3E%3C/svg%3E)

_In a nutshell, when I use a positive number, it starts from the top of the array and gives me the specified number of records, and when I use a negative number, it starts from the bottom of the array and gives me the specified number of records_.

One limitation you need to know about the take function is that it would always return a contiguous range of rows or columns. This means that you cannot use this function alone to extract row number 1 and row number 3 from the top.

Example 2 – Extract Columns from the Beginning or End
-----------------------------------------------------

Just like rows, you can also use the Take function to extract the columns from the beginning or from the end of the array.

Below is a table from which I want to extract the first two columns:

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Here is the formula to do this:

\=TAKE(Data,,2)

This will give me all the values in the Name and the Region column, as shown below:

![TAKE function to get first two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20694%20438'%3E%3C/svg%3E)

Note that in the above formula, I have left the row argument empty, so it returns all the rows and then gives me the specified number of columns.

Example 3 – Extract a Sub-segment of an Array
---------------------------------------------

You can also use both row and column number arguments to extract a subsegment of an array.

For example, below, I have a table, and I want to extract the 1st 3 names in the table.

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Below is the formula that will do this:

\=TAKE(Data,3,1)

The above formula extracts the first three rows from the table and then only returns the values from the first column.

![TAKE function to extract Sub-segment of Array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20694%20433'%3E%3C/svg%3E)

Example 4 – Extract Non-Contiguous Columns
------------------------------------------

While the TAKE function itself cannot return non-contiguous rows or columns, this can be done by using a combination of TAKE function with CHOOSECOLS or CHOOSEROWS.

_CHOOSECOLS or CHOOSEROWS are new [Excel functions](https://trumpexcel.com/excel-functions/)
 that are available in Excel for Microsoft 365, Excel for the web, and Excel for Microsoft 365 for Mac_

Below, I have a table from which I want to get the first three records, but I only want the names and their sales values. So I need to somehow extract column number 1 and 3 while leaving out column number 2.

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Here is the formula that would do that:

\=TAKE(CHOOSECOLS(Data,1,3),3)

![TAKE Function to Extract Non-Contiguous Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20860%20439'%3E%3C/svg%3E)

In the above formula, I have used CHOOSECOLS to first extract only columns 1 and 3.

This result is then fed into the TAKE function to extract the top three records from it.

Example 5 – Using TAKE with SORT Function
-----------------------------------------

So far, I’ve just shown you how to extract records using the TAKE function.

But you can do a lot more meaningful work when you combine it with functions such as SORT and FILTER.

Let’s take the below example table, from which I want to get the top three records of people who have made the most sales.

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Since my table is not already sorted, I can first use the SORT function to get a sorted data set and then use the take function to extract the top three rows.

Below is the formula that would give me the records for the top three salesmen by sales value:

\=TAKE(SORT(Data,3,-1),3)

![TAKE function with SORT function1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20820%20486'%3E%3C/svg%3E)

The above formula uses the SORT function to first give me an array that is sorted based on the sales value (which is column 3) in descending order. These areas are then fed into the take function, which gives me the top three rows.

If you want to get the bottom three people based on their sales values, you can use the below formula:

\=TAKE(SORT(Data,3,-1),-3)

![TAKE function with SORT function bottom three](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20825%20488'%3E%3C/svg%3E)

If you want to get the records of the top three salespeople but only get their name and their sales values, you can use the formula below:

\=TAKE(CHOOSECOLS(SORT(A2:C12,3,-1),1,3),3)

![TAKE function with SORT function bottom three two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201020%20484'%3E%3C/svg%3E)

Example 6 – Using TAKE with FILTER Function
-------------------------------------------

Now, let’s see another helpful example where you can use a combination of the TAKE and [FILTER functions](https://trumpexcel.com/filter-function/)
.

Below I have a table that shows the sales values for different people along with their region name and I want to get the top three sales people in the US based on their sales.

![Dataset for TAKE function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20452'%3E%3C/svg%3E)

Since my data set is not sorted, the first thing I need to do is sort this data set, then extract only the records for US, and then use the TAKE function to give me the top three records.

Here is the formula that will do this:

\=TAKE(FILTER(SORT(Data,3,-1),CHOOSECOLS(SORT(Data,3,-1),2)="US"),3)

![Using TAKE function with FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20974%20582'%3E%3C/svg%3E)

The above function first sorts the table based on the sales values (which are in column 3) in descending order. This result is then fed into the FILTER function that uses SORT(Data,3,-1) as the array and CHOOSECOLS(SORT(Data,3,-1),2)=”US” as the criteria.

The CHOOSECOLS(SORT(Data,3,-1),2)=”US” Part of the formula uses the choose calls function to only pick up the second column that contains the region values in the sorted data set and then checks whether the value is US or not. This returns an area of cruise and falls that works as the criteria value for the FILTER function.

The _FILTER(SORT(Data,3,-1),CHOOSECOLS(SORT(Data,3,-1),2)=”US”)_ part of the formula gives us all the records for the US in the table, which are also sorted in descending order.

Now, we use the TAKE function on this result to get the top three records for the US.

If I want to get the top three salespeople for Europe, I can replace ‘US’ with ‘Europe’, and my formula would become:

\=TAKE(FILTER(SORT(Data,3,-1),CHOOSECOLS(SORT(Data,3,-1),2)="Europe"),3)

![Using TAKE function with FILTER function Different Region](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201017%20587'%3E%3C/svg%3E)

You can also make this better by having the region value in a cell and using that cell reference in the formula. For example, if I have the region value in cell E1, I can use the below formula:

\=TAKE(FILTER(SORT(Data,3,-1),CHOOSECOLS(SORT(Data,3,-1),2)=E1),3)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20944%20584'%3E%3C/svg%3E)

Similarly, if you want to get the bottom three performing salespeople for a specific region, you can use the below formula:

\=TAKE(FILTER(SORT(Data,3,-1),CHOOSECOLS(SORT(Data,3,-1),2)="US"),-3)

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/f9gn45wqxbrf9o85tbsxy/Take-Function-in-Excel.xlsx?rlkey=xa3bynh9277isowgt4thvimkq&dl=1)
_**

In this article, I showed you how to use the TAKE function in Excel using some practical examples. While the TAKE function is useful on its own, too, its actual utility in using it with other functions such as SORT and FILTER.

I hope you found this article helpful. If you have any questions or suggestions for me, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [VLOOKUP Vs. INDEX/MATCH – Which One is Better? (Answered)](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [INDEX & MATCH Functions Combo in Excel (10 Easy Examples)](https://trumpexcel.com/index-match/)
    
*   [Excel HLOOKUP Function](https://trumpexcel.com/excel-hlookup-function/)
    
*   [Find the Closest Match in Excel (using Formulas)](https://trumpexcel.com/find-closest-match-in-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [SWITCH Function in Excel](https://trumpexcel.com/excel-functions/switch-function/)
    

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