# Rounding time to nearest minute or quarter hour etc. [formulas] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/rounding-time-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Rounding time to nearest minute or quarter hour etc. \[formulas\]
=================================================================

*   Last updated on June 26, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

The other day, I was building a spreadsheet to calculate FTE (full time equivalent) for staff based on hours worked on various days in a fortnight. While building the spreadsheet, I came across an interesting problem. _**Rounding Time to nearest minute.**_  We can’t use ROUND() or MROUND() to round time as these formulas aren’t designed to work with time values. Although time values are technically decimal, rounding time to nearest minute (or quarter hour etc.) can be tricky when usual round formulas. Let me share a few formulas to round time to nearest point.

![round-time-in-excel](https://chandoo.org/wp/wp-content/uploads/2017/06/round-time-in-excel.png)

Let’s say you have a time value (either user input or calculated) in cell A1.

### Use below formulas to round time in A1.

**Nearest second**: =TIME(HOUR(A1), MINUTE(A1), SECOND(A1)).

*   SECOND formula rounds up any fractions and returns full seconds.

**Nearest 15 seconds:** \=TIME(HOUR(A1), MINUTE(A1), MROUND(SECOND(A1),15))

*   Use MROUND() to round up seconds values to nearest multiple of 15 (or whatever else)

**Nearest Minute: =**TIME(HOUR(A1), MINUTE(A1)+(SECOND(A1)>30),0)

*   The seconds value will always be zero. We just look at fractional minutes portion to see if they are more then 30 to round up to next minute. The trick is to add up Boolean check (SECOND(A1)>30) to minutes value.

**Nearest 15 minutes:** =TIME(HOUR(A1), MROUND(MINUTE(A1)+SECOND(A1)/60,15),0)

*   This one uses MROUND to round total mins (including fraction) to nearest multiple of 15.

**Nearest 37th minute:** \=TIME(HOUR(A1), MROUND(MINUTE(A1)+SECOND(A1)/60,37),0)

*   Same logic. Just to show you how to round to an arbitrary minute.

**Nearest hour:** =TIME(HOUR(A1) +((MINUTE(A1)+SECOND(A1)/60)>30),0,0)

*   Check if total minutes is greater than 30 and add the result to hours.

### Time for some home work

Let’s test your timing skills. Assuming A1 has date & time value (like 26-Jun-2017 7:21:32 AM), round it **up** to nearest working hour.

*   The working hours are 9AM to 6PM on weekdays (Monday – Friday)

Post your answers in the comments section. Tick tock, tick tock… time is ticking, post your answers.

### Time to polish your skills

_Always having a hard time working with times in Excel?_ Its high time you took some time to learn about Excel time.

*   [Working with date & time values in Excel – a quick intro](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
    
*   [Convert fractional time to hours & minutes](http://chandoo.org/wp/2014/08/19/convert-fractional-excel-time-to-hours-minutes-quick-tip/)
    
*   [Highlighting over due items](http://chandoo.org/wp/2015/08/03/overdue-items/)
    
*   [42 tips for Excel time travelers](http://chandoo.org/wp/2013/10/17/excel-date-time-tips/)
     – calculating past, present and future time values using formulas
*   [Sorting by birthday](http://chandoo.org/wp/2013/08/26/sort-by-birthday-quick-tip/)
    
*   [More date & time tips](http://chandoo.org/wp/tag/date-and-time/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/rounding-time-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/rounding-time-in-excel/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mround](https://chandoo.org/wp/tag/mround/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [round](https://chandoo.org/wp/tag/round/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousSUMPRODUCT Vs. Power Query on Mt. KauKau](https://chandoo.org/wp/sumproduct-vs-power-query/)

[NextHow to add a lot of Goal Seeking to a modelNext](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/)

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