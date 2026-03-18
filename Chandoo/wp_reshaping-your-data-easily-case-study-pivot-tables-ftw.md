# Reshaping your data easily - Case study [Pivot tables FTW] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/reshaping-your-data-easily-case-study-pivot-tables-ftw

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Reshaping your data easily – Case study \[Pivot tables FTW\]
============================================================

*   Last updated on March 16, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Late. Jayaram, my uncle is also a teacher. When I was a kid, I used to spend a lot of time with him, learning all sorts of things. He taught me chess, maths and so many life lessons. I remember one such lesson very vividly.  One day, he asked me to do something. I did it in a very long way. After seeing me struggle for several minutes, he chipped in and showed me how to do it easily. He then said, _**“when someone asks you where your nose is, you don’t twist arm around your head. You just point to your nose directly.”**_

![show-me-your-nose](https://chandoo.org/wp/wp-content/uploads/2017/03/show-me-your-nose.jpg)

The idea is that when you have a direct, simple way to do something, you should use it.

**Nose and pivot tables… how are they connected?**

We are coming to the point. Recently, learneagerly, one of our forum users asked a question about [how to transform (reshape) a set of data in Excel](http://forum.chandoo.org/threads/copy-paste-6-n-cells-from-2-different-columns-in-a-third-column.33619/)
.

**Marc L**, one of our Excel ninjas, posted an awesome VBA script to do that.

Later in the day, I chipped in and shared a formula approach to transform the data.

_I suggest checking out both approaches for learning more about VBA & INDEX formula respectively._

After posting my answer, I got thinking… May be there is a more direct way to reshape the data.

Why, yes, there is. You can use [**Pivot Tables**](http://chandoo.org/wp/excel-pivot-tables/)
.

### Let’s take a look at the data & problem first

Here is a snapshot of raw data and expected output.

![data-and-expected-output-reshaping-with-pivots](https://chandoo.org/wp/wp-content/uploads/2017/03/data-and-expected-output-reshaping-with-pivots.png)

As you can see, we have two columns of data and we need to extract _n_ (here it is 6) items from first column, then _n_ from second column and lay them out in output. We repeat this until we run out of the data.

### Reshape this thing with a Pivot

![raw-data-reshape-with-pivots-v1](https://chandoo.org/wp/wp-content/uploads/2017/03/raw-data-reshape-with-pivots-v1.png)The first step is to add two extra columns to your raw data. Let’s call them Running & Repeat.

*   **Running:** with numbers 1 thru 6 and repeat the pattern (just auto fill or copy paste)
*   **Repeat:** with 6 cells of 1, 6 cells of 2… and repeat this pattern (auto-fill)

**But what if I want a different _n_**

Even better. use formulas. Let’s say your data starts from H6:I6

*   **Running:**  \=MOD(ROWS($I$6:I6)-1,_**n**_)+1
*   **Repeat:**  \=IF(J6=1,SUM(K5,1),K5)

Related: [Using ROWS() to generate running numbers in Excel](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
.

Now that we have these extra columns, select all the data (2 columns of data + 2 extra columns we just added) and insert a pivot table.

**Set up the report by,**

*   Adding Repeat & Running to row labels area (in that order)
*   Add Col A & Col B to values area.
*   Move the **? values** to row labels area (by dragging it)
*   Position **? values** between Repeat & Running row labels.
*   Your pivot report’s last column will have the transformed data.
*   Viola, nose pointed!

![pivot-table-ftw](https://chandoo.org/wp/wp-content/uploads/2017/03/pivot-table-ftw.png)

### Download Example Workbook

[**Here is the example workbook**](https://chandoo.org/wp/wp-content/uploads/2017/03/reshape-data-with-pivots.xlsx)
. Examine the pivot table & formulas in Running & Repeat columns to learn more.

### Get your Excel muscles in to shape

_**Are you struggling to find your nose** or worse still, twisting your arm on the way?_ If so, check out our Excel school program. We have awesome online lessons, beautiful explanations, powerful techniques and easy to understand downloads. It won’t be long before you are smelling roses.

[**Check out our Excel School online class & join today**](http://chandoo.org/wp/excel-school/)
.

### How do you reshape your data?

**[Pivot Tables](http://chandoo.org/wp/excel-pivot-tables/)
 and [Power Query](http://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
 are my go to tools** for almost all kinds of reshaping problems. Often, I indulge in [INDEX formulas](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 or a bit of [VBA](http://chandoo.org/wp/excel-vba)
. For example, just a few days ago, I had to split first 100,000 digits of Pi ? in chunks of 3 digits, 3 digits and 14 digits in a pattern. As the data is too long, loading it Excel cell was impractical. Loading it in to multiple lines with each having _**x**_ digits was impractical (as I may need to split them in another pattern). So I used a simple VBA script to zap the data and get what I need.

_In case you are curious:_ I made a [chart to celebrate the Pi day](https://twitter.com/r1c1/status/841547517519044608)
 (14th of March) with our community on Twitter.

But when I am not splitting irrational stuff, I usually rely on Pivot tables or PQ.

_**What about you?**_ How do you reshape your data? Please share your approaches and tips in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/reshaping-your-data-easily-case-study-pivot-tables-ftw/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/reshaping-your-data-easily-case-study-pivot-tables-ftw/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [reader questions](https://chandoo.org/wp/tag/reader-questions/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousFiguring out Employee Churn with Power Query \[HR Analytics\]](https://chandoo.org/wp/figuring-out-employee-churn-with-power-query-hr-analytics/)

[NextSand Pendulums – Lissajous Patterns in ExcelNext](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/)

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