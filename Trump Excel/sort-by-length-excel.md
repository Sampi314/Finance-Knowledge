# How to Sort by Length in Excel? Easy Formulas!

**Source:** https://trumpexcel.com/sort-by-length-excel

---

[Skip to content](https://trumpexcel.com/sort-by-length-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-by-length-excel/#below-title)

Excel allows you to sort your data set based on numeric values, text values, dates, as well as colors in the cell.

However, there is no inbuilt functionality in Excel to sort the cells based on the length of the text in the cells.

In one of my Excel training sessions, I was asked whether it is possible to ‘sort by the length of text in the cells in Excel or not.

I could come up with two simple methods to do this (there could be more I am sure).

In this tutorial, I’m going to share these two simple methods you can use to quickly **sort by the length in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-by-length-excel/#)

Sort by Length Using the LEN Function + Sort Functionality
----------------------------------------------------------

Below I have a data set where I have the names of some people in column A, and I want to sort this data set based on the length of the name in the cell.

![Names Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20372'%3E%3C/svg%3E)

So, I want the shortest name to be at the top and the longest one at the bottom.

In this method, I will show you how to do this using the helper column along with the inbuilt sort functionality in Excel.

The logic here would be simple, first find out the length of the name in each cell in the helper column, and then use that helper column to sort the data.

Below are the steps to do this:

1.  Enter the text ‘Helper’ in cell B1. This will become the column header for the helper column
2.  In cell B2, enter the below formula:

\=LEN(A2)

![LEN formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20421'%3E%3C/svg%3E)

3.  Apply the formula for all the other cells in column B. You can do this by selecting the cell that already has the formula (B2), placing the cursor on the [Fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
    , and when it turns into the plus icon, double-clicking on it. Or you can simply copy-paste the cell that has the formula to [fill the other remaining cells](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    

![Apply formula to entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20372'%3E%3C/svg%3E)

4.  Select the entire data set – including the helper column as well as the headers

![Select the entire dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20375'%3E%3C/svg%3E)

5.  Click the ‘Data’ tab in the ribbon
6.  Click on the ‘Sort’ icon. This will open the Sort dialog box

![Click the Sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20223'%3E%3C/svg%3E)

7.  In the Sort dialog box, check the option ‘My data has headers’

![Check My data has headers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20298'%3E%3C/svg%3E)

8.  Click the ‘Sort by’ dropdown and select the ‘Helper’ option. Doing this will ensure that the helper column is used to sort the data

![Select the Helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20298'%3E%3C/svg%3E)

9.  Select the Order of sorting (I will go with Smallest to Largest here)

![Select Smallest to Largest](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20298'%3E%3C/svg%3E)

10.  Click OK

The above steps would instantly sort the data based on the length of the name in each cell in column A.

![Final Dataset with names sorted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20373'%3E%3C/svg%3E)

Once you are done with the sorting, you can delete the helper column.

**Pro Tip**: In case you need to keep the original data as well, it’s best to create a backup copy of the dataset

**Note**: I have used the [LEN function](https://trumpexcel.com/excel-len-function/)
 to find out the total number of characters in each cell. In case the cells have [leading, trailing or double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 in between the names, these would also be counted. This can give you unexpected sort results, so make sure to remove any extra spaces.

Sort by Length Using the SORTBY Formula (New Function in Office 365)
--------------------------------------------------------------------

If you’re using the new version of Excel (that comes with the Microsoft 365 subscription), you would have access to additional sort functions that make it really easy to sort based on the length of text.

Below I have the same data set where I have the names in column A and I want to sort this data based on the length of the name.

![Names Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20372'%3E%3C/svg%3E)

Here is the formula that will do this for me:

\=SORTBY(A2:A11,LEN(A2:A11),1)

Enter the above formula in the cell where you want the result. Since this is an array formula, the result would spill over and show the result in the cells below the one where the formula is entered.

![SORTBY function to sort by length in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20424'%3E%3C/svg%3E)

In this example, I have entered this formula in cell B2.

Now, let me quickly explain how this formula works.

In the above SORTBY function I have used three arguments:

*   **The array that needs to be sorted** – this would be the names in column A that needs to be sorted based on the length of the name
*   **The array based on which you need to sort the first array** – this is the criteria based on which we need to sort the names data set. Since I want to sort this based on the length of the name, I have used the LEN function to first calculate the length of the name in each cell and then use that as the criteria to sort the name’s data
*   **Sort order** – I have used 1 here as I want the sorting to be done in ascending order

Also, here are some important things you need to know when using this formula to sort based on text length:

*   Since this is the result of an array formula, you will not be able to change or delete any one cell that has the result of the formula. You can delete the entire result but cannot edit or delete specific elements of the resulting array
*   When you enter the SORTBY formula and hit enter, the result of the formula spills over to the cells below the one where you have entered the formula. If any of the cells (that is supposed to be filled with the resulting array) already has anything in it, the formula would give you the SPILL error. To correct this error, you will have to make sure that the cells are empty so that they can be occupied by the result of the SORTBY formula

So these are two simple ways you can use to quickly **sort based on the text length in the cells in Excel**.

If you’re using an older version of excel, you can use the LEN function along with the sort functionality, and if you’re using the newer versions of Excel and have access to the SORTBY function, you can get this done with a single formula.

I’m sure you can also get this done using VBA or Power Query, but I wanted to keep it simple and show you the two easiest methods that I could come up with.

**Other Excel tutorials you may also like:**

*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [How to SORT in Excel (by Rows, Columns, Colors, Dates, & Numbers)](https://trumpexcel.com/sort-excel/)
    
*   [How to Sort By Color in Excel (in less than 10 seconds)](https://trumpexcel.com/sort-by-color/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [How to Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    
*   [How to Undo Sort in Excel](https://trumpexcel.com/undo-sort-excel/)
    
*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    
*   [Sort Dates By Month in Excel](https://trumpexcel.com/sort-dates-by-month-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-by-length-excel/#respond)

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