# Excel Timesheet Templates, Resource Management Templates - Project Management using Excel Spreadsheets

**Source:** https://chandoo.org/wp/excel-time-sheets-project-management

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Time Sheets and Resource Management \[Project Management using Excel – Part 4 of 6\]
==========================================================================================

*   Last updated on October 1, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is the fourth installment of [project management using excel](https://chandoo.org/wp/project-management/)
 series.**_

[Preparing & tracking a project plan using Gantt Charts](https://chandoo.org/wp/gantt-charts-project-management/)
  
[Team To Do Lists – Project Tracking Tools](https://chandoo.org/wp/todo-lists-project-tracking-tools/)
  
[Project Status Reporting – Create a Timeline to display milestones](https://chandoo.org/wp/project-milestones-in-timeline/)
  
**Part 4: Time sheets and Resource management**  
[Issue Trackers & Risk Management](https://chandoo.org/wp/issue-trackers/)
  
[Project Status Reporting – Dashboard](https://chandoo.org/wp/project-status-dashboard/)
  
[Bonus Post: Using Burn Down Charts to Understand Project Progress](https://chandoo.org/wp/burn-down-charts/)

![Timesheets are like TPS reports - Necessary for Managers, May be annoying for team members](https://chandoo.org/img/pm/tps-reports-thumb.png)Timesheets are like TPS reports\* of any project. Team members think of them as an annoying activity. For managers, timesheets are a vital component to understand how team is working and where the effort is going. I will not get in to the merits and pitfalls of timesheets. However, I feel that by using Microsoft Excel capabilities you can create a truly remarkable timesheet tracking tool and still leave your team members un-annoyed.

In this tutorial we will learn 3 things about timesheets and resource management using Excel

1.  How to setup a simple timesheet template in excel?
2.  How to make a more robust timesheet tracker tool in Excel?
3.  How to use the timesheet data to make a resource loading chart?

1\. Make a Simple Excel Timesheet Template
------------------------------------------

[According to Wikipedia](https://en.wikipedia.org/wiki/Timesheet)
, timesheets are used for

> Timesheets may record the start and end time of tasks, or just the duration. It may contain a detailed breakdown of tasks accomplished throughout the project or program. This information may be used for payroll, client billing, and increasingly for project costing, estimation, tracking and management.

By defining a simple and straight forward template in Excel and using it to track time (or efforts) in your projects, you can easily consolidate the data, compare efforts and make any necessary analysis.

At its simplest form, the timesheet is nothing but list of team members and list of activities in a matrix. Look at the below example:

![Simple timesheet template using microsoft excel](https://chandoo.org/img/pm/simple-timesheet-excel-format.png)

You can easily create such template in excel.

2\. A More Robust Excel Timesheet Tracker
-----------------------------------------

While the time sheet format shown in the above section is good, it is a wrong format if you need to analyze the timesheet entries of a 100 member project. Also in large projects usually members do few activities at a time. That means the above format (in section 1) will result in a sparse matrix.

Using a tracker log format is much more convenient to both record and analyze timesheet entries. Look at the example below:

![Timesheet Tracker template using microsoft excel](https://chandoo.org/img/pm/timesheet-tracker-log.gif)

We can use excel features like [data validation drop downs](https://chandoo.org/wp/excel-add-drop-down-list/)
, shared workbooks to make the timesheet entry and management a breeze.

3\. Create a Resource Loading Chart – Project Management
--------------------------------------------------------

Resource loading charts are a good way to show how busy the team members are in a project. At the outset the resource loading chart is nothing but a [heatmap](https://chandoo.org/wp/partition-charts-excel-pie-alternative-visualization-hack/ "Excel Heatmap tutorial")
.

Look at an example resource loading chart below:

![Resource loading chart example using excel charts](https://chandoo.org/img/pm/resource-loading-chart-project-management.png)

You can make a resource loading chart in MS Excel by following the below steps:

1.  The pre-condition for the resource loading chart is that we have clear data available to make one. This is where the robust timesheet tracker shown in section 2 of this post comes handy.
2.  First create a blank table in excel with team member names in first column and week numbers in first row. (Please note, you can make other types of resource loading charts by changing the Row and Column headers. For eg. You can show resource loading by Project and Team member)
3.  Assuming we have the time sheet data in the format shown in Section 2,
4.  Assuming “log\_member\_names” refers to the member name column and log\_weeknum refers to the last column in the timesheet, we can write a simple COUNTIFS formula like this =COUNTIFS(log\_member\_names, “John Galt”, log\_weeknums, 3)
5.  Once we calculate values for all team members using the above formula, we can [apply conditional formatting](https://chandoo.org/wp/excel-conditional-formatting-basics/)
     to make the heat map. In Excel 2016 / 365, this is one step.   
    ![Resource loading chart using conditional formatting heatmaps](https://chandoo.org/img/pm/resource-loading-chart-conditional-formatting.png)
6.  That is all.

Download the Excel Timesheet & Resource Loading Chart Templates
---------------------------------------------------------------

You can download the excel time sheet template, timesheet tracker log template and resource loading chart template from here. Click the below links:

*   If you have Excel 2016 / 365  or 2007 or above, [download the .xlsx template](https://chandoo.org/wp/wp-content/uploads/2019/10/resource-and-timesheet-templates.xlsx)
    
*   If you have Excel 2003 and earlier, [download the .xls template](https://chandoo.org/wp/wp-content/uploads/2019/10/resource-and-timesheet-templates.xls)
    
*   [Download 24 Project Management Templates for Excel](https://chandoo.org/wp/project-management-templates/ "Project Management Templates for Excel")
    

What Next?
----------

Timesheets are a great way to understand how the effort is spent. Even though project estimation models have become more and more effective, still lots of projects are overshooting budgets and timelines. And this is where timesheets can help you as a manager. While estimation looks in to future, timesheets look at past. Timesheets give feedback to your estimation models. This can help you in making better estimates in future.

**In the next installment of this series, learn about [tracking issues and risks using excel spreadsheets](https://chandoo.org/wp/issue-trackers/)
.**

If you are new to the series, please read the first 3 parts as well.

*   [Preparing & tracking a project plan using Gantt Charts](https://chandoo.org/wp/gantt-charts-project-management/)
    
*   [Team To Do Lists – Project Tracking Tools](https://chandoo.org/wp/todo-lists-project-tracking-tools/)
    
*   [Project Status Reporting – Create a Timeline to display milestones](https://chandoo.org/wp/project-milestones-in-timeline/)
    
*   While at it, also check out the bonus post about [Burn Down Charts](https://chandoo.org/wp/burn-down-charts/)
    .

### Resources for Project Managers

Check out my [Project Management using Excel page](https://chandoo.org/wp/project-management/)
 for more resources and helpful information on project management.

**Your thoughts and suggestions?**

What are your ideas about timesheets using excel? Does your organization use excel as a way to manage timesheets or do you use some time tracking software? What is the granularity of detail captured in timesheets? As a project manager, what use do you find in time sheet data?

Share your ideas and experiences using comments.

\*PS: If you are wondering what the heck TPS reports are, then you are spending way too much time with Excel buddy. And while at it, you missed the greatest comedy of all time. Go watch [office space](https://www.imdb.com/title/tt0151804/)
, now!

PPS: the TPS report image is from [wikipedia](https://en.wikipedia.org/wiki/File:Tps_report.png)
.

[![Project Management Templates for Excel](https://chandoo.org/img/ads/project-management-bundle-excel-ad-4.png)](https://chandoo.org/wp/project-management-templates/ "Project Management Templates for Excel")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [33 Comments](https://chandoo.org/wp/excel-time-sheets-project-management/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-time-sheets-project-management/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [resource loading chart](https://chandoo.org/wp/tag/resource-loading-chart/)
    , [resource management](https://chandoo.org/wp/tag/resource-management/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [timesheet tracker](https://chandoo.org/wp/tag/timesheet-tracker/)
    , [timesheets](https://chandoo.org/wp/tag/timesheets/)
    , [timestamps](https://chandoo.org/wp/tag/timestamps/)
    , [tps reports](https://chandoo.org/wp/tag/tps-reports/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousIf Excel is a Superhero … \[5k Contest and Giveaway\]](https://chandoo.org/wp/if-excel-is-a-superhero/)

[NextCount the number of unique values in a range \[Quick Tip\]Next](https://chandoo.org/wp/count-number-of-unique-cells/)

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
    
    [Reply](https://chandoo.org/wp/excel-time-sheets-project-management/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-time-sheets-project-management/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-time-sheets-project-management/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ