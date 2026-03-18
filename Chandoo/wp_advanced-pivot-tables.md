# Advanced Pivot Table Tricks for you » Data Analysis » Chandoo.org

**Source:** https://chandoo.org/wp/advanced-pivot-tables

---

*   [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

Advanced Pivot Table Tricks for you
===================================

*   Last updated on February 27, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel Pivot tables make data analysis and visualization easy. With the help of these **advanced pivot table skills,** you can create powerful data analytics and reports.  

New to Pivot Tables? If you are new to Pivot Tables, check out this excellent [introduction to Pivot Tables page](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
. ×

#### Table of Contents

#1 - One Slicer, Two Pivots
---------------------------

**[Slicers](https://chandoo.org/wp/introduction-to-slicers/)** are visual filters. You can filter a pivot table or chart by adding  a slicer on any field. Do you know that you can link slicer to more than one pivot table? Yes, this advanced usage of slicers makes it handy to update multiple reports with one click.

To link multiple pivot tables to same slicer:

1.  Right click on the slicer and select “Report connections”
2.  Check pivot tables that you want to connect.
3.  Done.

You can use the same approach to link multiple pivot tables with a timeline too.

**Here is a video tutorial explaining this trick.**

#2 - Distinct Count
-------------------

We can easily get count, sum, average and median from our data with Pivot Tables. But what about **distinct counts?** You can use **data model** feature of Pivot tables to get distinct count. 

To get distinct count in pivot tables:

1.  Select your data and go to insert pivot table screen.
2.  On that screen, enable “Add to data model” option.
3.  Click ok to insert pivot table.
4.  Add the field you want to distinct count to the value field area of the pivot table.
5.  Go to value field settings and select summarize by “Distinct count”

Here is a video explaining the process.

#3 - Value and Percent in same Pivot
------------------------------------

Let’s say you are looking at a pivot report detailing total sales by region. You want to know how much each region’s sales are as a percent of total sales too. That is you want both value and percent in the same report?

Simple, just add the sales field to values area again and this time use “show value as” feature to display number as **% of column total**.

Here is a video explaining this trick.

#4 - Layout Tricks
------------------

By default pivot tables are in **compact layout.** But you can change the layout, appearance and position of fields to create completely new reports. In this video tip, I will show you several powerful layout ideas to try next time you are making a pivot table. 

#5 - Two Tables, One Pivot
--------------------------

We can all create pivot reports from single tables or ranges of data. What if you need to create a pivot from data that is in two or more tables? You can use **“Data Model”** feature of Excel to connect multiple tables and create pivots from them. This technique opens up doors for advanced data analysis with ease.

To create pivot reports from multiple tables,

1.  **Set up your data as tables.** If the data is in ranges, simply create tables from them using CTRL+T or Insert > Table option. \[Related: [Introduction to Excel Tables](https://chandoo.org/wp/data-tables/)\
    \]
2.  **Set up relationships to create data model:** Imagine one table of your data as Sales information and other table has Customer information. You can link them up. To set up the relationship, just go to Data ribbon and click on relationship button. \[Related: [Introduction to Excel Relationships](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)\
    \]
3.  **Insert a pivot table:** Go ahead and insert a pivot table from any of your tables. Make sure check the “Add to data model” option at the bottom of insert pivot screen.
4.  **Create pivots from multiple tables.**  Now you can mash-up fields from any table to create complex business reports easily.

Here is a video summarizing the whole process with few demoes. 

#6 - Two Files, One Pivot
-------------------------

You already know how to make a pivot from data in one file. How about **creating a pivot with data from multiple files**? You can use Excel Power Query to connect to multiple files and fetch the data. We can then load this data in to “Data model” and create pivot tables from it easily.

**To make pivot tables from data in multiple files:**

1.  **Use “Get & Transform data” option** in Excel data ribbon to connect to your source data files. These can be either spreadsheets or database tables or web pages etc.
2.  **Load data in to data** **model** from Power Query so that Excel can access this data.
3.  **Insert Pivot Table** from the data model

\[Related: [Introduction to Power Query](https://chandoo.org/wp/resources/introduction-to-power-query/)\
\]

Watch this video to understand how to make pivots from multiple files.

#7 - Top 10 Filter
------------------

By default Pivot Tables will show all of your data. What if you want to limit the information to just top 10 records. For example, you want to see which of the sales persons are top 10 in a given region? You can use **value filters** to easily set up such conditions. 

**To set up top 10 value filter:**

1.  Create your pivot table so that all data shows up.
2.  Go to filter on the row (or column label) area. Select Value filter > top 10
3.  Set up the criteria for filtering. You can switch to “Bottom” to see bottom 10 values too. 

Here is a video explaining the process of top 10 filtering.

#8 - Measures & DAX with Power Pivot
------------------------------------

Excel Data Model is not just for connecting multiple tables and pivoting them. Here is a secret: You can use data model to create **power pivot reports too.** You can apply extra calculations with DAX (Data Analysis Expressions) syntax. These calculations are called **measures.** 

\[Related: [What is Power Pivot?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)\
\]

Here is a quick lesson on **DAX & Measures for Excel.**

#9 - Grouping Data
------------------

Let’s say you have Sales data at daily level, but you want to see totals (or averages) by month. You can use **grouping** feature of Excel pivot tables to quickly **aggregate** data to monthly or quarterly or yearly level. 

While grouping is a powerful feature of Excel pivot tables, it is not universal. If you have a data model driven pivot, then you have limited grouping choices available (dates can be grouped, but other fields won’t work).

In this trick, I will share two techniques for setting up grouping in Pivot tables to address these concerns.

### #9.1 - Grouping Data without Data Model

If your pivot tables are not from data model, you can group any fields.

*   Dates can be grouped in to days / months / quarters / years
*   Numbers can be grouped by chunks
*   Text can be grouped by selecting items on the report

Here is a video detailing grouping options for _non-data-model_ pivots.

### #9.2 - Grouping Data WITH Data Model

If your pivot tables are part of data model, then you have limited grouping choices. In Excel 365 / 2019, 

*   You can group by dates

In all other versions of Excel 

*   You cannot group by on any field.

The best option for all versions of Excel is to create additional tables and link them up in the data model to **_mimic_** grouping behavior. This can be done easily with the help of Power Query.

In this video, I will show you few options to generate groupings from data using Power Query.

#10 - Conditional Formatting for Pivots
---------------------------------------

You may already know about **Excel Conditional Formatting.** But do you know that similar rules can be applied to Pivot Tables too? 

Yes, conditional formatting for pivots can make them pretty and presentable. My favorite types of CF for Pivots are,

*   Heatmaps (colorscales)
*   Databars
*   Icons

It is very easy to add conditional formatting to a pivot report. Just follow below steps.

1.  Select any cell with value field for which you want to apply conditional formatting.
2.  From Home > Conditional Formatting, apply the format you want.
3.  Initially, the rule will be applied only to the selected cell, But Excel will show a prompt giving choices to change the region. Select the last option (unless you want CF for grand-totals too).

Here is a video explaining some conditional formatting tricks for Pivot Tables.

#11 - Interactive Pivot Charts
------------------------------

You can turn any Pivot Table into a chart easily. With the power of Slicers and Timelines, you can quickly **create interactive charts in Excel**. Such charts provide intuitive and awesome experience to your users. 

**To create an interactive pivot chart:**

1.  Create a regular pivot chart (you can add one from a pivot table or create a pivot chart directly from your data)
2.  Add a slicer or timeline
3.  Now the chart will change every-time you interact with the slicer.

Pro tip: Multiple slicer + chart combinations You can link more than one slicer to a chart and more than one chart to a slicer. This can create truly immersive and powerful analytics for your business.

Here is a video explaining how to create and use **interactive pivot charts.**

#12 - Dashboard with Pivot Tables
---------------------------------

**Dashboards provide complete overview of a business in one view.** However, they are usually complex and tricky to create. But we can use Power Query Excel Data Model, Measures, Pivot Tables, Slicers and Pivot Charts to create **business dashboards quickly**.

Here is a call center dashboard built using all the **advanced pivot table tricks** you have seen so far. 

[![Dashboard with Excel Pivot Tables](https://chandoo.org/wp/wp-content/uploads/2020/02/dashboard-with-pivot-tables.png)](https://chandoo.org/wp/wp-content/uploads/2020/02/dashboard-with-pivot-tables.png)

**How to create a dashboard with Pivot Tables**

1.  Identity information goals for your dashboard and list them down.
2.  Create a mock-up (rough sketch) of your dashboard on paper or paint.
3.  Gather all the necessary data and set up data model (use Power Query if needed)
4.  Calculate the numbers using Pivot Tables (and simple formulas if needed)
5.  Insert a worksheet for the dashboard and place items on it by linking them to the pivot tables.
6.  Add necessary charts, conditional formats
7.  Insert slicers / timelines as needed.
8.  Include key messages + alerts as needed.
9.  Format everything.

While this process may look simple, it requires a fair bit of thought and execution. I created a detailed video explaining the steps and construction for our call center dashboard.  Please watch it below to understand everything.

Resources + Next Steps
----------------------

### Downloads

[Please click here to download the files](https://chandoo.org/wp/wp-content/uploads/2020/02/adv.-pivot-table-tricks.zip)
 for **advanced pivot tables page.** In the download (zipped file), you will find 4 workbooks:

*   For non-data-model pivot table tricks – adv. pivot table tricks – 1
*   For data model pivot table tricks + dashboard – adv. pivot table tricks – 2
*   Refer to the two files in “Data for Power Query” folder for sample data.

### Resources for more Pivot Table goodness

Pivot Tables make data analysis and reporting easy. In this page, I have covered a heap of techniques. But if you are hungry for more, check out below pages too.

**Beginner:**

*   [Pivot Table from multiple tables – Data Model & Relationships](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    
*   [Number and Percentages in same Pivot](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/)
    
*   [5 Pivot tables to try when you have too much data](https://chandoo.org/wp/pivot-tables-from-large-data-sets/)
    
*   [Sub-totals but only on one level](https://chandoo.org/wp/selective-subtotals-in-pivot-tables/)
    
*   [Distinct count in Excel Pivot Tables](https://chandoo.org/wp/distinct-count-pivot-tables/)
    
*   [How to use Report Filters](https://chandoo.org/wp/pivot-table-report-filters/)
    

**Intermediate & Advanced Users:**

*   [All you need to know about Slicers](https://chandoo.org/wp/introduction-to-slicers/)
    
*   [Introduction to GETPIVOTDATA](https://chandoo.org/wp/getpivotdata-in-dashboards/)
    
*   Getting started with Power Pivot – [Percentage of something calculation example](https://chandoo.org/wp/percentage-of-another-value-pivot-table/)
    

**Recommended Websites & Books:**

These are my favorite places to learn more about Pivot Tables.

**Websites:**

*   [Excel Pivot Tables page](https://www.contextures.com/CreatePivotTable.html)
     on Contextures
*   [101 Advanced Pivot Table tips](https://www.howtoexcel.org/pivot-tables/pivot-table-tips-and-tricks/)
     on HowtoExcel 
*   [50 things you can do with Pivot Tables](https://www.myexcelonline.com/blog/50-things-you-can-do-with-excel-pivot-tables/)
     from MyExcelOnline

**Books:**

*   [Excel Pivot Table data crunching](https://amzn.to/36RK3Cl)
     by Bill Jelen
*   [MS Excel Data Analysis and Business Modeling](https://amzn.to/2ShBzPS)
     by Wayne Winston
*   [Excel Bible](https://amzn.to/2RVN9Bf)
     by J Walkenbach

### Next Steps

If you found these examples and tips on Advanced Pivot Tables useful, you will love my **online Excel Training Program**. In this comprehensive, step-by-step course, you will learn below topics:

*   Power Query for data management
*   Tables & formatting
*   Formulas for data analysis
*   Relationships & Pivots
*   Charting & Advanced story telling
*   Time saving tips & tricks
*   Pro user techniques
*   Dashboard Reporting

If all of this sounds exciting, [please check out Excel School program page](https://chandoo.org/wp/excel-school-program/)
 for more information & sign up today.

[Tell me more about Excel School](https://chandoo.org/wp/excel-school-program/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/advanced-pivot-tables/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/advanced-pivot-tables/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [advanced pivot tables](https://chandoo.org/wp/tag/advanced-pivot-tables/)
    , [call centre dashboard](https://chandoo.org/wp/tag/call-centre-dashboard/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [data model](https://chandoo.org/wp/tag/data-model/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousExcel Pivot Tables Tutorial : What is a Pivot Table and How to Make one](https://chandoo.org/wp/excel-pivot-tables-tutorial/)

[NextHow-to create an elegant, fun & useful Excel Tracker – Step by Step TutorialNext](https://chandoo.org/wp/create-an-excel-tracker/)

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
    
    [Reply](https://chandoo.org/wp/advanced-pivot-tables/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/advanced-pivot-tables/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/advanced-pivot-tables/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ