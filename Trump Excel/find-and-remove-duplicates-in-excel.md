# Find and Remove Duplicates in Excel - The Ultimate Guide

**Source:** https://trumpexcel.com/find-and-remove-duplicates-in-excel

---

[Skip to content](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#below-title)

**Watch Video – How to Find and Remove Duplicates in Excel**

**_With a lot of data…comes a lot of duplicate data._** 

Duplicates in Excel can cause a lot of troubles. Whether you import data from a database, get it from a colleague, or collate it yourself, duplicates data can always creep in. And if the data you are working with is huge, then it becomes really difficult to find and remove these duplicates in Excel.

![Find and Remove Duplicates in Excel - Image](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20420'%3E%3C/svg%3E)

In this tutorial, I’ll show you how to find and remove duplicates in Excel.

#### **CONTENTS:**

1.  **[FIND and HIGHLIGHT Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Find_and_Highlight_Duplicates_in_Excel)
    .**
    *   [Find and Highlight Duplicates in a Single Column](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Finding_and_Highlight_Duplicates_in_a_Single_Column)
        .
    *   [Find and Highlight Duplicates in Multiple Columns](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Finding_and_Highlight_Duplicates_in_Multiple_Columns)
        .
    *   [Find and Highlight Duplicate Rows](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Finding_and_Highlighting_Duplicate_Rows)
        .
2.  **[REMOVE Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Remove_Duplicates_in_Excel)
    .**
    *   [Remove Duplicates from a Single Column](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Remove_Duplicates_from_a_Single_Column)
        .
    *   [Remove Duplicates from Multiple Columns](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Remove_Duplicates_from_Multiple_Columns)
        .
    *   [Remove Duplicate Rows](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#Remove_Duplicate_Rows)
        .

Find and Highlight Duplicates in Excel
--------------------------------------

Duplicates in Excel can come in many forms. You can have it in a single column or multiple columns. There may also be a duplication of an entire row.

###### Finding and Highlight Duplicates in a Single Column in Excel

[Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 makes it simple to highlight duplicates in Excel.

Here is how to do it:

*   Select the data in which you want to highlight the duplicates.

![Find and Remove Duplicates in Excel - Single Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20129%20299'%3E%3C/svg%3E)

*   Go to Home –> Conditional Formatting –> Highlight Cell Rules –> Duplicate Values.

![Find and Remove Duplicates in Excel - Conditional Formatting Duplicate Values Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20421'%3E%3C/svg%3E)

*   In the Duplicate Values dialog box, select Duplicate in the drop down on the left, and specify the format in which you want to highlight the duplicate values. You can choose from the ready-made format options (in the drop down on the right), or specify your own format.

![Find and Remove Duplicates in Excel - Specify Duplicate Color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20148'%3E%3C/svg%3E)

*   This will highlight all the values that have duplicates.

![Find and Remove Duplicates in Excel - Highlighted values in one column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20297'%3E%3C/svg%3E)

**Quick Tip:** Remember to check for [leading or trailing spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
. For example, “John” and “John ” are considered different as the latter has an extra space character in it. A good idea would be to use the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 to clean your data.

###### Finding and Highlight Duplicates in Multiple Columns in Excel

If you have data that spans multiple columns and you need to look for duplicates in it, the process is exactly the same as above.

Here is how to do it:

*   Select the data.
*   Go to Home –> Conditional Formatting –> Highlight Cell Rules –> Duplicate Values.
*   In the Duplicate Values dialog box, select Duplicate in the drop down on the left, and specify the format in which you want to highlight the duplicate values.
*   This will highlight all the cells that have duplicates value in the selected data set.

![Find and Remove Duplicates in Excel - Highlighted values in multiple columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20271%20299'%3E%3C/svg%3E)

###### Finding and Highlighting Duplicate Rows in Excel

Finding duplicate data and finding duplicate rows of data are 2 different things. Have a look:

![Find and Remove Duplicates in Excel - duplicate rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20723%20326'%3E%3C/svg%3E)Finding duplicate rows is a bit more complex than finding duplicate cells.

Here are the steps:

*   In an adjacent column, use the following formula:  
    \=A2&B2&C2&D2  
    Drag this down for all the rows. This formula combines all the cell values as a single string. (You can also use the [CONCATENATE function](https://trumpexcel.com/excel-concatenate-function/)
     to combine text strings)

![Find and Remove Duplicates in Excel - duplicate rows data combines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20276'%3E%3C/svg%3E)By doing this, we have created a single string for each row. If there are duplicate rows in this dataset, then these strings would be exactly the same for it.

Now that we have the combined strings for each row, we can use conditional formatting to highlight duplicate strings. A highlighted string implies that the row has a duplicate.

Here are the steps to highlight duplicate strings:

*   Select the range that has the combined strings (E2:E16 in this example).
*   Go to Home –> Conditional Formatting –> Highlight Cell Rules –> Duplicate Values.
*   In the Duplicate Values dialog box, make sure Duplicate is selected and then specify the color in which you want to highlight the duplicate values.

This would highlight the duplicate values in column E.

![Find and Remove Duplicates in Excel - highlight duplicate row string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20300'%3E%3C/svg%3E)In the above approach, we have highlighted only the strings that we created.

But what if you want to highlight all the duplicate rows (instead of highlighting cells in one single column)?

Here are the steps to highlight duplicate rows:

*   In an adjacent column, use the following formula:  
    \=A2&B2&C2&D2  
    Drag this down for all the rows. This formula combines all the cell values as a single string.

![Find and Remove Duplicates in Excel - duplicate rows data combines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20276'%3E%3C/svg%3E)

*   Select the data A2:D16.
*   With the data selected, go to Home –> Conditional Formatting –> New Rule.

![Find and Remove Duplicates in Excel - New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20194%20376'%3E%3C/svg%3E)

*   In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
*   In the field below, use the following [COUNTIF](https://trumpexcel.com/excel-countif-function/)
     function:  
    \=COUNTIF($E$2:$E$16,$E2)>1

![Find and Remove Duplicates in Excel - Formula in CF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20393%20379'%3E%3C/svg%3E)

*   Select the format and click OK.

This formula would highlight all the rows that have a duplicate.

![Find and Remove Duplicates in Excel - Duplicate rows highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20298'%3E%3C/svg%3E)

Also read: [Remove Duplicates Within a Cell in Excel](https://trumpexcel.com/remove-duplicates-from-cell-excel/)

Remove Duplicates in Excel
--------------------------

In the above section, we learned how to find and highlight duplicates in excel. In this section, I will show you how to get rid of these duplicates.

###### **Remove Duplicates from a Single Column in Excel**

If you have the data in a single column and you want to remove all the duplicates, here are the steps:

*   Select the data.
*   Go to Data –> Data Tools –> Remove Duplicates.![Find and Remove Duplicates in Excel - Data Remove Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20137'%3E%3C/svg%3E)
*   In the Remove Duplicates dialog box:
    *   If your data has headers, make sure the ‘My data has headers’ option is checked.
    *   Make sure the column is selected (in this case there is only one column).

![Find and Remove Duplicates in Excel - delete duplicate dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20466%20309'%3E%3C/svg%3E)

*   Click OK.

This would remove all the duplicate values from the column, and you would have only the unique values.

_**CAUTION:** This alters your data set by removing duplicates. Make sure you have a back-up of the original data set. If you want to extract the [unique values](https://trumpexcel.com/unique-items-from-a-list-in-excel/)
 at some other location, copy this dataset to that location and then use the above-mentioned steps. Alternatively, you can also use [Advanced Filter to extract unique values](https://trumpexcel.com/excel-advanced-filter/)
 to some other location._

###### **Remove Duplicates from Multiple Columns in Excel**

Suppose you have the data as shown below:

![Find and Remove Duplicates in Excel - delete duplicates multiple row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20299'%3E%3C/svg%3E)

In the above data, row #2 and #16 have the exact same data for Sales Rep, Region, and Amount, but different dates (same is the case with row #10 and #13). This could be an entry error where the same entry has been recorded twice with different dates.

To [delete the duplicate row](https://trumpexcel.com/delete-rows/)
 in this case:

*   Select the data.
*   Go to Data –> Data Tools –> Remove Duplicates.![Find and Remove Duplicates in Excel - Data Remove Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20137'%3E%3C/svg%3E)
*   In the Remove Duplicates dialog box:
    *   If your data has headers, make sure the ‘My data has headers’ option is checked.
    *   Select all the columns except the Date column.

![Find and Remove Duplicates in Excel - delete duplicates multiple row selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20292'%3E%3C/svg%3E)

*   Click OK.

This would remove the 2 duplicate entries.

NOTE: This keeps the first occurrence and removes all the remaining duplicate occurrences.

###### **Remove Duplicate Rows in Excel**

To delete duplicate rows, here are the steps:

*   Select the entire data.
*   Go to Data –> Data Tools –> Remove Duplicates.![Find and Remove Duplicates in Excel - Data Remove Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20137'%3E%3C/svg%3E)
*   In the Remove Duplicates dialog box:
    *   If your data has headers, make sure the ‘My data has headers’ option is checked.
    *   Select all the columns.

![Find and Remove Duplicates in Excel - delete duplicate row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20293'%3E%3C/svg%3E)

*   Click OK.

Use the above-mentioned techniques to clean your data and get rid of duplicates.

You May Also Like the Following Excel Tutorials:

*   [10 Ways to Clean Data in Excel Spreadsheets.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [Remove Leading and Trailing Spaces in Excel](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    .
*   [24 Daily Excel Issues and their Quick Fixes](https://trumpexcel.com/24-excel-tricks/)
    .
*   [How to Find Merged Cells in Excel.](https://trumpexcel.com/find-merged-cells/)
    
*   [Remove Duplicate Values in Excel Using VBA](https://trumpexcel.com/excel-vba/remove-duplicate-values/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “Find and Remove Duplicates in Excel”
----------------------------------------------------

1.  This blog is very neat and helpful with proper details. I came across this when I was trying to figure out a way to find duplicates in excel rows.
    
    Thank you for writing this. Truly appreciate the efforts.
    
    Thank you!
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-31253)
    
2.  hi,  
    i have two column to remove duplicate entry, but i wanna remove only one to one, if the same figure exist three time in column 1 and in 2nd column exist two time i wanna remove one to one figure while i compare two column,  
    3rd one figure should not be delete and cell should not up and down,  
    Please guide me.
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-12501)
    
3.  Useful tip with nice article keep sharing articles
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-11117)
    
4.  I have a question that I can’t find the answer to. How do i find and delete duplicate row data in multiple column data when columns are not unique. For example I have fantasy football lineup combinations and you would have a QB RB RB WR WR WR TE DST K and I want to eliminate duplicate lineups. However, a WR could show up in any of those WR columns and you could have the same group of players show up in multiple rows depending on which column that player got entered in but its really the same lineup.
    
    Is there a way to get around this to remove duplicate rows?
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2609)
    
5.  dear sir how ca i insert a column between 1  
    1  
    2  
    3  
    4  
    6  
    8  
    12  
    15
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2342)
    
6.  concoranate better than index
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2341)
    
7.  Nice and neatly explained. Can we find the same with the help of Vlookup or not?
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2340)
    
    *   Thanks for commenting Narendra.. Finding duplicates using VLOOKUP may not be the best way to go about it
        
        [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2415)
        
8.  Hi Sumit,  
    I have an query that if i want to know that which no. is repeated how many times then which formula should we use.
    
    Like I want to check that every duplicate value is how many times repeated. Please explain.
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2339)
    
9.  I like the caption you put on the photo! 🙂
    
    Nicely explained article on the topic. Just one gentle reminder on the use of Concatenate in your example. In normal case, there won’t be an issue but to play safe, I would suggest the use of a delimiter in between. i.e. A2&”|”&B2&”|”&C2&”|”&D2……
    
    Please see my post here for reference:  
    [http://wmfexcel.com/2015/02/14/pay-attention-when-you-concatenate-a1-b1-vs-a1-b1/](http://wmfexcel.com/2015/02/14/pay-attention-when-you-concatenate-a1-b1-vs-a1-b1/)
    
    Cheers,  
    MF
    
    [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2327)
    
    *   Thanks for sharing.. Using CONCATENATE is definitely a better idea. I avoided a delimiter as it works fine without it too, but it surely does improve the readability of the string
        
        [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2328)
        
        *   Hi Sumit,  
            My point is not about readability, it’s about robustness of the formula.  
            There are rare cases that may give you wrong “duplicated rows” without the use of delimiter.
            
            [Reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#comment-2329)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-and-remove-duplicates-in-excel/#respond)

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