# Quick and easy Gantt chart using Excel [templates] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/quick-gantt-chart-excel-template

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Quick and easy Gantt chart using Excel \[templates\]
====================================================

*   Last updated on February 18, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**[Gantt charts](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 are a very popular way to visually depict project plans**. Today, let us learn how to use Excel to make quick & easy Project Plan Gantt Chart.

This is what we will be creating,

![Quick gantt chart using Excel - download template](https://img.chandoo.org/pm/quick-gantt-chart-template-excel.png)

### Step 1: Set up project plan grid

First step is simple.

In a blank worksheet, set up an empty grid like this:

![Quick gantt chart - data entry grid explained](https://img.chandoo.org/pm/quick-gantt-chart-data-entry-grid.png)

Key things to note:

*   Project start date goes in to _cell C3_
*   Project dates appear from cell D5 & D6 onwards, one day per column.
*   Make the grid as big as you want. I choose 20 activities x 120 days.

### Step 2: Fill up dates

Now, lets load the dates in to the plan. The first day of the project is known (_it is in cell C3_.)

1.  Select D5 and point it to C3 by typing =C3
2.  Set D6 to the same value as D5 by typing = D6
3.  Now, both D5 & D6 contain the same date. (Why 2 dates? You will understand in a minute!)
4.  In next column (E), we want the next working day.
5.  So in E5 type =WORKDAY(D5, 1)
6.  Now, select D5:E5, format them so only DAY portion of date is shown. To do this, press CTRL+1 after selecting them, in Number tab, select Custom and type d, click ok.
7.  Select D6, format it so only the first letter of the month is shown instead of entire date. To do this, set number format code as MMMMM.
8.  Drag E5 sideways for all the dates.
9.  Drag D6 sideways for all the dates.
10.  Our dates are ready!

_**Here is a demo of all the steps:**_

![Demo of formulas for filling up dates - Quick gantt chart using Excel](https://img.chandoo.org/pm/quick-gantt-chart-filling-dates-demo-v1.gif)

### Step 3: Enter project plan data

Now that our grid is ready, enter the data. This is simple. Just type 1 whenever an activity is happening on a date. For example, if Activity 1 happens on 18th & 19th of February, type 1 in both cells.

![Project plan data - Quick gantt chart template](https://img.chandoo.org/pm/gantt-chart-grid-with-sample-data.png)

### Step 4: Calculating Duration

This is really simple. In the duration column, select first cell and type =COUNT(D7:DS7)

_Note: Make sure you change the cell references based on the number of columns and where your data is!_

Drag down the formula to get duration for all activities.

### Step 5: Apply conditional formatting

Now that all the plan data is ready, lets tell Excel to highlight all 1’s so that we get a Gantt chart. Quick & Easy!

1.  Select the entire grid (excluding activity names, durations & dates)
2.  Go to Home > Conditional formatting > New rule (Related: [Introduction to conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    )
3.  Specify a rule to fill color in all cells with 1.
4.  Also, set cell formatting to ;;; so that the contents (ie 1s) are not visible. (Related: [Making cell contents invisible](http://chandoo.org/wp/2009/06/05/hide-cell/)
    )
5.  See the conditional formatting rule I have used below:

![Conditional formatting rule for quick gantt chart - explained](https://img.chandoo.org/pm/conditional-formatting-rule-gantt-chart-excel.png)

**Bonus trick: Visually separate weeks with a border**

Since our plan has many weeks, it would be cool to show a vertical line between every week. To do this:

1.  Select the grid again.
2.  Add a new conditional formatting rule
3.  Select the type of rule as “Use a formula…”
4.  Use this formula =WEEKDAY(D$5) = 6
5.  Set up formatting so that right-side vertical border is shown when the rule is met.
6.  You are done!

![Conditional formatting rule for highlighting weeks - quick gantt chart in excel](https://img.chandoo.org/pm/highlight-weeks-gantt-chart-excel.png)

### That’s all, our quick Gantt chart is ready

_That is all. Your quick project plan is ready_. Go ahead and show it off. Use it for an upcoming project and impress your boss.

### Download the quick Gantt chart template

[**Click here to download the template**](https://img.chandoo.org/pm/quick-gantt-chart-template.xlsx)
. It contains instructions on how to modify the template. Go ahead and example the formulas, conditional formatting rules to understand more.

### How do you like this quick & easy template?

Although I have a lot of complex project plan templates, often I rely something quick & easy like this. It simply works and lets me focus on the project at hand.

**What about you?** Do you use quick templates like this? _Please share your experiences and ideas using comments_.

### More on Project Management using Excel

Are you a project manager or analyst? Here are a few more examples, templates & resources for you.

*   [Excel Project Management page – huge collection of tips, resources and downloads](http://chandoo.org/wp/project-management/)
    .
*   [Gantt charts using Excel](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
    
*   [Project status dashboard using Excel](http://chandoo.org/wp/2009/10/06/project-status-dashboard/)
    
*   [Project Portfolio dashboard using Excel](http://chandoo.org/wp/2012/11/19/project-portfolio-dashboard-excel-template/)
    

If you are a project manager or analyst, you would be working with Gantt charts, status reports, issue trackers & project dashboards every day. If you are tired of creating these from scratch, get my Excel Project Management template pack.

It contains 25+ Excel templates for various needs of project management – right from planning to tracking to reporting. All beautifully designed and easy to customize so that you can be an awesome project manager.

[**Click here to know more and get your copy today**](http://chandoo.org/pmt/pmt-index-1.html)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [35 Comments](https://chandoo.org/wp/quick-gantt-chart-excel-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/quick-gantt-chart-excel-template/#respond)
    
*   Tagged under [charts](https://chandoo.org/wp/tag/charts/)
    , [custom cell formatting](https://chandoo.org/wp/tag/custom-cell-formatting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [workday](https://chandoo.org/wp/tag/workday/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousLearn how to create these 11 amazing dashboards](https://chandoo.org/wp/dashboard-training-course/)

[NextHeads up! Our Join Power Pivot classNext](https://chandoo.org/wp/heads-up-our-join-power-pivot-class/)

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
    
    [Reply](https://chandoo.org/wp/quick-gantt-chart-excel-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/quick-gantt-chart-excel-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/quick-gantt-chart-excel-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ