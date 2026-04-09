# How to Use Excel INT Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-int-function

---

[Skip to content](https://trumpexcel.com/excel-int-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-int-function/#below-title)

In this tutorial, you’ll learn how to use the INT function in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-int-function/#)

Excel INT Function Overview
---------------------------

![Excel INT Function](https://trumpexcel.com/wp-content/uploads/2014/03/INT-FORMULA-EXCEL.png)

### When to use Excel INT Function

INT Function is used when you want to get the integer portion of a number.

### What it Returns

It returns an integer number.

### Syntax

\=INT(number)

### Input Arguments

*   **number –** the number for which you want to get the integer value.

Excel INT Function Examples
---------------------------

Below are three examples of using the INT function in Excel.

### Example 1 – Getting the Integer Part from a Positive number

When you use INT function with a positive integer, it discards the decimal part and gives you the integer part of the number.

![Excel INT Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20124'%3E%3C/svg%3E)

For example, in the above example, it returns 4 as the function [rounds down](https://trumpexcel.com/round-to-nearest-integer/)
 the value in cell A2.

### Example 2 – Getting the Integer Part from a Negative number

When you use the INT function with a negative number, it rounds down the number. This means that you get the number which is lower that the given number.

![Excel INT Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20112'%3E%3C/svg%3E)

In the above example, the result is -5, which is lower than -4.89.

So instead of giving you the integer part (as it did in Example 1), it gives you the number which is an integer and lower than the given number.

### Example 3 – Getting the Age using Date of Birth

You can use the INT function to get the [age of a person using their date of birth](https://trumpexcel.com/calculate-age-in-excel/)
.

To do this, you need to use it along with TODAY and YEARFRAC functions.

Suppose the date of birth is 14 May 1988, then you can use the below formula to calculate the age in Excel:

\=INT(YEARFRAC(A2,TODAY()))

![Excel INT Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20766%20111'%3E%3C/svg%3E)

YEARFRAC formula takes the date of birth and the current date (which is given by the [TODAY function](https://trumpexcel.com/excel-today-function/)
) and returns the age in years. It has the integer as well as the [fraction](https://trumpexcel.com/display-numbers-as-fractions-excel/)
 part.

Then the INT function returns only the integer part from it.

Video Tutorial
--------------

**Related Excel Functions:**

*   [Excel MOD Function](https://trumpexcel.com/excel-mod-function/)
    .
*   [Excel RAND Function](https://trumpexcel.com/excel-rand-function/)
    .
*   [Excel RANDBETWEEN Function](https://trumpexcel.com/excel-randbetween-function/)
    .
*   [Excel ROUND Function](https://trumpexcel.com/excel-round-function/)
    .
*   [Excel RANK Function](https://trumpexcel.com/excel-rank-function/)
    .
*   [Excel LARGE Function](https://trumpexcel.com/excel-large-function/)
    .
*   [Excel MAX Function](https://trumpexcel.com/excel-max-function/)
    .
*   [Excel MIN Function](https://trumpexcel.com/excel-min-function/)
    .
*   [Excel SMALL Function](https://trumpexcel.com/excel-small-function/)
    .
*   [Excel LN Function – Calculating Natural Log in Excel](https://trumpexcel.com/excel-functions/ln-natural-log/)
    

**Related Excel Tutorials:**

*   [How to Remove Time from Date in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Use Excel INT Function (Examples + Video)”
---------------------------------------------------------------

1.  In cell A8, it should be =INT(A3)
    
    [Reply](https://trumpexcel.com/excel-int-function/#comment-8777)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-int-function/#respond)

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