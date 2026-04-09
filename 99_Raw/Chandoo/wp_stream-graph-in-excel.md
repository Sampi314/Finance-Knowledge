# How to make stream graphs in Excel? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/stream-graph-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

How to make stream graphs in Excel?
===================================

*   Last updated on July 16, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Stream graph or stream plot is a variation of area chart that looks like a** _**stream**._ Here is a quick demo of a stream chart. Learn how to create such a graph in this page.

![x men appearances - stream chart in excel - trailer](https://chandoo.org/wp/wp-content/uploads/2020/07/x-men-appearances-stream-chart-in-excel-trailer.gif)

Background & Inspiration
------------------------

Stream graphs have been around for many years. But this particular graph, showing the **appearance of X-men characters** is originally designed by Cédric Scherer. I saw [his tweet](https://twitter.com/CedScherer/status/1278236004068012034)
 sometime back and immediately wanted to recreate this in Excel.

[![](https://chandoo.org/wp/wp-content/uploads/2020/07/cedrics-tweet-with-stream-graph-made-in-ggplot2-R.png)](https://twitter.com/CedScherer/status/1278236004068012034)

So I went to the [github project page](https://github.com/Z3tt/TidyTuesday "github project page - TidyTuesday - Cedric Scherer")
 where Cedric shares his R code, datasets and detail on the construction for all his visuals. I grabbed a copy of the dataset and used it to make the _interactive stream graph in Excel_.

_Big thanks to Cedric for the inspiration._ 🙏

Download the Stream Chart Workbook
----------------------------------

[**Please click here to download the Stream Chart: X-Men appearances workbook**](https://chandoo.org/wp/wp-content/uploads/2020/07/xmen-appearances-demo.xlsx)
. Play with it to enjoy. Examine the calculations, worksheet setup and chart formatting options to learn more.

How to make a stream graph - 4 steps
------------------------------------

As you can guess, there is no “Stream graph” option in insert ribbon on Excel. So we will need to make it by mixing a few bits and bobs. For the first part of the tutorial, let’s focus on creating a stream plot in Excel. The process involves 4 simple steps.

1.  Make a regular area chart
2.  Float the areas with a dummy series at bottom
3.  Smoothen the areas
4.  Format the chart

Let’s start with sample data as depicted below.

![sample data - stream graph](https://chandoo.org/wp/wp-content/uploads/2020/07/sample-data-stream-grapht.png)

### Step 1 - Make regular area chart

Select the data and insert a stacked area chart. We get this.

![stream graph - step 1 - regular area chart](https://chandoo.org/wp/wp-content/uploads/2020/07/stream-graph-step-1-regular-area-chart.png)

### Step 2 - Float the areas with dummy series at bottom

To make our area chart look like a _stream,_ we need to first lift the areas. To do this, we need _to add a dummy series at the bottom_.

**But what would the value of this dummy series?**

*   To make it look like a stream, each point of the area chart needs to move down or up around a center line.
*   We can do this by taking a big enough number (say 100) and subtracting _half_ the height of total area at each point.
*   To make it look natural, we can add a small random number to this.

Here is how our dummy float series will look:

![dummy float values to create stream chart effect](https://chandoo.org/wp/wp-content/uploads/2020/07/dummy-float-values-to-create-stream-chart-effect.png)

And this is how our area chart will look once you add the dummy series at the bottom.

![](https://chandoo.org/wp/wp-content/uploads/2020/07/stream-graph-step-2-after-adding-dummy-float-series.png)

### Step 3 - Smoothen the areas

You must be thinking… “Hey, where is the stream… 😕?”

We are getting there. Our area chart has all sorts of _sharp lines._ We just need to smoothen it out. I recommend 60 grit sandpaper.

Just kidding. No need to sand the edges. We just use formulas to smoothen the data. Time for some concepts.

### How to smoothen / curvify data in Excel?

![smooth line option is only available in line charts](https://chandoo.org/wp/wp-content/uploads/2020/07/smoothed-line-effect.png)If you are making a line graph, you can use the ever helpful “smooth line” option to smoothen it. Unfortunately, we need to use _area charts_ for the stream effect. So we are out of luck and need to learn how to smoothen or curvify our data.

You can use **regression** to smoothen the data, but it tends to be too complex.

The easy option: **use moving average**.

Take your data and apply moving average with a window size of 5 (try few different options and pick the one that gives good looking curve).

[Here is a tip on how to calculate moving average in Excel](https://chandoo.org/wp/calculate-moving-average/)
.

Here is the moving averaged data. Remember to include the **dummy series** in moving average calculations.

![smoothed data with moving average](https://chandoo.org/wp/wp-content/uploads/2020/07/smoothed-data-with-moving-average-1.png)

If you create an area chart from this data, suddenly those areas don’t look so sharp anymore. Our stream is _almost ready!!!_

![stream graph - step 3 - smoothed area chart from mv data with dummy float](https://chandoo.org/wp/wp-content/uploads/2020/07/stream-graph-step-2-smoothed-area-chart-from-mv-data-with-dummy-float.png)

### Step 4 - Format the chart

This last step is real simple. Just format the chart by making **dummy series transparent.** Remove any unnecessary chart elements and you have a nice stream going.

![stream graph - step 4 - final chart](https://chandoo.org/wp/wp-content/uploads/2020/07/stream-graph-step-4-final-chart.png)

Back to X-Men Appearances Stream Chart
--------------------------------------

Now that you know how to make a stream appear, let me unravel the rest of this beautiful x-men appearances chart.

### Data for the visualization:

The data for this came from Github project page ([link](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-06-30/character_visualization.csv)
). It is in a convenient CSV format. I used Power Query to connect to the file and add an extra column to extract mutant character names.

### Interactivity – Option buttons:

The interactivity in the stream graph is done with 4 option buttons, icons, text & conditional formatting. See below illustration to understand how they all create the _illusion._

![stream graph interactivity](https://chandoo.org/wp/wp-content/uploads/2020/07/stream-graph-interactivity.png)

Related: [How to make your charts & dashboards interactive?](https://chandoo.org/wp/making-dashboards-interactive/)

### Stream chart edges – lines with smoothing option:

To get the crisp stream effect, I have added two lines, one at bottom and one on top of the stream. I made these lines **smooth lines** and colored them in white.

![lines in stream graph](https://chandoo.org/wp/wp-content/uploads/2020/07/lines-in-stream-graph.png)

### Axis labels are data labels on a hidden line:

I added another line series on top. Used that to make axis labels for important issue #s and hidden the line. We get these beauties.

![axis labels in stream graph](https://chandoo.org/wp/wp-content/uploads/2020/07/axis-labels-in-stream-graph.png)

### Error bars for gridlines:

As regular gridlines can be too grainy, I removed them and used error bar technique to draw a line from bottom to top of the stream.

![gridlines in stream graph](https://chandoo.org/wp/wp-content/uploads/2020/07/gridlines-in-stream-graph.png)

### Legend is shapes + typed text:

The legend is _almost manual._ I just created a bunch of rectangles and typed the text in them. I used gradient fill technique to get two colors in the same box. 

![legend for stream plot](https://chandoo.org/wp/wp-content/uploads/2020/07/legend-for-stream-plot.png) 

### How did the stream tapered nicely?

That is for you to figure out. Use the download file to learn how that is done.

Stream Chart in Excel - Video
-----------------------------

I made a video explaining the whole process. It has many additional charting tips too. Watch it below or [on my YouTube channel](https://youtu.be/Pq4ltHJcjeA)
.

Download Stream Chart Excel File
--------------------------------

Just in case, you missed the link above…

[**Please click here to download the Stream Chart: X-Men appearances workbook**](https://chandoo.org/wp/wp-content/uploads/2020/07/xmen-appearances-demo.xlsx)
. Play with it to enjoy. Examine the calculations, worksheet setup and chart formatting options to learn more.

Advanced Excel Charting Ideas & Inspiration
-------------------------------------------

If you are looking for creative, fun and interesting ways to present data, you’ve come to the right place. Please click on below images to learn more.

[![Joy plot in Excel](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-in-excel.png)](https://chandoo.org/wp/joyplot-in-excel/)

### [Joy Plot in Excel](https://chandoo.org/wp/joyplot-in-excel/)

Another area chart, to make joy plot.

[![taxes in USA over the years - interactive chart](https://chandoo.org/wp/wp-content/uploads/2020/07/tax-burden-over-years-chart-in-excel-large.png)](https://chandoo.org/wp/tax-burden-chart-excel/)

### [Taxes in USA overtime - interactive chart](https://chandoo.org/wp/tax-burden-chart-excel/)

How have the taxes for various income levels changed over time? This interactive chart shows you how...

[![Jittered plot in Excel](https://chandoo.org/wp/wp-content/uploads/2017/08/jitter-plot-visualizing-employee-salary-hikes.png)](https://chandoo.org/wp/visualize-salary-increases-jitter-plot/)

### [Jitter Plot in Excel](https://chandoo.org/wp/visualize-salary-increases-jitter-plot/)

How to visualize 3000+ salaries with ease? A jitter plot of course.

[![world-goes-to-polls-chart-recreated-in-excel](https://chandoo.org/wp/wp-content/uploads/2020/07/world-goes-to-polls-chart-recreated-in-excel.png)](https://chandoo.org/wp/world-elections-in-2014-chart/)

### [Annual voting calendar of the world](https://chandoo.org/wp/world-elections-in-2014-chart/)

So many elections around the world, one graph to present them all.

[![network-relationship-chart-excel](https://chandoo.org/wp/wp-content/uploads/2020/07/network-relationship-chart-excel.png)](https://chandoo.org/wp/network-relationship-chart/)

### [Network relationships chart](https://chandoo.org/wp/network-relationship-chart/)

Visualize relationships between various stakeholders. Find out who has the biggest clout.

[![Excel School program](https://chandoo.org/wp/wp-content/uploads/2020/07/introducing-advanced-excel-training.png)](https://chandoo.org/wp/excel-school)

### [Want more...?](https://chandoo.org/wp/excel-school)

My Excel School program has tons of advanced charting & data analysis material. Check it out and sign up for more.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/stream-graph-in-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/stream-graph-in-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [stream graphs](https://chandoo.org/wp/tag/stream-graphs/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousThese Pivot Table tricks massively save your time](https://chandoo.org/wp/pivot-table-time-saving-tricks/)

[NextIntroducing Power BI Play Date – Online class to master Power BI (oh yeah, Power Query & Power Pivot too)Next](https://chandoo.org/wp/power-bi-play-date-is-here/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ