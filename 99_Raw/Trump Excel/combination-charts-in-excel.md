# How to Create Combination Charts in Excel - Step-by-Step Tutorial

**Source:** https://trumpexcel.com/combination-charts-in-excel

---

[Skip to content](https://trumpexcel.com/combination-charts-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combination-charts-in-excel/#below-title)

Combination charts in Excel let you present and compare two different data-sets that are related to each other (in a single chart).

When you create a regular chart in Excel, it usually has only one X-axis and one Y-axis. But with combination charts, you can have two Y-axis, which allows you to have two different type of data points in the same chart.

For example, you may be interested in plotting the annual revenue numbers of a company, and at the same time, also be able to show how the profit margin has changed.

A combination chart (as shown below) is a good way of doing this in Excel.

![Combination Charts in Excel - final result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20697%20427'%3E%3C/svg%3E)

You can see that a revenue number are in thousands and are way higher than the profit margin numbers (which is in %). By [adding a secondary Y-axis](https://trumpexcel.com/add-secondary-axis-charts/)
, we can plot the profit margin numbers separately (and still be able to plot both in the same chart).

Creating a Combination Chart in Excel 2013/2016
-----------------------------------------------

Suppose I have the data set as shown below and I want to plot both the revenue and profit margin numbers in the same chart.

![Combination Charts in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20226'%3E%3C/svg%3E)

To create this combination chart, I first need to create a regular chart where I have all the above data plotted on it.

Below are the steps to create a regular chart using the above data (the snapshots are of Excel 2016):

1.  Select the Revenue and Profit Margin data (B1:C6 in this example).
2.  Click the Insert tab.![Combination Charts in Excel - Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20432%20198'%3E%3C/svg%3E)
3.  In the Charts group, click on the ‘Insert Column Chart’ icon.![Combination Charts in Excel - Insert Column or Bar Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20136'%3E%3C/svg%3E)
4.  Click on Clustered Column chart. This will insert the chart in the worksheet area.![Excel Combination Charts - click on clustered column chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20500'%3E%3C/svg%3E)
5.  With the Chart Selected, go to the Design tab and click on Select Data.![Combo Charts in Excel - click on Select Data in Design tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20177'%3E%3C/svg%3E)
6.  In the ‘Select Data Source’ dialog box, click on Edit option (below the ‘Horizontal (Category) Axis Labels’).![Combo Charts in Excel - click on Edit button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20712%20406'%3E%3C/svg%3E)
7.  Select years that you want to plot in the chart (A2:A6 in this example).
8.  Click OK.

The above steps would give you a chart that has revenue and profit margin plotted as a clustered column chart. If you can’t see the Profit Margin bar in the chart, it’s because the value of Profit Margin is very less as compared to the Revenue value (but it’s there as we can see it’s listed in the legend in orange color).

![Regular clustered column Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20366'%3E%3C/svg%3E)

Now to create a combination chart from this clustered column chart, follow the below steps:

1.  Right-click on any of the bars.
2.  Click on ‘Change Series Chart Type’.![Change Series chart type to create a combo chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20796%20485'%3E%3C/svg%3E)
3.  In the Change Chart Type dialog box, make sure Combo category is selected (which it should be by default).![Combo is selected in the dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20473'%3E%3C/svg%3E)
4.  Click on the drop-down for Profit Margin.![Click the profit margin drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20517%20167'%3E%3C/svg%3E)
5.  In the drop-down, click on ‘Line with Markers’.![Combo chart - line with markers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20509'%3E%3C/svg%3E)
6.  Check the Secondary Axis checkbox for Profit Margin.![Plot line with markers on a secondary axis to make it a combo chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20139'%3E%3C/svg%3E)
7.  Click OK.

The above steps would give you the combination chart (also called combo chart) as shown below.

![Combination Chart in Excel - final result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20472'%3E%3C/svg%3E)

You can now further customize the chart (such as change the title, remove the grid lines, etc.)

Another good use case of creating combination charts is when you have to show actual vs target values in the same chart. You can create a simple clustered column chart, or create something more fancy by converting one bar into markers. Click here to read how to create an [Actual vs Target](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
 combination charts in Excel.

Creating Combination Charts in Excel 2010
-----------------------------------------

While the first part of creating a chart is the same in all versions of Excel, converting that chart into a combination chart is done a bit differently in Excel 2010.

Below are the steps to convert a regular clustered column chart into a combo chart in Excel 2010:

1.  Click on any of the Profit margin bars. This will select all bars for profit margin.
2.  Right-click and select Format Data Series.

![Combination Charts in Excel - Select Format Data Series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20352%20347'%3E%3C/svg%3E)

1.  In the Format Data Series dialogue box, select Secondary Axis (in the Plot Series On group)
    *   This will plot Profit Margin Data in a secondary Axis. You would be able to see a vertical axis on the right of the chart.

![Combo Charts in Excel - Secondary Axis Selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20225'%3E%3C/svg%3E)

1.  Right-click and select Change Series Chart Type

![Combination Charts in Excel - Select Change Series Chart Type Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20353%20308'%3E%3C/svg%3E)

1.  In the Change Chart Type dialogue box, select Line with Markers option.

![Combination Charts in Excel - Select Different chart Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20242'%3E%3C/svg%3E)

1.  That’s It. You would have the chart. Format it the way you want.

**You May Also Like the Following Excel Charting Tutorials:**

*   [Creating Combination charts using Checkboxes](https://trumpexcel.com/dynamic-excel-chart-check-box/)
    .
*   [Creating Actual vs Target Chart in Excel](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    .
*   [How to Make a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Creating a Pareto Chart in Excel.](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    .
*   [Excel Sparklines – A Complete Guide](https://trumpexcel.com/sparklines/)
    
*   [Area Chart in Excel](https://trumpexcel.com/area-chart/)
    .
*   [Add a Trendline in Excel Charts](https://trumpexcel.com/trendline/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Create Combination Charts in Excel – Step-by-Step Tutorial”
---------------------------------------------------------------------------------

1.  Didn’t help. I need to do this in 2013 and there is no way to do combo graphs in Excel 2013
    
    [Reply](https://trumpexcel.com/combination-charts-in-excel/#comment-13385)
    
2.  Very fine
    
    [Reply](https://trumpexcel.com/combination-charts-in-excel/#comment-11840)
    
3.  can you give me online classes for graphs
    
    [Reply](https://trumpexcel.com/combination-charts-in-excel/#comment-11044)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/combination-charts-in-excel/#respond)

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