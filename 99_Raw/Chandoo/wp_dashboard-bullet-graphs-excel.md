# Excel Bullet Chart Tutorial & Download

**Source:** https://chandoo.org/wp/dashboard-bullet-graphs-excel

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

Excel Bullet Graphs
===================

*   Last updated on June 9, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![bullet graph - becoming a dashboard ninja using Microsoft excel conditional formatting and formulas](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/finalizedbulletgraphs.gif)**Bullet graphs provide an effective way to dashboard target vs. actual performance data**, the bread and butter of corporate analytics.

Howmuchever effective they are, the sad truth is there is no one easy way to do them in excel. I have prepared a short tutorial that can make you a dashboard ninja without writing extensive formulas or installing unknown add-ins. So get out your _[shinobigatana](http://en.wikipedia.org/wiki/Ninjato)
_ and join me in a fresh excel sheet arena.

Before we create our first bullet graph, **let us spend a few moments understanding these graphs**. [Stephen Few](http://www.perceptualedge.com/)
 [proposed bullet graphs](http://www.perceptualedge.com/blog/?p=217)
 as way to provide crisp view of “target vs. actual performance” numbers. Shown below is a sample bullet graph and how you would read it.

![Sample bullet graph layout and how to read them](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/BulletGraphDescription.gif)

Read up more on this at [PTS blog](http://peltiertech.com/WordPress/2008/07/18/a-gauge-that-works/)
 and on a [Gauge chart that actually works](http://blog.instantcognition.com/excel/2008/07/14/a-gauge-chart-that-works/)
.

Let us create your first bullet graph
-------------------------------------

[**Click here** to download bullet-graph template excel sheet so that you can see while reading](https://chandoo.org/wp/wp-content/uploads/2008/07/bullet-graph-ninja.xls)

Our technique of involves conditional formatting and simple formulas applied to a cell grid. Just follow these 4 easy steps:

### Step 1: Prepare your data for charting

![bullet-graphs-empty-cellls-step-1](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/bullet-graphs-empty-cellls-step-1.gif)Since we are going to plot bullet graphs on a cell grid, we first need to normalize our data. I have chosen to plot each bullet graph on 20 cells in a row as shown in the raw grid shown to the right:

Assuming we have fictitious sales data like this:

![bullet-chart-ninja-normalized-data-cells-Microsoft-excel-visualization](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/bullet-chart-ninja-normalized-data-.gif)

You can normalize YTD sales figures using a simple formula like this : `ROUND(YTD-sales/target*20,0)`

Now that we have our data steaming hot, lets brew the graphs

### Step 2: Lets make the raw grid formatted based on data

Now we will take the raw 20 cell grid in each row and [conditionally format](https://chandoo.org/wp/dashboard-bullet-graphs-excel/chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
 these cells so that we have background of the bullet graph drawn on them.

> For eg. If the normalized sales data for Bad range is 7 and for OK Range is 15 then,
> 
> We will highlight first 7 cells lighter shade of gray, next 8 cells gray and last 5 cells with darker shade of gray.

I have shown the conditional formatting applied to these cells below:  
![bullet-graph-excel-conditional-formatting](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/bullet-graph-excel-conditional-form.gif)

When we are done, a sample row looks like this:

![bullet-graphs-building-background-step-1](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/bullet-graphs-building-background-s.gif)

We have our cell grids ready now, lets shoot some bullets. 🙂

### Step 3: Plot bullets on our graph canvas

Our final step involves print a bullet symbol (either – or + or | ) in each cell depending on one of the following conditions:

> 1\. If the cell position (1,2,3 … 20) is equal to Year ago value and cell position is less than YTD value print a + symbol  
> 2\. If the cell position is equal to Year ago value and cell position is more than YTD value print a | symbol  
> 3\. If the cell position is less than YTD value print a –  
> 4\. Else print a blank

See the formula below:  
![bullet-graph-MS-excel-if-formula](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/bullet-graph-microsoft-excel-if-for.gif)

[Download the excel template for bullet graphs to understand this formula better](https://chandoo.org/wp/wp-content/uploads/2008/07/bullet-graph-ninja.xls)

### Step 4: Show off your bullet graphs, awe your boss or colleagues, bask in your Ninja glory

Unfortunately, I cannot tell you how to do this. I can only teach you to be a Ninja, but you have to be one to charm people with your tactics. 🙂

Shown below is another variation you can try. Also, you can experiment with the symbols printed (instead of + – | you can try other ASCII characters, for more [download the excel sheet containing bullet graph templates](https://chandoo.org/wp/wp-content/uploads/2008/07/bullet-graph-ninja.xls)
)

![excel-bullet-charts-like-a-ninja-dashboard](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/excel-bullet-charts-like-a-ninja.gif)

**Also try:** [Partition charts](https://chandoo.org/wp/dashboard-bullet-graphs-excel/chandoo.org/wp/2008/07/09/partition-charts-excel-pie-alternative-visualization-hack/)
, [Incell Graphs](https://chandoo.org/wp/dashboard-bullet-graphs-excel/chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/)
 and [much more](http://chandoo.org/wp/category/excel/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [36 Comments](https://chandoo.org/wp/dashboard-bullet-graphs-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dashboard-bullet-graphs-excel/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [technology](https://chandoo.org/wp/tag/technology/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

[PrevPreviousPhotographic Fridays #5 – Dawn](https://chandoo.org/wp/dawn-photo/)

[NextExcel Links – to iPhone or not to iPhone editionNext](https://chandoo.org/wp/excel-links-of-week/)

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
    
    [Reply](https://chandoo.org/wp/dashboard-bullet-graphs-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dashboard-bullet-graphs-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dashboard-bullet-graphs-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ