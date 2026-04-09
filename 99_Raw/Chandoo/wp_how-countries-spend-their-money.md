# How countries spend their money - chart alternatives » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-countries-spend-their-money

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

How countries spend their money – chart alternatives
====================================================

*   Last updated on September 22, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Econimist’s [daily chart](http://www.economist.com/blogs/graphicdetail)
** is a one of my daily data porn stops. They take interesting data sets and visualize in compelling ways. While the daily chart page is insightful, sometimes they make poor charting choices. For example, [this recent chart](http://www.economist.com/blogs/graphicdetail/2015/09/daily-chart-9)
 visualizing how countries spend their money uses a variation of _notorious_ bubble chart. Click on the chart to enlarge.

[![20150912_woc650_1](https://chandoo.org/wp/wp-content/uploads/2015/09/20150912_woc650_1.png)](https://chandoo.org/wp/wp-content/uploads/2015/09/20150912_woc650_1.png)

### What is wrong with this chart?

**Bubble charts force us to measure and compare areas of circles**. Unless you have a measuring tape somehow embedded in your eyes and you are a walking human scientific calculator, you would find this task impossible.

So when you look at the chart and want to find out what percentage Japanese spend on restaurants or how much Americans pay for housing, your guesses will have large error margins.

Not only bubble charts are difficult to read, they are very hard to align. So when you have a bunch of bubbles, no matter how hard you try, your chart looks clumsy (see how the Russian food bubble eats in to Mexico’s bubble, as if it is too hungry 😉 )

### Let’s check out a few alternatives to this chart

The simplest alternative for all the bubble madness? **Use bar charts!**

Bar charts are easy – you can make them in no-time, your audience can read them in no-time. 2X time saved. What not to like 🙂

**Alternative 0 – Straight replacement of bubbles with bars:**

This one is simple. We take the data, apply conditional formatting > data bars on top of it. We can add an additional rule to show only MIN & MAX values in each row and hide the rest of the values with a custom formatting code – ;;;

This is what you get:

![alternative-0-how-they-spend-it-chart](https://chandoo.org/wp/wp-content/uploads/2015/09/alternative-0-how-they-spend-it-chart.png)

The above chart is way better than bubbles. If you want to shift the focus from country to expense category, you can transform the same chart.

_Related resources:_

*   [Hiding cell contents with custom cell format code](http://chandoo.org/wp/2009/06/05/hide-cell/)
    

**Alternative 1 – Transformed bar chart**

![alternative-1-how-they-spend-it-chart](https://chandoo.org/wp/wp-content/uploads/2015/09/alternative-1-how-they-spend-it-chart.png)

Again, same techniques, applied on transformed data set.

**Alternative 2 – Highlighting above & below average values in different colors**

While conditional formatting data bars are fun and simple, they can only show up in one color. So if you want a few bars to be in different color based on a condition (for ex: all values less than average in different color), you need to venture beyond the data bars.

We can use 2 techniques:

1.  Create in-cell bar charts, using REPT formula and color the bars with conditional formatting
2.  Create a regular bar chart with two series of data – above & below average and color them differently

REPT formula approach is fun and easy. Using that, we get this:

![alternative-2-how-they-spend-it-chart](https://chandoo.org/wp/wp-content/uploads/2015/09/alternative-2-how-they-spend-it-chart.png)

_Related resources:_

*   [Create in-cell bar charts with REPT formula](http://chandoo.org/wp/2010/01/21/excel-incell-chart-font/)
    
*   [In-cell bars + conditional formatting = AWESOME](http://chandoo.org/wp/2008/07/17/better-incell-charts/)
    

**Alternative 3 – Adding labels to MIN & MAX values too**

Once we have the REPT() based chart, we can add extra columns to conditionally show the data labels too.

This is what we get:

![alternative-3-how-they-spend-it-chart](https://chandoo.org/wp/wp-content/uploads/2015/09/alternative-3-how-they-spend-it-chart.png)

### Download ‘how they spend’ chart alternatives

[**Click here to download the Excel workbook containing all these charts**](https://chandoo.org/wp/wp-content/uploads/2015/09/how-do-they-spend.xlsx)
. Examine the formulas & conditional formats to learn more.

### More charting stories & case-studies

Check out below examples to learn few more powerful ways to tell stories using charts. [![In cell panel chart to visualize survey results](https://chandoo.org/img/cb/bi-vendor-survey-results-panel-chart.gif)](http://chandoo.org/wp/2010/04/01/incell-panel-chart/)

*   [Changing stubborn opinions with visualizations](http://chandoo.org/wp/2015/05/29/changing-opinions-with-visualizations/)
    
*   [Narrating the story of change – Excel charting case study](http://chandoo.org/wp/2015/05/18/story-of-change/)
    
*   [Evolution of Facebook privacy policies – Excel Panel Chart](http://chandoo.org/wp/2010/05/13/facebook-privacy-panel-chart/)
    
*   [Visualizaing survey results – incell panel chart](http://chandoo.org/wp/2010/04/01/incell-panel-chart/)
    

### How would you visualize this data?

What do you feel about the bubble chart? If you think it is a poor choice, how would you visualize this data? **Please share your thoughts and implementations in the comment section.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/how-countries-spend-their-money/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-countries-spend-their-money/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [bubble chart](https://chandoo.org/wp/tag/bubble-chart/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [data bars](https://chandoo.org/wp/tag/data-bars/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [economist charts](https://chandoo.org/wp/tag/economist-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousShow forecast values in a different color with this simple trick \[charting\]](https://chandoo.org/wp/show-forecast-values-different-color/)

[NextCP045: Introduction to Monte Carlo Simulations in ExcelNext](https://chandoo.org/wp/introduction-to-monte-carlo-simulations/)

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
    
    [Reply](https://chandoo.org/wp/how-countries-spend-their-money/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-countries-spend-their-money/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-countries-spend-their-money/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ