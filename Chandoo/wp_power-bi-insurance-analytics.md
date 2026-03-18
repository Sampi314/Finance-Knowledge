# How to Create a Power BI Dashboard for Insurance Analytics (With Examples) »

**Source:** https://chandoo.org/wp/power-bi-insurance-analytics

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    

How to Create a Power BI Dashboard for Insurance Analytics (With Examples)
==========================================================================

*   Last updated on April 6, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

1\. **Introduction**
--------------------

![insurance analytics dashboard with Power BI](https://chandoo.org/wp/wp-content/uploads/2025/04/screenshot-0038.png)

Insurance is a perfect industry for data analysis. There is plenty of data – right from lead generation to to underwriting to policy issuance to administration to claims processing. With a careful and well thought data strategy insurance companies can become profitable.

Power BI makes data analysis in insurance space a breeze. Whether you’re tracking profitability, claim patterns, or policy lapse rates, Power BI let’s us understand the insights and patterns buried in the data easily.

In this article, we’ll walk through how to design an impactful **insurance analytics dashboard in Power BI**. Let me share essential **KPIs**, **DAX formula patterns** behind key metrics, and break down a real-world design example to help you build dashboards that drive business value.

* * *

2\. **Why Insurance Needs Data Dashboards**
-------------------------------------------

![](https://chandoo.org/wp/wp-content/uploads/2025/04/SNAG-0120.png)

> > … it is estimated that 2.5 quintillion bytes of data are generated every day, with factors such as claims processing, customer interactions, and regulatory compliance contributing to this staggering figure.
> > 
> > [data-axle.com](https://www.data-axle.com/resources/blog/insurance-industry-data-questions-answered)

Insurance is one of the most data-rich industries — every customer, policy, claim, and vehicle interaction generates data. The problem is, this data is often scattered across multiple systems, spreadsheets and silos.

Dashboards can consolidate and visualize this information in a single, interactive format. This enables decision makers & managers to:

*   **Monitor performance** across policy types, agents and regions.
*   **Track key metrics** like claim ratios, underwriting profit, and policy lapses
*   **Spot trends and outliers** (e.g., rising claims in a specific region or vehicle type)
*   **Assess risk and profitability** at both macro and micro levels

With Power BI, we can build dashboards that update automatically, allow role-based access (e.g., for underwriters, actuaries, or claims assessors), and integrate with internal data systems (databases, underwriting tables, claims processing systems, call center data etc.)

* * *

3\. **Why Power BI Is Perfect for Insurance Analytics**
-------------------------------------------------------

If your organization is running Microsoft stack for data & internal systems (SQL server, Azure, SharePoint, MS Office & Windows), then Power BI becomes a natural ally in the data analytics journey. Here are some of its key strengths.

### Seamless Data Integration

Connects to Excel files, SQL databases, policy admin systems, and even cloud platforms like Azure and AWS. You can also merge claims, premiums, and customer data from disparate systems.

### Advanced Analytics with DAX

Want to calculate claims to premium ratio? Understand what percentage of policies are lapsing from a specific region? We can use DAX to quickly and elegantly analyze data even when you have billions of records.

### Interactive Visuals for All Roles

Whether you are an underwriter or claims assessor or policy administrator, you can use Power BI visuals to interact and understand data better. Power BI features like slicers, drillthrough and visual interactions coupled with RLS (Row Level Security) enables us to present right data to right people at correct time.

### Security and Scalability

Row-Level Security (RLS) ensures the right people see only the data relevant to them. We can even auto-refresh data when there is new information. Managers & users of the report can subscribe and monitor KPIs with built-in alert system. What more, Power BI integrates naturally with teams & MS Power Point for easy sharing and comms of your data.

* * *

4\. **Example Insurance Analytics Dashboard with Power BI**
-----------------------------------------------------------

Here is an excellent Insurance BI dashboard example. I created this for a recent training session and everyone loved it. You can see the “interactive” report below. Click on the slicers or select any item to see values updated. You can also [check the dashboard online on Power BI service here](https://app.powerbi.com/view?r=eyJrIjoiMmM1YTM0ZTktNGZmNC00NzgyLTliMWUtNWM3Y2NjZmFkMjZmIiwidCI6IjUzNTA4ZDUyLWQxYjAtNDliMC1iNGJhLTM1MzNjMTI0OWEwMSJ9)
.

* * *

5\. **How to design Insurance data analytics dashboard?**
---------------------------------------------------------

Here is how we can design a successful dashboard with BI tools like Power BI for insurance industry. The 7 key steps of the process are,

1.  Identifying KPIs that matter
2.  Designing the mock-up report
3.  Data preparation
4.  Report building
5.  Testing the report
6.  Deployment
7.  Improving when your business (needs) change

I have illustrated the first 4 steps below.

![](https://chandoo.org/wp/wp-content/uploads/2025/04/insurance-dashboard-design-process.png)

* * *

6\. **Examples of Insurance KPIs to Track (with Context)**
----------------------------------------------------------

Identifying KPIs (Key Performance Indicators) is the first step of getting your insurance dashboard right. Here are some of the most useful and relevant KPIs for insurance data analysis.

### Policy Metrics

*   **Policies Opened:** Total count of active or new policies issued during the selected period.
*   **Policy Lapse Rate:** Shows the percentage of policies not renewed — a key retention metric.
*   **Retention Rate:** Indicates customer loyalty; higher is better.
*   **Sum Insured Booked:** Total exposure covered — important for risk profiling.

### Premium Metrics

*   **Total Premium Earned:** Gross income from policies.
*   **Average Premium:** Helps identify shifts in customer spending or policy value.
*   **Net Written Premium:** Premiums retained after reinsurance costs — useful for profit calculations.
*   **Premium Growth Rate:** Year-over-year growth helps track sales or pricing strategy effectiveness.

### Claim Metrics

*   **Total Claims Paid:** Overall amount paid across claims.
*   **Average Claim:** Indicates claim severity and possible fraud or cost control issues.
*   **Claim Frequency:** Claims per 1,000 policies — a good indicator of risk per product.
*   **Loss Ratio:** Claims Paid ÷ Premium Earned. A core metric for insurer profitability.

### Underwriting & Risk Metrics

*   **Underwriting Profit:** Premiums – Claims – Expenses. Direct profit from insurance operations.
*   **Combined Ratio:** A benchmark profitability KPI; values <100% are desirable.
*   **High-Risk Policy Ratio:** Helps isolate segments or demographics prone to higher claims.

### Segment & Demographic Insights

*   **Profitable Segments (Heatmap):** Product or usage segments ranked by profitability across years.
*   **Top Claiming Demographics (e.g., by gender, region, vehicle type):** Useful for targeted risk mitigation.
*   **Vehicle Make/Model Trends:** Can highlight which brands are associated with higher risk or profitability.

Together, these KPIs give decision-makers a 360° view of business health, risk exposure, and customer behavior. Each one can be calculated with a combination of base data and DAX formulas, which we’ll cover in detail in the next section.

* * *

7\. Example DAX measures & formula patterns
-------------------------------------------

The exact syntax of DAX measures depends on your insurance data & how you modeled it in Power BI. For the sake of our discussion, assume you have policy data in below format. You can download sample Policy data from [my github page.](ttps://github.com/chandoo-org/Power-BI/tree/main/insurance_dashboard)
 This data is [sourced from Edossa Terefe on Mendeley Data](https://data.mendeley.com/datasets/34nfrk36dt/1)
.

![sample insurance policy data - for insurance analytics dashboard with Power BI\
](https://chandoo.org/wp/wp-content/uploads/2025/04/SNAG-0121.png)

### DAX Measures for Policy Analytics:

Here is the sample code for DAX measures using the above insurance data.

    // Total Policies
    Policy Opened:=COUNTROWS(policies)
    
    // ? Total Premium collected
    Total Premium:=SUM(policies[PREMIUM])
    
    // Average premium
    Avg. Premium:=DIVIDE([Total Premium], [Policies Opened])
    
    // ? Total Claims paid out
    Total Claims Paid:=SUM(policies[CLAIM_PAID])
    
    // ? Ratio of Premiums to Claims - tells us how profitable we are, >100% is good
    Premium to Claims Ratio:=DIVIDE([Total Premium], [Total Claims Paid])
    
    // Claim count
    Claim Count:=CALCULATE(policies[Policies Opened], policies[CLAIM_PAID]>0)
    
    // Average claim paid
    Avg. Claim:=DIVIDE([Total Claims Paid], [Policies Opened])
    
    // Simple underwriting profit, as we don't have any other expense columns.
    U/W Profit:=[Total Premium] - [Total Claims Paid]

* * *

8\. **Design Best Practices for a successful insurance dashboard**
------------------------------------------------------------------

![extended process for designing a successful insurance analytics dashboard with Power BI](https://chandoo.org/wp/wp-content/uploads/2025/04/insurance-dashboard-design-process-extended.png)

The dashboard design process is a living process. Here is the extended process with all the 7 steps. If you ignore one or few of these steps, your analytics project will fail. Here are some of the key things to keep in mind, when it comes to the “Design”.

*   **Color:** Use clear, simple colors to indicate various Key metrics & alerts. (e.g. green = profitable, red = unprofitable).
*   **More info on demand:** We can use Power BI features like [tooltips](https://chandoo.org/wp/how-to-create-tooltips-in-power-bi/)
     to show relevant, useful information on demand. Here is a quick demo.

![Power BI Insurance Report - Tooltip demo](https://chandoo.org/wp/wp-content/uploads/2025/04/2025-04-02_12-13-00.gif)

*   **Filter to what matters:** Use slicers, visual & page filters to narrow down data to important and useful factors.
*   **Use simple charts:** Insurance is a data rich space. So don’t clutter your reports with too many and too complex visuals. Stick to basic chart types like bars, columns, lines, cards & tables for best results. [Here is a guide on how to select Power BI visuals](https://chandoo.org/wp/powerbi-when-to-use-which-chart/)
    .

* * *

9\. Going Live: Sharing your Report
-----------------------------------

Congratulations on building your insurance report and thoroughly testing it (you did test everything right?). The next step is to go live with your report and share it with the users. Here is a go-live ? check list:

**Row Level Security:** Check right people can see the right data. Use the “view report as” feature in Power BI to test this. You can also try this in Power BI service.

![](https://chandoo.org/wp/wp-content/uploads/2025/04/Snag_905f3688.png)

**Refresh Process:** See if your refresh process runs smoothly. If needed, set up any data flows or Power Automate based automations to synchronize various systems and their data update frequencies.

**Screen vs. Mobile view:** Check how the report renders on mobile screens and whether important information can be accessed on smaller devices (if your users rely on this).

**Analyze in Excel:** Power BI offers helpful “analyze in Excel” option. If your users (power users…?) prefer this option over Power BI reports, educate them how to access the semantic model in Excel.

* * *

10\. **Performance Tips & Troubleshooting**
-------------------------------------------

If for whatever reason your Power BI insurance report is loading slow or unresponsive, try below strategies.

*   **Optimize your data model:** Power BI prefers and works faster with star-schema models over large flat tables or network models (typically found in transactional production databases). Design dimension and fact tables and set up proper star schema to optimize query and DAX performance.
*   **Pre-aggregation:** You can also use pre-aggregation of your large data tables. You can do this at data layer or with in Power BI (right click on table and use Manage Aggregations).
*   **Minimize unwanted interactions:** Interactions or cross-filtering can take a lot of time when you have lots of data and too many visuals. Customize interaction behaviors to reduce this unwanted effect and speed up your report.
*   **Measure what is slowing things down:** Using the Power BI’s performance analyzer tool, benchmark each page and interaction and see what is taking too much time. Then improve your DAX or visual set up to attack the problem.

* * *

11\. **Bonus: What’s Next? AI + Insurance Dashboards**
------------------------------------------------------

Of course, no report or data analytics project is complete without AI integration. We can use CoPilot or other native AI features of Power BI to enhance our insurance dashboards. Check out below features to add a layer of AI insights to your analytics reports.

*   **Key Influencers Visual:** Use the Key Influencer visual to understand how one KPI is impacted by a set of dimensions (for example underwriting profit and how it is impacted by various vehicle makes & driver sex).
*   **Smart Narratives:** You can generate narrative statements to explain the data using “smart narrative” feature of Power BI.
*   **CoPilot for creating measures:** Use Copilot in Power BI to create necessary DAX measures from your insurance data model.
*   **CoPilot for insights:** We can also use CoPilot to find insights, abnormalities and patterns in the data or even create complete reports.

* * *

12\. **Conclusion**
-------------------

As you can see, Power BI is a great choice for analyzing and exploring insurance data. If you need help with Power BI based Insurance data analytics reach out to me. I am happy to offer our consulting services for your next analytics project.

**[Get in touch here](https://chandoo.org/wp/contact/)
**.

* * *

Suggested Resources:
--------------------

Please check out below pages for more information on Power BI:

*   [Getting Started with Power BI](https://chandoo.org/wp/powerbi-introduction/)
    
*   [Insurance Dashboard with Power BI – Video](https://youtube.com/live/TazNFzgWtgA?feature=share)
    
*   [How to use Power Query to prepare & clean your data](https://chandoo.org/wp/power-query-tutorial/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/power-bi-insurance-analytics/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-bi-insurance-analytics/#respond)
    
*   Tagged under [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    

[PrevPreviousEasily Convert JSON to Excel – Step by Step Tutorial](https://chandoo.org/wp/json-to-excel-howto/)

[NextHow to create SVG DAX Measures in Power BI (Easy, step-by-step Tutorial with Sample File)Next](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/)

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
    
    [Reply](https://chandoo.org/wp/power-bi-insurance-analytics/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/power-bi-insurance-analytics/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/power-bi-insurance-analytics/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ