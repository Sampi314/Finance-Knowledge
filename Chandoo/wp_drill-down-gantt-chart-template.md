# Excel Gantt Chart with Drill-down feature » Templates

**Source:** https://chandoo.org/wp/drill-down-gantt-chart-template

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

Project Plan – Gantt Chart with drill-down capability \[Templates\]
===================================================================

*   Last updated on July 29, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Gantt charts are useful for visualizing a project’s timeline and activity flow**. In this article, learn how to create an interactive project **gantt chart with drill-down capability** using Excel. Here is a demo of the gantt chart we will be creating.

![Project Plan Gantt chart with drill down capability in Excel](https://chandoo.org/wp/wp-content/uploads/2020/07/interactive-project-gantt-chart-demo.gif)

Download the Drill-down Gantt Chart Template
--------------------------------------------

[**Please click here to download the gantt chart template**](https://chandoo.org/wp/wp-content/uploads/2020/07/interactive-gantt-chart.xlsx)
. Just change the input data and click on “Refresh” button from Data ribbon to update the gantt chart.

If you want more project management templates, [please click here](https://chandoo.org/pmt/pmt-index-1.html)
.

Step by Step Tutorial - Gantt Chart with Drill-down
---------------------------------------------------

Please watch below short tutorial to learn how to create an interactive multi-level project gantt chart in Excel. Alternatively, just read on to get the instructions.

If you want to create a similar gantt chart from your data, Please follow below steps. 

### Step 1: Get your data

You need _at least_ these four columns of data. 

![sample data - interactive gantt chart](https://chandoo.org/wp/wp-content/uploads/2020/07/sample-data-interactive-gantt-chart.png)

### Step 2: Make a pivot table from the data

Insert a pivot table from this data. Set it up as shown below. You need,

*   Slicer on “module”
*   Activity on row labels
*   Start date min on values
*   End date max on values

Related: [Learn how to create Pivot Tables in Excel](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
.

![pivot table for the gantt chart](https://chandoo.org/wp/wp-content/uploads/2020/07/pivot-table-for-the-gantt-chart.png)

### Step 3: Create a gantt chart empty outline

In a new worksheet, set up gantt chart outline like below.

You need,

*   4 columns to display activity, start date, end date and duration
*   another 90 narrow columns to show the project plan. Feel free to adjust the number of columns based on your needs.

![Empty gantt chart grid](https://chandoo.org/wp/wp-content/uploads/2020/07/empty-gantt-chart-grid.png)

### Step 4: Making the left side of gantt chart

The left side portion of our project plan is rather simple to make. We just need to refer to Pivot Table values to get first three columns (Activity, Start and Finish).

We can then calculate the duration using =NETWORKDAYS(start, finish)

After the duration is calculated, add conditional formatting > data bars to it, so that we can easily spot activities that take too long to complete.

![gantt chart construction - left side](https://chandoo.org/wp/wp-content/uploads/2020/07/gantt-chart-construction-left-side.png)

### Step 5: Gantt chart grid (right side portion)

Now that our gantt chart is ready on the left, let’s complete the grid. 

Start by calculating the earliest project start date using min formula =MIN(plan\[Start date\])

Place this formula in the grid top left cell, as shown below.

![project plan gantt chart construction - right side](https://chandoo.org/wp/wp-content/uploads/2020/07/project-plan-gantt-chart-construction-right-side.png)

Calculate remaining 89 dates by adding +1 working day. Use =WORKDAY(previous date, 1) formula for this.

This will give us a bunch of dates.

Use the next two rows to show month & day portion of this date by referring to the date calculation row. As the cells are too small, merge 2 or 3 of them and show the values. 

Now that all the dates are ready, let’s figure out the logic for making gantt chart view.

![conditional formatting rule for gantt chart](https://chandoo.org/wp/wp-content/uploads/2020/07/conditional-formatting-rule-for-gantt-chart.png)

As shown above, we need a rule to highlight any cell if the date in top row falls between start and finish dates for the corresponding project activity.

To do this, select the entire grid of 100 rows x 90 columns and apply a new conditional formatting rule.

Use “formula” type rule and apply this formula.

\=MEDIAN($C6, $D6, M$3) = M$3

_Adjust cell references based on your gantt chart setup._

Related: [Using MEDIAN formula to check between condition in Excel](https://chandoo.org/wp/between-formula-excel/)

![conditional formatting rule - excel gantt chart](https://chandoo.org/wp/wp-content/uploads/2020/07/conditional-formatting-rule-excel-gantt-chart.png)

Apply necessary formatting and your gantt chart will be ready.

### Step 6: Move the slicer to the gantt chart worksheet

This is the last and easiest step.

Just cut and paste the slicer near the gantt chart. Your interactive chart is ready.

![Project Plan Gantt chart with drill down capability in Excel](https://chandoo.org/wp/wp-content/uploads/2020/07/interactive-project-gantt-chart-demo.gif)

**Bells & whistles:**

*   You can add a conditional formatting rule to highlight current date
*   Another rule to highlight alternative rows (zebra-shading)
*   Adjust the conditional formatting rule to show **completed activities** in a different color.

How to update the Gantt Chart?
------------------------------

When ever you have new data, simply update the input data worksheet. Then refresh pivot tables (shortcut: Alt+Ctrl+F5). Your Gantt chart will be updated too.

Download the Drill-down Gantt Chart Template
--------------------------------------------

[**Please click here to download the gantt chart template**](https://chandoo.org/wp/wp-content/uploads/2020/07/interactive-gantt-chart.xlsx)
. Just change the input data and click on “Refresh” button from Data ribbon to update the gantt chart.

If you want more project management templates, [please click here](https://chandoo.org/pmt/pmt-index-1.html)
.

Questions or Suggestions?
-------------------------

Got some questions or issues when using this template? Have a suggestion for this Gantt Chart? Please post them in the comments section.

Also check out:

*   [Project Status Dashboard in Excel](https://chandoo.org/wp/project-management-templates/project-dashboards/)
    
*   [Project Portfolio Dashboard in Excel](https://chandoo.org/wp/design-project-portfolio-dashboard/)
    
*   [Risk Management tracker + chart in Excel](https://chandoo.org/wp/excel-risk-map-template/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/drill-down-gantt-chart-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/drill-down-gantt-chart-template/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [median() formula](https://chandoo.org/wp/tag/median-formula/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousIntroducing Power BI Play Date – Online class to master Power BI (oh yeah, Power Query & Power Pivot too)](https://chandoo.org/wp/power-bi-play-date-is-here/)

[NextPower Query Tutorial – What is it, How to use, Full examples, Tips & TricksNext](https://chandoo.org/wp/power-query-tutorial/)

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
    
    [Reply](https://chandoo.org/wp/drill-down-gantt-chart-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/drill-down-gantt-chart-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/drill-down-gantt-chart-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ