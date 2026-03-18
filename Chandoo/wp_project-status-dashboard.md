# Project Management Dashboard, Project Status Report using Excel - Templates and Downloads

**Source:** https://chandoo.org/wp/project-status-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Project Management Dashboard / Project Status Report using Excel \[Part 6 of 6\]
================================================================================

*   Last updated on October 1, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is the last installment of [project management using excel](http://chandoo.org/wp/project-management/)
 series.**_

[Preparing & tracking a project plan using Gantt Charts](https://chandoo.org/wp/gantt-charts-project-management/)
  
[Team To Do Lists – Project Tracking Tools](https://chandoo.org/wp/todo-lists-project-tracking-tools/)
  
[Project Status Reporting – Create a Timeline to display milestones](https://chandoo.org/wp/project-milestones-in-timeline/)
  
[Time sheets and Resource management](https://chandoo.org/wp/excel-time-sheets-project-management/)
  
[Part 5: Issue Trackers & Risk Management](https://chandoo.org/wp/issue-trackers/)
  
**Project Status Reporting – Dashboard**  
[Bonus Post: Using Burn Down Charts to Understand Project Progress](https://chandoo.org/wp/burn-down-charts/)

_**Communication**_ is a very important aspect of project management. Communicating with stakeholders, sponsors, team members and other interested parties takes up quite a bit of project manager’s time.

In almost all the projects I have been part of, the first and foremost question anyone used to ask us is, “how is the project going?”. There is no one line answer to this. A project status dashboard or project status report can help us express the project status in a crisp yet effective manner.

In today’s installment of project management using excel series, we will learn how to make a project management dashboard using Microsoft excel. \[related: [Making Dashboards using Excel](https://chandoo.org/wp/excel-dashboards/)\
\]

### To make the project management dashboard, you must answer the following questions,

*   **Who is the audience of this dashboard?**
    *   Top management or project sponsors or team members or other departments?
*   **What are they interested to know?**
    *   Day to day issues or High level stuff or Plans or Budgets?
*   **What is the frequency for updating the dashboard?**
    *   Weekly, Bi-weekly or Monthly or Once in a blue moon?

The answers to these questions will determine what goes in to the dashboard and how it should be constructed.

For our example, I have assumed the following scenario, but you can easily change the dashboard constituents based on your situation.

*   **Audience of the report:** Project Sponsorship Team
*   **Interested to know:** Project Progress wrt Plan, Blocking issues, Overall timeline and Delivery Progress
*   **Frequency:** _irrelevant_ (could be weekly or bi-weekly)

Step 1: Make an outline sketch of the dashboard
-----------------------------------------------

Based on the above answers, we vaguely know what should go in to the dashboard. Based on this, we should make an outline sketch of the dashboard. This will help you structure the dashboard on an excel spreadsheet. For our example, this is the outline I have prepared.

![Project management dashboard - outline sketch](https://chandoo.org/img/pm/project-status-dashboard-outline.png)

_**the finalized dashboard will look like this:**_ ([click here](http://chandoo.org/img/pm/project-status-dashboard-l.png)
 for a bigger version)  
[![Project Management Dashboard](https://chandoo.org/img/pm/project-status-dashboard-s.png)](http://chandoo.org/img/pm/project-status-dashboard-l.png)

Step 2: Get the data to be placed on dashboard
----------------------------------------------

[Making a dashboard in excel](http://chandoo.org/wp/management-dashboards-excel/)
 is a complex and intricate process. Knowing the outline of the dashboard is only the 10% of work. Getting your data to calculate the dashboard metrics (or KPIs) is the most vital part of any dashboard construction.

In our outline, the sections 1,2 and 3 are purely data and 4,5 and 6 are charts prepared from data.

To facilitate this, first, let us create a worksheet named _**“data”**_ where we can capture user inputs. These inputs can be further manipulated to make the dashboard.

**For our dashboard, we need the following inputs,**

*   Overall project status and progress
*   List of ongoing activities and issues

**We will derive other inputs from the following,**

*   [Project Plan Gantt Chart](https://chandoo.org/wp/gantt-charts-project-management/)
     discussed in Part 1 will provide us the project plan
*   [Project Timeline Chart](http://chandoo.org/wp/2009/07/09/project-milestones-in-timeline/)
     in Part 2 will give us the timeline chart
*   [Burn down chart](http://chandoo.org/wp/2009/07/21/burn-down-charts/)
     will give us the project deliverable status
*   [Issue Tracker](http://chandoo.org/wp/2009/09/08/issue-trackers/)
     discussed in Part 5 will give us the metrics related to issues

Step 3: Put everything together and make a dashboard
----------------------------------------------------

\[PS: I have greatly simplified the process of dashboard construction to keep the article readable. Please note that this step usually takes a few of hours and has lot more detail\]

Now that we have all the bits of our data ready, we just need to bring them together to make a dashboard.

**We will use the following excel concepts,**

*   [Excel Camera Tool](https://chandoo.org/wp/how-to-use-picture-links/)
     to get a live snapshot of the project gantt chart
*   [Conditional Formatting](https://chandoo.org/wp/excel-conditional-formatting-basics/)
     to show Red, Green or Amber traffic light to depict the project status
*   [Thermo-meter chart](https://chandoo.org/wp/thermometer-charts-in-excel-howto/)
     to show the project progress against 100% total
*   We will create a stacked bar chart of _**outstanding issues**_ by using [SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
    . \[counts for issue status=”open” and issue priority=”high”, issue status=”open” and issue priority=”medium”, issue status=”open” and issue priority=”low”\]

**Let us place the remaining pieces of dashboard from already constructed charts and available data,**

*   [Burn-down chart](https://chandoo.org/wp/burn-down-charts/)
     to show the project deliverable status
*   [Project Time line](https://chandoo.org/wp/project-milestones-in-timeline/)
     to show the project milestones over a period of time
*   We will create references to the “issue” and “activity” data and show only the first 5 items.

**See the below illustration to understand how each part of the dashboard is constructed.**

![Project Status Report / Dashboard - Construction](https://chandoo.org/img/pm/project-status-dashboard-report-construction.gif)

That is all, our dashboard is ready now.

Download the project management dashboard excel file
----------------------------------------------------

Unlike other downloads on Chandoo.org, this file is locked. You can purchase unlocked version along with 23 other project management templates – [**Click here to buy it.**](https://chandoo.org/wp/project-management-templates/)

*   To download the locked version of project management dashboard excel file click these links:  [excel 2003](http://chandoo.org/img/d/project-status-dashboard-xl2003.zip)
    , [excel 2007](http://chandoo.org/img/d/project-status-dashboard-xl2007.zip)
    
*   To get an unlocked version of the dashboard along with 23 other templates, **[click here](http://chandoo.org/wp/project-management-templates/)
    **.

Tell us about your Project Management Dashboard / Status Report
---------------------------------------------------------------

Tell me about your project management dashboard, project status report formats and how it is constructed. Do you use excel or some other tool (like powerpoint, word) to prepare the report? How the report / dashboard generated? Is the process automated or manual? What have you learned from using / making such status reports?

Resources for Project Managers
------------------------------

Check out my [Project Management using Excel page](http://chandoo.org/wp/project-management/)
 for more resources and helpful information on project management.

Also check out below posts to make your project management files awesome.

*   [Project Portfolio Management Dashboard](https://chandoo.org/wp/design-project-portfolio-dashboard/)
    
    [![Project Portfolio Dashboard Template](https://img.chandoo.org/pm/project-portfolio-dashboard-small.png)](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/)
    
*   [Gantt Box chart – depict uncertainty in your projects](https://chandoo.org/wp/gantt-box-chart-tutorial-template/)
    
*   [Excel Risk Map template](https://chandoo.org/wp/excel-risk-map-template/)
    

What next?
----------

This is the last installment of project management using excel series. I am looking for ideas to extend this series in useful manner. Please use comments to tell me what other activities of project management can be made easy using Microsoft Excel. I will try to write follow up posts if the topics are interesting.

**Thanks a lot for reading the series and suggesting valuable inputs to make it better**. I have learned a lot about project management and excel writing this series. I hope you have picked up few concepts too.

Tell me your feedback using comments.

[![Project Management Templates for Excel](https://chandoo.org/img/ads/project-management-bundle-excel-ad-4.png)](http://chandoo.org/wp/project-management-templates/ "Project Management Templates for Excel")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [49 Comments](https://chandoo.org/wp/project-status-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/project-status-dashboard/#respond)
    
*   Tagged under [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [camera tool](https://chandoo.org/wp/tag/camera-tool/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [thermometer charts](https://chandoo.org/wp/tag/thermometer-charts/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMake a Bubble Chart in Excel \[15 second tutorial\]](https://chandoo.org/wp/bubble-chart-tutorial/)

[NextAnother Reason why Tables are so awesome \[quick tip\]Next](https://chandoo.org/wp/excel-tables-scroll-feature/)

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
    
    [Reply](https://chandoo.org/wp/project-status-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/project-status-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/project-status-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ