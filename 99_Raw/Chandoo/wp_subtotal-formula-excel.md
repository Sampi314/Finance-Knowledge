# What is Excel SUBTOTAL formula and 5 reasons why you should use it » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/subtotal-formula-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

What is Excel SUBTOTAL formula and 5 reasons why you should use it
==================================================================

*   Last updated on February 8, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Subtotal Formula Excel](https://img.chandoo.org/f/subtotal-formula-excel.png "Subtotal Formula Excel")**Today we will learn Excel SUBTOTAL formula and 5 beautiful reasons why you should give it a try.**

SUBTOTAL formula is used to find out subtotal of a given range of cells. You give SUBTOTAL two things – (1) a range of data (2) type of subtotal. In return, SUBTOTAL will give you the subtotal for that data.

Unlike SUM, AVERAGE, COUNT etc. which do one thing and only one thing, _**SUBTOTAL is versatile**_. You can use it to sum up, average, count a bunch of cells.

**Here is the SUBTOTAL syntax:**

`=SUBTOTAL (TYPE OF TOTAL, RANGE OF CELLS)`

![Excel Subtotal Formula Syntax](https://img.chandoo.org/f/excel-subtotal-formula-syntax.png "Excel Subtotal Formula Syntax")

So, for example, =SUBTOTAL(9,A1:A10) will give us the sum of all values in A1:A10, provided none are filtered(more on this filtering thing below). **That is because “9” stands for SUM in SUBTOTAL lingo.** If you want a count of values, you can use “2”.

**Hmm, that sounds like any other formula, what is so special about it?**

Well, SUBTOTAL is not just any other formula, it is a special one. We don’t need to be Jedi masters to tell that force is with SUBTOTAL.

Here I have listed 5 reasons why this is such a special formula.

### 1) You can use SUBTOTAL to find sum of filtered values

I think the title says it all. See this example to know more.

![Subtotal Formula With Filters](https://img.chandoo.org/f/subtotal-formula-with-filters.gif "Subtotal Formula With Filters")

### 2) You can use SUBTOTAL to ignore values in hidden rows

Often, we use hide rows feature in excel to remove irrelevant items from view. You can use SUBTOTAL with special type codes so that values in hidden rows are neglected.

For eg. SUBTOTAL(9,A1:A10) finds the sum of values in cells A1:A10 where as SUBTOTAL(109,A1:A10) will find sum of values in visible rows only.

### 3) You can use SUBTOTAL to dynamically summarize data

Since the “type of total” is a parameter to SUBTOTAL, we can use that to make a dynamic summary like this:

![Subtotal Dynamic Summary](https://img.chandoo.org/f/subtotal-dynamic-summary.gif "Subtotal Dynamic Summary")

This is very handy in [dashboards](http://chandoo.org/wp/management-dashboards-excel/)
 or when you don’t have space for everything.

### 4) If there are _subtotals_ in SUBTOTAL range, they will be neglected

![Subtotals Inside Subtotal Formula](https://img.chandoo.org/f/subtotals-inside-subtotal-formula.png "Subtotals Inside Subtotal Formula")

This is a killer feature of SUBTOTAL. If you have any SUBTOTAL formulas in the input range of another SUBTOTAL formula, these values are neglected so that double counting is avoided. Need I say more?

### 5) You can automatically create SUBTOTALs using Excel Data Tools

While SUBTOTAL formula looks kind of neat, writing them when you have tabular data can be a drag. But you don’t have to worry about that. In Excel’s Data menu / ribbon, there is an option on called “Subtotals” that automates the whole process for you.

![Automatic Subtotals Excel](https://img.chandoo.org/f/automatic-subtotals-excel.png "Automatic Subtotals Excel")

To generate automatic SUBTOTALS, just select your table of data, go to Data ribbon (or menu) and click on “Subtotals”. This will launch a Subtotal dialog where you can easily specify the type of total grouping you want.

That simple!

### Related Excel Formulas:

[SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 | [VLOOKUP](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 | [SUMIF & COUNTIF](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)

### Have you used SUBTOTAL formula?

I have never really bothered to test SUBTOTAL formula until few days ago. Now that I found some really cool uses for it, I am itching to implement some of them in future. What about you? Have you used SUBTOTAL formula before? Do you got any tips to share? Please use comments to discuss.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [75 Comments](https://chandoo.org/wp/subtotal-formula-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/subtotal-formula-excel/#respond)
    
*   Tagged under [data filters](https://chandoo.org/wp/tag/data-filters/)
    , [group ungroup](https://chandoo.org/wp/tag/group-ungroup/)
    , [hide](https://chandoo.org/wp/tag/hide/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [SUBTOTAL](https://chandoo.org/wp/tag/subtotal/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel School is Open for Admissions](https://chandoo.org/wp/excel-school-is-open/)

[NextPreparing Profit / Loss Pivot Reports \[Part 2 of 6\]Next](https://chandoo.org/wp/profit-loss-reports-excel-2/)

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