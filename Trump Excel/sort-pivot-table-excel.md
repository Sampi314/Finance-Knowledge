# How to Sort Pivot Table in Excel - All You Need to Know!

**Source:** https://trumpexcel.com/sort-pivot-table-excel

---

[Skip to content](https://trumpexcel.com/sort-pivot-table-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-pivot-table-excel/#below-title)

[Pivot Tables](https://trumpexcel.com/pivot-table/)
 come with a lot of in-built sorting options that allow you to structure your data the way you want.

While you can use the regular sorting options (sorting A-Z / Z-A or Smallest to Largest or Largest to Smallest), there are also options to sort based on a custom list and even specify the sorting order manually.

In this article, I will cover everything you need to know about sorting Pivot Tables in Excel.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/hto0d85dj8rkv4hsk9h26/Pivot-Table-Sorting.xlsx?rlkey=oprdguqf6eli5vm8wxjgh8cnp&dl=1)
_**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-pivot-table-excel/#)

Sort Rows or Columns Area
-------------------------

When you [create a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
, the rows and the columns area are automatically sorted in an ascending order.

For example, in the below Pivot Table, you can see that the _Salesperson_ names in the row area and the _Category_ names in the column area are sorted alphabetically in an ascending order from A to Z.

![Pivot table data set for sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20662%20596'%3E%3C/svg%3E)

If you want to change the sort order, here’s how to do it.

1.  Click on the drop-down icon in the Salesperson’s cell.
2.  Select from the options to _Sort A to Z_ or _Sort Z to A_. In this example, let’s choose the _Sort Z to A_ option.

![Sort Z to A in Excel pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201156%20769'%3E%3C/svg%3E)

Alternatively, you can also select any cell in the column, then go to the Data tab, and click on the sort icons.

![Sort icons in the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20935%20533'%3E%3C/svg%3E)

This will give you the dataset as shown below.

![Names sorted in the sending order in the pivot table.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20592'%3E%3C/svg%3E)

Now here is an interesting thing about sorting in pivot tables.

When you apply a sort order to a column, the PivotTable is going to remember it and even if you change the structure of your PivotTable, that sort order would still be maintained.

For example, if I add the Category option to the rows area as well, you will notice that within each Category, the names data is still sorted in the descending order.

![Names sorted even when there is an outer field pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20741%201340'%3E%3C/svg%3E)

Even if you remove the salesperson’s names data from the Pivot Table and then add it back, it would still be sorted in the descending order.

Similarly, if you want to sort the data in the columns area, you can do the same thing by:

1.  Clicking on the drop-down in the column label cell and then choosing the sort order, or
2.  Selecting any cell in the columns area and then using the sort options in the _Data_ tab

**Important Note**: When you create a Pivot Table, the sorting preference is given to custom lists that are already saved in your Excel application. This is why when you create a pivot table that has month names, those would be listed chronologically (January, February, March) and not alphabetically. If there are no custom lists relevant for your dataset, then your data would be sorted in an alphabetically in an ascending order.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/hto0d85dj8rkv4hsk9h26/Pivot-Table-Sorting.xlsx?rlkey=oprdguqf6eli5vm8wxjgh8cnp&dl=1)
_**

Sort the Values Area
--------------------

In most cases, you would want to apply sorting to the values area in your pivot table.

For example, in the below Pivot Table, I want to sort the Clothing column in a descending order (from largest to smallest).

![Dataset to sort values area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201358%20655'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select any cell in the Clothing column (or any column based on which you want to do the sorting)
2.  Click the _Data_ tab in the ribbon.
3.  Click on the _Sort Largest to Smallest_ icon (the Z to A icon)

![Click on the descending icon in the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201023%20533'%3E%3C/svg%3E)

Alternatively, you can also right-click on any cell in the Clothing column and go to the _Sort_ option and click on the _Sort Largest to Smallest_ option.

This will sort the Clothing column in descending order.

![Dataset to sort values area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201358%20655'%3E%3C/svg%3E)

Unlike the row and column area level sorting (where Pivot Table remembers the sorting that you applied) in case of the values area, it won’t.

For eg., if I remove the revenues value and add it back again, it would forget that I sorted the clothing column in a descending order. It would revert to showing the sales rep names in the alphabetical order or whatever sorting has been applied on that column.

### Sort Left to Right in Values Area

You can also sort the data set in a Pivot Table from left to right.

Below I have a pivot table where I have:

*   Salespeople’s names in the rows area
*   Categories in the columns area
*   Values showing the sum of sales

![Dataset to sort values area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201358%20655'%3E%3C/svg%3E)

Now, in this Pivot Table, I want to sort the data for Emma Brown from largest to smallest.

Here are the steps to do this:

1.  Select any cell in the row that shows the values for Emma Brown.
2.  Click the _Data_ tab in the ribbon.
3.  Click on the _Sort_ icon.

![Click on the sort icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20937%20533'%3E%3C/svg%3E)

4.  In the Sort by Value dialog box that opens, select the following:
    *   Sort options – _Largest to Smallest_
    *   Sort direction – _Left to Right_

![Select Left to Right in the Sort by value dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20962%20794'%3E%3C/svg%3E)

5.  Click OK

This will sort the Pivot Table based on the values in the row for Emma Brown.

![Left to right sort in pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201342%20652'%3E%3C/svg%3E)

Sorting the Outer Row Field in Pivot Table
------------------------------------------

Below I have a pivot table where I have already sorted the data based on sales value in a descending order. So the person with highest sales shows up at the top and the one with lowest shows up at the bottom.

![Pivottable with data sorted in descending order by sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20660%20595'%3E%3C/svg%3E)

Now, if I add the _Category_ as the outer field in this Pivot Table, you will get something as shown below:

![Outer field Sorted alphabetically](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%201317'%3E%3C/svg%3E)

Now you can see that while the salesperson’s names are sorted in a descending order based on their sales values, the outer category (which has Clothing, Electronics, and Furniture) is not sorted based on the total sales values (it’s sorted alphabetically).

It would be more useful if the category is also sorted in the descending order, where the one with the largest sales is shown at the top.

And this can be fixed easily.

Pivot Table considers the outer field and the inner field as separte datasets, and you can apply the same or different sorting criteria to each of these fields.

So, if in this example I want the outer field to be sorted in a descending order as well, I would select any cell in the values area corresponding to the outer field and apply the sorting (using the sort icons in the Data tab in the ribbon).

![Select the outer field cell and then click on the sort icon.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201928%201727'%3E%3C/svg%3E)

For example, if I choose cell B4 and apply the descending sort order. I’ll get something as shown here.

![Outer field is also sorted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%201293'%3E%3C/svg%3E)

Sorting the outer field will not disturb the sorting already applied on the inner field.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/hto0d85dj8rkv4hsk9h26/Pivot-Table-Sorting.xlsx?rlkey=oprdguqf6eli5vm8wxjgh8cnp&dl=1)
_**

Manual Sorting in Pivot Tables
------------------------------

Pivot Tables also have an interesting Manual sorting option where you can set the sorting criteria by manually rearrangging the rows and columns around.

Below, I have a Pivot Table where I have the salesperson’s name in the rows area and the product category in the columns area.

![Dataset to sort values area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201358%20655'%3E%3C/svg%3E)

By default, my Pivot Table is sorted in the alphabetical order (for both Salesperson’s name and the Category names).

Now let’s say that I want to focus on the Furniture category and would like it to show up at the first column.

Here are the steps to manually do this:

1.  Select the Furniture column label, which is the cell that contains the text Furniture.
2.  Place the cursor around the edge of the selection. You’ll notice that your cursor changes to a four-arrow pointed icon.

3.  Press the left mouse key and then drag the cell to the position where you want it. You will see a thick green line as you are moving the cursor. Bring the line where you want the column and then leave the mouse key. In this case, I will drag it right next to the Salesperson column

![Manual Sorting in Pivot Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201286%20658'%3E%3C/svg%3E)

By doing this, I have sorted my Pivot Table manually, where Furniture becomes the first column, and all the remaining columns shift to the right.

Another way to do manual sorting is to simply change the column label. For example, if I want the furniture column to appear instead of the clothing column, I can just change the word ‘Clothing’ to ‘Furniture’ and as soon as I hit Enter, Pivot Table would understand that I want to do the manual sorting, so it will bring the Furniture column in place of the Clothing column and shift the Clothing column to the right.

**Caution when using Manual Sorting:**

*   There is no visual indication showing that manual sorting has been done (except that my column label data is not sorted in the alphabetical order).
*   When you sort a column in an ascending or descending order, and then you use manual sorting, it is going to redo the sorting based on what column now appears in its position. For example, if my data was sorted based on the Clothing column in a descending order, and then I apply manual sorting, it will then sort based on whatever column takes the position of the Clothing column. This is non-intuitive and can be confusing.

**_[Click here to download the example file](https://www.dropbox.com/scl/fi/hto0d85dj8rkv4hsk9h26/Pivot-Table-Sorting.xlsx?rlkey=oprdguqf6eli5vm8wxjgh8cnp&dl=1)
_**

Sort Using Custom List
----------------------

You can also create your own custom lists that can be used for sorting the data in the rows and columns area in your Pivot Tables.

Custom lists get priority when it comes to sorting pivot tables. So if you already have a custom list, Pivot Table will first use that to apply the sorting criteria, and if there is no relevant custom list, it will sort alphabetically.

Excel already has four built-in custom lists.

*   Sun, Mon, Tue,….
*   Sunday, Monday, Tuesday….
*   Jan, Feb, Mar,….
*   January, February, March,….

This is why when you add dates to the rows or columns area and show the data based on days or months, it is going to use these built-in custom lists to arrange the data.

Below is an example where I have added Months (Date) in the Rows area and Revenue in the columns area.

![Pivot Table shows data using inbuilt custom list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20661%20355'%3E%3C/svg%3E)

You can see that it automatically puts January at the top, followed by February, March, and so on (which makes sense).

You can also create your own custom list that would be used by default when you create any new Pivot Table.

For example, let’s say I have the same data and I always want to show my data in the following order: _Furniture –> Clothing –> Electronics_

Here are the steps to create your own custom list:

1.  Click the _File_ tab.

![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20880%20533'%3E%3C/svg%3E)

2.  In the backstage area that opens, click on _Options_.
3.  In the _Excel Options_ dialog box, click on the _Advanced_ option in the left pane.

![Select the advanced option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201193%201008'%3E%3C/svg%3E)

4.  Scroll down and at the bottom, you’ll find a button called _Edit custom lists_. Click on it.

![Click on the Edit Custom Lists button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201812%20847'%3E%3C/svg%3E)

5.  In the Custom List dialog box, enter the custom list you want in the _List Entries_ box. Put each item on a separate line.

![Enter each item on a separate line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201492%201290'%3E%3C/svg%3E)

6.  Click on Add

The above steps would create a custom list that would now be used when you create any new pivot table.

When I manually enter the items in the custom list, you can also have these items in a range in Excel and then import it into the custom list dialog box.

So now, if I create my pivot table again from scratch from the source data and then put the category field in the columns area, it would automatically sort it using the custom list I created.

This article covered everything you need to know about sorting in Pivot Tables and some sorting tricks that you can use to help you get the data in the structure that you want.

I hope you found this article helpful. In case you have any questions or suggestions, please let me know in the comments section.

**Other Excel and Pivot Table articles you may also like:**

*   [Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    
*   [Change Pivot Table to Tabular Form](https://trumpexcel.com/pivot-table-tabular-form/)
    
*   [Pivot Table Keyboard Shortcuts](https://trumpexcel.com/pivot-table-shortcuts/)
    
*   [Connect a Single Slicer to Multiple Pivot Tables](https://trumpexcel.com/connect-slicer-to-multiple-pivot-tables/)
    
*   [Using Slicers in Excel Pivot Table](https://trumpexcel.com/slicers-excel-pivot-table/)
      
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-pivot-table-excel/#respond)

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