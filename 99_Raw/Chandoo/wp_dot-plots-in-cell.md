# Create Excel Dot Plots (in-cell) - Tutorial and Downloadable Template

**Source:** https://chandoo.org/wp/dot-plots-in-cell

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Incell Dot Plots in Microsoft Excel
===================================

*   Last updated on December 5, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Dot plots are a very popular and effective charts. According to [dot plots wikipedia article](http://en.wikipedia.org/wiki/Dot_plot_(statistics))
,

> Dot plots are one of the simplest plots available, and are suitable for small to moderate sized data sets. They are useful for highlighting clusters and gaps, as well as outliers. Their other advantage is the conservation of numerical information.

Today we will learn about creating in-cell dot plots using excel. We will see how we can create a dot plot using 3 data series of some fictitious data. We will create something like this:  
![Excel In-cell Dot Plots - Tutorial](https://chandoo.org/img/l/excel-in-cell-dot-plots.png)

Note: If you are new to in-cell charting, I suggest you read the [incell bar charts](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/)
 article to understand the concept.

### 1\. Take your data and massage it a bit

Since we are doing an incell variation of dot plot, we need to pre-process the data a little bit. Assuming we have data on revenues of 3 imaginary companies – MegaHard, Grape and Twogle like this:  
![Dot Plot Data](https://chandoo.org/img/l/dotplot-data.png)  
We need to normalize the data to some meaningful number like 100 (remember, [incell graphs](http://chandoo.org/wp/tag/in-cell-charting/)
 print some character for each unit in the data.) so that the in-cell dot plot looks meaningful.

After normalizing the data we will also need to calculate some helper columns so that we can develop the incell dot plot easily. The helper columns (3 of them) will show,

1.  Smallest value in each row – 1
2.  Next smallest value in each row – previous helper column – 2
3.  The largest value in each row – previous two helper columns – 3

![Dot Plot Data (Normalized)](https://chandoo.org/img/l/dotplot-normalized-data.png)

_**Helper columns ?!? wh**__**y are we doing this?**_

The helper columns (or intermediate values) are usual practice when we need to pre-process data for dashboards or charts. Once the chart is ready, I usually hide the helper columns as they do not really say anything.

In our case, we are using helper columns since the formulas for plotting the incell dot plot are rather long and we would make then even longer if we don’t use these.

### 2\. Identify Symbols for Each Data Series

This is the simple job. In our case I have shown the symbols we are going to use in the above image. You can find some interesting symbols like triangles, rectangles, circles etc. in a regular font like Arial. Just go to Menu > Insert > Symbol (or Insert > Symbol in Ribbon) to find the symbols you like.

_Let us assume the symbols are in the range C5:E5_

### 3\. Finally Write the Formulas That Generate the In-cell Dot Plot

Now comes the fun part. We have the normalized data in the range C16:E16, and the helper values  in F16, G16, H16.

For the first row of the dot plot, the formula looks like:  
`=REPT("-",F16)&INDEX($C$5:$E$5,MATCH(SMALL(C16:E16,1),C16:E16,0))&REPT("-",G16)&INDEX($C$5:$E$5,MATCH(SMALL(C16:E16,2),C16:E16,0))&REPT("-",H16)&INDEX($C$5:$E$5,MATCH(SMALL(C16:E16,3),C16:E16,0))&REPT("-",100-MAX(C16:E16))`

huh! it has to be one of the longest formulas I have written in a while.

I thought long and hard about how this formula can be explained and came up with the below illustration.  
![In-cell Dot Plot - Formula](https://chandoo.org/img/l/incell-dot-plot-formula.png)  
Once you have the formula for one row, we just need to copy paste it over the entire range to show dot plot for each year of the data. That simple!

Some formula help if you are stuck – [REPT()](http://chandoo.org/excel-formulas/rept.html "REPT Excel Function - Help and Examples")
 | [SMALL()](http://chandoo.org/excel-formulas/small.html "SMALL Excel Function - Help and Examples")
 | [MATCH()](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/ "MATCH Excel Function - Help and Examples")
 | [MAX()](http://chandoo.org/excel-formulas/max.html "MAX Excel Function - Help and Examples")

### How to Generate 2 Series Dot Plots?

The 2 series dot plots have even simpler formulas. So I am leaving it to your imagination. But when you finish it, the dot plot looks something like this:  
![2 series dot plot example - microsoft excel](https://chandoo.org/img/l/in-cell-dot-plots-microsoft-excel-2-series-example.png)

### Download the In-cell Dot Plot Template and Make your own Dot plots

The [downloadable workbook](http://chandoo.org/img/l/incell-dot-plots-1.zip "Excel Dot Plots - In-cell - Template and Example")
 has examples for 2 series and 3 series in-cell dot plots. Go ahead and play with it.

### Further Resources on Dot Plots

Dot plots are not new, there is quite a bit of material and tools available for you to understand and make dot plots. They are proven to be very effective tools for communicating small to medium series of data. I suggest you to read few of these articles to learn more about dot plots.

[Naomi’s Article on B-eye Network on Dot Plots](http://www.b-eye-network.com/view/2468)

[Excel Dot Plots using Bar Charts by Jon Peltier](http://peltiertech.com/Excel/Charts/DotPlot.html)
 (Also try [Excel Dot Plotter Add-in](https://www.e-junkie.com/ecom/gb.php?ii=373494&c=ib&aff=49044&cl=84674)
)

[Excel User on Dot plots and why they are better](http://www.exceluser.com/dash/dotplot.htm)

### More on In-cell Charts

[Incell Bar](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/)
 | [Sparklines](http://chandoo.org/wp/2008/05/13/creating-in-cell-bar-charts-histograms-in-excel/)
 | [Pie charts](http://chandoo.org/wp/2008/05/07/create-in-cell-pie-charts-in-excel-how-to/)
 | [Bullet Graphs](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/)
 | [w/ Conditional Formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/dot-plots-in-cell/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dot-plots-in-cell/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [data processing](https://chandoo.org/wp/tag/data-processing/)
    , [dot plots](https://chandoo.org/wp/tag/dot-plots/)
    , [dot strip plots](https://chandoo.org/wp/tag/dot-strip-plots/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [rept](https://chandoo.org/wp/tag/rept/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousNetworkingdays() an improved version of networkdays formula](https://chandoo.org/wp/networkingdays/)

[NextInterviewing Garr Reynolds on this Friday, send me your questionsNext](https://chandoo.org/wp/garr-reynolds-send-interview-questions/)

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
    
    [Reply](https://chandoo.org/wp/dot-plots-in-cell/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dot-plots-in-cell/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dot-plots-in-cell/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ