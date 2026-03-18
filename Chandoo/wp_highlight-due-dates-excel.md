# How to highlight overdue items, coming up and completed in Excel? » Conditional Formatting » Chandoo.org

**Source:** https://chandoo.org/wp/highlight-due-dates-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Highlight due dates in Excel – Show items due, overdue and completed in different colors
========================================================================================

*   Last updated on May 18, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Congratulations to you if your job does not involve dead lines._ For the rest of us, deadlines are the sole motivation for working (barring free internet & the coffee machine in 2nd floor, of course). So today, lets talk about a very familiar problem.

**_How to highlight overdue items in Excel?_**

The item can be an invoice, a to do activity, a project or anything. Here is an example of overdue, upcoming activities highlighted.

![Highlight overdue items in Excel - Show items due, overdue and completed in different colors](https://chandoo.org/wp/wp-content/uploads/2020/05/highlight-overdue-items-in-excel.png)

highlight-overdue-items-in-excel

The problem – Highlight due dates in Excel
------------------------------------------

Lets say you work at Awesome inc. and you have list of to-do items as shown below.

![sample data for highlighting overdue items](https://chandoo.org/wp/wp-content/uploads/2020/05/sample-data-overdue-items.png)

sample-data-overdue-items

And your problem is,

*   Highlight items & due dates, subject to these conditions  
      
    ![Criteria for highlighting - highlight if due](https://chandoo.org/wp/wp-content/uploads/2020/05/rules-for-highlighting-due-items.png "Criteria for highlighting - highlight if due")
*   And of course start working on the items that are due

The Solution – Conditional Formatting
-------------------------------------

As you can guess, highlighting the due items is easier than _actually_ doing them. First lets look at the solution and then learn why it works.

**Lets assume that,**

*   The data is in the range – B6:D15, with Items (column B), Due date (C) and Completed?(D)

![sample-data-overdue-items](https://chandoo.org/wp/wp-content/uploads/2020/05/sample-data-overdue-items.png "Highlight if due - data")

How to apply conditional formatting rules
-----------------------------------------

We need to apply 3 rules. Follow below steps:

### Highlight overdue items:

![Conditional formatting rule for highlighting overdue items](https://chandoo.org/wp/wp-content/uploads/2020/05/conditional-formatting-rule-for-overdue-items.png)

conditional-formatting-rule-for-overdue-items

1.  Select the entire range (B6:D15) and from home ribbon select [conditional formatting](https://chandoo.org/wp/excel-conditional-formatting-basics/)
    
2.  Click on New rule
3.  Select the rule type as “use a formula…”
4.  Write =AND($C6<=TODAY(),$D6<>”Yes”)
5.  And set fill color to red & font color to white.

### Highlight upcoming items:

![Rule for upcoming activities or items in green color](https://chandoo.org/wp/wp-content/uploads/2020/05/conditional-formatting-rule-for-upcoming-tasks.png)

conditional-formatting-rule-for-upcoming-tasks

1.  Add one more “use a formula…” rule
2.  Write =AND(MEDIAN(TODAY()+1,$C6,TODAY()+7)=$C6,$D6<>”Yes”)
3.  And set fill color to green.

### Completed items rule:

![Highlighting completed items in a different color - highlight if due](https://img.chandoo.org/cf/rule-for-completed-items-highlight-if-due.png "Highlighting completed items in a different color - highlight if due")

1.  Add another “use a formula…” rule
2.  Now write =$D6=”Yes”
3.  And set font color to dull gray from formatting button.  
    

**Now, the items will be highlighted based on the current date (TODAY) and change colors as you make progress.**

Why does it work? – Explanation
-------------------------------

At this point you may have 2 burning questions.

1.  Why does this work?
2.  How the heck am I supposed to _ship 100 units of smile._

Lets talk about the solution & understand why it works.

**Understanding the highlighting conditions**

We have 3 conditions in our highlight table (shown above).

*   If done show in dull gray color
*   Not done & due in next 7 days show in orange color fill.
*   If not done & already due show in red fill, white color

**Rule for completed items:**

The first condition is easy to check. We just see if a todo item is completed and then highlight the whole row dull gray color. So we write =$D6=”Yes” as the condition. We use $D6 (not D6) because we want Excel to look at column D (completed?) even when we are highlighting other columns (B – Item, C – Due date).

**If not done & due in next week:**

This is tricky. We need to check,

If completed is not yes

AND

If due date is with in next week

So we start with an AND formula. We write =AND($D6<>”Yes”

Then to check if due date is in next week, [we use MEDIAN formula](https://chandoo.org/wp/between-formula-excel/)
, like this MEDIAN(TODAY()+1,$C6,TODAY()+7)

So the condition becomes =AND(MEDIAN(TODAY()+1,$C6,TODAY()+7)=$C6,$D6<>”Yes”)

![conditional-formatting-rule-for-upcoming-tasks](https://chandoo.org/wp/wp-content/uploads/2020/05/conditional-formatting-rule-for-upcoming-tasks.png)

**If already due:**

This is another simple AND formula =AND($C6<=TODAY(),$D6<>”Yes”)

![conditional-formatting-rule-for-overdue-items](https://chandoo.org/wp/wp-content/uploads/2020/05/conditional-formatting-rule-for-overdue-items.png)

_**Remember:**_

We need to use $D6 & $C6 (instead of D6, C6) because we want Excel to check Completed & Due date columns. By removing the $ Excel will check relative columns and the conditions would not work!

More: [Using relative vs. absolute references in Excel formulas](https://chandoo.org/wp/relative-absolute-references-in-formulas/)

Now that we understand how this works, give me a big smile. And repeat that 99 more times & you know how to ship 100 smiles 🙂

Highlight overdue items – Video
-------------------------------

If you are still confused about the conditional formatting rules for highlighting overdue items, check out this video. Watch it below or [see it on my YouTube channel](https://www.youtube.com/watch?v=mAOAAQoN4h8)
.

Download Example File
---------------------

[**Click here to download example file**](https://chandoo.org/wp/wp-content/uploads/2020/05/highlight-if-due.xlsx)
. Break it apart, play with it to understand the whole **_highlight if due_** thing.

_Note: I use random formulas to generate due dates & completed values._ Press F9 to get fresh set of dates. Start typing your own values to remove formulas.

How do you handle dead-lines?
-----------------------------

**Do you use conditional formatting to see which items are due?** I use conditional formatting for this all the time. What techniques you use? Is your dead-line criteria very different than shown above? Please share your tips & ideas with us using comments. I would love to learn from you.

Using Conditional Formatting & Dates – More Examples
----------------------------------------------------

Here are a few useful articles if you use Excel to track to do items & reminders.

*   [Conditional formatting & Dates – an introduction](http://chandoo.org/wp/conditional-formatting-dates/)
     – Must read
*   [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/)
     – a complete overview
*   [Another ovredue items example](https://chandoo.org/wp/overdue-items/)
     – activities by employee

[![](https://chandoo.org/img/trackers/employee-shift-calendar-template-demo.gif)](https://chandoo.org/wp/shift-calendar-excel-template/)

*   [Christmas shopping list in Excel](http://chandoo.org/wp/christmas-shopping-list-template/)
    : conditional formatting to track budgets, bought items etc.
*   [Employee shift calendar in Excel:](http://chandoo.org/wp/shift-calendar-excel-template/)
     Using dates, shift data to show busy & dull times.
*   [Annual goals tracker](http://chandoo.org/wp/employee-goal-tracker-excel/)
    : Track goals by % completed

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [54 Comments](https://chandoo.org/wp/highlight-due-dates-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/highlight-due-dates-excel/#respond)
    
*   Tagged under [and()](https://chandoo.org/wp/tag/and/)
    , [conditional formatting dates](https://chandoo.org/wp/tag/conditional-formatting-dates/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [median() formula](https://chandoo.org/wp/tag/median-formula/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMultiple Find Replace with Power Query List.Accumulate()](https://chandoo.org/wp/multiple-find-replace-list-accumulate/)

[NextCelebrating 50k Subscribers on YouTube + Give awayNext](https://chandoo.org/wp/50k-give-away/)

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
    
    [Reply](https://chandoo.org/wp/highlight-due-dates-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/highlight-due-dates-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/highlight-due-dates-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ