# Calculate Percentage Change in Excel (% Increase/Decrease Formula)

**Source:** https://trumpexcel.com/percentage-change-excel

---

[Skip to content](https://trumpexcel.com/percentage-change-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/percentage-change-excel/#below-title)

When working with data in Excel, calculating the percentage change is a common task.

Whether you working with professional sales data, resource management, project management, or personal data, knowing how to calculate percentage change would help you make better decisions and do better data analysis in Excel.

It’s really easy, thanks to amazing MS Excel features and functions.

In this tutorial, I will show you how to **calculate percentage change in Excel** (i.e., percentage increase or decrease over the given time period).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/percentage-change-excel/#)

Calculate Percentage Change Between Two Values (Easy Formula)
-------------------------------------------------------------

The most common scenario where you have to calculate percentage change is when you have two values, and you need to find out how much change has happened from one value to the other.

For example, if the price of an item increases from $60 to $80, this could be a scenario where you have to calculate how much increase in percentage happened in this case.

Let’s have a look at examples.

### Percentage Increase

Suppose I have the data set as shown below where I have the old price of an item in cell A2 and the new price in cell B2.

![Dataset to calculate percent increase](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20105'%3E%3C/svg%3E)

The formula to calculate the percentage increase would be:

\=Change in Price/Original Price

Below is the formula to calculate the price percentage increase in Excel:

\=(B2-A2)/A2

![Formula to calculate percentage increase](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20180'%3E%3C/svg%3E)

There’s a possibility that you may get the resulting value in decimals (the value would be correct, but need the right format).

To convert this decimal into a [percentage value](https://trumpexcel.com/calculate-percentages-excel/)
, select the cell that has the value and then click on the percentage icon (%) in the Number group in the Home tab of the Excel ribbon.

![Convert decimal to percentage icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20163'%3E%3C/svg%3E)

In case you want to increase or decrease the number of digits after the decimal, use the Increase/Decrease decimal icons that are next to the percentage icon.

![increase decimal icons](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20163'%3E%3C/svg%3E)

Important: It is important to note that I have kept the calculation to find out the change in new end old price in brackets. This is important because I first want to calculate the difference and then want to divide it by the original price. in case you don’t put these in brackets, the formula will first divide and then subtract (following the order of precedence of operators)

### Percentage Decrease

Calculating a percentage decrease works the same way as a percentage increase.

Suppose you have the below two values where the new price is lower than the old price.

![Dataset to calculate percent decrease](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20102'%3E%3C/svg%3E)

In this case, you can use the below formula to calculate the percentage decrease:

\=(B2-A2)/A2

![Formula to calculate percentage decrease](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20167'%3E%3C/svg%3E)

Since we are calculating the percentage decrease, we calculate the difference between the old and the new price and then divide that value from the old price.

Also read: [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)

Calculate the Value After Percentage Increase/Decrease
------------------------------------------------------

Suppose you have a data set as shown below, where I have some values in column A and the percentage change values in column B.

![Dataset to calculate percentage change in column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20372'%3E%3C/svg%3E)

Below is the formula you can use to calculate the final value that would be after incorporating the percentage change in column B:

\=A2\*(1+B2)

![Formula to calculate value after percentage change](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20422'%3E%3C/svg%3E)

You need to copy and paste this formula for all the cells in Column C.

In the above formula, I first calculate the overall percentage that needs to be multiplied with the value. to do that, I [add the percentage](https://trumpexcel.com/add-subtract-percentage-from-number-excel/)
 value to 1 (within brackets).

And this final value is then multiplied by the values in column A to get the result.

As you can see, it would work for both percentage increase and percentage decrease.

In case you’re using Excel with Microsoft 365 subscription, you can use the below formula (and you don’t need to worry about copy-pasting the formula:

\=A2:A11\*(1+B2:B11)

Increase/Decrease an Entire Column with Specific Percentage Value
-----------------------------------------------------------------

Suppose you have a data set as shown below where I have the old values in column A and I want the new values column to be 10% higher than the old values.

![Dataset to calculate 10% change](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20372'%3E%3C/svg%3E)

This essentially means that I want to increment all the values in Column A by 10%.

You can use the below formula to do this:

\=A2\*(1+10%)

![Formula to calculate value after 10% increase](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20415'%3E%3C/svg%3E)

The above formula simply multiplies the old value by 110%, which would end up giving you a value that is 10% higher.

Similarly, if you want to decrease the [entire column](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
 by 10%, you can use the below formula:

\=A2\*(1-10%)

![Formula to calculate value after 10% decline](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20417'%3E%3C/svg%3E)

Remember that you need to copy and paste this formula for the entire column.

In case you have the value (by which you want to increase or decrease the entire column) in a cell, you can [use the cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 instead of hardcoding it into the formula.

For example, if I have the percentage value in cell D2, I can use the below formula to get the new value after the percentage change:

\=A2\*(1+$D$2)

![Percentage change using value in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20421'%3E%3C/svg%3E)

The benefit of having the percentage change value in a separate cell is that in case you have to change the calculation by changing this value, you just need to do that in one cell. Since all the formulas are linked to the cell, the formulas would automatically update.

Percentage Change in Excel with Zero
------------------------------------

While calculating percentage change in excel is quite easy, you will likely face some challenges when there is a zero involved in the calculation.

For example, if your old value is zero and your new value is 100, what do you think is the percentage increase.

If you use the formulas we have used so far, you will have the below formula:

\=(100-0)/0

But you can’t divide a number by zero in math. so if you try and do this, Excel will give you a division error (#DIV/0!)

This is not an Excel problem, rather it’s a math problem.

In such cases, a commonly accepted solution is to consider the percentage change as 100% (as the new value has grown by 100% starting from zero).

Now, what if you had the opposite.

What if you have a value that goes from 100 to 0, and you want to calculate the percentage change.

Thankfully, in this case, you can.

The formula would be:

\=(100-0)/100

This will give you 100%, which is the correct answer.

So to put it in simple terms, if you calculating percentage change and there is a 0 involved (be it as the new value or the old value), the change would be 100%

Percentage Change With Negative Numbers
---------------------------------------

If you have negative numbers involved and you want to calculate the percentage change, things get a bit tricky.

With negative numbers, there could be the following two cases:

1.  Both the values are negative
2.  One of the values is negative and the Other one is Positive

Let’s go through this one by one!

### Both the Values are Negative

Suppose you have a dataset as shown below where both the values are negative.

![Dataset when both values are negative](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20545%20122'%3E%3C/svg%3E)

I want to find out what’s the change in percentage when values change from -10 to -50

The good news is that if both the values are negative, you can simply go ahead and use the same logic and formula you use with positive numbers.

So below is the formula that will give the right result:

\=(A2-B2)/A2

![Formula to calculate percentage when both values are negative](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20169'%3E%3C/svg%3E)

In case both the numbers have the same sign (positive or negative), the math takes care of it.

### One Value is Positive and One is Negative

In this scenario, there are two possibilities:

1.  Old value is positive and new value is negative
2.  Old value is negative and new value is positive

Let’s look at the first scenario!

### Old Value is Positive and New Value is Negative

If the old value is positive, thankfully the math works and you can use the regular percentage formula in Excel.

Suppose you have the dataset as shown below and you want to calculate the percentage change between these values:

The below formula will work:

\=(B2-A2)/A2

As you can see, since the new value is negative, this means that there is a decline from the old value, so the result would be a negative percentage change.

So all’s good here!

Now let’s look at the other scenario.

### Old Value is Negative and New Value is Positive

This one needs one minor change.

Suppose you’re calculating the change where the old value is -10 and the new value is 10.

![Dataset where old value is negative and new is positive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20122'%3E%3C/svg%3E)

If we use the same formulas as before, we will get -200% (which is incorrect as the value change has been positive).

This happens since the denominator in our example is negative. So while the value change is positive, the denominator makes the final result a negative percentage change.

Here is the fix – **make the denominator positive**.

And here is the new formula you can use in case you have negative values involved:

\=(B2-A2)/ABS(A2)

![Formula to calculate percentage when old value is negative](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20171'%3E%3C/svg%3E)

The ABS function gives the absolute value, so negative values are automatically changes to positive.

So these are some methods that you can use to calculate percentage change in Excel. I have also covered the scenarios where you need to calculate percent change when one of the values could be 0 or negative.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How To Subtract In Excel (Subtract Cells, Column, Dates/Time)](https://trumpexcel.com/subtract-in-excel/)
    
*   [How to Multiply in Excel Using Paste Special](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
    
*   [How to Stop Excel from Rounding Numbers (Decimals/Fractions)](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Add Decimal Places in Excel (Automatically)](https://trumpexcel.com/add-decimal-places-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [How to Calculate PERCENTILE in Excel](https://trumpexcel.com/percentile-excel/)
    
*   [Percentage Change Calculator (X% of Y / Increase / Decrease)](https://trumpexcel.com/calculator/percentage-change/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/percentage-change-excel/#respond)

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