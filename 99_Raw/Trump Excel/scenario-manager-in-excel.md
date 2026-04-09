# Data Analysis - Scenario Manager in Excel

**Source:** https://trumpexcel.com/scenario-manager-in-excel

---

[Skip to content](https://trumpexcel.com/scenario-manager-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/scenario-manager-in-excel/#below-title)

This is the third article of the five-part series on Data Analysis in Excel. In this section, I will show you how to use the Scenario Manager in Excel.

**[Download File](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Scenario-Manager.xlsx)
**

_**Other articles in this series:**_

*   [One Variable Data Table in Excel.](https://trumpexcel.com/one-variable-data-table-in-excel/)
    
*   [Two Variable Data Table in Excel](https://trumpexcel.com/two-variable-data-table-in-excel/)
    .
*   [Goal Seek in Excel](https://trumpexcel.com/goal-seek-in-excel/)
    .
*   [Excel Solver](https://trumpexcel.com/solver-in-excel/)
    .

**Watch Video – Scenario Manager in Excel**

Scenario Manager in Excel can be the tool of choice when you have multiple variables, and you want to see the effect on the final result when these variables change.

Suppose you have a dataset as shown below and you want to calculate the profit value:

![Scenario Manager in Excel - Data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20151'%3E%3C/svg%3E)

The Profit value is dependent on 3 variables – Sale Quantity, Price per Unit, and the Variable Cost per Unit. Here is the formula I have used to calculate the profit:

\=B2\*B3-B4-B5\*B2

The idea is to see how this final result changes when we change these dependent variables.

As shown in the first 2 articles of this series, if you only have one or two variables changing, you can create one variable or two-variable data table. But if you have 3 or variables that can change then scenario manager is the way to go.

Setting up Scenario Manager in Excel
------------------------------------

*   Go to Data Tab –> Data Tools –> What-If Analysis –> Scenario Manager.![Accessing Scenario Manager in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20200'%3E%3C/svg%3E)
*   In the Scenario Manager dialogue box, click on Add.![Scenario Manager in Excel - Add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20292'%3E%3C/svg%3E)
*   In the Add Scenario dialogue box, fill in the following details:
    *   Scenario name: Worst Case
    *   Changing cells: $B$2,$B$3,$B$5 (you can also select it by pressing the CONTROL button and using mouse left-click).
    *   Comment: Any comment you wish you add. You can also leave this blank.![Scenario Manager in Excel - Add a Scenario Details](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20338'%3E%3C/svg%3E)
*   Click OK. This opens the Scenario Values dialogue box.
*   In the Scenario Values dialogue box, fill in the following values (since this is the worst case scenario, enter the values accordingly). _If you create names for each cell, that name is visible instead of the cell address_:
    *   $B$2: 50
    *   $B$3: 30
    *   $B$4: 30![Scenario Manager in Excel - Scenario Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20179'%3E%3C/svg%3E)
*   Click OK (Click on Add if you want to add another scenario).

This creates the Worst Case scenario for this data set. You can similarly follow these steps and create multiple scenarios (for example, Worst Case, Realistic, Best Case).![Scenario Manager in Excel - Added Scenarios](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20276%20278'%3E%3C/svg%3E)

Once you have created all the scenarios, you can view the result from each of the scenarios by simply double-clicking on any of the scenarios. As you double click, the values would change based on that scenario.

Additionally, you can also _**create a summary of all the scenarios.**_

Create a Summary of all the Scenarios
-------------------------------------

*   Click on the Summary button in the Scenario Manager dialogue box.![Scenario Manager in Excel - Summary Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20372'%3E%3C/svg%3E)
*   In the Scenario Summary dialogue box, select Scenario Summary or Pivot Table (these are the 2 ways to show summary). Also specify the Result cells (the cell where you have the output of this calculation; B6 in this example)![Scenario Manager in Excel - Scenario Summary OPtions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20189'%3E%3C/svg%3E)
*   Click OK. Instantly a new tab is created with the summary of all the three scenarios.![Scenario Manager in Excel - Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20257'%3E%3C/svg%3E)

Scenario manager in Excel is a great tool when you need to do sensitivity analysis. Simply create scenarios and a summary can be generated instantly, giving you a complete comparative overview.

_**Download File… Try it yourself[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/12/Data-Analysis-Scenario-Manager.xlsx)
**_

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Making Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “Data Analysis \[Part 3 of 5\] – Scenario Manager in Excel”
--------------------------------------------------------------------------

1.  A greatful thanks to you,  
    For giving this types of excel knowledge.
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-14778)
    
2.  Hi, I have a simple but important question.
    
    I’m trying to link and automate the scenario values. Instead of feeding it generic values, I’m using a cell reference, it works (instead of “50”, I’m using “=A1”). However, the values from that cell reference are being fixed and will not update when I change the scenario values in those cells.
    
    The problem is once I give it the cell reference as input, e.g. = A1, it takes the generic value inside A1 and fixes it as the scenario figure. When I manually modify this value in A1, the scenario doesn’t update because it’s no longer referring to the cell A1.
    
    Any ideas?
    
    Thanks.
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-14300)
    
3.  Thanks I got it interesting
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-14265)
    
4.  Is it possible to do a forward looking analysis with is excel tool?
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-9444)
    
5.  Sumit, Thanks for the presentation.
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-9443)
    
6.  Hello
    
    I am Fredrick from Ghana
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-9442)
    
7.  Thank you Sumit. great to learn 😀
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-1634)
    
    *   Thanks for commenting hubert.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-2353)
        
8.  Good article. Now I know how I can do some sensitivity analysis in Excel. Keep up the good work.
    
    [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-1632)
    
    *   Thanks for commenting Ryan.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/scenario-manager-in-excel/#comment-2352)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/scenario-manager-in-excel/#respond)

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