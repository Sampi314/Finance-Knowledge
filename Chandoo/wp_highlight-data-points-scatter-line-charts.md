# Highlighting Data Points in Excel Scatter and Line Charts

**Source:** https://chandoo.org/wp/highlight-data-points-scatter-line-charts

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Highlighting Data Points in Scatter and Line Charts
===================================================

*   Last updated on November 11, 2010

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

**Meet our new guest author, Ian Huitson, or Hui.**

Hui will share excel tutorials, implementations with us once a week. Please visit [About – Hui](http://chandoo.org/wp/about-hui/)
 to learn more about him.

This week I am going to introduce a method for allowing single points to be highlighted and interactively moved in Excel Scatter / X-Y Charts and Line Charts.

You will see a lot of these style charts in various places where you want to highlight various aspects of the chart to your audience. It is a great technique for complex scientific and engineering charts where you may have hundreds or thousands of points.

**Introduction**
----------------

Excel charting basically has 2 styles of charts with these being Y value vs X Value charts and Y value vs X Label charts.

Examples of the X Value charts are Scatter and Bubble charts. Examples of the X Label charts are Line, Column, Surface, Area, Radar and Bar charts.

The basic differences between these is that the former has a variable X Axis and the later has a fixed X-Axis spacing between subsequent data points.

Some members of the X Label charts can display a value-type X axis when the X entries are dates, ie: The X values are plotted proportionally to the dates they represent. These types include Line, Area, Column, and Bar (Thanx Jon)

**Y value vs X value (Scatter Charts)**
---------------------------------------

As these charts are plotting Y vs X directly onto the chart, it is simple to add a series which contains the points you want to highlight.

It is worth noting that chart series for Scatter Charts don’t have to have an equal number of entries in each series. We will use this add a new series with just one point.

### **Method:**

Goto Pg1 of the sample file. [Sample File](https://chandoo.org/wp/wp-content/uploads/2010/11/Chart_Point_Highlighter.xlsx)

My Data is an X-Y set of data in B2:C41, each Y value in Column C is plotted on the chart against the corresponding X value.

To plot a single point it is a matter of adding a new data series to the chart

The new series will be the 2 cells at **B43:C43**

1\. Setup 2 lookup cells

In B43 put the equation =OFFSET(B$1,$B$44,0)

In C43 put the equation =OFFSET(C$1,$B$44,0)

Note that both these formula retrieve  a value that is the value in the Cell Reference cell, B44, below B1 and C1 respectively.

2\. Setup a Cell Reference cell  

Put a value in B44 for now say 1

3.Add a new Data Series to the Chart  

Right click on the chart and goto **Select Data**

Add a New Series

Series Name  Highlight

X Values  =’Pg1′!$B$43

Y Values  =’Pg1′!$C$43

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Add_Data1.png "Add_Data")](https://chandoo.org/wp/wp-content/uploads/2010/11/Add_Data1.png)

4\. Add a slider

The slider is already installed

5\. Set the Sliders Cell Link, Min, Max and other details

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Slider_Setup.png "Slider_Setup")](https://chandoo.org/wp/wp-content/uploads/2010/11/Slider_Setup.png)

You will now have a new data point which will be at point 1 on the chart

6\. Format the New Data Series

Right Click the new point and **Format Data Series**

Select a larger Marker Size and make it a Bold Red to stand out

7\. Add a data Label to the series

Right Click the New Series and select **Add Data Labels**

8\. Format the Data Label

Right Click the New Series and select **Format Data Labels**

On the **Labels Options** Tab, Tick the X & Y values

Select the Label and change the Font to a Bold and Increase Size so that it stands out

**[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Completed_Scatter_Chart.png "Completed_Scatter_Chart")](https://chandoo.org/wp/wp-content/uploads/2010/11/Completed_Scatter_Chart.png)
**

### **Use:**

As you move the slider the Highlighted point will move back and forwards across the screen and show both the location and X & Y Values of the data point.

### How Does This Work?

The chart contains a second series consisting of a single point (x,y)  which has been formatted to make it stand out on the chart

The coordinates for the new point are retrieved from the My Data list by using an offset from the top of the list.

The offset retrieves its offset value from a Cell Reference cell which in turn is controlled by a slider.

Why use Offset instead of Vlookup or Index/Match?

We aren’t concerned with looking up the actual value of the highlighted point, we are interested in retrieving for example the 9th data point from the list and the the 10th or 8th as we move the slider. The Offset only cares about how far it has to go to get the value, not the value.

By doing this we can mix up the X values, as Scatter charts allow you to do, and offset will happily retrieve data in order and doesn’t care about duplicates or having sorted data. Type any values into the X Column and watch as the offset happily maintains the highlighted point.

**Line Charts**
---------------

As these charts are plotting Y vs the position of the value on the X-Axis, a slightly different method is employed to highlight a point of interest.

For Line Charts we will add a new series to the chart and then use a method for hiding the non-highlighted points  so that only the highlighted point is visible.

### **Method**

Goto Pg2 of the sample file. [Sample File](https://chandoo.org/wp/wp-content/uploads/2010/11/Chart_Point_Highlighter.xlsx)

1\. Setup a Cell Reference cell

Setup a Cell Reference cell by putting a 1 in D43

2\. Add a New Data Series

Besides the sample data, add a new series Highlight

D1:  Highlight

D2: =IF(ROW()-1=$D$43,C2,NA())

Copy D2 down to D27, Don’t worry about the errors #N/A, you put them there.

3\. Add a new Data Series to the Chart  

Right click on the chart and goto **Select Data**

Add a New Series

Series Name – Highlight

Y Series =’Pg2′!$D$2:$D$27

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Add_Data_LineCht.png "Add_Data_LineCht")](https://chandoo.org/wp/wp-content/uploads/2010/11/Add_Data_LineCht.png)

Note there is no X Value as the Y values are plotted in order against the existing X Values

You will now have a new data point which will be at point 1 on the chart

4\. Format the new Data Series

Right Click the new point and **Format Data Series**

Select a Bigger marker size and make it a Bold Red to stand out

5\. Add Data Labels

Right Click the New Series and select **Add Data Labels**

Right Click the New Series and select **Format Data Labels**

On the **Labels Options** Tab, Tick the X & Y values

Select the Label and change the Font to a Bold and Increase Size so that it stands out

6\. Add a slider

The slider is already installed

7\. Set the Sliders Cell Link, Min, Max and other details

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Slider_Setup_LineCht.png "Slider_Setup_LineCht")](https://chandoo.org/wp/wp-content/uploads/2010/11/Slider_Setup_LineCht.png)

### **Use:**

As you move the slider the Highlighted point will move back and forwards across the screen and show both the location and X & Y Values of the data point.

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Completed_Line_Cht.png "Completed_Line_Cht")](https://chandoo.org/wp/wp-content/uploads/2010/11/Completed_Line_Cht.png)

### How Does This Work?

The chart contains a second series consisting of a Column of #N/A error messages and a single cell containing teh Y value for the corresponding data point

Excel ignores and doesn’t plot the cells with the error message and so only the highlighted cell is plotted

The coordinates for the new point are retrieved from the My Data list by comparing the current Row to the Cell Reference cells value and if they are the same retrieving the Y value, all others rows have an error message inserted.

The slider is connected to the Cell Reference cell and so when the slider is moved the Cell reference cell updates and the new highlighted cell retries its value.

### Quick Tip #1:

You can change the highlight from a standard marker to pretty much anything you like

Insert an Icon on your worksheet, Insert Menu, Insert Icon

Format the icon as you wish, Color, Size and Copy the icon

Select the Chart and select the Highlighted data point and Paste

To apply the picture/icon to all points in a series select the series and paste

### Quick Tip #2:

You can add multiple highlights using the same techniques described in this post ie: for showing Min and Max values.

Instead of linking the Cell Reference cell to a slider link it to the Minimum or Maximum value of the data: =Min(Range), =Max(range)

Checkout the example on Pg3 of the Sample File: [Sample File](https://chandoo.org/wp/wp-content/uploads/2010/11/Chart_Point_Highlighter.xlsx)

### FUNCTIONS USED:

Offset: [http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/](https://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/ "Offset")

Row: =Row() returns the Row number of the Current cell

\=Row(M10) returns the Row Number of Cell M10 = 10

NA: = Returns the Error Message #N/A

**How do you like to highlight your data? Let us all know in the comments below:**

**What would you like to see discussed as a How To? Let me know in the comments below:**

### NEXT THURSDAY: Scheduling Resources

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [30 Comments](https://chandoo.org/wp/highlight-data-points-scatter-line-charts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/highlight-data-points-scatter-line-charts/#respond)
    
*   Tagged under [chart](https://chandoo.org/wp/tag/chart/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [Highlight](https://chandoo.org/wp/tag/highlight/)
    , [hui](https://chandoo.org/wp/tag/hui/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Line Chart](https://chandoo.org/wp/tag/line-chart/)
    , [na()](https://chandoo.org/wp/tag/na/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [Scatter Chart](https://chandoo.org/wp/tag/scatter-chart/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousGetting the 2nd matching value from a list using VLOOKUP formula](https://chandoo.org/wp/vlookup-second-value/)

[Next90% of you can see up to cell M26 & other findings \[visualization\]Next](https://chandoo.org/wp/last-visible-cell-visualization/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/highlight-data-points-scatter-line-charts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/highlight-data-points-scatter-line-charts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/highlight-data-points-scatter-line-charts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ