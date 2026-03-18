# How to Sort By Color in Excel (in less than 10 seconds)

**Source:** https://trumpexcel.com/sort-by-color

---

[Skip to content](https://trumpexcel.com/sort-by-color/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-by-color/#below-title)

Excel has a lot of options when it comes to sorting data.

And one of those options allows you to sort your data based on the color of the cell.

For example, in the below dataset, you can sort by color to get the names of all the students who scored above 80 together at the top and all the students who scored less than 35 together at the bottom.

![Sort by Color in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20466%20314'%3E%3C/svg%3E)

With the sorting feature in Excel, you can sort based on the color in the cell.

In this tutorial, I will show you different scenarios where you can sort by color and the exact steps you need to do this.

Note that in this tutorial, I have taken examples where I am sorting based on numeric values. However, these methods work perfectly well even if you have text or dates instead of numbers.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-by-color/#)

Sort Based on a Single Color
----------------------------

If you only have a single color in your dataset, you can easily sort it based on it.

Below is a dataset where all the students who have scored more than 80 have been highlighted in green.

![Sort by single color in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20377'%3E%3C/svg%3E)

Here are the steps to sort by the color of the cells:

1.  Select the entire dataset (A1:B11 in this example)
2.  Click the Data tab![Click the Data Tab in the Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20192'%3E%3C/svg%3E)
3.  Click on the ‘Sort’ option. This will open the Sort dialog box.![Click the Sort Option in the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20569%20192'%3E%3C/svg%3E)
4.  In the Sort dialog box, make sure ‘My Data has headers’ is selected. In case your data doesn’t have headers, you can keep this option unchecked.![Make Sure My Data Has Headers is selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20298'%3E%3C/svg%3E)
5.  Click the ‘Sort By’ drop down and select ‘Marks’. This is the column based on which we want the data to be sorted.![Select Marks from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
6.  In the ‘Sort On’ drop down, click on Cell Color.![Select Cell Color from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
7.  In the ‘Order’ drop-down, select the color based on which you want to sort the data. Since there is only one color in our dataset, it only shows one color (green)![Select the green color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
8.  In the second drop-down in Order, select On-top. This is the place where you specify whether you want all the colored cells at the top of the dataset or at the bottom.![Select On Top from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
9.  Click OK.

The above steps would give you a dataset as shown below.

![Sorted by Single Color - final result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20380'%3E%3C/svg%3E)

**Keyboard Shortcut to Open the Sort Dialog box** – ALT A S S (hold the ALT key then press A S S keys one by one)

Note that sorting based on color only rearranges the cells to bring together all the cells with the same color together. Rest of the cells remain as is.

This method works for cells that you have highlighted manually (by giving it a background color) as well as the ones where the cell color is because of [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 rules.

Sort Based on Multiple Colors
-----------------------------

In the above example, we only had cells with one color that needed to be sorted.

And you can use the same methodology to sort when you have cells with multiple colors.

For example, suppose you have a dataset as shown below where all the cell where the marks are more than 80 are in green color and the ones where marks are less than 35 are in red color.

![Sort by Multiple Colors - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20370'%3E%3C/svg%3E)

And you want to sort this data so that you have all the cells with green at the top and all the ones with red at the bottom.

Below are the steps to sort by multiple colors in Excel:

1.  Select the entire dataset (A1:B11 in this example)
2.  Click the Data tab.
3.  Click on the Sort option. This will open the Sort dialog box.
4.  In the Sort dialog box, make sure ‘My Data has headers’ is selected. In case your data doesn’t have headers, you can keep this option unchecked.
5.  Click the ‘Sort By’ drop down and select ‘Marks’. This is the column based on which we want the data to be sorted.
6.  In the ‘Sort On’ drop down, click on Cell Color.
7.  In the ‘Order’ drop-down, select the first color based on which you want to sort the data. It will show all the colors that are there in the dataset. Select green.![Sort by multiple colors - select Green in the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
8.  In the second drop-down in Order, select On-top.![Sort by Multiple Colors - Select on top option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
9.  Click on Add Level button. This is done to add another condition of sorting (as we want to sort based on two colors). Clicking this button would add another set of sorting options.![Click the Add Level Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
10.  Click the ‘Then by’ drop-down and select ‘Marks’![Add Level and then sort by marks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
11.  In the ‘Sort On’ drop down, click on Cell Color.![Select second level sorting color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
12.  In the ‘Order’ drop-down, select the second color based on which you want to sort the data. It will show all the colors that are there in the dataset. Select Red.![Select red color for second level sorting 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
13.  In the second drop-down in Order, select On-Bottom.![Select On Bottom for second level sorting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)
14.  Click OK

The above steps would sort the data with all the green at the top and all the reds at the bottom.

**Clarification**: Sorting by color works with numbers as well as text data. You may be thinking that you can achieve the results shown above by just sorting the data based on the values. While, this will work in this specific scenario, imagine you have a huge list of clients/customers/products that you have manually highlighted. In that case, there is no numeric value, but you can still sort based on the color of the cells.

Sort Based on Font Color
------------------------

Another amazing thing about sorting in Excel is that you can also sort by font color in the cells.

While this is not as common as getting data where cells are colored, this is still something a lot of people do. After all, it only takes one click to change the font color.

Suppose you have a dataset as shown below and you want to sort this data to get all the cells with the red color together.

![Sort Based on font color - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20342'%3E%3C/svg%3E)

Below are the steps to sort by font color in Excel:

1.  Select the entire dataset (A1:B11 in this example)
2.  Click the Data tab
3.  Click on the Sort option. This will open the Sort dialog box.
4.  In the Sort dialog box, make sure ‘My Data has headers’ is selected. In case your data doesn’t have headers, you can keep this option unchecked.
5.  Click the Sort By drop down and select ‘Marks’. This is the column based on which we want the data to be sorted.
6.  In the ‘Sort On’ drop down, click on Font Color.
7.  In the ‘Order’ drop-down, select the color based on which you want to sort the data. Since there is only one color in our dataset, it only shows one color (red)
8.  In the second drop-down in Order, select On-top. This is the place where you specify whether you want all the colored cells at the top of the dataset or at the bottom.
9.  Click OK.

The above steps would sort the data with all the cells with the font in red color at the top.

![Sort Based on font color - result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20340'%3E%3C/svg%3E)

Sort Based on Conditional Formatting Icons
------------------------------------------

Conditional formatting allows you to add a layer of visual icons that can make your data or your reports/dashboards look a lot better and easy to read.

If you have such data with conditional formatting icons, you can also sort this data based on the icons

Suppose you have a dataset as shown below:

![Sort based on conditional formatting icon - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20376'%3E%3C/svg%3E)

Below are the steps to sort by conditional formatting icons:

1.  Select the entire dataset (A1:B11 in this example)
2.  Click the Data tab
3.  Click on the Sort option. This will open the Sort dialog box.
4.  In the Sort dialog box, make sure ‘My Data has headers’ is selected. In case your data doesn’t have headers, you can keep this option unchecked.
5.  Click the ‘Sort By’ drop down and select ‘Marks’. This is the column based on which we want the data to be sorted.
6.  In the ‘Sort On’ drop down, click on ‘Conditional Formatting Icon’.
7.  In the ‘Order’ drop-down, select the icon based on which you want to sort the data. It will show all the icons that are there in the dataset. Select the green one first.
8.  In the second drop-down in Order, select On-top.
9.  Click on Add Level button. This is done to add another condition of sorting (as we want to sort based on three icons). Clicking this button would add another set of sorting options.
10.  Click the ‘Then by’ drop-down and select ‘Marks’
11.  In the ‘Sort On’ drop down, click on ‘Conditional Formatting Icons’.
12.  In the ‘Order’ drop-down, select the second icon based on which you want to sort the data. It will show all the icons that are there in the dataset. Select yellow.
13.  In the second drop-down in Order, select On-Top.
14.  Click on Add Level button. This is done to add another condition of sorting. Clicking this button would add another set of sorting options.
15.  Click the ‘Then by’ drop-down and select ‘Marks’
16.  In the ‘Sort On’ drop down, click on ‘Conditional Formatting Icons’.
17.  In the ‘Order’ drop-down, select the third icon based on which you want to sort the data. It will show all the icons that are there in the dataset. Select Red.
18.  In the second drop-down in Order, select On-Top.
19.  Click OK.

The above steps would sort the data set and give you all the similar icons together.

![Sort based on conditional formatting icon - result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20380'%3E%3C/svg%3E)

Note that sorting will follow the order in which you have it in the sorting dialog box. For example, if all the icons are set to sort and show at the top, first all the cells with green icons would be shown as it’s at the top in our three conditions. Then the resulting data would have the yellow icons and then the red icons.

Not Losing the Original Order of the Data
-----------------------------------------

When you sort the data, you lose the original order of the dataset.

In case you want to keep the original dataset as well, it’s best to create a copy of the data and then perform the sorting on the copied data.

Another technique to make sure you can get back the original data is to insert a column with [row numbers](https://trumpexcel.com/number-rows-in-excel/)
.

Once you have this column added, use this when sorting the data.

In case you need the original data order back at a later stage, you can easily sort this data based in the columns with the numbers.

Interested in learning more about sorting data in Excel. Here is a massive give on [how to sort in Excel](https://trumpexcel.com/sort-excel/)
 that covers a lot of topics such as sorting by text/dates/numbers, sorting from left-to-right, sorting based on partial text, case sensitive sorting, multi-level sorting and much more.

**You May Also Like the Following Excel Tutorials:**

*   [Highlight Rows Based on a Cell Value in Excel](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Sort by Length in Excel?](https://trumpexcel.com/sort-by-length-excel/)
    
*   [How to Sum by Color in Excel (Formula & VBA)](https://trumpexcel.com/sum-by-color-excel/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [Search and Highlight Data Using Conditional Formatting](https://trumpexcel.com/search-highlight-using-conditional-formatting/)
    
*   [Multiple Level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    
*   [Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    
*   [How to Move Rows and Columns in Excel](https://trumpexcel.com/move-rows-columns/)
    
*   [Highlight the Active Row and Column in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [How to Undo Sort in Excel](https://trumpexcel.com/undo-sort-excel/)
    
*   [Filter By Color in Excel](https://trumpexcel.com/filter-by-color-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Sort By Color in Excel (in less than 10 seconds)”
-----------------------------------------------------------------------

1.  Always helpful. I learn so much with every single tip. Thank you!
    
    [Reply](https://trumpexcel.com/sort-by-color/#comment-11503)
    
2.  Brilliant site
    
    [Reply](https://trumpexcel.com/sort-by-color/#comment-11501)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-by-color/#respond)

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