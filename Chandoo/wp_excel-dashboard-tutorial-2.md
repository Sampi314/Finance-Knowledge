# Making a Dynamic Dashboard in Excel [Part 2 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-dashboard-tutorial-2

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Making a Dynamic Dashboard in Excel \[Part 2 of 4\]
===================================================

*   Last updated on May 26, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

*   Part 1: [Introduction & overview](http://chandoo.org/wp/2010/03/16/excel-dashboard-tutorial-1/)
    
*   **Part 2: Dynamic Charts**
*   Part 3: [VBA behind the Dynamic Dashboard a simple example](http://chandoo.org/wp/2010/04/22/excel-dashboard-tutorial-3/)
    
*   Part 4: [Pulling it all together](http://chandoo.org/wp/2010/05/26/excel-dashboard-tutorial-4/)
    

[Part 1 of dynamic dashboard tutorial](http://chandoo.org/wp/2010/03/16/excel-dashboard-tutorial-1/)
 introduced the purpose and general functionality of the model. In this post we are going to look at the first 4 charts and see how they work.

Chart 1 and Chart 2 : Flexible pie charts
-----------------------------------------

These are Dynamic pie charts with the option to select the KPI, period and product/salesperson to be analyzed. As both pie charts use the same functionality I will focus on the chart in CH1.

![Dynamic Sales Chart - Excel Dashboard - Demo](https://chandoo.org/img/ed/dynamic-sales-chart.gif)

The key to the flexibility of these otherwise simple pie charts is taking a little time to set up the chart source data.

### 1) Selection criteria

We want to be able to select data by product group and month and be able to choose the key performance indicator to report. We also want to be able to report on all product groups and for all periods.

To ensure that only valid criteria are selected, each selection is driven from a data validation list driven from a named range:

![data validation in dynamic excel dashboard - example](https://chandoo.org/img/ed/data-validation-in-dashboard.png)

### 2) The formula

The main formula being used is the SUMIFS(Sum range, Criteria range, criteria,…). This was a new formula in 2007 and provides a simpler solution to [the SUMPRODUCT() formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
.

_**So the formula in cell D24 in CH1 is:**_

`=SUMIFS(INDIRECT($C$21),Sales_Per,B24,Product,$C$19,Period,$C$20)`

Right, lets break it down for you:

#### Sum range

To create flexibility around the values returned I have used the INDIRECT formula to reference a named range. The named ranges are Count, Total\_sales KPI\_1 and Total\_GP. I have then referenced these three named ranges within the data validation list.

#### Criteria range 1 and criteria 1

This matches the sales person in B24 against the list of sales people (named range Sales\_Per) in the data tab.

#### Criteria range 2 and criteria 2

This matches the product in C19 against the list of products (named range Product) in the data tab.

#### Criteria range 3 and criteria 3

This matches the period in C20 against the list of periods (named range Period) in the data tab.

The result of bringing all of this together is that the value returned is:

*   The value range as defined in C21
*   The sales person as defined in B24
*   The product as defined in C19
*   The period as defined in C20

### 3) The final step – Dealing with “All”

The final element to enable the fully flexibility is to allow “all” to be selected for product and period. This gives you four options:

*   Product and period specified
*   Product specified, all periods
*   All products, period specified
*   All products and all periods

To manage this I have created a column for each option with a variation of the formula defined above. Finally I used a column as source data for the chart which pulls though the relevant information based on the selections made. They look like this:

![Dynamic Sales Chart - Calculations](https://chandoo.org/img/ed/dynamic-sales-chart-calculations.png)

I leave the interpretation of the actual formulas to you.

CH3 and CH4 Flexible line charts
--------------------------------

![Charts 3 & 4 - Dynamic Dashboard](https://chandoo.org/img/ed/charts-3-4-dynamic-dashboard.png)

These are dynamic line charts with the option to select the KPI, period and product/salesperson to be analyzed. As both line charts use the same functionality I will focus on the chart in CH3.

### 1) Selection criteria

This uses the same functionality as used in the pie chart illustration.

### 2) The formula

Once again the basic formula is the same as in the pie chart illustration.

The additional step is to allow flexibility around the period to display for the trend. This is achieved by selecting a period from a validation list. The following periods are then looked up from the validation list using HLOOKUP and MATCH. First take a look at how it works:

![dynamic line chart demo](https://chandoo.org/img/ed/dynamic-line-chart-example.gif)

Now the formula is:  
`=HLOOKUP("YTD",Period_List,MATCH($C$23,Period_List2,0)+2,FALSE)`

#### How this formula works?

C23 contains the first cell from which starting month can be changed. Based on that, we need to increment the month value for subsequent columns by 1, 2 and 3. The above is the formula for first such month. If you look at the downloaded file carefully, you will know why this works. 🙂

### 3) The final step – Dealing with “All”

As with the pie charts illustration the final step is to enable the user to select all. As the functionality as very similar to that used in the pie charts I will allow you to work through how it works.

Creating other Dynamic Charts in the Dashboard:
-----------------------------------------------

Links for how to create the other charts in this report can be found below:

*   Boxcharts \[[Link](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/ "Bullet Charts in Excel")\
    \]
*   Scrolling report \[[Link](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/ "Comparison Charts")\
    \]
*   Competitor analysis \[[Link](http://chandoo.org/wp/2009/03/12/comparison-charts-1/ "Comparison Charts in Excel")\
    \]
*   Use of camera tool \[[Link](http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/ "Excel Camera Tool")\
    \]
*   In cell microcharts \[[Link](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/ "Incell Charts in Excel")\
    \]

### What Next?

We now know how to create the charts for the Dynamic Dashboard. Next week we will look at [Part 3 VBA behind the Dynamic Dashboard, by studying a simple example](http://chandoo.org/wp/2010/04/22/excel-dashboard-tutorial-3/)
.

### Download the complete dashboard

Go ahead and download the dashboard excel file. The dynamic dashboard can be downloaded [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.xlsm)
 \[[mirror](http://chandoo.org/img/ed/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
, [ZIP Version](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
\]

It works on Excel 2007 and above. You need to enable macros and links to make it work.

### Added by PHD:

Myles has taken various important concepts like Microcharts, form controls, macros, camera snapshot, formulas etc and combined all these to create a truly outstanding dashboard. I am honored to feature his ideas and implementation here on PHD. I have learned several valuable tricks while exploring his dashboard. I am sure you would too.

**If you like this tutorial please say thanks to Myles.**

### Related Material & Resources

*   [Excel Dynamic Charts – Tutorials, Examples and Demos](http://chandoo.org/wp/tag/dynamic-charts)
    
*   [Excel Dashboards – Tutorials & Templates Section of PHD](http://chandoo.org/wp/management-dashboards-excel/)
    
*   [6 Part Tutorial on Making KPI Dashboards in Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/excel-dashboard-tutorial-2/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-dashboard-tutorial-2/#respond)
    
*   Tagged under [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [hlookup](https://chandoo.org/wp/tag/hlookup/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [pie charts](https://chandoo.org/wp/tag/pie-charts/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to Check whether a Table is Filtered or not using Formulas](https://chandoo.org/wp/data-filter-formula-test/)

[Next101 Excel Secrets – Recommended E-BookNext](https://chandoo.org/wp/101-excel-secrets-recommended-e-book/)

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
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-2/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-2/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-2/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ