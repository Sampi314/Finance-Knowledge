# How to Group Numbers in Pivot Table in Excel

**Source:** https://trumpexcel.com/group-numbers-in-pivot-table

---

[Skip to content](https://trumpexcel.com/group-numbers-in-pivot-table/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/group-numbers-in-pivot-table/#below-title)

You can group numbers in Pivot Table to create frequency distribution tables. This helps in analyzing numerical values by grouping it into ranges.

A simple example of this could be to analyze how many students scored marks between 40 and 50 and how many got marks between 50 and 60 and so on..

Another example could be to create a frequency distribution of age of a group of people. This would help in identifying how many people fall in the 30-40 age group and how many in 40-50 age group and so on.

Let’s take an example of retail sales data to see how you can group numbers in Pivot Table in Excel.

**[Click here to Download the Example File to follow along](https://trumpexcel.com/wp-content/uploads/2016/05/Group-numbers-in-Pivot-Table.xlsx)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/group-numbers-in-pivot-table/#)

### Group Numbers in Pivot Table in Excel

Suppose you have retail sales data as shown below:

![Group Numbers in Pivot Table in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20339'%3E%3C/svg%3E)

Using this data, I’ve created a Pivot Table with Stores and Sales in the Rows area and Sales in the Value area. This will give you a Pivot Table as shown below (tabular form):

![Group Numbers in Pivot Table in Excel - Pivot Table Tabular](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20360'%3E%3C/svg%3E)

Note that the values column has COUNT instead of SUM. This can be made by changing the value field settings of the Sales value to display COUNT (as shown below).

![Group Numbers in Pivot Table in Excel - Count display](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20776%20564'%3E%3C/svg%3E)

As of now, the Pivot table isn’t of much use as it shows a lot of data. But you can group the sales value for each store and create a frequency distribution.

To do this:

*   Select any cells in the row labels that have the sales value.
*   Go to Analyze –> Group –> Group Selection.![Group Numbers in Pivot Table in Excel - Analyze Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20136'%3E%3C/svg%3E)
*   In the grouping dialog box, specify the Starting at, Ending at, and By values. In this case, By value is 250, which would create groups with an interval of 250.![Group Numbers in Pivot Table in Excel - gruop by](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20224%20183'%3E%3C/svg%3E)
*   Click OK.

This would create a Pivot Table that shows the frequency distribution of the number of sales transactions within the groups that we created.

![Group Numbers in Pivot Table in Excel - frequency distribution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20334%20378'%3E%3C/svg%3E)

This Pivot Table now has a frequency distribution that can be used for analysis such as:

*   Which stores are doing more high-value transactions?
*   Which stores need to improve sales by trying to increase transaction value?

You can also move the grouped sales to the column area to create a matrix that is even easier to read.

![Group Numbers in Pivot Table in Excel - in Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20237'%3E%3C/svg%3E)

[**Click here**](https://trumpexcel.com/wp-content/uploads/2016/05/Group-numbers-in-Pivot-Table.xlsx)
 **to download the example file**.

### How to Ungroup Numbers in Pivot Table

To ungroup these number groups, select any of the group and go to Analyze –> Group –> Ungroup.

![Group Numbers in Pivot Table in Excel - ungroup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20132'%3E%3C/svg%3E)

### Error While Grouping Numbers in Pivot Table

Sometimes, you may get the ‘Cannot group selection’ error (as shown below) while creating groups with numbers.

![Group Numbers in Pivot Table in Excel - error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20239%20124'%3E%3C/svg%3E)

This may happen if you have cells that contain text instead of numbers.

In such cases, you need to go back to the data source and remove the text with appropriate numerical value.

Sometimes, numbers are stored as text in Excel. In such case, you need to [convert these text to numbers](https://trumpexcel.com/convert-text-to-numbers-excel/)
 before grouping it in Pivot Table.

**You May Also Like the Following Pivot Table Tutorials:**

*   [How to Group Dates in Pivot Table in Excel](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    .
*   [How to Create a Pivot Table in Excel](https://trumpexcel.com/creating-excel-pivot-table/)
    .
*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    .
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    .
*   [Using Slicers in Excel Pivot Table – A Beginner’s Guide.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    .
*   [How to Add and Use an Excel Pivot Table Calculated Field](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    .
*   [Pivot Cache in Excel – What Is It and How to Best Use It?](https://trumpexcel.com/pivot-cache-excel/)
    
*   [Count Distinct Values in Pivot Table](https://trumpexcel.com/count-distinct-pivot-table/)
    
*   [Sort Pivot Table in Excel](https://trumpexcel.com/sort-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Group Numbers in Pivot Table in Excel”
------------------------------------------------------------

1.  Perfect – thanks 🙂
    
    [Reply](https://trumpexcel.com/group-numbers-in-pivot-table/#comment-14526)
    
2.  Thanks! Very helpful
    
    [Reply](https://trumpexcel.com/group-numbers-in-pivot-table/#comment-10975)
    
3.  Hello there:
    
    I am trying to create pivot table/chart for an overtime report. I want to summarize by the workgroup and have the hours fall into a range (0-25), (26-100), (101-200),(201-300),(301-400), (>400). My pie chart will be by the hour range. Also, is there a way to import the data (downloaded from SAP into a .csv file) and automatically populate these graphs and pivot tables?
    
    [Reply](https://trumpexcel.com/group-numbers-in-pivot-table/#comment-8642)
    
4.  Interesting
    
    [Reply](https://trumpexcel.com/group-numbers-in-pivot-table/#comment-3320)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/group-numbers-in-pivot-table/#respond)

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