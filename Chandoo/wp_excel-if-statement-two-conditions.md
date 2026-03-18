# Excel IF Statement Two Conditions » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-if-statement-two-conditions

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel IF Statement Two Conditions
=================================

*   Last updated on May 29, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

You want to check two conditions with Excel IF function? You’ve come to the right place.  
IF is one of Excel’s most popular and versatile functions. But things get exciting when you start combining it with **multiple conditions** — especially using `AND`, `OR`, `nested IFs`, and even blending it with `SUMIFS`.

In this article, let me show you how to write IF formulas with a real-life example using a sales dataset, depicted below. [Click here to download the data file](https://chandoo.org/wp/wp-content/uploads/2025/05/if-multiple-conditions.xlsx)
.

[![Sample data - Excel IF Function with two conditions](https://chandoo.org/wp/wp-content/uploads/2025/05/sample-data-if-function-excel-two-conditions.png)](https://chandoo.org/wp/wp-content/uploads/2025/05/if-multiple-conditions.xlsx)

* * *

Example 1: Excel IF Statement Two Conditions Using `AND`
--------------------------------------------------------

![Excel IF Function - Two Conditions - Example scenario](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0120-1.png)

**Scenario:** You want to check if a sale happened in the **North** region and if the **revenue is more than 2000**.

    =IF(AND(G4>2000, C4="North"), "Yes", "No")

**What this does:** If both conditions are true, it says “Yes”. If even one fails, you get “No”.

This is perfect for filtering VIP-level sales in specific territories.  

* * *

Example 2: IF with Date Condition
---------------------------------

![IF and Date conditions in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)

**Scenario**: You want to see if the salesperson is Bob and the sale happened before April 15, 2025.

    =IF(AND(D4="Bob", B4<DATE(2025,4,15)), "Yes", "No")

? DATE(2025,4,15) ensures your comparison stays clean even if the actual cell has time info baked in.  

* * *

Example 3: Bonus Calculation Using IF + Arithmetic
--------------------------------------------------

![Using IF with two conditions in Excel to calculate bonus](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0122.png)

**Scenario**: You want to calculate bonus:

*   If revenue > 3000 and units sold > 35 ? 5% bonus
*   Otherwise ? 3% bonus

    =IF(AND(G4>3000, F4>35), 5%, 3%) * G4

This is a very common use-case: checking two values to decide payout level.

* * *

Example 4: Multiple OR Conditions Inside IF
-------------------------------------------

![Using AND + OR functions inside IF function - Complex example](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0124.png)

**Scenario**: Approve if either region is North or South, and salesperson is either Alice or Bob.

    =IF(AND(OR(C4="North", C4="South"), OR(D4="Alice", D4="Bob")), "YES", "NO")

? Combine AND and OR when you need multiple “paths” to approval.

* * *

Example 5: Categorizing Using Nested IFs and Between
----------------------------------------------------

![Nested IF function example](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0125.png)

**Scenario:** Label accounts based on revenue:

*   Over 4500 ? “Major Account”
*   Between 3000 and 4500 ? “Key Account”
*   Else ? “Normal Account”

    =IF(G4>4500, "Major Account", IF(AND(G4>=3000, G4<=4500), "Key Account", "Normal Account"))

Nested IFs are a good fit when you have tiered logic like this.

\[[Learn how to write BETWEEN Condition in Excel](https://chandoo.org/wp/between-formula-excel/)\
\]

* * *

Example 6: Day of Week Based Label
----------------------------------

![Nested IF with dates to figure out start, mid or end of week](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0126.png)

**Scenario**: Label the day based on when the sale occurred:

*   Monday–Wednesday ? “Start of Week”
*   Thursday–Friday ? “Mid Week”
*   Weekend ? “Weekend”

    =IF(WEEKDAY(B4,2)<=3, "Start of Week", IF(WEEKDAY(B4,2)<=5, "Mid Week", "Weekend"))

**Note**: WEEKDAY(date, 2) makes Monday = 1 and Sunday = 7.

* * *

Bonus: Beyond IF – Using Conditions in SUMIFS
---------------------------------------------

IF is great when you’re checking one row at a time. But if you want to sum based on multiple filters, use [SUMIFS](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
.

### SUMIFS Examples:

#### Total revenue from North region and Bob:

![Combining IF and SUM to add up values that meet two criteria](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0127.png)

    =SUMIFS(G4:G33, C4:C33, "North", D4:D33, "Bob")

#### Units sold for Product A before or on April 20, 2025:

![SUM IF with date conditions example](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0128.png)

    =SUMIFS(F4:F33, E4:E33, "Product A", B4:B33, "<=20-Apr-2025")

#### Revenue from South between April 10 and 25:

![Dates between condition for SUMIFS - example](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0129.png)

    =SUMIFS(G4:G33, C4:C33, "South", B4:B33, ">=10-Apr-2025", B4:B33, "<=25-Apr-2025")

* * *

Highlight IF conditions are met
-------------------------------

We can use Excel conditional formatting to highlight cells that meet one or more conditions. Here is a quick demo of how to highlight all revenue > 3000.

![Highlight values that meet IF condition - excel example](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-30_09-42-31.gif)

*   Select the data you want to highlight
*   Go to Home > Conditional Formatting > and set up the rule based on the behavior you want. (For example, highlight cells -> Greater than is perfect for the above example)
*   Specify the input and format
*   Click ok to have the rule “dynamically applied” to your data
*   You can add more complex and multiple condition rules too. Refer to my [conditional formatting basics page for a proper tutorial](https://chandoo.org/wp/excel-conditional-formatting-basics/)
    .

* * *

A Few More Handy Patterns
-------------------------

Here are a few more patterns you can experiment with:

### Check for blank cells:

    =IF(ISBLANK(D4), "Missing", "Present")

### Combine IF with SEARCH (for partial matches):

    =IF(ISNUMBER(SEARCH("Bob", D4)), "It's Bob", "Not Bob")

### Complex multi-check with helper column idea:

Use a helper column like IsQualified that uses:

    =IF(AND(G4>2500, F4>=25, C4="North"), "Qualified", "Nope")

Then you can filter or pivot based on IsQualified.  

* * *

Final Thoughts
--------------

Combining IF with AND, OR, and nesting gives you powerful logic control — without writing code. Start with two conditions, then try combining patterns as shown here.

Want to go further? Try writing a formula that combines:

*   Multiple date checks
*   Region + product filters
*   Revenue thresholds

Let Excel do the thinking for you!

### Additional Resources for you

Refer to below pages for more help on IF conditions with Excel.

*   [10 Advanced IF tricks you must know](https://chandoo.org/wp/advanced-if-tricks/)
     ([or watch this video](https://www.youtube.com/watch?v=-yFpzIRifK4)
    )
*   [How to use SUMIFS to add up data that meets one or more conditions](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
    
*   [Replacing long, nested IF functions with CHOOSE formula](https://chandoo.org/wp/introduction-to-choose-function/)
    
*   [BETWEEEN Formula in Excel](https://chandoo.org/wp/two-dates-in-month-check/)
    
*   [Conditional formatting – Highlight IF rules are met](https://chandoo.org/wp/excel-conditional-formatting-basics/)
    
*   IF challenges for you:
    *   [Can you vote in Sumeria?](https://chandoo.org/wp/sumerian-voter-problem/)
        
    *   [Blood pressure categorization](https://chandoo.org/wp/bp-category-problem/)
        
    *   [Check if both dates are in the same month?](https://chandoo.org/wp/two-dates-in-month-check/)
        

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/excel-if-statement-two-conditions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-if-statement-two-conditions/#respond)
    
*   Tagged under [conditional formatting](https://chandoo.org/wp/tag/conditional-formatting-2/)
    , [date](https://chandoo.org/wp/tag/date/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [if then statement](https://chandoo.org/wp/tag/if-then-statement/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [ifs](https://chandoo.org/wp/tag/ifs/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Nested If](https://chandoo.org/wp/tag/nested-if/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[NextHow to enable developer ribbon in Excel?Next](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/excel-if-statement-two-conditions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-if-statement-two-conditions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-if-statement-two-conditions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ