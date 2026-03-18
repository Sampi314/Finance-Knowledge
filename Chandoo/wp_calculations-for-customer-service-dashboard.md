# Data and Calculations for our Customer Service Dashboard [Part 2 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculations-for-customer-service-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Data and Calculations for our Customer Service Dashboard \[Part 2 of 4\]
========================================================================

*   Last updated on August 31, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Welcome back_. In part 2 of **Making a Customer Service Dashboard using Excel** let us learn how the data & calculations for the dashboard are setup.  
[Designing Customer Service Dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
  
**Data and Calculations for the Dashboard**  
[Creating the dashboard in Excel](http://chandoo.org/wp/2012/04/18/creating-customer-service-dashboard-in-excel/)
  
[Adding Macros & Final touches](http://chandoo.org/wp/2012/04/26/adding-macros-customer-service-dashboard/)

Data for the Customer Service Dashboard
---------------------------------------

We have seen a snapshot of the data last week. This is how it looks:

![Data for the customer service dashboard](https://img.chandoo.org/dashboards/data-for-customer-service-dashboard.png "Data for the customer service dashboard")

Let us quickly understand what each column contains:

1.  Call ID: Unique identifier for each call.
2.  Date Time: Date and time of the call when we received it.
3.  Product: The product category to which this call belongs.
4.  Region: Region to which the call belongs.
5.  Customer type: Type of the calling customer
6.  Call duration in seconds
7.  Resolved: Whether the reason for call is resolved or not.
8.  Satisfaction rating 1 to 5
9.  Up sell in $s.
10.  Agent who answered the call

Calculations needed for the dashboard
-------------------------------------

All the calculations for this dashboard are kept in a worksheet named **Calcs**.

At last count, there are 4,000+ cells with formulas in this dashboard. If we try to look and understand all of these formulas, we might end at Christmas. So, instead let me list down the key calculations we need to do and the formulas behind them.

### A look at the variables that drive the dashboard

The information & charts displayed on the dashboard depend on these key variables (value that we can change):

1.  **Starting date:** Entered in cell R2 in dashboard, this used to calculate all the summaries, chart data for 4 week period.
2.  **Comparison type:** This is selected from a combo-box in dashboard and tells us what is the option we want to compare – can be one of _products, customer types, regions or agents._
3.  **Comparison Option #1 & #2:** These are 2 things we want to compare. For ex. Agent Vinod with Agent Mary, Desktops with Laptops etc. The actual selections are determined by VBA and placed in 2 named cells – _valOption1, valOption2._
4.  **Chart type:** The type of chart we need to show. Can be one of the , _Calls by day_, _Talk time by day_, _Resolution Rate by day_, _Satisfaction by day_, _Upsell $s by day._

![Variables in Customer Service Dashboard - Excel](https://img.chandoo.org/dashboards/variables-in-our-customer-service-dashboard.png "Variables in Customer Service Dashboard - Excel")

### Important Names that we need

Before taking a look at the actual calculations, we need to understand a few names that I have defined.

*   **cs**: This is the table name which contains all call center data. So if you write cs\[Region\] it refers to all the 14832 region values from which we got the calls.
*   **lstChosen:** This name refers to the column in _**cs**_ that is chosen for comparison. So if you select _**Products**_ in dashboard to compare, this contains cs\[Product\]. If you select Region, this contains `cs[Region]`.
*   **lstCallDates:** Since we are only using date portion of the date & time for calls, I have created a named range, lstCallDates that refers to just Date portion of the date & time. This is done with the formula `=INT(cs[Date Time])`

Apart from these 3, there are 16 more names I have defined to simplify various calculations. You can see all the names further down this post.

### Fetching the data for 4 weeks starting given date:

The first step in our calculations is to fetch only a portion of data for the given 4 week period, starting the date entered in R2 cell in dashboard (dashboard!R2)

I have created a table like this, with 16 columns. First column with date, and next 3 columns for Total calls (all calls, calls for option 1 & option 2 that user picked), next 3 columns for talk time, next 3 columns for resolution rate, next 3 for satisfaction rating and final 3 for up-sell $s, like this:

![Calculations for 4 weeks - Customer Service Dashboard](https://img.chandoo.org/dashboards/calculations-for-4weeks-customer-service-dashboard.png "Calculations for 4 weeks - Customer Service Dashboard")

This table is in the range **_calcs!B10:Q37_**

Filling the dates is easy part. We just load the first cell with dashboard!R2 and then add 1 to next date.

To count total calls received on each date, we can [use SUMPRODUCT](https://chandoo.org/wp/calculations-for-customer-service-dashboard/chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
, like this: `=SUMPRODUCT(--(lstCallDates=given_date))`. Here _given\_date_ refers to the date in first column.

To count total calls received for selected option 1, we use `=SUMPRODUCT((lstCallDates=given_date)*(lstChosen=selection1))`. Here _selection1_ refers to the first selection made by our user.

To count total calls received for selected option 2, we use `=SUMPRODUCT((lstCallDates=given_date)*(lstChosen=selection2))`. Here _selection2_ refers to the second selection made by our user.

We can use similar SUMPRODUCT formulas to calculate total hours of talk time, resolution rate, satisfaction rating & upsell $s.

### Calculating the summaries

Once all the data for 4 week period is fetched, calculating summaries becomes a breeze.

![Summary Section of Customer Service Dashboard - Excel](https://img.chandoo.org/dashboards/customer-service-dashboard-summary-section.png)

To get the total number of calls in a 4 week period we use: `=SUM(C10:C37)` _as column C contains the total calls received by date for each of 28 days._

To calculate the averages (average call duration etc.), we divide the SUM with count of calls.

### Calculating the distribution of satisfaction ratings

This is an interesting part. We are showing how the satisfaction rating is distributed from 1 to 5. To get these numbers, we use a variation of SUMPRODUCT. The calculation output is shown below:

![Distribution of Satisfaction Ratings - Customer Service Dashboard](https://img.chandoo.org/dashboards/satisfaction-rating-distribution.png "Distribution of Satisfaction Ratings - Customer Service Dashboard")

Just use your imagination to figure out how the distribution is calculated.

### All the names used in our Customer Service Dashboard

Now that you have seen all the important formulas, here is a detailed list of names defined to get our dashboard done. While you have already seen some of these names used in various formulas, the rest will be used while creating the charts & adding final touches.

\[if you cannot see the names list below, [click here](https://img.chandoo.org/dashboards/names-in-customer-service-dashboard.html)\
\]

  

|     |     |     |     |
| --- | --- | --- | --- |
| #   | Name | Definition | Purpose |
| 1   | lstAgents | `=Data!$P$6:$P$11` | List of all unique Agents |
| 2   | lstProducts | `=Data!$M$6:$M$11` | List of all unique Products |
| 3   | lstRegions | `=Data!$N$6:$N$10` | List of all unique Regions |
| 4   | lstCtypes | `=Data!$O$6:$O$9` | List of all unique Customer Types |
| 5   | lstCallDates | `=INT(cs[Date Time])` | List of Call Dates – INT makes the time portion zero |
| 6   | lstCharts | `=calcs!$J$2:$J$6` | List of all charts |
| 7   | lstChosen | `=CHOOSE(calcs!$C$4, cs[Product],cs[Region], cs[Customer Type],cs[Agent ID])` | List of values chosen for comparison |
| 8   | lstMaxCallDurations | `='sp1'!$C$4:$C$31` | Maximum call duration by day |
| 9   | lstMinCallDurations | `='sp1'!$B$4:$B$31` | Minimum call duration by day |
| 10  | lstWaysToCompare | `=Data!$M$5:$P$5` | List of ways to compare |
| 11  | lstWaysToCompareV | `=calcs!$L$2:$L$5` | List of ways to compare (vertical) |
| 12  | rngSel1 | `=Dashboard!$B$18:$D$23` | Range of options to compare on left side in dashboard view |
| 13  | rngSel2 | `=Dashboard!$Q$18:$R$23` | Range of options to compare on right side in dashboard view |
| 14  | selChart | `=CHOOSE(valChartToDisplay, calcs!$C$73:$H$81, calcs!$C$84:$H$92, calcs!$C$95:$H$103, calcs!$C$114:$H$122, calcs!$C$125:$H$133)` | Selected Chart – range has the chart – used in picture link / camera tool output |
| 15  | selection1 | `=calcs!$E$4` | Selected option #1 |
| 16  | selection2 | `=calcs!$G$4` | Selected option #2 |
| 17  | valChartToDisplay | `=calcs!$H$4` | Which chart to display |
| 18  | valHelpStatus | `=calcs!$O$3` | Whether to display help or not |
| 19  | valOption1 | `=calcs!$E$3` | Number of selected option #1 |
| 20  | valOption2 | `=calcs!$G$3` | Number of selected option #2 |
| 21  | cs  | `=Data!$B$6:$K$14837` | Table of all call data. Dynamic. |

Download the Final Customer Service Dashboard
---------------------------------------------

[**Click here to download the dashboard workbook**](https://img.chandoo.org/dashboards/customer-service-dashboard-v1.xlsm)
 so that you can examine these formulas and learn better. Change the drop-downs, date values in dashboard sheet to see how the formulas work.

What Next? – Creating the Charts & Sparklines
---------------------------------------------

Now that we have done all the ground work, in the next installment, [learn how to create the charts & sparklines that go in this dashboard](http://chandoo.org/wp/2012/04/18/creating-customer-service-dashboard-in-excel/)
. Also learn how to use Conditional Formatting to create alert icons etc.

How would you design dashboard for this data?
---------------------------------------------

Since all the data for this dashboard is included in the [downloadble workbook](https://img.chandoo.org/dashboards/customer-service-dashboard-v1.xlsm)
, why don’t you go ahead and create your own dashboard? If you want, go ahead and add an extra column or two to capture additional data. Create a dashboard and share with us in comments.

Also tell me how you like the dashboard? _**Please share your opinions using comments.**_

References & Related Learning
-----------------------------

If you are looking for examples, information & tutorials on Excel dashboards, you are at the best. At Chandoo.org we have elaborate examples, tutorials, training programs & templates on Excel dashboards, to make you awesome. Please go thru below to learn more:

*   [Customer Service Dashboard Example](http://chandoo.org/wp/2011/03/22/customer-service-dashboard/)
    
*   [KPI Dashboards in Excel – 6 part tutorial](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [**Excel Dashboards**](http://chandoo.org/wp/excel-dashboards/)
     – Information, Examples, Templates & Tutorials
*   [**Excel SUMPRODUCT Formula**](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
     – what is it, how to use it and detailed examples. ([more on sumproduct](http://chandoo.org/wp/tag/sumproduct/)
    )
*   [**Excel School Dashboards Program**](http://chandoo.org/wp/excel-school/)
     – Learn how to create this and other dashboards in Excel in detail

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/calculations-for-customer-service-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/calculations-for-customer-service-dashboard/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Dashboard Tutorials](https://chandoo.org/wp/tag/kpi-dashboards-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sparklines](https://chandoo.org/wp/tag/sparklines/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousWhat is so special about Go To Special? \[15 tips\]](https://chandoo.org/wp/go-to-special/)

[NextThis week, Speed up your Spreadsheets – Your Action RequiredNext](https://chandoo.org/wp/speedy-spreadsheet-week/)

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
    
    [Reply](https://chandoo.org/wp/calculations-for-customer-service-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/calculations-for-customer-service-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/calculations-for-customer-service-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ