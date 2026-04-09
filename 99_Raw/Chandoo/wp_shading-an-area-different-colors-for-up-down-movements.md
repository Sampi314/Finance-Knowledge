# Shading an area chart with different colors for up & down movements [case study] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/shading-an-area-different-colors-for-up-down-movements

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Shading an area chart with different colors for up & down movements \[case study\]
==================================================================================

*   Last updated on July 29, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**We all know that area charts are great for understanding how a list of values have changed over time.** Today, let’s learn how to create an area chart that shows different colors for upward & downward movements.

The inspiration for this came from a [recent chart published in Wall Street Journal](http://graphics.wsj.com/gallery/china-markets-latest-selloff)
 about Chinese stock markets (shown below).

![wsj-chinese-stock-market-chart](https://chandoo.org/wp/wp-content/uploads/2015/07/wsj-chinese-stock-market-chart.png)

We will try to create a similar chart using Excel.

This is what we are going to come up with.

![indian-stock-market-chart](https://chandoo.org/wp/wp-content/uploads/2015/07/indian-stock-market-chart.png)

**Looks interesting? Read on…**

### Creating an area chart with different colors for up & down slopes

**Step 1. Gather the data**

For our example, let’s use Indian stock market data for last 10 years. Specifically, BSE Sensex weekly closing prices between 1-July-2005 and 27-July-2015.

![raw-data-shaded-area-chart](https://chandoo.org/wp/wp-content/uploads/2015/07/raw-data-shaded-area-chart.png)

There are 3 columns in this data – Date, Closing price & Volume, as shown below. Let’s say all of this data is in a tabled named _data_ that starts at cell B6.

**Step 2. Find out when to switch colors**

The next step is to find out when to switch colors.

We can add 3 additional columns to our data to spot the switches, and split data to Advances & Declines accordingly.

Here is what we get.

![calculations-explained-shading-area-chart-by-direction](https://chandoo.org/wp/wp-content/uploads/2015/07/calculations-explained-shading-area-chart-by-direction.png)

**Detecting when a switch occurs:**

When looking at closing price for a day, we need to know if the line direction has changed or not. To detect this, we can use a formula like this:

Assuming the closing price we are looking at is in cell C7,

\=C7<>MEDIAN(C6:C8) will tell us if the value in C7 is switching the trend or not.

_Why does this formula work?_ Think again. For more on this technique, refer to [BETWEEN Formula in Excel](http://chandoo.org/wp/2010/06/24/between-formula-excel/)
.

**Step 3. Expanding the data so that we can create an area chart**

If we create an area chart with just the data from above step (only advances & declines columns), we end up with a chart that looks like this.

![area-chart-with-different-colors-for-up-and-down-slopes](https://chandoo.org/wp/wp-content/uploads/2015/07/area-chart-with-different-colors-for-up-and-down-slopes.png)

As you can see, the green & red areas (advancing & declining data) have tiny white space between them.

This is because, when we switch from green to red, the green series goes from peak to 0 and simultaneously, red series goes from 0 to peak, creating an effect like below (chart made from sub-set of data)

![area-chart-with-different-shades-wrong](https://chandoo.org/wp/wp-content/uploads/2015/07/area-chart-with-different-shades-wrong.png)

To create correct shading effect, we need to expand the data so that on dates when switching happens, there is a duplicate row.

See below illustration to understand what we need.

![expaned-data-explained](https://chandoo.org/wp/wp-content/uploads/2015/07/expaned-data-explained.png)

**Writing formulas to expand data**

We can use simple arithmetic along with healthy dose of [INDEX formulas](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 to create expanded data set. Can you figure out the formulas yourself as homework?

Please examine the downloadable workbook to understand these formulas more.

After expanding the data, the same area chart looks like this:

![area-chart-with-different-shades-correct](https://chandoo.org/wp/wp-content/uploads/2015/07/area-chart-with-different-shades-correct1.png)

**Step 4. Create area chart from expanded dataset**

Select the expanded advances & declines columns and create an area chart from them. Make sure horizontal axis labels are pointing to the expanded date column we constructed in step 3.

Your chart is ready now.

We can add few more bells and whistles to it and come up with below output.

![indian-stock-market-chart](https://chandoo.org/wp/wp-content/uploads/2015/07/indian-stock-market-chart.png)

*   The volume chart at the bottom is a [sparkline](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
    
*   We can find longest bull & bear rallies using [longest winning streak formula](http://chandoo.org/wp/2015/01/30/longest-winning-streak-problem/)
    

### Download Area Chart with different colors for up & down slopes workbook

**[Please click here to download area chart with different colors workbook](https://chandoo.org/wp/wp-content/uploads/2015/07/shaded-area-chart-adv-declines.xlsx)
**. Play with the chart & formulas to learn more.

### How do you like area chart with different shades?

I think this is a powerful technique to quickly eye-ball data and see where directional changes are occurring, what patterns (if any) are they following etc.

If you observe carefully, our Excel version and WSJ’s charts differ in one key aspect. In WSJ chart, they are shading bull & bear markets where overall trend is upwards or downwards with minor changes during the market period. **What formula / approach changes do you think are necessary to make exact replica of WSJ chart in Excel?**

Also, do share your feedback about this chart and how you are planning to reuse the concepts at your work.

### Addendum – Moving average based smoothing of trends

We can use simple [moving averages](http://chandoo.org/wp/2009/04/28/calculate-moving-average/)
 to smooth the trends so that we can spot upward / downward movements better.  
Here is an example chart.

![shading-area-chart-with-up-and-down-colors-moving-average-smoothing](https://chandoo.org/wp/wp-content/uploads/2015/07/shading-area-chart-with-up-and-down-colors-moving-average-smoothing.png)

You may [download this workbook to examine the formulas & chart](https://chandoo.org/wp/wp-content/uploads/2015/07/shaded-area-chart-adv-declines-ma.xlsx)
.

### Charts to show change over time

Understanding change is a key component of any analysis. Check out below charting techniques & tutorials to learn few more valuable skills.

*   [Narrating the story of change](http://chandoo.org/wp/2015/05/18/story-of-change/)
     – Case study on how fast America changes its mind
*   [Advances vs. Declines chart](http://chandoo.org/wp/2013/02/21/advances-vs-declines-chart/)
    
*   [How tax burden has changed over years – interactive Excel chart](http://chandoo.org/wp/2012/12/06/tax-burden-chart-excel/)
    
*   [Use indexed charts when analyzing change over time](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
    
*   [Never show simple numbers in your dashboards](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/)
    
*   [Comparing with benchmarks – shading under / over achievement](http://chandoo.org/wp/2013/02/13/shaded-line-charts-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/shading-an-area-different-colors-for-up-down-movements/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/shading-an-area-different-colors-for-up-down-movements/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [stock charts](https://chandoo.org/wp/tag/stock-charts/)
    , [visualization principles](https://chandoo.org/wp/tag/visualization-principles/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousAnnouncing Awesome August](https://chandoo.org/wp/announcing-awesome-august/)

[NextCP040: Intro. to Power Query – What is it and how to get started – with Miguel EscobarNext](https://chandoo.org/wp/intro-to-power-query-podcast/)

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