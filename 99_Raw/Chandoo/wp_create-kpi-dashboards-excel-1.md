# KPI (Key Performance Indicator) Dashboards in Excel - Tutorial [Part 1 of 6]

**Source:** https://chandoo.org/wp/create-kpi-dashboards-excel-1

---

*   [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Creating KPI Dashboards in Microsoft Excel \[Part 1 of 6\]
==========================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Creating KPI Dashboards in Microsoft Excel is a series of 6 posts by [Robert](http://www.clearlyandsimply.com/)
._

### This 6 Part Tutorial on KPI Dashboards Teaches YOU:

[](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
Creating a Scrollable List View in Dashboard  
[Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
  
[Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
  
[Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
  
[Compare 2 KPIs in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
  
[Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

**[Dashboards](http://chandoo.org/wp/management-dashboards-excel/)
 have become quite popular in the last few years** and in spite of all the Business Intelligence software products that provide dashboards, a lot of dashboards are still implemented with Microsoft Excel.

### What is a Dashboard?

According to [Stephen Few](http://www.perceptualedge.com/)
, one of the world-wide leading authorities on visualization and dashboard design,

> **a dashboard is a visual display of the most important information \[…\] which fits entirely on a single computer screen** \[…\]  
> (Information Dashboard Design, 2006)

### The Scrolling Problem

Fitting on a single computer screen is the challenge this post will solve. Imagine you have a large list of 100 or more items (e.g. products, sales regions, etc.) with several corresponding Key Performance Indicators (e.g. prices, costs of goods sold, sales, etc.) and you want to show this in a table on your management dashboard. The whole table will not fit on a single computer screen anymore. Most of the time it will be sufficient to show the first or largest 10 items only. But what if the user of your dashboard wants to scroll down the table and see the rest of the data? Sure, you might teach him to go to the sheet with the data and scroll up and down there. But this is not convenient, not user-friendly, insecure and not the purpose of a dashboard.

### The solution

![kpi-dashboard-excel-with-scrolling](https://chandoo.org/wp/wp-content/uploads/2008/08/kpi-dashboard-excel-scrolling.gif "kpi-dashboard-excel-scrolling")

The table on our dashboard doesn’t need much explanation. The only thing that differs from millions of other numeric tables in Excel is the slider scroll-bar between the names of the items and the data. This scroll-bar allows the user of the dashboard to walk through the whole list and see all items without leaving the dash-board. The table is small and leaves a lot of space for tables or charts on the dashboard.

**[Download the excel sheet containing KPI Dashboard solution](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-table-scroll.xls)
 to learn this better.**

### The implementation

*   **First have our raw data ready in a separate sheet**, this is the easy step, you know how to get your data in to one sheet. So skip to next one.
*   **Next create a 10 row table for the dash board**

![forms-toolbar-spreadsheets-excel](https://chandoo.org/wp/wp-content/uploads/2008/08/forms-toolbar-spreadsheets-excel.png "forms-toolbar-spreadsheets-excel")

*   **Insert a scroll bar form control** Go to Menu > view > tool bars and select “forms” to see the forms tool bar. Select the scrollbar control from forms tool bar and draw one on your spreadsheet. ![scroll-bar-form-control](https://chandoo.org/wp/wp-content/uploads/2008/08/scroll-bar-form-control.png "scroll-bar-form-control")
*   **Assign the scroll bar control to a cell** right click on it and select format control option. In the dialog box, go to “control” tab and adjust the values as shown below:  
    ![scroll-bar-contrl-excel-properties](https://chandoo.org/wp/wp-content/uploads/2008/08/scroll-bar-contrl-excel-properties.png "scroll-bar-contrl-excel-properties")
*   **Finally write OFFSET() formula** to display any consecutive 10 values in our scrollable table: OFFSET is used on the dashboard to bring back those 10 lines from the sheet with the raw data that are selected by using the scroll bar. A sample formula is shown here: `=OFFSET(Data!E5,Calculation!$D$5,0)` where Data!E5 refers to the column containing the required data, Calculation!$d$5 has the current scroll bar value. That is all, you will have a small table that you can use to see all data using scroll

### What next?

Make sure you have downloaded **[KPI Dashboard solution workbook](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-table-scroll.xls)
** to learn this better.

Read the next article in this series:[Part 2: Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)

Also, Checkout our [Excel Dashboards Page](http://chandoo.org/wp/excel-dashboards/)
 for more examples and resources.

_**Chandoo’s note:** Robert is a regular reader and commenter on this blog. Drop your comments / questions here and I am sure he will answer them 🙂_

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [245 Comments](https://chandoo.org/wp/create-kpi-dashboards-excel-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/create-kpi-dashboards-excel-1/#respond)
    
*   Tagged under [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    
*   Category: [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousDell tells me to buy a finger print reader in order to have another color on the system](https://chandoo.org/wp/dell-finger-print-reader/)

[NextDisplay symbols in excel chart axisNext](https://chandoo.org/wp/display-symbols-excel-chart/)

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
    
    [Reply](https://chandoo.org/wp/create-kpi-dashboards-excel-1/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/create-kpi-dashboards-excel-1/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/create-kpi-dashboards-excel-1/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ