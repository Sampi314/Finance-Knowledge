# Data Analysis - Two Variable Data Table in Excel

**Source:** https://trumpexcel.com/two-variable-data-table-in-excel

---

[Skip to content](https://trumpexcel.com/two-variable-data-table-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/two-variable-data-table-in-excel/#below-title)

This is the second article of the five part series on Data Analysis in Excel. In this section, I will show you how to use Two Variable Data Table in Excel.

**[Download Example File](https://trumpexcel.com/wp-content/uploads/2014/11/Two-Variable-Data-Table-in-Excel.xls)
**

_**Other articles in this series:**_

*   [One Variable Data Table in Excel.](https://trumpexcel.com/one-variable-data-table-in-excel/)
    
*   [Scenario Manager in Excel.](https://trumpexcel.com/scenario-manager-in-excel/)
    
*   [Goal Seek in Excel.](https://trumpexcel.com/goal-seek-in-excel/)
    
*   [Excel Solver.](https://trumpexcel.com/solver-in-excel/)
    

**Watch Video – Two-variable Data Table in Excel**

Two-variable data table is best suited in situations when you want to see how the final result changes when two of the input variables change simultaneously (as against [One Variable Data Table](https://trumpexcel.com/one-variable-data-table-in-excel/)
 where only one of the input variable changes).

If you want to analyze data when more than 2 variables change, [scenario manager](https://trumpexcel.com/scenario-manager-in-excel/)
 is the way to go.

#### When to use Two Variable Data Table in Excel

Suppose you have a data set as shown below:![Data Table in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20106'%3E%3C/svg%3E)

In the above data set, we have the Loan Amount, Interest Rate, and Number of Monthly payments. Based on these 3 input variables, Monthly Payment is calculated (it is in red as it is an outflow of money). The following formula is used to calculate the Monthly Payment:

\=PMT(B2/12,B3,B1)

Now you may want to do an analysis to see what should be the ideal combination of Loan Amount and Number of Monthly Payment to suit your requirement. For example, you may want to keep the Monthly Payment at $500 or less, and analyze what Loan Amount and Tenure combination can give you this.

In such a situation, a two variable data table should be used.

#### Setting up Two Variable Data Table in Excel

Here are the steps to set up a Two variable data table in Excel:

*   In a column, have all the different values that you want to test for Number of Monthly Payments. In this example, we are testing for 72, 84, 96… 240. At the same time, have the different loan amount values in the row just above the column values (beginning one cell to the right) as shown in the pic below.![Two Variable Data Table in Excel - Data Set 2 Variable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20265'%3E%3C/svg%3E)
*   Type \=B4 in cell D1, which is one row above the values in the column. This is a construct that needs to be followed when you work with two variable data table. Also, make sure that the value in cell D1 is dependent on both the variables (Number of Monthly Payments and Loan amount). It won’t work if you manually enter the value in cell D1.  
    _In this case, cell D1 refers to cell B4, which has a value calculated using a formula which uses cells B1, B2 and B3_.![Two Variable Data Table in Excel - Refer to Cell 2 variable data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20263'%3E%3C/svg%3E)
*   Now the data is all set to be used for a two variable data table calculation.
*   Select the data (D1:J16). Go to Data Tab –> Data Tools –> What if Analysis –> Data Table![Data Table in Excel - Selecting from Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%20120'%3E%3C/svg%3E)
*   In the Data Table Dialogue box, use the following references:
    *   Row input cell: $B$1
    *   Column input cell: $B$3![Two Variable Data Table in Excel - Dialogue Box 2 variable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20240%20134'%3E%3C/svg%3E)
*   Click OK. As soon as you click OK, it instantly fills the all the empty cells in the selected data range. It quickly gives you a view of Monthly Payments for a various combinations of Loan amount and Number of Monthly Payments.![Two Variable Data Table in Excel - Two Variable data calculated](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20264'%3E%3C/svg%3E)

For example, if you want to identify the combinations of Loan Amount and Number of Monthly Payment that would result in a Monthly Payment of less than $500 per month payout, you can simply use this 2 variable data table method.

###### _**Note:**_

*   Once you have calculated the values using data table, it can not be undone using Control + Z. You can however manually select all the values and delete it.
*   You can not delete/modify any one cell in the entire set of calculated values. Since this is an array, you will have to delete all the values.

_**Download File.. Try it yourself**_

[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/11/Two-Variable-Data-Table-in-Excel.xls)

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Making Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    
*   [How to Find Slope in Excel?](https://trumpexcel.com/find-slope-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    
*   [How to Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Data Analysis \[Part 2 of 5\] – Two Variable Data Table in Excel”
--------------------------------------------------------------------------------

1.  I have a table which contains the employees age in range against the salary range and wanted to retrieve the number of employees with the age against the salary
    
    Ages Salary  
    15-25 26-30 31-3  
    18-25 1 2 3  
    26-30 4 5 6  
    31-35 7 8 9  
    Require excel formula when the age is punch between the age and salary the corresponding value gets displayed
    
    Example
    
    Age 29  
    Sal 29
    
    Output 5
    
    [Reply](https://trumpexcel.com/two-variable-data-table-in-excel/#comment-12669)
    
2.  How can you change the reference cell (D1) to be a word? Like if I wan’t to make D1 say ‘Rate’, but without it affecting the data in the data table? Like is there some way to lock the information in the data table, in order for me to make D1 say ‘Rate’?
    
    [Reply](https://trumpexcel.com/two-variable-data-table-in-excel/#comment-9751)
    
3.  Very useful video…
    
    [Reply](https://trumpexcel.com/two-variable-data-table-in-excel/#comment-3794)
    
    *   Thanks for commenting.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/two-variable-data-table-in-excel/#comment-3799)
        
4.  Great Article. Thanks for sharing.
    
    [Reply](https://trumpexcel.com/two-variable-data-table-in-excel/#comment-1633)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/two-variable-data-table-in-excel/#respond)

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