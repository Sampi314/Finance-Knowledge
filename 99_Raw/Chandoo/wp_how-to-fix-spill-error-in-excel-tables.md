# How to fix SPILL Error in Excel Tables (3 easy solutions) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to fix SPILL Error in Excel Tables (3 easy solutions)
=========================================================

*   Last updated on February 21, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

So you have a **_SPILL error in your Excel tables?_** In this quick article, let me show you 3 easy fixes to the problem.

Fix 0: See if Excel can auto-fix the formula
--------------------------------------------

This is not really a fix. But if you write certain types of formulas in table, Excel will warn you about the _potential_ spill error and fix it for you. See this example:

![Excel auto correcting the SPILL error in tables](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3197.png)

One lesson we can take away from this _auto-correction of the formula_ is that if you are using a table column style formula, change it to \[@ column\] style.

For example:

*   Instead of LEFT(\[Name\]) use LEFT(\[@Name\], 1)
*   \=IF(LEN(\[Value\])>6, “Too long”, “Short enough”) can be =IF(LEN(\[**@**Value\])>6, “Too long”, “Short enough”)

Note: This auto-correction of formulas is seems to be a new feature, so may not be active in all Excel 365 versions.

Fix 1: Change to a non-spillable formula
----------------------------------------

If an Excel formula can result in more than one value, _it automatically spills_. Such formulas are called **[Dynamic Array Excel Functions](https://chandoo.org/wp/dynamic-array-functions/)
.** A simple example is the SEQUENCE function.

\=SEQUENCE(10)

will return the numbers 1 to 10.

If you use them in a normal cell in Excel, they work ok.

But when you type the same formula in a table, it gives the SPILL error (see this demo).

![Spill error in Excel Tables - quick demo](https://chandoo.org/wp/wp-content/uploads/2024/02/2024-02-22_09-34-52.gif)

So **an easy fix is to change your formula to a version that doesn’t spill**.

Refer to below table to see non-spillable alternatives for some common situations.

| Purpose | Spill Version | Non-Spill Alternative |
| --- | --- | --- |
| To generate row numbers in the table automatically | \=SEQUENCE(10) | \=ROW()-ROW(\[#Headers\]) |
| Show all matching values with FILTER | \=FILTER(data, data=10) | _Return only the first matching value:_  <br>\=XLOOKUP(10, data, data)  <br>_Concatenate all matches into one list:_  <br>\=TEXTXJOIN(“, “,, FILTER(data, data=10)) |

Fix 2: Convert Table to a Range
-------------------------------

If you must have a spillable formula in the table column, an easy fix is to convert the table to a range. You will however, loose all the table features (such as structural references, data model connectivity and ability to send data to Power Query).

To convert table to a range, just select the table, go to **Table Design ribbon and click on “Convert to Range” button.**

![convert table to a range using Table Design Ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3194.png)

Once your table is in a range format,

1.  Remove any spill formulas in the row 2 onwards in your range
2.  This will fix the #SPILL! error, as demoed below.

![Spill error will go away after you convert a table to range.](https://chandoo.org/wp/wp-content/uploads/2024/02/no-spill-error-after-converting-to-range.png)

Fix 3: Move the formula outside the table
-----------------------------------------

Tables do not support any sort of spill behavior. So another easy fix is to move the spill formula outside the table to an adjacent column. Something like this:

![Moving the dynamic array formula (spillable) outside the table resolves it!](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3195.png)

But what if I need the formula along with my table?
---------------------------------------------------

Unfortunately Excel **_currently_** doesn’t support having SPILLABLE formulas inside tables. But if you still need a formula result along with your table data (for some calculation purposes), you can use the HSTACK function, like below:

\=HSTACT(your\_table, spill\_formula\_here)

For example, I want to add a ID number column to my table. Here is the HSTACK for that:

\=HSTACK(my\_table, SEQUENCE(ROWS(my\_table)))

Why do we even get this error?
------------------------------

It’s not because Excel hates you. There are two things at play here.

*   **Dynamic Array Formulas:** want to spill the formula results down (or sideways) when there is more than value returned by the formula (example: SEQUENCE(10)). They throw a SIPLL error whenever something is preventing the formula from **_spilling._**
*   **Excel Tables:** want to apply the same formula for all cells in the table column.

So when you type an array formula in a table cell, Excel tries to apply the same formula for all cells of the table. This creates a situation where each table row has a formula that wants to return multiple values. So while first row’s formula is trying to spill, second row has a formula of its own (as Excel tables automatically apply the same formula across). Thus the SPILL errors.

Know more about Excel Tables & Dynamic Arrays
---------------------------------------------

Please read below articles to understand Excel Tables & Dynamic Array features of Excel.

*   [What is Excel Table and how to use it?](https://chandoo.org/wp/data-tables/)
    
*   [What is Dynamic Array Function in Excel?](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [How to use XLOOKUP in Excel?](https://chandoo.org/wp/xlookup-examples/)
    
*   [More about SPILL Error](https://support.microsoft.com/en-us/office/how-to-correct-a-spill-error-ffe0f555-b479-4a17-a6e2-ef9cc9ad4023)
     \[Microsoft Help\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/#respond)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousLoan Amortization Schedule in Excel – FREE Template](https://chandoo.org/wp/loan-amortization-schedule-in-excel/)

[NextGet all BOLD text out Excel Cells AutomaticallyNext](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ