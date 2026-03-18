# How to Add and Use an Excel Pivot Table Calculated Field

**Source:** https://trumpexcel.com/excel-pivot-table-calculated-field

---

[Skip to content](https://trumpexcel.com/excel-pivot-table-calculated-field/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-pivot-table-calculated-field/#below-title)

Often, once you [create a Pivot table](https://trumpexcel.com/creating-excel-pivot-table/)
, there is a need you to expand your analysis and include more data/calculations as a part of it.

If you need a new data point that can be obtained by using existing data points in the Pivot Table, you don’t need to go back and add it in the source data. Instead, you can use a **Pivot Table Calculated Field** to do this.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-pivot-table-calculated-field/#)

**[Download the dataset and follow along](https://trumpexcel.com/wp-content/uploads/2017/01/Pivot-Table-Calculated-Field-Data.xlsx)
.**

What is a Pivot Table Calculated Field?
---------------------------------------

Let’s start with a basic example of a Pivot Table.

Suppose you have a dataset of retailers and you create a Pivot Table as shown below:

![Excel Pivot Table Calculated Field - Data](https://trumpexcel.com/wp-content/uploads/2017/01/Pivot-Table-Calculated-Field-Data.png)

The above Pivot Table summarizes the sales and profit values for the retailers.

Now, what if you also want to know what was the profit margin of these retailers (where the profit margin is ‘Profit’ divided by ‘Sales’).

There are a couple of ways to do this:

1.  Go back to the original data set and add this new data point. So you can insert a new column in the source data and calculate the profit margin in it. Once you do this, you need to update the source data of the Pivot Table to get this new column as a part of it.
    *   While this method is a possibility, you would need to manually go back to the data set and make the calculations. For example, you may need to add another column to calculate the average sale per unit (Sales/Quantity). Again you will have to add this column to your source data and then [update the pivot table](https://trumpexcel.com/refresh-pivot-table-excel/)
        .
    *   This method also bloats your Pivot Table as you’re adding new data to it.
2.  Add calculations outside the Pivot Table. This can be an option if your Pivot Table structure is unlikely to change. But if you change the Pivot table, the calculation may not update accordingly and might give you the wrong results or errors. As shown below, I calculated the Profit Margin when there were retailers in the row. But when I changed it from customers to regions, the formula gave an error.![Pivot Table Calculated Field - Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20301'%3E%3C/svg%3E)
3.  Using a Pivot Table Calculated Field. This is the **most efficient way** to use existing Pivot Table data and calculate the desired metric. Consider Calculated Field as a virtual column that you have added using the existing columns from the Pivot Table. There are a lot of benefits of using a Pivot Table Calculated Field (as we will see in a minute):
    *   It doesn’t require you to handle formulas or update source data.
    *   It’s scalable as it will automatically account for any new data that you may add to your Pivot Table. Once you add a Calculate Field, you can use it like any other field in your Pivot Table.
    *   It easy to update and manage. For example, if the metrics change or you need to change the calculation, you can easily do that from the Pivot Table itself.

Adding a Calculated Field to the Pivot Table
--------------------------------------------

Let’s see how to add a Pivot Table Calculated Field in an existing Pivot Table.

Suppose you have a Pivot Table as shown below and you want to calculate the profit margin for each retailer:

![Pivot Table Calculated Field - Data](https://trumpexcel.com/wp-content/uploads/2017/01/Pivot-Table-Calculated-Field-Data.png)

Here are the steps to add a Pivot Table Calculated Field:

*   Select any cell in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Calculations –> Fields, Items, & Sets.![Pivot Table Calculated Field - Analyze Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20149'%3E%3C/svg%3E)
*   From the drop-down, select Calculated Field.![Pivot Table Calculated Field - Calculated Field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20252'%3E%3C/svg%3E)
*   In the Insert Calculated Filed dialog box:
    *   Give it a name by entering it in the Name field.
    *   In the Formula field, create the formula you want for the calculated field. Note that you can choose from the field names listed below it. In this case, the formula is ‘= Profit/ Sales’. You can either manually enter the field names or double click on the field name listed in the Fields box.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20302'%3E%3C/svg%3E)
*   Click on Add and close the dialog box.

As soon as you add the Calculated Field, it will appear as one of the fields in PivotTable Fields list.

![Pivot Table Calculated Field - Field List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20290'%3E%3C/svg%3E)

Now you can use this calculated field as any other Pivot Table field (note that you can not use Pivot Table Calculated Field as a report filter or slicer).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20319'%3E%3C/svg%3E)

As I mentioned before, the benefit of using a Pivot Table Calculated Field is that you can change the structure of the Pivot Table and it will automatically adjust.

For example, if I drag and drop region in the rows area, you will get the result as shown below, where Profit Margin value is reported for retailers as well as the region.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20386'%3E%3C/svg%3E) In the above example, I have used a simple formula (=Profit/Sales) to insert a calculated field. However, you can also use some [advanced formulas](https://trumpexcel.com/excel-functions/)
.

Before I show you an example of using an advanced formula to create a Pivot Table Calculate Field, here are some things you must know:

*   You CAN NOT use references or [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
     while creating a Pivot Table Calculated Field. That would rule out a lot of formulas such as [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
    , [INDEX](https://trumpexcel.com/excel-index-function/)
    , [OFFSET](https://trumpexcel.com/excel-offset-function/)
    , and so on. However, you can use formulas that can work without references (such SUM, IF, COUNT, and so on..).
*   You can use a constant in the formula. For example, if you want to know the forecasted sales where it is forecasted to grow by 10%, you can use the formula =Sales\*1.1 (where 1.1 is constant).
*   The order of precedence is followed in the formula that makes the calculated field. As a best practice, use parenthesis to make sure you don’t have to remember the order of precedence.

Now, let’s see an example of using an advanced formula to create a Calculated Field.

Suppose you have the dataset as shown below and you need to show the forecasted sales value in the Pivot Table.

For forecasted value, you need to use a 5% sales increase for large retailers (sales above 3 million) and a 10% sales increase for small and medium retailers (sales below 3 million).

_Note: The sales numbers here are fake and have been used to illustrate the examples in this tutorial._

Here is how to do this:

*    Select any cell in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Calculations –> Fields, Items, & Sets.![Pivot Table Calculated Field - Analyze Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20149'%3E%3C/svg%3E)
*   From the drop-down, select Calculated Field.![Pivot Table Calculated Field - Calculated Field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20252'%3E%3C/svg%3E)
*   In the Insert Calculated Filed dialog box:
    *   Give it a name by entering it in the Name field.
    *   In the Formula field, use the following formula: =IF(Region =”South”,Sales \*1.05,Sales \*1.1)![Pivot Table Calculated Field - advanced formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20302'%3E%3C/svg%3E)
*   Click on Add and close the dialog box.

This adds a new column to the pivot table with the sales forecast value.

![Pivot Table Calculated Field - advanced formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20380'%3E%3C/svg%3E)

**[Click here to Download the dataset](https://trumpexcel.com/wp-content/uploads/2017/01/Pivot-Table-Calculated-Field-Data.xlsx)
.**

An Issue With Pivot Table Calculated Fields
-------------------------------------------

Calculated Field is an amazing feature that really enhances the value of your Pivot Table with field calculations, while still keep everything scalable and manageable.

There is, however, an issue with Pivot Table Calculated Fields that you must know before using it.

Suppose, I have a Pivot Table as shown below where I used the calculated field to get the forecast sales numbers.

![Pivot Table Calculated Field - advanced formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20380'%3E%3C/svg%3E)

Note that the subtotal and grand totals are not correct.

While these should add the individual sales forecast value for each retailer, in reality, it follows the same calculated field formula that we created.

So for South Total, while the value should be 22,824,000, the South Total wrongly reports it as 22,287,000. This happens as it uses the formula 21,225,800\*1.05 to get the value.

![Pivot Table Calculated Field - Wrong Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20805%20384'%3E%3C/svg%3E)

Unfortunately, there is no way you can correct this.

The best way to handle this would be to remove subtotals and Grand Totals from your Pivot Table.

You can also go through [some innovative workarounds](http://www.contextures.com/excel-pivot-table-calculated-field.html#totals)
 Debra has shown to handle this issue.

How to Modify or Delete a Pivot Table Calculated Field?
-------------------------------------------------------

Once you have created a Pivot Table Calculated Field, you can modify the formula or delete it using the following steps:

*   Select any cell in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Calculations –> Fields, Items, & Sets.
*   From the drop-down select Calculated Field.
*   In the Name field, click on the drop-down arrow (small downward arrow at the end of the field).![Pivot Table Calculated Field - drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20302'%3E%3C/svg%3E)
*   From the list, select the calculated field you want to delete or modify.![Pivot Table Calculated Field - select CF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20302'%3E%3C/svg%3E)
*   Change the formula in case you want to modify it or click on Delete in case you want to delete it.![Pivot Table Calculated Field - modify delete CF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20302'%3E%3C/svg%3E)

How to Get a List of All the Calculated Field Formulas?
-------------------------------------------------------

If you create a lot of Pivot Table Calculated field, don’t worry about keeping track of the formula used in each one of it.

Excel allows you to quickly create a list of all the formulas used in creating Calculated Fields.

Here are the steps to quickly get the list of All Calculated Fields formulas:

*   Select any cell in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Fields, Items, & Sets –> List Formulas.![Pivot Table Calculated Field - List Formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20253'%3E%3C/svg%3E)

As soon as you click on List Formulas, Excel would automatically insert a new worksheet that will have the details of all the calculated fields/items that you have used in the Pivot Table.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20834%20254'%3E%3C/svg%3E)

This can be a really useful tool if you have to send your work to the client or share it with your team.

**You May Also Find the following Pivot Table Tutorials Useful:**

*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    .
*   [Using Slicers in Excel Pivot Table: A Beginner’s Guide](https://trumpexcel.com/slicers-excel-pivot-table/)
    .
*   [How to Group Dates in Pivot Tables in Excel](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    .
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    .
*   [How to Filter Data in a Pivot Table in Excel.](https://trumpexcel.com/filter-data-pivot-table-excel/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    .
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    .
*   [Pivot Cache in Excel – What Is It and How to Best Use It](https://trumpexcel.com/pivot-cache-excel/)
    ?
*   [How to Delete a Pivot Table in Excel](https://trumpexcel.com/delete-pivot-table/)
    
*   [How to Show Pivot Table Fields List? (Get Pivot Table Menu Back)](https://trumpexcel.com/show-pivot-table-fields/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “How to Add and Use an Excel Pivot Table Calculated Field”
------------------------------------------------------------------------

1.  How can I use already aggregated data in let say column A and B in calculated field (column C)  
    Example:  
    Column A Column B Column C  
    SumSales CountSales Calc.field1(Average amount of sale A/B)  
    row 1 120.000 (sum) 15 (count) ?????  
    row 2 160.000 (sum) 10 (count) ?????
    
    I want to receive product of A and B in Column C
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-14230)
    
2.  I’m trying to create a calculated field with an “If” statement but it’s not behaving as I’d expect. I have a pivot table with “Employee Type” that can be “Contractor” or “Permanent” and then various cost rates per employee. I need to do one calculation for Contractor and a different one for Employees. I’m using the following:
    
    \=IF(‘Employee Type'”Contractor”,(WeeklyCappedHours/hours)\*’$ Cost’, hours)
    
    However no matter what I do the formula doesn’t calculate differently for Permanent people v. Contractors.
    
    What am I doing wrong?
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-12489)
    
3.  I’m hoping someone can help with a calculated field of a Pivot table: I want to take say, column B in the Pivot Table and divide it by the TOTAL of column A. Can anyone help?
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-11284)
    
4.  I have a pivot table that has sales by year for 8 years. I only want to show the difference between sales for the last two years (2018 vs 2017). I know how to use Show Values As > Difference From – but that gives me the difference for all year pairs. Is there a way to have it for only the last two years of the table?
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-10267)
    
5.  I have a pivot table that has sales by year for 8 years. I only want to show the difference between sales for the last two years (2018 vs 2017). I know how to use Show Values As > Difference From – but that gives me the difference for all year pairs. Is there a way to have it for only the last two years of the table?
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-10268)
    
6.  formula in 1st example should be profit/sales & not other way.
    
    [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-8686)
    
    *   Thanks mate.. have corrected the image
        
        [Reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#comment-8689)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-pivot-table-calculated-field/#respond)

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