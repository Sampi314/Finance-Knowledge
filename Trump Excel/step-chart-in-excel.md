# Step Chart in Excel - A Step by Step Tutorial

**Source:** https://trumpexcel.com/step-chart-in-excel

---

[Skip to content](https://trumpexcel.com/step-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/step-chart-in-excel/#below-title)

**Watch Video – Creating a Step Chart in Excel**

A step chart can be useful when you want to show the changes that occur at irregular intervals. For example, the price rise in milk products, petrol, tax rate, interest rates, etc.

Let’s take the example of a Petrol hike in India. It can happen any day (as decided by the government) and the value remains constant between these changes. In such a case, a step chart is the right way to visualize such data points.

Unfortunately, Excel does not have an inbuilt feature to create a step chart, however, it can easily be created by rearranging the data set.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/step-chart-in-excel/#)

Step Chart in Excel
-------------------

In this tutorial, you’ll learn:

*   The difference between a Step Chart and a Line Chart.
*   Creating a Step Chart using the “Line Chart technique”.

### Line Chart Vs. Step Chart

A line chart would connect the data points in such a way that you see a trend. The focus in such charts is the trend and not the exact time of change.

On the contrary, a step chart shows the exact time of change in the data along with the trend. You can easily spot the time period where there was no change and can compare the magnitude of change in each instance.

Here is an example of both the line chart and step chart – created using the same data set (petrol prices in India).

![Line Chart Vs Step Chart - Comparison 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20710%20247'%3E%3C/svg%3E)

Both of these charts look similar, but the line chart is a bit misleading.

It gives you the impression that the petrol prices have gone up consistently during May 2015 and June 2015 (see image below).

But if you look at the step chart, you’ll notice that the price increase took place only on two occasions.

![Line Chart Vs Step Chart - Comparison 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20710%20246'%3E%3C/svg%3E)

Similarly, a line chart shows a slight decline from September to November, while the step chart would tell you that this was the period of inactivity (see image below).

![Line Chart Vs Step Chart - Comparison 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20710%20247'%3E%3C/svg%3E)

Hope I have established some benefits of using a Step Chart over a Line Chart. Now let’s go ahead a look at how to create a step chart in Excel.

### Creating a Step Chart in Excel

_First things first_. The credit for this technique goes to Jon Peltier of [PeltierTech.com](http://peltiertech.com/)
. He is a charting wiz and you will find tons of awesome stuff on his website (including this [technique](http://peltiertech.com/Excel/ChartsHowTo/StepChart.html)
). Do pay him a visit and say Hello.

Here are the steps to create a step chart in Excel:

*   Have the data in place. Here I have the data of petrol prices in India in 2015.![Step Chart - Petrol price india data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20247%20334'%3E%3C/svg%3E)
*   Have a copy of the data arranged as shown below.
    *   The easiest way is to construct the additional data set right next to the original data set. Start from the second row of the data. In cell D3, enter the reference of the date in the same row (A3) in the original data set. In cell E3, enter the reference of the value in the row above (B2) in the original dataset. Drag the cells down to the last cell of the original data.![Step Chart in Excel - Data Rearrangement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20334'%3E%3C/svg%3E)
*   Copy the original data (A2:B18 in the above example), and paste it right below the additional dataset that we created.
    *   You will have something as shown below (the data in yellow is the original data and green is the one that we created). Note that there is a blank row between the header and the data (as we started from the second row). If you are too finicky about how data looks, you can delete those cells.
    *   You don’t need to sort the data. Excel takes care of it.![Step Chart in Excel - Rearranged Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20520'%3E%3C/svg%3E)
*   Select the entire data set, go to Insert –> Charts –> 2-D Line Chart.![Step Chart in Excel - 2d line chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20244'%3E%3C/svg%3E)
*   That’s it! You’ll have the step chart ready.![Step Chart in Excel Final](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20261'%3E%3C/svg%3E)

**_Download the Example File  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/01/Step-Chart-in-Excel.xlsx)
_**

**How does this work:**

To understand how this works, consider this – You have 2 data points, as shown below:

![Step Chart in Excel - Explanation data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20235%2095'%3E%3C/svg%3E)

What happens when you plot these 2 data points on a line chart? You get a line as shown below:

![Step Chart in Excel - Explanation chart 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20218'%3E%3C/svg%3E)

Now to convert this line chart into a step chart, I need to show in the data that the value remained the same from 1 to 2 January, and then suddenly increased on 2 January. So I restructure the data as shown below:![Step Chart in Excel - Explanation chart 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20246'%3E%3C/svg%3E)

I carry forward the data to the next date when the change in value happens. So for 2nd January, I have two values – 5 and 10. This gives me a step chart where the increase is shown as a vertical line.

The same logic is applied to the restructuring of the data while creating a full-blown step chart in Excel.

While it would be nice to get an inbuilt option to create step charts in Excel, once you get a hang of restructuring the data, it won’t take more than a few seconds to create this.

**_Download the Example File  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/01/Step-Chart-in-Excel.xlsx)
_**

Hope you find this useful. Let me know your thoughts/comments/suggestions in the comments below 🙂

**Related Tutorials:**

*   [Step Chart Tutorial by Jon Peltier](http://peltiertech.com/Excel/ChartsHowTo/StepChart.html)
    .
*   [Line Chart Vs. Step Chart by Jon Peltier](http://peltiertech.com/line-chart-vs-step-chart/)
    .
*   [Creating Actual Vs Target Charts in Excel](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    .

**Other Excel Charting Tutorials You Might Like:**

*   [Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [How to Find Slope in Excel?](https://trumpexcel.com/find-slope-excel/)
    
*   [Thermometer Chart in Excel](https://trumpexcel.com/thermometer-chart/)
    .
*   [Sales Funnel Chart in Excel](https://trumpexcel.com/sales-funnel-chart-in-excel/)
    .
*   [Histogram Chart in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Waffle Chart in Excel](https://trumpexcel.com/waffle-chart-excel/)
    .
*   [Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    .
*   [Excel Sparklines](https://trumpexcel.com/sparklines/)
    .
*   [Area Chart in Excel](https://trumpexcel.com/area-chart/)
    .
*   [Advanced Excel Charts](https://trumpexcel.com/advanced-charts/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “Step Chart in Excel – A Step by Step Tutorial”
--------------------------------------------------------------

1.  How do you create a step chart when the label is not a date, but a value?
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-12478)
    
2.  Direct and to the point. Many thanks!
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-12429)
    
3.  Thanks for sharing! Is there a way to end the chart with a vertical line rather than a horizontal?
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-11779)
    
4.  Thank you for the tutorial. Is it possible to have the axis not as date Format but only in Numbers like Step 1, Step 2, Step 3, …?
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-9359)
    
5.  Dear Sir, I have a problem while sorting the same thing in various cell and to add their values. Can you please solve this problem for me. If you will give me your mail Id it would be better for me to send the data to resolve.
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-8745)
    
6.  Hej how to add a second step chart to the graphics above?
    
    like the one here: [http://www.factcheck.org/2016/02/trump-vs-clinton/](http://www.factcheck.org/2016/02/trump-vs-clinton/)
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-7033)
    
7.  Hello Sumit,  
    Thank you for sharing this wonderful tutorial. However I have a problem with my data set. Unable to load the picture. But the problem is that when I follow the above steps, I get 2 points as “16-02-2015” on X axis at different locations and Y axis values mapped to it ,56.49 and 57.31. Same is the case with every X axis point which is duplicate. PLease help.
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-3533)
    
    *   Can you share the data file so I can have a look?
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-8594)
        
    *   what you have problem in charts
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-11100)
        
8.  Hi Sumit.  
    I kinda get this and it’s cool so thank you. But I’m not clear on why you need to copy the original data twice, as in col. D (with the extra row) + E. Why couldn’t it just be done from one set of data – add the blank row and copy the date (from below) and the amount (from above). I know it doesn’t work (I’ve tried it – lol) but I just don’t get the premise behind the dual sets of data in D + E. Can you explain that a little bit, pls. Thanks, Brenda
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2830)
    
    *   Hello Brenda.. Here is the logic. Let’s say the value on Day 1 is 10 and the value on Day 2 is 20. If I plot it in a line graph, I will have a line connecting 10 and 20. But If I have 3 values (Day 1 – 10, Day 2 – 10, Day 2 – 20), then it would show that from day 1 to day 2 the value was 10, and then on day 2 it went up to 20. The reason we duplicate values is so that we have this transition where day 1 to day 2 the value remains the same, and on day 2, it witnesses the change.
        
        I also explain the logic in the video. Have a look as it also shows the graph in action.
        
        Hope this helps.
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2872)
        
        *   Thanks Sumit. I appreciate your time.
            
            [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2926)
            
9.  Thank you very much for this idea
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2829)
    
    *   Thanks for commenting Hossein.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2871)
        
10.  I really really like this tutorial. Not only for the how-to but especially for the WHY.
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2781)
    
    *   Thanks for dropping by Oz.. Glad you liked the tutorial 🙂
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2782)
        
11.  Hi! thnaks for sharing. I got a question about date column. Is it possible to format like months? I’ve tried and it didn´t work. thanks!
    
    [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2769)
    
    *   Hi Dilma.. Try this – right click on the axis and select format axis. In the Axis Options, select Axis type as Date. Should work with monthly data as well
        
        [Reply](https://trumpexcel.com/step-chart-in-excel/#comment-2774)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/step-chart-in-excel/#respond)

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