# Making a Dynamic Dashboard in Excel [Part 1 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-dashboard-tutorial-1

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Making a Dynamic Dashboard in Excel \[Part 1 of 4\]
===================================================

*   Last updated on March 21, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

**In this and next 3 posts, we will learn how to make a Dynamic Dashboard using Microsoft Excel.**

At the end of this tutorial, you will learn how easy it is to set up a dynamic dashboard using excel formulas and simple VBA macros.

![Dynamic Dashboard in Excel](https://chandoo.org/img/ed/excel-dynamic-dashboard-final.png "Dynamic Dashboard in Excel")

\[[Click here for large version of the image](http://chandoo.org/img/ed/excel-dynamic-dashboard-final-l.png)\
\]

Introduction:
-------------

The dashboard also demonstrates the standard approach I use in all of my models which is to incorporate three key sheets in addition to the data and analysis tabs.

These are:

*   Home page
*   Inputs (or drivers)
*   Helpsheet

The dynamic dashboard can be downloaded [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.xlsm)
 \[[mirror](http://chandoo.org/img/ed/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
, [ZIP Version](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
\]

The dashboard file works in Excel 2007+. Pls. enable macros to get it work.

The plan is to break this dashboard tutorial down into four parts over the next four weeks. If further topics fall out as a result of discussions either Chandoo or I will pick them up and if necessary post further parts.

*   **Part 1: Introduction & overview**
*   Part 2: [Dynamic Charts in the Dashboard](http://chandoo.org/wp/2010/03/30/excel-dashboard-tutorial-2/)
    
*   Part 3: [VBA behind the Dynamic Dashboard a simple example](http://chandoo.org/wp/2010/04/22/excel-dashboard-tutorial-3/)
    
*   Part 4: [Pulling it all together](http://chandoo.org/wp/2010/05/26/excel-dashboard-tutorial-4/)
    

I would like to take a quick opportunity to give credit for some of the elements of functionality in the model:

*   Boxcharts – Chandoo \[[Link](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/ "Bullet Charts in Excel")\
    \]
*   Scrolling report – Chandoo \[[Link](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/ "Comparison Charts")\
    \]
*   Competitor analysis – Chandoo \[[Link](http://chandoo.org/wp/2009/03/12/comparison-charts-1/ "Comparison Charts in Excel")\
    \]
*   Use of camera tool – Chandoo \[[Link](http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/ "Excel Camera Tool")\
    \]
*   In cell microcharts – Chandoo \[[Link](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/ "Incell Charts in Excel")\
    \]
*   Helpsheet – John Walkenbach

Okay so lets get started with an overview:

### What is the objective of the report?

The Dynamic Dashboard is intended to provide pertinent summary information to aid management decision making. Combining a high level of flexibility within each report and then allowing the user to choose which reports to include and where to position them allows an enormous amount of flexibility over the message to be communicated.

### What does this Dynamic Dashboard do?

**The dynamic dashboard allows the user to select a report from the range of reports within the model and decide where to position it on the page.** The user can select “hide” to hide a report that they do not want to see or select “view” to preview it prior to choosing its position.

*   Clicking on either the hyperlink name or the report image will take you to the report.
*   Each report is highly flexible allowing the user to cut the data in many ways to show management the most pertinent information.

Overview of Dashboard Tabs:
---------------------------

### Home Page

I always include a homepage in my models and often set an auto\_open routine to select this as the first page seen on opening. The Home page is designed to present the contents of the model to the user and provide links to each page for easy navigation.  
![Dynamic Dashboard - Homepage Worksheet](https://chandoo.org/img/ed/dynamic-dashboard-homepage.png)

### The Dynamic Dashboard

This is the main tab for pulling together the dashboard and will be covered in parts 3 and 4.  
![Dynamic Dashboard - Finalized Dashboard](https://chandoo.org/img/ed/excel-dynamic-dashboard-final-th.png)

### Inputs

This is the page for all validation lists and drivers.  
![Input Data for Dashboard Data](https://chandoo.org/img/ed/input-data-dashboard.png)

### Help Sheet

Once again a sheet that is in all of my models. This user form based help sheet provides the user with a quick help function and complements the accompanying user notes. I find it helpful to lay it out in tab order.

![Dashboard Help Sheet Setup](https://chandoo.org/img/ed/dashboard-helpsheet.png)

This is how the Help user form looks once opened. The user can either choose the topic from the dropdown or by clicking next.

![Dashboard Help Sheet Demo](https://chandoo.org/img/ed/dynamic-dashboard-help.gif)

### Chart 1 and 2 : Flexible pie charts

Dynamic pie charts with the option to select the KPI, period and product/salesperson to be analyzed. These are covered in part 2.  
![Charts 1 & 2 - Dynamic Dashboard](https://chandoo.org/img/ed/charts-1-2-dynamic-dashboard.png)

### Chart 3 & 4: Flexible line charts

Dynamic line charts with the option to select the KPI, period and product/salesperson to be analyzed. These are also covered in part 2.  
![Charts 3 & 4 - Dynamic Dashboard](https://chandoo.org/img/ed/charts-3-4-dynamic-dashboard.png)

### Chart 5: Box Chart

[Details on how to create these box charts.](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/ "Bullet Charts in Excel")
  
![Chart 5 - Bullet Chart - Dynamic Dashboard](https://chandoo.org/img/ed/chart-5-bullet-chart-dynamic-dashboard.png)

### Chart 6: Scrolling Report of KPIs

Chandoo’s blog on [how to create this scrolling report can be found here](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/ "Comparison Charts")
. Micro charts which is of my favorite blogs from Chandoo are covered [here](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/ "Incell Charts in Excel")
.

![Chart 6 - Scrollable KPI List - Dynamic Dashboard](https://chandoo.org/img/ed/scrollable-list-kpis-dynamic-dashboard.png)

### Chart 7: Scrolling Comparison Chart

Details on [how to create this scrolling chart](http://chandoo.org/wp/2009/03/12/comparison-charts-1/ "Comparison Charts in Excel")
.  
![Chart 7 - Scrollable Comparison Chart - Dynamic Dashboard](https://chandoo.org/img/ed/comparison-chart-dynamic-dashboard.png)

### Chart 8 : Executive Summary

A simple executive summary. Please see Chandoo’s article on a [twitter board](http://chandoo.org/wp/2009/05/07/tweetboard/)
 for an alternative view.  
![Chart 8 - Executive Summary - Dynamic Dashboard](https://chandoo.org/img/ed/exec-summary-dynamic-dashboard.png)

**So that was an overview of the model and its main tabs.**

### What Next?

Next week we will look at  [Part 2 of this series and learn how to construct dynamic charts](http://chandoo.org/wp/2010/03/30/excel-dashboard-tutorial-2/)
.

### Download the complete dashboard

Go ahead and download the dashboard excel file. The dynamic dashboard can be downloaded [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.xlsm)
 \[[mirror](https://chandoo.org/img/ed/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
, [ZIP Version](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
\]

It works on Excel 2007 and above. You need to enable macros and links to make it work.

### Added by PHD:

Myles has taken various important concepts like Microcharts, form controls, macros, camera snapshot, formulas etc and combined all these to create a truly outstanding dashboard. I am truly honored to feature his ideas and implementation here on Chandoo.org. I have learned several valuable tricks while exploring his dashboard. I am sure you would too.

**If you like this tutorial please say thanks to Myles.**

### Related Material & Resources

*   [Excel Dashboards – Tutorials & Templates Section of PHD](http://chandoo.org/wp/management-dashboards-excel/)
    
*   [6 Part Tutorial on Making KPI Dashboards in Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [Recommended Product: Jorge Camoes’ Dashboard Training Kit](https://www.e-junkie.com/ecom/gb.php?ii=226797&c=ib&aff=49044&cl=8496)
    

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.  
[![Are you ready for Excel Automation? - Get Free Trial of ApeSoft](https://cache.chandoo.org/content/das/ApeSoftChandooFreeTrialm1.png)](http://apesoft.us/excel-automation-chandoo "Are you ready for Excel Automation? - Get Free Trial of ApeSoft")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [35 Comments](https://chandoo.org/wp/excel-dashboard-tutorial-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-dashboard-tutorial-1/#respond)
    
*   Tagged under [bullet charts](https://chandoo.org/wp/tag/bullet-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Links – Back to India Edition](https://chandoo.org/wp/excel-links-15mar/)

[NextSuper Timesaver Tip – Add “Select Objects” to Quick Access ToolbarNext](https://chandoo.org/wp/select-objects-tool-in-qat/)

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
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-1/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-1/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-1/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ