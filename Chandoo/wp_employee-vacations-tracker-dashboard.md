# Employee Vacation Tracker & Dashboard using MS Excel

**Source:** https://chandoo.org/wp/employee-vacations-tracker-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Designing a dashboard to track Employee vacations \[case study\]
================================================================

*   Last updated on May 11, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

HR managers & department heads always ask, _“So what is the vacation pattern of our employees? What is our average absent rate?”_

Today lets tackle that question and **learn how to [create a dashboard](http://chandoo.org/wp/excel-dashboards/)
 to monitor employee vacations.**

What do HR Managers need? (end user needs)
------------------------------------------

There are 2 aspects tracking vacations.

1.  Data entry for vacations taken by employees
2.  Status dashboard to summarize vacation data

Based on my interaction with few HR managers, the below questions are asked most often when it comes to vacation tracking:

*   What is the absent rate of our employees (in any year or latest 3 month period)
*   What are the vacation patterns for individual employees (or teams)
*   On which dates most employees are absent?
*   Who is taking most (or least) vacation days?

A look at the completed Vacation Dashboard
------------------------------------------

Take a look at the completed dashboard (click to enlarge).

[![Employee Vacation Dashboard & Tracker using Excel](https://img.chandoo.org/dashboards/employee-vacation-dashboard.png)](https://img.chandoo.org/dashboards/employee-vacation-dashboard-full-view.png)

Constructing Employee Vacation Dashboard
----------------------------------------

The construction process can be broken in to 3 steps:

1.  Vacation tracker for entering dates & types of vacations.
2.  Calculation engine
3.  Dashboard design & formatting

### Step 1: Creating a tracker for vacations

**The best way to create a tracker is to [use Excel tables](http://chandoo.org/wp/2009/09/10/data-tables/)
**. Set up one with 4 columns – Employee name, vacation type, start date & end date, like below:

![Employee vacations tracker made using Excel tables](https://img.chandoo.org/dashboards/vacation-tracker-data.png)

**By using tables, we can continue to add more vacation data (or remove older data) and all our formulas continue to work seamlessly.**

**Additional tables required…**

Apart from the main vacations table, we need below tables:

*   Employees table – to keep the names of employees
*   Vacation types table – to keep the type of vacations
*   Holidays table – with official holiday dates

### Step 2: Calculation engine

There are 3 portions in our dashboard and each of them requires certain calculations.

1.  Date logic
2.  Employee view
3.  Calendar view

For all the views, _the main driver is latest date_, which is the maximum value of end date column in vacations table (=MAX(Vacations\[End Date\]))

Tip: [Use Max to find latest date](http://chandoo.org/wp/2012/06/14/use-max-to-find-latest-date-in-a-list/)

_Although the calculations are not very complex, explaining each of them can be very tedious_. So let me summarize them with a diagram.

![Anatomy of the calculation engine - Employee vacation dashboard](https://img.chandoo.org/dashboards/calculation-engine-mind-map-employee-vacation-dashboard.png)

### Important formulas used in the calculations:

The key formulas & ideas used are,

*   [Range lookup formula](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
    
*   [SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    
*   [Calendar formulas](http://chandoo.org/wp/2009/12/11/2010-calendar-excel-template-downloads/)
    
*   [EDATE, EOMONTH, WEEKDAY, NETWORKDAYS Formulas](http://chandoo.org/wp/tag/date-and-time/)
    
*   _The lovely INDEX formula_

### Step 3: Dashboard design & formatting

This dashboard is an excellent example of synthesis – _combination of multiple Excel features to create something very simple and easy to use._

### Excel features & ideas used:

There are many Excel features & ideas used in this dashboard. First take a look at the illustration below.

![Excel features used in employee vacation dashboard](https://img.chandoo.org/dashboards/excel-features-used-in-employee-vacation-dashboard.png)

1.  [Combo box form control](http://chandoo.org/wp/2011/03/30/form-controls/#combo-box)
     to select an employee to highlight their vacations
2.  [Conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/ "Conditional formatting basics")
     & cell grid to show vacations in a [gantt chart like view](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
    .
3.  Highlighting selected employee’s vacations _again using conditional formatting._
4.  Calendar view created by [picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    
5.  Heat map of number of people away on each date using conditional formatting ([similar example](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/ "Flu Trends Chart in Excel")
    ).
6.  Header section with references to calculations & cell formatting.
7.  [Hyperlink](http://chandoo.org/wp/2011/03/31/excel-hyperlinks/ "Excel Hyperlinks & links")
     on a rounded rectangle shape to link to tracker sheet.

### Formatting the dashboard:

The basic layout of dashboard is just 3 boxes – a big summary box on top, a large employee view box (70%) and a small calendar view box (30%).

The fonts are Calibri & Cambria _default fonts in Excel 2007 or above._

I used variations of Tan color in most areas of dashboard (headers, box backgrounds, buttons etc.) and shades of pink, blue, green & gray for marking the vacations. Orange is used to highlight selected employee’s vacations.

Although there is a lot of data, I designed this dashboard with minimal clutter. It is very easy to use (there is only one input control).

Download Employee Vacation Dashboard
------------------------------------

[**Click here to download the employee vacation tracker & dashboard workbook**](https://img.chandoo.org/dashboards/vacation%20tracker%20and%20dashboard.xlsx)
. Play with it to learn more.

How do you like this dashboard?
-------------------------------

I have thoroughly enjoyed the process of building this dashboard. I especially loved how picture links, conditional formatting heat maps (color scales) & simple calendar logic all have blended in to create a stunning calendar view.

**What about you?** Do you like this dashboard? How would you have designed it? Go ahead and share your feedback, ideas & suggestions for improvements in comments. _**I am eager to learn from you.**_

Want to learn more about this dashboard?
----------------------------------------

[![Detialed tutorial on Employee Vacation Dashboard - Now available in Excel School](https://img.chandoo.org/dashboards/detailed-tutorial-on-employee-vacation-dashboard-excel-school.png)](http://chandoo.org/wp/excel-school/)

**If you want to learn how this dashboard is constructed in a detailed fashion** (along with 6 other dashboards & ton of material on dashboard design process) then please consider joining in our Excel School Dashboards program. Just today, I have uploaded a lesson (35 mins) on Employee Vacation dashboard to our Excel School website. You can use it and 32 hours more of video instruction to become awesome in Excel.

[**Click here to know more & join our Excel School program**](http://chandoo.org/wp/excel-school/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [132 Comments](https://chandoo.org/wp/employee-vacations-tracker-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/employee-vacations-tracker-dashboard/#respond)
    
*   Tagged under [calendar](https://chandoo.org/wp/tag/calendar/)
    , [combo box](https://chandoo.org/wp/tag/combo-box/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Excel Dashboard Tutorials](https://chandoo.org/wp/tag/kpi-dashboards-posts/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [networkdays()](https://chandoo.org/wp/tag/networkdays/)
    , [small business tools](https://chandoo.org/wp/tag/small-business-tools/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [trackers](https://chandoo.org/wp/tag/trackers/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousWhat is Power Pivot – an Introduction](https://chandoo.org/wp/introduction-to-power-pivot/)

[NextCan you calculate vacation days in a period? \[Homework\]Next](https://chandoo.org/wp/calculate-vacation-days/)

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
    
    [Reply](https://chandoo.org/wp/employee-vacations-tracker-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/employee-vacations-tracker-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/employee-vacations-tracker-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ