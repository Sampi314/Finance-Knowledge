# How to Combine Duplicate Rows and Sum the Values in Excel

**Source:** https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel

---

[Skip to content](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/#below-title)

As a part of my full-time job a few years ago, one of the things I had to deal with was to combine data from different workbooks shared by other people.

And one of the common tasks was to combine the data in such a way that there were no duplicate records.

For example, below is a dataset that multiple records for the same region.

![Dataset with duplicate records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20330%20365'%3E%3C/svg%3E)

And the final result needs to be a consolidated dataset where each country is reported only once.

![Dataset where duplicate rows are combines and sum](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20314'%3E%3C/svg%3E)

In this tutorial, I will show you how to combine duplicate rows and sum the values to create a single consolidated dataset.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/#)

Combine and Sum Data Using the Consolidate Option
-------------------------------------------------

If all you need to do is consolidate data and add all the values for the repeating records, it’s best to use the consolidate feature in Excel.

The other method is to [use a Pivot table](https://trumpexcel.com/creating-excel-pivot-table/)
 and summarize the data (covered next in this tutorial).

Suppose you have a data set as shown below where the country name repeats multiple times.

![Dataset with duplicate records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20330%20365'%3E%3C/svg%3E)

While these are unique records as the sales value is different, for reporting purposes you may want to remove multiple instances of the same country and show the sales value as one consolidated sum.

Below are the steps to do this:

1.  Copy the headers of the original data and paste it where you want the consolidated data![Copy the headers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20711%20310'%3E%3C/svg%3E)
2.  Select the cell below the leftmost header![Select the left most cell below the header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20705%20317'%3E%3C/svg%3E)
3.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20201'%3E%3C/svg%3E)
4.  In the Data Tools group, click on the Consolidate icon![Click the Consolidate icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20179'%3E%3C/svg%3E)
5.  In the Consolidate dialog box, select Sum from the function drop-down (if not already selected by default)![Select Sum as the function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20388'%3E%3C/svg%3E)
6.  Click on the range selection icon in the Reference field.![Select the Left Column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20388'%3E%3C/svg%3E)
7.  Select the range A2:B9 (the data excluding the headers)
8.  Select the Left column checkbox![Select the Left Column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20388'%3E%3C/svg%3E)
9.  Click Ok

The above steps would consolidate the data by removing the duplicate entries and adding the values for each country.

![Dataset where duplicate rows are combines and sum](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20314'%3E%3C/svg%3E)

In the end result, you get a unique list of countries along with the sales value from the original data set.

I chose to get the SUM of the values from each record. You can also choose other options such as Count or Average or Max/Min.

In this example, I have shown you how to consolidate the data in a single data set in a worksheet. you can also use this feature to consolidate data from multiple worksheets in the same workbook, and even multiple different workbooks.

Also read: [Remove Duplicates Within a Cell in Excel](https://trumpexcel.com/remove-duplicates-from-cell-excel/)

Combine and Sum Data Using Pivot Tables
---------------------------------------

A Pivot Table is the Swiss army knife of slicing and dicing data in Excel.

It can easily give you a summary which is a combined data set with no duplicates and the values that are the sum of all the similar records, and do a lot more.

The downside of this method as compared to the previous one is that this one takes more clicks and a few more seconds compared to the previous one.

Suppose you have a data set as shown below where the country name repeats multiple times and you want to consolidate this data.![Dataset with duplicate records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20330%20365'%3E%3C/svg%3E)

Below are the steps to create a Pivot table:

1.  Select any cell in the dataset
2.  Click the Insert tab![Click the Insert Option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20201'%3E%3C/svg%3E)
3.  In the Tables group, click on PivotTable option![Click the Pivot Table option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20201'%3E%3C/svg%3E)
4.  In the Create PivotTable dialog box, make sure the Table/Range is correct![Mkae sure the Pivot Table range is correct](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20448'%3E%3C/svg%3E)
5.  Click on the Existing Worksheet![Choose the Existing worksheet option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20448'%3E%3C/svg%3E)
6.  Select the location where you want the resulting Pivot Table to be inserted.![Add the cell reference where you want the resulting pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20448'%3E%3C/svg%3E)
7.  Click OK

The above steps would insert a Pivot table in the selected destination cell.

![Pivot Table inserted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20466'%3E%3C/svg%3E)

Now, we can do all sorts of things with a pivot table – including consolidating our data set and removing the duplicates.

Below are the steps to do this:

1.  Click anywhere in the pivot table area and it would open the pivot table pane on the right
2.  Drag the put the Country field into the Row area
3.  Drag and put the Sales field into the Values area

![Add fileds to the row and value areas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20747'%3E%3C/svg%3E)

The above steps summarize the data and give you the sum of sales for all the countries.

![Resulting summarized data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20246'%3E%3C/svg%3E)

If this is all that you want and you have no need for a pivot table, you can copy the data and [paste it as values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 somewhere else and [delete the pivot table](https://trumpexcel.com/delete-pivot-table/)
.

This will also help you reduce the size of your Excel workbook.

So these are two quick and easy methods that you can use to consolidate the data where it would combine the duplicate rows and sum all the values in those records.

I hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [Combine Data from Multiple Workbooks in Excel](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    
*   [How to Combine Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    
*   [How to Combine Multiple Excel Files Into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    
*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Combine Duplicate Rows and Sum the Values in Excel”
------------------------------------------------------------------------

1.  you made this so easy for a newbie like me, thanks a lot
    
    [Reply](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/#comment-31318)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/#respond)

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