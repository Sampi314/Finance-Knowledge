# Show Details On-demand in Excel [Tutorial + Training Program] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/show-details-on-demand-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [products](https://chandoo.org/wp/category/products/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Show Details On-demand in Excel \[Tutorial + Training Program\]
===============================================================

*   Last updated on April 7, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Yesterday, we have seen [a beautiful example](http://chandoo.org/wp/2011/04/06/show-average-and-distribution/ "Give more details by showing average and distribution ")
 of how showing details (like distribution) on-demand can increase the effectiveness of your reports. Today, we will learn how to do the same in Excel.

_**Before jumping in to the tutorial,**_

In this post, I have explained one technique of using charts + VBA to dynamically show details for a selected item. There are 4 other ways to do the same – _viz._ using cell comments, pivot charts, group / un-group feature and hyperlinks. I have made a 45 minute video training explaining all the 5 techniques in detail. Plus there an Excel workbook with all the techniques demoed. You can get both of these for $17.

**[Click here to get the video training](http://www.e-junkie.com/ecom/gb.php?c=cart;i=920427;cl=49044;ejc=2)
 – Showing on-demand details in Excel**

\[[Alternative payment link](https://www.e-junkie.com/ecom/gb.php?i=920427&c=2co&cl=49044)\
\]

### How does the on-demand details chart work – demo:

This is a replica of yesterday’s chart from Amazon. When you click on any cell inside the Items + Rating table, the corresponding items review break-up is shown in the chart aside.

![Show details on-demand in Excel - Demo](https://img.chandoo.org/c/on-demand-analysis-and-details-in-excel-demo.gif)

Creating this chart in Excel – Step-by-step Instruction
-------------------------------------------------------

So you are ready to learn how to do this chart? Great, grab a cup of coffee or tea and get started.

### 1\. Understanding the data

This is how I have setup the source data for the chart. It has 3 columns – Item name, Reviewer ID and Rating. Each item has several ratings from several different reviewers. And our goal is to summarize all these ratings.

![Data for the chart - on-demand charts in Excel](https://chandoo.org/img/c/on-demand-charts/data-for-the-chart.png)

All this data is in the range Table1. We will use structured references \[[what are they?](http://chandoo.org/wp/2009/09/10/data-tables/)\
\] in formulas to keep them readable.

### 2\. Setting up the Item & Rating Table

The first step is to show a table with all the products we sell and their corresponding average rating. We will then add the circle indicators at the end to visually show the rating.

![Item and Rating Table - Explanation - On-demand Charts in Excel](https://chandoo.org/img/c/on-demand-charts/item-and-rating-table-explanation.png)

**Calculating the averages using AVERAGEIF() formula:**

The formula is quite simple. Assuming the product names are in C5:C13,

We just write =AVERAGEIF(Table1\[Item\],C5,Table1\[Rating\]) for first product’s average. Fill the rest by dragging the formula down.

**Displaying Circles:**

![Circle Symbols - Wingdings 2 font - excel](https://chandoo.org/img/c/on-demand-charts/circle-symbols-wingdings-font.png)There are no star symbols in the default fonts. But we have circles – a full circle, an empty circle and a donut to indicate half-circle. These symbols are available in _**Wingdings 2**_ font. We will [use an incell chart](http://chandoo.org/wp/tag/in-cell-charting/)
 to display the circles. Assuming the rating is 2.83, we need to print 2 full circles, one donut and 2 empty circles. \[related: [inserting symbols in to Excel workbooks](http://chandoo.org/wp/2010/10/11/insert-symbols-in-excel-howto/)\
\]

The formula is quite simple. Since the ratings are in D5:D13, the formula becomes,

\=REPT(**fullCircleSymbol**,INT(D5)) & REPT(**donutSymbol**,(INT(D5)<>D5)+0) & REPT(**emptyCircleSymbol**,INT(5-D5))

**Naming this grid**

Now that we are done with the rating grid, let us name it – _**rngReviews**_.

### 3\. Finding out which cell is selected

Now comes the macro part.

Before jumping in to the code, take a sip of that coffee. It is getting cold.

When a user selects any cell inside rngReviews, we need to findout which product it is so that we can load corresponding details.

**The macro logic is quite straight forward.**

1.  On Worksheet\_SelectionChange, check if the ActiveCell overlaps with rngReviews
2.  If so,
    1.  findout the relative row number of ActiveCell with respect to topmost row in rngReviews (ie the position of selected cell inside rngReviews)
    2.  Put this value in to a cell on worksheet – say _**E28**_

The macro code can be found in the downloaded workbook. [Here is an image of macro code](https://img.chandoo.org/c/on-demand-charts/vba-code-for-changing-the-chart.png)
.

### 4\. Using the macro output to drive…,

We need to use the value E28 to do 2 things.

1.  Highlight the corresponding row in the rngReviews [using conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    .
2.  Findout the corresponding product [using INDEX formula](http://chandoo.org/wp/tag/index)
    .

I am leaving both of these to your imagination.

### 5\. Calculating Product – Rating Breakup

In order to show details for the product, we must calculate the corresponding breakup of ratings (_ie_ how many 1 star, 2 star … 5 star reviews the product got).

I am leaving the formulas for this to your imagination. But when you are done, make sure your output looks like this:

![Calculating Product-wise Rating Breakup - On-demand charts in Excel](https://chandoo.org/img/c/on-demand-charts/source-range-of-data-for-chart.png)

(hint: [use COUNTIFS formula](http://chandoo.org/wp/tag/countifs/)
).

### 6\. Create a Chart to show Rating Break-up

This is the last one before we put everything together. Just follow below 5 steps.

1.  Select the 3 columns – Rating type, number of reviews, total reviews and create a bar chart (not stacked bar chart). In my workbook, this data is in the range C29:E34 in the sheet “Rating Summary”.
2.  Reverse the order of categories as Excel shows them upside down. For this select the vertical axis and hit CTRL+1 (or go to axis options from right click menu). Here check the “Show categories in reverse order” option. Also remove the chart legend.
3.  Set both series of the chart such that they completely overlap each other \[[image](http://chandoo.org/img/c/on-demand-charts/completely-overlapping-one-series-with-another.png)\
    \]. Adjust the gap width to 50%. Also, adjust the order of the series from Chart’s source data options \[[image](http://chandoo.org/img/c/on-demand-charts/adjusting-series-order-from-chart-data-options.png)\
    \].
4.  Remove grid lines, axis line and horizontal axis. Format the chart colors to your pink and translucent green (really!).
5.  Re-size the chart, add title, add labels, remove border. You need to use dynamic titles.

![How to make the product rating details chart - 5 steps - on-demand charts in Excel](https://chandoo.org/img/c/on-demand-charts/how-to-make-the-chart.png)

### 7\. Put everything together

Now is the time to put everything together and test. Move the chart close to the rating table. Test it by clicking on any value inside table.

You can also do some colorful formatting if you prefer.

![Show details on-demand in Excel - Demo](https://img.chandoo.org/c/on-demand-analysis-and-details-in-excel-demo.gif)

Finish the coffee and show-off the chart to a colleague or boss. Bask in glory.

Download Example Workbook – On-demand Details in Excel
------------------------------------------------------

[**Click here to download the workbook**](https://img.chandoo.org/d/on-demand-details-in-excel-demo.xlsm)
 with this example. Play with it to understand how this chart works.

Note: You must **enable macros** to use the file.

Note2: _**If the file does not open on double-click,**_ just open Excel (2007 or above) and drag the file inside to Excel.

_**Learn this + 4 other techniques using Video Training,**_

In this post, I have explained one technique of using charts + VBA to dynamically show details for a selected item. There are 4 other ways to do the same – _viz._ using cell comments, pivot charts, group / un-group feature and hyperlinks. I have made a 45 minute video training explaining all the 5 techniques in detail. Plus there an Excel workbook with all the techniques demoed. **You can get both of these for $17**.

**[Click here to get the video training](http://www.e-junkie.com/ecom/gb.php?c=cart;i=920427;cl=49044;ejc=2)** – Showing on-demand details in Excel

\[[Alternative payment link](https://www.e-junkie.com/ecom/gb.php?i=920427&c=2co&cl=49044)\
\]

How do you like this chart?
---------------------------

Ever since I learned this technique from a good friend, I have been using it in dashboards & complex models to make them more user friendly.

_**What about you?**_ Did you like this technique? Where are you planning to use it? **Please share your views & ideas using comments.**

More Resources to One-up your Chart Awesomeness
-----------------------------------------------

_Want more, here is more:_

*   [Grammy Bump Charts – a dynamic excel chart](http://chandoo.org/wp/2011/02/22/the-grammy-bump-chart-in-excel/)
    
*   [Showing same data in multiple views](http://chandoo.org/wp/2011/03/16/analytical-charts-tutorial/)
    
*   [Using Checkboxes to make dynamic charts](http://chandoo.org/wp/2010/08/31/dynamic-chart-with-check-boxes/)
    
*   [More on Excel Dynamic Charts](http://chandoo.org/wp/tag/dynamic-charts/)
    
*   [More on Excel Charts](http://chandoo.org/wp/category/visualization/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [48 Comments](https://chandoo.org/wp/show-details-on-demand-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/show-details-on-demand-in-excel/#respond)
    
*   Tagged under [axis formatting](https://chandoo.org/wp/tag/axis-formatting/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [insert symbol](https://chandoo.org/wp/tag/insert-symbol/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [products](https://chandoo.org/wp/tag/products/)
    , [rept](https://chandoo.org/wp/tag/rept/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [structured references](https://chandoo.org/wp/tag/structured-references/)
    , [tables](https://chandoo.org/wp/tag/tables/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [products](https://chandoo.org/wp/category/products/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousGive more details by showing average and distribution \[Charting Tips\]](https://chandoo.org/wp/show-average-and-distribution/)

[NextAuditing Spreadsheets? – Disable Direct Editing Mode to save time \[quick tip\]Next](https://chandoo.org/wp/spreadsheet-auditing-tip-disable-direct-editing-mode/)

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
    
    [Reply](https://chandoo.org/wp/show-details-on-demand-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/show-details-on-demand-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/show-details-on-demand-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ