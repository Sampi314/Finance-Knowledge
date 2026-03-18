# How to Create a KPI Dashboard in Excel [Part 3 of 3]

**Source:** https://trumpexcel.com/kpi-dashboard-in-excel-part-3

---

[Skip to content](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#below-title)

**Watch Video – Creating KPI Dashboard in Excel – Part 3/3**

This is the third and final article of the three-part tutorial series on Creating a KPI Dashboard in Excel.

[Part 1: Creating a Dynamic Scatter Chart in Excel](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
  
[Part 2: Spotting the Data Point and Creating a Dynamic Interpretation for the Chart](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/)
  
Part 3: Extract List of Companies from the Scatter Chart + Company comparison( using Bullet Charts)

If you have followed [Part 1](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
 and [Part 2](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/)
 of this KPI Dashboard in Excel series, by now you would know how to create a dynamic [scatter chart](https://trumpexcel.com/scatter-plot-excel/)
, spot a data point in the chart, and create a dynamic interpretation for the chart. Something as shown below:

![KPI Dashboard in Excel - Dynamic Interpretation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20456'%3E%3C/svg%3E)

### KPI Dashboard in Excel – Part 3/3

In this final part of the series, I will show you:

*   How to extract a list of companies from a specific quadrant of the scatter chart
*   How to Insert a Dynamic Bullet Chart

**[Click here to download the dashboard](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel_Part-3.xlsx)
**

#### Extract List of Companies from the Scatter Chart

To extract the list of all the companies from a quadrant, we need to insert 5 radio buttons (four buttons for the four quadrants and one for getting all the companies)

###### Inserting Radio/Option Buttons

To insert a radio button:

*   Go to [Developer Tab](https://trumpexcel.com/excel-developer-tab/)
     –> Insert –> Form Controls –> Option Button.
*   Click anywhere on the worksheet and it would insert a radio button.
*   Right-click on the radio button and select Format Controls.
*   In the Format Control dialog box, specify a cell link (in this dashboard, I have linked it to cell B11 in the calculation sheet).
*   Rename the button text.

Follow the same steps (as mentioned above) to insert four more radio buttons. Note that you can only select one radio button at a time. All these radio buttons are linked to the same cell. When you select All, it returns the value 1 in the cell B11. When you select Top-Left button, it returns the value 2 and so on..

![KPI Dashboard in Excel - Radio Buttons](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%2054'%3E%3C/svg%3E)

###### Extracting Data based on Radio Button Selection

Based on the radio button selection, matching records are extracted. For example, if the Top-left radio button is selected, then all the companies in the top-left quadrant gets extracted. Below is the snapshot from the calculation worksheet showing how to set up and extract the data:

![KPI Dashboard - Radio Button Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20876%20459'%3E%3C/svg%3E)

This extracted data is now shown on the dashboard. Since all the data can not be shown in the dashboard at one go, I have inserted a scroll bar (to show 10 records at a time).

Here is a detailed tutorial on **[how to insert a scroll bar in Excel](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
.**

To make the dashboard more visually appealing and to increase the readability, I have created a [heat map](https://trumpexcel.com/heat-map-excel/)
 of the KPI values.

![KPI Dashboard in Excel - Heatmap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20246'%3E%3C/svg%3E)

#### Inserting a Dynamic Bullet Chart

Once we have the list of all the companies in a specific quadrant, the next logical step is too deep dive into company performance. A bullet chart can come in handy to show a comparison of the company’s KPIs versus peer average. As soon as the user selects a company (from the drop down), the bullet chart gets updated with selected companies KPI values.

Here is a step-by-step tutorial on how to create a **[bullet chart in excel](https://trumpexcel.com/bullet-chart-in-excel/)
.**

Here is how the final dashboard looks like:

![KPI Dashboard in Excel - Final](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20944%20468'%3E%3C/svg%3E)

_**Download the Full Dashboard  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel_Part-3.xlsx)
**_

_As a whole, this KPI dashboard in Excel enables a user to quickly segment a list of companies into quadrants (based on selected KPI values). The user can drill down further and focus on a specific quadrant by extracting the list of companies in that quadrant. He can further drill down to see how a company performs as compared to its peers on the KPIs._

As mentioned, I and my team have used this dashboard as a starting point to down-select accounts. So this has real world utility. Go ahead and use these techniques in creating awesome Excel Dashboards.

Also, take a minute and let me know what you think. Leave your thoughts in the comments section.Other

Learn to Create World-Class Dashboards in Excel. Join the **[Excel Dashboard Course](https://trumpexcel.com/excel-dashboard-course/)
**.

**Other Dashboard Tutorials:**

*   [Excel Dashboards – Examples, Best Practices & Resources](https://trumpexcel.com/creating-excel-dashboard/)
    .
*   [Game of Thrones Dashboard in Excel](https://trumpexcel.com/game-of-thrones-dashboard/)
    .
*   [Excel Dashboard: Premier League Season 2014-15 visualized](https://trumpexcel.com/excel-dashboard-epl-visualization/)
    .
*   [Call Center Performance Dashboard in Excel](https://trumpexcel.com/call-center-performance-dashboard-excel/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [How to Create a Drop-down in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [Adding and Using Checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Adding and Using Radio Buttons in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “KPI Dashboard in Excel \[Part 3 of 3\] – Extract List of Companies from the Scatter Chart”
----------------------------------------------------------------------------------------------------------

1.  Sumit,  
    Every one of your tutorials has been able to strengthen my ability to provide meaningful guidance to the decision makers at my firm. Additionally, they are fun and invigorating. Thank you for your amazing resources!!
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-11354)
    
2.  Thanks for this! Do you have an example of how to create the chart on the bottom right? Is it a template? Thanks!
    
    Edited – nevermind! Found it!
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-9506)
    
3.  Good day, How do i add other types of leaves for example my company has the following types leave  
    Annual Leave  
    Sick Leave  
    Maternity / Paternity Leave  
    Compassionate Leave  
    Time off  
    Unpaid leave
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-7716)
    
4.  Hi Sumit, i need an help even i created a similar kind of chart to display product name and Add to bag % and my question here is i created a scatter chart with 4 list box for Quadrants to show the product names and when someone select a product in the list box that data point is highlighted in the chart but management team want when someone select the data point in the graph it should highlight that particular product name in the list box and also it should show the product name in the selected data point in the graph. is this possible? if so can you please let me know how this can achieved.
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-3154)
    
    *   Hello Nandish.. I am afraid I don’t know how to do this. When I was creating this dashboard for the management in my company, this was one of the things they asked for. I tried but it gets overly complicated and had to give it up. This is the reason I created the way to spot the data point feature in the dashboard.
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-3155)
        
5.  Hello Sumit, your work is AWESOME. It is unbelievable how you use your knowledge in the creation of this Master Pieces. I have a question. Do you know how to create the extrapolation model (formula for forecasting) for “Fan Charts”? Or how to get something like what the prediction check mark does on the Google Trend charts? Thank you again!
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2480)
    
6.  This is great stuff! Thanks!
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2407)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2411)
        
7.  Thanks so much for this 3 part tutorial. I have gradually being working through it as time permits. As someone who has used Excel since it’s first release (Lotus 1-2-3 and Multiplan before that) I find you presentations informative and easy to follow.
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2330)
    
    *   Thanks for commenting Chris.. Glad you like the tutorial 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2410)
        
8.  Great Job. Sumit, You are very specialist in create dashboard. Congrats
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2291)
    
    *   Thanks for the kind words Pablo 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2293)
        
9.  Love the dashboard. It makes a lot of business sense. I will try and customize it to use for some KPI tracking that I do. Thanks for sharing
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2288)
    
    *   Thanks for commenting Jon.. Do let me know what you come up with 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#comment-2292)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/#respond)

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