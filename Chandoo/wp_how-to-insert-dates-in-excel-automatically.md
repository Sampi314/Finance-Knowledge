# How to insert dates in Excel automatically » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to insert dates in Excel automatically
==========================================

*   Last updated on May 7, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Ever wanted to get a set of dates, but don’t want to manually type? Here are three ways to insert dates in Excel automatically.

Option1: Enter a start date and Drag down
-----------------------------------------

This is the easiest option if you just want a handful of dates. Just type in your starting date in a cell. Click in the bottom right corner of cell and drag down to get the next consecutive dates automatically.

Here is a quick demo of how to do this:

![automatically insert dates in Excel by dragging](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)

### Insert just weekdays only

While dragging the dates, you can ask Excel to just insert weekdays only. This is helpful for creating dates for a project tracker or planner or other kinds of spreadsheets. To do this, after dragging your dates, click on the “options” button that appears at the bottom and select “Fill Weekdays Only” option.

See this demo:

![Filling weekdays only with Excel dates\
](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-38-28.gif)

### Fill Dates in Months

You can also fill dates by Months. For this, just type the first date, drag down and use the “options” button to select “Fill Months” option. See this demo:

![Filling Months only - Excel dates\
](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-41-23.gif)

### Automatic PayDays (or any other dates really!)

We can use the “dragging” mechanism to fill any kind of arbitrary dates too. Say, you want to see all the Pay Days in 2025. Type in the very first Pay Day (first Wednesday of the calendar year for example) and then, in the cell underneath, write the formula =cellabove+14 (replace cellabove with the actual address of the cell). Then drag this new cell down as far as you want.

See this quick demo:

![How to insert all paydays in Excel automtically](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-44-36.gif)

Option 2: Using the “Fill Series” Secret Menu
---------------------------------------------

Excel also offers a fairly powerful and easy way to fill dates if you want to get a large series of dates for a work project or spreadsheet. This is called “Fill Series” menu. This menu is hidden (buried really) but super helpful. Here is the step by step process:

1.  Type the very first date of your series of dates in a cell.
2.  Select a range big enough for all your dates. Tip: If you have a large series of dates to fill, just select all the cells in the column until end.
3.  Press the keyboard shortcut sequence **`ALT H FI S`** or Go to File Ribbon > Fill > Fill Series button
4.  Select “Date” and specify the “date unit” from the choices – Day, Weekday, Month or Year.
5.  Enter the “step value” and “stop value” (tip: Use Step Value of 7 to get days filled by week, 14 for fortnight)
6.  Click “OK” to see the magic. The dates are filled by Excel automatically.

See this quick GIF to understand the whole process.

![Using "Fill Series" to fill dates in Excel automatically until a stop date](https://chandoo.org/wp/wp-content/uploads/2025/05/how-to-use-fill-series-to-get-any-number-of-dates-in-excel-automatically.gif)

Related: [Learn about fill-series option in Excel](https://support.microsoft.com/en-us/office/fill-data-automatically-in-worksheet-cells-74e31bdd-d993-45da-aa82-35a236c5b5db)

Option 3: Using SEQUENCE Formula
--------------------------------

This one is for hardcore Excel fans and people who love to automate things. We can use the “new” SEQUENCE function of Excel to auto generate dates from any starting point until any end point. The formula is really easy to use and offers a ton of flexibility when it comes to building date trackers, project sheets or even financial models.

Let me share two simple yet powerful examples:

### SEQUENCE Dates Example 1: All Dates in Year 2025

To generate all the dates in Year 2025, go to an empty cell and type the below formula.

    =  SEQUENCE(365,, DATE(2025,1,1))

![using sequence function in excel to get automatic dates for year 2025](https://chandoo.org/wp/wp-content/uploads/2025/05/using-sequence-function-in-excel-to-get-automatic-dates.gif)

**Syntax of SEQUENCE to get dates automatically**  
  
`**=SEQUENCE(number of days,,starting date,** _optional step value_**)**`  
  
Tip: Use the step value of 14 to generate dates by fortnight.

### Working Days only – SEQUENCE Example 2

Let’s say for an upcoming project you want to list all the working days only. But you don’t know when the project starts. So you want to keep the “starting date” flexible and generate next “n” working days.

Imagine the start date of the project in cell C4 and number of working days in C5.

We can use below SEQUENCE function to get all the working days in the project.

    =WORKDAY.INTL(C4,SEQUENCE(C5))

![List all working days only with Excel SEQUENCE function](https://chandoo.org/wp/wp-content/uploads/2025/05/list-of-working-days-only-with-sequence-function-in-excel.gif)

**Bonus Tip: How to Set “Custom” Weekend Types**  
  
We can use WORKDAY.INTL function to tell Excel when your weekend is. For example if your weekend is “Friday & Saturday”, you can use below syntax:  
`**=WORKDAY.INTL(C4,SEQUENCE(C5),7)**`  
Here 7 stands for Friday & Saturday weekend.

### Why I love SEQUENCE() approach

Of the 3 techniques outlined here, SEQUENCE() based approach is my favorite.

*   **Flexible:** Many real-world scenarios where I need dates are dynamic. The starting date, end date, step value and what I need (days / weekdays / weeks / months) all change. Using SEQUENCE() I can create a robust yet flexible auto listing of dates for my workbooks.
*   **Can be linked to other formulas:** As SEQUENCE generates a dynamic _spill range,_ I can use # to access the range and build other scalable and flexible formulas. For example, if I want to calculate depreciation schedules for next “n” months, I can do so easily. When “n” changes, I don’t need to adjust anything as both my dates (from SEQUENCE) and depreciation calculations auto adjust.
*   **Fewer errors:** Spillable formulas like SEQUENCE mean, there is only one formula that produce all the results. This avoids crazy errors like _inconsistent formulas_ or _hard-coded values_.
*   **Faster:** Dynamic formulas like SEQUENCE() are really fast and scale well even when I need to list dates for next century!

Related: [Learn how to use SEQUENCE and other Dynamic Functions in Excel](https://chandoo.org/wp/dynamic-array-functions/)

### Take Caution when using SEQUENCE()

*   **SEQUENCE function doesn’t format the dates.** So you must format the cells after (or beforehand) to see the correct date format. Else Excel will list the dates as 45658, 45659 for 1-Jan-2025, 2-Jan-2025 etc.
*   **SPILL Errors:** As SEQUENCE will _dynamically fill the cells_ if your spreadsheet doesn’t have enough space for the SEQUENCE() to fill all dates, it will throw SPILL error.
*   **Can’t be used in Excel Tables:** SEQUENCE and other dynamic functions don’t work inside Excel tables. [Read this page for more information and possible fixes](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/)
    .
*   **Need Excel 365 or Excel on Web:** To use SEQUENCE function, you need Excel 365 or Excel on the Web as this is a new functionality and not supported in older versions of Excel.

Working with Dates in Excel – More Tips & Tricks
------------------------------------------------

Dates are integral part of any spreadsheet and data analysis scenario. Please refer to below pages and resources to learn more about important Date functions and tricks.

[![2025 Calendar Excel Template](https://chandoo.org/wp/wp-content/uploads/2024/12/SNAG-3923.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2025/)

*   [Working With Date & Time values in Excel – A quick primer](https://chandoo.org/wp/date-time-tips-ms-excel/)
    
*   [Date Calculation Tips](https://chandoo.org/wp/excel-date-time-tips/)
     (future / past dates and times made easy)
*   [Using Power Query to auto-generate Dates](https://chandoo.org/wp/power-query-calendar-table-best-method/)
    
*   [Free 2025 Calendar & Planner Template (uses SEQUENCE)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2025/)
    
*   [Calculate difference between two dates](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/)
    
*   [Highlight Due Dates in Excel automatically](https://chandoo.org/wp/highlight-due-dates-excel/)
    
*   [3 Powerful & Essential Date functions in Excel](https://youtu.be/NIvTVKZqmM0)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/#respond)
    
*   Tagged under [auto fill](https://chandoo.org/wp/tag/auto-fill/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sequence](https://chandoo.org/wp/tag/sequence/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to create SVG DAX Measures in Power BI (Easy, step-by-step Tutorial with Sample File)](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/)

[NextExcel IF Statement Two ConditionsNext](https://chandoo.org/wp/excel-if-statement-two-conditions/)

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
    
    [Reply](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ