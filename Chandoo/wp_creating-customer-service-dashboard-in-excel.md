# Creating Customer Service Dashboard in Excel [Part 3 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/creating-customer-service-dashboard-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Creating Customer Service Dashboard in Excel \[Part 3 of 4\]
============================================================

*   Last updated on August 31, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Welcome back_. In part 3 of **Making a Customer Service Dashboard using Excel** let us learn how to create the charts in our dashboard.

[Designing Customer Service Dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
  
[Data and Calculations for the Dashboard](http://chandoo.org/wp/2012/03/14/calculations-for-customer-service-dashboard/)
  
**Creating the dashboard in Excel**  
[Adding Macros & Final touches](http://chandoo.org/wp/2012/04/26/adding-macros-customer-service-dashboard/)

![Creating Customer Service Dashboard in Excel](https://img.chandoo.org/dashboards/constructing-charts-customer-service-dashboard.png "Creating Customer Service Dashboard in Excel")

Deconstructing the header area – Customer Service Dashboard
-----------------------------------------------------------

I like to keep a header area on all my [dashboards](http://chandoo.org/wp/excel-dashboards/)
. The purpose of header is simple. It shows key summaries and gives the users a sense of what is going on. In our customer service dashboard, the header has various key metrics & their trends, as shown below.

![Charts in Header area - Customer Service Dashboard](https://img.chandoo.org/dashboards/charts-in-header-customer-service-dashboard.png "Charts in Header area - Customer Service Dashboard")

### Constructing the spark-line for trend

![Excel 2010 Sparklines for Dashboard](https://img.chandoo.org/dashboards/excel-2010-sparklines-for-dashboards.png "Excel 2010 Sparklines for Dashboard")The trend of calls for “All” and 2 selected options is shown as sparklines. Sparklines, a new feature introduced in Excel 2010 is very handy and easy to use. All you had to is select the 28 day call volume figures for ALL & 2 selected options and then go to Insert > Sparkline. Select the line sparkline & bingo, the sparklines are added to your workbook. Just cut them and paste them on the dashboard sheet.  
Related: [Learn how to use Excel 2010 Sparklines for dashboards](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/ "What are Excel Sparklines & How to use them? [Excel 2010]")

### Constructing the traffic lights for call resolution

This is done with [Conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
. Another favorite feature. First we need to decide the traffic light conditions. In our case, I have defined below rules.

![Conditional Formatting Traffic Lights for Customer Service Dashboard](https://img.chandoo.org/dashboards/conditional-formatting-rules-traffic-light-csd.png "Conditional Formatting Traffic Lights for Customer Service Dashboard")  
Related: [Using Conditional Formatting Traffic Lights for your dashboards](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/ "Alerts & Traffic Lights in Dashboards - howto?")

### Constructing Satisfaction Rating Chart

Distribution of customer satisfaction ratings is shown as a column chart. This is in fact a sparkline. The data for this is in `Calcs!L42:N46`. This is calculated using beloved [SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 as shown in 2nd installment.

To insert the chart, just select `L42:N46` in Calcs sheet and click on Insert > Sparklines (Column) chart. Move the chart to Dashboard sheet.

Related: [Learn how to use Excel 2010 Sparklines for dashboards](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/ "What are Excel Sparklines & How to use them? [Excel 2010]")

Deconstructing the Dynamic Comparison Chart
-------------------------------------------

The heart of this dashboard is [dynamic chart](http://chandoo.org/wp/tag/dynamic-charts/)
 at bottom. It has a lot going on,

*   You can change the 4 week period for this chart
*   You can select how you want to compare
*   You can select which 2 options you want to compare
*   You can tell what type of chart to show – (call volume, talk time, resolution rate, satisfaction rating & upsell $s)

To explain the dynamism of this chart, I have made a brief video. Please watch it first.  
\[[Watch the video on our Youtube Channel](http://www.youtube.com/watch?v=OiWMp2JzdYA)\
\]

### So how this chart is made?

Even though we see dynamic chart in our dashboard, it is actually a [picture link](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
. This is how the chart works:

1.  From the calculations we have learned in [2nd part](http://chandoo.org/wp/2012/03/14/calculations-for-customer-service-dashboard/ "Data and Calculations for our Customer Service Dashboard [Part 2 of 4]")
    , you know that we constructed 28 day information for all 5 charts.
2.  Select each of these 5 types of info & create charts.
3.  We will end up with 5 charts. Place them neatly in empty cells.
4.  Next, define a named range `selChart`, that returns one of these 5 cell ranges based on which chart user wants.
5.  The definition for selChart is, =CHOOSE(valChartToDisplay,  calcs!$C$73:$H$81, calcs!$C$84:$H$92, calcs!$C$95:$H$103, calcs!$C$114:$H$122, calcs!$C$125:$H$133)

_**I am sure you can figure out the rest of the details.**_ See this illustration to understand how this chart is made.

![Deconstructing the Dynamic chart in Customer Service Dashboard](https://img.chandoo.org/dashboards/deconstructing-dynamic-chart-customer-service-dashboard.png "Deconstructing the Dynamic chart in Customer Service Dashboard")

Download Customer Service Dashboard
-----------------------------------

Excel 2010 version: [**Click here to download the dashboard workbook**](https://img.chandoo.org/dashboards/customer-service-dashboard-v1.xlsm)

Excel 2007 version: [**Click here to download the dashboard workbook**](https://img.chandoo.org/dashboards/customer-service-dashboard-v1-xl2007.xlsm)

Examine the charts to learn better. Change the drop-downs, date values in dashboard sheet to see how the formulas work.

What next? – Adding final touches to the dashboard
--------------------------------------------------

So far, we have learned about the [design of this dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
, [calculations behind it](http://chandoo.org/wp/2012/03/14/calculations-for-customer-service-dashboard/)
 & how the charts are put together.

In the final installment, learn about the remaining pieces of the puzzle – [VBA code, design tricks & future direction of the dashboard](http://chandoo.org/wp/2012/04/26/adding-macros-customer-service-dashboard/)
.

What charts you would put in this dashboard?
--------------------------------------------

I liked the challenge of creating one dynamic chart that can show any data & analysis based on user’s wants. But I am sure there are more interesting ways to display call center data. So go ahead and tell me what charts you would include in a customer service dashboard. Bonus points if you can make the dashboard and share it with us. **Go ahead and share your thoughts using comments.**

Learn more about Dashboards
---------------------------

If you are looking for examples, information & tutorials on Excel dashboards, you are at the best. At Chandoo.org we have elaborate examples, tutorials, training programs & templates on Excel dashboards, to make you awesome. Please go thru below to learn more:

*   [Customer Service Dashboard Example](http://chandoo.org/wp/2011/03/22/customer-service-dashboard/)
    
*   [KPI Dashboards in Excel – 6 part tutorial](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [**Excel Dashboards**](http://chandoo.org/wp/excel-dashboards/)
     – Information, Examples, Templates & Tutorials
*   [**Excel Dynamic Charts**](http://chandoo.org/wp/tag/dynamic-charts/)
     – Examples, tutorials & inspiration
*   [**Excel School Dashboards Program**](http://chandoo.org/wp/excel-school/)
     – Learn how to create this and other dashboards in Excel

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Excel 2010](https://chandoo.org/wp/tag/excel-2010/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [sparklines](https://chandoo.org/wp/tag/sparklines/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousCreating Cash Flow Statement by Indirect Method – II](https://chandoo.org/wp/creating-cash-flow-statement-by-indirect-method-ii/)

[NextFormula Forensic No 019. Converting uneven Text Strings to TimeNext](https://chandoo.org/wp/formula-forensic-no-019/)

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
    
    [Reply](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ