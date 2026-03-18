# How to Undo Sort in Excel (Revert to Original)

**Source:** https://trumpexcel.com/undo-sort-excel

---

[Skip to content](https://trumpexcel.com/undo-sort-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/undo-sort-excel/#below-title)

It’s common for Excel users to sort their data set when they’re analyzing.

Sometimes, you may want to revert to the original data that you had before you did the sorting.

In this tutorial, I will cover four techniques you can use to undo the sorting you have done on a dataset. The method you choose will depend upon your dataset in your situation.

Let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/undo-sort-excel/#)

Method 1 – Undo Sort Using Control + Z to Undo Sort
---------------------------------------------------

If you have just sorted the data and want to revert to the original data before the sort, you can do that by using the below [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
.

**Control + Z** (in Windows)

![Control Z shortcut in Excel keyboard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20254'%3E%3C/svg%3E)

To use the shortcut, hold the control key and then press the Z key once.

If you’re using a Mac, you can use **Command + Z**

This is the keyboard shortcut to undo your last action, and when your last action was to sort your dataset, using the shortcut would undo the sort.

**Advanced Excel Tip**: If you have used the above shortcut to undo the sort and you want to get the sort applied again, you can use the keyboard shortcut **Control + Y**

You can only use this keyboard shortcut to undo the sort action right after you have done the sorting. If you have done anything else after the sorting operation, you will have to use the above keyboard shortcut multiple times so that all the actions still the sorting action have been undone. This also means that any changes you made after sorting the data would also be undone.

Also read: [How to SORT in Excel (by Rows, Columns, Colors, Dates, & Numbers)](https://trumpexcel.com/sort-excel/)

Method 2 – Revert to Original Sort Using Helper Column
------------------------------------------------------

Let me show you a more advanced and foolproof way to revert to the original sort order of a dataset.

For this method, we will have to add a helper column where we would add sequential numbers before sorting the data.

And when you want to undo the sort and get the original data back, you can simply sort the helper column.

Below I have a data set where I have city names in column A and their sales values in column B, and I want to sort this dataset based on the sales values.

![Data set with city name and sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20310'%3E%3C/svg%3E)

However, I want to have the ability to unsort this data and get the original data back in case I need it in the future.

Below are the steps to unsort a data set using a helper column:

1.  Add a [new blank column](https://trumpexcel.com/insert-columns-in-excel/)
     to the left of column A. To do this, right-click on the column header and then click on the Insert option

![add the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20298%20403'%3E%3C/svg%3E)

2.  Add a column header for this helper column (I am using the text ‘Helper’)

![Helper column added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20310'%3E%3C/svg%3E)

3.  In the new column that is inserted, [enter sequential numbers](https://trumpexcel.com/number-rows-in-excel/)
     starting from 1

![enter sequential numbers in the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20311'%3E%3C/svg%3E)

4.  Select the entire data set and sort it based on the sales column values.

![data sorted based on the sales column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20311'%3E%3C/svg%3E)

This gives us the [sorted data](https://trumpexcel.com/multiple-level-sorting-excel/)
, along with an extra helper column, which we can use in case we want to revert to the original data using the below steps.

5.  Select the entire data set, including the Helper column
6.  Click the Data tab

![click the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20614%20178'%3E%3C/svg%3E)

7.  Click the Sort icon

![click the sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20442%20131'%3E%3C/svg%3E)

8.  In the Sort dialog box, select Helper in the Sort By drop-down and set the Order to ‘Smallest to Largest’.

![sort helper column from smallest to largest](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20268'%3E%3C/svg%3E)

9.  Click Ok

The above steps would sort your entire data set using the helper column and bring it back to the original order where the numbers in the helper column were in a sequence (starting from 1)

![unsorted data reverted back to original](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20311'%3E%3C/svg%3E)

Once you have the original sort order, you can delete the helper column if you want.

_Note: You can only use this method if you have added the helper column before you do the sorting._

The benefit of this method is that it allows you to undo the sort anytime after you do the sorting. For example, if you sorted your data and did many other things in your worksheet, you can still get the original sort order back without disrupting the changes you made after the sorting. This is something you cannot do when using the keyboard shortcut covered in the previous method.

Also read: [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)

Method 3 – Create a Back-Up Copy of Your Data
---------------------------------------------

One of the best methods to have the ability to revert to the original data set after sorting is to create a backup copy of your data set.

You can either create a copy of the worksheet and hide it or create a copy of the entire workbook.

This way, in case you need to get the original data sometime in the future after sorting it, you can refer to the backup copy of the data.

In this article, I’ve covered three methods you can use to undo the sort in Excel. if you have just sorted the data and want to get the original data back, you can use the keyboard shortcut Control + Z.

And if you want the ability to get the original data back sometime in the future after sorting that data, you can use the helper column with the sequential numbers method.

**Other Excel articles you may also find helpful:**

*   [How to Sort by Length in Excel?](https://trumpexcel.com/sort-by-length-excel/)
    
*   [How to Edit Cells in Excel? (Shortcuts)](https://trumpexcel.com/edit-cells-excel/)
    
*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [Separate First And Last Name In Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    
*   [How to Sort By Color in Excel](https://trumpexcel.com/sort-by-color/)
    
*   [How to Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    
*   [How to Undo in Power Query?](https://trumpexcel.com/power-query/undo/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/undo-sort-excel/#respond)

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