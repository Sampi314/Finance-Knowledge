# Revenue vs. Commission growth - Getting the message across [BYOD] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/revenue-vs-commission-growth-getting-the-message-across-byod

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Revenue vs. Commission growth – Getting the message across \[BYOD\]
===================================================================

*   Last updated on February 17, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week, I asked my email newsletter readers to submit “one data analysis problem you are struggling with”. We called it BYOD – Bring your own data. More than 100 people have emailed various interesting (and often very difficult) problems. This week (between 16th of February to 20th of February), let’s take a look at some of these problems and solve them.

_This problem is sent by Fiona._ 

### Situation: Our commissions are growing way faster than revenues

Let’s say you are looking revenues & sales commissions of your company for last few years. The data looks like this:

![revenue-growth-vs-commission-growth-data](https://chandoo.org/wp/wp-content/uploads/2015/02/revenue-growth-vs-commission-growth-data.png)

And you want to highlight the fact that commissions are growing faster than revenues.

So you plot YoY growth rates for revenues & commissions.

### Problem: The chart of YoY growth rates is not convincing

Take a look at the chart. It doesn’t convey the message that we want. At best it says “revenue growth is less than commission growth”

![revenue-growth-vs-commission-growth-problem](https://chandoo.org/wp/wp-content/uploads/2015/02/revenue-growth-vs-commission-growth-problem.png)

How to convey the message _**“Commission growth is a problem for us”**_?

### Option 1. Use indexed charts

When comparing 2 sets of values (that are in different order of magnitudes) over time, we can **[use indexed charts](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/ "Use Indexed charts when understanding change [Charting Techniques]")
**. They can tell the story of how the values have changed over time clearly.

Here is the indexed chart for our data:

![revenue-commission-growth-indexed-chart](https://chandoo.org/wp/wp-content/uploads/2015/02/revenue-commission-growth-indexed-chart.png)

**How to create this chart?**

![calculating-indexed-values](https://chandoo.org/wp/wp-content/uploads/2015/02/calculating-indexed-values.png)Simple. Just follow below steps.

1.  Calculate index values. Assume first year value for each series as 100 (so revenues = 100, commissions=100 in year 2010)
2.  For next year, calculate the value as this year value / first year value
3.  Plot these indexed values on a line chart
4.  Adjust the line chart axis minimum to 1 (or 100%) _if all values are >1_
5.  You are done

### Option 2. Visualize ‘for every % in revenue growth, commission grows by…”

We can calculate what is the change in commission growth rate for every % growth in revenues & plot this. This will depict the situation in a powerful & dramatic fashion, like this:

![pct-change-in-commission-for-every-pct-change-in-revenues](https://chandoo.org/wp/wp-content/uploads/2015/02/pct-change-in-commission-for-every-pct-change-in-revenues.png)

**How to create this chart?**

![calculating-values-pct-change-revenues-commission-growth](https://chandoo.org/wp/wp-content/uploads/2015/02/calculating-values-pct-change-revenues-commission-growth.png)Even simpler. Just do these steps:

1.  Calculate % values by dividing YoY commission growth with YoY revenue growth
2.  Plot this as a column chart
3.  Draw a line at 100%
4.  Add a text box at this line and write “Ideal” on it.
5.  You are done.

### Download Revenue vs. Commission growth charts

[**Click here to download the example workbook**](https://chandoo.org/wp/wp-content/uploads/2015/02/rev-vs-comission-growth.xlsx)
. Examine the formulas & chart settings to learn better.

### How would you present this information?

My favorite approach is to use indexed charts. They are designed for this exact purpose.

**What about you?** How would you visualize this kind of information? What charting techniques will you use to get your message across? Please share your inputs in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/revenue-vs-commission-growth-getting-the-message-across-byod/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/revenue-vs-commission-growth-getting-the-message-across-byod/#respond)
    
*   Tagged under [byod](https://chandoo.org/wp/tag/byod/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [indexed charts](https://chandoo.org/wp/tag/indexed-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [visualization principles](https://chandoo.org/wp/tag/visualization-principles/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousHow to consolidate data that is different shapes \[BYOD\]](https://chandoo.org/wp/consolidate-data-in-different-shapes/)

[NextWho is the most consistent seller? \[BYOD\]Next](https://chandoo.org/wp/calculating-consistency-in-excel/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ