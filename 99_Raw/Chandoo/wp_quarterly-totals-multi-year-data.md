# Quarterly totals when you have multi-year data [SUMPRODUCT again] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/quarterly-totals-multi-year-data

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Quarterly totals when you have multi-year data \[SUMPRODUCT again\]
===================================================================

*   Last updated on April 30, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

In yesterdays post – [Find Quarterly Totals from Monthly Data](http://chandoo.org/wp/2010/04/29/quarterly-totals-from-monthly-data/)
, we have learned how to use SUMPRODUCT formula to find totals by Quarter from a set of monthly values. The approach is fine, but has one glaring draw back.

_**It only works when you have data for one year.**_

In that post, [_Martin_ said](http://chandoo.org/wp/2010/04/29/quarterly-totals-from-monthly-data/#comment-103965)
,

> …  
> Ever since i read this post, I am struggling with a table that has the same layout as the example, and **I wanted to add the totals per year and per Q, years as rows, Qs as columns.**  
> …

### So, you want to get the totals like this:

![Quarterly totals when you have multi-year data](https://chandoo.org/img/f/quarterly-totals-multi-year-data.png)

Of course, **the easiest and quickest option is to use a pivot report with grouped dates.** It takes a few clicks and you have the data.

![Quarterly Totals from Monthly Data - Excel Pivot Report](https://chandoo.org/img/f/quarterly-totals-from-grouped-pivot-report.png)

1.  [Make a pivot table](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
     with your multi-year data
2.  Now add months to either “rows” or “columns” area.
3.  Sales to the “values” area.
4.  Right click on row and select “Group”
5.  Select “Quarters” and “Years” \[[learn more about grouping dates in pivot reports](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)\
    \]
6.  And your report is ready.

_**But if prefer a formula version**_, like _Martin_ does, then,

Assuming you have quarters in a column and years in a row (cells F4:H4), like this:

![Quarterly Totals from Multi-year Monthly Data in Excel](https://chandoo.org/img/f/quarterly-totals-multi-year-blanks.png)

And monthly data in the range: B4:C39,

### The formula will be,

`=SUMPRODUCT((ROUNDUP(MONTH($B$4:$B$39)/3,0)=ROWS($E$5:E5))*($C$4:$C$39)*(YEAR($B$4:$B$39)=F$4))`

### How this formula works?

Today is Friday and I am not in a mood to explain how this formula works. But I will give you some clues,

*   The Red portion finds if a month is in Q1 \[ROWS($E$5:E5) is used to get running numbers – [learn more about this technique](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/ "Using ROWS() Excel Formula to generate running numbers")\
    \]
*   The Green portion finds if a month is in the given year
*   The Blue portion is the actual values

Now,  run to the espresso machine, get a latte and figure out why this works.

### Download the example file:

I have enhanced yesterdays file with multi-year data and added both pivot report and formula based quarterly totals in the file. Go ahead and [download it](https://img.chandoo.org/f/quarterly-totals-from-monthly-data-new.xls)
. Play with the file to learn how this works.

### Share your tips and ideas:

We have excel rockstars like [_**Daniel Ferry**_](http://excelhero.com/)
 telling us some really [awesome ways to improve the formula](http://chandoo.org/wp/2010/04/29/quarterly-totals-from-monthly-data/#comment-103898)
 yesterday. I encourage you to share more tips and ideas on how you usually handle situations like these.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/quarterly-totals-multi-year-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/quarterly-totals-multi-year-data/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [group by quarter](https://chandoo.org/wp/tag/group-by-quarter/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [month](https://chandoo.org/wp/tag/month/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [year](https://chandoo.org/wp/tag/year/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFind Quarterly Totals from Monthly Data \[SUMPRODUCT Formula\]](https://chandoo.org/wp/quarterly-totals-from-monthly-data/)

[NextWow!!!, Thank You :)Next](https://chandoo.org/wp/wow-thank-you/)

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