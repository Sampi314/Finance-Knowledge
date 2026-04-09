# 5 Simple & Useful Conditional Formatting Tricks » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/5-useful-conditional-formatting-tricks

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

5 Simple & Useful Conditional Formatting Tricks
===============================================

*   Last updated on February 15, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Excel conditional formatting** is incredibly useful feature. In this page, let me share 5 simple & creative tricks for you.

If you are a beginner, please read [introduction to conditional formatting](https://chandoo.org/wp/conditional-formatting-top-tips/)
 page.

Trick 1 - Icons, but not too many
---------------------------------

Please click on below button to download the Excel file with all these tricks and refer to it when reading the article.

[Download Example Workbook](https://chandoo.org/wp/wp-content/uploads/2021/02/5-cf-tricks-2021.xlsx)

Iconset feature of conditional formatting is great for highlighting important bits of your data. But often then can be overkill. Let’s say you want to use icons to show which products have increased ▲or decreased ▼ their sales. But you don’t want them all the time…

![trick1-icons with limits](https://chandoo.org/wp/wp-content/uploads/2021/02/trick1-icons-with-limits.png)

You can do this by setting up upper & lower limit for the conditional  formatting rule and creating a 3 icon rule (with no cell icon for middle one).

See this:

![icon limits cf rule](https://chandoo.org/wp/wp-content/uploads/2021/02/icon-limits-cf-rule.png)

Trick 2 - Highlight entire row / column
---------------------------------------

If you want to highlight which values are above 2000, you can easily apply the **greater than…** conditional formatting rule. But what if you want to highlight the entire row when certain column has values above 2000?

![highlight entire row rule](https://chandoo.org/wp/wp-content/uploads/2021/02/highlight-entire-row-rule.png)

You can use **formula based** conditional formatting rules for this.

1.  Select all your data
2.  Go to “new rule” on conditional formatting
3.  Set the rule type to **Use a formula to determine which cells to format**
4.  Type the rule as depicted below
5.  Set formatting options
6.  Now your row will be highlighted

![cf rule for highlighting entire row](https://chandoo.org/wp/wp-content/uploads/2021/02/cf-rule-for-highlighting-entire-row.png)

Bonus trick: How to highlight entire column? Change the reference style to lock-in the column in your CF rule to highlight entire column.  
For ex: D$5>2000 would highlight entire column.

Trick 3 - Advanced Zebra Shading
--------------------------------

Zebra shading (highlighting every other row) is proven technique to improve readability of your data. But Excel doesn’t have built-in zebra shading options for non-tabular data. You can use Conditional Formatting rules to **add the zebra shading easily**. Below is an example of **advanced zebra shading.**

![zebra lines with conditional formatting](https://chandoo.org/wp/wp-content/uploads/2021/02/zebra-lines-with-conditional-formatting.png)

**To add regular zebra shading (highlight alternative rows):**

1.  Select your data and add a new formula based CF rule.
2.  Type the rule as =ISEVEN(ROW())
3.  Set the formatting you want
4.  Apply the rule.

**Rule for advanced zebra shading:**

1.  Use the rule like this to highlight 5 rows at a time.
2.  \=ISODD(QUOTIENT(ROW()-ROW(header\_row)-1, 5))

Change the header\_row to **absolute reference** of header row cell.

Trick 4 - Highlight dates in next week
--------------------------------------

Imagine you are tracking a project plan in Excel. you have a bunch of due dates and want to instantly see which items are due _**next week.**_ You can use **relative dates** feature of conditional formatting rules to do just that.

![relative dates cf rule](https://chandoo.org/wp/wp-content/uploads/2021/02/relative-dates-cf-rule.png)

1.  Select the column with dates
2.  Go to conditional formatting > highlight cells
3.  Click on “a date occurring” option
4.  Select the period you want
5.  Apply the format you need
6.  Done.

Bonus trick: Highlight full row with formula rules Use **formula based rule** to highlight entire row easily.  
For ex. the rule =AND($D4>TODAY(), $D4<=TODAY()+7) will highlight any rows where column D has a date in next 7 days.

Trick 5 - Databars & Icons in the same cell
-------------------------------------------

Databars are good. Icons are good. _Together they are great_.

Ever wanted to show an additional icon when databar reaches the goal (say 100%)? 

![databar and icon in the same cell](https://chandoo.org/wp/wp-content/uploads/2021/02/databar-and-icon-in-the-same-cell.png)

To get them in the same cell,

1.  Add databar rule 
2.  Set the maximum value of “databar” to twice the target. So 2 for 100%.
3.  Add icon rule as well. Set the icon to show only when value is 100% and **no cell icon** for other cases.
4.  Now, you get both databar and icon in the cell.

Download Example Workbook
-------------------------

Click below button to download the example workbook with all 5 techniques. Examine the rules or use sample data to replicate the ideas.

[Download Example Workbook](https://chandoo.org/wp/wp-content/uploads/2021/02/5-cf-tricks-2021.xlsx)

5 Tricks - Video
----------------

If you prefer to see a video with these tricks explained, check it out below or [watch it on my YouTube channel](https://youtu.be/gpbwBxTRYRM)
.

More Conditional Formatting Tricks
----------------------------------

[![on / off conditional formatting in dashboards - tip](https://chandoo.org/wp/wp-content/uploads/2016/07/toggle-cf-tip.gif)](https://chandoo.org/wp/on-off-conditional-formatting/)
Conditional formatting is a must have for any advanced Excel user. Please learn more about this powerful feature by reading these examples.

*   [On / off conditional formatting with this simple trick](https://chandoo.org/wp/on-off-conditional-formatting/)
    
*   [Linking slicers & conditional formatting for WOW factor](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/)
    
*   [Advanced tips on conditional formatting icons](https://chandoo.org/wp/green-down-arrow-cf-trick/)
    
*   more on [conditional formatting](https://chandoo.org/wp/tag/conditional-formatting)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/#respond)
    
*   Tagged under [conditional formatting dates](https://chandoo.org/wp/tag/conditional-formatting-dates/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [zebra lines](https://chandoo.org/wp/tag/zebra-lines/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMerry Christmas & Happy New Year 2021](https://chandoo.org/wp/holiday-card-2020/)

[NextDynamic Arrays Live Masterclass – ReplayNext](https://chandoo.org/wp/excel-da-free-live-event/)

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
    
    [Reply](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ