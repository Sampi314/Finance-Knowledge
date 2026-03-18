# OFFSET formula - Explained » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/offset-formula-explained

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

OFFSET formula – Explained
==========================

*   Last updated on September 17, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**_Today, lets learn OFFSET formula._**

What is OFFSET and why bother using it?
---------------------------------------

OFFSET formula gives us reference to a range, from a given starting point with given height and width in cells.

### OFFSET formula syntax

OFFSET formula looks like this:

> \=OFFSET(starting point, rows to move, columns to move, height, width)

*   **Starting point:** This is a cell or range from which you want to offset
*   **Rows & columns to move:** How many rows & columns you want to move the starting point. Both of these can be positive, negative or zero. More on this below.
*   **Height & width:** This is the size of range you want to return. For ex. 4,3 would give you a range with 4 cells tall & 3 cells wide.

_**And yes,**_ All the arguments to OFFSET can be references to other cells. That means, you can write =OFFSET(A1,D1,D2,D3,D4) which will refer to a range

*   Starting from A1
*   Offset by D1 rows & D2 columns
*   having the size of D3 rows & D4 columns

See below examples to understand the formula better.

### OFFSET formula examples

![Microsoft Excel OFFSET Formula Examples](https://img.chandoo.org/f/excel-offset-formula-examples.png "Microsoft Excel OFFSET Formula Examples")

### Why use OFFSET?

Why not write a reference like A1:C4 directly?

Here are a few reasons why,

1.  **Dynamic ranges:** Reference like A1:C4 always refers to the range A1:C4. _ie_ it is static. But sometimes, we want our ranges to be dynamic. This is required because our data is changing (every month new row is added, every time we launch a product new column is added etc.)
2.  **We don’t know the exact address:** Sometimes, we don’t know what our ranges actual address is. Rather, we just know it is starting from a certain cell etc. In such situations OFFSET is useful.

Understand OFFSET formula – Interactive Workbook
------------------------------------------------

Since OFFSET formula is somewhat tricky to get, I created an interactive workbook so that you can understand how it works. When you input all the 5 parameters, the workbook highlights the range that your OFFSET will give. After playing with it for a few minutes, you will understand the formula better.

[![OFFSET Formula - Interactively explained - Click to download](https://img.chandoo.org/f/offset-formula-interactive-explanation.gif "OFFSET Formula - Interactively explained - Click to download")](https://img.chandoo.org/f/offset-formulas.xlsx)

[![Learn OFFSET formula - Download Interactive Workbook](https://img.chandoo.org/f/download-interactive-excel-workbook-offset-examples.png "Learn OFFSET formula - Download Interactive Workbook")](https://img.chandoo.org/f/offset-formulas.xlsx)

Practical use for OFFSET – Average of latest week
-------------------------------------------------

Lets say we monitor quality of a plant producing purple puppets. One of the KPIs we monitor is _% of rejected puppets_. We have been tracking the % of rejects by day in a spreadsheet that looks like this:

![Average of Latest Week - Practical use of OFFSET formula](https://img.chandoo.org/f/average-of-latest-week-data.png "Average of Latest Week - Practical use of OFFSET formula")

So how do we calculate **average of latest week?**

Assuming the values are in range C3:C18, we can write =AVERAGE(C12:C18)

**BUT, WE NEED TO CHANGE THIS FORMULA EVERYDAY!!!**

_Even puppets would find that boring._

By using the OFFSET awesome sauce, we can write the AVERAGE formula once and forget about it.

\=AVERAGE(OFFSET(C3,COUNTA(C3:C300)-7,0,7,1))

### Lets break-apart this formula and understand

*   To calculate latest week’s average, we need to go all the to the last data point and then get 7 rows from it and average those values.
*   This is where COUNTA(C3:C300) – 7 comes in to picture. It counts how many values are there in column C and then subtracts 7 from it.
*   The OFFSET would then starting point from C3 to latest week’s starting point.
*   To know how this formula works, watch below demo.

![Average of latest week - OFFSET formula usage - demo](https://img.chandoo.org/f/average-last-7-days-offset-formula-explanation.gif "Average of latest week - OFFSET formula usage - demo")

OFFSET limitations
------------------

While offset formula can return with a dynamic range when you beckon, it does have few limitations:

*   **OFFSET formula is volatile:** In plain English it means, whenever there is any change in your workbook, OFFSET formula is recalculated, thus keeping Excel busy a tiny bit longer. This is not an issue if you use OFFSET formula in a small workbook. But when you use lots of OFFSET formulas in large workbooks, you will end up cursing Excel as it takes too much time to recalculate.
*   **OFFSET formulas are tricky to debug:** Because the references are dynamic, debugging a workbook with lots of OFFSETs can get tricky quickly.

Alternatives to OFFSET formula
------------------------------

There 2 fine alternatives to OFFSET formula.

*   **Use Excel Tables:** Since Excel 2007, we can create tables from structured data and write formulas, create charts that refer to dynamic ranges with ease. [Click here to know more about tables](http://chandoo.org/wp/2009/09/10/data-tables/)
    .
*   **Use INDEX formula:**  Although not exactly same as OFFSET, INDEX formula can also be used to generate dynamic range references. Plus, INDEX is a non-volatile formula, so it wont keep Excel busy unnecessarily. [Know more about INDEX formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    .

Do you use OFFSET formula?
--------------------------

For most of my dynamic range needs, I rely on tables or INDEX formula. I use OFFSET formula when I have to calculate values like _average of latest week_. In such cases OFFSET is an elegant solution.

**What about you?** Do you use OFFSET formula? In which situations do you use it? Please share your tips & examples with us using comments.

### Know More about OFFSET

_Check out below examples to understand OFFSET formula better:_

*   Calculations: [Sum of values between 2 dates](http://chandoo.org/wp/2011/09/27/sum-between-2-dates/)
     | [Moving averages](http://chandoo.org/wp/2009/04/28/calculate-moving-average/)
     | [Average of closest numbers](http://chandoo.org/wp/2011/01/19/average-of-closest-2-numbers/)
    | [_**More…**_](http://chandoo.org/wp/category/formula-forensics/)
    
*   Modeling: [Calculate IRR of dynamic ranges](http://chandoo.org/wp/2011/10/04/offset-function-to-calculate-irr-for-dynamic-range/)
     | [Manage scenario analysis](http://chandoo.org/wp/2012/02/14/reporting-scenarios-using-offset/)
    
*   Charting & Dashboards: [Dynamic range charts](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/)
     | [Top x chart](http://chandoo.org/wp/2009/11/12/topx-chart/)
     | [Analyzing large datasets](http://chandoo.org/wp/2010/11/04/analysing-large-tables/)
     | [KPI dashboards](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   Validations & Pivots: [Dynamic Data Validation](http://chandoo.org/wp/2010/09/13/dynamic-data-validation-excel/)
     | [Dependent Drop downs](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/)
     | [De-duplicate & Sort data](http://chandoo.org/wp/2010/09/27/remove-duplicates-using-pivot-tables/)
    
*   _[And many more uses of OFFSET](http://chandoo.org/wp/tag/offset/)
    _

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [88 Comments](https://chandoo.org/wp/offset-formula-explained/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/offset-formula-explained/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow many values are common in 2 lists? \[homework\]](https://chandoo.org/wp/count-of-common-values-in-2-lists/)

[NextCustomize Zebra lines Quickly using Table Styles \[tip\]Next](https://chandoo.org/wp/custom-zebra-lines-table-styles/)

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
    
    [Reply](https://chandoo.org/wp/offset-formula-explained/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/offset-formula-explained/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/offset-formula-explained/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ