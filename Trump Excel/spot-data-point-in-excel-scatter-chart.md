# How to Spot Data Point in Excel Scatter Chart

**Source:** https://trumpexcel.com/spot-data-point-in-excel-scatter-chart

---

[Skip to content](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/#below-title)

**Watch Video – How to Spot Data Point in Excel Scatter Chart**

I often use scatter chart with many data points. One of the most irritating things is to spot the data point in Excel chart. Excel does not give you a way to display the names of the data points.

While there are many add-ins available to do this, I will show you a super cool (without add-in) workaround to spot the data point you are looking for.

Something as shown below: ![Spot Data Point in Excel Scatter Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20264'%3E%3C/svg%3E)

This technique instantly gives you a way to identify the company’s position in the scatter chart.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/#)

Spot Data Point in Excel Scatter Chart
--------------------------------------

1.  Go to Insert –> Charts –> Scatter Chart.

![Spot Data Point in Excel Scatter Chart - Insert Scatter Chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20134'%3E%3C/svg%3E)

1.  Click on the empty chart and go to Design –> Select Data.

![Spot Data Point in Excel Scatter Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20156'%3E%3C/svg%3E)

1.  In the Select Data Source dialogue box, click on Add.

![Spot Data Point in Excel Scatter Chart - Add data in Scatter Chart in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20204'%3E%3C/svg%3E)

1.  In the Edit Series dialogue box, select the range for X axis and Y axis.
2.  Click Ok.

This will create a simple [scatter chart](https://trumpexcel.com/scatter-plot-excel/)
 for you. Now comes the interesting part – creating the marker to spot your selected company. This has 3 parts to it:

### 2.1 – Create a Drop Down List with Company (data point) Names

1.  Go to a cell where you want to create the drop down.
2.  Go to Data –> Data Validation.
3.  In the Data Validation dialogue box, select List (as validation criteria) and select the entire range that has names of the companies (in this case, the list is in B3:B22), and click OK.

![Spot Data Point in Excel Scatter Chart - Data Validation Drop down in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20320'%3E%3C/svg%3E)

### 2.2 – Extracting the Values for the Selected Company

1.  Select a cell and refer it to the cell with the drop down. For example, in this case, the [drop down](https://trumpexcel.com/excel-drop-down-list/)
     is in F3, and in B25 I have the formula =F3.
    *   Cell B25 would change whenever I change the drop down selection.
2.  In cell C25, use the [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
     formula to extract the Revenue (X axis) value for the company in cell B25:
    
    \=VLOOKUP(B25,$B$3:$D$22,2,0)
    
3.  In cell D25, use the VLOOKUP formula to extract the Profit Margin (Y axis) value for the company in cell B25:
    
    \=VLOOKUP(B25,$B$3:$D$22,3,0)
    

### 2.3 – Creating the Spotter

1.  Select the already created scatter chart.
2.  Go to Design –> Select Data.
3.  In the Select Data Source dialogue box, Click Add.
4.  Select cell C25 as x-axis value.
5.  Select cell D25 as Y axis Value.
6.  There would be a data point in a color and shape different from the other data points. Select that data point, right click and select Format Data Series.

![Spot Data Point in Excel Scatter Chart - Creating a Spotter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20280'%3E%3C/svg%3E)

1.  In Format Data Series Dialogue box
    *   Select Marker Option –> Built-in –> Type (select circular shape and increase the size to 11).
    *   Marker Fill –> No Fill.
    *   Marker Line Color –> Solid Line (Red or whatever color you want).
    *   Marker Line Style –> Width (Make it 1 or higher).

![Spot Data Point in Excel Scatter Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20301'%3E%3C/svg%3E)

That’s it. You have it ready. Now you can select a company and it would circle and highlight the company. Cool isn’t it?

_Note: If you have a lot of data points, your highlighter may get hidden behind the data points. In this case, simply put it on [secondary axis](https://trumpexcel.com/add-secondary-axis-charts/)
, and ensure that setting are same for primary and secondary axis_

_**Try it yourself.. Download the file**_ [![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Spot-the-data-in-Chart-in-Excel.xls)

###### **Other Excel tutorials you may also like:**

*   [Spice Up Excel Chart Data Labels – Show Positive/Negative Trend Arrows](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/)
    
*   [Color Negative Chart Data Labels in Red with a downward arrow](https://trumpexcel.com/chart-data-labels-in-red-with-arrows/)
    
*   [Handling Data Gaps in Excel Charts](https://trumpexcel.com/data-gaps-in-excel-charts/)
    
*   [Creating a Drop Down List in Excel](https://trumpexcel.com/excel-drop-down-list/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/#respond)

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