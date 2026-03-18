# Creating a BULLET Chart in Excel (a Step-by-Step Guide)

**Source:** https://trumpexcel.com/bullet-chart-in-excel

---

[Skip to content](https://trumpexcel.com/bullet-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/bullet-chart-in-excel/#below-title)

**Watch Video – Creating a Bullet Chart in Excel**

One of the challenges while creating a dashboard is to present the analysis in limited screen space (preferably a single screen). Hence, it is important to make smart choices while creating the right chart. And here is where Bullet Charts score over others.

Bullet charts were designed by the dashboard expert [Stephen Few](http://www.perceptualedge.com/about.php)
, and since then it has been widely accepted as one of the best charting representations where you need to show performance against a target.

One of the best things about bullet charts is that it is power-packed with information and takes little space in your report or dashboards.

Here is an example of a Bullet Chart in Excel:![Bullet Chart in Excel - Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20315'%3E%3C/svg%3E)

This single bar chart is power-packed with analysis:

*   Qualitative Bands: These bands help in identifying the performance level. For example, 0-60% is Poor performance (shown as a dark blue band), 60-75% is Fair, 75-90% is Good and 90-100% is Excellent.
*   Target Performance Marker: This shows the target value. For example, here in the above case, 90% is the target value.
*   Actual Performance Marker: This bar shows the actual performance. In the above example, the black bar indicates that the performance is good (based on its position in the qualitative bands), but it doesn’t meet the target.

_**Download Bullet Chart Template**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/rbkez290xx7j00v/Bullet%20Chart%20in%20Excel%20trumpexcel.com.xlsx?dl=1)

Now, let me show you how to create a bullet chart in Excel.

Creating a Bullet Chart in Excel
--------------------------------

Here are the steps to creating a Bullet Chart in Excel:

1.  Arrange the data so that you have the band values (poor, fair, good, and excellent) together, along with the actual value and the target value.![Bullet Chart in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20268%20191'%3E%3C/svg%3E)
2.   Select the entire data set (A1:B7), go to Insert –> Charts –> 2D Column –> Stacked Column.![Bullet Chart in Excel - Insert Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20678%20248'%3E%3C/svg%3E)
3.  In the above step, you will get a chart where all the data points have been plotted as separate columns. To combine these into one, select the chart and go to Design –> Data –> Switch Row/Column. This will give you one column with all the data points _(the first four colors are the qualitative bands, the fifth one is actual value and the top most is target value)._![Bullet Chart in Excel - Switch Row Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20185'%3E%3C/svg%3E)
4.  Click on Target Value bar (the orange color bar at the top). Right-click and select change series chart type.![Bullet Chart in Excel - change series chart type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20213'%3E%3C/svg%3E)
5.  In the Change Chart Type dialog box, change the Target Value chart type to Stacked Line with Markers, and [put it on the secondary axis](https://trumpexcel.com/add-secondary-axis-charts/)
    . Now, there would be a dot in the middle of the bar.![Bullet Chart in Excel - chart type as line chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20429'%3E%3C/svg%3E)
6.  You would notice that the primary and secondary vertical axis are different. To make it same, select the secondary axis and delete it.![Bullet Chart in Excel - delete secondary axis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20232'%3E%3C/svg%3E)
7.  Select the Actual Value bar, right-click and select Change Chart Type. In the Change Chart Type dialog box, put Actual Value on the secondary axis.![Bullet Chart in Excel - Actual Value on Secondary Series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20433'%3E%3C/svg%3E)
8.  Select the Value bar, right-click and select Format Data Series (or press Control + 1).
9.  In the Format Data Series pane, change the Gap Width to 350% (you can change it based on how you want your chart to look). ![Bullet Chart in Excel - Actual Value Bar Gap Width](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20294'%3E%3C/svg%3E)
10.  Select the Target value marker dot, right click and select format data series (or press Control +1).
11.  In the Format Data Series dialogue box, select Fill & Line –> Marker –>Marker Options –> Built-in (and make the following changes):
    *   Type: Select dash from the drop down
    *   Size: 15 (change it according to your chart)![Bullet Chart in Excel - Marker Type and Size](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20314'%3E%3C/svg%3E)
12.  Also, change the Marker fill to red and remove the border![Bullet Chart in Excel - Marker Color and Border](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20502'%3E%3C/svg%3E)
13.  Now you are all set! Just change the color of the bands to look like a gradient (gray and blue look better)![Single KPI Bullet Chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20180%20284'%3E%3C/svg%3E)

_**Download the Excel Bullet Chart Template**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/rbkez290xx7j00v/Bullet%20Chart%20in%20Excel%20trumpexcel.com.xlsx?dl=1)

Creating Multi KPI Bullet Chart in Excel
----------------------------------------

You can extend the same technique to create a multi-KPI bullet chart in Excel.

Here are the steps to create a multi KPI bullet chart in Excel:

1.  Get the data in place (as shown below)
2.  Create a single KPI bullet chart as shown above
3.  Select the chart and drag the blue outline to include additional data points![Multi-KPI Bullet Chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20282'%3E%3C/svg%3E)

**Note:** Creating Multi-KPI bullet chart technique works well if the axis is the same for all the KPIs (for example here all the KPIs are scored in percentage varying from 0 to 100%). You can extend this to margins – for example comparing Net Income margin, EBITDA margin, Gross profit margin, etc. If the scales are different, you would need to create separate bullet charts.

While I am a big fan of bullet charts, I believe a single-KPI bullet chart is not always the best visualization. I often gravitate towards a speedometer/gauge chart in

I often gravitate towards a speedometer/gauge chart in the case of a single KPI. Let me know what you think by leaving a comment below.

**You May Also Like the Following Excel Tutorials:**

*   [Creating a KPI Dashboard in Excel](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
    
*   [Dynamic Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Charting Examples showing Actual Vs. Target comparison](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    .
*   [Creating a Thermometer Chart in Excel](https://trumpexcel.com/thermometer-chart/)
    .
*   [Creating a Sales Funnel Chart in Excel](https://trumpexcel.com/sales-funnel-chart-in-excel/)
    .
*   [Creating Heat Maps in Excel](https://trumpexcel.com/heat-map-excel/)
    .
*   [10 Advanced Excel Charts that You Can Use In Your Day-to-day Work](https://trumpexcel.com/advanced-charts/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “A Step-by-step Guide on Creating a BULLET Chart in Excel”
------------------------------------------------------------------------

1.  I have taught Excel and I use charts in my career, but today I have learned something new. Thank you! This is a great chart and well put together!
    
    [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-12890)
    
2.  Can I have help in getting a thermometer chart to show the increasing value of invoices paid for school fees. I know the total of all invoices but would like to show the actual in a thermometer graph during the year. Can you assist.
    
    [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-9672)
    
    *   Hello Dottie.. Have a look a this tutorial: [https://trumpexcel.com/thermometer-chart-in-excel/](https://trumpexcel.com/thermometer-chart-in-excel/)
        
        [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-9673)
        
3.  Smart way! very short but very meaningful. Thanks Sumit. Keep on keeping on.
    
    [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-2134)
    
    *   Thanks for commenting Amal.. Glad you liked the tutorial 🙂
        
        [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-2135)
        
4.  I hope that one day is equal to you
    
    [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-2132)
    
5.  I found this way of presenting the fantastic results Sumit.
    
    Congratulations on your expertise.
    
    [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-2131)
    
    *   Thanks for commenting Pablo.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/bullet-chart-in-excel/#comment-2133)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/bullet-chart-in-excel/#respond)

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