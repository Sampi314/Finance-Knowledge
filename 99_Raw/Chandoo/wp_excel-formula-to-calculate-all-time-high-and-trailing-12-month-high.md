# Simple Excel Formula to Calculate All-time High, Trailing 12 Month High Values [Quick Tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Simple Excel Formula to Calculate All-time High, Trailing 12 Month High Values \[Quick Tip\]
============================================================================================

*   Last updated on February 10, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is not too sunny here, but I am going to put on my business man hat. At the end of each month, I ask myself if my business (chandoo.org that is) has performed better or worse. One simple way is to look at previous month’s numbers and then I know how good the latest month is.

But thanks to awesome people like you, my business is growing every month. So **mere comparison with previous month’s values is not enough. I would like to know, for eg. if the latest month is,**

*   The best month ever
*   The best month in last 12 months (trailing 12 months)

Now, it would be a shame if I have to find these answers manually. **So I write an Excel formula. That is right!, a formula to tell me if the latest month’s value is all time best, best in last 12 months.**

**![Analyze Sales Values by finding All-time high, trailing 12 month high values - Excel Formulas](https://chandoo.org/img/f/alltime-high-values-excel-formula.png)  
**

### How to write such formulas?

Oh, the formulas are really simple. More so, if you compare it with the effort it takes to make a month all time best in sales (or any other metric).

Assuming we have a bunch of sales numbers by month in the range B6:C30,

### To test for All time high condition:

*   In cell D6, write =C6=MAX($C$6:C6)
*   Drag the formula to fill remaining cells in column D
*   Now you will see a bunch of TRUE and FALSE values. **TRUE** means the corresponding month’s sales is an all time high.

![](https://cache2.chandoo.org/images/icons/tip-icon.png)**Tip:** See how we are using $C$6:C6 in the MAX. This style of referencing is called as mixed cell referencing. By using this, when you fill the formula for remaining months, the range inside MAX grows. Thus for each month we get the maximum sales value thus far. [more »](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)
.

### To test for Trailing 12 month high condition:

*   We will test this condition in column E.
*   In E17 (trailing 12 month high can not be calculated for first 11 months…) write = C17=MAX(C6:C17)
*   Drag the formula to fill remaining cells in column E
*   Now you will see a bunch of TRUE and FALSE values. **TRUE** means the corresponding month’s sales is a  trailing 12 month high.

![](https://cache2.chandoo.org/images/icons/tip-icon.png)**Tip:** The range C6:C17 is relative. Thus when you fill the formula down, it changes to C7:C18, C8:C19… referring to previous 12 months. [more »](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)
.

### Download Example Workbook

I have prepared a simple example file. **[Download](https://img.chandoo.org/d/alltime-high-values-excel-formula.xlsx)
** it to understand these formulas.

### How do you analyze your sales data?

Apart from the above techniques, I also use line charts & trend lines to understand the sales trend. Also, I use pivot tables to segment my sales based on product, customer type, region etc. Since my business is new, I do not have previous year values for many products. But where possible, I compare sales from last month same year to see how well the product has grown / shrunk. I do not set any targets at monthly level as I aim to enjoy the process. So I do not use bullet charts or target vs. actual charts per se.

**What about you?** How do you analyze sales or similar data? What metrics do you use to gauge the performance? **Please share using comments.**

### Resources to Understand Your Sales Data better:

*   [Calculating Moving Average](http://chandoo.org/wp/2009/04/28/calculate-moving-average/)
    
*   [Min-Max Charts – show the trend and range](http://chandoo.org/wp/2008/08/11/min-max-excel-charts/)
    
*   [How I analyze Excel School Sales using Pivot Tables](http://chandoo.org/wp/2010/09/22/analyzing-product-launch-sales/)
    
*   [Sales Dashboards – 32 Examples & Templates](http://chandoo.org/wp/2010/01/04/sales-dashboards/)
    
*   More on [Formulas](http://chandoo.org/wp/tag/formulas/)
    , [Charting](http://chandoo.org/wp/category/visualization/)
     & [Quick Excel Tips](http://chandoo.org/wp/tag/quick-tip/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [9 Comments](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [references](https://chandoo.org/wp/tag/references/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousIntroduction to Project Finance Modeling in Excel](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/)

[NextHow long have you been using Excel? \[poll\]Next](https://chandoo.org/wp/your-excel-age-poll/)

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
    
    [Reply](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ