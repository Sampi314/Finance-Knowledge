# How to do Multiple Level Data Sorting in Excel

**Source:** https://trumpexcel.com/multiple-level-sorting-excel

---

[Skip to content](https://trumpexcel.com/multiple-level-sorting-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/multiple-level-sorting-excel/#below-title)

_In this tutorial, I cover how to do a multi-level sorting in Excel. You can watch the video below, or you can read the tutorial below it._

When working with data in Excel, [sorting the data](https://trumpexcel.com/sort-excel/)
 is one of the common things you might have to do.

In most of the cases, you need to sort a single column.

But in some cases, there may be a need to sort two columns or more than two columns.

For example, in the below dataset, I want to sort the data by the Region column and then by the Sales Column. This will allow me to see which sales rep has done well in which regions.

![multiple level data sorting in Excel (by two columns) - unsorted Dataset short](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20325%20398'%3E%3C/svg%3E)

While it’s straightforward to sort data by one column in Excel, when it comes to sorting by two columns, you need to take a couple of additional steps.

In this tutorial, I will show you two ways to do a multiple level data sorting in Excel (i.e., sort by two columns)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/multiple-level-sorting-excel/#)

Multi-Level Sorting Using Dialog Box
------------------------------------

When you sort data using the sort dialog box, you get an option to add multiple levels to it.

Here are the steps to do  multi-level sorting using the dialog box:

1.  Select the entire data set that you want to sort.
2.  Click the Data tab.
3.  Click on the Sort Icon (the one shown below). This will open the Sort dialog box.![multi-level data sorting in Excel (two columns) - sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20172'%3E%3C/svg%3E)
4.  In the Sort Dialogue box, make the following selections
    *   Sort by (Column): Region (this is the first level of sorting)
    *   Sort On: Values
    *   Order: A to Z
    *    _If your data has headers, ensure that ‘My data has headers’ option is checked.![multi-level data sorting in Excel (two columns) - sort dialog box column 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)_
5.  Click on Add Level (this will add another level of sorting options).![multi-level data sorting in Excel (two columns) - Add level](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
6.  In the second level of sorting, make the following selections:
    *   Then by (Column): Sales
    *   Sort On: Values
    *   Order: Largest to Smallest![multi-level data sorting in Excel (two columns) - sort dialog box column then by](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
7.  Click OK

The above steps would give you the result as shown below. This sorts the data first by Region and then by Sales column. Note that since it sorts the Region column first when the Sales column is sorted, the Region column remains unchanged.

![multiple level data sorting in Excel (by two columns) - sorted data dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20484'%3E%3C/svg%3E)

In this example, I have sorted the data for two columns. You can have more than two-column sorting as well. All you need to do is add these sorting levels and specify the details.

Note: While this method is longer and takes a few more steps (as compared with the multi-sorting method covered next), I recommend using this as it is less confusing.

Multi-Level Sorting Using Sort Icons
------------------------------------

Not many people know this way of doing a multiple level data sorting in Excel.

This technique works the same way with a minor difference – you sort the second level first and then move to the first level sorting column.

Here are the steps to do it:

1.  Select the column that you want to be sorted last (in this case, select the Sales data first – C1:C13).
2.  Click on the Data tab.
3.  In the Sort and Filter group, click on the Z to A sorting icon. This will sort the sales data from largest to smallest.![multi-level data sorting in Excel (two columns) - z to a icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20172'%3E%3C/svg%3E)
4.  The above step would make a Sort Warning dialog box pop-up. Make sure ‘Expand the selection’ is selected. This makes sure the entire dataset is sorted, and not just data in the Sales column.![Sort Warning in Excel to Expand Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20228'%3E%3C/svg%3E)
5.  Click Sort.
6.  Select the Region column.
7.  In the Data tab, click on the A to Z sort icon.![multi-level data sorting in Excel (two columns) - a to z icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20172'%3E%3C/svg%3E)
8.  In the Sort Warning dialog box pop-up, make sure ‘Expand the selection’ is selected.
9.  Click Sort.

The above steps would sort the data just like it did in the first method.

While this method works fine, I recommend using the sort dialog bo method.

Sort dialog box makes it less error-prone (as you can see which levels getting sorted in which order).

Also, there are more ways to sort data with the dialog box. For example, you can [sort a column based on the cell/font color](https://trumpexcel.com/sort-by-color/)
 and you can also use your own custom sorting criteria.

**You May Also Like the Following Excel Tutorials:**

*   [Sort Data using Custom Lists](https://trumpexcel.com/custom-list-in-excel/)
    
*   [Automatically Sort Data in Alphabetical Oder using Excel Formulas.](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    
*   [How to Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    .
*   [How to do a Multiple Level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    
*   [Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [How to Flip Data in Excel](https://trumpexcel.com/flip-data-in-excel/)
    
*   [How to Undo Sort in Excel](https://trumpexcel.com/undo-sort-excel/)
    
*   [Sort Pivot Table in Excel](https://trumpexcel.com/sort-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to do a Multiple Level Data Sorting in Excel”
----------------------------------------------------------------

1.  Thanks
    
    [Reply](https://trumpexcel.com/multiple-level-sorting-excel/#comment-11915)
    
2.  Great explanation, everything clear , there is no problem anymore. A real professional at work.Thanks 🙂
    
    [Reply](https://trumpexcel.com/multiple-level-sorting-excel/#comment-11371)
    
3.  this is useful i get it
    
    [Reply](https://trumpexcel.com/multiple-level-sorting-excel/#comment-10852)
    
4.  Instructions unclear, massive schlong stuck in disk drive
    
    [Reply](https://trumpexcel.com/multiple-level-sorting-excel/#comment-10570)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/multiple-level-sorting-excel/#respond)

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