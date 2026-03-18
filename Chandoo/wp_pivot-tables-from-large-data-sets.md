# How to make pivot tables from large data-sets - 5 examples » Chandoo.org

**Source:** https://chandoo.org/wp/pivot-tables-from-large-data-sets

---

*   [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Pivot Tables from large data-sets – 5 examples
==============================================

*   Last updated on August 2, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Let’s say you are starting at a large data-set with multiple columns. You need to make a pivot report from it for a client or manager. **_How would you go about it?_**

![pivot tables from large datasets](https://chandoo.org/wp/wp-content/uploads/2019/08/pivot-tables-from-large-datasets-howto.png)

This is the exact problem Jo, my wife faced the other day. She came home and after catching up on each other’s day, she asked me how I would do it. That got me thinking. This blog post is born out of that rumination.

### Large data-set? Tell me more:

Imagine you have sales data which customer bought products in each city of operation. Say, you have 100s of customers, operate in 50 major cities and sell 16 different products. If you try to [make a pivot table](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
 with all these fields, you will end up with a monstrosity of 5000 rows. Nobody can read that pivot and make any sense.

![example large data set](https://chandoo.org/wp/wp-content/uploads/2019/08/large-dataset-example.png)

**_What now?_**

Ideas for creating **pivot tables from large data-sets**
--------------------------------------------------------

Here is a list of five ideas to use **_when you need to create pivot tables from large data-sets_**.

### Idea #1 – Add slicer to one of the fields

Even though you have many fields, chances are the report user wants to focus on one of the elements to start conversation. Add it a slicer. (Related: [Introduction to Excel Slicers](https://chandoo.org/wp/introduction-to-slicers/)
)

![slicer driven pivot - example](https://chandoo.org/wp/wp-content/uploads/2019/08/slicer-pivot-from-large-data-1.png)

### Idea #2 – Show just top values

You can apply value filtering on pivot tables to show just the top performing customer (or product, city etc.). This will greatly reduce the size of your pivot table. You can also collapse a sub-level detail so that user can press + if they want to see details.

![pivot table showing just top value per city](https://chandoo.org/wp/wp-content/uploads/2019/08/Top-1-customer-pivot-from-large-data-2.png)

To set top 1 filter, simply click on the filter icon on field you want to set it, go to value filters > top 10 and then set it to **top 1**.

![how to apply top 1 value filter in pivot tables](https://chandoo.org/wp/wp-content/uploads/2019/08/top10-value-filter.png)

### Idea #3 – Individual pivots with drill down option

You can double click on any number in pivot tables to see detail rows that add-up to that number. We can show summary _pivot tables from large data-sets_ instead of full-blown ones. Here is an example.

![individual pivots with drill-down option](https://chandoo.org/wp/wp-content/uploads/2019/08/individual-pivots-with-drill-down-pivot-from-large-data-3.png)

### Idea #4 – Set up support table to show top 3 vs. other view

You can categorize fields like products, customers etc. by introducing an extra table that splits them in to groups. For example, we can categorize products to two types:

*   Top 3 products: Most selling products across all our data
*   Other products

![Product types table by ranking products based on sales volume](https://chandoo.org/wp/wp-content/uploads/2019/08/support-table-product-types.png)

Once you have such a table, you can connect this product.types table to original data using relationships and then build a multi-table pivot.

Related: [How to use relationships to build multi-table pivots in Excel](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)

![City level sales by product type](https://chandoo.org/wp/wp-content/uploads/2019/08/product-types-instead-of-details-pivot-from-large-data-4.png)

### Idea #5 – Add two-level filtering by alphabets

When using fields like customers or products, you cannot easily apply slicer or report filter on them. This is because such fields have 100s of values usually. One way to reduce the clutter is by introducing two-level filtering.

We can easily do this by adding an extra column to our data to calculate the first letter of customer name. (something like **\=LEFT(\[@customer\],1)** will do.

Once you have such new field, you can set up a multi-level filtered pivot report like below.

![Two level filtering with customer name first letter](https://chandoo.org/wp/wp-content/uploads/2019/08/two-level-filtering-pivot-from-large-data-5-1.png)

### Video Tutorial – How to pivot large data sets?

Here is a quick video explaining the problem, 5 pivot tables from large data-set and how to set up extra bits like conditional formatting in detail. Watch it below or [**view it on Chandoo.org YouTube Channel**](https://youtu.be/u4aeZ4ukrqI)
.

### Download Workbook – Large data set pivot table ideas

**[Click here to download the sample workbook for this tip](https://chandoo.org/wp/wp-content/uploads/2019/08/5-pivot-ideas-for-large-datasets.xlsx)
**. You can examine all the pivots in there. Feel free to create something on your own and share it in the comments section.

### How do you make pivot tables from large data sets?

I try to avoid large pivot tables. But if I must (either because a customer wanted them or they are part of a larger report), I follow the ideas presented in this post.

**What about you?** How do you create pivot tables from large data sets? Please share your thoughts in the comments section below.

More pivot table tips
---------------------

*   [How to get percentage of something calculation in pivots?](https://chandoo.org/wp/percentage-of-another-value-pivot-table/)
    
*   [Distinct count in Excel pivots](https://chandoo.org/wp/distinct-count-pivot-tables/)
    

[![Distinct count in Excel pivot tables - tip](https://assets.chandoo.org/wp/wp-content/uploads/2018/05/distinct-count-excel-pivot.png)](https://chandoo.org/wp/distinct-count-pivot-tables/)

*   [Currency format pivot table values with one-click (macro)](https://chandoo.org/wp/currency-format-pivot-fields-with-one-click/)
    
*   [More tips & tricks on Excel pivot tables](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/pivot-tables-from-large-data-sets/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/pivot-tables-from-large-data-sets/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [top 10 values](https://chandoo.org/wp/tag/top-10-values/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousHow to conditionally format visuals in Power BI?](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/)

[NextHow-to highlight maximum value in Excel charts? \[Quick tip\]Next](https://chandoo.org/wp/how-to-highlight-maximum-value-in-excel-charts/)

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
    
    [Reply](https://chandoo.org/wp/pivot-tables-from-large-data-sets/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/pivot-tables-from-large-data-sets/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/pivot-tables-from-large-data-sets/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ