# Comparing 2 Key Performance Indicators - KPI Dashboards [Part 5 of 6]

**Source:** https://chandoo.org/wp/excel-dashboard-visualization-techniques-1

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

KPI Dashboards – Compare 2 Decision Parameters \[Part 5 of 6\]
==============================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a Guest Post by _**Robert**_ on Visualization Techniques for KPI Dashboards using Excel.

### This 6 Part Tutorial on Management Dashboards Teaches YOU:

[Creating a Scrollable List View in Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
  
[Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
  
[Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
  
[Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
  
[](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
Compare 2 KPIs in the Dashboards Using Form Controls  
[Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

As you all know dashboards provide “Information at a glance” with often the power to “deep dive to analyze”. Most dashboards succeed in providing information. But the exceptional ones succeed in “at a glance” part of it while maintaining the deep diving capabilities. In this and [next post](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)
 we will discuss 2 powerful visualizations that can be added to your dashboards to provide better insights at a glance. If you are not familiar with excel based dashboards we recommend reading the [dashboards using excel](http://chandoo.org/wp/management-dashboards-excel/)
.

The challenge
-------------

Part 3 of the series already displays parts of the [relationships within the 5 KPI data sets by highlighting the 10% best and 10% poorest performers](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
 of the 4 KPI that are not selected as the sort criteria. But what if we want to have a closer look on how the KPI are related to each other? We need another analytical feature that enables the user to compare the complete data sets at a glance in a graphical visualization.

The solution
------------

An XY scatter chart is the best way to analyze and visualize the relationship and correlation between two sets of quantitative data.

An XY scatter chart, however, is 2-dimensional and therefore limited to compare only two data sets.

Since we have 5 different KPI, we would need 10 different charts to display all possible combinations of KPI pairs on our dashboard. This would need too much real estate on the dashboard and it would probably be too complex and unclear for the users of the dashboard.

Again we need an interactive, flexible way to display the data in one single chart and let the user decide which 2 KPI to display (see above). Additionally we want to highlight the data points that are displayed on the dashboard table and of course we want to do this without VBA.

![comparing-2-parameters-management-dashboard-visualization](https://chandoo.org/wp/wp-content/uploads/2008/10/comparing-2-parameters-dashboard-visualization.png "comparing-2-parameters-management-dashboard-visualization")

The implementation
------------------

Download [**Excel Dashboard Visualization Techniques \[part 1\] workbook**](https://chandoo.org/wp/wp-content/uploads/2008/10/excel-dashboard-visualization-techniques-1xls.zip)
 and read on how this is implemented.

1.  Create an input list form control with the names of the 5 KPI (calculation!E10:E14)
2.  Define two cells to store the results of the combo boxes to select the displayed KPI (calculation!E16:E17)
3.  Insert two combo boxes (from the forms control toolbar) on the dashboard and link the input lists and the cell links accordingly.
4.  ![using-offset-fetching-2-series-data-kpi-dashboard-excel](https://chandoo.org/wp/wp-content/uploads/2008/10/using-offset-fetching-2-series-data-kpi-dashboard-excel.png "using-offset-fetching-2-series-data-kpi-dashboard-excel")Add 4 extra columns (calculation!AS:AT and calculation!AV:AW) and create OFFSET formulas to fill these new cell ranges with the values of the selected KPI (i.e. using the values in calculation!E16:E17, see 2.).
5.  Create an XY scatter chart with two data series (data source: the 4 new cell ranges, see 4.). Format the first series as circles without fill colors and the second series as circles with a grey fill color, add a legend to the chart and bring the chart to the dashboard.
6.  Reposition the chart on the dashboard (remember this trick: keeping the ALT-key pressed during resizing and repositioning makes the chart auto-fit to the cell grid underneath) and position the combo boxes.
7.  If you want to, you could easily add a trend line to the chart and display the equation and/or the R-squared value for deeper analysis of the correlation between the two KPIs.

That’s it. Play around with the new analytical feature: change the selected two KPIs, change the sort criteria, toggle the sort order or scroll up and down the dashboard table and watch the changes on the XY scatter chart.

What’s next? – Last Part of the KPI Dashboards using Excel
----------------------------------------------------------

Make sure you have downloaded the [**Excel Dashboard Visualization Techniques \[part 1\] workbook**](https://chandoo.org/wp/wp-content/uploads/2008/10/excel-dashboard-visualization-techniques-1xls.zip)

Go to next post: [Part 6: Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

Also, Checkout our [Excel Dashboards Page](http://chandoo.org/wp/excel-dashboards/)
 for more examples and resources.

_Chandoo’s note:_ Thanks Robert for another excellent post.

Please leave your comments, questions and love here, Robert is a regular reader of this blog he will be happy to respond to you as early as possible.

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/excel-dashboard-visualization-techniques-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-dashboard-visualization-techniques-1/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts & Graphs](https://chandoo.org/wp/tag/charts-graphs/)
    , [comparison charts](https://chandoo.org/wp/tag/comparison-charts/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [scatter charts](https://chandoo.org/wp/tag/scatter-charts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousReplace Radar Charts with Tables to Make Comparison Easy](https://chandoo.org/wp/excel-radar-charts-replacement-spot-matrix-download-template/)

[NextVisualizations of the Week \[Oct 10\]Next](https://chandoo.org/wp/visualizations-of-the-week-oct-10/)

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
    
    [Reply](https://chandoo.org/wp/excel-dashboard-visualization-techniques-1/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-dashboard-visualization-techniques-1/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-dashboard-visualization-techniques-1/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ