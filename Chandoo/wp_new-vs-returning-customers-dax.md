# New vs. Returning Customers Analysis with DAX [Easy Formulas]

**Source:** https://chandoo.org/wp/new-vs-returning-customers-dax

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

New vs. Returning Customers Analysis with DAX \[Easy Formulas\]
===============================================================

*   Last updated on March 5, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![New vs. Returning customer counts with DAX in Power BI](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0107.png)

DAX offers powerful way to analyze “new” vs. “returning” customers. In this article learn easy and simple DAX measure patterns to count number of new customers and number of returning customers from your data.

What is a Returning Customer?
-----------------------------

![Who is a returning customer - illustration](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0108.png)

A returning customer is someone who comes back to our business and does another transaction. For example, in the above illustration, CUST-001 and CUST-004 are repeat or returning customers.

What is a NEW customer?
-----------------------

A new customer is someone who is doing their first transaction with us. In the above example data, all other customers (except CUST-001 & CUST-004) are _technically_ **NEW CUSTOMERS.**

Note: A new customer today might be a _returning customer in future._

DAX measures for calculating new vs. returning customer counts
--------------------------------------------------------------

All the measures in this example are based on a simple “Data” table with 4 columns – Customer ID, Date, Order Qty and Product Name.

![sample data - new vs. returning customer dax](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0109.png)

### Customer Count Measure

    =Customer Count = DISTINCTCOUNT(data[Customer ID])

This is a simple **distinct count** measure that tells us how many distinct customers transacted with us. When used with a the context of a date or product we will get the number of customers per each.

### Returning Customer Count Measure

    Returning Customer Count = 
        var custs = DISTINCT(data[Customer ID])
        var curr_date = LASTDATE(data[Date])
    return
        sumX(custs, CALCULATE([Customer Count], data[Date]<curr_date))

This measure tells us how many returning customers are there for the context of current “time-period”.

### How this returning customer count works?

Imagine the below output and let’s focus on the second row.

![returning customer count DAX measure - explained](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0110.png)

*   For the date context of 6-January
*   We create custs variable which gives us all the 92 customer IDs.
*   The curr\_date variable tells us the latest date – _i.e._ 6-January.
*   We then iterate for each of the customers in custs table and calculate the \[Customer Count\] prior to the curr\_date. This would be 1 if the customer has previously transacted with us and 0 otherwise.
*   The SUMX adds up all these values (ie all 1s) and tells us 33, which is the number of returning customers.

### New Customers Measure

    New Customers = [Customer Count] - [Returning Customer Count]

If you already have both the total \[customer count\] and \[returning customer count\], you can easily subtract one from another to get the \[new customers\] count.

But if you don’t have the \[returning customer count\] or just want to _directly_ calculate the \[new customers\], you can use below DAX measure.

    New Customer Count - direct = 
        var custs = DISTINCT(data[Customer ID])
        var curr_date = LASTDATE(data[Date])
    return
        SUMX(custs, IF(CALCULATE([Customer Count], data[Date] < curr_date)=0,1,0))

The above measure uses the same approach as \[Returning Customer Count\] but flips the logic inside SUMX by using the IF function to negate the CALCULATE result.

Returning Customers in Last 4 Weeks or similar
----------------------------------------------

![Returning customers in last 4 weeks](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0111.png)

While the above \[Returning Customer Count\] works flawlessly, it may not be realistic to consider a customer to be returning if they _rarely_ transact. So a more realistic calculation would be to consider a customer to be returning if they did some business in the last 4 weeks (or x periods). Here is the DAX pattern for that.

    Returning Customers in Last 4 Weeks = 
        var custs = DISTINCT(data[Customer ID])
        var curr_date = LASTDATE(data[Date])
        var start_date = DATEADD(curr_date,-28,DAY)
    return
        SUMX(custs, CALCULATE([Customer Count], data[Date]<curr_date && data[Date]>=start_date))

In this case, we simply calculate the “start\_date” for our calculation window as well. Here I have used 28 days as an example, but you can easily change this to any window size.

Then we apply the same SUMX logic but modify the filter context in the CALCULATE to check both boundaries of the dates.

Why not do this analysis in SQL or somewhere upstream?
------------------------------------------------------

![Why not use SQL for tagging customers](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0112.png)

When I mentioned about this approach to my wife Jo, she said, why not do this in SQL directly and tag each customer as “new” or “returning”?

Here is why I prefer to do this with DAX:

*   **Business Rule Flexibility:** With DAX based approach, we can easily change the business rule surrounding who is a returning customer. For example, we can use the 4 week window like above easily.
*   **Interactivity:** We can add a product slicer (see below) to analyze which customers returned to purchase the same product. This is incredibly helpful to understand customer loyalty and campaign effectiveness.

Of course, there are advantages with SQL approach too. Mainly,

*   **SQL tagging is faster:** Unlike DAX calculations which run in real-time & client-side, SQL calculations are done once and at server side. When you have millions or billions of records, doing SUMX in real-time is going to be slow.
*   **Consistency:** Applying customer tagging at server side in the data layer means the business rule & logic is consistently applied for every report.

Sample Power BI Workbook:
-------------------------

If you want to play with these measures and understand the calculation better, check out the [sample PBIX file here](https://chandoo-my.sharepoint.com/:u:/g/personal/me_chandoo_onmicrosoft_com/EZsfwVVfw69Bls6cgS9KdcwBPoy7ip8sNIofvTM0bs83Xw?e=XP1MP3)
.

In conclusion
-------------

New vs. Returning Customer analysis is a must-have for customer analytics. The DAX required for this is easy to implement and works beautifully. Try this analysis to understand the effectiveness of marketing campaigns (lead gen, customer capture) and loyalty programs (reward points, notifications). Using a time-window based calculations (ex: 4 weeks) is a great way to understand customer behavior and purchasing patterns.

Learn more:
-----------

*   [Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)
    
*   [Employee Churn Analysis with Power Query](https://chandoo.org/wp/figuring-out-employee-churn-with-power-query-hr-analytics/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/new-vs-returning-customers-dax/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/new-vs-returning-customers-dax/#respond)
    
*   Tagged under [calculate](https://chandoo.org/wp/tag/calculate-2/)
    , [dax](https://chandoo.org/wp/tag/dax/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [sumx](https://chandoo.org/wp/tag/sumx/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

[PrevPreviousHow to find duplicate values in two columns in Excel using formula](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/)

[NextEasily Convert JSON to Excel – Step by Step TutorialNext](https://chandoo.org/wp/json-to-excel-howto/)

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
    
    [Reply](https://chandoo.org/wp/new-vs-returning-customers-dax/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/new-vs-returning-customers-dax/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/new-vs-returning-customers-dax/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ