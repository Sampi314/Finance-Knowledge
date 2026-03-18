# KPI Dashboard using Microsoft Excel - Downloadable Workbook, Demo & Details

**Source:** https://chandoo.org/wp/kpi-dashboard-revisited

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

KPI Dashboard – Revisited
=========================

*   Last updated on March 25, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This post is part of [Excel Dashboard Week](http://chandoo.org/wp/tag/dashboard-week/)

Background:
-----------

In 2008, I received an email from [Robert Mundigl](http://clearlyandsimply.com/)
, which was the start of a life-long friendship. _**Robert**_ asked me if he can teach us how to make KPI dashboards using Excel. I gladly said yes because I am always looking for new ways to use Excel.

The original [KPI dashboards using Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
 article was so popular. They still help around 12,000 people around the globe every month. Many of our regular readers and members have once started their journey on Chandoo.org from these articles.

In this article, we will revisit the dashboard and give it a fresh new spin using Excel 2007.

KPI Dashboard – Reconstructed in Excel 2007
-------------------------------------------

### KPI Dashboard – Snapshot

First, take a look at the dashboard I have constructed. This uses almost the same data as Robert’s original dashboard, but adds a lot of new features etc.

![KPI Dashboard in Excel - Snapshot](https://chandoo.org/img/dashboards/dw/kpi-dashboard-revisited-snapshot.png)

### KPI Dashboard – Demo Video

\[[Watch the video on YouTube](http://www.youtube.com/watch?v=0AS9TIK1QFk)\
\]

How is this KPI Dashboard Constructed?
--------------------------------------

It would take me 2300 words and 7 cups of coffee to type out the entire instruction. So I will instead tell you what new things I have added to it and how they are done.

_Note: For a detailed step-by-step instruction, please consider joining Excel School because this is a 3 part, 120 minute lesson in our class._

### Changes to the KPI Dashboard:

_**I have made the following changes to the original dashboard:**_

*   Added a top bar where we show top 3 products in each KPI
*   Added ability to restore to original sort order (as per the input data in Data sheet)
*   Instead of showing triangle arrows, used conditional formatting arrow icons – green for values >=90th percentile and red for <= 10th percentile for any given KPI.
*   Added individual KPI targets by product (instead of same KPI targets for all products). Also, changed the bar chart visualization to show target markers.
*   Added ability to switch on/off the target indicators.
*   Added a KPI distribution chart and ability to search by any product.

![Changes to the KPI Dashboard - Excel Dashboards](https://chandoo.org/img/dashboards/dw/kpi-dashboard-changes.png)

### How are these changes made?

**Restoring original sort-order:**

For this, I have used the product numbers (values 1 to 100) in Data sheet and sorted them on ascending order. When you click on the product column’s sort button, in the background I just use the product numbers column to sort the KPIs.

**Percentile Indicators:**

This is the same technique as [alert icons in dashboard](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/)
. Just that I also showed green icons.

**Turning on / off the KPI target indicators:**

Based on the check-box setting, I return #N/A (thru NA() formula) or actual target value to the chart’s source data range. Rest of the puzzle, you can figure out.

The technique is also explained here: [Dynamic Excel Chart with Checkboxes](http://chandoo.org/wp/2010/08/31/dynamic-chart-with-check-boxes/)
.

**Search by Product & Highlight KPI values:**

For this I have used an active-x text box and linked it to a cell (L22). Then, I used COUNTIF with wild-card search to locate if a product matches the input or not. \[More on the [wild-card search technique](http://chandoo.org/wp/2010/11/01/using-wildcards-with-vlookup/)\
\]

**KPI Distribution Chart:**

This is an area chart, re-sized to fit inside the space. The red-lines are y-error bars and they are drawn for products that match the search criteria.

Download the KPI Dashboard Workbook
-----------------------------------

[**Click here to download**](https://img.chandoo.org/dashboards/dw/kpi-dashboard-revisted.xlsx)
 the Excel workbook with the KPI Dashboard.

### Thanks you Robert:

Special thanks to _Robert_ for such a beautiful dashboard. [Visit his clearlyandsimply blog](http://clearlyandsimply.com/)
 to get some more awesome dashboard / Excel ideas.

### How would you have designed the KPI Dashboard?

Share your views on the above dashboard. Also, tell me how you would have designed the same. What charts / tables will you retain. What will you remove and what will you add.

_**Share your ideas using comments.**_

### More Resources on Excel Dashboards:

*   [Excel Dashboards – Lots of examples, information and downloads](http://chandoo.org/wp/excel-dashboards/)
    .
*   [Sales Dashboards – 32 Examples & Download workbooks](http://chandoo.org/wp/2010/01/04/sales-dashboards/)
    
*   [KPI Dashboards using Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
     – 6 part tutorial
*   [Dynamic Dashboards in Excel](http://chandoo.org/wp/2010/03/16/excel-dashboard-tutorial-1/)
     – 4 part tutorial
*   [**Excel School Dashboard Program**](http://chandoo.org/wp/excel-school/)
     – Learn how to make world-class dashboards using Excel

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/kpi-dashboard-revisited/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/kpi-dashboard-revisited/#respond)
    
*   Tagged under [active-x controls](https://chandoo.org/wp/tag/active-x-controls/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [dashboard week](https://chandoo.org/wp/tag/dashboard-week/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [na()](https://chandoo.org/wp/tag/na/)
    , [percentile()](https://chandoo.org/wp/tag/percentile/)
    , [percentilerank()](https://chandoo.org/wp/tag/percentilerank/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousExecutive Review Dashboard in Excel \[Dashboard Week\]](https://chandoo.org/wp/executive-review-dashboard/)

[NextLearning Dashboards? – Go thru these 33 Recommended ResourcesNext](https://chandoo.org/wp/resources-for-making-dashboards/)

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
    
    [Reply](https://chandoo.org/wp/kpi-dashboard-revisited/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/kpi-dashboard-revisited/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/kpi-dashboard-revisited/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ