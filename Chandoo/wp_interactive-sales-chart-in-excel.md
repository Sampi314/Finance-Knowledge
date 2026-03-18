# Interactive Sales Chart using MS Excel [video] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-sales-chart-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Interactive Sales Chart using MS Excel
======================================

*   Last updated on May 9, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Finally, I got some time to sit down and do what I love most – **_write a blog post to make you awesome in Excel_**. After a whirlwind trip to Sydney, I am back in India to spend few days with my kids & wife before rushing to Australia to run 2nd leg of my training programs (in Perth, Melbourne & Brisbane). I did 2 sessions in Sydney – one for KPMG and other for public and both went very well. We got lots of positive feedback and people really loved it. I am saving the details for another post, but today lets talk about **Interactive Sales Chart using Excel**.

Take a look at the Interactive Sales Chart
------------------------------------------

First, take a look at interactive sales chart. Today, you will learn how to build this using Excel.

![Interactive Sales Chart in Excel - Demo](https://img.chandoo.org/vp/interactive-sales-chart-demo-2.gif "Interactive Sales Chart in Excel - Demo")

Inspiration for this chart
--------------------------

Before we learn how you can create such a chart, let me tell where the inspiration came from. Yesterday, _Persol_, a forum member asked, [How to make an info-radar chart](http://chandoo.org/forums/topic/how-do-you-make-the-info-radar-chart-i-found-on-the-link-below)
, where he mentioned the [below chart from Good.is](http://awesome.good.is/transparency/web/1010/political-climate-chart/interactive.html)

![Political Climate - Interactive Chart from Good.is](https://img.chandoo.org/vp/political-climate-interactive-chart-good.is.png "Political Climate - Interactive Chart from Good.is")

\[[Click here to play with this chart](http://awesome.good.is/transparency/web/1010/political-climate-chart/interactive.html)\
\]

While I took inspiration from the above chart, I replaced the radar chart with a regular column chart (as column charts are easier to read) and modified the data to a sales data set.

How to create interactive sales chart in Excel?
-----------------------------------------------

### First, take a look at the data

The sales data for this chart looked like this:

![Data for interactive sales chart](https://img.chandoo.org/vp/data-for-interactive-sales-chart.png "Data for interactive sales chart")

I have set up this data in an [Excel Table](http://chandoo.org/wp/2009/09/10/data-tables/)
 called as _tblSales_ so that it is easier to write formulas.

### The formulas

To calculate various values in the chart, we use ample doses of [SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
.

### The Interactivity

When you click on any year, region or product name, we run _worksheet\_seletionchange_ event. This tells our calculation engine which year, region & product are chosen. Then the formulas would (re)calculate the data for charts. This updates the charts & conditional formats.

\[Related: [Show on-demand details in Excel using VBA](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)\
\]

**_Here is how the interactive chart works:_**

![Interactive Sales Chart in Excel - the nuts & bolts](https://img.chandoo.org/vp/interactive-sales-chart-nuts-and-bolts.png "Interactive Sales Chart in Excel - the nuts & bolts")

How to create interactive charts like this – Video
--------------------------------------------------

Since the actual mechanics of this are quite elaborate, I made a short video (15 min) explaining how various parts of this chart work. Please watch it below.

\[[You can watch the video on our Youtube channel too](http://www.youtube.com/watch?v=6ZNrlA41a2c)\
\]

Download Interactive Sales Chart Workbook
-----------------------------------------

[**Click here to download the workbook**](https://img.chandoo.org/vp/interactive-sales-chart.xlsm)
 & play with it. Examine the macros & formulas to learn more.

How do you like this chart?
---------------------------

I really liked Good.is chart and wanted to see how much of it we can do in Excel. It was a fun exercise. I have noticed that such charts excite people (decision makers too) and make your reports fun.

**What about you?** How do you like the interactive sales chart? What additions / modifications would you do to it? _Please share your thoughts using comments._

Create Interactive Charts using Excel
-------------------------------------

Interactive charts are one my favorite visualizations. They let users play with the chart & decide what they want. So, naturally I write about them every now and then. Please go thru these examples if you want to learn various interactive charting techniques in Excel.

*   [Show top x values in a chart interactively](http://chandoo.org/wp?p=2395)
    
*   [Interactive dashboard using hyperlinks](http://chandoo.org/wp?p=3609)
    
*   [Suicides vs. Murders – Interactive Excel Chart](http://chandoo.org/wp?p=3759)
    
*   [Create a quick dynamic chart in Excel](http://chandoo.org/wp?p=2144)
    
*   [Interactive charts that leave your boss drooling](http://chandoo.org/wp?p=2815)
    
*   [More on Interactive Charts](http://chandoo.org/wp/tag/dynamic-charts/)
    

I also recommend enrolling in our Excel + VBA Class if you want to learn these techniques and create stunning reports & charts. [**Click here to learn more about our Excel + VBA training program**](http://chandoo.org/wp/vba-classes/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [95 Comments](https://chandoo.org/wp/interactive-sales-chart-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-sales-chart-in-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [interactive](https://chandoo.org/wp/tag/interactive/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousDisplaying Text Values in Pivot Tables without VBA](https://chandoo.org/wp/displaying-text-values-in-pivot-tables-without-vba/)

[NextVBA Move data from one sheet to multiple sheetsNext](https://chandoo.org/wp/vba-move-data-from-one-sheet-to-multiple-sheets/)

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
    
    [Reply](https://chandoo.org/wp/interactive-sales-chart-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-sales-chart-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-sales-chart-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ