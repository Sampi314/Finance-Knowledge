# Creating Key Performance Indicator (KPI) Dashboard in Excel [Part 1/3]

**Source:** https://trumpexcel.com/kpi-dashboard-in-excel-part-1

---

[Skip to content](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#below-title)

**Watch Video – Creating KPI Dashboard in Excel – Part 1/3**

Learn the exact steps I take to create World Class Dashboards in Excel. Join the **[Excel Dashboard Course](https://trumpexcel.com/excel-dashboard-course/)
**.

A Key Performance Indicators ([KPI](https://en.wikipedia.org/wiki/KPI)
) dashboard is one of the most used dashboards in business.

Its primary objective is to show the performance of key KPIs and provide a comparative view of other KPIs or companies.

In this tutorial, I will show you how to create a KPI dashboard in Excel.

This is an improved version of a dashboard that I created last year in my previous job role as a financial/data analyst.

I have broken down this Excel KPI Dashboard tutorial into three parts:

*   _KPI Dashboard in Excel – Part 1: Dynamic Scatter Chart._
*   [KPI Dashboard in Excel – Part 2: Dynamic Interpretation.](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/)
    
*   [KPI Dashboard in Excel – Part 3: Dynamic Data Extraction + Bullet Chart](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/)
    .

Objective: We have the KPI data of 100 companies, and the objective is to create a dashboard that would help in identifying key accounts based on the performance. Apart from a comparative view, it should also enable the user to drill down on individual companies.

KPI Dashboard in Excel – Part 1/3
---------------------------------

Let me first show you how the final KPI dashboard looks like:

![KPI Dashboard in Excel - Description](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20709%20417'%3E%3C/svg%3E)

In this Key Performance Indicator (KPI) dashboard, a user can select the KPIs that he/she needs to compare. It would instantly update the scatter chart with a spread of all the 100 companies across the four quadrants. It is a great way to segment companies based on performance.

At the top-right (of the dashboard), a user has the option-buttons to select a quadrant and get a list of all the companies in that quadrant.

Below it, there is a [bullet chart](https://trumpexcel.com/bullet-chart-in-excel/)
 that shows the KPIs Vs. Peer Average comparison for the selected company.

I have broken down this dashboard creation process into 3 parts. In today’s article, I will show you how to create a dynamic scatter chart.

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel-Part-1.xlsx)
**

KPI Dashboard in Excel – Dynamic Scatter Chart
----------------------------------------------

I have the KPI data for 100 companies. For the purpose of this dashboard, let’s call these companies Com 1, Com 2, and so on.. and the KPIs are KPI 1, KPI 2, KPI 3, and KPI 4. The data looks as shown below:

![KPI Dashboard in Excel - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20323'%3E%3C/svg%3E)

*   The dashboard comprises 3 worksheets – ‘Data’, ‘Calculation’, and ‘Dashboard’.
*   It is almost always a good idea to convert raw data into an Excel Table. In this case, I have named this table KPIData.
*   In the Dashboard sheet, insert 2 ActiveX Combo Box. The input to these Combo Box would be the name of the KPIs (KPI 1, KPI 2…) and each Combo Box is linked to a cell in the Calculation sheet.![KPI Dashboard in Excel - ComboBox Cell Links](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20331'%3E%3C/svg%3E)
*   We now need to create a dataset for the chart (this data resides in the Calculation worksheet). Since the chart updates when the drop-down selection is changed, the data needs to be dependent on the selection. We can do this using a combination of [INDEX](https://trumpexcel.com/excel-index-function/)
     and [ROWS](https://trumpexcel.com/excel-rows-function/)
     formula. Here it is:
    *   X Axis: \=INDEX(KPIData,ROWS($A$15:A15),$B$8+1)
    *   Y Axis: \=INDEX(KPIData,ROWS($A$15:B15),$B$9+1)  
        ![KPI Dashboard in Excel - Dynamic Chart Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20329%20350'%3E%3C/svg%3E)
*   Now this data is fed into a scatter chart. Since the data is dependent on the Combo Box drop downs, as soon as the drop-down selection is changed, the chart instantly updates.  
    ![KPI Dashboard in Excel - Scatter Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20344'%3E%3C/svg%3E)

**Download the Example File  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/07/KPI-Dashboard-in-Excel-Part-1.xlsx)
  
**

This simple dynamic [scatter chart](https://trumpexcel.com/scatter-plot-excel/)
 is really helpful when you want to down-select a handful of companies based on their KPI performance.

In the **[next article](https://trumpexcel.com/kpi-dashboard-in-excel-part-2/)
** of this series, I will show you how to spot a company in this chart, and how to get the dynamic interpretation of the chart (in the text box below the chart).

Let me know what you think? Leave your thoughts in the comments section.

Stay Tuned… More awesome excel stuff coming your way in the next article (KPI Dashboard in Excel – Part 2) 🙂

**Other Excel Dashboard Tutorials:**

*   [Excel Dashboards – Examples, Best Practices & Resources](https://trumpexcel.com/creating-excel-dashboard/)
    .
*   [Game of Thrones Dashboard in Excel](https://trumpexcel.com/game-of-thrones-dashboard/)
    .
*   [Excel Dashboard: Premier League Season 2014-15 visualized](https://trumpexcel.com/excel-dashboard-epl-visualization/)
    .
*   [KPI Dashboard by Chandoo – A 6 Part Series](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [How to Create a Drop-down in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [Adding and Using Checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Adding and Using Radio Buttons in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .
*   [Creating Heat Maps in Excel](https://trumpexcel.com/heat-map-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

26 thoughts on “KPI Dashboard in Excel \[Part 1 of 3\] – Dynamic Scatter Chart”
-------------------------------------------------------------------------------

1.  what is no numbers or percentage is given , how do we make the chrts then .  
    i have an excel file , where theres no percentage given , n i have to make a kpi dashboard of it .
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-12143)
    
2.  I Love This site
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-10681)
    
3.  I want to learn VBA, can anyone provide me a right path for it ?
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-8667)
    
4.  Muchas gracias por compartir tu conocimiento e inteligencia, (thank you very much!! from argentina)
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-3322)
    
5.  Sumit I just got to know your website last month. Plenty of good stuff. I will be visiting more often for ideas.
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2301)
    
    *   Thanks for commenting.. Glad you find the website useful.. Look forward to having you here more often 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2303)
        
        *   I want to have the strike price wise OI data across weeks (max-3) culled from NSE.COM site after certain intervals.  
            Can you help me
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-14784)
            
        *   I want to have the strike price wise OI data across weeks (max-3) culled from NSE.COM site after certain intervals.  
            Can you help me
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-14785)
            
6.  Good one Sumit
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2279)
    
    *   Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2304)
        
        *   Hi Sumit,  
            Keep On Keeping On!
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2354)
            
        *   Hi Sumit, I just made a thermometer chart as per your guidance. One issue comes up when I set actual value more than 85 then the Axis value changes, it works fine when actual value is less. Down loaded your copy also and find the same.  
            Could you give clue how this can be fixed.
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2549)
            
        *   Hi Sumit,  
            Just ignor earlier note, I tried and now it is ok. Axis setting changed to RESET from Auto for Min and Max.  
            Thanks
            
            Regards,
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2550)
            
7.  This is Great……..
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2276)
    
    *   Thanks for commenting Pradip.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2277)
        
8.  Thanks for such a tip u really made it so simple
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2272)
    
    *   Thanks for stopping by and commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2274)
        
9.  Hi Sumit,  
    I created a marketing dashboard using VBA which has lots of formulas. Making it slow while clicking on command button. Would request you to provide some tricks or tools in order to make it faster. Thanks
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2268)
    
    *   A lot of formulas does make a dashboard slow. There are some tips here on making the dashboard faster – [http://trumpexcel.com/2014/04/suffering-from-slow-excel-spreadsheets/](http://trumpexcel.com/2014/04/suffering-from-slow-excel-spreadsheets/)
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2270)
        
10.  Thanks Sumit for this post. It’s always helpful to visit your site. However, I downloaded the file and it doesn’t seem to contain all the components of the dashboard as shown in picture above. Would be great if you re-upload the file. Thanks.
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2267)
    
    *   Hello Anil.. Thanks for dropping by and commenting.. I will be posting the remaining 2 parts of the dashboard series soon. The 3rd part would have the fully functional dashboard. I have kept the download file to show only the elements that I talk about in this tutorial.
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2269)
        
        *   Thanks Sumit for your prompt reply. You are awesome.
            
            [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2271)
            
11.  Thank you for making it look so simple – this can be such a treasure to my work.
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2262)
    
    *   Thanks for commenting Pierre.. Glad you find this useful 🙂
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2266)
        
12.  This is awesome.. Would love to get my hands on the final dashboard
    
    [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2261)
    
    *   Thanks for commenting Scott.. I will soon be publishing the remaining 2 parts of this series
        
        [Reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#comment-2265)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/#respond)

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