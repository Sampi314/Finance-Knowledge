# How To Subtract In Excel (Subtract Cells, Column, Dates/Time)

**Source:** https://trumpexcel.com/subtract-in-excel

---

[Skip to content](https://trumpexcel.com/subtract-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/subtract-in-excel/#below-title)

While Excel is an amazing tool for data analysis, many people use it for basic arithmetic calculations such as addition, subtraction, multiplication, and division.

If you’re new to Excel and wondering how to subtract in Excel, you’re at the right place.

In this tutorial, I will show you how to subtract in Excel (subtract cells, ranges, columns, and more).

I will start with the basics and then would cover some advanced subtraction techniques in Excel. I also cover how to subtract dates, times, and percentages in Excel.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/subtract-in-excel/#)

Subtracting Cells/Values in Excel
---------------------------------

Let’s start with a really simple example, where I have two values (say 200 and 100) and I want to subtract these and get the result.

Here is how to do this:

1.  Select the cell where you want to subtract and enter an equal to sign (=)
2.  Enter the first value
3.  Enter the subtraction sign (minus sign -)
4.  Enter the second number
5.  Hit Enter

![Simple Subtraction with hardcoded values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20157'%3E%3C/svg%3E)

The above steps would perform the calculation in the cell and display the result.

Note that this is called a formula in Excel, where we start with an equal-to sign and then have the formula or the equation that we want to solve.

In the above example, we hard-coded the values in the cell. This means that we manually entered the values 200 and 100 in the cell.

You can also use a similar formula when you have these values in cells. In that case, instead of entering the values manually, you can use the reference of the cell.

Suppose you have two values in cell B1 and B2 (as shown below), and you want to subtract the value in cell B2 from the value in cell B1

![Values in cell B1 and B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20338%20208'%3E%3C/svg%3E)

Below is the formula that will do this:

\=B1-B2

![Simple Subtraction formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20263'%3E%3C/svg%3E)

It’s the same construct, but instead of manually entering the values in the formula, we have used the cell reference which holds the value.

The benefit of doing this is that in case the values in the cells change, the formula would automatically update and show you the correct result.

Subtracting a Value from an Entire Column
-----------------------------------------

Now let’s get to slightly more advanced subtraction calculations.

In the above example, we had two values that we wanted to subtract.

But what if you have a list of values in a column, and you want to subtract one specific value from that entire column.

Again, you can easily do that in Excel.

Suppose you have a data set as shown below and you want to subtract the value 10 from each cell in column A.

![Dataset with values in column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20402'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In cell B2, enter the formula: =A2-10

![Formula to subtract 10 from cell value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20456'%3E%3C/svg%3E)

2.  Copy cell B2
3.  Select cell B3 to B12
4.  Paste the copied cell

![Subtraction result for the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20403'%3E%3C/svg%3E)

When you do this, Excel will copy the formula in cell B2, and then apply that to all the cells where you pasted the copied cell.

And since we are using a cell reference in the formula (A2), Excel would automatically adjust the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 as it goes down.

For example, in cell B3, the formula would become =A3-10, and in cell B4, the formula would become A4-10.

### If Using Microsoft 365

The method that I’ve covered above will work with all the versions of Excel, but if you using Microsoft 365, then you can use an even easier formula.

Suppose you have the same data (with data in column A) and you want to subtract 10 from each cell, you can use the below formula in cell B2:

\=A2:A12-10

![Subtract using dynamic array formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20456'%3E%3C/svg%3E)

That’s it!

You don’t need to worry about copying and pasting the formula in other cells as Excel would take care of it.

This is called a dynamic array formula, where the result does not return one single value, but an array of values. And these are values are then spilled over to other cells in the column

Note: For these dynamic array formulas to work, you need to make sure the cells where the result would be populated are empty. In case there is already a number of text in these cells, you will see the #SPILL! error in the cell where you enter the formula.

Subtracting a Cell Value from an Entire Column
----------------------------------------------

In the above example, I subtracted 10 from multiple cells in a column.

We can use the same concept to subtract a value in a cell from an entire column.

Suppose you have a dataset as shown below where you want to subtract the value in cell D2 with all the cells in column A.

![Dataset to subtract one value from a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20454'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In cell C2, enter the formula: =A2-$D$2

![Formula to subtract a value from a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20503'%3E%3C/svg%3E)

2.  Copy cell C2
3.  Select cell C3 to C12
4.  Paste the copied cell

![Copy formula to entire column to subtract entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20508'%3E%3C/svg%3E)

In this example, I have used the formula A2-$D$2, which makes sure that when I copy the formula for all the other cells in column C, the value that I am subtracting remains the same, which is cell B2.

When you add a dollar before the column alphabet and the row number, it makes sure that in case you copy the cell with this reference and paste it somewhere else, the reference would still remain $D$2. This is called absolute reference (as these don’t change).

When you copy this formula in cell C3, it would become A3-$D$2, and in cell C4, it would become A4-$D$2.

So while the first part of the reference keeps changing from A3 to A4 as we copy it down, the absolute reference doesn’t change,

This allows us to subtract the same value from all the cells in column A.

### If Using Microsoft 365

If you’re using Microsoft 365 and have access to dynamic arrays, you can also use the below formula:

\=A2:A12-D2

![Dynamic array formula to subtract](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20505'%3E%3C/svg%3E)

With dynamic arrays, you don’t have to worry about references changing. It will take care of it itself.

Subtract Multiple Cells From One Cell
-------------------------------------

Similar to the above example, you can also delete values in an entire column from a single value or the cell that holds the value.

Suppose you have a data set as shown below and you want to subtract all the values in column B from the value in cell A2.

![Dataset to subtract column from one value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20506%20452'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In cell C2, enter the formula: =$A$2-B2
2.  Copy cell C2
3.  Select cell C3 to C12
4.  Paste the copied cell

![Subtraction using absolute reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20505'%3E%3C/svg%3E)

The logic used here is exactly the same as above, where I’ve locked the reference $A$2 by adding a $ sign before the column alphabet and row number.

This way, the cell reference $A$2 doesn’t change when we copy it in column C, but the second reference of the formula (B2), keeps changing when we go down the cell.

### If Using Microsoft 365

If you’re using Microsoft 365 and have access to dynamic arrays, you can also use the below formula:

\=A2-B2:B12

![Subtract using dynamic array formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20506'%3E%3C/svg%3E)

Subtracting Cells in Two Columns
--------------------------------

In most practical cases, you will have two columns where you want to subtract the cells in each column (in the same row) and get the result.

For example, suppose you have the Revenue and Expense values in two columns and you want to calculate the Net Income (which is the difference between revenue and expenses)

![Dataset to subtract two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20371'%3E%3C/svg%3E)

Here is how to do this:

1.  In cell C2, enter the formula: =B2-C2

![Subtract two cells formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20421'%3E%3C/svg%3E)

2.  Copy cell C2
3.  Select cell C3 to C12
4.  Paste the copied cell

![Copy subtraction formula to entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20561%20424'%3E%3C/svg%3E)

The above formula will automatically adjust the reference as it’s copied down and you will get the difference between Revenue and Expense in that row.

### If Using Microsoft 365

The method that I’ve covered above will work with all the versions of Excel, but if you using Microsoft 365, then you can use an even easier formula.

Suppose you have the same data and you want to subtract the two columns, you can use the below formula:

\=B2:B11-C2:C11

![Dynamic formula to subtract two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20561%20424'%3E%3C/svg%3E)

Note that this is made possible because Excel in Microsoft 365 has something called Dynamic Arrays. If you don’t have these, then it’s won’t be able to use this formula.

Subtract Dates in Excel
-----------------------

Dates and Time values are stores as numbers in the backend in Excel.

For example, 44197 represents the date 01 Jan 2021, and 44198 represents ṭhe date 2 Jan 2021.

This allows us to easily subtract dates in Excel and find the difference.

For example, if you have two dates, you can subtract these and find out how many days have elapsed between these two dates.

Suppose I have a dataset as shown below where I have the ‘Start Date’ and the ‘End Date’ and I want to find out the number of days between these two dates.

![Dataset to subtract dates in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20370'%3E%3C/svg%3E)

A simple subtraction formula would give me the result.

\=B2-A2

![Date subtraction formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20424'%3E%3C/svg%3E)

There is a possibility that Excel will give you the result in the date format instead of a number as shown above.

This sometimes happens when Excel tries to be helpful and pick up the format from the adjacent column.

You can easily adjust this and get the values in numbers by going to the Home tab, and select General in the number format drop-down.

Note: This formula would only work when you using a date that Excel recognizes as a valid date format. For example, if you use 01.01.2020, Excel won’t recognize it as a date and consider it a text string. So you won’t be able to subtract dates with such a format

You can read more about [subtracting dates in Excel here](https://trumpexcel.com/calculate-time-in-excel/)

Subtract Time in Excel
----------------------

Just like dates, even time values are stored as numbers in Excel.

While the day part of the date would be represented by the whole number, the time part would be represented by the decimal.

For example, 44197.5 would represent 01 Jan 2021 12:00 PM and 44197.25 would represent 01 Jan 2021 09:00 AM

In case you have time values in Excel, what you really have in the back end in Excel are decimal numbers that represent that time value (which are formatted to be shown as time in the cells).

And since these are numbers, you can easily subtract these.

Below I have a data set where I have the start time and the end time, and I want to calculate the difference between these two times.

![Dataset to subtract time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20341'%3E%3C/svg%3E)

Here is the formula that will give us the difference between these time values:

\=B2-A2

![Time difference in decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20390'%3E%3C/svg%3E)

There is a high possibility that Excel will change the format of the result column to show the difference as a time value (for example, it may show you 9:00 AM instead of 0.375). You can easily change this by going to the Home tab and selecting General from the format dropdown.

![Apply the general format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20376'%3E%3C/svg%3E)

Note that in case of times, you will get the value in decimals, but if you want it in hours, minutes, and seconds, you can do that by multiplying the decimal value with 24 (for getting hours), or 24\*60 for getting minutes and 24\*60\*60 for getting seconds.

So if you want to know how many hours are there in the given time in our dataset, you can use the below formula:

\=(B2-A2)\*24

![Formula to get time difference in hours](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20391'%3E%3C/svg%3E)

Subtract Percentages in Excel
-----------------------------

[Subtracting percentages](https://trumpexcel.com/add-subtract-percentage-from-number-excel/)
 from a number in Excel is a little different than subtracting two whole numbers or decimals.

Suppose you have two [percentage values](https://trumpexcel.com/calculate-percentages-excel/)
 (as shown below) and you want to subtract one from another, you can use a simple subtraction formula

![Subtracting percentages in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20429%20248'%3E%3C/svg%3E)

But if you want to subtract a percentage value from a non-percentage value, you need to do it differently.

Suppose you have 100 in cell B1 and you want to subtract 20% from this value (i.e., subtract 20% of 100 from 100).

You can use the below formal in this case:

\=B1\*(1-20%)

![After subtracting a percentage in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20503%20173'%3E%3C/svg%3E)

You can also use the below formula:

\=B1-B1\*20%

In case you have the percentage value in a cell, then you can use the cell reference as well. For example, if you have the dataset as shown below, and you want to subtract the percentage value in cell B2 from the number in B1.

![Subtract Percentage dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20192'%3E%3C/svg%3E)

Then you can use the below formula:

\=B1-B1\*B2

![Formula to subtract percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20245'%3E%3C/svg%3E)

Subtract Using Paste Special
----------------------------

And finally, you can also use [Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
 trick to subtract in Excel.

This is useful when you want to quickly subtract a specific value from an entire column.

Suppose you have the dataset as shown below and you want to subtract 100 from each of these numbers.

![Dataset to subtract using paste special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20371'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In an empty cell, enter the value that you want to subtract from the entire column. In this example, I will enter this value in cell D1

![Enter the value to subtract in an empty cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20371'%3E%3C/svg%3E)

2.  Copy cell D1 (which is the cell where you have entered this value you want to subtract)

![Copy the cell that has the value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20371'%3E%3C/svg%3E)

3.  Select the entire column from which you want to subtract the copied value
4.  Right-click and then click on the Paste Special option

![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20517%20377'%3E%3C/svg%3E)

5.  In the special dialog box, select Values as the Paste option

![Click on Values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20413'%3E%3C/svg%3E)

6.  Under Operations, select Subtract

![Click on Subtract](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20413'%3E%3C/svg%3E)

7.  Click OK
8.  Delete the value that you entered in the cell in Step 1

The above steps but simply subtract the value that you copied from the selected column. The result you get from this is a static value.

![Resulting Data where value has been subtracted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20371'%3E%3C/svg%3E)

The benefit of this method is that you do not need an additional column where you need to apply a formula to subtract the values. In case you want to keep the original values as well, simply create a copy of the column and then use the above steps

So these are different ways that you can use Excel to **subtract values/percentages, cells, and columns**.

Understanding these basic concepts will help you use the Excel spreadsheet tool the most efficient way.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Multiply in Excel Using Paste Special](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
    
*   [How to Sum Only Positive or Negative Numbers in Excel](https://trumpexcel.com/sum-positive-numbers-excel/)
    
*   [Change Negative Number to Positive in Excel \[Remove Negative Sign\]](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Subtract Multiple Cells from One Cell in Excel](https://spreadsheetplanet.com/subtract-multiple-cells-from-one-cell-excel/)
    
*   [Calculate Percentage Change in Excel (% Increase/Decrease Formula)](https://trumpexcel.com/percentage-change-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/subtract-in-excel/#respond)

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