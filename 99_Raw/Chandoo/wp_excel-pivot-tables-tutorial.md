# Excel Pivot Tables Tutorial : What is a Pivot Table and How to Make one

**Source:** https://chandoo.org/wp/excel-pivot-tables-tutorial

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Excel Pivot Tables Tutorial : What is a Pivot Table and How to Make one
=======================================================================

*   Last updated on July 8, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel pivot tables are very useful and powerful feature of MS Excel. They are be used **to create instant summaries, reports and data analysis from your raw data**. 

In this page, learn all about how to create an Excel pivot table and customize it.

#### Table of Contents

What are Excel Pivot Tables?
----------------------------

A pivot table _turns_ your data into report format. Here is a sample Pivot table from sales data, showing **total sales by region.**

![Example of an Excel Pivot Table](https://chandoo.org/wp/wp-content/uploads/2019/08/example-excel-pivot-table.png)

How to create a Pivot Table?
----------------------------

We will use 2019 sales data of a fictional company. This data contains 466 rows of sales information in columns – Month, Salesman, Region, Product, No.  Customers, Net Sales, Profit / Loss. Here is a preview of our data.

![Sample data - Pivot tables in Excel](https://chandoo.org/wp/wp-content/uploads/2019/08/sample-data-excel-pivot-tables.png)

[Download the sample data & example pivot tables here.](https://chandoo.org/wp/wp-content/uploads/2019/08/excel-pivot-tables-example-file.xlsx)

To create a pivot table showing **totals sales by region**, follow these steps.

1.  Select any cell in the data.
2.  Go to Insert ribbon and click “Pivot Table” button.  
    ![Insert Pivot Table button - Excel ribbon](https://chandoo.org/wp/wp-content/uploads/2019/08/insert-pivot-table-button-excel-1.png)
3.   Click ok on the next screen.  
    ![Create Pivot Table dialog](https://chandoo.org/wp/wp-content/uploads/2019/08/create-pivottable-dialog.png)
4.  You will be taken a new spreadsheet with _blank Pivot Table canvas._  Here, using the Pivot Table Fields panel set “Regions” field to row label area, “Products” to “Filter” area and “Net Sales” to values area. See below illustration.  
    ![how to use pivot table fields - setting up a pivot table](https://chandoo.org/wp/wp-content/uploads/2019/08/how-to-use-pivot-table-fields-setting-up-a-pivot-table-1.png)

Your pivot table will be ready. We can see that “West” is our best region. This is why Pivot tables are easy for finding answers to common business questions.

Two dimensional Pivots - Row & Column fields
--------------------------------------------

You can add fields to both “Row” and “Column” label area of a pivot. Such Pivot Tables are normally called **two dimensional pivots.** Here is a demo of a two dimensional pivot table showing **Total Sales by Region & Sales Person**.

![Two dimensional pivot - demo](https://chandoo.org/wp/wp-content/uploads/2019/08/two-dimensional-pivot.png)

### Multi-dimensional Pivots - Row & Column fields

You can also add more than one item to “Row” or “Column” label area. This creates a multi-dimensional Pivot Report. Here is one such pivot report showing total sales by Region, Sales Person & Product for selected months.

![Example Pivot Report - A very detailed Pivot Table with sub-totals and totals](https://chandoo.org/wp/wp-content/uploads/2009/08/detailed-pivot-report.png)

How to format Pivot Table values?
---------------------------------

By default, numbers in Pivot Tables tend to just look like zip codes, without any proper formatting. This is easy to fix though. Simply right click on the values and use “Value Field Settings” to set up the formatting. To set currency formatting for our **Total sales by region Pivot Report,** 

1.  Go to value field settings
2.  Click on Number Format button
3.  Set up the formatting to “Currency”
4.  Done.

See this illustration.

![How to currency format pivot table values](https://chandoo.org/wp/wp-content/uploads/2019/08/formatting-pivot-table-values.png)

Sorting in Excel Pivot Tables
-----------------------------

You can easily sort pivot report by ascending or descending order of the value. To do this, just right click on the value, select Sort > and specify the order.

Here is an example of **sorted pivot report of Number of customers by Sales person**.

![Sorting a pivot table in descending order of sales](https://chandoo.org/wp/wp-content/uploads/2019/08/sorting-pivot-tables.png)

Bonus tip: Manual sorting You can also manually adjust the order of Pivot items by dragging and dropping them. [See this tip in action](https://chandoo.org/wp/custom-sort-pivot-tables/ "Sort pivot table values manually")
.

Filtering Excel Pivot Tables
----------------------------

You are looking at Regional total sales and want to know what the total is for just “RapidZoo” product. You can do this by **filtering** the pivot table. Excel offers two powerful ways to filter Pivot Tables

1.  Report filters
2.  Slicers

Both methods are illustrated below. Read on to learn how to use them.

![Filtering an excel pivot table - two methods](https://chandoo.org/wp/wp-content/uploads/2019/08/filtering-a-pivot-table-two-methods.png)

### Filtering with Report Filters

Report filter is a great way to restrict the data that is flowing to your pivot. To set them up, just add the field to “Filters” area in the fields panel. Now, using the filter button next to “Product”, select the product you want.

Here is a quick demo of report filters in action.

![Report filter demo](https://chandoo.org/wp/wp-content/uploads/2019/08/report-filter-excel-pivot-tables-demo.gif)

### Filtering with Slicers

There are a ton of cool features in Excel Pivot Tables, but slicers are hands-down the best feature. At-least, that is what I think. They make filtering and ad-hoc data analysis a breeze.

A slicer is a **visual filter.** You can add a slicer on any field by right clicking on it from the fields panel. See the illustration “Adding filters to a pivot report” from above. 

Once you have a slicer on Product, simply click on any product name to see the report for that. 

**Here is a quick demo of Pivot Table with slicers.**

![Filtering a pivot table with slicer - demo](https://chandoo.org/wp/wp-content/uploads/2019/08/filtering-with-slicers-excel-pivot-tables.gif)

Bonus Tip: Use Timeslines for date filtering When you have a date field (Month in our data), you can use special type of a slicer, called timeline. This enables you to interactively select a portion of time.

### Other kinds of filtering - Value & Label Filters

Apart from report filters & Slicers, Pivot Tables also allow you to filter by a field or value. 

**Field or Label Filter:** If you don’t want to see “Middle” region in a row label area, just click on the filter button next to “Row Labels” and uncheck the region. This type of filtering is called Label Filtering.

**Value Filter:** If you want to see just the top 2 regions by total sales, then you need a **value filter.** Simply go to filter button next to row labels and using value filters, apply a top 10 filter but set it to top 2 values by “Sum of net sales.”

Changing Calculations in Pivot Tables
-------------------------------------

The default calculation in Pivot Tables is SUM for number fields and COUNT for all others. But you can also customize the calculation easily. Just right click on the value field and choose different type of summary from right click menu.

### Changing from SUM to AVERAGE in a Pivot Table

Here is a quick illustration of how to change calculation type from “SUM” to “AVERAGE”.

![how to change pivot table calculations](https://chandoo.org/wp/wp-content/uploads/2019/08/how-to-change-pivot-table-calculations.png)

Pivot Table Layouts & Colors
----------------------------

By default, Excel Pivot Tables are in **compact layout.** This means, if you add multiple fields to row label area, they will all be shown in same column, with indentation.

You can change the layout of a pivot table to other formats too. 

*   Compact form (default)
*   Outline form
*   Tabular form

You can change the layout from **Pivot Table Design ribbon**.

![Pivot Table layout options](https://chandoo.org/wp/wp-content/uploads/2019/08/pivot-table-layout-options.png)

Here is an example of **same Pivot Table in both Compact and Tabular layouts.** 

![Compact vs. Tabular Layouts for Pivot Tables in Excel](https://chandoo.org/wp/wp-content/uploads/2019/08/compact-vs-tabular-layout-pivot-tables.png)

### Styling & colors of Excel Pivot Tables

**You can apply any formatting to the pivot tables.** MS Excel has some very good pivot table styles. Just select pivot table cells, go to Pivot Table Design ribbon. See below image to understand various options available.

![Pivot table design options](https://chandoo.org/wp/wp-content/uploads/2019/08/pivot-table-design-ribbon-options.png)

Bonus tip: Copy Pivot Tables to format quicker If you like the formatting (colors, layout etc.) of a Pivot Table and want to use the same set up for a new Pivot Table, simply copy and paste the original table. Then you can change the fields and your new Pivot will be ready.

Visualizing with Pivot Charts
-----------------------------

You can use Pivot Charts to visualize the same information in a graphic format. Here is a sample **Pivot Chart of Net Sales by Region & Product.**

![Excel Pivot Chart - Example](https://chandoo.org/wp/wp-content/uploads/2019/08/excel-pivot-chart-demo.png)

**Steps for creating a Pivot Chart:**

1.  Select any cell in the Pivot Table.
2.  Click on Insert > Chart or Analyze > Pivot Chart button.
3.  Insert the type of chart you want.
4.  You will get a Pivot Chart.

Bonus tip: Add Pivot Chart directly from data You can insert Pivot Chart directly from data. Just select your data and press Pivot Chart button in the insert ribbon (in charts area). Use Fields Panel to set up the chart.

### Interactive Pivot Chart with Slicers

Slicers make it incredibly easy to create **interactive charts.** Once you have a regular Pivot Chart, simply add a slicer to it (right click on the field in “Pivot Table Fields” area and select “Add as Slicer”). You now have an interactive Pivot Chart.

Here is a demo of **interactive Pivot Chart.** 

![interactive pivot chart with slicers](https://chandoo.org/wp/wp-content/uploads/2019/08/dynamic-pivot-chart-with-slicers.gif)

Updating Pivot Tables (Refresh)
-------------------------------

Whenever you have new data, just use “Refresh” button to update your Pivot Tables. You can find this button in multiple places.

*   Data ribbon
*   Pivot Table Analyze ribbon
*   On right clicking any Pivot Table
*   By pressing ALT+F5 (refreshes single pivot) or CTRL+ALT+F5 (refreshes all pivots)

**![Refresh and change data source options - Excel Pivot Table Analyze ribbon](https://chandoo.org/wp/wp-content/uploads/2019/08/refresh-and-change-data-source-options.png)What if you want to point Pivot to new data?**

Select any cell in the Pivot Table and from Analyze ribbon, use the “Change Data Source” button. Point input data to a new source. As long as the new data has same fields, everything will work smoothly.

Pivot Tables in Excel - Complete video tutorial
-----------------------------------------------

I have made a 21 minute video explaining how to create, format, customize, visualize, filter and refresh Pivot Tables. This video is packed with many tricks, ideas and inspiration. Check it out below.

Download - Sample data & example Pivot Tables
---------------------------------------------

[**Please click here to download the sample file**](https://chandoo.org/wp/wp-content/uploads/2019/08/excel-pivot-tables-example-file.xlsx)
 for this article. It contains fictional sales data, several example pivot tables, charts and additional resources. 

Examine the pivot table settings and use the data to learn more.

Next Steps
----------

Now that you are familiar with Pivot Tables, explore these additional pages to learn more about data analysis & reporting.

**Beginner:**

*   [Pivot Table from multiple tables – Data Model & Relationships](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    
*   [Number and Percentages in same Pivot](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/)
    
*   [5 Pivot tables to try when you have too much data](https://chandoo.org/wp/pivot-tables-from-large-data-sets/)
    
*   [Sub-totals but only on one level](https://chandoo.org/wp/selective-subtotals-in-pivot-tables/)
    
*   [Distinct count in Excel Pivot Tables](https://chandoo.org/wp/distinct-count-pivot-tables/)
    
*   [How to use Report Filters](https://chandoo.org/wp/pivot-table-report-filters/)
    

**Intermediate & Advanced Users:**

*   [All you need to know about Slicers](https://chandoo.org/wp/introduction-to-slicers/)
    
*   [6 Time Saving Pivot Table Tricks](https://chandoo.org/wp/pivot-table-time-saving-tricks/)
    
*   [Advanced Pivot Table Tricks](https://chandoo.org/wp/advanced-pivot-tables/)
    
*   [Conditional formatting for Pivot Tables](https://chandoo.org/wp/monthly-values-and-changes-pivot-table/)
    
*   [Introduction to GETPIVOTDATA](https://chandoo.org/wp/getpivotdata-in-dashboards/)
    
*   Getting started with Power Pivot – [Percentage of something calculation example](https://chandoo.org/wp/percentage-of-another-value-pivot-table/)
    

**Recommended Websites & Books:**

These are my favorite places to learn more about Pivot Tables.

**Websites:**

*   [Excel Pivot Tables page](https://www.contextures.com/CreatePivotTable.html)
     on Contextures
*   [Pivot Table tips](https://exceljet.net/pivot-table-tips)
     from Excel Jet
*   [50 things you can do with Pivot Tables](https://www.myexcelonline.com/blog/50-things-you-can-do-with-excel-pivot-tables/)
     from MyExcelOnline

**Books:**

*   [Excel Pivot Table data crunching](https://amzn.to/36RK3Cl)
     by Bill Jelen
*   [MS Excel Data Analysis and Business Modeling](https://amzn.to/2ShBzPS)
     by Wayne Winston
*   [Excel Bible](https://amzn.to/2RVN9Bf)
     by J Walkenbach

**Courses:**

*   [Excel School program by Chandoo](https://chandoo.org/wp/excel-school-program/)
    

Happy Learning.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [161 Comments](https://chandoo.org/wp/excel-pivot-tables-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-pivot-tables-tutorial/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [data](https://chandoo.org/wp/tag/data/)
    , [data processing](https://chandoo.org/wp/tag/data-processing/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot charts](https://chandoo.org/wp/tag/pivot-charts/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [spreadcheats](https://chandoo.org/wp/tag/spreadcheats/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousMake a random sentence with Excel formulas](https://chandoo.org/wp/random-sentence-excel-formula/)

[NextAdvanced Pivot Table Tricks for youNext](https://chandoo.org/wp/advanced-pivot-tables/)

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
    
    [Reply](https://chandoo.org/wp/excel-pivot-tables-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-pivot-tables-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-pivot-tables-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ