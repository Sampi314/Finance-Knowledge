# Dynamic Chart Ranges in Excel - How to & Tutorial

**Source:** https://chandoo.org/wp/dynamic-chart-data-series

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Making a chart with dynamic range of values
===========================================

*   Last updated on November 11, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know that to make a chart we must specify a range of values as input.

**But what if our range is dynamic and keeps on growing or shrinking.** You cant edit the chart input data ranges every time you add a row. Wouldn’t it be cool if the ranges were dynamic and charts get updated automatically when you add (or remove) rows?

Well, you can do it very easily using excel formulas and named ranges. It costs just $1 per each change. 😉

Ofcourse not, there are 2 ways to do this.

The easiest way to make charts with dynamic ranges
--------------------------------------------------

If you are using Excel 2003 or above you can [create a data table](http://chandoo.org/wp/2009/09/10/data-tables/)
 (or list) from the chart’s source data. This way, when you add or remove rows from the data table, the chart gets automatically updated.

_**See the below screencast to understand how this works**_

![Make Dynamic Charts using Tables](https://chandoo.org/img/c/make-dynamic-charts-using-tables.gif)

Using OFFSET formula to make dynamic ranges for chart data
----------------------------------------------------------

For some reason if you cannot use data tables, the next method is to use [OFFSET formula](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 along with named ranges.

![Make Dynamic Charts using OFFSET formula](https://chandoo.org/img/c/make-dynamic-charts-use-offset-formula.gif)

We all know that OFFSET formula is used to get a range of cells by passing on starting point and number of cells to offset. Steps for creating dynamic chart ranges using OFFSET formula:

### 1\. Identify the data from which you want to make dynamic range

![Input Data for the Chart Series](https://chandoo.org/img/c/input-data-for-the-dynamic-chart.png)In our case the data should be filled in the following table. As user keeps on adding new rows we will have to update our chart’s source data.

Lets assume the data table is in the cell range: $F$6: $G$14

### 2\. Write OFFSET formulas and create named ranges from them

Ok, the problem is that as and when we add a row at the end (or remove a row), we should update the chart’s data range. For this, we can use OFFSET formula.

A refresher on how to use OFFSET formula:

![how-offset-excel-formula-works](https://chandoo.org/wp/wp-content/uploads/2008/11/how-offset-excel-formula-works.png "how-offset-excel-formula-works")

### 3\. Create a new named range and type OFFSET formula

Create a new named range and in the “refers to:” input box, type the OFFSET formula that would generate a dynamic range of values based on no. of sales values typed in the column G. I have used the below formula. You can write your own or use the same technique.

\=OFFSET($G$6,0,0,COUNTA($G$6:$G$14),1)

Set the named range’s name as “sales\_data” or something like that.

![Dynamic Named Range using OFFSET formula](https://chandoo.org/img/c/using-offset-formula-to-make-chart-ranges-dynamic.png)

Now repeat the same for years column as well and call it “years\_data”

### 4\. Create a column chart and set the source data to these named ranges

Create a column chart. For the source data use the named ranges we have just created.

![Dynamic Chart Series Data using Named Ranges](https://chandoo.org/img/c/chart-data-series-dialog.png)

Important: You must use the named range along with worksheet name, otherwise excel wont accept the named range for chart source data.

_**That is all, now your chart is dynamic**_

Download the Dynamic Chart Ranges Tutorial Workbook
---------------------------------------------------

**[Click here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-chart-ranges-tutorial.xlsx)
** to download the dynamic chart ranges workbook and use it to learn this trick. I have given Excel 2007 file since the file includes tables.

Bonus Tip: Edit chart series data ranges using mouse
----------------------------------------------------

If you have no time for writing lengthy formulas or setting up data tables, you can still save time when editing chart series data ranges. Just select the series by clicking on the chart. Now excel shows highlighted border around the cells from which the chart series is created. Just click on the bottom-right corner and drag it up and down to edit the chart series data ranges. (more: [Edit formula ranges using mouse](https://chandoo.org/wp/dynamic-chart-data-series/chandoo.org/wp/2009/05/05/edit-formulas-with-mouse/)
)

See the demo to understand this:

![Edit Chart Ranges using Mouse](https://chandoo.org/img/c/edit-chart-series-data.gif)

More tricks to make dynamic charts using Excel
----------------------------------------------

Here is a list of tutorials and examples recommend just for you. Go check them out and make your charts even more dynamic.

*   [Filter Charts just like you filter Data](https://chandoo.org/wp/2009/05/19/dynamic-charts-in-excel/)
    
*   [Select and show one chart from many](http://chandoo.org/wp/2008/11/05/select-show-one-chart-from-many/)
    
*   [Dynamically Group Related Data in the Charts](https://chandoo.org/wp/2009/08/27/dynamic-event-grouping-in-charts/)
    
*   [Use Data Filters as Chart Filters and Make Dynamic Charts](http://chandoo.org/wp/2009/02/12/make-a-dynamic-chart-using-data-filters/)
    
*   [A Dynamic Donut Bar Chart – Show total and break-ups in an interesting way](http://chandoo.org/wp/2009/09/30/donut-bar-chart/)
    

**Tell me about your experience with dynamic charts using comments.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [103 Comments](https://chandoo.org/wp/dynamic-chart-data-series/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dynamic-chart-data-series/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel 2007](https://chandoo.org/wp/tag/excel-2007/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [howtos](https://chandoo.org/wp/tag/howtos/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [lists](https://chandoo.org/wp/tag/lists/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousThe Project Management Bundle for Excel is Here, Download your copy today](https://chandoo.org/wp/project-management-bundle-for-excel/)

[NextHow to get Excel 2003 Toolbars in Excel 2007 \[productivity hack\]Next](https://chandoo.org/wp/excel-2003-toolbar-in-2007/)

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
    
    [Reply](https://chandoo.org/wp/dynamic-chart-data-series/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dynamic-chart-data-series/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dynamic-chart-data-series/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ