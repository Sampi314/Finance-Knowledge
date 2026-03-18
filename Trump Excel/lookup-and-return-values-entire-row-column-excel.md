# How to Lookup Entire Row / Column in Excel

**Source:** https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel

---

[Skip to content](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/#below-title)

[VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 is one of the most used functions in Excel. It looks for a value in a range and returns a corresponding value in a specified column number.

Now I came across a problem where I had to lookup entire row and return the values in all the columns from that row (instead of returning a single value).

So here is what I had to do. In the below dataset, I had Sales Rep names and the Sales they made in 4 quarters in 2012. I had a drop [down with their names, and I wanted to extract the maximum sales for that Sales Rep in those four quarters](https://trumpexcel.com/calculate-quarter-from-date-excel/)
.

![Lookup Entire Row / Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20333'%3E%3C/svg%3E)

I could come up with 2 different ways to do this – Using [INDEX](https://trumpexcel.com/excel-index-function/)
 or VLOOKUP.  

#### **Lookup Entire Row / Column Using INDEX Formula**

Here is the formula I created to do this using Index

\=LARGE(INDEX($B$4:$F$13,MATCH(H3,$B$4:$B$13,0),0),1)

##### How it works:

Let first look at the INDEX function that is wrapped inside the [LARGE](https://trumpexcel.com/excel-large-function/)
 function.

\=INDEX($C$4:$F$13,MATCH(H3,$B$4:$B$13,0),0)

Let’s closely analyze the arguments of the INDEX function:

*   Array – $B$4:$F$1
*   Row Number –  MATCH(H3,$B$4:$B$13,0)
*   **Column Number – 0**

Notice that I have used column number as 0.

The trick here is that when you use column number as 0, it returns all the values in all the columns. So if I select John in the drop down, the index formula would return all the 4 sales values for John {91064,71690,67574,25427}.

Now I can use the Large function to extract the largest value

_Pro Tip - Use Column/Row number as 0 in Index formula to return all the values in Columns/Rows._

#### **Lookup Entire Row / Column Using VLOOKUP Formula**

While Index formula is neat, clean and robust, VLOOKUP way is a bit complex. It also ends up making the function [volatile](https://trumpexcel.com/excel-volatile-formulas/)
. However, there is an amazing trick that I would share in this section. Here is the formula:

\=LARGE(VLOOKUP(H3,B4:F13, ROW(INDIRECT("2:"&COUNTA($B$4:$F$4))), FALSE),1) 

##### How it works

*   ROW(INDIRECT(“2:”&COUNTA($B$4:$F$4))) – This formula returns an array {2;3;4;5}. Note that since it uses INDIRECT, this makes this formula volatile.

*   VLOOKUP(H3,B4:F13,ROW(INDIRECT(“2:”&COUNTA($B$4:$F$4))),FALSE) – Here is the best part. When you put these together, it becomes VLOOKUP(H3,B4:F13,{2;3;4;5},FALSE). Now notice that instead of a single column number, I have given it an array of column numbers. And VLOOKUP obediently looks up values in all these columns and returns an array.

*   Now just use LARGE function to extract the largest value.

_Remember to use Control + Shift + Enter to use this formula._

_Pro Tip - In VLOOKUP, instead of using a single column number, if you use an array of column numbers, it will return an array of lookup values._

**You may also like the following Excel tutorials:**

*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [VLOOKUP vs XLOOKUP Function](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)
    
*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    .
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    .
*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [How to Return Cell Address Instead of Value in Excel](https://trumpexcel.com/return-cell-address-instead-of-value-excel/)
    
*   [How to Apply Formula to the Entire Column in Excel](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Lookup and Return Values in an Entire Row/Column in Excel”
------------------------------------------------------------------------

1.  Keep me posted on videos updates on LOOKUP post examples on YouTube and reminder to  
    My email id
    
    [Reply](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/#comment-12726)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/#respond)

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