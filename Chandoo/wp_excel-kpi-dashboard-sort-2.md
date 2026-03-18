# Creating Key Performance Indicator (KPI) Dashboards in Microsoft Excel [Part 2 or 6] - Adding Sort Feature

**Source:** https://chandoo.org/wp/excel-kpi-dashboard-sort-2

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Creating KPI Dashboards in Microsoft Excel \[Part 2 or 6\] – Adding One Click Sort
==================================================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Creating KPI Dashboards in Microsoft Excel is a series of 6 posts** by [**_Robert_**](http://www.clearlyandsimply.com/)
 from Munich, Germany.

### This 6 Part Tutorial on KPI Dashboards Teaches YOU:

[Creating a Scrollable List View in Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
  
[](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
Add Ability to Sort on Any KPI to the Dashboard  
[Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
  
[Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
  
[Compare 2 KPIs in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
  
[Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

* * *

The Challenge – Sorting
-----------------------

With the post [KPI Dashboard – Setting up a Scrollable Table](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
 we started a little series of posts on how to create interactive dashboard tables with Microsoft Excel. Showing an extract of a longer list of items and enabling the user to scroll up and down was only the first step. Allowing deeper data analysis on the executive dashboard definitely needs more features. One of the most simple but common techniques for data analysis is sorting. Again we want to enable the user to select the sort criteria and see the results immediately without leaving the dashboard. That is: no need to go to the sheet with the raw data, no need to select ranges, no need to use the sort commands on the Excel menu or ribbon. And of course we want to do this without using VBA.

The Solution
------------

![management-dashboard-scroll-microsoft-excel-animated](https://chandoo.org/wp/wp-content/uploads/2008/08/kpi-dashboard-scroll-microsoft-excel-animated.gif "management-dashboard-scroll-microsoft-excel-animated")

The table on our KPI dashboard looks almost the same as the first one, except the 5 option buttons to select the sort criteria beneath the column headers and the fact that the selected column is highlighted with a darker fill color.

**Download the excel file with [KPI Dashboards – Scroll and Sort](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-table-scroll-and-sort.xls)
 and read below to find how it is done.**

The implementation
------------------

After some smaller changes on the dashboard, like adding the option buttons, linking them to the same cell and adding simple conditional formatting to the columns, the interesting part is the sorting algorithm on the sheet “calculations”. There are various solutions for sorting in excel using formulas. Most of them are use array formulas, definitely the most elegant way of doing this, but hard to understand. The step-by-step solution with several “help columns” may not be as elegant as an array formula, but it will probably be easier to understand.

**This is how the dashboard sorting works:**

![kpi-how-table-is-sorted-using-excel-functions](https://chandoo.org/wp/wp-content/uploads/2008/08/kpi-how-table-is-sorted-using-excel-functions.png "kpi-how-table-is-sorted-using-excel-functions")

*   Get the relevant data (depending on the sort criteria) by using the function OFFSET (column E)
*   Make sure to have a list with unique entries by adding a very small number (column F)
*   Sort the list using the function LARGE (column G)
*   Use MATCH to find the corresponding position of every value within the unsorted list (column H)
*   Put together the whole data table in a sorted form by using the results in column H and OFFSET (columns (J to O)

We are almost there. All we have to do now is changing the starting references in the OFFSET-functions on the dashboard (refer to row 9 on sheet calculation instead of row 5 on sheet data). That is all.

Final remarks
-------------

If you are using Excel 2007, you will notice that the conditional formatting of the cells underneath the option buttons will behave somehow strangely when clicking on another button. If you scroll down until the range is out of sight and scroll back again, everything looks fine. This doesn’t happen with Excel 2003, so it seems to be a bug in Excel 2007.

What next?
----------

[Download the KPI Dashboards Excel and learn](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-table-scroll-and-sort.xls)

Read the next post in this series: **[Part 3: Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
**

Also, Checkout our [Excel Dashboards Page](http://chandoo.org/wp/excel-dashboards/)
 for more examples and resources.

> **Update on Aug 28, 2008** [_Justin_ commented](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/#comment-20118)
>  that it would be better if the sort order could be reversed so that you can analyze bottom 10 of any KPI using the dashboard. _Robert_ is kind enough to oblige the request. He sent me another excel with sort enhancement. [Download](https://chandoo.org/wp/wp-content/uploads/2008/08/dashboard-table-scroll-and-sort-enhanced.xls)
>  it if you want to see this.

* * *

_**Chandoo**__**‘s note:** Robert is a regular reader of this blog. Leave your comments / questions / love here and I am sure he will respond during free time._

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [94 Comments](https://chandoo.org/wp/excel-kpi-dashboard-sort-2/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-kpi-dashboard-sort-2/#respond)
    
*   Tagged under [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel links of the week – weekend without wire \[Aug 26\]](https://chandoo.org/wp/microsoft-excel-links/)

[NextWhat they dont teach you in any school – AppreciationNext](https://chandoo.org/wp/appreciation-life-skill/)

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
    
    [Reply](https://chandoo.org/wp/excel-kpi-dashboard-sort-2/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-kpi-dashboard-sort-2/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-kpi-dashboard-sort-2/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ