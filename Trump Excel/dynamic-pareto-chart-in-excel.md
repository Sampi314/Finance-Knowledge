# How to Make a Pareto Chart in Excel (Static & Interactive)

**Source:** https://trumpexcel.com/dynamic-pareto-chart-in-excel

---

[Skip to content](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#below-title)

**Watch Video – How to Make a Pareto Chart in Excel**

Pareto Chart is based on the [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)
 (also known as the 80/20 rule), which is a well-known concept in project management.

According to this principle, ~80% of the problems can be attributed to about ~20% of the issues (or ~80% of your results could be a direct outcome of ~20% of your efforts, and so on..).

The 80/20 percentage value may vary, but the idea is that of all the issues/efforts, there a few that result in maximum impact.

This is a widely used concept in project management to prioritize work.

Creating a Pareto Chart in Excel
--------------------------------

In this tutorial, I will show you how to make a:

*   Simple (Static) Pareto Chart in Excel.
*   Dynamic (Interactive) Pareto Chart in Excel.

Creating a Pareto Chart in Excel is very easy.

All the trickery is hidden in how you arrange the data in the backend.

Let us take an example of a Hotel for which the complaints data could look something as shown below:![Pareto Chart in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20232'%3E%3C/svg%3E)

_NOTE: To make a Pareto chart in Excel, you need to have the data arranged in descending order._

_**Download the Excel Pareto Chart Template[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Dynamic-Pareto-Chart1.xlsx)
**_

Creating a Simple (Static) Pareto Chart in Excel
------------------------------------------------

Here are the steps to create a Pareto chart in Excel:

1.  Set up your data as shown below. ![Dataset for creating a Pareto chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20232'%3E%3C/svg%3E)
2.  Calculate cumulative % in Column C. Use the following formula: \=SUM($B$2:B2)/SUM($B$2:$B$1)![Pareto Chart in Excel - Cumulative Value Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20230'%3E%3C/svg%3E)
3.  Select the entire data set (A1:C10), go to Insert –> Charts –> 2-D Column –> Clustered Column. This inserts a column chart with 2 series of data (# of complaints and the cumulative percentage).![Pareto Chart in Excel - Inserting Clustered Column Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20247'%3E%3C/svg%3E)
4.  Right-click on any of the bars and select Change Series Chart Type.![Pareto Chart in Excel - Change series chart type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20275'%3E%3C/svg%3E)
5.  In the Change Chart Type dialogue box, select Combo in the left pane.
6.  Make the following changes:
    *   \# of Complaints: Clustered Column.
    *   Cumulative %: Line (also check the Secondary Axis check box).![Pareto Chart in Excel - Change Chart Type Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20460'%3E%3C/svg%3E)_\[If you are using Excel 2010 or 2007, it will be a two-step_ _process. First, change the chart type to a line chart. Then right click on the line chart and select Format Data Series and select Secondary Axis in Series Options\]_
7.  Your Pareto Chart in Excel is ready. Adjust the Vertical Axis values and the Chart Title.![Pareto Chart in Excel - Simple Final](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20295'%3E%3C/svg%3E)

**How to Interpret this Pareto Chart in Excel**

This Pareto chart highlights the major issues that the hotel should focus on to sort the maximum number of complaints. For example, targeting the first 3 issues would automatically take care of ~80% of the complaints.

For example, targeting the first 3 issues would automatically take care of ~80% of the complaints.

Creating a Dynamic (Interactive) Pareto Chart in Excel
------------------------------------------------------

Now that we have a static/simple Pareto chart in Excel, let’s take it a step further and make it a bit interactive.

Something as shown below:![Pareto Chart in Excel - Dynamic Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20348'%3E%3C/svg%3E)

In this case, a user can specify the % of complaints that need to be tackled (using the [excel scroll bar](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
), and the chart will automatically highlight the issues that should be looked into.

The idea here is to have 2 different bars.

The red one is highlighted when the cumulative percentage value is close to the target value.

Here are the steps to make this interactive Pareto chart in Excel:

1.  In cell B14, I have the target value that is linked to the scroll bar (whose value varies from 0 to 100).![Pareto Chart in Excel - Scroll Bar Linked Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%2076'%3E%3C/svg%3E)
2.  In cell B12, I have used the formula \=B14/100. Since you cannot specify a percentage value to a scroll bar, we simply divide the scroll bar value (in B14) with 100 to get the percentage value.![Pareto Chart in Excel - Scroll Bar Percentage Target Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%2088'%3E%3C/svg%3E)
3.  In cell B13, enter the following combination of [INDEX](https://trumpexcel.com/excel-index-function/)
    , [MATCH](https://trumpexcel.com/excel-match-function/)
    , and [IFERROR](https://trumpexcel.com/excel-iferror-function/)
     functions:  
    \=IFERROR(INDEX($C$2:$C$10,IFERROR(MATCH($B$12,$C$2:$C$10,1),0)+1),1)  
    This formula returns the cumulative value that would cover the target value. For example, if you have the target value as 70%, it would return 77%, indicating that you should try and resolve the first three issues.

![Pareto Chart in Excel - Scroll Bar Percentage Target Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20348'%3E%3C/svg%3E)

1.  In cell D2, enter the following formula (and drag or copy for all cell – D2:D10):  
    \=IF($B$13>=C2,B2,NA())
2.  In cell E2 enter the following formula (and drag or copy for all cell – E2:E10):  
    \=IF($B$13<C2,B2,NA())
3.  Select the Data in Column A, C, D & E (press control and select using the mouse).
4.  Go to Insert –> Charts –> 2-D Column –> Clustered Column. This will insert column chart with 3 series of data (cumulative percentage, the bars to be highlighted to meet the target, and remaining all other bars)
5.  Right-click on any of the bars and select Change Series Chart Type.
6.  In the Change Chart Type dialogue box, select Combo in the left pane and make the following changes:
    *   Cumulative %: Line (also check the Secondary Axis check-box).
    *   Highlighted Bars: Clustered Column.
    *   Remaining Bars: Clustered Column.
7.  Right-click on any of the highlighted bars and change the color to Red.

That’s It!

You have created an interactive Pareto Chart in Excel.

Now, when you change the target using the scroll bar, the Pareto chart would update accordingly.

_**Download the Excel Pareto Chart Template  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Dynamic-Pareto-Chart1.xlsx)
  
**_

Do you use the Pareto Chart in Excel?

I would love to hear your thoughts on this technique and how you have used it. Do leave your footprints in the comments section 🙂

**Related Project Management and Charting Tutorials:**

*   [Analyzing Restaurant Complaints using Pareto Chart](http://www.excel-easy.com/examples/pareto-chart.html)
    .
*   [Creating a Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [Creating a Milestone chart in Excel](https://trumpexcel.com/milestone-chart-in-excel/)
    .
*   [Creating a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [Employee Leave Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Creating a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    .
*   [Advanced Excel Charts](https://trumpexcel.com/advanced-charts/)
    
*   [How to Add a Secondary Axis in Excel Charts.](https://trumpexcel.com/add-secondary-axis-charts/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

29 thoughts on “Creating a Pareto Chart in Excel (Static & Dynamic)”
--------------------------------------------------------------------

1.  If you are using excel this deeply you should be investing in software that does this already for you.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-13064)
    
    *   If you can learn to do this in Excel, you may not need to invest in more expensive software. Learning to be a power user with less expensive and more commonly available tools is a valuable proposition.
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-14503)
        
2.  formula: =SUM($B$2:B2)/SUM($B$2:$B$1) SHOWING WRONG NUMBER.  
    S/B  
    formula: =SUM($B$2:B2)/SUM($B$2:$B$10)
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-11952)
    
3.  Fantastic. You helped me 100% at right time
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-11892)
    
4.  The error in the formula is fixed by making the last reference B10 instead of B1. B10 is the last cell in the column of data. You also have to multiply by 100 to get percentage.
    
    \=SUM($B$2:B2)/SUM($B$2:$B$10)\*100
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-10841)
    
5.  I’m not able to get the cumulative percentage to work. The first line says 100% and then the rest are in the thousands of percents?
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-10824)
    
6.  My Excel cannot open the “developer” can you help me how to do this?
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-10600)
    
7.  Thanks for sharing this to us. Really big useful to me.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-9970)
    
8.  Nice Post, thnx alot
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-9146)
    
9.  Learn Excel Online – Free Online Excel Training Course – Improve Excel Skills. Excel Everest is one of the reputed institutes for Online Excel Course in UK.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-8965)
    
10.  Help, steps 9 onwards don’t work for me! Everything else is great just can’t get the bars to change colour.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-8845)
    
11.  Got asked to do my first Pareto Graph today. By the end of the day, I had produced what I refer to as a “Live Pareto Graph”. All the data is compiled and resorted on the fly as data within the spreadsheet is changed. This can be real handy if you need multiple people to manipulate the project. Less steps to train.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-8800)
    
12.  l like this blog [Excel Everest](https://exceleverest.com/)
     offers Microsoft ExcelTutorials: Our administrations are Microsoft Excel Training, Online Excel Training,Excel Courses.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-8698)
    
13.  Why My excel Target % can’t auto update , when I scroll bar link value to 10, 20 etc.. the target is remain 0%
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-3516)
    
    *   Have you linked the target cell with the scroll bar value?
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-8801)
        
14.  If I add a value of 0 (Zero) in the complaints column the chart is no longer sorted from high to low.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-3390)
    
    *   Hello Kevin.. You’ll need to sort the data in an descending order for this chart to work. If you add a value once you have created the chart, simply sort column A and B (using the values in column B in a descending order)
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-3440)
        
15.  Sumit – nice post – love your creative thought process. One question – does this make sense? I added another IFERROR function to the overall INDEX formula so that if you have a 100% target it registers 1 (100%). I was getting a #REF error otherwise.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1786)
    
    *   Hi Mike.. I just noticed the #REF error at 100%. I have updated the article and the download file.. Thanks for sharing..You are awesome!
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1787)
        
16.  Nice charts!
    
    However, the dynamic one highlights one colum to much, e.g. for 80% 4 columns are highlighted, but – as you mentioned – 3 would be correct, i.e. INDEX($C$2:$C$10,MATCH($B$12,$C$2:$C$10,1)).  
    Furthermore, you won’t need an additional column for the remaining bars if you optimize the order of the other columns.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1781)
    
    *   Hi Frank.. Thanks for commenting..The reason I highlight 4 columns for 80% is because 3 columns would constitute only 77%. So I take an additional value (uptill 84.4%). But if you need it to be 3 only, then your formula is the way to go.
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1782)
        
17.  This is great!
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1779)
    
    *   Thanks for commenting Meera.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1783)
        
18.  I liked this !!! Well in my Excel 2010 (Std.), the combo option is not available. However, I could select individual series and could do it.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1776)
    
    *   Hi Yogi.. Thanks for commenting.. Glad you liked it 🙂 You are right! Excel 2010 doesn’t have the combo option, but it can be done using chart type.
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1778)
        
19.  Nice work. I really like the dynamic slider.
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1775)
    
    *   Hi Terry.. Thanks for commenting.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1777)
        
20.  Thank you SO much for this’ MUCH needed
    
    [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1771)
    
    *   Thanks for commenting Ferriyah.. Glad you found it useful!
        
        [Reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#comment-1772)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-pareto-chart-in-excel/#respond)

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