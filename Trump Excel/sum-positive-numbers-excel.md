# How to Sum Only Positive or Negative Numbers in Excel (Easy Formula)

**Source:** https://trumpexcel.com/sum-positive-numbers-excel

---

[Skip to content](https://trumpexcel.com/sum-positive-numbers-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-positive-numbers-excel/#below-title)

When you work with numbers in Excel, you often need to conditional add the data.

One common example of this is when you have to sum the positive numbers in Excel (or only sum the negative numbers).

And this can easily be done using the in-built formulas in Excel.

In this tutorial, I will show you how to **sum only positive or negative numbers in Excel** using simple formulas.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-positive-numbers-excel/#)

SUM Positive Numbers Only
-------------------------

Suppose you have a dataset as shown below and you want to sum all the positive numbers in column B.

![Dataset to sum only positive values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20345'%3E%3C/svg%3E)

Below is  the formula that will do this:

\=SUMIF(B2:B8,">0",B2:B8)

![SUMIF formula to sum only positive values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20535%20480'%3E%3C/svg%3E)

The above [SUMIF formula](https://trumpexcel.com/excel-sumif-function/)
 takes three arguments:

1.  The first argument is the criteria range. This is where we will check for criteria and only add values that meet the criteria. In our example, this is B2:B8
2.  The second argument is the criteria itself. Since we only want to sum the positive numbers, this is “>0”. Remember that when you use an operator, it should be within double-quotes.
3.  The third argument has the actual range that you want to sum.

Note that with the SUMIF formula, the criteria range and the range of cells that you want to sum can be different. In our example, both the criteria range and the sum range is the same (B2:B8).

Since I only have one criterion in this case, I have used the SUMIF formula. In case you have multiple criteria to check you can use this [SUMIFS formula](https://trumpexcel.com/excel-sumifs-function/)
 in Excel.

### SUM All Positive Numbers Greater than 100

In the previous example, we added all the cells that had a positive value. You can also use the SUMIF formula, so only at those specific cells that meet another criterion.

For example, in the below data set, I only want to add those cells where the value is greater than 100.

![Dataset to sum only positive values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20345'%3E%3C/svg%3E)

All I need to do is adjust the criteria so that instead of adding all the positive numbers it adds all the numbers that are greater than 100.

Below is the formula that would do this:

\=SUMIF(B2:B8,">100",B2:B8)

![SUMIF formula to sum only positive values greater than 100](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20482'%3E%3C/svg%3E)

As you can see, all I’ve done is adjusted the second argument, which is the criteria argument.

### Add All Numbers where Another Cell Value is Positive

In the above examples, we have used the SUMIF formula in which the ‘criteria range’ and the ‘sum range’ is the same.

But as I mentioned, you can have these as separate ranges as well.

So you can have a range of cells where you evaluate a criterion and then based on whether a cell meets the criteria or not, you can then add the value in a corresponding range.

Below I have a data set where I want to add or the cells where the growth is positive which is in column C.

![Dataset to sum positive value based on another cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20267'%3E%3C/svg%3E)

Below is the formula that will add only those cells in column B, where the corresponding cell in column C has a positive value:

\=SUMIF(C2:C6,">0",B2:B6)

![SUMIF formula to sum only positive values based on another cell value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20404'%3E%3C/svg%3E)

Note that this is a similar formula as we had used above (with one change). Instead of having the same ‘criteria’ and ‘sum’ range, it’s different in this formula.

**Pro tip**: When you have specified the criteria range, you don’t need to specify the entire sum range. For example, the following formula will work just fine –  =SUMIF(C2:C6,”>0″,B2). Since C2:C6 is already specified, you don’t need to specify B2:B6. Only the first cell will do. The formula will automatically take the same size range starting from B2.

Also read: [SUM Based on Partial Text Match in Excel (SUMIF)](https://trumpexcel.com/sum-partial-match/)

SUM Negative Numbers Only
-------------------------

Just like we did the sum of all the positive numbers, you can use a similar concept to sum only the negative values only.

Suppose you have the dataset as shown below and you want to sum only the negative numbers in column B.

![Dataset to sum only positive values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20345'%3E%3C/svg%3E)

Below is the formula to do this:

\=SUMIF(B2:B8,"<0",B2:B8)

![Formula to sum negative values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20483'%3E%3C/svg%3E)

The above formula uses “<0” as the criteria (second argument), which only adds the negative numbers.

And you can use the same concepts shown earlier to add negative numbers below a specific number and can even have separate criteria and sum ranges.

So this is how you can use a simple SUMIF formula to add only the positive numbers or negative numbers in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [Change Negative Number to Positive in Excel \[Remove Negative Sign\]](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Sum Across Multiple Sheets in Excel? (3D SUM Formula)](https://trumpexcel.com/sum-across-multiple-sheets-excel/)
    
*   [How to Add Plus Sign Before Numbers in Excel](https://trumpexcel.com/add-plus-sign-before-numbers-excel/)
    
*   [SUMPRODUCT vs SUMIFS Function in Excel](https://spreadsheetplanet.com/sumproduct-vs-sumifs-function-excel/)
    
*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How To Subtract In Excel (Subtract Cells, Column, Dates/Time)](https://trumpexcel.com/subtract-in-excel/)
    
*   [Show Negative Numbers in Parentheses (Brackets) in Excel (Easy Ways)](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Sum Only Positive or Negative Numbers in Excel (Easy Formula)”
-----------------------------------------------------------------------------------

1.  What about if we would like to sum only postive or greater/smaller numbers from a list of cells like A2, A4, A6, A8, etc instead of a range of cells like A1:A9?
    
    [Reply](https://trumpexcel.com/sum-positive-numbers-excel/#comment-44720)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-positive-numbers-excel/#respond)

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