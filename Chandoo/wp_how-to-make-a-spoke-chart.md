# Produce a custom Spoke Chart in Excel

**Source:** https://chandoo.org/wp/how-to-make-a-spoke-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

How to make a Spoke Chart
=========================

*   Last updated on June 6, 2014

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/spoke-chart "Spoke Chart ")
, **MarnieB** asked:

“I have been asked to produce a chart that looks like the spokes in a wheel. Lines for each data point that start from the same point in the middle and go out in different directions. The length of the line indicates the value of the data point. There are only 5 or 6 data points.”

Lets see how we can produce such a “**Spoke Chart**” in Excel.

**Disclaimer**: Before I go too far I want to say that this post isn’t recommending the use of this type of chart. The post is about introducing techniques which you can use as the basis of many custom chart types. The post just uses this chart as a simple example.

EXCEL CHART TYPES
-----------------

Excel doesn’t have a native Spoke Chart in its catalog of built in Chart Types.

As MarbnieB found out, Radar Chart give some level of simulation, but there not ideal for what MarnieB’s boss wanted.

Luckily for us Excel has a Scatter Chart and this chart type can be used as a veritable drawing board for your own purposes.

The Scatter Chart draws lines between sets of coordinates in the X-Y plane.

Typically Scatter Chart are used for Plotting two variables against each other where neither the X or Y axis has a regular occurrence frequency,

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/SC04.png "SC04")](https://chandoo.org/wp/wp-content/uploads/2012/07/SC04.png)

But Scatter Charts can also be used for adding custom chart types as we will see below.

MARNIEB’s SPOKE CHART
---------------------

Lets look at MarnieB’s specifications:

*   It should have 5 or 6 spokes
*   Spokes radiate out from a central hub
*   The length of the spokes should reflect the spokes value

So it will look something like this:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/SC01.png "SC01")](https://chandoo.org/wp/wp-content/uploads/2012/07/SC01.png)

(Not drawn to scale)

We can imagine that the center of the Spoke is at a position X=0, Y=0 or (0, 0) on the Cartesian plane.

We can then break up a circle into a number of segments n. MarnieB’s requirements n = 6.

As a full circle is 360 degrees we can see that each spoke will be separated by 360/6 = 60 Deg

Hence there will be spokes at:

*   0 Deg
*   60 Deg
*   120 Deg
*   180 Deg
*   240 Deg
*   300 Deg

The length of each spoke will be supplied by MarnieB.

We can use the Scatter chart to plot each Spoke as a separate series on the scatter chart.

Each series will consist of two points, being the center point (0, 0) and another point at the end of the spoke (x, y).

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/SC02.png "SC02")](https://chandoo.org/wp/wp-content/uploads/2012/07/SC02.png)

We will need to determine the X and Y values for each end of the spoke.

Using some simple trigonometry we see that:

X = Length \* Cos ( angle )

Y = Length \* Sin ( angle )

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/SC03.png "SC03")](https://chandoo.org/wp/wp-content/uploads/2012/07/SC03.png)

Now we know the angles and lengths and so in Excel we can setup a small table to calculate the X, Y values for each end of the spokes.

Using Excel we need to remember that Excel requires angles in radians. This just requires a simple modification to the formula to:

X = Length \* Cos (Radians( angle ) )

Y = Length \* Sin (Radians( angle ) )

### Setup the Chart Series

Before we jump in you can follow along this example using a new Excel file or the worked Example File, [Excel 97/03](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke-Chart.xls "Spoke Chart 97/03")
, [Excel 07/10](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke-Chart.xlsx "Spoke Chart 07/10")
.

As mentioned above each spoke will require two points

Point 1, The center of the spoke at 0,0 and a point at X, Y

In Excel we setup a small table of the Inputs including the Point Id, Angle and Length

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke1.png "Spoke1")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke1.png)

We can then add some formulas to take the inputs and convert them to X, Y Cartesian coordinates using the formulas described above.

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke2.png "Spoke2")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke2.png)

### Putting the Chart Together

Once you have the Spoke coordinates you can construct the chart

With NO data selected, goto the **Insert Ribbon** and select **Scatter**, **Scatter with Straight Lines**

A blank chart will appear on the Screen

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke3.png "Spoke3")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke3.png)

You can resize and shift the chart to a useable location if you require.

Right Click on the Chart and select the **Select Data** option

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke4.png "Spoke4")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke4.png)

The following dialog appears:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke5.png "Spoke5")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke5.png)

Select the **Add**, button and the Edit Series dialog appears.

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke6.png "Spoke6")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke6.png)

**The Series Name**: is linked to the Spokes Name **$A$4**

**The Series X values**: is linked to the two Chart X values: **E3:E4**

**The Series Y values**: is linked to the two Chart X values: **F3:F4**

**Ok** when complete

You can now go ahead and add the other 5 Series to the chart by selecting the **Add** button.

Your Select data dialog will now appear like:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke6a.png "Spoke6a")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke6a.png)

And the chart will appear something like:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke7.png "Spoke7")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke7.png)

### Cleanup and Format the Chart

We now need to clean up and format the chart

Select and Delete the Charts Title, Chart Legend & Horizontal Grid Lines

Select Each Axis in Turn, Right Click and **Format Axis**

Set the **Minimum** and **Maximum** values to something greater than our data eg: -20, +20 in our example. The Minimum and Maximum for the Horizontal and Vertical axis bust be the same so that the chart scales correctly.

Resize the Chart so that it is approximately square

Leave the axis for now, it is simple to delete them later

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke8.png "Spoke8")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke8.png)

Select each spoke in turn

Right Click and select **Format Data Series**

Set the Marker Options, Marker Fill, Line Style, Line Color to suit your preferences

If you want to add a marker to one end of the line, Select the line, then use the Right/Left arrow keys to select the end you want, **Ctrl 1** to Edit the Format of that end only.

Your chart should now be something like:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke9.png "Spoke9")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke9.png)

### Add Data Labels

Select each spoke in turn using the Up/Down arrows, then using the Right/Left Arrow keys, select the outer end of the Spoke

Right Click and **Add Data Label**

A Default value will appear which is the Y Value for the data point

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke10.png "Spoke10")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke10.png)

Right Click on the Data Label then select **Format Data Label** or simply press **Ctrl 1**

Unclick the **Y Value** and Tick the **Series Name**

Repeat for each Spoke.

You may want to change the alignment for some of the Data Labels so they don’t clash with the spokes.

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke11.png "Spoke11")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke11.png)

### Add Circular Grid Lines

Lets add 3 Grid lines at a Maximum value and at 1/3rd and 2/3rds of that value

First we need to calculate the Grid Values

In cells C22:C24 I added 3 formulas

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke11a.png "Spoke11a")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke11a.png)

I have then assigned 3 Named Formulas to the 3 cells

**Max\_Circle**: \=$C$22

**Mid\_Circle**: \=$C$23

**Min\_Circle**: \=$C$24

To make a circle on a Scatter Chart we will need some points for the X and Y values for each point around the circle

To achieve this I will use a few Named Formulas:

**t**: \=RADIANS(ROW(OFFSET(‘1’!$A$1,,,361,1)))

**X\_1**: \=SIN(t)\*Max\_Circle

**Y\_1**: \=COS(t)\*Max\_Circle

**X\_2**: \=SIN(t)\*Mid\_Circle

**Y\_2**: \=COS(t)\*Mid\_Circle

**X\_3**: \=SIN(t)\*Min\_Circle

**Y\_3**: \=COS(t)\*Min\_Circle

Lets look at a few of these and see what is going on:

**t**: \=RADIANS(ROW(OFFSET(‘1’!$A$1,,,361,1)))

This formula sets up an Array of 360 values from 1 to 361, corresponding to 1 degree to 361 degrees. This occurs using the formula: = ROW(OFFSET(‘1’!$A$1,,,361,1)) which takes the Row value of an temporary range which is setup from cell A1 and offset 0 Rows, 0 Columns and is 361 rows high and 1 Column wide.

In a blank cell **C27** type: \= ROW(OFFSET(‘1’!$A$1,,,361,1)) press **F9** not Enter

Excel will display \={1;2;3;4;5; … ;355;356;357;358;359;360;361}

1 number for each row, which will be used to represent the degrees of the circle

In a blank cell **C28** type: \=Radians( ROW(OFFSET(‘1’!$A$1,,,361,1))) press **F9** not Enter

Excel will display \={0.0174532925199433;0.0349065850398866;0.0523598775598299; … ; 6.2482787221397;6.26573201465964;6.28318530717959;6.30063859969953}

The same array of Degrees now converted to Radians

You can learn more about how this style of formula works by reading the [Formula Forensics Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")
 where a number of similar formulas are used.

We can now use the Array of Radians to feed the Formula for the X and Y values

Looking at X: the X value of each point will be X = Circle Radius \* Cos( t )

Where **t** is our array of Radians

So for Circle 1, the Maximum Circle the X Values will be

**X\_1**: \=Cos(t)\*Max\_Circle

In a blank cell **C29** type: \=COS(t)\*Max\_Circle press **F9** not Enter

Excel will display \={14.9977154273459;14.9908624052864;14.9794430213186; … 14.9908624052864;14.9977154273459;15;14.9977154273459}

This is an array of the X Values of the Maximum Circle, all 360 of them.

You can check out the other X and Y values for the other circles yourself.

To add the Circular Grid lines to the chart, Right Click on the Chart, Select Data

This is the same Dialog we saw earlier

Select Add

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke12.png "Spoke12")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke12.png)

**Series name**: \=”Max Circle”

**Series X values**: \=’1′!x\_1

**Series Y values**: \=’1′!y\_1

Note: that we have added the worksheet name and the Named formula to the Series X and Series Y value fields. This serves to reference the Named Formula to this worksheet, sheet “1”.

Select **Ok** and add the Mid and Min Circles in a similar manner.

Your chart should now be similar to this:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke13.png "Spoke13")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke13.png)

### Add Grid Annotation

Add Grid Annotation by adding 3 more series to the chart, 1 series for each annotation point.

We can put a point at the intersection of the 3 circles and the X Axis because we know the radius and the Y value = 0 so the 3 points will be at

(Min\_Circle, 0)

(Mid\_Circle, 0)

(Max\_Circle, 0)

Once again Right Click on the Chart, **Select Data**

This is the same Dialog we saw earlier

Select **Add**

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke14.png "Spoke14")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke14.png)

**Series name**: \=”Min Annotation”

**Series X values**: \=’1′!Min\_Circle

**Series Y values**: \={0}

We can note that we have used the Named Formula for the Min Circle value as the X Value and that we have used a constant array for the Y value of 0.

Repeat this for the Mid and Max annotation points.

### Format the Annotation Points

The 3 points you have just added to the chart may or may not be visible

The easiest way to find them is to either

Use the **up/down** arrow keys to scroll through the Chart series until you see it selected

Or

Select the Chart

Goto the Chart Tools, layout Ribbon and select the **Min Annotation** series from the drop down list:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke15.png "Spoke15")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke15.png)

If there is a marker showing, set the Marker Style to None

Close the Format Dialog and Right Click on the Marker, **Add Data Labels**

Select the Data Label and Change it from the **Y Value** to the **X Value**

Also change the Label Position to **Above**

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke16.png "Spoke16")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke16.png)

### Resize the Chart

Right Click on the outside of the Chart and select **Format Chart Area**

On the Size Tab, set the **Height** and **Width** to the same value

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke17.png "Spoke17")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke17.png)

Select the Horizontal Axis and Delete it and repeat for the Vertical Axis

Your chart is now complete

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke_Master.png "Spoke_Master")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke_Master.png)

DOWNLOAD THE ABOVE FILE
-----------------------

You can download the Example File used above: [Excel 97/03](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke-Chart.xls "Spoke Chart 97/03")
, [Excel 07/10](https://chandoo.org/wp/wp-content/uploads/2012/07/Spoke-Chart.xlsx "Spoke Chart 07/10")
.

OTHER CHARTS DONE IN EXCEL USING SCATTER CHARTS
-----------------------------------------------

As you have seen above the Scatter Chart can form the basis of your own custom Charts with the results being limited by your imagination.

Presented below are three Scatter charts where the authors have taken Scatter Charts to the extreme.

### Hui’s – 3D Pendulums

In 2011, I produced an animated Scatter Chart consisting of 18 x 3D Pendulums in Excel which includes the ability to rotate the chart whilst the pendulums are swinging.

This is a Scatter Chart that consists of about 22 series, 18 for the Pendulums and a few others for the Frames and Axis.

The maths behind the pendulums locations and the rotations is all done via named formulas with a very simple macro driving the animation.

[http://chandoo.org/wp/2011/07/06/3d-dancing-pendulums/](http://chandoo.org/wp/2011/07/06/3d-dancing-pendulums/ "Hui's 3D Pendulums")

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Huis-3D-Excel-Pendulums.gif "Huis-3D-Excel-Pendulums")](https://chandoo.org/wp/wp-content/uploads/2012/07/Huis-3D-Excel-Pendulums.gif)

### Excel Hero – Smith Chart

Daniel Ferry at Excel Hero.com has produced what I consider one of the most amazing charts in Excel I have ever seen.

I don’t make this statement just for the actual modelling of the Smith Chart or the use of Excel and Named Formulas in particular but also for the sheer Beauty that is displayed in the finished chart.

[http://www.excelhero.com/blog/2010/08/excel-high-precision-engineering-chart-1.html](http://www.excelhero.com/blog/2010/08/excel-high-precision-engineering-chart-1.html "ExcelHero.com - Smith Chart")

[![ExcelHero - Smith Chart](https://chandoo.org/wp/wp-content/uploads/2012/07/Smith-Chart.png "Smith Chart")](https://chandoo.org/wp/wp-content/uploads/2012/07/Smith-Chart.png)

### Frankens Team

The Frankens team has published a number of strange charts with a lot of them based on Scatter Charts.

[https://sites.google.com/site/e90e50fx/home/creative-and-advanced-chart-design-in-excel](https://sites.google.com/site/e90e50fx/home/creative-and-advanced-chart-design-in-excel "Frankens Team - Charts")

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Spring1.png "Spring1")](https://chandoo.org/wp/wp-content/uploads/2012/07/Spring1.png)

Please note that some of these charts use advanced excel techniques and are not for the feint hearted.

**Yes the 3 charts above are all Scatter Charts, illustrating the incredible diversity that can be achieved using this tool.**

WHAT CHART STYLES WOULD YOU LIKE TO SEE ?
-----------------------------------------

What do you think of the techniques discussed above ?

What chart styles would you like to see ?

Let us know your thoughts to the above in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [92 Comments](https://chandoo.org/wp/how-to-make-a-spoke-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-make-a-spoke-chart/#respond)
    
*   Tagged under [Cos()](https://chandoo.org/wp/tag/cos/)
    , [Frankens Team](https://chandoo.org/wp/tag/frankens-team/)
    , [Named Formula](https://chandoo.org/wp/tag/named-formula/)
    , [Pendulum](https://chandoo.org/wp/tag/pendulum/)
    , [Radians()](https://chandoo.org/wp/tag/radians/)
    , [Scatter Chart](https://chandoo.org/wp/tag/scatter-chart/)
    , [Sin()](https://chandoo.org/wp/tag/sin/)
    , [Smith Chart](https://chandoo.org/wp/tag/smith-chart/)
    , [Spoke Chart](https://chandoo.org/wp/tag/spoke-chart/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousCheck if a list has duplicate numbers \[Quick tip\]](https://chandoo.org/wp/check-list-for-duplicate-numbers/)

[NextFind the last date of an activityNext](https://chandoo.org/wp/find-the-last-date-of-an-activity/)

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
    
    [Reply](https://chandoo.org/wp/how-to-make-a-spoke-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-make-a-spoke-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-make-a-spoke-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ