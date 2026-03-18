# Gantt Box Chart - An Alternative to Gantt Chart - Download Excel Template & Online Tutorial

**Source:** https://chandoo.org/wp/gantt-box-chart-tutorial-template

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Gantt Box Chart Tutorial & Template – Download and Try today
============================================================

*   Last updated on July 12, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Gantt Box Chart - An Excel Template & Download](https://chandoo.org/img/pm/gantt-box-chart-template-download.png)

**On Firday, we [proposed a new chart for showing project plans](http://chandoo.org/wp/2010/07/09/gantt-box-chart-proposal/)
.** I chose an ugly name for it and **called it Gantt Box Chart.**

Essentially, a gantt box chart is what you get when a gantt chart and box plot go to a bar, get drunk and decide to make out. It shows the project plan like any other gantt chart, and it shows the distribution of activity end dates, like any other box plot.

You can see an example gantt box chart for a fictional software project above.

Today, we will learn how to create a similar chart in Excel. Get a steaming cup of coffee or whatever keeps you going and follow these simple steps to make a gantt box chart.

\[[Read this post if you want to know what GBC is and how to read it](http://chandoo.org/wp/2010/07/09/gantt-box-chart-proposal/ "Gantt Box Chart - an alternative to traditional gantt chart")\
\]

### 1\. Set up your data:

Just like any other chart in excel, a gantt box chart too requires well structured data. In our case, we need 5 things.

1.  Activity name
2.  Start Date
3.  Best Case End Date
4.  Realistic (or Plan) End Date
5.  Worst Case End Date

Getting all the 3 variations of End dates can be tricky. But if you are managing projects for long, you might already know how to get these dates. Otherwise, here is one approach, proposed by Joel Spolsky, called as [Evidence Based Scheduling](http://www.joelonsoftware.com/items/2007/10/26.html)
 that can help you.

We will also need 3 additional helper columns where we need to calculate some numbers so that our gantt box chart can be constructed without resorting to magic wands. These are,

1.  BC: Number of days between Start Date and Best Case End Date
2.  R: Number of days between Best Case End Date and Realistic Date
3.  W: Number of days between Realistic Date and Worst Case End Date

![Gantt Box Chart - Source Data](https://chandoo.org/img/pm/gantt-box-chart-source-data.png)

### 2\. Create a Stacked Bar Chart

Add a new stacked bar chart. The series to be stacked are,

1.  Best case end date
2.  R
3.  W

Use the “Activity Name” column for category axis labels.

_**Now, our chart should look like:**_

![Gantt Box Chart - Stacked Bar Chart](https://chandoo.org/img/pm/stacked-bar-chart-gantt-box-chart.png)

### 3\. Say your favorite curse word and Reverse the categories

![Reverse Cateogry Axis Values - Excel Gantt Box Chart](https://chandoo.org/img/pm/reverse-category-axis-values-gantt-box-chart.png)Ok, time for a minor annoyance. Excel has magically showed the first activity of project at bottom. So, we need to reverse the category axis values before any further.

Just select the category axis, go to format axis (press CTRL+1) and click the little box that says “order reverse in Categories”.

_**Now, the chart should look like this:**_

![Excel Gantt Box Chart - After reversing category axis values](https://chandoo.org/img/pm/reverse-category-values-gantt-box-chart.png)

### 4\. Add Error Bars to Best Case Series

Now, add error bars to the best case series of the chart so that it looks like a line is drawn connecting best case date to start date of each activity. To do that, follow these steps:

1.  Select “best case end date” series.
2.  Add Error Bars (from format ribbon)
3.  Specify the type of error bar as “Negative only”
4.  Select “Custom” for error bar values
5.  Now, point the error bar values to the helper column “BC”
6.  Format the error bar in such a way that no cap is shown and it is thick.

_**At this point, our gantt box chart should look like this:**_

![Adding Error Bars to Gantt Box Chart](https://chandoo.org/img/pm/add-error-bars-gantt-box-chart.png)

### 5\. Finally, format the chart

Now, our gantt box chart is almost ready. But it is still ugly. We need not hire a Hollywood grade make-up man to beautify this. We just need a few clicks.

1.  Remove legend
2.  Add vertical and horizontal grid lines. Make them subtle.
3.  Change text colors to soothing ones.
4.  Remove fills from all series in stacked bar chart.
5.  Apply borders to 2nd and 3rd series to create a box effect.
6.  [Format the date axis](http://chandoo.org/wp/tag/date-axis/)
    ,
    1.  Adjust the starting point (unfortunately you have to enter the number equivalent of date, like 1-May-2010 as 40299)
    2.  Adjust major unit – I used 14 days, you can try something else depending on overall project length.
    3.  Set the axis number formatting to d-mmm or mmm or myy or something else that works for you.
7.  Add a chart title

**That is all. Our Gantt Box Chart is finally ready.** Now, go figure why your project is not on track and do something about it.

![Final Gantt Box Chart](https://chandoo.org/img/pm/gantt-box-chart-template.png)

### Displaying Completed Activities:

**The easiest way to show completed activities is to change all 3 end dates to the same date:** that of the actual end date. This way, you just see a line when an activity is done and a box when there are variations in end dates.

Of course, you can use another helper column to show a vertical line or a symbol of your choice to denote the end point as well. I leave it to you to figure out that portion.

### Download the Gantt Box Chart Template:

I have prepared an excel template for creating Gantt Box Charts quickly. Go ahead and download the version that you want.

[Excel 2007+ version](https://img.chandoo.org/d/gantt-box-chart-template.xlsx)
 | [Excel 2003 version](https://img.chandoo.org/d/gantt-box-chart-template.xls)

Here is a [mirror](http://cid-b663e096d6c08c74.office.live.com/self.aspx/Public/projman/gantt-box-chart-template.zip)
 with both files as a zip. Go on, be awesome 🙂

### Share your experiences of using Gantt Box Chart:

If you like this chart and implementing it in one of your projects, do tell me how it went. Or just share your thoughts on this implementation and any suggestions. Go ahead and share.

### Templates & Tutorials on Project Management:

*   [Excel Gantt Chart Template](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
    
*   [Project Milestones – Timeline Template](http://chandoo.org/wp/2009/07/09/project-milestones-in-timeline/)
    
*   [Project Status Dashboard Template](http://chandoo.org/wp/2009/10/06/project-status-dashboard/)
    
*   _**More resources on [using Excel for Project Management](http://chandoo.org/wp/project-management/)
    **_

### Project Management Template Set – Get a copy today

I have made a set of 24 templates that take care of various activities in a project right from planning to time sheets to issues to project status reporting thru dashboards. These templates have been bought by more than 500 project managers all over the world and they are saving hours of time every week using these templates.

[![Project Management Templates for Excel](https://cache.chandoo.org/content/project-management-bundle-excel-ad-2.png)](http://chandoo.org/pmt/pmt-index-1.html "Project Management Templates for Excel")

[**Go ahead and a get a copy of my project management templates**](http://chandoo.org/pmt/pmt-index-1.html)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/gantt-box-chart-tutorial-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/gantt-box-chart-tutorial-template/#respond)
    
*   Tagged under [box plots](https://chandoo.org/wp/tag/box-plots/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [date axis](https://chandoo.org/wp/tag/date-axis/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThank you (and thank you Excel), We have a Car!](https://chandoo.org/wp/see-our-new-car/)

[Next4 Alternatives to Export Excel Dashboards as Web PagesNext](https://chandoo.org/wp/export-dashboards-to-web/)

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
    
    [Reply](https://chandoo.org/wp/gantt-box-chart-tutorial-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/gantt-box-chart-tutorial-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/gantt-box-chart-tutorial-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ