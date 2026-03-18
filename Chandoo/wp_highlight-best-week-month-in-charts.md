# Highlight best week & month in a trend chart [tutorials] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/highlight-best-week-month-in-charts

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Highlight best week & month in a trend chart \[tutorials\]
==========================================================

*   Last updated on December 12, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

When analyzing business data like sales, shop visits or productivity, one of the questions managers always ask is,

> _**What is the best month / week ?**_

To answer this question, we need to make a chart that looks like this:

![Highlight Best week & month in a trend chart - Excel Charting tutorial](https://img.chandoo.org/c/highlight-best-week-month-in-trend-charts-excel-howtos.png "Highlight Best week & month in a trend chart - Excel Charting tutorial")

How to highlight best week or best month in a chart?
----------------------------------------------------

Today, lets learn how to highlight portions of such charts that correspond to best week or best month.

### First, an important rule

**To highlight data:** If you have all the numbers for this chart in a range A1:A100, and you want to highlight the maximum value (or top 10 values), you [use conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
.

**But with charts:** there is no such thing as conditional formatting. So we must imitate the effect. This is done by creating extra series of data (for best week, best month etc.) and formatting it accordingly.

So the rule is **_To highlight a portion of chart, we need to create another series for that portion and format it the way we want._**

### Step 1: Create a regular line chart from your data

Lets assume our original data is like this:

![Data for trend chart - highlight best week or month in charts](https://img.chandoo.org/c/data-for-trend-chart.png "Data for trend chart - highlight best week or month in charts")

Select it and create a line chart to depict the trend of values.

### Step 2: Calculate Weeknum

Weeknum will have the week number for each date. This is calculated by =weeknum(date)&”-“&year(date)

### Step 3: Calculate Best week portion

For our analysis, lets assume that best week is the week with highest total sales. To do this:

1.  Add one more column, lets call it weekly total. In this, sum up the total for each week.  The formula =SUMIF(weeknum, current-weeknum, values) will give this.
2.  Now, find the maximum of this column using =MAX(weekly-total)
3.  Add one more column – best week. This will have NA() for all values except the maximum week. The formula for this would be =if(weekly-total=max-weekly-total,value,na())

### Step 4: Add the best week series to chart

Copy the best week column and paste it in your original chart.

At this stage, our chart has 2 series:

![Add & Highlight best week series to trend chart](https://img.chandoo.org/c/highlighting-best-week-excel-charts-howto.png "Add & Highlight best week series to trend chart")

1.  Original line corresponding to all dates
2.  Best week line corresponding to only best 7 dates

Format this new series in any way you want. And your chart highlights best week.

### Step 5: Follow similar process for Best month

To highlight best month, you need to calculate month, monthly total, max-monthly-total & best month values. Once they are ready, just add the best-month values to the chart and you are done!

**Calculations Explained:**

See this illustration to understand how the calculations for best week & month work.

![Calculations Explained - Highlighting best week and month in a chart - Excel tutorials](https://img.chandoo.org/c/calculations-highlight-best-week-and-month-in-charts.png "Calculations Explained - Highlighting best week and month in a chart - Excel tutorials")

Download Example Workbook
-------------------------

[**Click here to download the example workbook**](https://img.chandoo.org/c/highlight-best-week-month-in-charts.xlsx)
 & play with it. The workbook contains 2 charts.

*   Best week & month highlighted
*   Best week & month highlighted along with drop lines

Examine the formulas & resources section of download file to learn more.

Do you highlight portions of charts?
------------------------------------

Highlighting a portion of chart is very useful to draw user’s attention. I do this all the time in my dashboards & reports. Unfortunately, there is no automatic way to do this. So we resort to techniques like this.

**What about you?** Do you highlight portions of charts? What techniques do you use? _Please share your ideas & tips using comments._

Also, read more on [Dynamic Charts](http://chandoo.org/wp/tag/dynamic-charts/)
, [Excel Tables](http://chandoo.org/wp/2009/09/10/data-tables/)
 & [Interactive Highlighting in charts](http://chandoo.org/wp/2010/11/11/highlight-data-points-scatter-line-charts/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/highlight-best-week-month-in-charts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/highlight-best-week-month-in-charts/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [Highlight](https://chandoo.org/wp/tag/highlight/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumif()](https://chandoo.org/wp/tag/sumif/)
    , [weeknum()](https://chandoo.org/wp/tag/weeknum/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousDressing Financial Statements – What Motivated Mr. Bean to Defraud Latte?](https://chandoo.org/wp/dressing-financial-statements-using-excel/)

[NextCan you find that pattern? \[Homework\]Next](https://chandoo.org/wp/find-text-pattern/)

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
    
    [Reply](https://chandoo.org/wp/highlight-best-week-month-in-charts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/highlight-best-week-month-in-charts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/highlight-best-week-month-in-charts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ