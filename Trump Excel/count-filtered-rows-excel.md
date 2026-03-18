# How to Count Filtered Rows in Excel? Easy Formula!

**Source:** https://trumpexcel.com/count-filtered-rows-excel

---

[Skip to content](https://trumpexcel.com/count-filtered-rows-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-filtered-rows-excel/#below-title)

If you want to count filtered rows in Excel, you can do that using the SUBTOTAL function.

The SUBTOTAL function allows you to perform a regular count on a column with the ability to exclude those rows that have been filtered out.

In this short tutorial, I will show you how to use the SUBTOTAL function to count filter rows in Excel, and another visual way to quickly identify the total number of filtered rows.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-filtered-rows-excel/#)

Count Filtered Rows Using SUBTOTAL Function
-------------------------------------------

Below is a data set where I have the employee’s name in column A, the department name in column B, and the reporting manager’s name in column C.

![Data set without the filter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20653%20338'%3E%3C/svg%3E)

I have now applied a filter to this data set and filtered out the rows where the department name is finance. So you get the dataset as shown below.

![Data set when the filter has been applied](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20247'%3E%3C/svg%3E)

Now I want to get the count of filtered rows only.

Here is the SUBTOTAL formula that will give me the count of only those rows that are visible after the filtering is applied:

\=SUBTOTAL(3,B2:B10)

![Using subtotal function to count filtered rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20371'%3E%3C/svg%3E)

The above formula gives us 6, which is the total number of rows that we have left after we have filtered the data set.

In the above subtotal function, we have used two arguments:

*   **3 as the first argument** – the first argument of the SUBTOTAL function always needs to be a numeric value that tells the function what kind of operation it needs to do on the following range. Using 3 here tells the function that it needs to give the count of the range (specified in the second argument) and only count the visible rows.
*   **B2:B10** – this is the range on which the count is done.

**Note**: When you use 3 as the first argument, it is going to exclude the rows that have been filtered out (counts only the visible rows). In case you have not filtered your data set and have hidden some rows manually, these would still be counted. However, if you have hidden some rows and then filtered the data, then the hidden rows will not be counted (see the table below for more clarity).

Apart from the above formula, you can also use the below SUBTOTAL formula:

\=SUBTOTAL(103,B2:B10)

The above formula also works the same way, but when you 103, it will also ignore the hidden rows (i.e., not count the hidden rows) in an unfiltered dataset.

Note that these two arguments in the formula (3 and 103) work exactly the same when you use them with filters dataset. Both of these functions will not count rows that have been filtered out as well as those that are hidden.

But if you’re still confused about these two formulas, the table below should clear any confusion.

| Dataset Configuration | Using 3 | Using 103 |
| --- | --- | --- |
| Rows not hidden and not filtered | Counts all visible rows | Counts all visible rows |
| Rows hidden and not filtered | Hidden rows are counted | Hidden rows are not counted |
| Rows not hidden and filtered | Only visible rows are counted. Filtered-out rows are not counted | Only visible rows are counted. Filtered-out rows and hidden rows are not counted. |
| Rows are hidden and filtered | Only visible rows are counted. Filtered-out rows and hidden rows are not counted. | Only visible rows are counted. Filtered-out rows and hidden rows are not counted |

In short, if you have a filtered dataset, both 3 and 103 will give you the same result.

_The above formulas would work with [Excel Tables](https://trumpexcel.com/excel-table/)
 as well_.

Also read: [Select Visible Cells in Excel](https://trumpexcel.com/select-visible-cells/)

Check the Count of Filtered Rows in the Status Bar
--------------------------------------------------

Not many Excel users know this, but the count of filtered rows is also shown in the status bar.

As soon as you apply a filter to your data set, you will notice that the status bar shows you how many cells are visible after the filter from the total number of cells.

![Count of filtered rows in the status bar in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20222'%3E%3C/svg%3E)

Something like **6 of 9 records found** – where 6 is the number of records visible after the filter has been applied and 9 is the total number of records in the data set.

**Note**: Hidden rows do not impact this. It only tells you how many records should be visible after the filtering. If you manually hide any of the rows, that would still be counted.

In this tutorial, I showed you how to use the subtotal function to count filtered rows in Excel. I covered the difference between the two arguments you can use in these SUBTOTAL functions.

And I have also covered how to get the count of filtered rows through the status bar.

**Other Excel articles you may also like:**

*   [Delete All Hidden Rows and Columns in Excel](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
    
*   [Filter By Color in Excel](https://trumpexcel.com/filter-by-color-excel/)
    
*   [Paste into Filtered Column (Skipping Hidden Cells)](https://trumpexcel.com/paste-into-filtered-column/)
    
*   [Excel Filter Function](https://trumpexcel.com/filter-function/)
    
*   [Filter Cells that have Duplicate Text Strings (Words) in it](https://trumpexcel.com/duplicate-text-strings/)
    
*   [Dynamic Excel Filter Search Box – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [Count Rows Using VBA](https://trumpexcel.com/excel-vba/count-rows/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Count Filtered Rows in Excel?”
---------------------------------------------------

1.  Hi  
    Can you tell me the formula for identifying a specific set of text within a set of data and its number of occurances excluding flitered data.  
    Thanks
    
    [Reply](https://trumpexcel.com/count-filtered-rows-excel/#comment-16762)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-filtered-rows-excel/#respond)

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