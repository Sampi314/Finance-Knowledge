# Excel Filter Function - Explained with Examples + Video

**Source:** https://trumpexcel.com/filter-function

---

[Skip to content](https://trumpexcel.com/filter-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/filter-function/#below-title)

**Watch Video – Excel FILTER Function Examples**

Office 365 brings with some awesome functions – such as [XLOOKUP](https://trumpexcel.com/xlookup-function/)
, SORT, and FILTER.

When it comes to filtering data in Excel, in the pre-Office 365 world, we were mostly dependent on Excel in-built filter or at max the [Advanced filter](https://trumpexcel.com/excel-advanced-filter/)
 or complex [SUMPRODUCT](https://trumpexcel.com/excel-sumproduct-function/)
 formulas. In case you had to filter a part of a dataset, it was usually a complex workaround (something I have covered here).

But with the new FILTER function, it’s now really easy to quickly filter part of the dataset based on a condition.

And in this tutorial, I will show you how awesome is the new FILTER function and some useful things you can do with this.

But before I get into the examples, let’s quickly learn about the syntax of the FILTER function.

In case you want to get these new features in Excel, you can **[upgrade to Office 365](https://www.youtube.com/redirect?v=hjfGyo6fe18&redir_token=KYeFA5iBZZ2nqdoeXIp0mCL15l18MTU4MTU1NjYwNEAxNTgxNDcwMjA0&event=video_description&q=https%3A%2F%2Fmicrosoft.msafflnk.net%2FVk9OR)
** (join the insider program to get access to all features/formulas)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/filter-function/#)

Excel Filter Function – Syntax
------------------------------

Below is the syntax of the FILTER function:

\=FILTER(array,include,\[if\_empty\])

*   **array** – this is the range of cells where you have the data and you want to filter some data from it
*   **include** – this is the condition that tells the function what records to filter
*   **\[if\_empty\]** – this is an optional argument where you can specify what to return in case no results are found by the FILTER function. By default (when not specified), it returns the #CALC! error

Now let’s have a look at some amazing Filter function examples and stuff it can do which used to be quite complex in its absence.

**[Click here to download the Example file and follow along](https://www.dropbox.com/s/v2r8zqcfmpwbvn9/Filter%20Function%20Examples.xlsx?dl=1)
**

Example 1: Filtering Data Based on One Criteria (Region)
--------------------------------------------------------

Suppose you have a dataset as shown below and you want to filter all the records for the US only.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

Below is the FILTER formula that will do this:

\=FILTER($A$2:$C$11,$B$2:$B$11="US")

![Filter data based on the region](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20343'%3E%3C/svg%3E)

The above formula uses the dataset as the array and the condition is $B$2:$B$11=”US”

This condition would make the FILTER function check every cell in column B (one that has the region) and only those records that match this criterion would be filtered.

Also, in this example, I have the original data and the filtered data on the same sheet, but you can also have these in separate sheets or even workbooks.

Filter Function returns a result that is a dynamic array (which means that instead of returning one value, it returns an array that spills to other cells).

For this to work, you need to have an area where the result would come to be empty. In any of the cells in this area (E2:G5 in this example) already has something in it, the function will give you the #SPILL error.

Also, since this is a dynamic array, you can not change a part of the result. You can either delete the entire range that has the result or cell E2 (where the formula was entered). Both of these would delete the entire resulting array. But you can not change any individual cell (or delete it).

In the above formula, I have hard-coded the region value, but you can also have it in a cell and then reference that cell that has the region value.

For example, in the below example, I have the region value in cell I2 and this is then referenced in the formula:

\=FILTER($A$2:$C$11,$B$2:$B$11=I1)

This makes the formula even more useful, and now you can simply change the region value in cell I2, and the filter would automatically change.

You can also have a [drop-down](https://trumpexcel.com/excel-drop-down-list/)
 in cell I2 where you can simply make the selection and it would instantly update the filtered data.

Also read: [Excel LAMBDA Function](https://trumpexcel.com/excel-functions/lambda/)

Example 2: Filtering Data Based on One Criteria (More Than or Less Than)
------------------------------------------------------------------------

You can also use comparative operators within the filter function and extract all the records that are more or less than a specific value.

For example, suppose you have the dataset as shown below and you want to filter all the records where the sales value is more than 10000.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

The below formula can do this:

\=FILTER($A$2:$C$11,($C$2:$C$11>10000))

![Filter data based on the sales value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20344'%3E%3C/svg%3E)

The array argument refers to the entire dataset and the condition, in this case, is ($C$2:$C$11>10000).

The formula checks each record for the value in Column C. If the value is more than 10000, it is filtered, else it’s ignored.

In case you want to get all the records less than 10000, you can use the below formula:

\=FILTER($A$2:$C$11,($C$2:$C$11<10000))

You can also get more creative with the FILTER formula. For example, if you want to filter the top three record based on the sales value, you can use the below formula:

\=FILTER($A$2:$C$11,($C$2:$C$11>=LARGE(C2:C11,3)))

![Filter Top 3 results based on the sale value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20726%20346'%3E%3C/svg%3E)

The above formula uses the LARGE function to get the third largest value in the dataset. This value is then used in the FILTER function criteria to get all the records where the sales value is more than or equal to the third-largest value.

**[Click here to download the Example file and follow along](https://www.dropbox.com/s/v2r8zqcfmpwbvn9/Filter%20Function%20Examples.xlsx?dl=1)
**

Example 3: Filtering Data with Multiple Criteria (AND)
------------------------------------------------------

Suppose you have the below dataset and you want to filter all the records for the US where sale value is more than 10000.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

This is an AND condition where you need to check for two things – the region needs to the US and the sales need to be more than 10000. If only one condition is met, the results should not be filtered.

Below is the FILTER formula that will filter records with the US as the region and sales of more than 10000:

\=FILTER($A$2:$C$11,($B$2:$B$11="US")\*($C$2:$C$11>10000))

![Filter based on region and the sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20343'%3E%3C/svg%3E)

Note that the criterion (called the include argument) is ($B$2:$B$11=”US”)\*($C$2:$C$11>10000)

Since I am using two conditions and I need both to be true, I have used the multiplication operator to combine these two criteria. This returns an array of 0’s and 1’s, where a 1 is returned only when both the conditions are met.

In case there are no records that meet the criteria, the function would return the #CALC! error.

And in case you want to return something meaning (instead of the error), you can use a formula as shown below:

\=FILTER($A$2:$C$11,($B$2:$B$11="USA")\*($C$2:$C$11>10000),"Nothing Found")

Here, I have used “Not Found” as the third argument, which is used when no records are found that match the criteria.

Also read: [TAKE Function in Excel](https://trumpexcel.com/excel-functions/take-function/)

Example 4: Filtering Data with Multiple Criteria (OR)
-----------------------------------------------------

You can also modify the ‘include’ argument in the FILTER function to check for an OR criteria (where any one of the given conditions can be true).

For example, suppose you have the dataset as shown below and you want to filter the records where the country is either the US or Canada.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

Below is the formula that will do this:

\=FILTER($A$2:$C$11,($B$2:$B$11="US")+($B$2:$B$11="Canada"))

![Filter based on region OR condition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20334'%3E%3C/svg%3E)

Note that in the above formula, I have simply added the two conditions by using the addition operator. Since each of these conditions returns an array of TRUEs and FALSEs, I can add to get a combined array where it’s TRUE if any one of the conditions is met.

Another example could be when you want to filter all the records where either the country is the US or the sale value is more than 10000.

The below formula will do this:

\=FILTER($A$2:$C$11,($B$2:$B$11="US")+(C2:C11>10000))

Note: When using AND criteria in a FILTER function, use the multiplication operator (\*) and when using the OR criteria, use the addition operator (+).

Example 5: Filtering Data To Get Above/Below Average Records
------------------------------------------------------------

You can use formulas within the FILTER function to filter and extract records where the value is above or below the average.

For example, suppose you have the dataset as shown below and you want to filter all the records where the sale value is above average.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

You can do that using the following formula:

\=FILTER($A$2:$C$11,C2:C11>AVERAGE(C2:C11))

![Filter records above average](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20678%20343'%3E%3C/svg%3E)

Similarly, for below average, you can use the below formula:

\=FILTER($A$2:$C$11,C2:C11<AVERAGE(C2:C11))

**[Click here to download the Example file and follow along](https://www.dropbox.com/s/v2r8zqcfmpwbvn9/Filter%20Function%20Examples.xlsx?dl=1)
**

Example 6: Filtering Only the EVEN Number Records (Or ODD Number Records)
-------------------------------------------------------------------------

In case you need to quickly filter and extract all the records from even number rows or odd number rows, you can do that with the FILTER function.

To do this, you need to check the row number within the FILTER function, and only filter row numbers that meet the row number criteria.

Suppose you have the dataset as shown below and I only want to extract even-numbered records from this dataset.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

Below is the formula that will do this:

\=FILTER($A$2:$C$11,MOD(ROW(A2:A11)-1,2)=0)

![Filter all even numbered rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20346'%3E%3C/svg%3E)

The above formula uses the MOD function to check the row number of each record (which is given by the [ROW function](https://trumpexcel.com/excel-row-function/)
).

The formula MOD(ROW(A2:A11)-1,2)=0 returns TRUE when the row number is even and FALSE when it’s odd. Note that I have subtracted 1 from the ROW(A2:A11) part as the first record is in the second row, and this adjusts the row number to consider the second row as the first record.

Similarly, you can filter all the odd-numbered records using the below formula:

\=FILTER($A$2:$C$11,MOD(ROW(A2:A11)-1,2)=1)

Example 7: Sort the Filtered the Data With Formula
--------------------------------------------------

Using FILTER function with other functions allows us to get a lot more done.

For example, if you filter a dataset using the FILTER function, you can use the SORT function with it to get the result that is already sorted.

Suppose you have a dataset as shown below and you want to filter all the records where the sales value is more than 10000. You can use the SORT function with the function to make sure the resulting data is sorted based on the sales value.

![Dataset on which to use the Excel FILTER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20286'%3E%3C/svg%3E)

The below formula will do this:

\=SORT(FILTER($A$2:$C$11,($C$2:$C$11>10000)),3,-1)

![Sort and Filter the data using SORT and FILTER functions in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20722%20343'%3E%3C/svg%3E)

The above function uses the FILTER function to get the data where the sale value in column C is more than 10000. This array returned by the FILTER function is then used within the SORT function to sort this data based on the sales value.

The second argument in the SORT function is 3, which is to sort based on the third column. And the fourth argument is -1 which is to sort this data in descending order.

**[Click here to download the Example file](https://www.dropbox.com/s/v2r8zqcfmpwbvn9/Filter%20Function%20Examples.xlsx?dl=1)
**

So these are 7 examples to use the FILTER function in Excel.

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

1.  [How to Filter Cells with Bold Font Formatting in Excel](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
2.  [Filter By Color in Excel](https://trumpexcel.com/filter-by-color-excel/)
    
3.  [Dynamic Excel Filter Search Box](https://trumpexcel.com/dynamic-excel-filter/)
    
4.  [How to Filter Data in a Pivot Table in Excel](https://trumpexcel.com/filter-data-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Excel Filter Function – Explained with Examples + Video”
-----------------------------------------------------------------------

1.  How to filter region-wise top 3 data from the database?
    
    [Reply](https://trumpexcel.com/filter-function/#comment-14020)
    
2.  Can filter function on xl apply on google sheet.
    
    [Reply](https://trumpexcel.com/filter-function/#comment-13328)
    
    *   Yes, the FILTER function is also in Google Sheets with slight difference in the syntax. In my opinion, the one is Google Sheets slightly better as it allows you to have multiple conditions as separate arguments (so the AND condition example is easier in Google Sheets).
        
        [Reply](https://trumpexcel.com/filter-function/#comment-13335)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/filter-function/#respond)

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