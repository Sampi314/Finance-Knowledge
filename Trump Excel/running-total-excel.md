# 5 Easy Ways to Calculate Running Total in Excel (Cumulative Sum)

**Source:** https://trumpexcel.com/running-total-excel

---

[Skip to content](https://trumpexcel.com/running-total-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/running-total-excel/#below-title)

Running total (also called **cumulative sum**) is quite commonly used in many situations. It’s a metric that tells you what’s the sum of the values so far.

For example, if you have the monthly sales data, then a running total would tell you how much sales have been done till a specific day from the [first day of the month](https://trumpexcel.com/first-day-of-month-excel/)
.

There are also some other situations where running total is often used, such as calculating your cash balance in your bank statements/ledger, counting calories in your meal plan, etc.

In Microsoft Excel, there are multiple different ways to calculate running totals.

The method you choose would also depend on how your data is structured.

For example, if you have simple tabular data then you can use a simple SUM formula, but if you have an Excel table, then it’s best to use structured references. You can also use Power Query to do this.

In this tutorial, I’m going to cover all these different methods to **calculate running totals in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/running-total-excel/#)

Calculating Running Total with Tabular Data
-------------------------------------------

If you have tabular data (i.e., a table in Excel which is not converted into an [Excel table](https://trumpexcel.com/excel-table/)
), you can use some simple formulas to calculate the running totals.

### Using the Addition Operator

Suppose you have date-wise sales data and you want to calculate the running total in column C.

![Datewise data for Running total](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20357'%3E%3C/svg%3E)

Below are the steps to do this.

**Step 1** – In cell C2, which is the first cell where you want the running total, enter

\=B2

This will simply get the same sale values in cell B2.

![Enter B2 in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20414'%3E%3C/svg%3E)

**Step 2** – In cell C3, enter the below formula:

\=C2+B3

![Enter another formula in cell C3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20416'%3E%3C/svg%3E)

**Step 3** – [Apply the formula to the entire column](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
. You can use the [Fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
 to select and drag it, or simply and copy-paste the cell C3 to all the remaining cells (which would automatically adjust the reference and give the right result).

This will give you the result as shown below.

![Apply the formula to the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20360'%3E%3C/svg%3E)

It’s a really simple method and works well in most cases.

The logic is simple – every cell picks up the value above it (which is the cumulative sum till the date before) and adds the value in the cell adjacent to it (which is the sale value for that day).

There is only one drawback – in case you [delete any of the existing rows](https://trumpexcel.com/vba-delete-row-excel/)
 in this data set, all the cells below that would return a [reference error (#REF!)](https://trumpexcel.com/ref-error-in-excel/)

![Ref Error when a row is deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20334'%3E%3C/svg%3E)

If that’s a possibility with your data set, use the next method that uses the [SUM formula](https://trumpexcel.com/excel-sum-function/)

Also read: [Weighted Average In Excel](https://trumpexcel.com/weighted-average-in-excel/)

### Using SUM with Partially Locked Cell Reference

Suppose you have date-wise sales data and you want to calculate the running total in column C.

![Datewise data for Running total](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20357'%3E%3C/svg%3E)

Below is the SUM formula that will give you the running total.

\=SUM($B$2:B2)

![SUM formula to calculate running total](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20411'%3E%3C/svg%3E)

Let me explain how this formula works.

In the above SUM formula, I have used the reference to add as $B$2:B2

*   $B$2 – this is an absolute reference, which means that when I copy the same formula in the cells below, this reference is not going to change. So when copying the formula in the cell below, the formula would change to SUM($B$2:B3)
*   B2 – this is the second part of the reference which is a relative reference, which means that this would adjust as I copy the formula down or to the right. So when copying the formula in the cell below, this value will become B3

Also read: [Absolute, Relative, and Mixed Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)

The great thing about this method is that in case you [delete any of the rows](https://trumpexcel.com/delete-rows/)
 in the data set, this formula would adjust and still give you the right running totals.

Calculating Running Total in Excel Table
----------------------------------------

When working with tabular data in Excel it’s a good idea to convert it into an Excel table. It makes it a lot easier to manage the data and also allows makes it easy to use tools such as Power Query and Power Pivot.

Working the Excel tables comes with benefits such as structured references (which makes it really easy to refer to the data in the table and use it in formulas), and automatic adjustment of references in case you add or delete data from the table.

While you can still use the above formula that I have shown you in an Excel table, let me show you some better methods to do this.

Suppose you have an Excel table as shown below and you want to calculate the running total in column C.

![Calculate running total in Excel Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20407'%3E%3C/svg%3E)

Below is the formula that will do this:

\=SUM(SalesData\[\[#Headers\],\[Sale\]\]:\[@Sale\])

![Excel table formula to calculate running total](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20458'%3E%3C/svg%3E)

The above formula may look a bit long, but you don’t have to write it yourself. what you see within the sum formula are called structured references, which is Excel’s efficient way to refer to specific data points in an Excel table.

For example, SalesData\[\[#Headers\],\[Sale\]\] refers to the Sale header in the SalesData table (SalesData is the name of the Excel table that I gave when I created the table)

And \[@Sale\] refers to the value in the cell in the same row in the Sale column.

I just explained this here for your understanding, but even if you know nothing about structured references, you can still easily create this formula.

Below are the steps to do this:

1.  In cell C2, enter =SUM(
2.  Select cell B1, which is the header of the column that has the sale value. You can use the mouse or use the arrow keys. You will notice that Excel automatically enters the structured reference for that cell
3.  Add a : (colon symbol)
4.  Select cell B2. Excel would again automatically insert the structured reference for the cell
5.  Close the bracket and hit enter

You will also notice that you don’t have to copy the formula in the entire column, an Excel table automatically does it for you.

Another great thing about this method is that in case you add a new record in this data set, the Excel table would automatically calculate the running total for all the new records.

While we have included the header of the column in our formula, remember that the formula would ignore the header text and only consider the data in the column

Also read: [How to Calculate Percentile in Excel](https://trumpexcel.com/percentile-excel/)

Calculating Running Total Using Power Query
-------------------------------------------

Power Query is an amazing tool when it comes to connecting with databases, extracting the data from multiple sources, and transforming it before putting it into Excel.

If you are already working with Power Query, it would be more efficient to add running totals while you are transforming the data within the Power Query editor itself (instead of 1st getting the data in Excel and then adding the running totals using any of the above methods covered above).

While there is no inbuilt feature in Power Query to add running totals (which I wish there was), you can still do that using a simple formula.

Suppose you have an Excel table as shown below and you want to add the running totals to this data:

![Dataset for running total using Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20251%20358'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select any cell in the Excel table
2.  Click on Data![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20201'%3E%3C/svg%3E)
3.  In the Get & Transform tab, click on the from Table/Range icon. This will open the table in the Power Query editor![Click on From Table Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20201'%3E%3C/svg%3E)
4.  \[Optional\] In case your Date column is not already sorted, click on the filter icon in the Date column, and then click on Sort ascending![Sort date in ascending order if not already](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20431'%3E%3C/svg%3E)
5.  Click the Add Column tab in the Power Query editor![Click on Add Column tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20140'%3E%3C/svg%3E)
6.  In the General group, click on the Index Column dropdown (do not click on the Index Column icon, but on the small black tilted arrow right next to it to show more options)
7.  Click on the ‘From 1’ option. Doing this will add a new index column that would start from one and enter numbers incrementing by 1 in the entire column![Click on From 1 in the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20276'%3E%3C/svg%3E)
8.  Click on the ‘Custom Column’ icon (which is also in the Add Column tab)![Click on Custom Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20140'%3E%3C/svg%3E)
9.  In the custom column dialog box that opens up, enter a name for the new column. in this example, I will use the name ‘Running Total’![Enter new name for the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20470'%3E%3C/svg%3E)
10.  In the Custom column formula field, enter the below formula: **List.Sum(List.Range(#”Added Index”\[Sale\],0,\[Index\]))![Enter the formula in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20489'%3E%3C/svg%3E)**
11.  Make sure there’s a checkbox at the bottom of the dialog box that says – ‘No syntax errors have been detected’![No syntax errors have been detected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20470'%3E%3C/svg%3E)
12.  Click OK. This would add a new running total column
13.  Remove the Index Column![Delete the INDEX column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20360'%3E%3C/svg%3E)
14.  Click on the File tab and then click on ‘Close and Load’![Click on Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20536%20415'%3E%3C/svg%3E)

The above steps would insert a new sheet in your workbook with a table that has the running totals.

![Running total result from Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20357'%3E%3C/svg%3E)

Now if you’re thinking that these are just too many steps as compared to the previous methods of using simple formulas, you’re right.

If you already have a data set and all you need to do is add running totals, it’s better not to use Power Query.

Using Power Query makes sense where you have to extract data from a database or [combine data from multiple different workbooks](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
 and in the process also add running totals to it.

Also, once you do this automation using Power Query, the next time your data set changes you do not have to do it again you can simply refresh the query and it would give you the result based on the new data set.

**How does this work?**

Now let me quickly explain what happens in this method.

The first thing we do in the Power Query editor is to insert an index column starting from one and incrementing by one as it goes down the cells.

We do this because we need to use this column while we calculate the running total in another column that we insert in the next step.

Then we insert a custom column and use the below formula

List.Sum(List.Range(#"Added Index"\[Sale\],0,\[Index\]))

This is a List.Sum formula that would give you the sum of the range that is specified within it.

And that range is specified using the List.Range function.

The List.Range function gives the specified range in the sale column as the output and this range changes based on the Index value. For example, for the first record, the range would simply be the first sale value. And as you go down the cells, this range would expand.

So, for the first cell. List.Sum would only give you the sum of the first sale value, and for the second cell, it would give you the sum for the first two sale values and so on.

While this method works well, gets [really slow](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
 with large datasets – thousands of rows. If you’re dealing with a large data set and want to add running totals to it, [have a look at this tutorial](https://www.myonlinetraininghub.com/quickly-create-running-totals-in-power-query)
 that shows other methods that are faster.

Also read: [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)

Calculating Running Total Based on Criteria
-------------------------------------------

So far, we have seen examples where we have calculated the running total for all the values in a column.

But there could be cases where you want to calculate the running total for specific records.

For example, below I have a data set and I want to calculate the running total for Printers and Scanners separately in two different columns.

![Dataset for running total based on conditions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20358'%3E%3C/svg%3E)

This can be done using a [SUMIF formula](https://trumpexcel.com/excel-sumif-function/)
 that calculates the running total while making sure the specified condition is met.

Below is the formula that will do this for the Printer columns:

\=SUMIF($C$2:C2,$D$1,$B$2:B2)

![Running totals for Printer only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20413'%3E%3C/svg%3E)

Similarly, to calculate the running total for Scanners, use the below formula:

\=SUMIF($C$2:C2,$E$1,$B$2:B2)

![Running total for scanner only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20412'%3E%3C/svg%3E)

In the above formulas, I have used SUMIF, which would give me the sum in a range when the specified criteria are met.

The formula takes three arguments:

1.  **range**: this is the criteria range that would be checked against the specified criteria
2.  **criteria**: this is the criteria that would be checked in only if this criterion is met then the values in the third argument, which is the sum range, would be added
3.  **\[sum\_range\]**: this is the sum range from which the values would be added if the criteria are met

Also, in the **range** and **sum\_range** argument, I have locked the second part of the reference, so that as we go down the cells, the range would keep expanding. This allows us to only consider and add values till that range (hence running totals).

In this formula, I have used the header column (Printer and Scanner) as the criteria. you can also hardcode the criteria if your column headers are not exactly the same as the criteria text.

In case you have multiple conditions that you need to check, then you can use the [SUMIFS formula](https://trumpexcel.com/excel-sumifs-function/)
.

Running Total in Pivot Tables
-----------------------------

If you want to add running totals in a [Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
 result, you can easily do that using an inbuilt functionality in Pivot tables.

Suppose you have a Pivot Table as shown below where I have the date in one column and the sale value in the other column.

![Pivot table where to create running total](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20245%20429'%3E%3C/svg%3E)

Below are the steps to add an additional column that will show the running total of the sales by date:

1.  Drag the Sale field and put it in the Value area.![Drag sale to value area again](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20631'%3E%3C/svg%3E)
2.  This will add another column with the Sales values![Click on Sum of Sale 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20631'%3E%3C/svg%3E)
3.  Click on the Sum of Sale2 option in the Value area
4.  Click on the ‘Value Field Settings’ option![Click on Value field settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20659%20419'%3E%3C/svg%3E)
5.  In the Value Field Settings dialog box, change the Custom Name to ‘Running Totals’![Add custom name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20413'%3E%3C/svg%3E)
6.  Click on the ‘Show Value As’ tab![Select show values as tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20413'%3E%3C/svg%3E)
7.  In the Show value as drop-down, select the ‘Running Total in’ option![Click on Running Total in from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20413'%3E%3C/svg%3E)
8.  In the Base field options, make sure Date is selected![Make sure Date is selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20413'%3E%3C/svg%3E)
9.  Click Ok

The above steps would change the second sale column into the Running Total column.

![Running Total added in Pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20432'%3E%3C/svg%3E)

So these are some of the ways you can use to calculate the running total in Excel. If you have data in tabular format, you can use simple formulas, and if you have an Excel table, then you can use formulas that make use of structured references.

I’ve also covered how to calculate running total using Power Query and in Pivot Tables.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [Excel Quick Analysis Tool – How to Best Use it? 10 Examples!](https://trumpexcel.com/excel-quick-analysis-tool/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/running-total-excel/#respond)

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