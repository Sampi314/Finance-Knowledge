# How to Create 100% Stacked Bar Chart in Excel

**Source:** https://trumpexcel.com/stacked-bar-chart-in-excel

---

[Skip to content](https://trumpexcel.com/stacked-bar-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/stacked-bar-chart-in-excel/#below-title)

A colleague asked me if there was a way to create a dynamic in-cell 100% stacked bar chart in Excel for three product sales.

As usually is the case, there were thousands of rows of data. There is no way she could have used Excel in-built charts as that would have taken her ages to create charts for each set of data points.

This got me thinking, and fortunately, [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 came to the rescue. I was able to quickly create something neat that fits the bill.

##### Creating a 100% Stacked Bar Chart in Excel

Suppose you have sales data for 12 months for three products (P1, P2, and P3). Now you want to create a 100% stacked bar chart in Excel for each month, with each product highlighted in a different color.

Something as shown below:

![Stacked Bar Chart in Excel - 100 percent stacked bar chart in excel data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20289'%3E%3C/svg%3E)

**Download the Example file**_**  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dynamic-100-percent-Stacked-Bar-Chart-using-CF.xls)
  
**_

##### **How to create this:**

First, you need to [calculate the percentage](https://trumpexcel.com/calculate-percentages-excel/)
 breakup for each product for each month (_I was trying to make a 100% stacked chart remember!!_).

To do this, first create three helper columns (each for P1, P2, and P3) for all the 12 months. Now simply calculate the % value for each product. I have used the following formula:

\=(C4/[SUM](https://trumpexcel.com/excel-sum-function/)
($C4:$E4))\*100)

![Stacked Bar Chart in Excel - helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20285'%3E%3C/svg%3E)Once you have this data in place, let’s dive in right away to make the stacked chart

1.  Select 100 columns and set their column width to **0.1.**
2.  Select these 100 cells in the first data row (K4:DF4) in this case.
3.  Go to Home –> Conditional Formatting –> New Rule.
4.  In New Formatting Rule Dialogue box, click on ‘Use a formula to determine which cells to format’ option.![stacked bar chart in excel CF Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20271'%3E%3C/svg%3E)
5.  In the ‘Edit the Rule Description’ put the following formula and set the formatting to Blue (in ‘Fill’ tab)

\=[COLUMNS](https://trumpexcel.com/excel-columns-function/)
($K$4:K4)<=$G4

![stacked bar chart in excel - Conditional Formatting DB](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20338'%3E%3C/svg%3E)

1.  Now again select the same set of cells and go to Home – Conditional Formatting – **Manage Rules**. Click on New Rule tab and again go to ‘Use a formula to determine which cells to format’ option. Now put the formula mentioned below and set the formatting to green color.

\=AND(COLUMNS($K$4:K4)>$G4,COLUMNS($K$4:K4)<=($G4+$H4))

1.  And finally again repeat the same process and add a third condition with the following formula and set the formatting to orange color.

\=AND(COLUMNS($K$4:K4)>($G4+$H4),COLUMNS($K$4:K4)<=100)

1.  Now click Ok and you would get something as shown below:

![100 percent stacked bar chart in excel final](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20288'%3E%3C/svg%3E)Hide the helper columns, and you have your dynamic 100% stacked bar chart ready at your service.

Now it’s time to bask in the glory and take out some time to brag about it ![;)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2015%2015'%3E%3C/svg%3E)

_**Try it yourself.. Download the Example file from here  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dynamic-100-percent-Stacked-Bar-Chart-using-CF.xls)
**_

**If you have enjoyed this tutorial, you might also like these:**

*   [Creating a Sales funnel chart in Excel](https://trumpexcel.com/sales-funnel-chart-in-excel/)
    .
*   [Creating a Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [Creating a dynamic Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Step Chart in Excel – A Step by Step Tutorial](https://trumpexcel.com/step-chart-in-excel/)
    .
*   [Creating Heat Map in Excel Using Conditional Formatting](https://trumpexcel.com/heat-map-excel/)
    .
*   [How to Quickly Create a Waffle Chart in Excel](https://trumpexcel.com/waffle-chart-excel/)
    .
*   [Excel Sparklines – A Complete Guide](https://trumpexcel.com/sparklines/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “Conditional Formatting to Create 100% Stacked Bar Chart in Excel”
---------------------------------------------------------------------------------

1.  It’s an ingenious solution and mr. TrumpExcel is the master of such hacks. The math baffles me, but I managed to get it working on columns just by adding another helper column and including it into the calculations such as the part with +.
    
    While working on it be careful cos the $K$4:K4 part seems to change all of a sudden while adding the other conditional formatting rules, so you need to check back at end for any such seemingly random changes that may have occurred.
    
    Next process is to try and figure out how to make this with just 10 columns, cos 100 columns is insane and may slow down a huge worksheet…
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-13445)
    
    *   …get it working on 4\* columns…
        
        [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-13446)
        
2.  Hi, We have this in an excel report but left to right scrolling becomes difficult as there are 100 columns. Is there a different way to do it without 100 columns?
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-12344)
    
    *   do with 10 columns. Most can probably do without such a high precision in the chart.
        
        [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-13444)
        
3.  Is there a quick way to “select 100 columns”?
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-10894)
    
4.  HI Summit
    
    Can you help me understating the Formulas and the results — I am not getting the logics and not the reaching the solution too.
    
    \=COLUMNS($K$4:K4) no of columns =1 which is less than or equal to Cell g4  
    \=AND(COLUMNS($K$4:K4)>$G4,COLUMNS($K$4:K4)($G4+$H4),COLUMNS($K$4:K4)<=100 ???
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-9571)
    
5.  I need a stacked data bar that is in-cell. Doesn’t need to be 100% Can you help?
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1996)
    
6.  Can you explain the COLUMNS function a little bit, please? Why do you start at row 9?
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1553)
    
    *   Hi Amanda.. Here is a video tutorial on COLUMNS function – [http://trumpexcel.com/learn-excel/excel-formulas/columns/](http://trumpexcel.com/learn-excel/excel-formulas/columns/)
        
        Hope this helps!
        
        [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1559)
        
7.  Really cool idea and implementation!
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1548)
    
8.  Thank you for an excellent written tutorial! I was wondering if this can also be realised when you have more than 3 ‘Sales’ columns. Would you happen to have an example with 5 or 7 cells? Thanks a lot!
    
    [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1341)
    
    *   Thanks Candrex. Glad you like it. This would work more than 3 columns as well. You can follow the same process with 5 or more columns, where you will have to put in 5 (or more) conditions with different colors.
        
        I don’t have a ready format for more than 3 columns, but if you get stuck, feel free to comment and I can help you out.
        
        [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-1342)
        
        *   Yeah that was very easy to put another column. Just had to add another + calculation after the others. I also made the last column data =100-G4-H4 and to show it as white, so now it looks rather like data bars all ending at different lengths.
            
            Actually if you’ve got little time I’d (and probably a few others) would need help converting this into just 10 columns, cos 100 is just too much processing power. The loss in accuracy is not an issue.
            
            [Reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#comment-13447)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/stacked-bar-chart-in-excel/#respond)

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