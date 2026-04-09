# How to show monthly values & % changes in one pivot table - Excel Pivot Table Examples

**Source:** https://chandoo.org/wp/monthly-values-and-changes-pivot-table

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Show monthly values & % changes in one pivot table
==================================================

*   Last updated on November 6, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

[Pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
 are great help when analyzing lots of data. One of the common questions managers & analysts ask (when looking at monthly sales data for example) is,

> _How is the monthly performance of our teams (or regions, products etc.)?_

A pivot report can answer this question in a snap.

![A typical Monthly sales report using pivot tables - this gives incomplete analysis](https://img.chandoo.org/pivot/monthly-sales-by-sales-person.png "A typical Monthly sales report using pivot tables - this gives incomplete analysis")

But the answer is incomplete!

Why? Because, _we don’t want sum of sales by month & sales person alone_. We want to **know their performance!** _Something like below:_

![Show monthly values & % changes in one pivot report - Excel Pivot Table examples](https://img.chandoo.org/pivot/monthly-values-and-percentage-changes-pivot-report.png "Show monthly values & % changes in one pivot report - Excel Pivot Table examples")

### Performance eh?!? How to measure it?

There are many ways to measure performance. For our monthly sales data, we can measure performance by comparing,

*   Sales with targets
*   This month value with previous month value
*   This month value with same month last year value
*   One person’s sale with rest of team etc.

One of the most common ways to measure performance in situations like this is to see _**how this months value has changed compared to previous month**_.

How to show monthly values &  % changes in pivot?
-------------------------------------------------

Do you know that with just a few clicks, we can add % changes to our pivot? Follow these steps:

1\. Create a pivot report with months & sales persons (or months & products, months & regions etc.)

2\. Add Net sales (or any other metric) to value field area of pivot report

3\. Now, add net sales once again to value field area

That is right. You can add same metric more than once to pivot table value field area.

At this point, our report looks like this:

![Add same metric two times to the pivot report - this is how it looks after we are done](https://img.chandoo.org/pivot/adding-same-metric-twice-to-pivot-table.png "Add same metric two times to the pivot report - this is how it looks after we are done")

![Showing monthly differences in pivot report using value field settings](https://img.chandoo.org/pivot/showing-monthly-differances-in-pivot-report-value-field-settings.png "Showing monthly differences in pivot report using value field settings")4\. Right click on 2nd value and choose value field settings.

5\. Click on Show values as tab and follow below steps. (see image aside)

1.  Choose **“% Difference from”** from the drop down
2.  Select Month as base field
3.  Select (previous) as base item
4.  Click ok

**_This will show % changes with respect to previous month in the pivot report!_**

**![Showing monthly values & % difference in one pivot report - end result](https://img.chandoo.org/pivot/showing-%25difference-from-previous-month-pivot.png "Showing monthly values & % difference in one pivot report - end result")  
**

Extending this to make it even more awesome
-------------------------------------------

### 1\. Clean up the titles

Change the titles to Sales & % change. To do this, just select the first column title and type over. Repeat for 2nd column.

### 2\. Add conditional formatting

Select any cell in the % change column. Go to Home > Conditional Formatting > New rule

\[Resource: [Introduction to Excel Conditional Formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)\
, [more](http://chandoo.org/wp/tag/conditional-formatting/)\
\]

**Specify the rule as mentioned in below illustration.**

![Conditional formatting monthly sales pivot report - instructions](https://img.chandoo.org/pivot/conditional-formatting-pivot-tables.png "Conditional formatting monthly sales pivot report - instructions")

### 3\. Show just icons

We can go one more step and show just icons. **Since pivot tables show tool tips on hover**, we can easily find % change for any month / sales person by just pointing on that cell.

![Pivot table tool tip demo](https://img.chandoo.org/pivot/pivot-table-tool-tips-demo.gif "Pivot table tool tip demo")

Finalized monthly report
------------------------

Our final report looks like this:

![Show monthly values & % changes in one pivot report - Excel Pivot Table examples](https://img.chandoo.org/pivot/monthly-values-and-percentage-changes-pivot-report.png "Show monthly values & % changes in one pivot report - Excel Pivot Table examples")

Download Example Pivot Report
-----------------------------

[**Click here to download this example pivot report**](https://img.chandoo.org/pivot/show-monthly-sales-and-change-in-same-pivot-table.xlsx)
. Examine various settings & conditional formats to learn this better.

How do you use value field calculations in Pivot reports?
---------------------------------------------------------

Although most of my pivots use simple sum or count type of summaries, often I use custom calculations like % difference from, running total , % of row etc. to understand the data better. These are very simple to setup yet give powerful insights.

What about you? Do you use value field settings to modify your pivot reports? What other summary techniques you use? _**Please share your tips, ideas using comments.**_

More on Pivot Tables
--------------------

Along with formulas, Pivot tables are best friends of Excel analysts. They can take massive amounts of data, process and summarize in just a few clicks. To learn more about them, use below resources.

*   Tutorial: [Introduction to Excel Pivot Tables](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    
*   Resource: [Pivot tables – examples, tips & information](http://chandoo.org/wp/excel-pivot-tables/)
    
*   Case study: [Analyzing non-performing customers using pivot tables](http://chandoo.org/wp/2012/10/03/using-pivot-tables-to-find-out-non-performing-customers/ "Using pivot tables to find out non performing customers")
    
*   Feature: [Using slicers to setup quick dynamic dashboards](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
    
*   Training: **[Join Excel School & become a kick-ass analyst](http://chandoo.org/wp/excel-school/)
    **

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [54 Comments](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pivot table field settings](https://chandoo.org/wp/tag/pivot-table-field-settings/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousWrite a formula to check if two dates are in same month? \[homework\]](https://chandoo.org/wp/two-dates-in-month-check/)

[NextHighlight Quarters, Weekends in pivot reports using styles \[quick tip\]Next](https://chandoo.org/wp/highlight-quarters-weekends-in-pivot-reports/)

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
    
    [Reply](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ