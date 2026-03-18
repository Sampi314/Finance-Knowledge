# How to Create an Area Chart in Excel (explained with Examples)

**Source:** https://trumpexcel.com/area-chart

---

[Skip to content](https://trumpexcel.com/area-chart/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/area-chart/#below-title)

An area chart is similar to a line chart with one difference – the area below the line is filled with a color.

Both – a line chart and an area chart – show a trend over time.

In case you’re only interested in showing the trend, using a line chart is a better choice (especially if the charts are to be printed).

For example, in the below case, you can use a line chart (instead of an area chart)

![Line chart Vs Area Chart - a side by side comparison](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20844%20307'%3E%3C/svg%3E)

Area charts are useful when you have multiple time series data and you also want to show the contribution of each data set to the whole.

For example, suppose I have three product lines of Printers (A, B, and C).

And I want to see how the sales have been in the past few years as well as which printer line has contributed how much to the overall sales, using an area chart is a better option.

![Showing Area chart for the comparison in product line contribution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20308'%3E%3C/svg%3E)

In the above chart, we can see that Printer B (represented by the orange color) has the maximum contribution to the overall sales.

While it’s the same data, using an area chart, in this case, makes the overall contribution stands out.

Now let’s see how to create an area chart in Excel and some examples where area charts can be useful.

There are three in-built types of area charts available in Excel:

1.  Area Chart
2.  Stacked Area Chart
3.  100% Stacked Area Chart

Let’s see how to create each of these and in which scenario which one should be used.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/area-chart/#)

Creating an Area Chart
----------------------

This is just like a line chart with colors.

The problem with this type of chart is that there is always an overlap in the colors plotted on the chart.

For example, if you have a dataset as shown below:

![Dataset for Overlap area chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20170'%3E%3C/svg%3E)

If you use this data to create an area chart, you may end up getting a chart as shown below (where we have plotted three types of data, but you only see one color).

![Area Chart - Issue with overlap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20365'%3E%3C/svg%3E)

The above chart has data for Printers, Projectors, and White Boards, but only the data for White Boards is visible as it more than the rest two categories.

In such a case, a stacked area chart or a 100% stacked area chart is more suited (covered later in this tutorial).

The regular 2-D area chart is better suited for cases where you have two types of the dataset (an overall data set and a subset).

For example, suppose you have a dataset as shown below (where I have shown the Overall sales of the company and the Printer sales):

![Sales Data Overall and Printer Sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20171'%3E%3C/svg%3E)

I can use this data to create a regular area chart as there would no complete overlapping of colors (as one data series is a subset of another).

Here are the steps to create an area chart in Excel:

1.  Select the entire dataset (A1:D6)
2.  Click the Insert tab. ![Click the Insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20193'%3E%3C/svg%3E)
3.  In the Chart group, click on the ‘Insert Line or Area Chart’ icon.![Click on Insert Line or Area Chart icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20147'%3E%3C/svg%3E)
4.  In the 2-D Area category, click on Area.![Click on 2-D Area icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20493'%3E%3C/svg%3E)

This will give you an area chart as shown below:

![Area chart with subsets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20364'%3E%3C/svg%3E)

In this case, this chart is useful as shows the ‘Printer’ sales as well as the overall sales of the company.

At the same time, it also visually shows the printer sales as a proportion of the overall sales.

**Note**: There is an order plotting the colors in this chart. Note that the orange color (for printer sales) is over the blue color (overall sales). This happens as the in our dataset, the printer sales are on the column which is on the right of the overall sales column. If you change the order of columns, the order of colors would also change.

Creating a Stacked Area Chart
-----------------------------

In most of the cases, you will be using a stacked area chart.

Suppose you have the dataset below, which shows the sales of three different items (in thousands):

![Sales Data for Area chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20504%20171'%3E%3C/svg%3E)

Here are the steps to create an Area chart in Excel with this data:

1.  Select the entire dataset (A1:D6)
2.  Click the Insert tab.
3.  In the Chart group, click on the ‘Insert Line or Area Chart’ icon.
4.  In the 2-D Area category, click on Stacked Area.![Click on Stacked Area icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20493'%3E%3C/svg%3E)

This will give you the stacked area chart as shown below:

![Stacked area chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20365'%3E%3C/svg%3E)

In the above chart, you get the following insights:

1.  The overall value for any given year (for example, 1o5 in 2017 and 130 in 2018).
2.  The overall trend as well as the product wise trend.
3.  A visual representation of the proportion of each product sales to the overall sales. For example, you can visually see and deduce that the sales if projectors contributed the most to the overall sales and the White Boards contributed the least.

Creating a 100% Stacked Area Chart
----------------------------------

This chart type is just like a stacked area chart with one difference – all the values on the Y-axis amount to 100%.

Something as shown below:

![100% Stacked area chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20362'%3E%3C/svg%3E)

This helps you get a better representation of individual product lines, but it doesn’t give you the trend in the overall sales (as the overall sales for each year would always be 100%).

Here are the steps to create a 100% Stacked Area chart in Excel:

1.  Select the entire dataset (A1:D6)
2.  Click the Insert tab.
3.  In the Chart group, click on the ‘Insert Line or Area Chart’ icon.
4.  In the 2-D Area category, click on 100% Stacked Area.![Click on 100% Stacked area chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20493'%3E%3C/svg%3E)

In the above chart, you get the following insights:

1.  The overall trend in the proportion of each product line. For example, we can see that printers’ contribution to overall sales increased in 2018 but then declined in 2019.
2.  The percentage contribution of each product line to the overall sales. For example, you can visually deduce that projectors contributed ~40% of the overall sales of the company in 2017.

**Note**: This chart gives you a trend in the proportion of the contribution of overall sales, and NOT the trend of their absolute value. For example, if the proportion of Printer sales in 2018 went up, it doesn’t necessarily mean that the Printer sales went up. It just means that it’s contribution increased. So if the printer sales decline by 10% and all other product line sales decline by 30%, the overall contribution of printer sales automatically goes up (despite a decline in its own sales).

**You May Also Like the Following Excel Chart Tutorials:**

*   [How to Create a Thermometer Chart in Excel](https://trumpexcel.com/thermometer-chart/)
    .
*   [How to Create a Timeline / Milestone Chart in Excel.](https://trumpexcel.com/milestone-chart-in-excel/)
    
*   [Creating a Pareto Chart in Excel (Static & Dynamic)](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [How to Make a Bell Curve in Excel.](https://trumpexcel.com/bell-curve/)
    
*   [Excel Sparklines – A Complete Guide with Examples](https://trumpexcel.com/sparklines/)
    .
*   [Combination Charts in Excel.](https://trumpexcel.com/combination-charts-in-excel/)
    
*   [Creating a Pie Chart in Excel](https://trumpexcel.com/pie-chart/)
    
*   [Excel Histogram Chart](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Step Chart in Excel](https://trumpexcel.com/step-chart-in-excel/)
    
*   [Calculate Area Under Curve in an Excel](https://trumpexcel.com/calculate-area-under-curve-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Create an Area Chart in Excel (explained with Examples)”
------------------------------------------------------------------------------

1.  Absolute definition of each chart in excel. Much appreciated.
    
    [Reply](https://trumpexcel.com/area-chart/#comment-14732)
    
2.  This is helpful, thanks
    
    [Reply](https://trumpexcel.com/area-chart/#comment-13131)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/area-chart/#respond)

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