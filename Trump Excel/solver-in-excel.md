# Data Analysis - Using Solver in Excel

**Source:** https://trumpexcel.com/solver-in-excel

---

[Skip to content](https://trumpexcel.com/solver-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/solver-in-excel/#below-title)

This is the fifth and final article of the five-part series on Data Analysis in Excel. In this section, I will show you how to use Solver in Excel.

**[Download Example File](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Solver-in-Excel.xls)
**

_**Other articles in this series:**_

*   [One Variable Data Table in Excel.](https://trumpexcel.com/one-variable-data-table-in-excel/)
    
*   [Two Variable Data Table in Excel.](https://trumpexcel.com/two-variable-data-table-in-excel/)
    
*   [Scenario Manager in Excel.](https://trumpexcel.com/scenario-manager-in-excel/)
    
*   [Goal Seek in Excel.](https://trumpexcel.com/goal-seek-in-excel/)
    

**Watch Video – Using Solver in Excel**

Solver in Excel is an add-in that allows you to get an optimum solution when there are many variables and constraints. You can consider it to be an advanced version of Goal Seek.

##### How to Find Solver Addin in Excel

Solver add-in is disabled in Excel by default. Here are the steps to enable it:

Here are the steps to enable it:

*   Go to File –> Options.
*   In the Excel Options Dialogue Box, select Add-in the left pane.
*   In the right pane, at the bottom, select Excel Add-ins from the drop down and click on Go..![Solver in Excel - Add Solver Add in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20309%2062'%3E%3C/svg%3E)
*   In the Add-ins dialogue box, you will see a list of available Add-ins. Select Solver Add-in and click OK.![Solver in Excel - Add Solver Add in and Click GO](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20351'%3E%3C/svg%3E)
*   This will enable the Solver Add-in. It will now be available in the Data Tab under Analysis group.

##### Using Solver in Excel – Example

Solver gives you the desired result when you mention the dependent variables and the conditions/constraints.

For example, suppose I have a data set as shown below.

![Solver in Excel - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20132'%3E%3C/svg%3E)

This example has manufacturing data for 3 widgets – Quantity, Price per Widget, and Overall Profit.

_**Objective**__**:**_ To get the maximum profit.

If you have an idea about manufacturing, you’d know you need to optimize the production to get the best output. While in theory you can manufacture unlimited quantities of the highest profit widget, there are always a lot of constraints under which you need to optimize the production.

_**Constraints**__**:**_ 

Here are a couple of constraints that you need to consider while trying to maximize the profit.

*   At least 100 Quantity of Widget A should be made.
*   At least 20 Quantity of Widget B should be made.
*   At least 50 Quantity of Widget C should be made.
*   A total of 350 widgets should be made.

This is a typical manufacturing optimization issue and you can be easily answer it using Solver in Excel.

##### Steps to Use Solver in Excel

*   Once you have the solver add-in activated (as explained above in this article), Go to Data –> Analysis –> Solver.![Solver in Excel - Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%2082'%3E%3C/svg%3E)
*   In the Solver Parameter dialogue box, use the following:![Solver in Excel - Solver Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20395'%3E%3C/svg%3E)
    1.  Set Objective: $D$5 (this is the cell which has the desired value – in this case, it is overall profit).
    2.  To: Max (since we want the maximum profit).
    3.  By Changing Variable Cells: $B$2:$B$4 (variables that we want to optimize – in this case, it’s the quantity).
    4.  Subject to the Constraints:
        *   Here you need to specify the constraints. To add a constraint, click on Add. In the Add Constraint dialogue box, specify the Cell Reference, the condition and the Constraint Value (as shown below):![Solver in Excel - Add a Constraint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20161'%3E%3C/svg%3E)
        *   Repeat this process for all the constraints.
    5.  Select a Solving Method: Select Simplex LP.
    6.  Click Solve
        *   In case solver finds a solution, this will open the Solver Result dialogue box. You can choose to keep solver solution (which you can see in your data set), or choose to revert back to the original values.
            *   You can also Save this as one of the scenarios, that can be used in the Scenario Manager.
            *   Along with this, you can also choose to create reports: Answer, Sensitivity, and Limits. Just select it and click OK. This will create different tabs with details one each for Answer, Sensitivity, and Limits (if you select only one or two, then that many tabs are created).![Solver in Excel - Create Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20306'%3E%3C/svg%3E)

With this article, I have tried to introduce you to Solver. There is much more that can be done, and if you are into statistics, I would recommend you go and read more about it. Here are a couple of good articles that I could find online:

*   [Using Solver in Excel – MS Help](http://blogs.office.com/2009/09/21/new-and-improved-solver/)
    .
*   [A handbook on using Solver in Excel (with examples)](http://excelmasterseries.com/D-_Loads/New_Manuals/Step-By-Step_Optimization_S.pdf)
    ).

_**Try it Yourself.. Download the File**_  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Solver-in-Excel.xls)

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
    
*   [How to Remove (Disable) Add-Ins in Excel](https://trumpexcel.com/remove-add-ins-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Data Analysis \[Part 5 of 5\] – Using Solver in Excel”
---------------------------------------------------------------------

1.  Nice article & I agree with Mark. Sumit can we find some practice exercises in Excel format for Solver as well as for Data Analysis.
    
    [Reply](https://trumpexcel.com/solver-in-excel/#comment-1646)
    
    *   Thanks Asif. Glad you like the article. I have provided one sample file for download in this article. I will create some more example files and share with you and the others.
        
        [Reply](https://trumpexcel.com/solver-in-excel/#comment-1647)
        
2.  Good Series of Articles. Solver is something not many people use, but I can see it can be useful in many cases.
    
    [Reply](https://trumpexcel.com/solver-in-excel/#comment-1643)
    
    *   Thanks Mark.. Glad you like like it.
        
        [Reply](https://trumpexcel.com/solver-in-excel/#comment-1644)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/solver-in-excel/#respond)

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