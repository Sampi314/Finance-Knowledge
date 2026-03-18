# Data Analysis - Goal Seek in Excel

**Source:** https://trumpexcel.com/goal-seek-in-excel

---

[Skip to content](https://trumpexcel.com/goal-seek-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/goal-seek-in-excel/#below-title)

This is the fourth article of the five-part series on Data Analysis in Excel. In this section, I will show you how to use Goal Seek in Excel.

**[Download Example File](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Goal-Seek.xls)
**

_**Other articles in this series:**_

*   [One Variable Data Table in Excel.](https://trumpexcel.com/one-variable-data-table-in-excel/)
    
*   [Two Variable Data Table in Excel](https://trumpexcel.com/two-variable-data-table-in-excel/)
    .
*   [Scenario Manager in Excel](https://trumpexcel.com/scenario-manager-in-excel/)
    .
*   [Excel Solver.](https://trumpexcel.com/solver-in-excel/)
    

**Watch Video – Goal Seek in Excel**

Goal Seek in Excel, as the name suggests, helps you in achieving a value (the goal) by altering a dependent value.

For example, I have the data (as shown below), where I calculate the Monthly payment outflow with the given Loan Amount, Interest Rate and Number of Payments. _\[Monthly payment is in red and in round brackets as it is an outflow\]._

![Goal Seek in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20106'%3E%3C/svg%3E)

I use the following [PMT formula](https://trumpexcel.com/pmt-function/)
 in cell B4 to calculate the Monthly payment:

\=PMT(B2/12,B3,B1)

Now, I want to calculate the loan amount so that my monthly payment is  **$1,000**. I can try and use some trial and error by putting random values in Loan amount, but there is a better way to do this – using Goal Seek in Excel.

#### Using Goal Seek in Excel

*   Go to Data –> Data Tools –> What-If Analysis –> Goal Seek.![Goal Seek in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20162'%3E%3C/svg%3E)
*   In the Goal Seek Dialogue Box, use the following details:
    *   Set Cell: B4 (this is the cell with the goal/target).
    *   To Value: \-1,000 (this is the goal value. Its negative here as it is an outflow).
    *   By Changing Cell: B1 (this is the loan amount that we want to change to achieve the goal value).![Goal Seek in Excel - Values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20156'%3E%3C/svg%3E)
*   Click OK. This will open the Goal Seek Status dialogue box.
    *   Goal Seek Status dialogue box will inform you when a solution is found. If you wish to accept the solution, click on the OK button, and it will change the cell values. If you do not want to accept the solution, click on Cancel.
    *   It may happen that the Goal Seek is not able to find a solution. It will show you the relevant prompt in that case.![Goal Seek in Excel - Status Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20159'%3E%3C/svg%3E)
*   Once you accept the solution, it will be reflected in the cells.![Goal Seek in Excel - New Solution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20113'%3E%3C/svg%3E)

_**Try it yourself..Download the file[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Goal-Seek.xls)
**_

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    .
*   [Making Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    .
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Data Analysis \[Part 4 of 5\] – Goal Seek in Excel”
------------------------------------------------------------------

1.  what if you enter a negative number in the \[to:value\] but it doesn’t work? how do I get negatives to work?
    
    Thank you 🙂
    
    [Reply](https://trumpexcel.com/goal-seek-in-excel/#comment-14436)
    
2.  Bro it would really help if you explain us with few other examples coz I tried using you given formula but it ain’t working so..
    
    [Reply](https://trumpexcel.com/goal-seek-in-excel/#comment-13104)
    
3.  Amazing! Exactly what I was looking for.
    
    [Reply](https://trumpexcel.com/goal-seek-in-excel/#comment-1635)
    
    *   Thanks for commenting Nikhil.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/goal-seek-in-excel/#comment-2351)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/goal-seek-in-excel/#respond)

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