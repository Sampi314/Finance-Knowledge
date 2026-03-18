# Quick tip: Make a list of numbers (or dates) in Power Query easily » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/quick-tip-make-a-list-of-numbers-or-dates-in-power-query-easily

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Quick tip: Make a list of numbers (or dates) in Power Query easily
==================================================================

*   Last updated on November 13, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Just a quick tip to revive the blog from a month long silence.**_ I am alive and kicking. I have been occupied with a quest to rescue princess & maidens on video game console. Recently we bought SNES classic console from Nintendo and I have been playing Legend of Zelda – a link to past regularly. As it is almost summer, I am also enjoying the beautiful outdoors in Wellington. All this means, little time for blogging. I will try to post a few more times before the end of year.

### Make a list of numbers in a jiffy with Power Query:

We know that in Excel, you can type a few numbers and use the _fill handle_ to fill down (or up etc.) numbers as you want.

But what if you need some numbers in Power Query?

Simple, just type ={1..10} in the Power Query formula bar to get the numbers 1 thru 10. See this in action.

![make a list of numbers in Power Query](https://chandoo.org/wp/wp-content/uploads/2018/11/make-a-list-of-numbers-in-pq.gif)

**What formula bar? I don’t see any:** If your Power Query is devoid of formula bar, just go to view ribbon and slash “Formula bar” option with your master sword. You will now acquire the magical power of formula bar. You can see and edit mysterious M language instructions now.

Oh wait, my numbering needs are a little crazy
----------------------------------------------

Of course they are. You just need to unleash a bottled fairy on those numbers. Or take the easy route and use =List.Numbers() function. Go ahead, it won’t bite you.

### Examples of List.Numbers() in Power Query:

*   **List.Numbers(1,10)**:  Same as {1..10}
*   **List.Numbers(1,10,2)**: You get numbers {1,3,5…,19}  _ie_ first 10 odd numbers
*   **List.Numbers(0,10,2):** Take a guess… what do you think this will do?
*   **List.Numbers(0,100,10):** You get 100 multiples of 10, starting with 0, ending at 990

### Can I get some dates?

You can also get raisins, dried apricots and cranberries, but only on the bulk-food aisle. If you just want dates, as in 13th of November 2018, then you can use **List.Dates() function.**

**Examples of List.Dates():**

Unlike simple numbers and text values, dates & durations need to be typecasted. We use #date, #duration to generate the required format first. Keep that in mind when reading below examples.

*   **List.Dates(#date(2018, 1, 1), 365, #duration(1, 0, 0, 0)):** You get all 365 dates in year 2018, starting with 1 January 2018.
*   **List.Dates(#date(2018, 11, 13), 31, #duration(1, 0, 0, 0)):** You get 31 days from 13th of November 2018.

Try with other numbers in duration to see what happens.

### Last but not least – You get List, not Table

In all these cases, Power Query spits out a list. While it looks like a table, list is different and can ever have only one column. So if you want to do something with the list, you need to convert this to a table. This is a simple matter of spilling magic potion on the list using the List tools > Transform > “To Table” button.

Now that you have a table, you can add columns, sort or do other cool things easily.

### How do you make a bunch of numbers in Power Query?

I use a variation of {1..10} or List.Dates on most of my Power BI files when I need to make up some data.

**What about you?** How do you like this tip? Share your Power Query wins in the comments.

I am off to D&D now – Dinner and dungeon time that is. The seven maidens can’t be saved with Power Query. Tada…

New to Power Query? [Check out this great intro](https://chandoo.org/wp/resources/introduction-to-power-query/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/quick-tip-make-a-list-of-numbers-or-dates-in-power-query-easily/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/quick-tip-make-a-list-of-numbers-or-dates-in-power-query-easily/#respond)
    
*   Tagged under [list.dates](https://chandoo.org/wp/tag/list-dates/)
    , [list.numbers](https://chandoo.org/wp/tag/list-numbers/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousHui’s World ! – An Excel Project of Global Scale.](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/)

[NextElevator problem – Excel homeworkNext](https://chandoo.org/wp/elevator-problem/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ