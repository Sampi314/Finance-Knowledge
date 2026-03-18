# Automatic Rolling Months in Excel, Dynamic Rolling Months in Excel using Formulas

**Source:** https://chandoo.org/wp/rolling-months

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Automatic Rolling Months in Excel \[Formulas\]
==============================================

*   Last updated on April 6, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Often when we are making spreadsheets for forecasting or planning we would like to keep the _**starting month dynamic so that rest of the months in the plan can automatically rolled.**_ Don’t understand? See this example:

![Automatic Rolling Months in Excel](https://chandoo.org/img/f/dynamic-starting-month-demo.gif)

**This type of setup is quite useful as it lets us change the starting month very easily.** We can use such a set up in, for eg. [Gantt Charts](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 to change the project start dates with ease. Today we are going to learn how to set up automatic rolling months in Excel.

To set up such dynamic rolling months in Excel, just follow these simple steps:

### 1: Create a list of all the months

Enter the month names in a bunch of cells (Tip: Just enter the first month name and then click at the bottom right corner of that cell and drag to get all the other month names). Let us call this range as `B5:B16`. If you prefer, name this range as “`lstMonths`“.

### 2: Set up data validation drop down list on the first cell for automatic rolling

Now, let us assume we will use cells `A1:A12` for automatic rolling months. Select `A1` and [set up data validation list](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
 on it (so that users can only enter a valid month in that cell) and use “List” type as validation. See below:

![Excel Data Validation Drop Down List - Example](https://chandoo.org/img/f/datavalidation-list-example.png)

### 3: Now write formulas so that we fetch consecutive months based on first month

(Thanks to comments from [Jeff](http://chandoo.org/wp/2010/04/06/rolling-months/#comment-100196)
, [Hui](http://chandoo.org/wp/2010/04/06/rolling-months/#comment-100199)
, [Vipul](http://chandoo.org/wp/2010/04/06/rolling-months/#comment-100200)
 and others. I found a simpler and easier way to write the formula)

We will simply use Excel’s date formulas so that we can fetch consecutive rolling months based on the first selection.

Assuming the date is selected in cell A1,

#### In A2, write the formula:

\=DATE(2010,MATCH($A$1,lstMonths,0)+COLUMNS($A$2:A2),1)

#### What is above formula doing?

*   It is using the DATE Formula to create a next months first date.
*   The part MATCH($A$1,lstMonths,0) is used to fetch the position of selected month in the range lstMonths
*   The part COLUMNS($A$2:A2) is [used to generate the sequential numbers](https://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
     in excel.
*   Make sure you have formatted the cells A2:A12 as “date” with code “mmm” to show 3 letter month codes.
*   Rest all you can figure out easily 🙂

### A more complex solution

in-case you got some other types of values instead of months:

To make it a bit simple, I will use a helper cell where we can identify the position of selected month in the list of months, like this:

![automatic rolling months - excel formula](https://chandoo.org/img/f/automatic-rolling-months.png)

I have assumed that Jan is 0, Feb is 1 … Dec is 11. Also, assume, the helper cell is in `$B$4`.

Now, If the selected month is “5”, then the other months will be **6,7,8,9,10,11,0,1,2,3,4.**

![automatic rolling months - formula - MOD](https://chandoo.org/img/f/automatic-rolling-months-formulas.png)

The interesting part here is the sudden jump from 11 to 0 as highlighted above.

To get this type of output we must use an excel formula called as MOD.

#### What is Excel MOD Formula?

MOD formula takes 2 numbers tells us the remainder when first number is divided by second number. \[[Excel MOD formula, Introduction, Syntax & Examples](http://chandoo.org/excel-formulas/mod.html)\
\]

#### So how to use MOD formula to setup rolling months?

Very simple. We just take the value in `$B$4` (position of the first month in the list) and then add +1 to it and then find out the MOD of it when divided by 12. We now use this number to fetch the corresponding month from `lstMonths`.

We use +2 for second month…. +11 for the last month.

We can simplify the +1, +2..+11 part by [using COLUMNS formula to generate the sequential numbers](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
 for us.

#### The formula looks like this:

`=INDEX(lstMonths,MOD($B$4+COLUMNS($A$2:A2),12)+1)`

*   The Mod portion of this formula tells the position of the second, third, fourth, … eleventh month based on the first month.
*   We have to add +1 to output from MOD because we are using 0,1,2,3 positioning the month in B4, where as INDEX use 1,2,3,4 positioning.
*   INDEX formula then fetches the corresponding month from `lstMonths` (or `B5:B16`)

That is all.

### Download the example workbook and learn on your own

I have prepared a short example workbook where this technique is demonstrated. Feel free to [download it](http://chandoo.org/img/d/dynamic-starting-month.xls)
 and play with it to learn more.

### Where would you use such a rolling month setup?

I have once used the rolling month set up in a forecasting spreadsheet (where we made cash flow projections for a startup we were planning to acquire). I am also planning to upgrade my gantt chart templates include rolling month setup.

_**What about you? Where would you use automatic rolling months?**_

### Related Articles and Resources on PHD

*   [Excel Formula Tips & Techniques](http://chandoo.org/wp/tag/formulas)
    
*   [Data Validation in Excel – Tricks and Ideas](http://chandoo.org/wp/tag/data-validation/)
    
*   [Using INDEX Formula – Examples & Tutorials](http://chandoo.org/wp/tag/index/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [76 Comments](https://chandoo.org/wp/rolling-months/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/rolling-months/#respond)
    
*   Tagged under [columns()](https://chandoo.org/wp/tag/columns/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [date](https://chandoo.org/wp/tag/date/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [planning](https://chandoo.org/wp/tag/planning/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThere are Easter Eggs in this Post!!!](https://chandoo.org/wp/easter-eggs-2010/)

[NextUse CTRL+Click to speed up your formula entry \[Quick Tips\]Next](https://chandoo.org/wp/ctrl-click-formula-entry/)

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