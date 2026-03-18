# How to get non-adjacent columns with FILTER function in Excel

**Source:** https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to get non-adjacent columns with FILTER function in Excel
=============================================================

*   Last updated on March 12, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel 365’s FILTER() function is great for getting a cut of data that meets your criteria. But what if you need to filter and then show non-adjacent columns? Something like below. In this article, let me show you a few options to get discrete columns after filtering with the FILTER function.

![Get Non-adjacent columns with Excel FILTER function](https://chandoo.org/wp/wp-content/uploads/2024/03/image-100.png)

Using CHOOSECOLS with FILTER()
------------------------------

Imagine you have a table data named “staff” and you want to see all the staff who joined in year 2021. We can use below FILTER function for that.

    =FILTER(staff, YEAR(staff[date of join])=2021)

This will provide a list of all staff who joined in year 2021, as depicted below.

![filter result, but we don't want all the columns - just 1,2,7 & 8](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0040.png)

But we don’t want all columns, just ID, Gender, Salary and Leave Balance.

To see just columns 1,2,7 & 8 of this filtered data, we can use below formula.

    =CHOOSECOLS(
    FILTER(staff, YEAR(staff[date of join])=2021),
    1,2,7,8)

This will give you exactly what you need without anything else.

![Filter with choosecols - sample result](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0039.png)

What if I need to get data, but the column order is different from original data…
---------------------------------------------------------------------------------

![Showing columns out of order in Excel](https://chandoo.org/wp/wp-content/uploads/2024/03/filter-non-adjacent-columns-diff-order.png)

Say, you do want the columns 2,6,8&9 but you want them to show up in the order 6,8,2&9 in the final output.

You can still use the CHOOSECOLS function like below.

    =CHOOSECOLS(FILTER(staff, YEAR(staff[date of join])=2021),6,8,2,9)

How to get columns from a list of header names
----------------------------------------------

If you want to use a range of column names and show filtered data for only those columns, we can use XMATCH along with CHOOSECOLS and FILTER, as demoed below.

![using column headers to figure out which columns to show](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0036.png)

1.  Set up your column headers in a range like Z5:AC5
2.  Now, we can use XMATCH to find the positions of these headers. =XMATCH(Z5:AC5, staff\[#headers\])
3.  When you pass the result of XMATCH to CHOOSECOLS, you can pick these columns.

    =CHOOSECOLS(
         FILTER(staff,YEAR(staff[Date of Join])=2021),
         XMATCH(Z5:AC5,staff[#Headers]))

### How does this work…

*   Let’s go inside out.
*   The FILTER() function gets all the staff data for people whose joining date is in 2021.
*   **Range Z5:AC5 holds the names of the columns we want to see.**
*   XMATCH(Z5:AC5, staff\[#Headers\]) will tell you the column numbers for the columns you want by looking them up in the table header row.
*   CHOOSECOLS() will then return those exact columns

Learn more about these functions:
---------------------------------

*   [How to use FILTER function in Excel](https://chandoo.org/wp/dynamic-array-functions/#elementor-toc__heading-anchor-3)
    , [FILTER function video tutorial](https://youtu.be/JuTdj2j-9Kg)
    
*   [How to use XLOOKUP function in Excel](https://chandoo.org/wp/xlookup-examples/)
    
*   [How to use tables in Excel](https://chandoo.org/wp/data-tables/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [FILTER()](https://chandoo.org/wp/tag/filter/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousGet all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[NextWeighted Average in Excel \[Formulas\]Next](https://chandoo.org/wp/weighted-average-excel/)

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
    
    [Reply](https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-get-non-adjacent-columns-with-filter-function-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ