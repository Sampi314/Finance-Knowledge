# Calculating Moving Average in Excel [Simple, Weighted, & Exponential]

**Source:** https://trumpexcel.com/moving-average-excel

---

[Skip to content](https://trumpexcel.com/moving-average-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/moving-average-excel/#below-title)

Like many of my Excel tutorials, this one is also inspired by one of the queries I got from a friend. She wanted to calculate the moving average in Excel, and I asked her to search for it online (or watch a YouTube video about it).

But then, I decided to write one myself (the fact that I was somewhat of a statistics nerd in college also played a minor role).

Now, before I tell you how to calculate moving average in Excel, let me quickly give you an overview of what moving average mean and what types of moving averages are there.

In case you want to jump to the part where I show how to calculate moving average in Excel, [click here](https://trumpexcel.com/moving-average-excel/#Calculating-Moving-Averages-using-Data-Analysis-Toolpak-in-Excel)
.

Note: I am not an expert on statistics and my intent in this tutorial is not to cover everything about moving averages. I only aim to show you how to calculate moving averages in Excel (with a brief introduction of what moving averages mean).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/moving-average-excel/#)

What is a Moving Average?
-------------------------

I am sure you know what’s an average value.

If I have three days of daily temperature data, you can easily tell me the average of the last three days (hint: you can use the AVERAGE function in Excel to do this).

A Moving Average (also called as the rolling average or running average) is when you keep the time period of the average the same, but keeps moving as new data is added.

For example, on Day 3, if I ask you the 3-day moving average temperature, you will give me the average temperature value of Day 1, 2  and 3. And if on Day 4 I ask you the 3-day moving average temperature, you will give me the average of Day 2, 3, and 4.

As new data is added, you keep the time period (3 days) the same but use the latest data to calculate the moving average.

Moving average is heavily used for technical analysis and a lot of banks and stock-market analysts use it on a daily basis (below is an example I got from the [Market Realist site](https://marketrealist.com/2019/09/exxonmobil-chevron-do-moving-averages-show-breakout/)
).

![Example of Moving Average Use in technical Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20587%20420'%3E%3C/svg%3E)

One of the benefits of using the moving averages is that gives you the trend as well as smooths out fluctuations to an extent. For example, in case there is a really hot day, the three-day moving average of the temperature would still make sure that the average value has been smoothened (instead of showing you a really high value that could be an [outlier](https://trumpexcel.com/find-outliers-excel/)
 – a one-off instance).

Types of Moving Averages
------------------------

There are three types of moving averages:

*   Simple moving average (SMA)
*   Weighted moving average (WMA)
*   Exponential moving average (EMA)

### Simple Moving Average (SMA)

This is the simple average of the data points in the given duration.

In our daily temperature example, when you simply take an average of the past 10 days, it gives the 10-day simple moving average.

This can be achieved by averaging the data points in the given duration. In Excel, you can do this easily using the [AVERAGE function](https://trumpexcel.com/excel-average-function/)
 (this is covered later in this tutorial).

### Weighted Moving Average (WMA)

Let’s say that the weather is getting cooler with every passing day and you are using a 10-day moving average to get the temperature trend.

Day-10 temperature is more likely to be a better indicator of the trend as compared to Day-1 (since the temperature is dropping with every passing day).

So, we are better off if we rely more on the value of Day 10.

To make this reflect in our moving average, you can give more weight to the latest data and less to past data. This way, you still get the trend, but with more influence of the latest data.

This is called the weighted moving average.

### Exponential Moving Average (EMA)

The exponential moving average is a type of weighted moving average where more weight is given to the latest data and it decreases exponentially for the older data points.

It is also called the Exponential Weighted Moving Average (EWMA)

The difference between WMA and EMA is that with WMA, you can assign weights based on any criteria. For example, in a 3-point moving average, you may assign a 60% weight age to the latest data point, 30% to the middle data point and 10% to the oldest data point.

In EMA, a higher weight is given to the latest value and the weight keeps getting exponentially lower for earlier values.

Enough of statistics lecture.

Now let’s dive in and see how to calculate moving averages in Excel.

Also read: [How to Find Slope in Excel?](https://trumpexcel.com/find-slope-excel/)

Calculating Simple Moving Average (SMA) using Data Analysis Toolpak in Excel
----------------------------------------------------------------------------

Microsoft Excel already has an in-built tool to calculate the simple moving averages.

It’s called the **Data Analysis Toolpak**.

Before you can use the Data Analysis toolpak, you first need to check whether you have it in the Excel ribbon or not. There is a good chance you need to take a few steps to first enable it.

In case you already have the Data Analysis option in the Data tab, skip the steps below and see the steps on calculating moving averages.

Click on the Data tab and check whether you see the Data Analysis option or not. If you don’t see it, follow the below steps to make it available in the ribbon.

1.  Click the File tab![Click the File tab in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20319%20181'%3E%3C/svg%3E)
2.  Click on Options![Click on Options in the Excel Backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20303%20564'%3E%3C/svg%3E)
3.  In the Excel Options dialog box, click on Add-ins![Click on Add-ins in the left-pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20460'%3E%3C/svg%3E)
4.  At the bottom of the dialog box, select Excel Add-ins in the drop-down and then click on Go.![Select Excel Add-ins option and then click on Go](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20181'%3E%3C/svg%3E)
5.  In the Add-ins dialog box that opens, check the Analysis Toolpak option![Check the Analysis Toolpak option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20495'%3E%3C/svg%3E)
6.  Click OK.

The above steps would enable the Data Analysis Toolpack and you will see this option in the Data tab now.

![Data Analysis tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20199'%3E%3C/svg%3E)

Suppose you have the dataset as shown below and you want to calculate the moving average of the last three intervals.

![Data to calculate simple moving average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20375'%3E%3C/svg%3E)

Below are the steps to use Data Analysis to calculate a simple moving average:

1.  Click the Data tab![Click the Data tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20200'%3E%3C/svg%3E)
2.  Click on Data Analysis option![Data Analysis tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20199'%3E%3C/svg%3E)
3.  In the Data Analysis dialog box, click on the Moving Average option (you may have to scroll a bit to reach it).![Click on Moving Average option in the Data Analysis dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20254'%3E%3C/svg%3E)
4.  Click OK. This will open the ‘Moving Average’ dialog box.
5.  In the Input Range, select the data for which you want to calculate the moving average (B2:B11 in this example)![Enter the data range for which moving average is to be calculated](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20330'%3E%3C/svg%3E)
6.  In the Interval option, enter 3 (as we are calculating a three-point moving average)![Enter 3 as the interval](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20330'%3E%3C/svg%3E)
7.  In the Output range, enter the cell where you want the results. In this example, I am using C2 as the output range![Enter C2 as the output range - where the result would be shown](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20330'%3E%3C/svg%3E)
8.  Click OK

The above steps would give you the moving average result as shown below.

Note that the first two cells in column C have the result as #N/A error. This is because it’s a three-point moving average and needs at least three data points to give the first result. So the actual moving average values start after the third data point onwards.

You will also notice that all this Data Analysis toolpak has done is applied an AVERAGE formula to the cells.

So if you want to do this manually without the Data Analysis toolpack, you can certainly do that.

There are, however, a few things that are easier to do with the data analysis toolpak.

For example, if you want to get the standard error value as well as the chart of the moving average, all you need to do is check a box, and it will be a part of the output.

Also read: [Percentage Increase Formula in Excel](https://trumpexcel.com/percentage-change-excel/)

Calculating Moving Averages (SMA, WMA, EMA) using Formulas in Excel
-------------------------------------------------------------------

You can also calculate the moving averages using the AVERAGE formula.

In fact, if all you need is the moving average value (and not the standard error or chart), using a formula can be a better (and faster) option than using the Data Analysis Toolpak.

Also, Data analysis Toolpak only gives the Simple Moving Average (SMA), but if you want to calculate WMA or EMA, you need to rely on formulas only.

### Calculating Simple Moving Average using Formulas

Suppose you have the dataset as shown below and you want to calculate the 3-point SMA:

![Data to calculate simple moving average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20375'%3E%3C/svg%3E)

In the cell C4, enter the following formula:

\=AVERAGE(B2:B4)

Copy this formula for all the cells and it will give you the SMA for each day.

![Simple Moving Average (SMA) formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20430'%3E%3C/svg%3E)

Remember: When calculating SMA using formulas, you need to make sure the references on the formula are relative. This means that the formula can be =AVERAGE(B2:B4) or =AVERAGE($B2:$B4), but it can not be =AVERAGE($B$2:$B$4) or =AVERAGE(B$2:B$4). The row number part of the reference needs to be without the dollar sign. You can read more about [absolute and relative references here](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
.

Since we are calculating a 3-point Simple Moving Average (SMA), the first two cells (for the first two days) are empty and we start using the formula from the third day onwards. If you want, you can use the first two values as is, and use the SMA value from the third one onwards.

### Calculating Weighted Moving Average using Formulas

For WMA, you need to know the weights that would be assigned to the values.

For example, suppose you need to calculate the 3 point WMA for the below dataset, where 60% weight is given to the latest value, 30% to the one before it and 10% of the one before it.

![Data to calculate simple moving average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20375'%3E%3C/svg%3E)

To do this, enter the following formula in cell C4 and copy for all cells.

\=0.6\*B4+0.3\*B3+0.1\*B2

![Weighted Moving Average formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20519%20429'%3E%3C/svg%3E)

Since we are calculating a 3-point Weighted Moving Average (WMA), the first two cells (for the first two days) are empty and we start using the formula from the third day onwards. If you want, you can use the first two values as is, and use the WMA value from the third one onwards.

### Calculating Exponential Moving Average using Formulas

Exponential Moving Average (EMA) gives higher weight to the latest value and the weights keep on getting lower exponentially for earlier values.

Below is the formula to calculate the EMA for a three-point moving average:

EMA = \[Latest Value  - Previous EMA Value\] \* (2 / N+1) + Previous EMA

…where N would be 3 in this example (as we are calculating a three-point EMA)

Note: For the first EMA value (when you don’t have any previous value to calculate EMA), simply take the value as is and consider it the EMA value. You can then use this value going forward.

Suppose you have the below data set and you want to calculate the three-period EMA:

![Data to calculate simple moving average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20375'%3E%3C/svg%3E)

In cell C2, enter the same value as in B2. This is because there is no previous value to calculate EMA.

In cell C3, enter the below formula and copy for all cells:

\=(B3-C2)\*(2/4)+C2

![Formual to Calculate Exponential Moving Average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20493%20430'%3E%3C/svg%3E)

In this example, I have kept it simple and used the latest value and previous EMA value to calculate the current EMA.

Another popular way of doing this is by first calculating the Simple Moving Average and then using it instead of the actual latest value.

Adding Moving Average Trend Line to a Column Chart
--------------------------------------------------

If you have a dataset and you’re creating a bar chart using it, you can also add the moving average trend line with a few clicks.

Suppose you have a dataset as shown below:

Below are the steps to create a bar chart using this data and adding a three-part moving average trendline to this chart:

1.  Select the dataset (including the headers)
2.  Click the Insert tab![Click the Insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20197'%3E%3C/svg%3E)
3.  In the Chart group, click on the ‘Insert Column or Bar chart’ icon.![Click on Insert Bar or Column chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20158'%3E%3C/svg%3E)
4.  Click on the Clustered Column chart option. This will insert the chart in the worksheet.![Click on Clustered column chart icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20284%20457'%3E%3C/svg%3E)
5.  With the chart selected, click on the Design tab (this tab only appears when the chart is selected)![Click on the Design tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20180'%3E%3C/svg%3E)
6.  In the Chart Layouts group, click on ‘Add Chart Element’.![Click on Add Chart Element in the Design Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20307%20198'%3E%3C/svg%3E)
7.  Hover the cursor on the ‘Trendline’ option and then click on ‘More Trendline Options’![Click on More Trendline Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20411%20667'%3E%3C/svg%3E)
8.  In the Format Trendline pane, select the ‘Moving Average’ option and set the number of periods.![Select Moving Average trendline option and set the period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20426'%3E%3C/svg%3E)

That’s it! The above steps would add a moving trendline to your column chart.

![Chart with a moving average trend line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20661%20398'%3E%3C/svg%3E)

In case you want to insert more than one moving average trendline (for example one for 2 periods and one for 3 periods), repeat the steps from 5 to 8).

You can use the same steps to insert a moving average trend line to a line chart as well.

### Formatting the Moving Average Trend Line

Unlike a regular line chart, a moving average trend line doesn’t allow a lot of formatting. For example, if you want to highlight a specific data point on the trend line, you won’t be able to do that.

A few things you can format in the trendline include:

*   **Color** of the line. You can use this to highlight one of the trendlines by making everything in the chart light in color and making the trendline pop-out with a bright color
*   The **thickness** of the line
*    The **transparency** of the line

To format the moving average trendline, right-click on it and then select the Format Trendline option.

![Click on Format Trendline option in the Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20392'%3E%3C/svg%3E)

This will open the Format Trendline pane on the right. This pane as all the formatting options (in different sections – Fill & Line, Effects, and Trendline Options).

![Format Trendlines options in different sections](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20319%20228'%3E%3C/svg%3E)

**You may also like the following Excel tutorials:**

*   [What is Standard Deviation and How to Calculate it in Excel?](https://trumpexcel.com/standard-deviation/)
    
*   [How to Calculate Square Root in Excel](https://trumpexcel.com/calculate-square-root-in-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    
*   [How to Add a TrendLine in Excel Charts](https://trumpexcel.com/trendline/)
    
*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [5 Easy Ways to Calculate Running Total in Excel (Cumulative Sum)](https://trumpexcel.com/running-total-excel/)
    
*   [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]”
---------------------------------------------------------------------------------------

1.  Hi, where you are calculating the 3 day EWMA, why does the formula have n=4?  
    \=(B3-C2)\*(2/4)+C2  
    Is it a typo or a reason it is 4 not 3?
    
    [Reply](https://trumpexcel.com/moving-average-excel/#comment-13930)
    
2.  shouldn’t
    
    EMA = \[Latest Value – Previous EMA Value\] \* (2 / N+1) + Previous EMA
    
    be
    
    EMA = \[Latest Value – Previous EMA Value\] \* (2 / (N+1)) + Previous EMA
    
    ?
    
    [Reply](https://trumpexcel.com/moving-average-excel/#comment-13297)
    
3.  I just scrolled all the way through this blog post, just to tell you THANK YOU!!  
    I am a suddenly single mom who needs to get back in the workforce after 20+ years as a homeschool mom. Finding your videos has been a blessing from God. You explain everything so clearly. After each concept is taught, I pause the video to try it on my own spreadsheets. I am sharing the link to your videos with all my friends. I hope that this benefits you in someway, as you have benefited me. I could say more wonderful things, but I need to go start lesson 9. 🙂
    
    [Reply](https://trumpexcel.com/moving-average-excel/#comment-12712)
    
    *   Thank you so much for the kind words Martha.. I am glad you’re finding the videos useful. More power to you!
        
        [Reply](https://trumpexcel.com/moving-average-excel/#comment-12713)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/moving-average-excel/#respond)

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