# Interactive Pivot Table Calendar & Chart in Excel! » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-pivot-calendar

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Interactive Pivot Table Calendar & Chart in Excel!
==================================================

*   Last updated on September 12, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Can we make a calendar using Pivot Tables?!?**_

Of course we can. Today let us learn a simple technique to create calendar style reports using [Pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
.

### Thanks to Rob for inspiration

Before making any progress, let me thank Rob from PowerPivotPro for the inspiration. Recently he wrote an [article explaining how to use PowerPivot & DAX formulas to create calendar charts in Excel](http://www.powerpivotpro.com/2012/08/introducing-the-calendar-chart/)
. I applied similar technique to Pivot tables.

### Demo of Pivot Calendar

See a quick demo of pivot calendar chart before learning how to do this.

![Excel Pivot Table Calender - Demo & Explanation](https://img.chandoo.org/pivot/interactive-excel-pivot-calendar-demo.gif "Excel Pivot Table Calender - Demo & Explanation")

Creating a Pivot Table Calendar
-------------------------------

### Step 1: Set up an entire year of dates in a list

Lets assume, we want to make the calendar for year 2012. So write that in a cell (G3). Now, in a range of 366 cells, generate all the dates for the year (2012) using simple formulas.

*   First date will be =DATE(G3,1,1)
*   Next 365 dates will be previous date + 1

![Pivot calendar - Data & formulas to generate a pivot calendar](https://img.chandoo.org/pivot/pivot-calendar-data-and-formulas.png "Pivot calendar - Data & formulas to generate a pivot calendar")

### Step 2: Calculate Day, Month, Year and Weekday

Using DAY(), MONTH(), YEAR(), WEEKDAY() calculate the day, month, year and weekday for each of the 366 days.

### Step 3: Determine the week number in a month

Now comes the tricky part. We need to find out which row each date should be displayed. First take a look at this illustration.

![Pivot Calendar row number calculation explained](https://img.chandoo.org/pivot/pivot-calendar-row-number-calculation-explained.png "Pivot Calendar row number calculation explained")

The logic for calculating row numbers is very simple:

*   First day of a month is always in row number 1.
*   If a day is not Sunday, we just use previous row number
*   On Sundays, we just increment the previous row number and use it.

All of this can be expressed in a simple IF formula =IF(D7=D6,IF(F7=1,G6+1,G6),1)

*   D7 contains this month, D6 is previous day’s month
*   F7 contains weekday, will be 1 for Sunday and 7 for Saturday
*   G6 contains previous row number (weeknum)

### Step 4: Dealing with Leap years

So far we are good, except for a minor glitch. Certain years have 366 days (for example 2012) while others dont. That means, depending the year, we need to either use 365 rows or 366 rows of our data while generating the pivot report. To do this, we create a named range _tblDates_ that refers to below formula:

\=IF(Calcs!$D$3,Calcs!$B$5:$G$371,Calcs!$B$5:$G$370)

_Note:_ D3 is TRUE when an year is leap year.

### Step 5: Create pivot table that shows calendar

Now, we need to create a pivot table from the range _tblDates_.

Set up your pivot table like this:

![Setup Pivot Table Calendar - steps](https://img.chandoo.org/pivot/setup-calendar-pivot-table-like-this.png "Setup Pivot Table Calendar - steps")

### Step 6: Add a slicer

To enable users to select a particular month interactively, just [add a slicer](http://chandoo.org/wp/2010/05/17/what-is-new-in-excel-2010/)
 on months. For this,

1.  Select any cell in the pivot table and go to Options Ribbon > Insert Slicer
2.  Select Month as field to insert a slicer.
3.  Adjust slicer properties to show items in 6 columns (Slicer Options Ribbon > Columns)
4.  Done!

At this point, you can interactively select a month & see the corresponding calendar.

Related: [More examples on Slicers](http://chandoo.org/wp/tag/slicers/)

### Further Enhancements

Now that the basic Pivot Calendar is ready, try these ideas:

*   **Use a spin button / slider control to interactively adjust the year**. Remember, when you do this, you need to [refresh the pivot table in background using a simple macro](http://chandoo.org/wp/2011/09/19/refresh-all-pivot-tables/)
    .
*   **Adjust week start to Monday:** Likewise, you can modify your formulas to adjust weekstart to Monday or any other day you fancy.

Using Pivot Calendar as a Chart
-------------------------------

Of course, having a mere pivot calendar is not much fun. But you can apply this idea to create a calendar chart. See this:

### Calendar Chart Demo:

![Calendar chart using Pivot Tables & Conditional Formatting - Demo](https://img.chandoo.org/pivot/calendar-chart-in-excel-demo.gif "Calendar chart using Pivot Tables & Conditional Formatting - Demo")

### How to create this Calendar chart?

To keep things simple, lets understand how to create this chart with just one metric – Employee productivity.

*   Once the pivot calendar is ready, we add extra rows between each line in the calendar.  
    ![Calendar Chart - add empty rows so that we can show the color scales](https://img.chandoo.org/pivot/calendar-chart-empty.png "Calendar Chart - add empty rows so that we can show the color scales")
*   Now, lets say, we have our employee productivity details listed by date in a table.
*   Then, using lookup formulas, we fetch productivity for each day in the cell below.
*   Once all the values are fetched, just select all these cells and add conditional formatting > color scale to them.
*   Format the color scale settings so that you get desired colors.
*   And you are done!

_[More on Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
_

Video Explaining Pivot Calendar & Chart
---------------------------------------

Like this concept? Watch below video to understand how the whole thing is made.

\[[watch this video on our youtube channel](http://www.youtube.com/watch?v=z6bsOGztR1M&list=UU8uU_wruBMHeeRma49dtZKA&index=1&feature=plcp)\
\]

Download Pivot Calendar Template
--------------------------------

[**Click here to download pivot calendar & calendar chart templates**](https://img.chandoo.org/d/pivot-calendar-v1.xlsm)
. Play with them. Plug your own values and see what happens.

PS: You need Excel 2010 to view this file. Please enable macros to get full effect.

Do you like Pivot Calendar Idea?
--------------------------------

**I am very excited to try this out in a client project sometime soon.** I think a set up like this can be used when analyzing monthly data like employee attendance, vacations, productivity, shipments, meeting schedules, project milestones etc. Since such data is represented in calendar format in real life, your audience would find calendar metaphor easy to understand. That said, any data like KPI trends, sales, visits, calls etc. should always be represented as a line /bar charts rather than calendar charts.This way, we can spot trends quickly and understand data better.

**What about you?** Do you like this idea? Are you planning to use a pivot calendar / calendar chart sometime in future? _**Please share your thoughts using comments.**_

### Calendars & Similar ideas:

Please go thru below links to learn more about calendars & visualizing data:

*   [Project Milestone Chart template](http://chandoo.org/wp/2009/07/09/project-milestones-in-timeline/)
    
*   [Perpetual Calendar in Excel – Template](http://chandoo.org/wp/2011/12/27/download-free-2012-calendar/)
    
*   [Employee Shift Tracker Template](http://chandoo.org/wp/2011/08/01/shift-calendar-excel-template/)
    
*   [Visualizing Data Around the clock – Charting Technique](http://chandoo.org/wp/2008/08/14/plot-time-series-data-excel/)
    
*   _More on [Pivot Tables](http://chandoo.org/wp/excel-pivot-tables/)
    , [Slicers](http://chandoo.org/wp/tag/slicers/)
     & [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    _

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [49 Comments](https://chandoo.org/wp/interactive-pivot-calendar/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-pivot-calendar/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [calendar](https://chandoo.org/wp/tag/calendar/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pivot](https://chandoo.org/wp/tag/pivot/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [tables](https://chandoo.org/wp/tag/tables/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousA Spreadsheet walks in to a bar … \[open mic\]](https://chandoo.org/wp/spreadsheet-walks-into-bar/)

[NextHow many values are common in 2 lists? \[homework\]Next](https://chandoo.org/wp/count-of-common-values-in-2-lists/)

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
    
    [Reply](https://chandoo.org/wp/interactive-pivot-calendar/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-pivot-calendar/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-pivot-calendar/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ