# Employee Turnover Dashboard - Power BI for HR » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/employee-turnover-dashboard-powerbi

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

Employee Turnover Dashboard – Power BI for HR
=============================================

*   Last updated on March 8, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Employee Turnover / Attrition Dashboard – Power BI**

Jack – The recruiting hamster
-----------------------------

Meet Jack. He is a recruiter at East Coasters Inc. In the first quarter of 2019, so far 17 people in Engineering, 12 people in R&D, 9 people in Customer Care and 7 people in Finance have left East Coasters. Jack could only manage to replace 12 of them. What should he do?

_Buy Panadol, lots of it._

Jokes aside, people in HR know very well that the recruitment hamster wheel must go on. But you know what makes the HR manager’s life a little better? **If you know employee turonver looks, you can manage it better.**

So on that note, let’s see how you can **create an interactive, fun and useful Employee Turonver dashboard using Power BI**.

Quick demo of the HR Turnover dashboard
---------------------------------------

Before learning how to create this, just take a look at this beauty.

![](https://chandoo.org/wp/wp-content/uploads/2019/03/turnover-dashboard-powerbi-demo.gif)

Start with data
---------------

Typical staff recruitment and turnover data looks like this:

*   Employee details (name, designation etc.)
*   Where they work (department, branch etc.)
*   Date of join
*   Date of leaving
*   Reason for leaving

Let’s assume this is how our data looks like. We have two sets of it. One for recruitment and another for leaving.

*   [![](https://chandoo.org/wp/wp-content/uploads/2019/03/recruitment-data.png)](https://chandoo.org/wp/wp-content/uploads/2019/03/recruitment-data.png)
    
    Recruitment Data
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2019/03/leaving-data.png)](https://chandoo.org/wp/wp-content/uploads/2019/03/leaving-data.png)
    
    Leaving Data
    

Download sample data
--------------------

[Click to download sample data for this exercise](https://chandoo.org/wp/wp-content/uploads/2019/03/turnover-data.xlsx)
[Download](https://chandoo.org/wp/wp-content/uploads/2019/03/turnover-data.xlsx)

Load data and transform thru Power Query
----------------------------------------

Now that we have our data, let’s load it in to Power BI workbook. Open Power BI, click on Get data and point to your employee data set (in this case, the data came from an Excel file, for you this can be a SQL query, Oracle database or angry data dump from a bored data analyst in IT)

While at Power Query, it is a good idea to split the data in to dimension and fact tables. The exact set of tables depend on your input data. In our case, I have created below tables.

*   Fact Tables
    *   Recruitments data – called staff
    *   Leavers data – called leavers
*   Dimension Tables
    *   Branches – dBranch
    *   Departments – dDept
    *   Designations – dTitle
    *   Gender – dGender
    *   Calendar (generated thru Power Query List.Numbers function) – calendar

The process of creating these tables is fairly straight forward. If you are not sure how to make them from your source tables, watch the video at the end of this article.

Load data and Model it in Power BI
----------------------------------

At the end of this process, load data to Power BI and link up tables. Here is my data model. Dimension tables are in the middle.

![Data model - Employee turnover dashboard - Power BI](https://chandoo.org/wp/wp-content/uploads/2019/03/employee-data-model.png)

Create some measures
--------------------

Now that our data model is ready, let’s dax. I meant Data Analysis eXpressions, you silly. You can measure and analyze recruitment and leaver data in any number of ways. Since Power BI allows us to interactively explore and visualize data, I find that even simple measures can deliver powerful results (as you will see in the dashboard).

Here are a few measures you can create:  
(Refer to data model diagram above if you are not sure what a field refers to)

    Leaver Count = COUNTROWS(leavers)
    Joinee Count = COUNTROWS(staff)
    Tunrover % = DIVIDE([Leaver Count], [Joinee Count], blank())
    
    Total Staff to date = 
    CALCULATE(
    	[Joinee Count]-[Leaver Count],
    	FILTER(
    		ALLSELECTED('calendar'[Date]),
    		ISONORAFTER('calendar'[Date], MAX('calendar'[Date]), DESC)
    	)
    )

While the above 4 measures are simple, the next one is a bit tricky. So if you dax with two left hands, then ignore the next one. You can still create powerful reporting.

The next measure tells us about top 2 branches and their contribution to overall turnover.

    Top 2 branch leavers total = 
        var t2 = topn(2,dBranch,[Leaver Count],DESC)
        var t2_names = CONCATENATEX(t2, dBranch[Branch], ", ", [Leaver Count], DESC)
    return
        "Top 2 branches ("& t2_names &") account for " & format(divide(SUMX(t2, [Leaver Count]), CALCULATE([Leaver Count], all(dBranch)),0),"0%") & " of leavers"

Let’s get graphic
-----------------

So our data is ready, measures are clicking. Time to place them in some visuals to see whats going on with our turnover. There are many options when it comes visualizing this kind of data. Just play with Power BI and keep what you like.

Here are a few options.

### New Joinees vs. Leavers over time

![](https://chandoo.org/wp/wp-content/uploads/2019/03/visual-and-title-with-textbox.png)

Simple line chart with a text box for title. Uses \[Joinee Count\] and \[Leaver Count\] measures with Calendar\[date\] on horizontal axis.

### Leavers by branch and gender

![](https://chandoo.org/wp/wp-content/uploads/2019/03/attrition-by-region-gender-with-special-card.png)

This next one is stacked bar chart with gender, branch and \[leaver count\]. We can then overlay a card visual with \[top 2 branch leavers total\] measure to see more info about top 2 branches.

### Or a few cards with statistics

You can add multi-row cards to display statistics. When mixed with visual filters on relative date, you can get same measures in different context. See below for some inspiration.

![](https://chandoo.org/wp/wp-content/uploads/2019/03/same-card-different-filters.png)

![](https://chandoo.org/wp/wp-content/uploads/2019/03/relative-date-filtering.png)

Relative date filtering for the cards.

### See top 10 designations of leavers

![](https://chandoo.org/wp/wp-content/uploads/2019/03/top10-titles-with-turnover-table.png)

![](https://chandoo.org/wp/wp-content/uploads/2019/03/topn-filter.png)

You can never go wrong with a black dress or good old fashioned table. A simple table of turnover % by job title (designation) will always look flash. But what if you have 100s of jobs. Simple, **apply Top N filter** and you can look at things that matter most.

Complete Turnover Dashboard
---------------------------

click to enlarge

[![Employee turnover  / attrition dashboard](https://chandoo.org/wp/wp-content/uploads/2019/03/turnover-dashboard-powerbi.png)](https://chandoo.org/wp/wp-content/uploads/2019/03/turnover-dashboard-powerbi.png)

Download Power BI workbook
--------------------------

**[Click here to download the Power BI workbook](https://files.chandoo.org/pbix/HR%20turnover%20report.pbix)
**.

Video tutorial – Employee Attrition Dashboard
---------------------------------------------

If you are still not sure how everything works, check out this simple tutorial. Make sure you follow along in Power BI for best results. The video explains how to transform data in Power Query, how to generate custom calendar, how to create data model, measure development, visual selection and formatting. It is quite in-depth and yet not too long. Check it out below. Or [watch it on my YouTube channel](https://www.youtube.com/watch?v=D7Uh10nBMfo)
.

Are you HR + Power BI?
----------------------

Do you work in HR and use Power BI? How do you measure and analyze turnover? Please share your thoughts and tips in the comments box. Even if you don’t work in HR, I am sure you find this example very useful for Power BI, Power Query and dashboard development.

More Power BI examples
----------------------

If you have just started with Power BI and want to learn how to use the tech, check out below resources.

*   [What is Power BI, Power Query and Power Pivot?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)
    
*   [Nest egg (retirement) calculator using Power BI](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/)
    
*   [Star Wars + Power BI – The force is strong with this one](https://chandoo.org/wp/force-with-power-bi/)
    
*   [Intro to Power BI + full case study](https://chandoo.org/wp/introduction-to-power-bi/)
    

![](https://chandoo.org/wp/wp-content/uploads/2018/05/power-query-power-pivot-power-bi.png)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/#respond)
    
*   Tagged under [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [HR](https://chandoo.org/wp/tag/hr/)
    , [measures](https://chandoo.org/wp/tag/measures/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousQuickly Change Formulas Using Find / Replace](https://chandoo.org/wp/spreadsheet-formulas-edit/)

[NextPower BI Webinar, Amsterdam & Australia tours \[update time\]Next](https://chandoo.org/wp/power-bi-webinar-and-updates-march-2019/)

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
    
    [Reply](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ