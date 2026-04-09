# Drop Down Lists To Show Numbers Between Two Specified Numbers

**Source:** https://trumpexcel.com/drop-down-numbers

---

[Skip to content](https://trumpexcel.com/drop-down-numbers/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/drop-down-numbers/#below-title)

I recently got an email from one of my readers with an interesting query on using [drop-down lists](https://trumpexcel.com/excel-drop-down-list/)
 in Excel.

He asked me if it was possible to have a drop-down list that shows numbers based on the two specified numbers.

Something as shown below:

![Drop Down Lists with Specified Numbers](https://trumpexcel.com/wp-content/uploads/2017/06/Drop-Down-Lists-with-Specified-Numbers.gif)

Note that the drop-down start from the number in column A and goes up to the number in Column B. For example, the drop down in D2 shows numbers from 1 to 10, and the one in D3 shows numbers from 5 to 20, and so on.

This kind of drop-down can be created using a helper column and INDIRECT function.

Let’s dive in and see how to create this.

### Using INDIRECT Formula

This idea in this method is to use the [INDIRECT function](https://trumpexcel.com/excel-indirect-function/)
 to create a range that would show numbers between the two specified numbers. To do this, I have used a helper column.

Here are the steps to use the INDIRECT formula to create the drop-down between specified numbers:

*   In column C, enter the numbers from 1 to 1000 (you can do this quickly using the [fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
    ). The idea is to cover all the numbers that can be used in the drop down. This will be our helper column.![Drop Down List Between Numbers helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20392'%3E%3C/svg%3E)
*   Select the cell or range of cells in which you want the drop-down.
*   Go to the Data tab and click on Data Validation.![Data Validation in Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20131'%3E%3C/svg%3E)
*   In the Data Validation dialog box, within the settings tab, select List from the drop down.![Data Validation List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20319'%3E%3C/svg%3E)
*   In the Source field, enter the following formula: =INDIRECT(“$C$”&A2+1&”:$C$”&B2+1)![Data Validation Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20319'%3E%3C/svg%3E)
*   Click OK.

That’s it!

It will create a drop-down list that will show numbers that are in between the two specified numbers.

**How does this work?**

The helper column’s role is to provide a range of cells that can be referred to in the drop-down formula.

The INDIRECT formula creates this range by using the numbers in columns A and B. Note that in the formula, I have added 1 to the number (A2+1 and B2+1), as the helper column numbers start from the second row.

**[Click here](https://trumpexcel.com/wp-content/uploads/2017/06/Drop-Down-List-Between-Numbers.xlsx)
** to Download the Example file.

**You May Also Like the Following Excel Tutorials:**

*   [Select Multiple Items from a Drop Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [How to Create a Dependent Drop Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    .
*   [Extract Data from Drop Down List Selection in Excel](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Show Symbols in Drop-Down Lists in Excel](https://trumpexcel.com/symbols-in-drop-down-lists-excel/)
    
*   [How to Make a Yes/No Drop-Down in Excel?](https://trumpexcel.com/make-yes-no-drop-down-excel/)
    
*   [How to Remove Drop-Down List in Excel?](https://trumpexcel.com/remove-drop-down-list-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Drop Down Lists To Show Numbers Between Two Specified Numbers”
-----------------------------------------------------------------------------

1.  What if column C in a different work sheet, how can I write the formula? Thanks
    
    [Reply](https://trumpexcel.com/drop-down-numbers/#comment-14566)
    
2.  How would you apply this formula if you needed to reference cells in a different worksheet?
    
    [Reply](https://trumpexcel.com/drop-down-numbers/#comment-11225)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/drop-down-numbers/#respond)

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