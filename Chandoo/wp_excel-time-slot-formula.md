# Figure out slot from given time [quick tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-time-slot-formula

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

Figure out slot from given time \[quick tip\]
=============================================

*   Last updated on April 19, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Here is an interesting scenario.

Let’s say you are looking at a time, like 9:42 AM and want to know which 15 minute slot it fits into. The answer is 9:30 – 9:45. But how would you get this answer thru Excel formulas?

![timeslot-from-time-excel-formulas](https://chandoo.org/wp/wp-content/uploads/2016/04/timeslot-from-time-excel-formulas.png)

### Excel formula to find slot from time:

Assuming A1 contains the input time, here is one formula that tells you the time slot.

\=TEXT(TIME(HOUR(A1),INT(MINUTE(A1)/15)\*15,0),”hh:mm”)&” – “&TEXT(TIME(HOUR(A1),(INT(MINUTE(A1)/15)+1)\*15,0),”hh:mm”)

Whoa!, that’s long. Let’s examine the inner workings of this beast.

**Logic:** We need to figure out both lower & upper boundaries of fifteen minute slot for time in A1. The lower boundary is quotient of A1/15 minutes multiplied by 15. For example, 09:42’s lower boundary is 09:30. The upper boundary is lower boundary + 15 minutes.

**Implementation:**

**INT(MINUTE(A1)/15) \* 15 portion:** this part of the formula tells us the minutes. We extract the minute part of A1 (using MINUTE(A1)) and divide it with 15. We then take only the integer portion of this division and multiply that with 15 again. This gives us the _minute portion_ of lower boundary of our time slot.

**TIME(HOUR(A1), INT(..)\*15, 0) portion:** We then create a time value using the TIME formula by using the same hour as A1, minutes from lower boundary calculation using the INT(…)\* 15  and 0 as seconds.

**TEXT(TIME(…), “hh:mm”) portion:** This will convert the time value to text formatted as hh:mm.

So far we have constructed the lower boundary of time slot. The _upper boundary_ part of the formula is similar with one minor change. Go figure it out.

### How to find 1 hour time slot?

Let’s say you want to find the time slot on hourly basis, then what?

Below formula does the job.

\=HOUR(A1)&”:00 – ” & (HOUR(A1)+1) & “:00”

### What if your time slots are not uniformly spaced?

The above approaches work fine as long as your time slots are uniformly spaced (_ie_ 15 minutes, 1 hour, 4 hours or 8 hour apart). What if you have a _unique_ set up? Something like this:

![non-uniform-time-slots-how-to](https://chandoo.org/wp/wp-content/uploads/2016/04/non-uniform-time-slots-how-to.png)

In that case you can use the [**range lookup** method](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
.

Related: read about [pricing tier lookup](http://chandoo.org/wp/2015/12/01/pricing-tier-lookup-formula/)
 too.

So there you go. For more information about working with date & time values in Excel, check out below material.

*   [Convert fractional time to proper time in Excel](http://chandoo.org/wp/2014/08/19/convert-fractional-excel-time-to-hours-minutes-quick-tip/)
    
*   [Find last day of any month with this simple trick](http://chandoo.org/wp/2013/11/21/last-day-of-month-formula/)
    
*   **[42 tips for Excel time travelers](http://chandoo.org/wp/2013/10/17/excel-date-time-tips/)** – Must read!!!
*   [Check if two dates are in same month](http://chandoo.org/wp/2012/11/02/two-dates-in-month-check/)
    
*   More [formulas & tutorials on Excel date & time](http://chandoo.org/wp/tag/date-and-time/)
    

### A challenge for you:

How would you write the 15 minute time slot formula? Can you figure out _other_ ways to calculate it? Please share your formulas in the comments section. _Your time starts now!_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/excel-time-slot-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-time-slot-formula/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [INT()](https://chandoo.org/wp/tag/int/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [lookup](https://chandoo.org/wp/tag/lookup/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [time](https://chandoo.org/wp/tag/time/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

[PrevPreviousAdvanced Interactive Charts using Excel \[Master Class\]](https://chandoo.org/wp/advanced-interactive-charts-using-excel-master-class/)

[NextExcel Tips, Tricks, Cheats & Hacks – Microsoft MVP EditionNext](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/)

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
    
    [Reply](https://chandoo.org/wp/excel-time-slot-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-time-slot-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-time-slot-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ