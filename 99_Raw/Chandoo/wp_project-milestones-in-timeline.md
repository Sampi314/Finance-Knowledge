# Project Management: Show Milestones in a Timeline [Excel Template and Tutorial]

**Source:** https://chandoo.org/wp/project-milestones-in-timeline

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Project Management: Show Milestones in a Timeline \[Part 3 of 6\]
=================================================================

*   Last updated on October 2, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is the third installment of [project management using excel](https://chandoo.org/wp/project-management/)
 series.**_

[Preparing & tracking a project plan using Gantt Charts](https://chandoo.org/wp/gantt-charts-project-management/)
  
[Team To Do Lists – Project Tracking Tools](https://chandoo.org/wp/todo-lists-project-tracking-tools/)
  
**Part 3: Project Status Reporting – Create a Timeline to display milestones**  
[Time sheets and Resource management](https://chandoo.org/wp/excel-time-sheets-project-management/)
  
[Issue Trackers & Risk Management](https://chandoo.org/wp/issue-trackers/)
  
[Project Status Reporting – Dashboard](https://chandoo.org/wp/project-status-dashboard/)
  
[Bonus Post: Using Burn Down Charts to Understand Project Progress](https://chandoo.org/wp/burn-down-charts/)

### Why Create Project Timeline Chart?

There are 2 key elements in all the successful projects I have been part of.

*   They had exceptional individuals who are also exceptional team players
*   The communication and collaboration is really good.

While there is little that project management software can do when it comes to first point, the second point can be addressed by using right tools and visualizations. In this installment and the part 5 and 6 of this series, we will learn some excel based visualizations / charts that can help you to communicate about the project status and progress to your team and stake holders.

Project milestones can be shown in a simple time line chart in excel. While the chart doesn’t look complicated, it can provide good amount of information on project progress in a simple and understandable chart.

**We will learn to create a project milestone chart like this:**  
![Project Status Reporting - Show Timeline of Milestones](https://chandoo.org/img/pm/project-timeline-chart-excel.png)

### Steps to create a project milestone chart in excel

1.  **In order to create a project milestone chart, we need to have the milestone data.** The simplest format for milestone data is Date and the milestone. But since our chart requires the milestone to be displayed at a certain height on the chart, we will add the third column – height.  
    ![Project Status Reporting - Show Timeline of Milestones - Data for the chart](https://chandoo.org/img/pm/Project-Milestones-data-for-timeline-reporting.png)  
    PS: the height column can be easily calculated using formulas. I leave it to your imagination.
2.  Once you have the data in the above format, **we will add 2 more helper columns – named DUMMY and Milestone.** The Dummy column is used to create the timeline (where Y axis value is zero). The milestone column is a more cleaned up version of milestones (see how it is showing #NA where the milestone is blank.)  
    ![Project Status Reporting - Show Timeline of Milestones - Helper Data for the chart](https://chandoo.org/img/pm/helper-data-to-create-timelines-project-management.png)
3.  Now, select the date and dummy columns and insert a line chart.  
    ![Project Status Reporting - Show Timeline of Milestones - Add a line chart](https://chandoo.org/img/pm/1-add-a-line-chart-project-mgmt-excel.png)
4.  To this chart, we will add one more data series – Height column.  
    ![Project Status Reporting - Show Timeline of Milestones - Add another series](https://chandoo.org/img/pm/2-add-one-more-data-series-project-timelines.png)
5.  Now **select the height data series and change the chart type to a bar chart**. Also set the height series to be plotted on secondary axis. Learn more about [combining 2 chart types](https://chandoo.org/wp/2009/01/05/excel-combination-charts/)
     and [adding secondary axis](https://chandoo.org/wp/secondary-axis-combination-charts-howto/ "Add secondary axis to a chart")
     in excel.  
    ![Project Status Reporting - Show Timeline of Milestones - Change data series chart type](https://chandoo.org/img/pm/3-change-chart-type-project-reporting.png)
6.  We will also **set the horizontal / axis labels** for the height series as the “milestones”. We need to do this so that when we set the data labels for the height series, we will see the milestone instead of month.  
    ![Project Status Reporting - Show Timeline of Milestones - Change horizontal labels - data series](https://chandoo.org/img/pm/4-add-axis-labels-data-source-project-management.png)
7.  **At this point our chart should look like this:**  
    ![Project Status Reporting - Show Timeline of Milestones - Chart looks like this now](https://chandoo.org/img/pm/5-intermediate-version-of-timeline-chart.png)
8.  Now, we will **add data labels to the height series**. Set the label type as “category”
9.  We will also **add error bars to the height series** (the bar chart). We will configure the error bar in such a way that they are shown 100% on the negative side only.
10.  **After doing this, the chart should look like this:**  
    ![Project Status Reporting - Show Timeline of Milestones - Add error bars and data labels](https://chandoo.org/img/pm/6-add-error-bars-and-data-labels.png)
11.  Finally we will do some formatting like,
    
    1.  Removing fill color / line from height series by setting them to None / transparent.
    2.  Changing the error bar color to a dull shade of gray.
    3.  Adding chart title and aligning it.
    4.  Removing vertical axes and gridlines.
    5.  Formatting horizontal axis – changing label orientation, removing tick marks.
    
    After all this is done, our project milestone time line chart should look like this:  
    ![Project Status Reporting - Show Timeline of Milestones](https://chandoo.org/img/pm/project-timeline-chart-excel.png)
    
12.  That is all, we now have a cool looking project milestone chart ready. Now go and achieve a milestone.

### Download the Project Milestones Time Line chart template:

I am sure you are overwhelmed reading the above tutorial. You are probably thinking if it is easier to work towards the project milestones than creating this chart. Well, don’t worry. You can download the [time line chart template](https://chandoo.org/wp/wp-content/uploads/2019/10/project-timeline.xls)
 and play with it to suit your needs.

_[Download 24 Project Management Templates for Excel](https://chandoo.org/wp/project-management-templates/ "Project Management Templates for Excel")
_

### What next?

Project timelines are a great way to tell the story of project to strangers and new people joining your project. They are a good addition to project status meetings and reports.

In the next installment of this series, we will learn [how to use Excel to manage timesheets and resources](https://chandoo.org/wp/excel-time-sheets-project-management/)
.

If you are new, please read the first 2 parts of this series: [Project planning using gantt charts](https://chandoo.org/wp/gantt-charts-project-management)
, [Tracking day to day project progress with team todo lists](https://chandoo.org/wp/todo-lists-project-tracking-tools/)
.

### Your thoughts and suggestions?

What are your ideas on communicating project progress to stakeholders and new comers? What do you think about this tutorial? Please share through comments.

[![Project Management Templates for Excel](https://chandoo.org/img/ads/project-management-bundle-excel-ad-4.png)](https://chandoo.org/wp/project-management-templates/ "Project Management Templates for Excel")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [86 Comments](https://chandoo.org/wp/project-milestones-in-timeline/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/project-milestones-in-timeline/#respond)
    
*   Tagged under [axis labels](https://chandoo.org/wp/tag/axis-labels/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [data labels](https://chandoo.org/wp/tag/data-labels/)
    , [data series](https://chandoo.org/wp/tag/data-series/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [pm](https://chandoo.org/wp/tag/pm/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [timelines](https://chandoo.org/wp/tag/timelines/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to Round and Sort Data using Excel Formulas?](https://chandoo.org/wp/excel-formulas-round-sort/)

[NextMake an Impressive Product Catalog \[spreadsheets for small business\]Next](https://chandoo.org/wp/product-catalogs/)

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
    
    [Reply](https://chandoo.org/wp/project-milestones-in-timeline/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/project-milestones-in-timeline/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/project-milestones-in-timeline/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ