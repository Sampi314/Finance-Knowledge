# How to Visualize Survey Results using Incell Panel Charts [case study] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/incell-panel-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to Visualize Survey Results using Incell Panel Charts \[case study\]
========================================================================

*   Last updated on May 28, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Often when we make a survey to compare various products (or vendors, companies, brands) the results are in the following format:

![Survey Results - Data - Example](https://chandoo.org/img/cb/survey-results-data-example.png)

Now, we can visualize such data in several ways. One of the obvious ways to visualize is to make a stacked bar chart. But it results in poor representation of values as we cannot easily compare ratings of one vendor to another. This is where a panel chart would help. A sample panel chart for above data can be like this:

![Visualize Survey Results using Panel Charts](https://chandoo.org/img/cb/survey-results-panel-chart-example.png)

**A panel chart** (often called as trellis display or small-multiples) shows data for multiple variables in an easy to digest format. It lets users compare in any way and draw conclusions with ease.

_**Today, I want to discuss how the principles of panel chart can be applied to visualize a complex set of survey results.**_ For this we will use the recent survey conducted by Gartner on how various customers use BI (Business Intelligence) tools. The folks at [Tableau have done good analysis of this data](http://www.tableausoftware.com/blog/gartner-vendors-bi-activities)
 and presented the results in this format:

![BI Vendor Survey Results - Stacked Bar Chart](https://chandoo.org/img/cb/bi-vendor-survey-results-stacked-bar-chart.png)

While the above chart is ok, it doesn’t let you compare vendors very well. We can only compare them on first usage, “viewing static management reports”. For everything else, the base line changes, so it is difficult to draw meaningful conclusions if, for example, you want to know which software is getting used more for “doing complex adhoc analysis”.

_**Jon Peltier**_ has done [beautiful analysis of this chart and presented various alternatives in his post](http://peltiertech.com/WordPress/stacked-bar-chart-alternatives/)
 yesterday. One of his recommendations is, of course, making a panel chart like this:

![Panel Chart to Compare BI Vendors - Jon Peltier's chart](https://chandoo.org/img/cb/panel-chart-bi-vendor-survey-results.png)

_While, Jon’s Panel Chart greatly improves the readability of these survey results, I have **2 problems with it**._

1.  Making such a panel chart in Excel is like baking your own bread. If you are like me, after few hours, you would run to bakery both hungry and frustrated. Panel Charts are not native in Excel. That means, we have to bribe, coax, threaten, protest and bend over backwards to prepare something like this in Excel. Thankfully people have already done that. So we can follow the examples and learn from their lead. \[[here is a panel chart tutorial from Jon](http://peltiertech.com/WordPress/how-to-build-a-simple-panel-chart/)\
    \]. However, the point still remains that, **creating a panel chart in excel is a pain**.
2.  **Once such a panel chart is constructed, it is still pretty rigid.** For eg. if you are interested in knowing how IBM as a BI vendor fares, you would like to have the results sorted by IBM’s BI Usages, but doing that in this carefully weaved panel set up means going to square 1 with less dough. So, we are stuck with a panel chart where the values cannot be sorted by any one vendor.

### Is there a simpler way to construct panel charts in Excel?

So, I wondered, “_is there a better and simpler way to make this chart that would still let me compare values (by BI vendor or BI Usage), let me sort and still save me enough time to drive down to one of the best bakeries in town to get a nice fluffy donut?_“.

Of course there is…

The trick is to [use Incell Charts](http://chandoo.org/wp/2008/05/13/creating-in-cell-bar-charts-histograms-in-excel/)
. Ahem!

Instead of carefully tweaking chart options, adding dummy series and hiding them in the charts, we can just use incell charts with REPT formula and then align them in the cells. Since Excel naturally has the grid layout, creating panels (or small multiples) is as easy as snapping your fingers. (pls. note, this method of panel chart is only applicable for bar / column charts. If you need panels of line charts or scatter charts, you still need to use the methods suggested by Jon.)

We can also easily add a sorting option and use the lovely [LARGE formula](http://chandoo.org/excel-formulas/large.html)
 to sort the results based on selected vendor.

Here is what I prepared using the above recipe and it took me less than 20 minutes to set this up.

![BI Vendor Survey Results - Incell Panel Chart in Excel](https://chandoo.org/img/cb/bi-vendor-survey-results-panel-chart.gif)

\[[click here for larger version of this](http://chandoo.org/img/cb/bi-vendor-survey-results-panel-chart-l.gif)\
\]

### How is the above incell panel chart constructed?

I am sure you are eager to know how this chart is constructed. Here is the secret:

1.  I took the raw data from Jon’s site and then Pivoted it so that we get the survey results in a table (with vendors on top and usages on left).
2.  I have dedicated a cell to let user select the sort order. Let us call this cell as “K3”
3.  Based on the vendor selected in K3, I have sorted the entire raw data using LARGE formula (and generous use of MATCH, INDEX, OFFSET formulas as well – examples [here](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
     and [here](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
    ).
4.  Then I used the [REPT formula](http://chandoo.org/excel-formulas/rept.html)
     to plot the incell bar charts (and the font “play bill” so that the bars look thick and nice).
5.  I have topped this with [conditional formatting](http://chandoo.org/wp/tag/conditional-formatting)
     so that sorted vendor can be highlighted in different color.

### Download the Incell Panel Chart Workbook

[Download the Incell Panel chart workbook](http://chandoo.org/img/d/bi-vendor-incell-panel-chart.xls)
 to play with it. I am sure you will find something useful and fun in that. \[[mirror download link](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/chartbusters/bi-vendor-incell-panel-chart.xls)\
\]

### How would you chart survey results?

There are still few problems with this approach though (for eg. adding labels can be a pain), but all in all, this simplifies the charting task and leaves room for adding extra features like sorting, conditional formatting.

**Here is a open invitation.** We have a long weekend coming up, thanks to Easter. So go ahead and download the original data [here](http://peltiertech.com/images/2010-03/stackbardata.csv)
. And make your own charts for this survey data. The objective is that we should be able to compare vendors with each other with ease. Save your charts as images and upload them somewhere. Then leave a comment here with that URL so that we all can know how you would chart survey results.

_**Also, share your opinion on this type of panel charts.**_ What is your experience with them? Do you like / hate panel charts?

### Related:

*   [Excel Panel Charts – Examples from Process Trends](http://processtrends.com/toc_panel_charts.htm)
    
*   [How to build a panel chart from Peltier Tech](http://peltiertech.com/WordPress/how-to-build-a-simple-panel-chart/)
    
*   [Incell Charts in Excel – Examples and Tutorials](http://chandoo.org/wp/tag/in-cell-charting)
    
*   [Incell chart secret – use “Script” font to make better incell charts](http://chandoo.org/wp/2010/01/21/excel-incell-chart-font/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [48 Comments](https://chandoo.org/wp/incell-panel-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/incell-panel-chart/#respond)
    
*   Tagged under [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [Chart Busters](https://chandoo.org/wp/tag/chart-busters/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [panel charts](https://chandoo.org/wp/tag/panel-charts/)
    , [rept](https://chandoo.org/wp/tag/rept/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [surveys](https://chandoo.org/wp/tag/surveys/)
    , [visualiztion](https://chandoo.org/wp/tag/visualiztion/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious101 Excel Secrets – Recommended E-Book](https://chandoo.org/wp/101-excel-secrets-recommended-e-book/)

[NextThere are Easter Eggs in this Post!!!Next](https://chandoo.org/wp/easter-eggs-2010/)

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
    
    [Reply](https://chandoo.org/wp/incell-panel-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/incell-panel-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/incell-panel-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ