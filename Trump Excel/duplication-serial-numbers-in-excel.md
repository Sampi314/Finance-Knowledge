# Avoid Duplication in Serial Numbers in Excel

**Source:** https://trumpexcel.com/duplication-serial-numbers-in-excel

---

[Skip to content](https://trumpexcel.com/duplication-serial-numbers-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/duplication-serial-numbers-in-excel/#below-title)

A friend called me and asked if there is a way to have serial numbers in such a way that they are no duplication in serial numbers in Excel.

Something as shown below:

![Serial Numbers in Excel - Data](https://trumpexcel.com/wp-content/uploads/2013/07/Serial-Numbers-in-Excel-Data.png)

He wanted that the serial number for India should be 1 wherever it occurs. Similarly, US is the 2nd country and should always have 2 as its serial number.

This got me thinking.

And here are the two ways that I could come up with to avoid duplication in serial numbers in Excel.

##### **Method #1 – Using VLOOKUP Function  
**

The first way is to use our beloved [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
.

To do this, we first need to get a unique list of countries. Here are the steps to do that:

*   Create a copy of the list of countries (copy paste it in the same worksheet or another worksheet).
*   Select the copied data and go to Data –> Remove Duplicates. It will open the remove duplicate dialogue box.![Serial Numbers in Excel - Remove Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20285'%3E%3C/svg%3E)
*   Make sure that the option – My data has headers is checked (in case your data has the header. Else uncheck it).![Serial Numbers in Excel - Remove Duplicates has headers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20442%20285'%3E%3C/svg%3E)
*   Select the column from which you want to remove ṭhe duplicates.![Serial Numbers in Excel - Remove Duplicates seelct column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20285'%3E%3C/svg%3E)
*   Click OK.
*   That’s it. You will have a list of unique country names.

See Also: [The Ultimate Guide to Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
.

Now assign the serial numbers to each country. Make sure these numbers entered to the right of the unique country list, as VLOOKUP can’t fetch data from the left of the lookup value.![Serial Numbers in Excel - methodology](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20365'%3E%3C/svg%3E)

In the cell, where you want the serial numbers (B3:B15), use the below VLOOKUP formula:

\=VLOOKUP(C3,$F$3:$G$8,2,0)

This VLOOKUP formula takes the country name as the lookup value, checks for it in the data in F3:G8, and returns its serial number.

##### **Method #2** **– A Dynamic Formula**

While the VLOOKUP method is a perfectly fine way of doing this, it is not dynamic.

So if I add a new country or change an existing country, this method would not work and you will have to repeat the entire process of method #1 again.

Here is a formula that makes it dynamic:

\=IF([COUNTIF](https://trumpexcel.com/excel-countif-function/)
($C$3:$C4,$C4)=1,[MAX](https://trumpexcel.com/excel-max-function/)
($B$3:$B3)+1,[INDEX](https://trumpexcel.com/excel-index-function/)
($B$3:$C$18,[MATCH](https://trumpexcel.com/excel-match-function/)
($C4,$C$3:$C4,0),1))

To use this formula, you need to manually enter 1 in the first cell, and the above formula in all the other remaining cells.

**How it work****s:**

It uses an [IF function](https://trumpexcel.com/excel-if-function/)
 that checks the number of times a country has occurred prior to that row. If the country name occurs for the first time, the count is 1 and the condition is TRUE, and if the country name has occurred earlier as well, the count is more than 1 and the condition is FALSE.

*   _When the condition is TRUE:_

\=MAX($B$3:$B3)+1

If the value is TRUE, which means that the country name is appearing for the first time, it identifies the maximum value of serial number till then and adds 1 to it to give the next serial number value.

*   _When Value if FALSE:_

\=INDEX($B$3:$C$18,MATCH($C4,$C$3:$C4,0),1)

If the country has already occurred earlier, this formula goes to the cell where it appears first and returns the serial number of the first occurrence of that country.

**Download the Example File**_**[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2013/07/Avoid-Duplication-in-Serial-Numbers-in-Excel.xlsx)
**_

**You May Also Like the Following Excel Tutorials:**

*   [How to Use Flash Fill in Excel.](https://trumpexcel.com/flash-fill-excel/)
    
*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    .
*   [How to Quickly Fill Numbers in Cells without Dragging](https://trumpexcel.com/fill-numbers-in-cells-without-dragging/)
    .
*   [How to use Fill Handle in Excel](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Avoid Duplication in Serial Numbers in Excel”
------------------------------------------------------------

1.  Need a serial number
    
    [Reply](https://trumpexcel.com/duplication-serial-numbers-in-excel/#comment-12464)
    
2.  I need a serial number
    
    [Reply](https://trumpexcel.com/duplication-serial-numbers-in-excel/#comment-12463)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/duplication-serial-numbers-in-excel/#respond)

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