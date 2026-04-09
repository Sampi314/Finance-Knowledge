# Use Advances vs. Declines chart to understand change in values » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/advances-vs-declines-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Use Advances vs. Declines chart to understand change in values
==============================================================

*   Last updated on February 21, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Lets say you are responsible for sales of 100s of products (which belong to handful of categories). You are looking at sales of each product in last month & this month. And you want to understand whether sales are improving or declining by category. _**How would you do it?**_

Turns out, this is not a difficult problem. In fact, this question is asked every day & answered _using Advances vs. Declines chart._

You may have seen this chart in financial newspapers or websites. Shown below, **Advances vs. Declines chart tells us how many items have advanced & how many have declined**.

![Advances vs. Declines chart - Creating it using Excel](https://img.chandoo.org/c/advances-vs-declines-chart-explained.png)

When should you use Advances vs. Declines chart?
------------------------------------------------

As you can see, advances vs. declines chart does not give low level details about actual movement of values. Instead, it gives you a sense of what is going on. Use it in below situations:

*   To get a feel of how values have changed over time.
*   When you are dealing with data that constantly changes (sales, number of customers, defects etc.)

Create Advances vs. Declines chart in Excel
-------------------------------------------

You can easily create this chart in Excel from raw data. Just follow below tutorial.

### Step 1: Get the data & arrange it

You need at least 4 columns of data – item, category, previous value, current value

Once we have these, calculate % change in 5th column. Arrange data like below:

![Data for advances vs. declines chart](https://img.chandoo.org/c/data-for-advances-vs-declines.png)

### Step 2: Calculate Category-wise summaries

First list all unique categories in a column. Then using COUNTIFS formula, calculate the number of products declining & advancing.

_**The formula to count number of products going down by more than 10% is,**_

\=COUNTIFS(Sales\[category\], _Category name_, Sales\[% change\], _“<10%”_)

\[Related: [Introduction to Excel SUMIFS / COUNTIFS Formulas](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)\
\]

![Using COUNTIFS formula to calculate number of declines & advances](https://img.chandoo.org/c/calculating-number-of-advances-and-declines-formulas.png)

### Step 3: Calculate % break-ups for the chart

Once all the numbers are calculated, you can easily calculate the % split.

![Calculating Declines & Advances in percentage](https://img.chandoo.org/c/declines-and-advances-percentages.png)

**NOTE: Make sure you negate the % values for declines.** This will ensure that our chart shows stacked bars on both sides of axis.

### Step 4: Create a stacked bar chart from this data

Once all the numbers are in place, just select them and create a stacked bar chart. Your output should look like below:

![Stacked bar chart from advances and declines percentage data](https://img.chandoo.org/c/stacked-bar-chart-advances-vs-declines.png)

### Step 5: Adjust chart series order _if needed_

You may notice that, our stacked chart bars are not in correct order. Excel would have plotted <10% and >10% series before <0% and >0% series. To fix this:

1.  Right click on the chart
2.  Go to Select Data
3.  Now, select the series area
4.  Using up / down buttons adjust the order of series
5.  Done!

**See this demo to understand:**

![Adjusting chart series order - advances vs. declines chart using Excel](https://img.chandoo.org/c/adjusting-chart-series-order-demo.gif)

### Step 6: Adjust the colors & format the chart

Unleash your creativity and format the chart as you see fit. Make sure you add legend (otherwise the chart becomes very difficult to read).

![Advances vs. Declines chart - Completed](https://img.chandoo.org/c/advanes-vs-declines-chart-in-excel.png)

**And you are done!**

Download Advances vs. Declines chart template
---------------------------------------------

[**Click here to download the chart template**](https://img.chandoo.org/c/advances-vs-declines-chart-example.xlsx)
. Examine the formulas & chart settings to understand this better.

Do you use Advances vs. Declines chart?
---------------------------------------

I use variations of this chart often in my dashboards & reports. These charts are very concise and present a lot of information about distribution of changes.

**What about you?** Do you use advances vs. declines charts? How do you create them? **Share your experiences & techniques using comments.**

### Looking to advance your charting knowledge?

If you want to one up your Excel awesomeness quotient & create kick-ass charts, then you are at the right place. _**Check out below tutorials & see how deep the rabbit hole goes:**_

*   [Visualizing tax changes over time using Excel](http://chandoo.org/wp/2012/12/06/tax-burden-chart-excel/)
    
*   [Index Charts – to understand change over time](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
    
*   [Use Box plots to understand distribution of values](http://chandoo.org/wp/2012/07/31/excel-box-plot-tutorial/)
    
*   [Visualize monthly changes using Pivot Tables + Conditional formatting](http://chandoo.org/wp/2012/11/06/monthly-values-and-changes-pivot-table/)
    

**Recommended:** If all these sound exciting, you will incredibly benefit from our Excel School program, where we teach advanced charting & data analysis skills. [**Click here to know more & join us**](http://chandoo.org/wp/excel-school/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/advances-vs-declines-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/advances-vs-declines-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [budget vs. actual](https://chandoo.org/wp/tag/budget-vs-actual/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [stock charts](https://chandoo.org/wp/tag/stock-charts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousLast day for enrollments – Join our Power Pivot course & become awesome analyst](https://chandoo.org/wp/last-day-for-enrollments-join-our-power-pivot-course-become-awesome-analyst/)

[NextWork with several Excel files everyday? – Save them as a workspace \[Quick tip\]Next](https://chandoo.org/wp/excel-workspace-tip/)

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
    
    [Reply](https://chandoo.org/wp/advances-vs-declines-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/advances-vs-declines-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/advances-vs-declines-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ