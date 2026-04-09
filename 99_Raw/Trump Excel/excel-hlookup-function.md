# Excel HLOOKUP Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-hlookup-function

---

[Skip to content](https://trumpexcel.com/excel-hlookup-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-hlookup-function/#below-title)

![Excel HLOOKUP Function](https://trumpexcel.com/wp-content/uploads/2014/03/HLOOKUP-FORMULA-EXCEL.png)

### When to use Excel HLOOKUP Function

Excel HLOOKUP function is best suited for situations when you are looking for a matching data point in a row, and when the matching data point is found, you go down that column and fetch a value from a cell which is specified number of rows below the top row.

### What it Returns

It returns the specified matching value.

### Syntax

\=HLOOKUP(lookup\_value, table\_array, row\_index\_num, \[range\_lookup\])

### Input Arguments

*   **lookup\_value –** this is the look-up value that you are looking for in the first row of the table. It could be a value, a cell reference, or a text string.
*   **table\_array –** this is the table in which you are looking for the value. This could be a reference to a range of cells or a named range.
*   **row\_index –** this is the row number from which you want to fetch the matching value. If row\_index is 1, the function would return the lookup value (as it is in the 1st row). If row\_index is 2, the function would return the value from the row just below the lookup value.
*   **\[range\_lookup\] –** (Optional) here you specify whether you want an exact match or an approximate match. If omitted, it defaults to TRUE – approximate match _(see additional notes below)._

### Additional Notes

*   The match could be exact (FALSE or 0 in range\_lookup) or approximate (TRUE or 1).
*   In approximate lookup, make sure that the list is sorted in ascending order (left to right), or else the result could be inaccurate.
*   When range\_lookup is TRUE (approximate lookup) and data is sorted in ascending order:
    *   If the HLOOKUP function can not find the value, it returns the largest value, which is less than the lookup\_value.
    *   It returns a #N/A error if the lookup\_value is smaller than the smallest value.
    *   If lookup\_value is text, [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
         can be used (refer to the example below).

Excel HLOOKUP Function – Live Example
-------------------------------------

Excel HLOOKUP Function – Video Tutorial
---------------------------------------

**Related Excel Functions:**

*   [Excel VLOOKUP Function](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [Excel XLOOKUP Function](https://trumpexcel.com/xlookup-function/)
    
*   [Excel INDEX Function](https://trumpexcel.com/excel-index-function/)
    .
*   [Excel INDIRECT Function](https://trumpexcel.com/excel-indirect-function/)
    .
*   [Excel MATCH Function](https://trumpexcel.com/excel-match-function/)
    .
*   [Excel OFFSET Function](https://trumpexcel.com/excel-offset-function/)
    .
*   [Excel TAKE Function](https://trumpexcel.com/excel-functions/take-function/)
    
*   [DROP Function in Excel](https://trumpexcel.com/excel-functions/drop-function/)
    

**You May Also Like the Following Excel Tutorials:**

*   [VLOOKUP Vs Index/Match Combination](https://trumpexcel.com/vlookup-vs-index-match/)
    .
*   [Excel Index Match](https://trumpexcel.com/index-match/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-hlookup-function/#respond)

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