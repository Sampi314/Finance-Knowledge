# How to Quickly Create a Waffle Chart in Excel

**Source:** https://trumpexcel.com/waffle-chart-excel

---

[Skip to content](https://trumpexcel.com/waffle-chart-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/waffle-chart-excel/#below-title)

Have you heard of the Waffle Chart (also called the square pie chart)? I have seen these in a lot of [dashboards](https://trumpexcel.com/creating-excel-dashboard/)
 and news article graphics, and I find these really cool. A lot of times, these are used as an alternative to the pie charts.

Here is an example of a waffle chart (shown below):

![Waffle Chart in Excel - Example](https://trumpexcel.com/wp-content/uploads/2016/03/Waffle-Chart-in-Excel-Example.png)

In the above example, there are three waffle charts for the three KPIs. Each waffle chart is a grid of 100 boxes (10X10) where each box represents 1%. The colored boxes indicate the extent to which the goal was achieved with 100% being the overall goal.

**What do I like in a Waffle Chart?**

*   A waffle chart looks cool and can jazz up your dashboard.
*   It’s really simple to read and understand. In the KPI waffle chart shown above, each chart has one data point and a quick glance would tell you the extent of the goal achieved per KPI.
*   It grabs readers attention and can effectively be used to highlight a specific metric/KPI.
*   It doesn’t misrepresent or distort a data point (which a [pie chart](https://trumpexcel.com/pie-chart/)
     is sometimes guilty of doing).

**What are the shortcomings?**

*   In terms of value, it’s no more than a data point (or a few data points). It’s almost equivalent to having the value in a cell (without all the colors and jazz).
*   It takes some work to create it in Excel (not as easy as a bar/column or a pie chart).
*   You can try and use more than one data point per waffle chart as shown below, but as soon as you go beyond a couple of data points, it gets confusing. In the example below, having 3 data points in the chart was alright, but trying to show 6 data points makes it horrible to read (the chart loses its ability to quickly show a comparison).![Waffle Chart in Excel - 3 vs 6](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20350'%3E%3C/svg%3E)

If you want to deep dive into the good and bad of waffle charts, here is a really nice [article](https://eagereyes.org/blog/2008/engaging-readers-with-square-pie-waffle-charts)
 (do check out the comments too).

Now let’s learn to create a waffle chart in Excel using [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

**[Download the Example file](https://trumpexcel.com/wp-content/uploads/2016/04/Waffle-Chart.xlsx)** to follow along.

Creating a Waffle Chart in Excel
--------------------------------

While creating a waffle chart, I have Excel dashboards in mind. This means that the [chart needs to be dynamic](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
 (i.e., update when a user changes selections in a dashboard).

Something as shown below:

![Waffle Chart in Excel - Dynamic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20320'%3E%3C/svg%3E)

Creating a waffle chart using conditional formatting is a three-step process:

1.  Creating the Waffle Chart within the Grid.
2.  Creating the Labels.
3.  Creating a Linked Picture that can be used in Excel Dashboards.

### 1\. Creating the Waffle Chart within the Grid

*   In a worksheet, select a grid of 10 rows and 10 columns and resize it to make it look like the grid as shown in the waffle charts.![Waffle Chart in Excel - Grid 10X10](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20231'%3E%3C/svg%3E)
*   In the 10X10 grid, enter the values with 1% in the bottom-left cell of the grid (C11 in this case) and 100% in the top-right cell of the grid (L2 in this case). You can either enter it manually or use a formula. Here is the formula that will work for the specified range of cells (you can modify the references to work in any grid of cells):
    
    \=([COLUMNS](https://trumpexcel.com/excel-columns-function/)
    ($C2:C$11)+10\*([ROWS](https://trumpexcel.com/excel-rows-function/)
    (C2:$C$11)-1))/100
    
    ![Waffle Chart in Excel - grid filled](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20272'%3E%3C/svg%3E)_The font size in the image above has been reduced to make the values visible._
    
*   With the grid selected, go to Home –> Conditional Formatting –> New Rule.![Waffle Chart in Excel - New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20222%20386'%3E%3C/svg%3E)
*   In the New Formatting Rule dialog box, select Format Only cells that contain and specify the value to be between 0 and A2 (the cell that contains the KPI value).![Waffle Chart in Excel - cells that contain value between 0 and A2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20647%20374'%3E%3C/svg%3E)
*   Click on the Format button and specify the format. Make sure to specify the same [fill color](https://trumpexcel.com/shortcuts-fill-color-excel/)
     and the font color. This will hide the numbers in the cells.![Waffle Chart in Excel - fill and font color changed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20647%20374'%3E%3C/svg%3E)
*   Click OK. This will apply the specified format to the cells that have a value less than or equal to the KPI value.![Waffle Chart in Excel - conditional format applied](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20362%20283'%3E%3C/svg%3E)
*   With the grid selected, change the fill color and the font color to a lighter shade of the color used in conditional formatting. In this case, since we have used Green color to highlight cells, we can use a lighter shade of green.![Waffle Chart in Excel - fill and font changed green](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20280'%3E%3C/svg%3E)
*   Apply ‘All Border’ format using white border color.![Waffle Chart in Excel - white border](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20275'%3E%3C/svg%3E)
*   Give an outline to the grid with a gray ‘Outside Borders’ format.![Waffle Chart in Excel - gray border](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20280'%3E%3C/svg%3E)

This will create the waffle chart within the grid. Also, this waffle chart is dynamic as it is linked to cell A2. If you change the value in cell A2, the waffle chart would automatically update.

Now the next step is to create a label that is linked to the KPI value (in cell A2).

### 2\. Creating the Label

*   Go to Insert –> Text –> Text Box and click anywhere in the worksheet to insert the text box.![Waffle Chart in Excel - insert text box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20275%20190'%3E%3C/svg%3E)
*   With the text box selected, enter =A2 in the [formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
    . This would link the text box to cell A2 and any change in the cell value would also be reflected in the text box.![Waffle Chart in Excel - text box reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20135'%3E%3C/svg%3E)
*   Format the text box and place it in the waffle chart grid.![Waffle Chart in Excel - Text Box Placed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20333%20262'%3E%3C/svg%3E)

The waffle chart is now complete, but it can’t be used in a dashboard in its current form. To use it in a dashboard, we need to take a picture of this waffle chart and put it in the dashboard, such that it can be treated as an object.

### 3\. Creating the Linked Picture

*   Select the cells that make the waffle chart.
*   Copy these cells (Ctrl + C).
*   Go to Home –> Clipboard –> Paste –> Linked Picture.![Waffle Chart in Excel - paste as link](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20147%20324'%3E%3C/svg%3E)

This will create a picture that is linked to the waffle chart. You can now place this picture anywhere in the worksheet or even in any other worksheet of the same workbook. Since this picture is a copy of the cells that have the waffle chart, whenever the chart would update, this linked picture would also update.

**[Download the Example file](https://trumpexcel.com/wp-content/uploads/2016/04/Waffle-Chart.xlsx)
**.

Did you find this tutorial useful? Let me know your thoughts/feedback in the comments section below.

Learn to create world-class dashboards in Excel. Join the **[Excel Dashboard Course](https://trumpexcel.com/excel-dashboard-course/)
**.

**You May Also Like the Following Excel Charting Tutorials:**

*   [Creating a Sales Funnel Chart in Excel](https://trumpexcel.com/sales-funnel-chart-in-excel/)
    .
*   [Creating a KPI Dashboard in Excel](https://trumpexcel.com/kpi-dashboard-in-excel-part-1/)
    .
*   [Creating a Bullet Chart in Excel](https://trumpexcel.com/bullet-chart-in-excel/)
    .
*   [Creating a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Creating a Step Chart in Excel](https://trumpexcel.com/step-chart-in-excel/)
    .
*   [10 Example of Advanced Excel Charts](https://trumpexcel.com/advanced-charts/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “How to Quickly Create a Waffle Chart in Excel”
-------------------------------------------------------------

1.  Hi, Sumit!
    
    Thank you for imparting knowledge, this will really help me a lot when presenting data. I am not sure if I overlooked it or something, however, can you share with us the steps how to create a 3-product waffle chart? Thank you.
    
    [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-10911)
    
2.  hi Sumit,  
    I am new in here but thanks a lot for your impressive dash boards. Very dynamic and intuitive I must say. Looking forward to have the dash board course soon.  
    Please is it possible to come up with an election results dash board? Say Presidential and Parlementary election results. Thus, something more like the call center performance dash board.  
    Thank you
    
    [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3586)
    
3.  Hi Sumit,  
    Thanks for sharing this. This is really nice presentation of data.  
    I have a question, if I enter KPI value as 54.9% then it is showing 54% not 55%. Is there any solution to this? would like to have your comment on this. Thanks again.
    
    [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3383)
    
    *   Hello Anil, to do this, you can have the KPI value in cell B1, and in cell A2, use the formula =ROUND(B1,3)
        
        [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3443)
        
        *   Thanks Sumit
            
            [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3474)
            
4.  Thanks, this sort of chart will certainly impress sales people!
    
    [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3211)
    
    *   ouch!
        
        [Reply](https://trumpexcel.com/waffle-chart-excel/#comment-3585)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/waffle-chart-excel/#respond)

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