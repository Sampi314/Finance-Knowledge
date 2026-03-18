# Auditing Spreadsheets? - Disable Direct Editing Mode to save time [quick tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/spreadsheet-auditing-tip-disable-direct-editing-mode

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Auditing Spreadsheets? – Disable Direct Editing Mode to save time \[quick tip\]
===============================================================================

*   Last updated on April 11, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

For most of us, the prospect of inheriting a large, undisclosed sum of money is bleak. **But we have high probability of inheriting a complex Excel workbook** with 19 worksheets and 2300 rows of data and 195 formulas. The kind where entire rainbow colors are used to color code accounts receivable statuses. Then what do we do? We spend a whole afternoon (and then the rest of the month) breaking our head trying to figure out _why the total revenues are only $ 41.2 million when profits are $ 99.23 million_.

So how do we deal with our inheritance?

Here is a [quick tip](http://chandoo.org/wp/tag/quick-tip/)
 to help you get started. Disable “_**Direct editing mode**_“.

### What is direct editing mode?

By default Excel lets you edit a cell’s value (or formula) directly inside the cell. So if a cell contains the formula =C1+D3 and you double click on it, you will be able to edit the formula right inside the cell.

But many a times, we are only interested in knowing which cells a formula refers to.

### So what happens when you disable direct editing mode?

When you double click on a cell (with formula), Excel will take you to the cells that are referred to in the formula. So in the above example, upon double click Excel selects both C1 and D3 cells.

**See a demo to understand how this works:**

**![Auditing Spreadsheets - Disable Direct Editing Mode to save time](https://chandoo.org/img/q/find-dependent-cells-by-disabling-direct-editing-model-excel-tip.gif)  
**  
![How to disable direct editing mode in Excel - tip](https://chandoo.org/img/q/disable-direct-editing-mode-to-audit-spreadsheets-quickly.png)

### How to Disable Direct Editing Mode?

Very simple. Click on Office Button > Excel Options > Advanced. From here, uncheck “Allow editing directly in cells” option.  This is in the “Editing Options”. See aside.

### Things to keep in mind:

*   This method also highlights any named ranges you have defined.
*   _**This method also works for references in other sheets (as long as no cell in current sheet is referred)**_
    *   For example: if a cell in Sheet1 has the formula =Sheet2!A1+Sheet2!A2 then upon double click, Excel will take you to Sheet2 and selects both A1, A2.
    *   If a cell has the formula =Sheet2!A1+D3, then Excel will only select D3 (since D3 is in the current sheet).

### Do you inherit Excel Workbooks? How do you audit / maintain them?

During my job as a business analyst, I used to deal with Excel files made by others all the time. So understanding and debugging others formulas is something I would do regularly.

Now as a consultant, I often get big, complex Excel workbooks and I have to understand them before doing any customizations.

**My favorite techniques for dealing with inherited workbooks are,**

*   [Using F9 key to evaluate portions of formulas](http://chandoo.org/wp/2008/12/15/formula-debugging-tips-excel/)
    
*   Using CTRL+\` (backquote key) to show all formulas and then go thru them
*   Using formula auditing technique as discussed in this post
*   Using trace dependents / precedents tools in Formula ribbon.
*   [Understanding and dealing with Excel formula errors](http://chandoo.org/wp/2009/04/20/excel-formula-errors/)
    

_**What about you?**_ How do you deal with your inheritance? Go ahead and share techniques, shortcuts and ideas with us thru comments.

### Now if you will excuse me,

I need to go. I have to reply to an email from one Mr. James Chui, an Offshore banker from Nigeria, who claims he has large quantities of undisclosed money waiting to be inherited. 😉

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/spreadsheet-auditing-tip-disable-direct-editing-mode/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/spreadsheet-auditing-tip-disable-direct-editing-mode/#respond)
    
*   Tagged under [debugging](https://chandoo.org/wp/tag/debugging/)
    , [errors](https://chandoo.org/wp/tag/errors/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousShow Details On-demand in Excel \[Tutorial + Training Program\]](https://chandoo.org/wp/show-details-on-demand-in-excel/)

[NextHow to make a 5 Star Chart (Similar to Amazon)Next](https://chandoo.org/wp/how-to-make-a-5-star-chart/)

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