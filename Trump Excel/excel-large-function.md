# How to Use Excel LARGE Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-large-function

---

[Skip to content](https://trumpexcel.com/excel-large-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-large-function/#below-title)

Excel LARGE Function (Example + Video)
--------------------------------------

![Excel LARGE Function](https://trumpexcel.com/wp-content/uploads/2014/03/LARGE-FORMULA-EXCEL.png)

### When to use Excel LARGE Function

Excel LARGE function can be used to get the Kth largest value from a range of cells or array. For example, you can get the 3rd largest value from a range of cells.

### What it Returns

It returns the value which is the Kth largest value from a range of cells.

### Syntax

\=LARGE(array, k)

### Input Arguments

*   array – the array or range of cells from which you want to fetch the kth largest value.
*   k – the rank or position (from the top) of number that you want to fetch.

### Additional Notes

*   If array is empty, LARGE returns the #NUM! error value.
*   If k ≤ 0 or if k is greater than the number of data points, LARGE returns the #NUM! error value.
*   If n is the number of data points in a range, then LARGE(array,1) returns the largest value, and LARGE(array,n) returns the smallest value.

Examples – Excel LARGE Function
-------------------------------

Here are six example of using Excel LARGE Function:

### **#1 Getting the largest value from a list**

![Excel Large Function - Smallest Value from a list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20165'%3E%3C/svg%3E)

If you have a list of numbers (A2:A4) and you want to get the largest number from the list, you can use the following LARGE function: =LARGE(A2:A4,1)

Here the Kth value is 1, which would return the largest number from the range of numbers.

### **#2 Getting the second largest value from a list**

![Excel LARGE Function - Second largest Value from a list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20160'%3E%3C/svg%3E)

To get the second largest value from the list (A2:A4), use the following formula: =LARGE(A2:A4,2)

Since the Kth value in the formula is 2, it returns the second largest values from the range of numbers.

### **#3 Using LARGE function when there are blank cells in the range**

![Excel LARGE Function - Ignores Blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20172'%3E%3C/svg%3E)

If there are any blank cells in the range, it is ignored by the LARGE function.

For example, in the above example, while we take the range of cells as A2:A5, the blank cell is ignored by the LARGE function while returning the largest value from this list.

### **#4 Using LARGE function when there are cells with text**

![Excel LARGE Function - Ignores Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20221'%3E%3C/svg%3E)

Similar to blank cells, Excel LARGE function also ignores cells with text, alphanumeric characters, special characters, and logical values.

### **#5 Using LARGE function when there are cells with duplicates**

![Excel LARGE Function - Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20189'%3E%3C/svg%3E)

If there are duplicates in the range used in the LARGE function, it will treat those duplicates as consecutive values. In the above example, two cells have the value 7. Now when you use LARGE function to return the largest and second largest value, it returns 7 in both the cases.

### **#6 Using LARGE function when there is Error in the cells**

![Excel LARGE Function - Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20172'%3E%3C/svg%3E)

If there is an error in any of the cells used in the LARGE function, it will return an error.

Excel LARGE Function – Video Tutorial
-------------------------------------

**Related Excel Functions:**

*   [Excel INT Function](https://trumpexcel.com/excel-int-function/)
    .
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
*   [Excel MAX Function](https://trumpexcel.com/excel-max-function/)
    .
*   [Excel MIN Function](https://trumpexcel.com/excel-min-function/)
    .
*   [Excel SMALL Function](https://trumpexcel.com/excel-small-function/)
    .

**Other articles you may also like:**

*   [Find the Second Largest Value in Excel](https://trumpexcel.com/find-second-largest-value-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-large-function/#respond)

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