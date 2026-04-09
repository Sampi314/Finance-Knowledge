# Data Analysis - One Variable Data Table in Excel

**Source:** https://trumpexcel.com/one-variable-data-table-in-excel

---

[Skip to content](https://trumpexcel.com/one-variable-data-table-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/one-variable-data-table-in-excel/#below-title)

This is the first article of the five-part series on Data Analysis in Excel. In this section, I will show you how to create and use a One Variable Data Table in Excel.

**[Download Example File](https://trumpexcel.com/wp-content/uploads/2014/11/One-Variable-Data-Table-in-Excel.xls)
**

_**Other articles in the Data Analysis series:**_

*   [Two Variable Data Table in Excel.](https://trumpexcel.com/two-variable-data-table-in-excel/)
    
*   [Scenario Manager in Excel.](https://trumpexcel.com/scenario-manager-in-excel/)
    
*   [Goal Seek in Excel.](https://trumpexcel.com/goal-seek-in-excel/)
    
*   [Excel Solver.](https://trumpexcel.com/solver-in-excel/)
    

**Watch Video – One-Variable Data Table in Excel**

One variable Data Table in Excel is most suited in situations when you want to see how the final result changes when you change one of the input variables. _If you want to change two variables, use [two variable data table](https://trumpexcel.com/two-variable-data-table-in-excel/)
, or [Scenario Manager](https://trumpexcel.com/scenario-manager-in-excel/)
._

#### When to use One Variable Data Table in Excel

Suppose you have a data set as shown below:

![One Variable Data Table in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20106'%3E%3C/svg%3E)

In the above data set, we have the Loan Amount, Interest Rate, and Number of Monthly payments.

The Monthly Payment value is calculated based on these three variables (it is in red as it is an outflow of money). The following formula is used to calculate the Monthly Payment:

\=PMT(B2/12,B3,B1)

Now you may want to do an analysis to see what number of monthly payments suits your condition, and how would the monthly payment vary based on it. For example, you may want to keep the tenure of your loan (number of monthly payments) such that your Monthly Payment amount is not more than $1,000.

A quick way is to change the data in this table and the formula would automatically update. However, if you want to test if for many different Number of Monthly Payments, then a One Variable Data Table in Excel would be the way to go.

#### Setting Up a One Variable Data Table in Excel

Here are the steps to set up a One variable data table in Excel:

*   In a column, have all the different values of Number of Monthly Payments that you want to test. In this example, we are testing for 72, 84, 96… 240.![One Variable Data Table in Excel - Different Values to Test](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20332'%3E%3C/svg%3E)
*   Type \=B4 in cell E1, which is one row above the values in the adjacent column to the right. This is a construct that needs to be followed when you work with one variable data table in Excel. Also, make sure that the value in cell E1 is dependent on Number of Monthly Payments. It won’t work if you manually enter the value in cell E1.  
    _In this case, cell E1 refers to cell B4, which has a value calculated using a formula which uses cells B1, B2 and B3_.![One Variable Data Table in Excel - Refer to Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20328'%3E%3C/svg%3E)
*   Now the data is all set to be used in the One Variable data table.
*   Select the data (D1:E16). Go to Data Tab –> Data Tools –> What if Analysis –> Data Table.![One Variable Data Table in Excel - Selecting from Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%20120'%3E%3C/svg%3E)
*   In the Data Table dialogue box, refer to cell B3 in Column input cell field. Since we are using a one-variable data table, leave the Row input cell empty. Also, we chose Column input cell option as the data is structured in a column.![One Variable Data Table in Excel - Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20239%20137'%3E%3C/svg%3E)
*   Click OK. As soon as you click OK, it will automatically fill the cells adjacent to the variable data points (number of monthly payments).![One Variable Data Table in Excel - One Variable data calculated](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20485%20330'%3E%3C/svg%3E)

For example, if you wanted to calculated what number of monthly payments you should use to have the monthly payment less than $1,000. You can easily select 144 months (12 years).

###### _**Note:**_

*   Once you have calculated the values using data table, it can not be undone using Control + Z. You can however manually select all the values and delete it.
*   You can not delete/modify any one cell in the entire set of calculated values. Since this is an array, you will have to delete all the values.
*   You can do the same calculation by arranging the data horizontally. The only difference would be that you will have to use Row input cell in the data table dialogue box (instead of column input cell).

_**Download File.. Try it yourself**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/11/One-Variable-Data-Table-in-Excel.xls)

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Making Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [IRR Calculator Excel](https://trumpexcel.com/calculate-irr-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    
*   [How to Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Data Analysis \[Part 1 of 5\] – One Variable Data Table in Excel”
--------------------------------------------------------------------------------

1.  \=PMT(B2/12;B3;B1) Without comma. (excel 2007)
    
    [Reply](https://trumpexcel.com/one-variable-data-table-in-excel/#comment-1620)
    
    *   No…………. (with comma ,)
        
        [Reply](https://trumpexcel.com/one-variable-data-table-in-excel/#comment-13475)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/one-variable-data-table-in-excel/#respond)

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