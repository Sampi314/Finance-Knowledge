# How to Use Excel SMALL Function (Useful Examples + Video)

**Source:** https://trumpexcel.com/excel-small-function

---

[Skip to content](https://trumpexcel.com/excel-small-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-small-function/#below-title)

Excel SMALL Function – Overview
-------------------------------

![Excel SMALL Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20330'%3E%3C/svg%3E)

### When to use Excel SMALL Function

Excel SMALL function can be used to get the Kth smallest value from a range of cells or array. For example, you can get the 3rd smallest value from a range of cells.

### What it Returns

It returns the value which is the Kth smallest value from a range of cells.

### Syntax

\=SMALL(array, k)

### Input Arguments

*   array – the array or range of cells from which you want to fetch the kth smallest value.
*   k – the rank or position (from the bottom) of the number that you want to fetch.

### Additional Notes

*   If the array is empty, SMALL returns the #NUM! error value.
*   If k ≤ 0 or if k is greater than the number of data points, SMALL returns the #NUM! error value.
*   If n is the number of data points in a range, then SMALL(array,1) returns the smallest value, and SMALL(array,n) returns the largest value.

Excel SMALL Function – Examples
-------------------------------

Here are six example of using Excel SMALL Function:

### #1 Getting the smallest value from a list

![Excel Small Function - Smallest Value from a list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20678%20171'%3E%3C/svg%3E)

If you have a list of numbers (A2:A4) and you want to get the smallest number from the list, you can use the following small function: \=SMALL(A2:A4,1)

Here the Kth value is 1, which would return the smallest number from the range of numbers.

### #2 Getting the second smallest value from a list

![Excel Small Function - Second Smallest Value from a list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20168'%3E%3C/svg%3E)

To get the second smallest value from the list (A2:A4), use the following formula: \=SMALL(A2:A4,2)

Since the Kth value in the formula is 2, it returns the second smallest values from the range of numbers.

### #3 Using SMALL function when there are blank cells in the range

![Excel Small Function - Ignores Blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20172'%3E%3C/svg%3E)

If there are any blank cells in the range, it is ignored by the small function. For example, in the above example, while we take the range of cells as A2:A5, the blank cell is ignored by the SMALL function while returning the smallest value from this list.

### #4 Using SMALL function when there are cells with Text

![Excel Small Function - Ignores Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20221'%3E%3C/svg%3E)

Similar to blank cells, Excel SMALL function also ignores cells with text, alphanumeric characters, special characters, and logical values.

### #5 Using SMALL function when there are cells with Duplicates

![Excel Small Function - Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20196'%3E%3C/svg%3E)

If there are duplicates in the range used in the Excel SMALL function, it will treat those duplicates as consecutive values. In the above example, two cells have the value 1. Now when you use the SMALL function to return the smallest and second smallest value, it returns 1 in both cases.

### #6 Using SMALL function when there is an Error in the Range

![Excel Small Function - Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20175'%3E%3C/svg%3E)

If there is an error in any of the cells used in the Excel SMALL function, it will return an error.

Excel SMALL Function – Video Tutorial
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
*   [Excel LARGE Function](https://trumpexcel.com/excel-large-function/)
    .
*   [Excel MAX Function](https://trumpexcel.com/excel-max-function/)
    .
*   [Excel MIN Function](https://trumpexcel.com/excel-min-function/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Use Excel SMALL Function (Examples + Video)”
------------------------------------------------------------------

1.  single line formula to find 10 largest values in arrary
    
    [Reply](https://trumpexcel.com/excel-small-function/#comment-11778)
    
2.  I like the concept, but I want to know this, if I want the smallest number among 3 cells which contains no number, why must the answer be #NUM!
    
    [Reply](https://trumpexcel.com/excel-small-function/#comment-10979)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-small-function/#respond)

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