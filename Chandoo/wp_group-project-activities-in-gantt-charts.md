# Group Project Activities to Make Readable Gantt Charts - Excel Gantt Charts

**Source:** https://chandoo.org/wp/group-project-activities-in-gantt-charts

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Group Project Activities to Make Readable Gantt Charts
======================================================

*   Last updated on February 11, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

In [Excel Gantt Charts](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 part of our project management series, we have discussed about how using Conditional Formatting and Formulas we can make a gantt chart like this:

![Gantt Chart - Excel - Project Plan](https://chandoo.org/img/pm/gantt-chart-project-management.png)

But when you have large project plans, gantt charts like above can get pretty intense and hard to read. **So a better approach is to group various tasks in project plan – _like this:_**

![Readable Gantt Chart with Project Activities Grouped](https://chandoo.org/img/pm/project-gantt-chart-with-groups.png "Readable Gantt Chart with Project Activities Grouped")

In this article, **we will learn how you can make such a grouping in a regular gantt chart.**

For this tutorial, we will choose a familiar project – _**Project Peanut Butter Jelly Sandwich**_. (If you dont know what a PBJ is, you should find-out, prepare and eat one before reading any further. I am serious…)

### Step 1: Make the regular project plan gantt chart in the following format

We will not talk about making a regular gantt chart. Here is an excellent tutorial on [making excel gantt charts](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 ([and one more](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
).

Once you are done, the chart should look like this:  
![Gantt Chart without Project Activities Grouped](https://chandoo.org/img/pm/project-gantt-chart-without-groups.png "Gantt Chart without Project Activities Grouped")

### Step 2: Add a new column and define groups of activities

This is very simple. Just add a new column (preferably to the left of activities) and define groups of project activities there. Like this,  
![Add groups to project tasks](https://chandoo.org/img/pm/add-groups-to-plan.png "Add groups to project tasks")

### Step 3: Select the entire gantt chart and add “subtotals”

To do this, just go to Data Ribbon (or menu) and select “Subtotals”.  
![use-subtotal-to-group-project-plan-activities](https://chandoo.org/img/pm/use-subtotal-to-group-project-plan-activities.png "use-subtotal-to-group-project-plan-activities")  
Once you are inside the subtotals dialog, select “Start” and “End” columns to add subtotals.

In order to get the correct grouping in the gantt chart, we need _**minimum of start**_ and _**maximum of end**_ in each group. But this is not possible with subtotals dialog. So we just select “minimum” as the subtotal type.  
![Edit Subtotal Settings for Project Plan](https://chandoo.org/img/pm/excel-subtotal-dialog.png "Edit Subtotal Settings for Project Plan")  
Once you press OK, Excel will insert new rows and add [SUBTOTAL formulas](http://chandoo.org/wp/2010/02/09/subtotal-formula-excel/)
 automatically.

### Step 4: Change the SUBTOTAL formulas

Since both Start and End subtotals are pointing to minimum, we need to change the formulas for End so that they show Maximum. _**Just do that by editing the subtotal formulas manually and changing total type to “4” (MAX) for column End.**_

While we are at it, you can also change the labels from “Min of <group>” to “<group>”.

### Step 5: Modify the conditional formatting so that groups are shown in a different color

In the conditional formatting add another condition (like when activity is blank) so that we can show those rows in a different color. \[here are some [tutorials on conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)\
\]

Now our Project Plan for Peanut butter sandwich is ready with groups.  
![Readable Gantt Chart with Project Activities Grouped](https://chandoo.org/img/pm/group-project-activities-gantt-chart.gif "Readable Gantt Chart with Project Activities Grouped")

### Download the Gantt chart template with grouped activities

Download a copy of this example – [Excel 2007](https://img.chandoo.org/pm/grouped-project-plan-template.xlsx)
 | [Excel 2003](https://img.chandoo.org/pm/grouped-project-plan-template.xls)
 \[[mirror](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/projman/grouped-project-plan-template.zip)\
\]

**[Get a copy of my project management template set](http://chandoo.org/pmt/pmt-index-1.html)
** – It has 7 gantt chart templates and 17 other project management templates.

### Do you group tasks in your project plans ?

Grouping activities can be very useful to monitor project progress. In large projects usually there will be hundreds of activities. It can be a nightmare to know which ones are delayed, which ones need attention. By grouping you can present overall picture while allowing drill-down to items that need attention.

**_Do you group tasks in your plans? What is your experience like?_**

### More resources on Project Management using Excel:

I suggest reading my 7 part series on project management using excel. Starting with [Excel Gantt Charts](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 to [Project Dashboards](http://chandoo.org/wp/2009/10/06/project-status-dashboard/)
.

Also, read the [excel conditional formatting tips](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
 article and [primer on excel _subtotal_ formula](http://chandoo.org/wp/2010/02/09/subtotal-formula-excel/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/group-project-activities-in-gantt-charts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/group-project-activities-in-gantt-charts/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [group ungroup](https://chandoo.org/wp/tag/group-ungroup/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [SUBTOTAL](https://chandoo.org/wp/tag/subtotal/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousPreparing Profit / Loss Pivot Reports \[Part 2 of 6\]](https://chandoo.org/wp/profit-loss-reports-excel-2/)

[NextWhat is the most useless feature in Excel? \[poll\]Next](https://chandoo.org/wp/useless-features-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/group-project-activities-in-gantt-charts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/group-project-activities-in-gantt-charts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/group-project-activities-in-gantt-charts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ