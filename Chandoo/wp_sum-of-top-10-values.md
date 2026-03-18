# Calculate sum of top 10 values [formulas + homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/sum-of-top-10-values

---

*   [Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Calculate sum of top 10 values \[formulas + homework\]
======================================================

*   Last updated on August 3, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Analyzing top _n_ (or bottom _m_) items is an important part of any data analysis exercise. In this article, we are going to learn Excel formulas to help you with that.

Let’s say you are the lead analyst at a large retail chain in Ohio, USA. You are looking at the latest sales data for all the 300 stores. You want to calculate the total sales of top 10 stores.  Read on to learn the techniques.

### Meet the data

So here is the data we have. It is arranged in an [Excel table](http://chandoo.org/wp/2009/09/10/data-tables/)
, named **Sales**.

![sum-of-top-10-values-excel](https://chandoo.org/wp/wp-content/uploads/2015/08/sum-of-top-10-values-excel.png)

We need to answer to 2 questions.

*   What is the sum of top _**n**_ sales?
*   What is the sum of top _**n**_ sales for filtered data (say store=Dayton)?

### Sum of top n sales

First let’s take a look the formula.

`=SUMIFS(sales[Revenues],sales[Revenues],">="&LARGE(sales[Revenues],n))`

\[Related: [using structural references in Excel](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/)\
\]

**How does this formula work?**

There are 2 components in this formula:

1.  We need to sum up revenues column
2.  Such that, revenue >= top _n_th revenue

**Finding the top nth value:**

This is where [LARGE formula](http://chandoo.org/wp/2008/08/13/15-microsoft-excel-formulas/)
 helps. It looks at the revenue column and returns nth value.

**Sum of top n values thru SUMIFS:**

Then, SUMIFS formula calculates the total revenues where revenue >= top nth value.

\[Related: [Introduction to SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)\
\]

### Sum of top n sales in filtered data

This one is tricky. First, we will add an extra column to the _sales_ table. You can later hide this if you want.

This column just tells us whether a particular store is hidden or visible (ie filtered away or not).

Use the formula,

`=SUBTOTAL(3, [@Store]) = 1` in the new column. This will be TRUE if a row is visible and FALSE if a row is filtered away.

See below illustration to understand the formula.

![test-if-a-row-is-visible-or-hidden](https://chandoo.org/wp/wp-content/uploads/2015/08/test-if-a-row-is-visible-or-hidden-v2.png)

Next, we can use below formula to calculate the total of top n sales in filtered data:

`=SUMIFS(sales[Revenues],sales[Visible?],TRUE, sales[Revenues],">="&AGGREGATE(14,5,sales[Revenues],n))`

**How does this formula work?**

Again, we are using SUMIFS formula, but with 2 conditions.

1.  Store should be visible
2.  Revenue >= top nth revenue in visible stores

To calculate the top n value of a visible stores, we use AGGREGATE formula.

**`AGGREGATE(14,5,sales[Revenues],n)` – what does it do?**

AGGREGATE formula takes 3 or 4 parameters.

1.  Calculation number – 14 corresponds to LARGE
2.  Which data to ignore – 5 corresponds to ‘ignore hidden rows’
3.  Data – Sales\[Revenues\]
4.  n – optional parameter for LARGE or SMALL calculations

So, our `AGGREGATE(14,5,sales[Revenues],n)` formula will **return top nth value among the filtered data**.

Once we know that value, we just use SUMIFS to sum up all values greater than or equal to it.

### Download Example Workbook

**[Click here to download the sum of top 10 values workbook](https://chandoo.org/wp/wp-content/uploads/2015/08/sum-of-top-10-values.xlsx)
**. Play with the formulas to learn more. Also, attempt the homework problems and post your answers in comments.

### Your home work – 2 challenges:

So now that you understood how to calculate sum of top n values, I have 2 home work problems.

1.  What is the sum of bottom 10 values excluding zero values?
2.  What is the sum of bottom 10 values in filtered list, excluding zeros?

_**Go ahead and post your answers as comments.**_

### 6 more tips on analyzing top n values

Here are few more ways to analyze with top /bottom n  values.

*   [Sum of top 3 values that meet a criteria](http://chandoo.org/wp/2013/05/17/sum-of-top-3-values-meeting-criteria/)
    
*   [Show top 10 values in dashboards using pivot tables](http://chandoo.org/wp/2010/12/01/top-10-values-in-dashboards/)
    
*   [Calculating average of top 5 values](http://chandoo.org/wp/2010/06/04/average-of-top-5-values/)
    
*   [Create a top X chart](http://chandoo.org/wp/2009/11/12/topx-chart/)
    
*   [Highlight top 10 values using conditional formatting](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
    
*   [Find out nth largest value that meets a criteria using array formulas](http://chandoo.org/wp/2010/10/08/large-if-array-formula-tutorial/)
    

_This post is part of our [Awesome August](http://chandoo.org/wp/resources/awesome-august/)
  Excel Festival._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [35 Comments](https://chandoo.org/wp/sum-of-top-10-values/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/sum-of-top-10-values/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [aggregate()](https://chandoo.org/wp/tag/aggregate/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [top 10 values](https://chandoo.org/wp/tag/top-10-values/)
    
*   Category: [Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to highlight overdue items](https://chandoo.org/wp/overdue-items/)

[NextSave time with custom ribbons in Excel \[tutorial\]Next](https://chandoo.org/wp/custom-ribbons/)

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