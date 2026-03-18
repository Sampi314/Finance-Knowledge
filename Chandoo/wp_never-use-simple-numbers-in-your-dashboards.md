# Never use simple numbers in your dashboards (bonus tip: how to fix default conditional formatting) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Never use simple numbers in your dashboards (bonus tip: how to fix default conditional formatting)
==================================================================================================

*   Last updated on July 11, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Pop quiz: What is wrong with below report?**_

![Simple regional sales summary - can you find what is wrong with this?](https://img.chandoo.org/dashboards/simple-regional-summary.png)

At first glance, it looks alright. But if you observe closely, you realize that it is not telling the entire story. Just looking at regional sales numbers, you have not much clue what is going on with them.

_**So how to improve it?**_

1\. Add context
---------------

In order to know whether a number like $120,000 sales in South _is good or bad_, you need to provide some context. For example, if you include previous month sales figures, suddenly $120k is comparable to some other number. This tells a better story than a simple number alone.

![Regional sales summary with last month numbers - tells a better story](https://img.chandoo.org/dashboards/regional-sales-summary-with-last-month-sales-context.png)

You can also try these,

*   Target values
*   Same month last year values
*   YTD, QTD values

2\. Add % Change
----------------

When you have 2 numbers like $120k and $110k in a report, anyone looking at them are going to _mentally calculate the % change from last month to this month._ This is easy for numbers like 120 and 110, but if your numbers are like 36,450 and  43,150 then calculating % change values will take time.

**Why force your audience to do this mental math?** Instead show these %s on the report.

![Show % change values in the report](https://img.chandoo.org/dashboards/percent-change-values-added.png)

3\. Highlight bad numbers
-------------------------

Another way to enhance your report is to highlight poorly performing regions. Since each region is different, comparing sales of one with another is not good. But you can compare % change (from previous month / same month last year / targets etc.) and highlight poorly performing regions. This can be done with [conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
.

So lets go ahead and do it for our report above.

### 3.1 Add conditional formatting

Just select the %change column, go to conditional formatting > icon sets > and choose an arrow icon set that you fancy.

![Add conditional formatting to highlight bad numbers in your reports](https://img.chandoo.org/dashboards/applying-conditional-formatting-icons.png)

### 3.2 The default formatting kinda sucks

![The default conditional formatting is not going to work here.](https://img.chandoo.org/dashboards/conditional-formatting-applied.png)

We are not done yet. If you look at the default icon formatting, it looks in-accurate. We are seeing red colored, down-ward arrows even when there is a positive change. _And, when the % change is negative, we no longer need minus sign (-) because it will be indicated by down arrow._

### 3.3 Fix the conditional formatting icons

Select the cells again, go to home > conditional formatting > manage rules. Select the rule and edit it (you can double click on the rule to edit).

Change the rule type as shown below.

![Edit the conditional formatting icon set rule to fix the icons](https://img.chandoo.org/dashboards/editing-conditional-formatting-rule.png)

### 3.4 Remove the minus sign

Select the %change column once again, go to format cells (ctrl+1) and set the custom formatting code **0%;0%**

This will make sure that even when the percentage is negative, Excel will not show the sign (minus symbol).

_Related: [More on custom cell formatting in Excel](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/)
._

So there you go. A regional sales report that tells better story.

![Finalized regional sales report - this tells a better story.](https://img.chandoo.org/dashboards/final-regional-summary-report.png)

Key ideas to keep in mind
-------------------------

In your reports, try to provide as much context as possible. This can be done by

*   providing comparisons
*   including additional statistics (sum, count, median etc.)
*   indicating the time frame of the report
*   highlighting bad numbers or areas that require attention
*   [giving user a choice to change report criteria](http://chandoo.org/wp/2012/08/02/making-dashboards-interactive/ "Making your dashboards interactive [Dashboard Essentials]")
     (interactive features).

### Do you follow these principles when making reports or dashboards?

I try to observe these ideas in all my dashboards. What about you? Are you using simple numbers in your dashboards?

_Go ahead and tell us how you are making your dashboards better, in comments._

### Analyze data and make reports / dashboards often?

_If your job involves data analysis, reporting & dashboards, then you will love our Excel School program_. In this online course, you will learn how to use Excel to analyze data with formulas & pivot tables, highlight important stuff, create stunning charts & tables, make them interactive and put everything together to weave an informative dashboard & more.

[**Please click here to know more about Excel School program and join us**](http://chandoo.org/wp/excel-school/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [53 Comments](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/#respond)
    
*   Tagged under [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [custom cell formatting](https://chandoo.org/wp/tag/custom-cell-formatting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousWhat do you use Tables for? \[poll\]](https://chandoo.org/wp/what-do-you-use-tables-for/)

[NextFormula Challenge 001 – Return everything from a string after the first block of numbers (Part 1.)Next](https://chandoo.org/wp/formula-challenge-001-1/)

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
    
    [Reply](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ