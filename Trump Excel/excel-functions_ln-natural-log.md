# Excel LN Function - Calculating Natural Log in Excel

**Source:** https://trumpexcel.com/excel-functions/ln-natural-log

---

[Skip to content](https://trumpexcel.com/excel-functions/ln-natural-log/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/ln-natural-log/#below-title)

Excel has a dedicated function to calculate the natural logarithm of a number – LN Function.

While not as common, this is a useful function for many Excel users working with scientific, engineering, statistics, or financial data.

In this article, I will show you how to use the LN function to calculate the natural log value in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/ln-natural-log/#)

Excel LN Function – Syntax
--------------------------

Below is the syntax of the LN function in Excel:

\=LN(number)

where the number is the argument where you provide the positive number for which you want to calculate the natural log value. This could also be a cell reference that contains the number.

_The LN function can only take positive numbers as arguments. If you use a negative number within this function, it is going to give you the number error (#NUM!)_

The natural logarithm is the logarithm to the base of the mathematical constant e (called Euler’s number with an approximate value of 2.71828).

In mathematics, the natural logarithm is the power to which e must be raised to obtain a given value. So when I calculate the natural log of 10 and the result is 2.302585, it means that I need to stack up the value of e 2.302585 times to reach 10

Calculating Natural Log in Excel
--------------------------------

Now, let me show you an example of how to use the LN function.

Below, I have a data set where I have some numbers in column A, and I want to calculate their natural log value and get the result in column B:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20267'%3E%3C/svg%3E)

The following formula would do this:

\=LN(A2)

Enter this formula in cell B2, and then copy it for all the other cells in the column.

![Excel LN Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20314'%3E%3C/svg%3E)

And if you have dynamic arrays in your Excel, you can also use the below formula:

\=LN(A2:A6)

Here are a couple of interesting things to note:

*   The natural log of the number 1 is 0 (as e raised to power 0 would give us 1)
*   In cell A3, I have the value of E, which is 2.718281282. When I calculate the natural log for this number, it gives me 1. This is because e^1 is equal to 2.718281282.

**Interesting Fact**: The LN function in Excel is the inverse of the EXP function (EXP), which takes a number and gives us e raised to the power of that number. So if use =LN(EXP(10)), it would give me the result as 10. Another Similar function in Excel is the LOG function that returns the logarithm of a given number using the base you specify in the formula.

_Another Similar function in Excel is the LOG function that returns the logarithm of a given number using the base you specify in the formula._

In this article, I showed you how to use the Excel LN function to calculate the natural log of values.

I hope you found this article helpful.

If you have any questions about the Excel LN function or if you have any suggestions for me, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Excel Functions](https://trumpexcel.com/excel-functions/)
    
*   [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)
    
*   [How to Calculate Square Root in Excel (Using Easy Formulas)](https://trumpexcel.com/calculate-square-root-in-excel/)
    
*   [How to Use Excel INT Function](https://trumpexcel.com/excel-int-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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