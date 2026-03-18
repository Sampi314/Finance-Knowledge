# Shading above or below a line in Excel charts [tutorial] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/shaded-line-charts-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Shading above or below a line in Excel charts \[tutorial\]
==========================================================

*   Last updated on February 13, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**When comparing 2 sets of data, one question we always ask is,**_

*   How is first set of numbers different from second set?

A classic example of this is, **lets say you are comparing productivity figures of your company with industry averages.** Merely seeing both your series as lines (or columns etc.) is not going to tell you the full story. But if we can shade our productivity line in red or green when it is under or above industry average… now that would be awesome! Something like below:

![Shaded line charts - help us tell a better story when comparing one series with another](https://img.chandoo.org/c/shaded-line-chart-using-excel.png)

The above chart tells us where we are lagging and where we are good. It will let us ask poking questions about the gap and find answers (_may be removing coffee machine from 2nd floor last May was a bad idea!_)

**So how do we create such a chart?**

PS: This chart and article is inspired from a question asked by arobbins & excellent solution provided by Hui [here](http://chandoo.org/forums/topic/shading-chart-to-show-returns-above-or-below-average)
.

Creating a shaded line chart in Excel – step by step tutorial
-------------------------------------------------------------

### 1\. Place your data in Excel

Lay out your data like this.

![Original Data - Shaded line chart in Excel](https://img.chandoo.org/c/original-data-shaded-line-chart.png)

### 2\. Add 3 extra columns – min, lower, upper

If you look at the chart closely, you will realize it is a collection of 4 sets of data. See this illustration to understand.

![Anatomy of Shaded line chart made in Excel - 3 extra series explained](https://img.chandoo.org/c/anatomy-of-shaded-line-chart.png)

Write formulas to load values in to min, lower (green) & upper (red) series.

*   Min is minimum of productivity and ind. average
*   Lower (green) is difference between productivity and ind. average (or NA() if negative)
*   Upper (red) is difference between ind. average and productivity (or NA() if negative)

### 3\. Create a stacked area chart from this data

Select all the 4 series (productivity, min, lower & upper) and create a stacked area chart.

This is how it looks.

![Step 1 - create a stacked area chart - shaded line chart in Excel](https://img.chandoo.org/c/step1-create-stacked-area-chart-shaded-line-chart.png)

### 4\. Format the productivity series as line

Right click on productivity series and using “Change series chart type” option, change it to line chart.

![Step 2 - Format Productivity series as line - Shaded line chart in Excel](https://img.chandoo.org/c/step2-convert-series-to-line-shaded-line-chart.png)

### 5\. Make the min series transparent

Select min series and fill it with “No color”

![Step 3 - make the min series transperant - Shaded line chart in Excel](https://img.chandoo.org/c/step3-make-min-series-transperant-shaded-line-chart.png)

### 6\. Format lower & upper in green & red colors respectively

![Step 4 change the colors for lower & upper series - shaded line chart in Excel](https://img.chandoo.org/c/step4-format-the-chart-shaded-line-chart.png)

And you are done!

### Optional: adjust series formatting, add grid lines etc.

As a bonus, you can add vertical grid lines (so that we can understand the red green changes easily) and format the horizontal axis. You can also move around the legend and remove the words “min” from it.

This will make the chart look really awesome.

![Shaded line charts - help us tell a better story when comparing one series with another](https://img.chandoo.org/c/shaded-line-chart-using-excel.png)

Is this the only way to compare productivity with industry averages?
--------------------------------------------------------------------

Although our **shaded line chart is an excellent way to visualize differences** between 2 series of data, I kept thinking if there are _other ways to compare this._

After a bit of doodling & drawing inspiration from various charts I have seen earlier, here are 4 more options we can consider.

### Option 1 – Productivity vs. variance wrt Ind. average

![Alternative 1 - shaded line chart in Excel](https://img.chandoo.org/c/alternative-1-shaded-line-chart.png)

This chart shows the variance (industry average-productity) at bottom so that we can easily look at overall trend & understand how we fared with respect to industry.

To create this chart, you just have to calculate the variance in a separate column and create a column & line chart combination (column for variance & line for productivity). Once such a chart is ready, go to fill options for the column chart and check **invert colors if negative** option and set up green & red colors!

### Option 2 – Productivity vs. better or worse indicators

![Alternative 2 - Shaded line chart in Excel](https://img.chandoo.org/c/alternative-2-shaded-line-chart.png)

This chart just shows whether productivity surpassed industry average or not in a boolean state (green for yes, red for no)

This chart is a combination of line & column chart with same principle as above (invert if negative option).

### Option 2 (made using Excel 2010 Sparklines)

![Alternative 2 - made with Sparklines - Shaded line chart in Excel](https://img.chandoo.org/c/alternative-2-using-sparklines-shaded-line-chart.png)

You can create this chart very easily with [Excel 2010 sparklines](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
. Line chart for productivity and win-loss chart for better or worse indicators.

### Option 3 – Collapsed Productivity vs. variance wrt Ind. average

![Alternative 3 - collapsed - Shaded line chart](https://img.chandoo.org/c/alternative-3-shaded-line-chart.png)

Since the color is already telling us whether variance is negative or positive, we can collapse both to same side of axis (thus saving some space & reducing redundant information).

To create this chart, we need two series of data – positive variance & negative variance as 2 sets of areas on the chart.

### Option 4 – Collapsed Productivity vs. better or worse indicators

![Alternative 4 - Shaded line chart with collapsed indicators in Excel](https://img.chandoo.org/c/alternative-4-shaded-line-chart.png)

Well, this is same as option 2 but collapsed.

Download Example workbook
-------------------------

[**Click here to download the Excel workbook**](https://img.chandoo.org/c/shading-charts-based-on-condition.xlsx)
 containing all these examples. You can also see detailed steps for making the shaded line chart in it.

How do you compare one series with another?
-------------------------------------------

**I must confess that I never made shaded line chart until today**. For smaller data sets (<15 items), I usually compare by making column charts or [thermo-meter charts](http://chandoo.org/wp/2009/12/17/quick-thermometer-chart/)
. These are easy to make and easy to understand. For larger data sets, I try to [make dynamic charts](http://chandoo.org/wp/tag/dynamic-charts/)
 so that I can choose which series to include in comparison or make indexed charts.

Now that I learned how to set up shaded line charts, I will try them in my upcoming projects & consulting assignments to see how they fare.

**What about you?** Which types of charts do you use to compare one series with another? Please share your techniques & implementations using comments. _**I would love to learn more from you.**_

Compare often? Check out these charts
-------------------------------------

**If you compare apples to apples (or to an occasional  bushel of oranges) for living**, then check out these charting tutorials & techniques.

_WARNING: After learning these techniques, Suddenly you will become incomparably awesome in your office._

*   [Comparing one product sales with another using Excel charts](http://chandoo.org/wp/2011/04/25/comparing-sales-excel-techniques/)
    
*   [INDEX charts – compare uneven values over time](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
    
*   [Comparing world education rankings – case study](http://chandoo.org/wp/2010/12/20/world-education-rankings-visualization/)
    
*   [Best charts to compare actual vs. target values](http://chandoo.org/wp/2009/12/18/charts-to-compare-targets/)
    
*   [Us vs. Them – Interactive comparison chart](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
    
*   Dynamically comparing any 2 series:
    *   [Example 1 – Customer Service Dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
        
    *   [Example 2 – KPI Dashboard](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
        

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [19 Comments](https://chandoo.org/wp/shaded-line-charts-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/shaded-line-charts-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [budget vs. actual](https://chandoo.org/wp/tag/budget-vs-actual/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [comparison charts](https://chandoo.org/wp/tag/comparison-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [hui](https://chandoo.org/wp/tag/hui/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [na()](https://chandoo.org/wp/tag/na/)
    , [sparklines](https://chandoo.org/wp/tag/sparklines/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousDistinct Count & Blanks – Power Pivot Real Life Example](https://chandoo.org/wp/distinct-count-in-pivot-tables/)

[NextLove letters to Chandoo.orgNext](https://chandoo.org/wp/love-letters-to-chandoo-org/)

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