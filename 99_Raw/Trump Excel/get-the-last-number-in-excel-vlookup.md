# Use VLookup to Get the Last Number in a List in Excel

**Source:** https://trumpexcel.com/get-the-last-number-in-excel-vlookup

---

[Skip to content](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#below-title)

Excel has its own limitations, and in this blog post, I will show you how we can use one of the limitations to our advantage.

Get the Last Number in a List in Excel using Excel VLOOKUP Function
-------------------------------------------------------------------

The largest positive number that you can use in Excel is **9.99999999999999E+307** _(I tried this in Excel 2010)._

_That’s huge!!_

I don’t think you would ever need any calculation involving such a large number. And that is exactly what we can use get the last number in a list.

Suppose you have a dataset _(in A1:A14)_ as shown below and you want to get the last number in the list.![Get the Last Number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20226%20275'%3E%3C/svg%3E) Here is the formula you can use:

\=[VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
(9.99999999999999E+307,$A$1:$A$14,**TRUE)**

##### **How this works:**

*   _**List with NUMBERS only**_

Note that I have used an approximate match VLOOKUP _(notice TRUE at the end of the formula, instead of FALSE)._ This means that if the formula spots the exact match of the look-up value, it returns that value. Otherwise, it keeps on going one cell after the other and stops when the value in the next cell is higher. It then returns the value of the cell where it stopped.

We use this property by putting the largest possible number excel can handle as the look-up value. So, excel would keep on going till the last cell, and when it can’t find anything larger than this, it returns the value in the last cell.

*   **List with NUMBERS and TEXT both**

This formula would work with a list that has numbers as well as text. Here we use the fact that in Excel, _**the value of a text is higher than the value of a number**_ (try =”a”>9.99999999999999E+307 in any cell. It will return TRUE)

So when you use a list with numbers as well as text and use the above formula, it scans the entire list one cell at a time.

It stops when it can not find a number bigger than 9.99999999999999E+307. Since the value of text is considered higher than numbers in Excel, this formula would correctly return the last number from the list.

**You May Also Like the Following VLOOKUP Tutorials:**

*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    .
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    .
*   [VLOOKUP vs XLOOKUP](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)
    
*   [VLOOKUP Vs. INDEX/MATCH  – The Debate Ends Here!](https://trumpexcel.com/vlookup-vs-index-match/)
    .
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    .
*   [Find the Last Occurrence of a Lookup Value a List in Excel](https://trumpexcel.com/find-last-occurrence/)
    .
*   [Find the Second Largest Value in Excel](https://trumpexcel.com/find-second-largest-value-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Use VLookup to Get the Last Number in a List in Excel”
---------------------------------------------------------------------

1.  I love you!! I created a checking account spreadsheet years ago and because some month would have longer transactions then others, I never could find a formula to automatically pull the last transaction amount from the last month’s tab to start my new month’s tab. This was so simple to do, once I saw your formula I laughed at myself!
    
    [Reply](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#comment-1694)
    
    *   Thanks man.. sometimes it’s these small things that make our life so easy.. Glad this formula worked for you
        
        [Reply](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#comment-1696)
        
        *   Thanks today I have learned a new formula.
            
            [Reply](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#comment-9519)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/#respond)

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