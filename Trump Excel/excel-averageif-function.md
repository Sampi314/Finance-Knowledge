# How to Use Excel Averageif Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-averageif-function

---

[Skip to content](https://trumpexcel.com/excel-averageif-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-averageif-function/#below-title)

Excel AVERAGEIF Function (Example + Video)
------------------------------------------

![Excel Averageif Function](https://trumpexcel.com/wp-content/uploads/2014/03/AVERAGEIF-FORMULA-EXCEL.png)

### When to use Excel AVERAGEIF Function

Excel AVERAGEIF function can be used when you want to get the average (arithmetic mean) of all the values in a range of cells that meet a given criteria.

### What it Returns

It returns a numerical value that represents the average (arithmetic mean) of the values in a range of cells that meets the given criteria.

### Syntax

\=AVERAGEIF(range, criteria, \[average\_range\])

### Input Arguments

*   **range** – the range of cells against which the criteria is evaluated. It could be numbers, text, arrays, or references that contain numbers.
*   **criteria** – the criterion that is checked against the range and determines which cells to average.
*   **\[average\_range\]** – (optional) the cells to add. If this argument is omitted, it uses _range_ as the _sum\_range._

### Additional Notes

*   Empty cells are ignored in average\_range.
*   If the criteria is an empty cell, Excel treats it as 0.
*   If no cell meets the criteria, a #DIV/0! error is returned.
*   If range is a blank or text value, AVERAGEIF returns the #DIV0! error value.
*   Criteria could be a number, expression, cell reference, text, or a formula.
    *   Criteria which are text or mathematical/logical symbols (such as =,+,-,/,\*) should be in double quotes.
    *   [Wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
         can be used in criteria.

Excel AVERAGEIF Function – Examples
-----------------------------------

Here are three examples of using the Excel AVERAGEIF function.

### **#1 Getting the Average of a Matching Criteria**

![Excel Averageif Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20189'%3E%3C/svg%3E)

In the above example, Excel AverageIf functions checks for the criteria “Tom” in A2:A6. For all the matching values in Column A, it gives the average of corresponding values in column B.

![Excel Averageif Function - Example 1a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%20188'%3E%3C/svg%3E)

In this example, all the values in column B for Tom are averaged (10, 12, and 0).

You can also cell reference instead of manually entering the criteria.

### **#2 Using Wildcard Characters in Excel AVERAGEIF Function**

You can use wildcard characters in the Excel AVERAGEIF function to construct criteria.

There are three wildcard characters in Excel – a question mark (?), an asterisk (\*), and a tilde (~).

*   A question mark (?) matches any single character.
*   An asterisk (\*) matches any sequence of characters.
*   If you want to find an actual question mark or asterisk, type a tilde (**~**) before the character.

![Excel Averageif Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20193'%3E%3C/svg%3E)

In the above example, the AVERAGEIF function checks for the criteria where the name has the alphabet ‘a’ in it. Since it is flanked by asterisks (\*) at both sides, it means that the word can have any number of characters before and after the alphabet ‘a’.

Of all the names, Jane and Arjun meet the criteria and the function gives the average of values for these two names (12 and 15).

![Excel Averageif Function - Example 2a](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20206'%3E%3C/svg%3E)

### **#3 Using Comparison Operators within Excel AVERAGEIF function**

![Excel Averageif Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20210'%3E%3C/svg%3E)

In the Excel AVERAGEIF function, if you omit the last argument (average\_range) then it takes the first argument (the criteria range) as the average\_range also. In the above example,

In the above example, B2:B6 is used to check for the criteria as well as to calculate the average. The criteria here is “>10” which checks for all the numbers greater than 10, and averages them.

Note that the operator always needs to be in double quotes. So you can use “>10” or “>”&10 or “>”&B2 (where B2 has the numerical value).

Excel AVERAGEIF Function – Video Tutorial
-----------------------------------------

**Related Excel Functions:**

*   [Excel AVERAGE Function](https://trumpexcel.com/excel-average-function/)
    .
*   [Excel AVERAGEIFS Function](https://trumpexcel.com/excel-averageifs-function/)
    .
*   [Excel SUM Function](https://trumpexcel.com/excel-sum-function/)
    .
*   [Excel SUMIF Function](https://trumpexcel.com/excel-sumif-function/)
    .
*   [Excel SUMIFS Function](https://trumpexcel.com/excel-sumifs-function/)
    .
*   [Excel SUMPRODUCT Function](https://trumpexcel.com/excel-sumproduct-function/)
    

**Other articles you may also like:**

*   [Insert X-Bar Symbol in Excel (Average / Mean)](https://trumpexcel.com/excel-insert-symbols/x-bar-average-mean/)
    
*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [Calculating Moving Average in Excel](https://trumpexcel.com/moving-average-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-averageif-function/#respond)

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