# How to Create a KPI Dashboard in Excel [Part 2 of 3]

**Source:** https://trumpexcel.com/kpi-dashboard-in-excel-part-2

---

[Skip to content](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#below-title)

**Watch Video – Creating KPI Dashboard in Excel – Part 2/3**

This tutorial is a part of a three-part Excel KPI Dashboard tutorial series:

*   [KPI Dashboard in Excel – Part 1: Dynamic Scatter Chart.](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
    
*   _KPI Dashboard in Excel – Part 2: Dynamic Interpretation._
*   [KPI Dashboard in Excel – Part 3: Dynamic Data Extraction + Bullet Chart](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/)
    .

In the [previous article](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
 of this 3 part ‘KPI Dashboard in Excel’ series, we learned how to create a dynamic scatter chart.

Something as shown below:

![KPI Dashboard in Excel - Scatter Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20344'%3E%3C/svg%3E)

### KPI Dashboard in Excel – Part 2/3

In this article, I will show you:

*   How to highlight a company in the chart when you select its name
*   How to create a dynamic interpretation from the Chart for the selected company

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel-Part-2.xlsx)
**

##### Highlighting the Selected Company in the Scatter Chart

To enable this, we need to create a drop down with the names of all the companies. Something as shown below:

![KPI Dashboard in Excel - Drop Down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20148'%3E%3C/svg%3E)

This [drop-down](https://trumpexcel.com/excel-drop-down-list/)
 in Excel can be made using the data validation feature. Once we have the drop-down list in place, we need to add a new series to the [scatter chart](https://trumpexcel.com/scatter-plot-excel/)
 such that the company’s data point gets highlighted when we select the company from the drop down. Something as shown below:

![KPI Dashboard in Excel - Spot the data in the scatter chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20496'%3E%3C/svg%3E)

To create this, we need to plot another series that has only one data point (for the company that we select). Here is a detailed tutorial on how to make it – **[Spot Data Point in Excel Scatter Chart](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/)
.**

Once you have the chart in place, next step is to create the dynamic interpretation for the selected company.

##### Dynamic Interpretation of a Data Point in the Chart

This idea came to me when I was working with a few sales guys in my previous organization. We had created a KPI Dashboard in Excel which had a similar dynamic scatter chart that also highlighted the selected company’s data point.

While the chart and the highlighted data point was a good visualization, some still struggled to quickly interpret the chart. To address this, we came up with the dynamic interpretation feature.

This dynamic interpretation feature lets you dynamically show the text that describes the chart insights in words. Something as shown below:

![KPI Dashboard in Excel - Dynamic Interpretation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20456'%3E%3C/svg%3E)

While I have used generic KPI names, a good example could be to show Profit Vs Cost chart, where the interpretation could be – _“Despite mounting costs, Com 1 was able to increase its margins”_ OR _“Rising Costs lead to a decline in profitability for Com 1”_

To create this, we need to create dynamic text for all the 4 quadrants. For example, for the bottom left quadrant (X-axis value < 50% and Y-axis value < 50%), the text would be “Com 1 Lags in Both the KPIs”. Similarly, we need to create text for all the four quadrants. Here the company name and KPI names would be the ones that are selected by the user.

![KPI Dashboard in Excel - Dynamic Interpretation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%2093'%3E%3C/svg%3E)

A data point plotted on the scatter chart would lie in any one of the four quadrants. All we need to do now is check the X and Y axis values for a company and select the text from the matching quadrant. For example, if X and Y axis values both are less than 50%, then it is bottom left quadrant, and so on…

Based on the quadrant the relevant text is selected and linked to the text box in the dashboard.

_**Download the File and Try it yourself  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel-Part-2.xlsx)
**_

In the [next and final part of this series](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/)
, I will show you how to extract the list of companies based on their position on the scatter chart (by quadrants), and also [create a bullet chart](https://trumpexcel.com/bullet-chart-in-excel/)
 to show company level performance against peers.

In the meantime, let me know what you think? Leave your thoughts in the comments section.

Stay Tuned 🙂

Learn to Create World Class Dashboards in Excel. Join the **[Excel Dashboard Course](https://trumpexcel.com/excel-dashboard-course/)
**.

**Other Dashboard Tutorials:**

*   [Excel Dashboards – Examples, Best Practices & Resources](https://trumpexcel.com/creating-excel-dashboard/)
    .
*   [Game of Thrones Dashboard in Excel](https://trumpexcel.com/game-of-thrones-dashboard/)
    .
*   [Excel Dashboard: Premier League Season 2014-15 visualized.](https://trumpexcel.com/excel-dashboard-epl-visualization/)
    
*   [Call Center Performance Dashboard in Excel](https://trumpexcel.com/call-center-performance-dashboard-excel/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [Adding and Using Checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Adding and Using Radio Buttons in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .
*   [Creating Heat Maps in Excel](https://trumpexcel.com/heat-map-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “KPI Dashboard in Excel \[Part 2 of 3\] – Dynamic Interpretation from Scatter Chart”
--------------------------------------------------------------------------------------------------

1.  I really love your way of teaching, thank you so much. Can I ask how did put that cross on the chart? Did you use ‘insert, shape’?
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#comment-2689)
    
2.  I cannot wait for Part 3 🙂
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#comment-2287)
    
    *   Thanks for commenting Leanne. Part 3 is available here – [http://trumpexcel.com/2015/07/kpi-dashboard-in-excel-part-3/](http://trumpexcel.com/2015/07/kpi-dashboard-in-excel-part-3/)
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#comment-2345)
        
3.  Sumit – I love this idea of dynamic interpretation. It so cool. Look forward to the last part
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#comment-2280)
    
    *   Thanks for commenting Phil.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#comment-2283)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/#respond)

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