# How to calculate WEEKNUMBER in Month / Quarter / Year with Excel?

**Source:** https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to calculate WEEKNUMBER in Month / Quarter / Year with Excel?
=================================================================

*   Last updated on August 20, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Week number in a month or quarter or year with excel formulas](https://chandoo.org/wp/wp-content/uploads/2024/08/SNAG-3687.png)

Let’s say you have daily data and your boss wants to see the trends by week of month or week of quarter? How do you calculate the week number of month or quarter? In this article, let me explain the logic and formulas we can use Excel for this.

Why calculate week in month or quarter?
---------------------------------------

Calculating “week of month” or “week of quarter” let’s us see trends by week in across months or quarters. Answering business questions like,

*   How many customers we had in first of week January vs. first week of February?
*   What are the total reservations in first 4 weeks of Q1 vs. first 4 weeks of Q3?
*   Cumulative weekly totals for March vs. June

is easier when you have the week of month and week of quarter available in your data.

Step 1: Calculate the WEEKNUM in year
-------------------------------------

![my data format](https://chandoo.org/wp/wp-content/uploads/2024/08/Snag_5672404c.png)

Before we can calculate the weeknum in a month or quarter, we need to do two other important calculations. The first one of them is WEEKNUM in year.

Add a column adjacent to your data and use the below formula to calculate the weeknumber in year.

    =WEEKNUM(B4,2)

This assumes your date is in the cell B4 and your week begins on Monday. If you want to do the analysis from SUNDAY start, just use =WEEKDAY(B4)

Step 2: Calculate the MONTH number
----------------------------------

Our next formula is to figure out which month we are in. Add another column adjacent to your data and use this formula.

    =MONTH(B4)

At this stage your data should look like this:

![Data with week and month number calculations](https://chandoo.org/wp/wp-content/uploads/2024/08/SNAG-3688.png)

Step 3: Calculate Week in Month
-------------------------------

Now that we know the “week in year” and “month number”, we can easily calculate the week in month using below formula.

    =D4-WEEKNUM(DATE(YEAR(B4),E4,1),2)+1

### How this “week in month” formula works?

*   D4 has the weeknumber in year
*   E4 has the month number
*   DATE(YEAR(B4),E4,1) tells us the first date of the month (for example, all dates in JAN 2024 will have this as 1-Jan-2024)
*   WEEKNUM(DATE(YEAR(B4),E4,1),2) will give us the weeknumber for that date (with Monday start)
*   D4-WEEKNUM(DATE(YEAR(B4),E4,1),2)+1 finally tells us the weeknumber of the month (we need to add +1 so that the first week of month will be 1 instead of 0)

\[Optional\] Step 4: Formula for Week in Quarter
------------------------------------------------

If you need to calculate the “Week in Quarter” for some analysis, you can use the below formula to do that.

    =D4-WEEKNUM(DATE(YEAR(B4),INT((E4-1)/3)*3+1,1),2)+1

### How this “week in quarter” formula works?

*   D4 has the weeknumber in year
*   E4 has the month number
*   INT((E4-1)/3)\*3+1 calculates the first month of the quarter (so months 1,2,3 ? 1, 4,5,6 ? 4 … )
*   DATE(YEAR(B4),INT((E4-1)/3)\*3+1,1) tells us the first date of the quarter (for example, all dates in JAN, FEB, MAR 2024 will have this as 1-Jan-2024)
*   WEEKNUM(DATE(YEAR(B4),INT((E4-1)/3)\*3+1,1),2) will give us the weeknumber for that date (with Monday start)
*   D4-WEEKNUM(DATE(YEAR(B4),INT((E4-1)/3)\*3+1,1),2)+1 finally tells us the weeknumber of the quarter (we need to add +1 so that the first week of quarter will be 1 instead of 0)

What if I want Sunday Week Start?
---------------------------------

If your week starts on Sunday, you can use the below formulas instead.

    'For Week in year 
    =WEEKNUM(B4)
    
    'For Month number
    =MONTH(B4)
    
    'For week in month
    =D4-WEEKNUM(DATE(YEAR(B4),E4,1))+1
    
    'For week in quarter
    =D4-WEEKNUM(DATE(YEAR(B4),INT((E4-1)/3)*3+1,1))+1

### For weeks beginning on other days (such as Friday start)

You just need to pass the type of week start to the WEEKNUM() function. Refer to below table to find what you need to use.

![weeknumber options](https://chandoo.org/wp/wp-content/uploads/2024/08/SNAG-3689.png)

Download Sample File with Weeknumber Formulas
---------------------------------------------

If you are having trouble implementing the formulas, **[refer to free example workbook](https://chandoo.org/wp/wp-content/uploads/2024/08/week-number-in-month.xlsx)
**. It has all the formulas for,

*   Calculating week number in year
*   Month number
*   Week of month
*   Week of quarter

In conclusion…
--------------

Calculating “week of month” and “week of quarter” is relatively simple and easy process with Excel. Once you have the values in your data, you can use them to better understand the trends across months or quarters. If you have the data in a table, then applying and maintaining these formulas is easy too, as Excel tables auto-extend the formulas for all cells.

Few additional tips to take this idea further:

*   **Integrate these calculations into Power Query:** If you are bringing external data into Excel through Power Query, try adding these columns with Power Query “Add column” feature. [Learn more about Power Query here](https://chandoo.org/wp/power-query-tutorial/)
    .
*   **Use a separate calendar table:** If you have too many rows of transactional data (like tickets or sales), then instead of calculating the week number for every row, use a calendar table and do the calculations there. After that use “data modeling” feature of Excel to link calendar table to your transactional data. This way you can combine data from both tables in your pivot reports. Learn more about [calendar tables](https://chandoo.org/wp/power-query-calendar-table-best-method/)
     and [data modeling feature](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    .

Other ways to work with dates
-----------------------------

Please refer to these tutorials and examples to solve other date problems in Excel.

[![](https://chandoo.org/wp/wp-content/uploads/2020/05/highlight-overdue-items-in-excel.png)](https://chandoo.org/wp/highlight-due-dates-excel/)

*   [Calculate time between two dates in years, months or days](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/)
    
*   [Highlight due dates in Excel](https://chandoo.org/wp/highlight-due-dates-excel/)
    
*   [Find first and last date of something in pivot tables](https://chandoo.org/wp/find-first-last-date-of-a-sale-using-pivot-tables-quick-tip/)
    
*   [Sum of values between two dates](https://chandoo.org/wp/sum-between-2-dates/)
    
*   [_More tips on Date & Time values in Excel_](https://chandoo.org/wp/tag/date-and-time/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quarter](https://chandoo.org/wp/tag/quarter/)
    , [weeknum](https://chandoo.org/wp/tag/weeknum-2/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousAutomatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[NextFREE Calendar & Planner Excel Template for 2025Next](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2025/)

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
    
    [Reply](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ