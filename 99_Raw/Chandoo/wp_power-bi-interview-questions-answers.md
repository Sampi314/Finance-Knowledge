# Top 10 Power BI Interview Questions (based on what I usually ask)

**Source:** https://chandoo.org/wp/power-bi-interview-questions-answers

---

*   [Interview Questions](https://chandoo.org/wp/category/interview-questions/)
    , [Power BI](https://chandoo.org/wp/category/power-bi/)
    

Top 10 Power BI Interview Questions & Answers
=============================================

*   Last updated on October 30, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently, I interviewed a few people for Power BI roles and here are some questions I asked in the initial rounds to assess their skill level. I’ve included sample answers below so you know how to approach such questions.

![Top 10 Power BI Interview Questions & Answers](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-3027.png)

Prefer video? See this...
-------------------------

I made a video with 10 questions and my (elaborate) answers to them. Watch to learn how to answer such interview questions.  See it below or [on my YouTube channel](https://youtu.be/aZihsRsEYTE)
.

1\. What are the main differences between Power BI Desktop and Power BI Service?
--------------------------------------------------------------------------------

Answer cues:

*   Power BI Desktop is the main tool for creating or _authoring_ reports.
*   We use PBI desktop to clean up data, create data model, set up measures, build and refine charts and construct the reports.
*   We then use Power BI Service to share the reports with the audience.
*   Desktop = creation tool, Service = consumption tool

2\. Explain the difference between a measure and a calculated column?
---------------------------------------------------------------------

*   Measures:
    *   calculate things **on top of tables.**
    *   **calculated in the run-time** based on the evaluation context.
    *   are usually aggregates.
    *   example: Shipment Count = COUNTROWS(_Shipments_)
*   Calculated columns:
    *   are **part of the table**.
    *   are **calculated at the time of creation** based on the row-context.
    *   have one value per row.
    *   example: Discount Rate _Row-wise calculation of discount rate based on order quantity_
*   Both measures and calculated columns use the same DAX language.

3\. Describe the steps you would take to connect multiple data sources in a Power BI report?
--------------------------------------------------------------------------------------------

*   We can use Power Query to connect more than one source of data.
*   We can also use PQ to merge / append / combine the data as needed.
*   We can selectively load the data to Power BI and keep the rest in PQ level but customizing the load behaviour.

4\. What do 1, \* and arrow (▶) mean in the data model diagram?
---------------------------------------------------------------

![Data model diagram (Power BI)](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-3028.png)

*   In a typical star-schema, we will have one to many relationship between dimension and fact table.
*   The one side is denoted with a 1 and many side is denoted with a \*
*   The arrow indicates the direction of filter propagation.
*   Power BI allows us to customize the filter direction (uni or bi-directional) and also have many-to-many relationships.

5\. What is DAX and give me an example of DAX you've recently used?
-------------------------------------------------------------------

*   DAX stands for Data Analysis eXpressions. It is the main language of Power Pivot.
*   Give examples based on your experiences and tell why / how they helped you solve problems.

6\. How do you optimize the performance of a slow Power BI report?
------------------------------------------------------------------

![Performance Optimization in Power BI](https://chandoo.org/wp/wp-content/uploads/2023/10/optimize-power-bi.jpg)

*   Answer questions like this based on your experience. If you have never optimized something, be honest and say that. Then give theoretical answers. 
*   Key optimization startegies:
    *   Reducing the data (filtering at PQ, Source level)
    *   Removing unwanted visuals, interactions and bookmarks
    *   Using performance profiler (Optimize ribbon in Power BI) to measure the performance of a page and identifying the problem areas.
    *   Setting up aggregate tables, pre-calculated views.
    *   \[NEW\] Using visual calculations instead of measures.
    *   Upgrading the Power BI on-prem servers, database servers (for direct query)
    *   Running time-consuming operations (such as PQ transformations) at low usage times (midnights, evenings)

7\. How do you publish a Power BI Report to the service?
--------------------------------------------------------

1.  Save and test the report. Make sure all calculations are correct and visuals represent the truth.
2.  Test any connections, refresh processes too.
3.  Publish the report (Publish button) and set the correct workspace.
4.  Test the report on the service view and make sure right people have access to the report.
5.  _Optional,_ Send an email or share the report with the audience.

8\. Explain RLS (Row Level Security) in Power BI?
-------------------------------------------------

*   Row Level Security allows us to provide access to the relevant data to right people.
*   For example, we can use RLS to show only USA data to the USA regional manager.
*   We can use “roles” option in Power BI to set and test the roles. 

9\. What is a Slowly Changing Dimension (SCD) and how do you handle it in Power BI?
-----------------------------------------------------------------------------------

![Type 2 SCD - Example (source: Oracle.com)](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-3030.png)

*   SCD (Slowly Changing Dimension) is a dimension (or aspect of a dimension) that changes slowly over time.
*   Give examples from your industry or previous work.
*   Example: In our product table, we have a feature called _**cocoa percentage.**_ For certain products this is changed once in a while based on customer feedback. This is an example of SCD.
*   We can either replace the old values with new ones or create effective date based records. 

10\. How would you handle missing data?
---------------------------------------

![Missing values in Power Query](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-3031.png)

*   We can use either Power Query or Power Pivot to handle missing values in our data. 
*   Power Query shows missing values in a column thru Column Quality feature. We can use this to identify and deal with missing values.
*   The key strategies for dealing with missing data are:
    *   Removing missing values
    *   Going back to source and fixing the problem
    *   Replacing missing values with an approximation (imputation)
    *   Ignoring missing values

Need more help? Watch the video
-------------------------------

I made a video with 10 questions and my (elaborate) answers to them. Watch to learn how to answer such interview questions.  See it below or [on my YouTube channel](https://youtu.be/aZihsRsEYTE)
.

Learn more: Power BI Weekend (2023)
-----------------------------------

My annual Power BI event – Power BI Weekend is happening this year on November 18 & 19. In this 4 hour event (2 hours on Saturday – Nov 18 & 2 more on Sunday – Nov 19), you will learn the Power BI Essentials to say yes to your next challenge.

[![Power BI Weekend 2023](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-3006.png)](https://chandoo.org/wp/power-bi-weekend/)

The topics covered are,

*   What is Power BI? How to use it?
*   Power BI vs Power Query vs. Power Pivot
*   Understanding Power BI Visual interactions & customizing them
*   Data cleanup and transformations with PQ
*   Setting up a star schema data model
*   Creating and using DAX measures
*   Interactive storytelling in Power BI
*   Saving & publishing your work
*   Resources to learn more
*   Q&A with you

Tickets are on sale now. Book yours before they sell-out.

[Power BI Weekend - Click here](https://chandoo.org/wp/power-bi-weekend/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [2 Comments](https://chandoo.org/wp/power-bi-interview-questions-answers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-bi-interview-questions-answers/#respond)
    
*   Category: [Interview Questions](https://chandoo.org/wp/category/interview-questions/)
    , [Power BI](https://chandoo.org/wp/category/power-bi/)
    

[PrevPreviousSQL vs. Power Query – The Ultimate Comparison](https://chandoo.org/wp/sql-vs-power-query/)

[NextWho went to both USA & UK? \[Excel Challenge\]Next](https://chandoo.org/wp/who-went-to-both-usa-uk-excel-challenge/)

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
    
    [Reply](https://chandoo.org/wp/power-bi-interview-questions-answers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/power-bi-interview-questions-answers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/power-bi-interview-questions-answers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ