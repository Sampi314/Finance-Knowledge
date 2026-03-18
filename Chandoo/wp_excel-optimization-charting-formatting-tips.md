# Charting & Formatting Tips to Optimize & Speed up Excel

**Source:** https://chandoo.org/wp/excel-optimization-charting-formatting-tips

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Speeding up & Optimizing Excel – Tips for Charting & Formatting \[Speedy Spreadsheet Week\]
===========================================================================================

*   Last updated on March 21, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Speeding up & Optimizing Excel - Tips for Charting & Formatting](https://img.chandoo.org/optimize/speeding-up-optimizing-excel-charts-formatting.png "Speeding up & Optimizing Excel - Tips for Charting & Formatting")

_**Is Excel acting slow & taking ages?**_ As part of our [Speedy Spreadsheet Week](http://chandoo.org/wp/tag/ssw/)
, today lets talk about optimizing & speeding up Excel by formatting & charting better. Use these tips & ideas to super-charge your sluggish workbook.

No matter how much data you got, how many formulas you wrote, the end users seldom see them on your workbook. They see the finalized dashboard, they play with the model, they look at the report. And if you make poor choices, your end users will thing your workbook is slow.

7 Charting & Formatting Tips to Optimize & Speed up Excel
---------------------------------------------------------

### 1\. Use picture links / camera snapshots wisely

[Picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
 (known as camera snapshots in Excel 2003 or earlier) are a blessing in disguise. They can let you create stunning dashboards & reports, but they can also drastically slow-down your workbook. If you add one too many picture links or make they too dynamic, any time you change something on the dashboard, the picture links must be refreshed and that slows Excel down.

Remedy? Simple, use fewer picture links. Limit dynamic changes to minimum. Try using charts instead of picture links and measure the performance. If you have added any animation (thru VBA), get rid off it.

Note: In Excel 2010, the performance of picture links has been improved, but they still slow-down your workbook.

**Resources to learn more about dynamic charts & picture links:**

*   [Introduction to picture links – what are they and how to use them?](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    
*   [Picture links in action – Cricket Worldcup Dashboard](http://chandoo.org/wp/2011/04/15/cricket-worldcup-dashboard/)
    
*   [Excel Dynamic Charts – lots of examples, tutorials & downloads](http://chandoo.org/wp/tag/dynamic-charts/)
    

### 2\. Do not load too much data in to the charts

Any time you have a chart that depicts more than half-a-dozen series of data, stop and reject the idea. See if you can re-structure the chart so that it shows lesser information or becomes 2 charts. Some ground rules I follow,

*   Never make charts with too many data points.
*   Use form controls or user input to show a sub-set of data instead of everything.
*   Do not customize the charts too much. Instead rely on other techniques like,

*   Using drawing shapes & text-boxes.
*   Using multiple charts
*   Using a mix of charts & cell formatting

*   Group the data and visualize at the group level (works for pivot tables)

**Resources to learn about charting better:**

*   [Which chart to use? a detailed guide](http://chandoo.org/wp/2010/04/19/chart-selection-process/)
    
*   [Using form controls to make dynamic charts – examples](http://chandoo.org/wp/tag/dynamic-charts/)
    
*   [Using text boxes in charts](http://chandoo.org/wp/2010/04/08/smart-chart-legends/)
    
*   [Panel charts – what are they and how to use them in Excel?](http://chandoo.org/wp/2010/05/12/introduction-to-panel-charts-using-excel-tutorial-template/)
    
*   [Grouping data in pivot tables](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)
    

### 3\. Stay away from fancy formatting in the charts

Fancy chart formatting options like 3d, shadows, perspective, reflection or gradients are CPU intensive and eye-sore. Even if your chart is rendered in a split second, because of all the additional detail in it, user takes more time to read it and hence perceives your workbook as slow.

Solution? Just use simple formatting. Use these guidelines,

*   Use fewer colors
*   Use fewer fonts (maximum 2 for a chart for best results)
*   Use 2d instead of 3d.
*   Stay away from features like 3d, perspective, shadows, reflections in the chart formatting.
*   If you must use these features, use them on a drawing shape and position it behind the chart.

**Resource to learn about chart formatting:**

*   [Chart formatting principles & best practices](http://chandoo.org/wp/tag/charting-principles/)
    
*   [Using drawing shapes to enhance chart formatting](http://chandoo.org/wp/2009/12/03/use-shapes-in-dashboards/)
    
*   [6 Excel charts you see in hell](http://chandoo.org/wp/2008/09/03/6-charts-to-never-use/)
    
*   [What colors to use in Excel charts?](http://chandoo.org/wp/2010/04/23/chart-colors-poll/)
    

### 4\. Use conditional formatting, in-cell charts instead of charts

With Excel 2007 & 2010, you can create rich conditional formatting that communicates better. So use it instead of charts in some places. Some excellent uses of conditional formatting are,

*   [Use CF icons as alerts in dashboards](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/)
    
*   [Use in-cell charts – examples, tutorials & downloads](http://chandoo.org/wp/tag/in-cell-charting/)
    
*   [Use CF to generate heat-maps](http://chandoo.org/wp/2010/11/12/last-visible-cell-visualization/)
     – Example

### 5\. Only format the cells you use

Often we format an entire column or row when we just use a bunch of cells. This used to be fine until Excel 2003 (where the maximum rows are 67k & max columns are 256). With Excel 2007 & 2010, the number of rows & columns in Excel worksheets has gone up significantly. So when you format an entire column you are asking for trouble. Follow below guidelines when formatting your worksheets to improve the performance.

*   Use tables when you are dealing with structured data. This way all the formatting is done automatically and extends only up to the last row / last column.
*   Never format an entire column or row. Just select the cells you use and format them.
*   Use simple formats. This way, even if you have to apply them to additional rows, you can do so faster.
*   Do not apply conditional formatting to very large ranges. This can significantly slowdown your workbook.
*   Hide rows & columns you do not need. This way the temptation to mess with them is gone.
*   Remove worksheets that are not required.
*   Use minimal formatting for non-output worksheets. And hide them if possible.
*   If you want to use very fancy formatting for a cell (multiple colors, multiple fonts etc.) use a text box instead. This way you can format it richer and the workbook remains lighter.

Related: [10 tips to create better & boss-proof Excel workbooks](http://chandoo.org/wp/2009/11/03/make-better-excel-sheets/)

### 6\. Limit cell styles to a minimum

I have not tested this, but I heard that when you use a lot of cell styles, the workbook becomes slower. So rely on fewer cell styles and use only the built-in styles.

### 7\. Use built-in features instead of 3rd party add-ins

I have nothing against add-ins and I personally use a few to do my work better. But when it comes to charting & formatting, you may want to use whatever is available if speed matters to you most. This is because built-in charts & features tend to be faster & bug-free. Plus they work on all computers.

If you must use 3rd party add-ins, use the ones made by a credible source & thoroughly test them. (Example: Jon’s charting add-ins, add-ins by other MVPs are usually better compared to a random macro code / add-in you found on internet).

More on Excel Optimization & Speeding up:
-----------------------------------------

Read these articles too,

*   [Optimization & Speeding-up Tips for Excel Formulas](http://chandoo.org/wp/2012/03/20/optimize-speedup-excel-formulas/ "Speed up your Excel Formulas [Speedy Spreadsheet Week]")
    
*   Optimizing & Speeding-up VBA Macros
*   Excel Optimization tips by Experts
*   Excel Optimization tips submitted by our readers

What formatting & charting tips you suggest to speed up Excel?
--------------------------------------------------------------

Most of my work involves producing dashboards & worksheet models – where charts & formatting plays a big role. So I follow pretty much all these tips to make my workbooks responsive.

**What about you?** What tips you suggest to make Excel faster? How do you format your workbooks & charts so that they look good & act fast? **Please share using comments.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/#respond)
    
*   Tagged under [cell styles](https://chandoo.org/wp/tag/cell-styles/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [excel optimization](https://chandoo.org/wp/tag/excel-optimization/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [picture link](https://chandoo.org/wp/tag/picture-link/)
    , [ssw](https://chandoo.org/wp/tag/ssw/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousThis week, Speed up your Spreadsheets – Your Action Required](https://chandoo.org/wp/speedy-spreadsheet-week/)

[NextOptimization Tips & Techniques for Excel VBA & Macros \[Speedy Spreasheet Week\]Next](https://chandoo.org/wp/vba-macros-optimization-techniques/)

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
    
    [Reply](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ