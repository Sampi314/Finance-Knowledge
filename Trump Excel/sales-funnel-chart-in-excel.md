# How to Create a Sales Funnel Chart in Excel

**Source:** https://trumpexcel.com/sales-funnel-chart-in-excel

---

[Skip to content](https://trumpexcel.com/sales-funnel-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sales-funnel-chart-in-excel/#below-title)

I am currently working on creating a sales pipeline management dashboard. I have all the data in place and now I am looking for some visualization to create the [dashboard](https://trumpexcel.com/creating-excel-dashboard/)
. One of the charts that I absolutely want in there is a sales funnel chart.

What is a Sales Funnel?
-----------------------

In any sales process, there are stages. A typical sales stage could look something as shown below:

_Opportunity Identified –> Validated –> Qualified –> Proposal –> Win/Loss_

If you think about the numbers, you would realize that this forms a sales funnel.

Many opportunities are ‘identified’, but only a part of it is in the ‘Validated’ category, and even lesser ends up as a potential lead.

In the end, there is only a handful of deals that are either won or lost.

If you try and visualize it, it would look something as shown below:![Sales Funnel Chart in Excel template- Example Picture](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20326%20221'%3E%3C/svg%3E)

Now let’s recreate this in Sales Funnel Chart Template in Excel.

**[Download the Sales Funnel Chart Template to follow along](https://trumpexcel.com/wp-content/uploads/2015/04/Sales-Funnel-Chart.xlsx)
**

**Watch Video – Creating a Sales Funnel Chart in Excel**

Sales Funnel Chart Template in Excel
------------------------------------

Lets first have a look at the data:

![Sales Funnel Chart in Excel template - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20127'%3E%3C/svg%3E)

Here are the steps to create the sales funnel chart in Excel:

1.  Arrange the data. I use the same dataset, as shown above, but have inserted an additional column between sales stage and deal value columns.![Sales Funnel Chart in Excel template - Dataset with dummy data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20152'%3E%3C/svg%3E)
2.  In the dummy data column, enter 0 in B2, and use the following formula in the remaining cells (B3:B6)
    
    \=([LARGE](https://trumpexcel.com/excel-large-function/)
    ($C$2:$C$6,1)-C3)/2
    

![Sales Funnel Chart in Excel template- Dataset with dummy data formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20185'%3E%3C/svg%3E)

1.  Select the data (A2:C6), and go to Insert –> Charts –> Insert Bar Chart –> Stacked Bar. ![Sales Funnel Chart in Excel template - Insert Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20290%20221'%3E%3C/svg%3E)
2.  The above steps creates a [stacked bar chart](https://trumpexcel.com/stacked-bar-chart-in-excel/)
     as shown below:![Sales Funnel Chart in Excel template - Inserted chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20298'%3E%3C/svg%3E)
3.  Select the vertical axis and press Control +1 (or right click and select Format Axis). In the Format Axis pane, within Axis Options, select categories in reverse order. This would reverse the order of the chart so that you have the ‘Identified’ stage bar at the top.![Sales Funnel Chart in Excel template - categories in reverse order](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20198%20363'%3E%3C/svg%3E)
4.  Select the blue bar (which is of dummy data) and make its color transparent![Sales Funnel Chart in Excel template - dummy data bars hidden](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20295'%3E%3C/svg%3E)
5.  Select the red bars, and press Control +1 (or right click and select Format Axis). In the Format Data series pane, select Series Options and change Gap Width to 0%. This would remove the gap between these bars![Sales Funnel Chart in Excel template - No gap between bars](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20296'%3E%3C/svg%3E)
6.  That’s it. Now remove the chart junk and format your chart to look awesome. Here are some steps I took to format it:
    *   Removed the legend and horizontal axis
    *   Changed Chart Title to ‘Sales Funnel’
    *   Changed bar colors to blue
    *   Added a border to the bars
    *   Added data labels
    *   Removed gridlines![Sales Funnel Chart in Excel template - Final](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20259'%3E%3C/svg%3E)

_**Download the Sales Funnel Template**_  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/04/Sales-Funnel-Chart.xlsx)

##### That’s all right Sumit. But where is the Dashboard?

I am working on it, and soon as I am done with it, I will share it with you all. For now, here is a glimpse of how I plan to use this sales funnel chart in the sales pipeline management dashboard.

![Sales Funnel Chart in Excel template - Dashboard Glimpse](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20244'%3E%3C/svg%3E)

I am really excited as it is the first time I will share a full-fledged dashboard on my blog. If you would like to see more of [Excel dashboard](https://trumpexcel.com/creating-excel-dashboard/)
 tutorials on this blog, give me a shout-out in the comments section.

Also, if you think there are any visualizations that would look cool in the sales pipeline dashboard, just drop me a note or leave your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Creating a simple and dynamic Pareto Chart in Excel.](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [Creating a Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [Creating Bullet Charts in Excel.](https://trumpexcel.com/bullet-chart-in-excel/)
    
*   [Creating Waffle Charts in Excel](https://trumpexcel.com/waffle-chart-excel/)
    .
*   [Step Chart in Excel.](https://trumpexcel.com/step-chart-in-excel/)
    
*   [Advanced Charting in Excel – Examples](https://trumpexcel.com/advanced-charts/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

16 thoughts on “How to Create a Sales Funnel Chart in Excel”
------------------------------------------------------------

1.  Its nice job with step by step explanations. Thanks a lot sir.
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-11604)
    
2.  Great tutorial, and Are you done with the Dashboard thing?
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-11466)
    
3.  Great tool!  
    Also have a look at [https://goo.gl/CKPyeZ](https://goo.gl/CKPyeZ)
      
    It is a great Sales Funnel Template for online whiteboard with realtime collaboration
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-9172)
    
4.  Can you do this with a pivot table/chart?
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-9002)
    
5.  Great tool you’ve created – visualizing the sales funnel is so important.
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-2540)
    
6.  sir please send all excel formula training chapter
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1987)
    
    *   You can find videos and live examples for 70+ formulas here – [http://trumpexcel.com/learn-excel/excel-formulas/](http://trumpexcel.com/learn-excel/excel-formulas/)
        
        [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1988)
        
7.  Good technique , I liked that. !
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1985)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1986)
        
8.  This is so cool 🙂
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1982)
    
    *   Thanks for commenting Mehar.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1984)
        
9.  Thanks for sharing Sumit.. Look forward to the dashboard
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1981)
    
    *   I will share it end of this month.. trying to come up with some useful visualizations
        
        [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1983)
        
        *   Thanks for sharing! Did you upload the tutorial for the dashboard?
            
            [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-9769)
            
10.  Good technique. Thanks for sharing.
    
    [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1979)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#comment-1980)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/sales-funnel-chart-in-excel/#respond)

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