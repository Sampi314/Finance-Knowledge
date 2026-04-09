# Creating a Pivot Table in Excel - Step by Step Tutorial

**Source:** https://trumpexcel.com/creating-excel-pivot-table

---

[Skip to content](https://trumpexcel.com/creating-excel-pivot-table/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/creating-excel-pivot-table/#below-title)

If you are reading this tutorial, there is a big chance you have heard of (or even used) the Excel Pivot Table. It’s one of the most powerful features in Excel (no kidding).

The best part about using a Pivot Table is that even if you don’t know anything in  Excel, you can still do pretty awesome things with it with a very basic understanding of it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/creating-excel-pivot-table/#)

Let’s get started.

**[Click here](https://trumpexcel.com/wp-content/uploads/2016/04/Pivot-Table-Data.xlsx)** to download the sample data and follow along.

What is a Pivot Table and Why Should You Care?
----------------------------------------------

A Pivot Table is a tool in Microsoft Excel that allows you to quickly summarize huge datasets (with a few clicks).

Even if you’re absolutely new to the world of Excel, you can easily use a Pivot Table. It’s as easy as dragging and dropping rows/columns headers to create reports.

Suppose you have a dataset as shown below:

![Creating a Pivot Table in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20306'%3E%3C/svg%3E)

This is sales data that consists of ~1000 rows.

It has the sales data by region, retailer type, and customer.

Now your boss may want to know a few things from this data:

*   What were the total sales in the South region in 2016?
*   What are the top five retailers by sales?
*   How did The Home Depot’s performance compare against other retailers in the South?

You can go ahead and use [Excel functions](https://trumpexcel.com/excel-functions/)
 to give you the answers to these questions, but what if suddenly your boss comes up with a list of five more questions.

You’ll have to go back to the data and create new formulas every time there is a change.

This is where Excel Pivot Tables comes in really handy.

Within seconds, a Pivot Table will answer all these questions (as you’ll learn below).

But the real benefit is that it can accommodate your finicky data-driven boss by answering his questions immediately.

It’s so simple, you may as well take a few minutes and show your boss how to do it himself.

Hopefully, now you have an idea of why Pivot Tables are so awesome. Let’s go ahead and create a Pivot Table using the data set (shown above).

Inserting a Pivot Table in Excel
--------------------------------

Here are the steps to create a pivot table using the data shown above:

*   Click anywhere in the dataset.
*   Go to Insert –> Tables –> Pivot Table.![Creating a Pivot Table in Excel - Insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20134'%3E%3C/svg%3E)
*   In the Create Pivot Table dialog box, the default options work fine in most of the cases. Here are a couple of things to check in it:
    *   _Table/Range:_ It’s filled in by default based on your data set. If your data has no blank rows/columns, Excel would automatically identify the correct range. You can manually change this if needed.
    *   If you want to create the Pivot Table in a specific location, under the option ‘Choose where you want the PivotTable report to be placed’, specify the Location. Else, a new worksheet is created with the Pivot Table.![Creating a Pivot Table in Excel - Insert Pivot Dialog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20354'%3E%3C/svg%3E)
*   Click OK.

As soon as you click OK, a new worksheet is created with the Pivot Table in it.

While the Pivot Table has been created, you’d see no data in it. All you’d see is the Pivot Table name and a single line instruction on the left, and [Pivot Table Fields](https://trumpexcel.com/show-pivot-table-fields/)
 on the right.

![Creating a Pivot Table in Excel - Blank Pivot Table Worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20265'%3E%3C/svg%3E)

Now before we jump into analyzing data using this Pivot Table, let’s understand what are the nuts and bolts that make an Excel Pivot Table.

Also read: [10 Excel Pivot Table Keyboard Shortcuts](https://trumpexcel.com/pivot-table-shortcuts/)

The Nuts & Bolts of an Excel Pivot Table
----------------------------------------

To use a Pivot Table efficiently, it’s important to know the components that create a pivot table.

In this section, you’ll learn about:

*   Pivot Cache
*   Values Area
*   Rows Area
*   Columns Area
*   Filters Area

### Pivot Cache

As soon as you create a Pivot Table using the data, something happens in the backend. Excel takes a snapshot of the data and stores it in its memory. This snapshot is called the Pivot Cache.

When you create different views using a Pivot Table, Excel does not go back to the data source, rather it uses the Pivot Cache to quickly analyze the data and give you the summary/results.

The reason a pivot cache gets generated is to optimize the pivot table functioning. Even when you have thousands of rows of data, a pivot table is super fast in summarizing the data. You can drag and drop items in the rows/columns/values/filters boxes and it will instantly update the results.

_Note: One downside of pivot cache is that it increases the size of your workbook. Since it’s a replica of the source data, when you create a pivot table, a copy of that data gets stored in the Pivot Cache._

**Read More:** [What is Pivot Cache and How to Best Use It](https://trumpexcel.com/pivot-cache-excel/)
.

### Values Area

The Values Area is what holds the calculations/values.

Based on the data set shown at the beginning of the tutorial, if you quickly want to calculate total sales by region in each month, you can get a pivot table as shown below (we’ll see how to create this later in the tutorial).

The area highlighted in orange is the Values Area.

![Creating a Pivot Table in Excel - Values Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20179'%3E%3C/svg%3E)

In this Pivot Table example, it has the total sales in each month for the four regions.

### Rows Area

The headings to the left of the Values area makes the Rows area.

In the example below, the Rows area contains the regions (highlighted in red):  
![Creating a Pivot Table in Excel - Rows Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20541%20141'%3E%3C/svg%3E)

### Columns Area

The headings at the top of the Values area makes the Columns area.

In the example below, Columns area contains the months (highlighted in red):

![Creating a Pivot Table in Excel - Columns Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20141'%3E%3C/svg%3E)

### Filters Area

Filters area is an optional filter that you can use to further drill down in the data set.

For example, if you only want to see the sales for Multiline retailers, you can select that option from the drop down (highlighted in the image below), and the Pivot Table would update with the data for Multiline retailers only.

![Creating a Pivot Table in Excel - Filters Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20174'%3E%3C/svg%3E)

Analyzing Data Using the Pivot Table
------------------------------------

Now, let’s try and answer the questions by using the Pivot Table we have created.

**[Click here](https://trumpexcel.com/wp-content/uploads/2016/04/Pivot-Table-Data.xlsx)** to download the sample data and follow along.

To analyze data using a Pivot Table, you need to decide how you want the data summary to look in the final result. For example, you may want all the regions in the left and the total sales right next to it. Once you have this clarity in mind, you can simply drag and drop the relevant fields in the Pivot Table.

In the Pivot Tabe Fields section, you have the fields and the areas (as highlighted below):

![Creating a Pivot Table in Excel - Fields and Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20292%20420'%3E%3C/svg%3E)

The Fields are created based on the backend data used for the Pivot Table. The Areas section is where you place the fields, and according to where a field goes, your data is updated in the Pivot Table.

It’s a simple drag and drop mechanism, where you can simply drag a field and put it in one of the four areas. As soon as you do this, it will appear in the Pivot Table in the worksheet.

![Creating a Pivot Table in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20468'%3E%3C/svg%3E)

Now let’s try and answer the questions your manager had using this Pivot Table.

**Q1: What were the total sales in the South region?**

Drag the Region field in the Rows area and the Revenue field in the Values area. It would automatically update the Pivot Table in the worksheet.

Note that as soon as you drop the Revenue field in the Values area, it becomes Sum of Revenue. By default, Excel sums all the values for a given region and shows the total. If you want, you can change this to Count, Average, or other statistics metrics. In this case, the sum is what we needed.

The answer to this question would be 21225800.

![Creating a Pivot Table in Excel - Q1a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20279%20166'%3E%3C/svg%3E)

**Q2 What are the top five retailers by sales?**

Drag the Customer field in the Row area and Revenue field in the values area. In case, there are any other fields in the area section and you want to remove it, simply select it and drag it out of it.

You’ll get a Pivot Table as shown below:

![Creating a Pivot Table in Excel - Q2a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20284%20319'%3E%3C/svg%3E)

Note that by default, the items (in this case the customers) are sorted in an alphabetical order.

To get the top five retailers, you can simply [sort this list](https://trumpexcel.com/sort-pivot-table-excel/)
 and use the top five customer names. To do this:

*   Right-click on any cell in the Values area.![Creating a Pivot Table in Excel - Q2b](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20313'%3E%3C/svg%3E)
*   Go to Sort –> Sort Largest to Smallest.![Creating a Pivot Table in Excel - Q2c](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20271'%3E%3C/svg%3E)

This will give you a sorted list based on total sales.

![Creating a Pivot Table in Excel - Q2d](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20284%20323'%3E%3C/svg%3E)

**Q3: How did The Home Depot’s performance compare against other retailers in the South?**

You can do a lot of analysis for this question, but here let’s just try and compare the sales.

Drag the Region Field in the Rows area. Now drag the Customer field in the Rows area below the Region field. When you do this, Excel would understand that you want to categorize your data first by region and then by customers within the regions. You’ll have something as shown below:

![Creating a Pivot Table in Excel - Q3a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20194%20417'%3E%3C/svg%3E)

Now drag the Revenue field in the Values area and you’ll have the sales for each customer (as well as the overall region).

![Creating a Pivot Table in Excel - Q3b](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20439'%3E%3C/svg%3E)

You can sort the retailers based on the sales figures by following the below steps:

*   Right-click on a cell that has the sales value for any retailer.
*   Go to Sort –> Sort Largest to Smallest.

This would instantly sort all the retailers by the sales value.

Now you can quickly scan through the South region and identify that The Home Depot sales were 3004600 and it did better than four retailers in the South region.

![Creating a Pivot Table in Excel - Q3c](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20315%20444'%3E%3C/svg%3E)

Now there are more than one ways to skin the cat. You can also put the Region in the Filter area and then only select the South Region.

**[Click here](https://trumpexcel.com/wp-content/uploads/2016/04/Pivot-Table-Data.xlsx)** to download the sample data.

I hope this tutorial gives you a basic overview of Excel Pivot Tables and helps you in getting started with it.

**Here are some more Pivot Table Tutorials you may like:**

*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    .
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    .
*   [How to Group Dates in Pivot Tables in Excel.](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    .
*   [How to Filter Data in a Pivot Table in Excel.](https://trumpexcel.com/filter-data-pivot-table-excel/)
    
*   [Using Slicers in Excel Pivot Table.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables.](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Fields](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    
*   [Change Pivot Table to Tabular Form](https://trumpexcel.com/pivot-table-tabular-form/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Make a Pivot Table in Excel (Easy Step-by-Step)”
----------------------------------------------------------------------

1.  I am not getting the excel tips free ebook
    
    [Reply](https://trumpexcel.com/creating-excel-pivot-table/#comment-18984)
    
2.  Hi,
    
    Just wanna say, thank you for sharing this it will help us, especially me as a beginner in this field.
    
    [Reply](https://trumpexcel.com/creating-excel-pivot-table/#comment-16344)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/creating-excel-pivot-table/#respond)

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