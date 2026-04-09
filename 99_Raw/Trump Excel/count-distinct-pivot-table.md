# Count Distinct Values in Excel Pivot Table (Easy Step-by-Step Guide)

**Source:** https://trumpexcel.com/count-distinct-pivot-table

---

[Skip to content](https://trumpexcel.com/count-distinct-pivot-table/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-distinct-pivot-table/#below-title)

[Excel Pivot Tables](https://trumpexcel.com/pivot-table/)
 are amazing (I know I mention this every time I write about Pivot Tables, but it’s true).

With a basic understanding and a little drag and drop, you can get a bucket-load of work done in a few seconds.

While a lot can be done with a few clicks in Pivot Tables, there are some things that would need a few extra steps or a little bit of work around.

And one such thing is to count distinct values in a Pivot Table.

In this tutorial, I will show you how to count distinct values as well as Unique Values in an Excel Pivot table.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-distinct-pivot-table/#)

But before I jump into how to count distinct values, it’s important to understand the difference between ‘distinct count’ and ‘unique count’

Distinct Count Vs Unique Count
------------------------------

While these may seem like the same thing, _it’s not_.

Below is an example where there is a dataset of names and I have listed unique and distinct names separately.

![Difference between unique count and distinct count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20367'%3E%3C/svg%3E)

**Unique values/names** are those that only occur once. This means that all the names that repeat and have duplicates are not unique. Unique names are listed in column C in the above dataset

**Distinct values/names** are those that occur at least once in the dataset. So if a name appears three times, it’s still counted as one distinct name. This can be achieved by removing the duplicate values/names and keeping all the distinct ones. Distinct names are listed in column B in the above data set.

Based on what I have seen, most of the times when people say that they want to get the unique count in a Pivot Table, they actually mean distinct count, which is what I am covering in this tutorial.

Count Distinct Values in Excel Pivot Table
------------------------------------------

Suppose you have the sales data as shown below:

![Pivot Table Data from which distinct values need to be counted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20484'%3E%3C/svg%3E)

[**Click here to download the example file and follow along**](https://www.dropbox.com/s/yawpobibblzhm5g/Pivot%20Table%20Distinct%20Count%20Data.xlsx?dl=1)

With the above dataset, let’s say that you want to find the answer to the following questions:

1.  How many sales rep are there in each region (which is nothing but the distinct count of sales reps in each region)?
2.  How many sales rep sold the printer in 2020?

While Pivot Tables can instantly summarize the data with a few clicks, to get the count of distinct values, you will need to take a few more steps.

If you’re using **Excel 2013 or versions after that**, there is an inbuilt functionality in Pivot Table that quickly gives you the distinct count. And if you’re using **Excel 2010 or versions before that**, you will have to modify the source data by adding a helper column.

The following two methods are covered in this tutorial:

*   Adding a helper column in the original data set to count [unique values](https://trumpexcel.com/unique-items-from-a-list-in-excel/)
     (works in all versions).
*   Adding the data to a data model and using Distinct Count option (available in Excel 2013 and versions after that).

There is a third method which Roger shows [in this article](https://www.contextures.com/pivottablecountunique.html)
 (which he calls the Pivot the Pivot Table method).

Let’s get started!

### Adding a Helper Column in the Dataset

Note: If you’re using Excel 2013 and higher versions, skip this method and move to the next one (as it uses an inbuilt Pivot Table functionality – _Distinct Count_).

This is an easy way to count distinct values in the Pivot Table as you only need to add a helper column to the source data. Once you have added a helper column, you can then use this new data set to calculate the distinct count.

While this is an easy workaround, there are some drawbacks to this method (covered later in this tutorial).

Let me first show you how to add a helper column and get a distinct count.

Suppose I have the data set as shown below:

![Pivot Table Data from which distinct values need to be counted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20484'%3E%3C/svg%3E)

Add the following formula in Column F and apply it for all the cells that have data in the adjacent columns.

\=IF(COUNTIFS($C$2:C2,C2,$B$2:B2,B2)>1,0,1)

The above formula uses the [COUNTIFS function](https://trumpexcel.com/excel-countifs-function/)
 to count the number of times a name appears in the given region. Also, note that the criteria range is $C$2:C2 and $B$2:B2. This means that it keeps expanding as you go down the column.

For example, in cell E2, the criteria ranges are $C$2:C2 and $B$2:B2 and in cell E3 these ranges expand to $C$2:C3 and $B$2:B3.

This ensures that the COUNTIFS function counts the first instance of a name as 1, the second instance of the name as 2, and so on.

Since we only want to get the distinct names, the [IF function](https://trumpexcel.com/excel-if-function/)
 is used which returns 1 when a name appears for a region the first time and returns 0 when it appears again. This makes sure that only distinct names are counted and not the repeats.

Below is how your dataset would look like when you have added the helper column.

![Distinct Count Helper Column in Pivot Table Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20770%20402'%3E%3C/svg%3E)

Now that we have modified the source data, we can use this to create a Pivot Table and use the helper column to get the distinct count of the sales rep in each region.

Below are the steps to do this:

1.  Select any cell in the dataset.
2.  Click the Insert Tab.![Click the Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20192'%3E%3C/svg%3E)
3.  Click on Pivot Table (or use the keyboard shortcut – ALT + N + V)![Click on Pivot Table option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20192'%3E%3C/svg%3E)
4.  In the Create Pivot Table dialog box, make sure that the Table/Range is correct (and includes the helper column) and’New Worksheet’ in selected.![Create Pivot Table Dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20366'%3E%3C/svg%3E)
5.  Click OK.

The above steps would insert a new sheet which has the Pivot Table.

Drag the ‘Region’ field in the Rows area and ‘D Count’ field in the Values area.

![Pivot table Areas to get distinct count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20297'%3E%3C/svg%3E)

You will get a Pivot Table as shown below:

![Pivot Table with sum of distinct count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20198'%3E%3C/svg%3E)

Now you can change the column header from ‘Sum of D count’ to ‘Sales Rep’.

#### **Drawbacks of Using a Helper Column:**

While this method is pretty straight forward, I must highlight a few drawbacks that come with modifying the source data in a Pivot Table:

*   The data source with the helper column is not as dynamic as a Pivot Table. While you can slice and dice the data any way you want with a Pivot Table, when you use a helper column, you lose a part of that ability. Let’s say that you add a helper column to get the count of a distinct sales rep in each region. Now, what if you also want to get the distinct count of sales rep selling printers. You will have to go back to the source data and modify the helper column formula (or add a new helper column).
*   Since you’re adding more data to the Pivot Table source (which also gets added to the [Pivot Cache](https://trumpexcel.com/pivot-cache-excel/)
    ), this can lead to a higher size of Excel file.
*   Since we are using an [Excel formula](https://trumpexcel.com/excel-functions/)
    , it may make your [Excel Workbook slow](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
     in case you have thousands of rows of data.

### Add Data to Data Model and Summarize Using Distinct Count

Pivot Table added new functionality in Excel 2013 that allows you to get the distinct count while summarizing the data set.

In case you’re using a previous version, you’ll not be able to use this method (as should try adding the helper column as shown in the method above this one).

Suppose you have a dataset as shown below and you want to get the count of the unique sales rep in each region.

![Excel Pivot Table Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20484'%3E%3C/svg%3E)

Below are the steps to get a distinct count value in the Pivot Table:

1.  Select any cell in the dataset.
2.  Click the Insert Tab.![Click the Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20192'%3E%3C/svg%3E)
3.  Click on Pivot Table (or use the keyboard shortcut – ALT + N + V)![Click on Pivot Table option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20192'%3E%3C/svg%3E)
4.  In the Create Pivot Table dialog box, make sure that the Table/Range is correct and New Worksheet in Selected.
5.  Check the box which says – “Add this data to the Data Model”![Create PivotTable Dialog Box - Check Add Data to Data Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20366'%3E%3C/svg%3E)
6.  Click OK.

The above steps would insert a new sheet which has the new Pivot Table.

Drag the Region in the Rows area and Sales Rep in the Values area. You will get a Pivot Table as shown below:

![Pivot Table created with data model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20197'%3E%3C/svg%3E)

The above Pivot Table gives the total count of the Sales rep in each region (and not the distinct count).

To get the distinct count in the Pivot Table, follow the below steps:

1.  Right-click on any cell in the ‘Count of Sales Rep’ column.
2.  Click on Value Field Settings![Click on Value Field Settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20577'%3E%3C/svg%3E)
3.  In the Value Field Settings dialog box, select ‘Distinct Count’ as the type of calculation (you may have to scroll down the list to find it).![Click on Distinct Count in Value Field Setting Dialog Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20413'%3E%3C/svg%3E)
4.  Click OK.

You will notice that the name of the column changes from ‘Count of Sales Rep’ to ‘Distinct Count of Sales Rep’. You can change it to whatever you want.

![Distinct Count of Sales Rep](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20196'%3E%3C/svg%3E)

Some things you know when you add your data to the Data Model:

*   If you save your data in the data model and then open in an older version of Excel, it will show you a warning – ‘Some pivot table functions will not be saved’. You may not see the distinct count (and the data model) when opened in an older version that doesn’t support it.
*   When you add your data to a Data Model and [make a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
    , it will not show the options to add [calculated fields](https://trumpexcel.com/excel-pivot-table-calculated-field/)
     and calculated columns.

[**Click here to download the example file**](https://www.dropbox.com/s/yawpobibblzhm5g/Pivot%20Table%20Distinct%20Count%20Data.xlsx?dl=1)

What If You Want to Count Unique Values (and not distinct values)?
------------------------------------------------------------------

If you want to count unique values, you don’t have any inbuilt functionality in the Pivot Table and will have to rely on helper columns only.

Remember – Unique values and distinct values are not the same. [Click here](https://trumpexcel.com/count-distinct-pivot-table/#Distinct-Count-Vs-Unique-Count)
 to know the difference.

One example could be when you have the below data set and you want to find out how many sales rep are unique to each region. This means that they operate in one specific region only and not the others.

In such cases, you need to create one of more than one helper columns.

For this case, the below formula does the trick:

\=IF(IF(COUNTIFS($C$2:$C$1001,C2,$B$2:$B$1001,B2)/COUNTIF($C$2:$C$1001,C2)<1,0,1),IF(COUNTIF($C2:C$22,C2)>1,0,1),0)

The above formula checks whether a sales rep name occurs in one region only or in more than one region. It does that by counting the number of occurrence of a name in a region and dividing it by the total number of occurrences of the name. If the value is less than 1, it indicates that the name occurs in two or more than two regions.

In case the name occurs in more than one region, it returns a 0 else it returns a one.

The formula also checks whether the name is repeated in the same region or not. If the name is repeated, only the first instance of the name returns the value 1, and all other instances return 0.

This may seem a bit complex, but it again depends on what you’re trying to achieve.

So, if you want to count unique values in a Pivot Table, use helper columns and if you want to count distinct values, you can use the inbuilt functionality (in Excel 2013 and above) or can use a helper column.

[**Click here to download the example file**](https://www.dropbox.com/s/yawpobibblzhm5g/Pivot%20Table%20Distinct%20Count%20Data.xlsx?dl=1)

**You May Also Like the Following Pivot Table Tutorials:**

*   [How to Filter Data in a Pivot Table in Excel](https://trumpexcel.com/filter-data-pivot-table-excel/)
    
*   [How to Group Dates in Pivot Tables in Excel](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [Slicers in Excel Pivot Table](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Refresh Pivot Table in Excel](https://trumpexcel.com/refresh-pivot-table-excel/)
    
*   [Delete a Pivot Table in Excel](https://trumpexcel.com/delete-pivot-table/)
    
*   [Pivot Table Sorting](https://trumpexcel.com/sort-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “Count Distinct Values in Excel Pivot Table (Easy Step-by-Step Guide)”
-------------------------------------------------------------------------------------

1.  It works, thanks a lot
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-41580)
    
2.  THANK YOU!!! So much appreciated
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-14201)
    
3.  Thank you
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-13929)
    
4.  Distinct Count added column formula was just what I needed. Awesome! Thanks!
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-13603)
    
5.  there is no such “Distinct Count” option my friend
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-13586)
    
6.  Thank you, very helpful!
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-13500)
    
7.  Thank you! Best on the internet.
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-12617)
    
8.  If I have a list of peoples Names in Column A and each week I add a list of people to column B. Is there a formula which will tell me if any of the names in Column B appear in Column A? Hopefully this will give me a yes/no or 0/1 situation in Column C. Thanks
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-11732)
    
    *   Hello Andrew.. Have a look at this – [https://trumpexcel.com/compare-two-columns/](https://trumpexcel.com/compare-two-columns/)
        
        [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-11734)
        
9.  I have a set of data where in we have requested for a feedback on each dept. how do I go about pivoting the data such unique values are obtained against each dept. with respective questions?
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-11725)
    
    *   send your data to my email.
        
        [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-13142)
        
10.  Very good write. Excel is my passion and I have been working in it since 2014.
    
    Thanks for good sharing.
    
    [Reply](https://trumpexcel.com/count-distinct-pivot-table/#comment-11701)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-distinct-pivot-table/#respond)

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