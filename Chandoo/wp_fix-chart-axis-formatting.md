# Fix Excel Chart's Axis Formatting

**Source:** https://chandoo.org/wp/fix-chart-axis-formatting

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Fix this chart \[excel homework #1\]
====================================

*   Last updated on July 22, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We have received a chart for [chart busters](http://chandoo.org/wp/tag/chart-busters/ "Chart Busters - Make Better Charts")
 that required some fixing. I thought, this will be a fun exercise for you. So here it goes,

> …column chart that shows daily, weekly or monthly data depending on the user’s choice. In daily the columns are displayed properly, but in weekly & monthly mode the columns are a fraction of the width they should be – why, and how can this be avoided? Bonus points if you can describe how to use an INDIRECT formula on the x-axis labels which is another problem I ran into whilst creating this mockup!

**You can download the workbook from [here](http://www.2shared.com/file/6265358/cc846caa/Chart_Doctor_-_gmoar.html)
**.

Here is how it is looking:

![Fix this chart - Chartbusters - Dynamic chart bug](https://chandoo.org/img/cb/axis-mixup-chart-fix.gif)

_Thanks **Gordon** for asking this question._

### Featured Answers:

There were several people who answered this correctly. I am featuring two answers for this problem.

_**By Jeff Weir:**_

> One way to fix this is to select the ‘axis options/axis type/text axis’ option in the axis dialogue box (it’s current setting is “Automatically select based on data”.
> 
> Then it would be good if you set the ‘interval between tick marks as one, as well as the ‘interval between labels’ as 1 also.
> 
> Unfortunately then you run into the problem that your dates are now too wide for the space allowed for them on the graph. Easiest way to do that is to firstly make the graph a little wider, and secondly have an intermediate formula that formats your dates so they have a character return between the month and year, like this:
> 
> 1 Jan
> 
> 2009
> 
> instead of this:
> 
> 1 Jan 2009
> 
> You can accomplish that with a formula along the lines of this:
> 
> \=DAY(B6)&CHOOSE(MONTH(B6),” Jan”, ” Feb”, ” Mar”, ” Apr”, ” May”, ” Jun”, ” Jul”, ” Aug”, ” Sep”,” Oct”,” Nov”,” Dec”)&CHAR(10)&YEAR(B6)
> 
> Also, the y axis could do with a custom number format. No point of displaying all those zeros if say $250k or 250k (assuming not a currency) will do.
> 
> You can see it [here](http://cid-f380a394764ef31f.skydrive.live.com/browse.aspx/.Public?uc=1)

_**By Gerald Higgins**_

> Well, here goes with the simple solution (in 2003).
> 
> Right click the chart, and select Chart Options.
> 
> On the AXES tab, there are 3 options under “Category (X) axis”.
> 
> I think the option for Time scale was originally selected.
> 
> The option for “Automatic” also does not work.
> 
> But the option for “Category” does work.

### All the commenters with an answer will receive their discount codes by this weekend. Enjoy.

### Lear more about making better charts using these chart busters examples:

1.  [Asset Allocation Charts – Done the right way](http://chandoo.org/wp/2009/06/19/bad-asset-allocation-chart/)
    
2.  [Calorie chart – How much you should exercise for what you eat – fixed properly](http://peltiertech.com/WordPress/chart-busters-calorie-chart/)
    

### Learn how to make dynamic charts:

1.  [Excel dynamic charts using data filters](http://chandoo.org/wp/2009/05/19/dynamic-charts-in-excel/)
    
2.  [Dynamic charts using INDEX() formula and Camera tool](http://chandoo.org/wp/2008/11/05/select-show-one-chart-from-many/)
    
3.  [Using scroll bar form control to make dynamic charts](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [22 Comments](https://chandoo.org/wp/fix-chart-axis-formatting/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/fix-chart-axis-formatting/#respond)
    
*   Tagged under [axis formatting](https://chandoo.org/wp/tag/axis-formatting/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [Chart Busters](https://chandoo.org/wp/tag/chart-busters/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [date axis](https://chandoo.org/wp/tag/date-axis/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [reader questions](https://chandoo.org/wp/tag/reader-questions/)
    , [user polls](https://chandoo.org/wp/tag/user-polls/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousCreate a number sequence for each change in a column in excel \[Quick Tip\]](https://chandoo.org/wp/generate-sequence-numbers/)

[NextBest month ever \[blogging updates\]Next](https://chandoo.org/wp/best-month-ever/)

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
    
    [Reply](https://chandoo.org/wp/fix-chart-axis-formatting/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/fix-chart-axis-formatting/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/fix-chart-axis-formatting/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ