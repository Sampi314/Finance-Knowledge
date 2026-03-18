# Adding Microcharts & Graphs to KPI Dashboards - [Part 4 or 6]

**Source:** https://chandoo.org/wp/kpi-dashboards-graphs-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel KPI Dashboards – Adding Micro Charts \[Part 4 of 6\]
==========================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is 4th part of **Creating Management Dashboards in Microsoft Excel** 6 post series by **_Robert_**.

### This 6 Part Tutorial on Management Dashboards Teaches YOU:

[Creating a Scrollable List View in Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
  
[Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
  
[Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
  
[](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
Add Microcharts to KPI Dashboards  
[Compare 2 KPIs in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
  
[Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

The Challenge – Adding Visualization to the KPI Dashboard
---------------------------------------------------------

In this final post on KPI dashboards with Microsoft Excel, we will show you how to add meaningful graphical visualization directly into our dashboard table. With scrolling, sorting and highlighting the dash-board already offers some interesting analytical features (see previous posts). But it is still displaying the data as pure numbers. That makes it difficult for the user to recognize the relative sizes of the values at a glance. Furthermore it is often necessary to communicate the relative position of the data compared to one or several other calculated or given values like the total average or a target.

The solution
------------

![dashboard-key performance indicator -excel-with-graphs](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-kpi-excel-with-graphs-4.png "dashboard-management-excel-with-graphs")

\[[click here to view larger size](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-kpi-excel-with-graphs-lrg.gif)\
\]

Inserting conditionally formatted bar-line-combination-charts directly into the dashboard table visualizes the shown data and enables the user to get an overview at a glance. The bars show the relative sizes of the corresponding values, the conditional formatting let us immediately identify which values are below target (red color) or larger than target (grey color) and the line makes it easy to see whether a value is above or below the total average.

**[Download the Excel file – KPI Dashboards with visualization](https://chandoo.org/wp/wp-content/uploads/2008/09/dashboard-table-scroll-sort-brush-and-visualize-v3-w-sortorder.xls)
**

The Implementation
------------------

To implement the charts, we need some knowledge about creating and formatting special charts with Microsoft Excel. In my humble opinion, the by far best resource on charts with Microsoft Excel is [Jon Peltier’s excel charts pages](http://peltiertech.com/Excel/Charts/index.html)
. All you have to know for our dashboard charts is brilliantly described on Jon’s website (follow the links below).

1.  Prepare the workbook for the new features (5 extra columns on the dashboard for the bar charts, additional rows on the data worksheet to define the targets and new columns on the calculation sheet).
2.  Insert 5 conditional formatted bar charts. Read Jon’s method to [create a conditional formatted chart](http://peltiertech.com/Excel/Charts/ConditionalChart1.html)
    .![excel-dashboard-graphs-howto](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-dashboard-graphs-howto.png "excel-dashboard-graphs-howto")
    
    Use the table on the dashboard as the data source for the chart and use the targets defined on the sheet “data” as the threshold whether a value is formatted red (below target) or grey (larger than or equal target).
    
3.  Calculate the total average on the calculation sheet for each KPI and add an average line to each of the bar charts by using an XY-scatter chart type. [Read more on Bar line combo](http://peltiertech.com/Excel/Charts/BarLineCombo.html)
    .The necessary calculations for the steps 2 and 3 can be found in columns Q to AQ of the sheet “calculation”.
4.  Format the charts to make only the bars and the average line visible (no axes, no grid lines, no data labels, no caption, no border or fill color of chart area and plot area). Like Albert Einstein said: “_as simple as possible, but not any simpler._“
5.  Adjust the charts on the dashboard to make them fit exactly to the corresponding cell ranges. One tip for this: Holding the ALT key pressed when resizing a chart will make the chart size auto-fit to the size of the cell range beneath it. That makes it easier to position the charts correctly.The bar charts already look exactly the way we want them to. But there is one undesirable effect: when scrolling up or down the table, the maximum scale of the horizontal axis changes and the bars seem to “jump” up or down.
    
    To avoid this, add two additional XY-scatter-series to the chart, representing the minimum and the maximum of the total data and assign them to the secondary axis. Furthermore add 2 additional bar series to the chart, again representing the minimum and the maximum of the total data and assign them to the primary axis. We thereby “force” both horizontal axes to be identical and stay the same when scrolling up or down. Since we do not want to display these dummy-series, format them with no line and invisible markers (XY-scatters) respectively with no fill color and no border.
    
6.  Finally update the caption beneath the table to explain the meaning of the line and the bar colors.

What is next?
-------------

*   [Download the excel KPI dashboard final workbook](https://chandoo.org/wp/wp-content/uploads/2008/09/dashboard-table-scroll-sort-brush-and-visualize-v3-w-sortorder.xls)
    
*   Bookmark [Dashboards using Excel](http://chandoo.org/wp/excel-dashboards/)
     pages for future reference.
*   **Drop a lovely note of thanks to Robert if you have benefited from this series.**

Read the next part: [Part 5: Compare 2 Decision Parameters in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)

Also, Checkout our [Excel Dashboards Page](http://chandoo.org/wp/excel-dashboards/)
 for more examples and resources.

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [83 Comments](https://chandoo.org/wp/kpi-dashboards-graphs-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/kpi-dashboards-graphs-excel/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [Charts & Graphs](https://chandoo.org/wp/tag/charts-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [micro charts](https://chandoo.org/wp/tag/micro-charts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHack together a Gauge Chart in Excel without sweat](https://chandoo.org/wp/excel-speedometer-chart-download/)

[NextTracking your stock portfolio using Google DocsNext](https://chandoo.org/wp/track-stock-mf-portfolio-google-docs/)

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
    
    [Reply](https://chandoo.org/wp/kpi-dashboards-graphs-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/kpi-dashboards-graphs-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/kpi-dashboards-graphs-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ