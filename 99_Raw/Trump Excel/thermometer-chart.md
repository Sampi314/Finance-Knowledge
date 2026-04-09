# How to Create a Thermometer Chart in Excel

**Source:** https://trumpexcel.com/thermometer-chart

---

[Skip to content](https://trumpexcel.com/thermometer-chart/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/thermometer-chart/#below-title)

**Watch Video – Creating Thermometer Chart in Excel**

Thermometer chart in Excel could be a good way to represent data when you have the actual value and the target value.

A few scenarios when where it can be used is when analyzing sales performance of regions or sales rep, or employee satisfaction ratings vs the target value.

![Thermometer Chart in Excel - Final Product](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20179%20414'%3E%3C/svg%3E)

In this tutorial, I will show you the exact steps you need to follow to create a thermometer chart in Excel.

**[Click here to download the example file and follow along](https://www.dropbox.com/s/035yl0rk73ux0gm/Thermometer%20Chart.xlsx?dl=0)
**.

Creating Thermometer Chart in Excel
-----------------------------------

Suppose you have the data as shown below for which you want to create a chart to show the actual value as well as where it stands as compared with the target value.

![Dataset for Thermometer graph in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20214%20467'%3E%3C/svg%3E)

In the above data, the Achieved% is calculated using the Total and Target values (Total/Target). Note that the Target percentage would always be 100%.

Here are the steps to create a thermometer chart in Excel:

1.  Select the data points![Select the data points to create a thermometer chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20226%2082'%3E%3C/svg%3E).
2.  Click the Insert tab.![Thermometer Chart in Excel - Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20193'%3E%3C/svg%3E)
3.  In the Charts group, click on the ‘Insert Column or Bar chart’ icon.![Thermometer Chart in Excel - Insert Column or Bar chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20129'%3E%3C/svg%3E)
4.  In the drop-down, click the ‘2D Clustered Column’ chart. This would insert a Cluster chart with 2 bars (as shown below).![Thermometer Goal Chart in Excel - inserting a 2D column chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20638'%3E%3C/svg%3E)
5.  With the chart selected, click the Design tab.![Thermometer Chart in Excel - Design Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20254%20133'%3E%3C/svg%3E)
6.  Click on Switch Row/Column option. This will give you the resulting chart as shown below.![Thermometer Chart in Excel - Switch row column with chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20549'%3E%3C/svg%3E)
7.  Right-click on the second column (orange column in this example) and select format data series.![Thermometer Chart in Excel - Format Data Series target column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20399'%3E%3C/svg%3E)
8.  In the Format Data Series task pane (or dialog box if you are using Excel 2010 or 2007), select [Secondary Axis](https://trumpexcel.com/add-secondary-axis-charts/)
     in Series Options. This will make both the bars align with each other.![Thermometer Chart in Excel - secondary Axis with chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20770'%3E%3C/svg%3E)
9.  Note that there are two vertical axes (left and right), with different values. Right-click on the vertical axis on the left and select format axis. ![Thermometer Chart in Excel - format axis left side one](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20414'%3E%3C/svg%3E)
10.  In the Format Axis task pane, change the maximum bound value to 1 and minimum bound value to 0. Note that even if the value is already 0 and 1, you should still manually change this (so that you see the Reset button on the right).![Minimum and Maximum bound for left axis - Thermometer goal chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20277'%3E%3C/svg%3E)
11.  Delete the axis on the right (select it and hit the delete key).
12.  Right-click on the column visible in the chart, and select format data series.![Thermometer Chart in Excel - Format Data Series Fill and Border settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20386'%3E%3C/svg%3E)
13.  In the format data series, make the following
    *   Fill: No Fill
    *   Border: Solid Line (choose the same color as that of actual value bar)![Fill and Border color for the thermometer goal chart generator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20610'%3E%3C/svg%3E)
14.  Delete the chart title, grid lines, the vertical axis on the right, and horizontal (category) axis, and the legend. Also, resize the chart to make it look like a thermometer.![Thermometer Chart in Excel - ready to measure goals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20284%20369'%3E%3C/svg%3E)
15.  Select the vertical axis on the left, right-click on it and select ‘Format Axis’.![Format Axis in left vertical axis tick marks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20293%20408'%3E%3C/svg%3E)
16.  In Format Axis task pane, select Major Tick Mark Type as Inside.![Major tick mark type as inside](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20347'%3E%3C/svg%3E)
17.  Select the chart outline, right-click and select Format Chart Area.![Format Chart Area for a thermometer goal graph in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20557'%3E%3C/svg%3E)
18.  In the task pane, make the following selection
    *   Fill: No Fill
    *   Border: No Line![Format Chart Area for a thermometer graph in Excel - fill and border](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20455'%3E%3C/svg%3E)
19.  Now click the Insert tab and insert a circle from the Shapes drop-down. Give it the same color as thermometer chart and align it to the bottom.![Oval Shape for thermometer bottom](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20231'%3E%3C/svg%3E)

That’s it! Your Thermometer chart is ready to measure.

_**Download Thermometer Chart Example File  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/035yl0rk73ux0gm/Thermometer%20Chart.xlsx?dl=0)
**_

Note: The thermometer chart is useful when you have one actual value and target value set. In case you have multiple such datasets, you either need to create multiple such thermometer charts, or need to use a different chart type (such as the [Bullet chart](https://trumpexcel.com/bullet-chart-in-excel/)
 or the [Actual Vs. Target charts](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
).

**You May Also Like the Following Excel Tutorials:**

*   [Creating a Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [How to Make a Bell Curve in Excel (Step-by-step Guide)](https://trumpexcel.com/bell-curve/)
    .
*   [Step Chart in Excel – A Step by Step Tutorial](https://trumpexcel.com/step-chart-in-excel/)
    .
*   [How to Make a Histogram in Excel (Step-by-Step Guide)](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Creating a Heatmap in Excel](https://trumpexcel.com/heat-map-excel/)
    .
*   [Area Chart in Excel](https://trumpexcel.com/area-chart/)
    .
*   [10 Advanced Excel Charts that You Can Use In Your Day-to-day Work](https://trumpexcel.com/advanced-charts/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “How to Create a Thermometer Chart in Excel”
----------------------------------------------------------

1.  Hi, thank you for this information. I am having trouble finding the secondary axis in order to align the column bars (Step 7 & 8). I am using google sheets and am wondering how to execute this using google sheets program and if there is an alternative way to get these steps done. Would really appreciate the help, thank you!
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-14759)
    
2.  Amazing
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-13098)
    
3.  Awesome! Thanks a bunch!
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-12326)
    
4.  Thanks for these explanations. It was very helpful!!!
    
    @mecoinst
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-10965)
    
5.  Thank You.I created a thermometer chart by reading your tutorial and in our office they are still using this daily for tracking teams score.Thank You so much.
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-10597)
    
6.  Thank you for this great tutorial! I was able to create the thermometer for tracking out team’s giving. Thank you for providing a great resource.
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-9385)
    
7.  Hi Sumit,
    
    I am attempting to modify this and changed the axis range to 7000. Every month, for the next 36 months I will be adding approx. 200. By the end of 36 months the thermometer should reach the target. I want be able to enter a value (that I am adding monthly) in a cell and also on another cell to show a cumulative running total of how much I’ve added. How do I do this?
    
    Thanks,  
    Jay.
    
    [Reply](https://trumpexcel.com/thermometer-chart/#comment-3105)
    
    *   Hello.. In this case, make the target value (in B3) 7000 and for actual value (in A3) use the formula =SUM(A5:A41) – assuming that the you’ll be entering the monthly values in A5:A41. Now, the cumulative sum would be reflected in A3 and the thermometer chart would work.
        
        [Reply](https://trumpexcel.com/thermometer-chart/#comment-3132)
        
        *   That was not the way I quite wanted, however I figured out a fancier way from searching the web for tips.
            
            The data entry part is in a separate tab sheet where I have a table with the date, amt. paid, and sum. (A1 to C1). In another cell, G2 I have an array formula =OFFSET(Data,ROWS(Data)-1,2), which gives the cummulative total from the table. I have a defined name data for the table to automatically expand as I enter data: =OFFSET(Data!$A$1:$C$1,0,0,COUNT(Data!$A:$A)+1) .
            
            The actual value in the chart sheet (A3) is a named referenced cell to the data sheet G2.
            
            Works like a charm!
            
            Jay.
            
            [Reply](https://trumpexcel.com/thermometer-chart/#comment-3143)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/thermometer-chart/#respond)

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