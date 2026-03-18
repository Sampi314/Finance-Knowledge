# Remove duplicates & sort a list using Pivot Tables » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/remove-duplicates-using-pivot-tables

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Remove duplicates & sort a list using Pivot Tables
==================================================

*   Last updated on September 27, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Removing duplicate data is like morning coffee for us, data analysts. _Our day must start with it._

It is no wonder that I have written extensively about it (here: [1](http://chandoo.org/wp/2009/06/22/remove-duplicates/)
, [2](http://chandoo.org/wp/2006/09/04/how-to-get-unique-items-using-excel/)
, [3](http://chandoo.org/wp/2008/06/19/quickly-display-unique-items-in-an-excel-list-using-advanced-filters/)
, [4](http://chandoo.org/wp/2008/11/06/unique-duplicate-missing-items-excel-help/)
, [5](http://chandoo.org/wp/2009/02/03/excel-pivot-tables-unique-items/)
, [6](http://chandoo.org/wp/2010/02/02/data-validation-using-an-unsorted-column-with-duplicate-entries-as-a-source-list/)
, [7](http://chandoo.org/wp/2009/10/26/duplicate-data-entry/)
, [8](http://chandoo.org/wp/2009/03/25/using-array-formulas-example1/)
).

But today I want to show you a technique I have been using to **dynamically extract and sort all unique items from a last list of values using Pivot Tables & OFFSET formula.**

![Remove Duplicates & sort list dynamically using Pivot Tables](https://chandoo.org/img/pivot/remove-duplicates-using-pivot-tables.png)

_**This is how it goes…,**_

### Step 1: Select your data & Create a pivot table

Just select any cell and insert a pivot table. Very simple right?

### Step 2: Drag the field(s) to row label area of pivot

Like this.

![Draf the fields to row label area of Pivot Table - Excel](https://chandoo.org/img/pivot/pivot-table-setup.png)

Make sure you have turned off grand totals and sub-totals as we just need the names. **And sort the pivot table.**

### Step 3: Create a named range that refers to the pivot table values

[Using OFFSET formula](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
, we can create a named range that refers to pivot table values and grows or shrinks as the pivot is refreshed. Assuming the pivot table row values start in cell F6, write a formula like,

`=OFFSET($F$6, 0,0,COUNTA($F:$F)-1,1)` and map it to a name like _lstProducts_.

![Dynamic Named Range - from Pivot Table values](https://chandoo.org/img/pivot/dynamic-named-range-pivots.png)

The formula gives us all the values in column F, starting F6. The COUNTA($F:$F)-1 ensures that we get only row labels and not the title (in this case **Product Names**).

### Step 4: Use the named range in formulas etc. as you see fit

That is all. Nothing else.

**Just make sure that you refresh the pivot table whenever source data changes.**

### Download example file with this technique

[Click here to download](https://img.chandoo.org/d/remove-duplicates-using-pivot-tables.xls)
 an example file and play with it to understand how this works.

### How do you deal with duplicate data?

In my work, I come across duplicate data all the time. I have been using pivot table based technique with great success. It is fast, reliable and easy to setup. The only glitch is that you need to refresh the pivot tables whenever source data changes. However, you can automate this by writing a simple macro.

What about you? How do you deal with duplicate data? Share your techniques, tips & ideas using comments.

### More tips on using Pivot Tables to Analyze data:

*   [Introduction to Pivot Tables – Tutorial](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    
*   [Pivot Table tricks to make you a data analytics star](http://chandoo.org/wp/2010/01/27/pivot-table-tricks/)
    
*   [Video Tutorial on Pivot tables](http://chandoo.org/wp/excel-tutorial/working-with-pivot-tables/)
    
*   [Grouping Dates in Pivot Tables](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [31 Comments](https://chandoo.org/wp/remove-duplicates-using-pivot-tables/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/remove-duplicates-using-pivot-tables/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [COUNTA()](https://chandoo.org/wp/tag/counta/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [remove duplicates](https://chandoo.org/wp/tag/remove-duplicates/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [unique items](https://chandoo.org/wp/tag/unique-items/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousDisplaying & Selecting a Scenario using VBA \[Modeling in Excel\]](https://chandoo.org/wp/displaying-selecting-a-scenario-using-vba-modeling-in-excel/)

[NextShow Zebra Lines when Value Changes \[Excel Conditional Formatting Homework\]Next](https://chandoo.org/wp/add-zebra-lines-when-value-changes/)

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