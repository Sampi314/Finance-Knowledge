# How to Calculate Square Root in Excel (Using Easy Formulas)

**Source:** https://trumpexcel.com/calculate-square-root-in-excel

---

[Skip to content](https://trumpexcel.com/calculate-square-root-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-square-root-in-excel/#below-title)

It’s amazing how you can find multiple ways to do the same thing in Excel. After all, there are so many awesome functionalities and functions.

A really simple and often needed task is to calculate the square root in Excel.

And as I said, there are multiple ways you can do that in Excel (formulas, VBA, Power Query).

In this tutorial, I will show you different ways to calculate square root in Excel (and you can choose whatever method you like best).

But before I get into how to calculate it, let me quickly cover what is square root (feel free to skip to the next section if I get too preachy).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-square-root-in-excel/#)

What is Square Root?
--------------------

When you multiply a number (let’s say X) with itself, you get a value (let’s say Y).

Here X is the square root of Y.

For example, 10 multiplied by 10 is 100.

Here 10 is the square root of 100.

That’s it! It’s simple. But it’s not so simple to calculate it.

For example, if I ask you to calculate the square root of 50, I am sure you can’t calculate it in your head (unless you’re a math whiz).

[Here is a detailed article](https://en.wikipedia.org/wiki/Square_root)
 on Wikipedia in case you’re interested in learning more about it.

In this tutorial, I will show you a couple of ways (easy ones I promise) to **calculate square root in Excel**.

So let’s get started!

Calculate Square Root Using the SQRT function
---------------------------------------------

Yes, there is a dedicated function in Excel whose purpose of existence is to give you the square root

SQRT function takes one single argument (could be the number or reference to the number) and returns the square root of that number.

![Calculate Square root using the SQRT function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20162'%3E%3C/svg%3E)

To calculate the square root of 100 in Excel, you can use the below formula:

\=SQRT(100)

The above formula will give you 10, which is the square root of 100.

You can also use a cell reference in the SQRT function as shown below:

![SQRT formula using a cell reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20131'%3E%3C/svg%3E)

Note: Another result here could be -10, but the formula only returns the positive value.

While this function works great with positive numbers, if you give it a negative number, it will return a #NUM error.

![SQRT function returns num error when the input number is negative](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%20126'%3E%3C/svg%3E)

This is understandable as in mathematics, a negative number [doesn’t have a square root](https://math.stackexchange.com/questions/677619/why-is-the-square-root-of-a-negative-number-impossible)
. Even if a number is negative, when you multiply it by itself, the result is positive.

But in case you still want the square root of a negative number (assuming it was a positive), you can need to first convert the negative number into a positive one and then find the square root of it. For example, if you want to get the square root of -100, you can use SQRT function with the ABS function:

\=SQRT(ABS(-100))

![getting square root of a negative value with ABS function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20127'%3E%3C/svg%3E)

ABS function gives you the absolute value and ignores the negative sign.

Note: There are two more square root related functions in Excel:

1.  **SQRTPI** – This function returns the square root of a number which has been multiplied by the constant Pi (π)
2.  **IMSQRT** – This function returns the square root of a complex number

Calculate Square Root Using the Exponential Operator
----------------------------------------------------

Another way to calculate the square root (or cube root or Nth root) in Excel is by using the exponential operator.

If all you need is the square root of a number, it’s easier to use the SQRT function. The benefit of using the exponential operator is that you can use it to find the square root, the cube root, or the nth root as well.

You can also use it to find the square of a number.

Below is the formula that will give you the square root of 100

\=100^(1/2)

or

\=100^0.5

![Square root using exponential sign](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20129'%3E%3C/svg%3E)

Similarly, you can get the cube root or the Nth root of a number as well.

Below is the formula to get the cube root of 100

\=100^(1/3)

And below is the formula to get the Nth root of 100 (replace N with any number you want)

\=100^(1/N)

_**Important note about brackets**: When using the exponential operator with [fractions](https://trumpexcel.com/display-numbers-as-fractions-excel/)
 (such as 1/2 or 1/3), make sure these fractions are in brackets. For example, =100^(1/2) and =100^1/2 would give two different results. This is because the exponential operator gets preference over division and is calculated first. Using brackets makes this issue go away._

Also read: [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)

Calculate Square Root Using the POWER Function
----------------------------------------------

Another easy way to calculate square root in Excel (or cube root or Nth root) is by using the POWER function.

Below is the syntax of the POWER function:

\=POWER(number,power)

It takes two arguments:

1.  the base number (could be any real numbers)
2.  the power/exponent to which this base number is raised

Unlike the SQRT function, you can use the POWER function to calculate the roots (such as square root or cube root) or powers (such as square or cube) of a number.

Below is the formula that will give you the square root of 100 in Excel:

\=POWER(100,1/2)

or

\=POWER(100,.5)

![Calculate Square root using the POWER function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20128'%3E%3C/svg%3E)

In case you want the cube root, you can use the below formula:

\=POWER(100,1/3)

And similarly, if you want the square of a number, you can use the same formula with the relevant second argument.

\=POWER(100,2)

In case you use a negative number in the POWER function, it will return a #NUM error.

Also read: [Insert Pi Symbol (π) in Excel](https://trumpexcel.com/pi-symbol-excel/)

Getting the Square Root Using Power Query
-----------------------------------------

While the above formulas as quick and, if you work with a lot of data and this is something you need to do quite often, you may also consider using Power Query.

This method is more suited when you have a large dataset where you want to calculate the square root of values in a column, and you get a new dataset every day/week/month/quarter. Using Power Query will minimize effort as you can simply plug in the new data and refresh the query and it will give you the result.

For the purpose of this example, I will use a simple dataset as shown below where I need to calculate the square root on values in column B.

![Dataset to use in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20482'%3E%3C/svg%3E)

Below are the steps to calculate square root using Power Query in Excel:

1.  Select any cell in the dataset
2.  Click the Insert tab![Click the Insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20200'%3E%3C/svg%3E)
3.  Click on Table icon (it’s in the Tables group). This will open the Create Table dialog box.![Click on the Table icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20198'%3E%3C/svg%3E)
4.  Check the range and check the Option ‘My table has headers’. Click OK. This will convert the tabular data into an Excel Table.![Check range in the Create Table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20185'%3E%3C/svg%3E)
5.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20200'%3E%3C/svg%3E)
6.  In the Get & Transform group, click on the ‘From Table/Range’ option. This will open the Power Query editor![Click from range or table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20200'%3E%3C/svg%3E)
7.  In the Query Editor, click on the column header![Select the column where you want to get the square root](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%20543'%3E%3C/svg%3E)
8.  Click the Transform tab![Click the Transform tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20171'%3E%3C/svg%3E)
9.  In the Number group, click on the scientific option
10.  Click on Square root. This would instantly change the values in the selected column and give you the square roots of the original numbers.![Click on Scientific option and then click on Square Root](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20281%20284'%3E%3C/svg%3E)
11.  Click the File tab![CLick the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20172'%3E%3C/svg%3E)
12.  Click on Close and Load.![Click on Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20220%20297'%3E%3C/svg%3E)

The above steps would create a new worksheet in the Excel workbook and insert the table from the Power Query. This new table will have the square roots of the original table data.

In case you have any negative values in the cells, you will get a #NUM error in the resulting table.

While there are a few steps involved in getting this to work with Power Query, the awesome benefit of Power Query is that now you can simply refresh and get the new results when you get the new data.

For example, if you now get new data next month, you need to simply copy and paste that data into the table we created (in Step 4), go to any cell in the table you got from Power Query, right-click and hit refresh.

So, while it takes a few clicks to get this done the first time, once set, you can easily transform the new data with a simple refresh.

Apart from the square root, you can also use the Power function in Power Query to get the cube root or Nth root (or to get the square or cube of the numbers).

Also read: [Insert Average (Mean) Symbol in Excel](https://trumpexcel.com/excel-insert-symbols/x-bar-average-mean/)

Inserting the Square Root Symbol (√) in Excel
---------------------------------------------

While a little off-topic, I thought I will also let you know how to insert the square root symbol in Excel.

This could be useful when you want to show value with the square root symbol and the square root of it side by side. Something as shown below.

And just like we have different formulas to calculate the square root value in Excel, we also have a couple of methods to insert the square root symbol too.

### Insert Square Root Symbol with a Shortcut

If you use a numeric keypad, here is the keyboard shortcut to insert the square root symbol:

ALT + 251

Hold the ALT key and then press the number keys 2,5, and 1 on the numeric keypad. Now when you leave the keys, the square root symbol will be inserted.

### Insert Square Root Symbol with a Formula

You can also use a formula to get the square root symbol in Excel.

This can be useful when having a column of values and you want to quickly add the square root symbol to all of these.

To get the square root symbol, you can use the below formula:

\=UNICHAR(8730)

![Insert square root symbol using UNICHAR formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20132'%3E%3C/svg%3E)

Since this is a formula, you can also combine it with other formulas or cell references. For example, if you have a column of values and you want to add the square root symbol to all these values, you can use the formula as shown below:

\=UNICHAR(8730)&A1

![Append square root symbol to a value using ampersand](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20400'%3E%3C/svg%3E)

Note: If you only want to get the square root symbol a couple of times, you can get it once using the keyboard shortcut or the formula, and then simply copy and paste it.

### Insert Square Root Symbol by Changing the Custom Number Format

And finally, the third way to add the square root symbol is by changing the cell  formatting in such a way that it would appear whenever you type anything in the cell

Below are the steps to change the cell formatting to automatically add the square root symbol:

1.  Select the cells where you want to the square root symbol to appear automatically
2.  Hold the control key and press the 1 key. This will open the Format Cells dialog box
3.  In the Category pane in the left, click on the Custom option
4.  In the Type field, enter √General![Change cell formatting using the Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20603'%3E%3C/svg%3E)
5.  Click OK

Once done, you will see that all the selected cells automatically gets the square root symbol.

One good thing about using this method is that it doesn’t change the value in the cell. It only changes how it’s being displayed.

This means that you can use these values in formulas and calculations without worrying about the square root symbol interfering. You can confirm this by selecting a cell and looking at the formula bar (which shows you the actual value in the cell).

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [What is Standard Deviation and How to Calculate it in Excel?](https://trumpexcel.com/standard-deviation/)
    
*   [Calculating Moving Average in Excel](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [How to Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    
*   [How to Calculate Compound Interest in Excel](https://trumpexcel.com/compound-interest-calculator/)
    
*   [How to Find Range in Excel](https://trumpexcel.com/find-range-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-square-root-in-excel/#respond)

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