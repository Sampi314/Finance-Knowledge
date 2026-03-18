# How to Conditionally Show or Hide Charts - Excel Chart Templates & Tutorials

**Source:** https://chandoo.org/wp/select-show-one-chart-from-many

---

*   [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Select & Show One Chart from Many
=================================

*   Last updated on May 30, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Yesterday I have learned this cool excel charting trick and I cant wait to share it with you all.

### The problem: I have too many charts & want to show one based on selection

You have made 3 charts to show your company performance in the last 8 years. But you don’t want to clutter the project report with all of them. You would rather want to show one chart and let user choose to see the any of the other two, like this:

![](https://chandoo.org/wp/wp-content/uploads/2008/11/excel-charts-conditionally-show-hide.gif "excel-charts-conditionally-show-hide")

### The Solution: Use INDIRECT() and a nifty image hack

*   First, **create your charts in a separate worksheet** like this (remember you need to create all 3 charts first)  
    [![](https://chandoo.org/wp/wp-content/uploads/2008/11/create-charts-in-another-sheet.gif "create-charts-in-another-sheet")](https://chandoo.org/wp/wp-content/uploads/2008/11/create-charts-in-another-sheet.gif)
    
*   Once the charts are created **adjust the width and heights of 3 cells** and place one chart in each like above.
*   ![](https://chandoo.org/wp/wp-content/uploads/2008/11/insert-named-range-excel.png "insert-named-range-excel")Now, go back to the sheet where you want to control the display, and **define a new named range**. Lets call it **_getChart_**. You can define new named ranges from menu > insert > name > define.  You will see a dialog box like this (right):
*   In the “Refers to:” area we will now write an INDIRECT() spreadsheet formula to refer to one of the 3 cells where charts are placed. A sample formula is below:`IF('View them here'!$C$2="Sales",INDIRECT("'Place your charts here'!F11"),IF('View them here'!$C$2="Expenses",INDIRECT("'Place your charts here'!F12"),INDIRECT("'Place your charts here'!f13")))`
*   The above formula assumes, you are going to control chart display thru cell C2 in the sheet ‘view them here’
*   Now adjust a cell’s size in this spread sheet to be big enough so that we can fit the selected chart.
*   **Go to Menu > Insert > Picture > From File and insert any picture.** This is just for a placeholder purpose, so any picture would do, including that of your cat’s. 🙂
*   Finally, **select the image and go to formula bar and type `=getChart`** (or whatever name you gave to the named range), like this:  
    ![](https://chandoo.org/wp/wp-content/uploads/2008/11/insert-picture-spreadsheet.png "insert-picture-spreadsheet")
*   Change the value in C2 and see the magic.

### How this hack works?

**In excel you can assign named ranges to images inserted in the sheet.** So when you adjusted the cell sizes in the sheet with charts and created indirect references through INDIRECT() formula and used it in the named range, excel fetched the content of the cell (the chart) and replaced your cat’s picture with that. This powerful little trick can help you make interactive dashboards within little space.

Pretty cool, eh?

### Download and see in action

Here is a link to the downloadable [conditional chart display workbook](https://chandoo.org/wp/wp-content/uploads/2008/11/select-chart-to-display.xls)
. I have tested this in Excel 2003, but I guess it should work the same way in most of the modern versions of excel. Feel free to drop a comment if you see this not working in a particular version.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [191 Comments](https://chandoo.org/wp/select-show-one-chart-from-many/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/select-show-one-chart-from-many/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [fun](https://chandoo.org/wp/tag/fun/)
    , [hacks](https://chandoo.org/wp/tag/hacks/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousUS Poll Trackers – Live Dashboards Ooze Visualization Goodness](https://chandoo.org/wp/us-poll-trackers-live-dashboards-ooze-visualization-goodness/)

[NextExtracting Unique, Duplicate and Missing Items using Formulas \[spreadcheats\]Next](https://chandoo.org/wp/unique-duplicate-missing-items-excel-help/)

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