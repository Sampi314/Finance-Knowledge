# Find Quarterly Totals from Monthly Data [SUMPRODUCT Formula] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/quarterly-totals-from-monthly-data

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Find Quarterly Totals from Monthly Data \[SUMPRODUCT Formula\]
==============================================================

*   Last updated on April 29, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Here is a problem we face very frequently. You have a list of values by months. And you want to find out the totals by Quarter. How do you go about it?

![Monthly Data - Example](https://img.chandoo.org/f/monthly-data-example.png)

There are 2 options:

1.  You can [make a pivot report](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
     from the data and then [group dates in that](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/ "Group Dates in Pivot Tables in Excel")
     to find totals by quarter
2.  You can write formulas to find the totals by quarter

While option 1 is good for knowing the values, we need option 2 if you want the values to be fed to another report, chart or dashboard.

### Writing Formulas to Get Quarterly Totals from Monthly Data:

#### First, understand a little math formula called ROUNDUP():

**ROUNDUP formula takes a number and rounds it up to the nearest fraction** as specified by you. So for eg.,

*   `ROUNDUP(1.234,1) = 1.3`
*   `ROUNDUP(1.234,2) = 1.24`
*   `ROUNDUP(1.234,0) = 2`
*   `ROUNDUP(1.0,0) = 1`

_Now, assuming your monthly data is in cells B4:C15,_

**Our objective is to find Quarters from dates and then add up all items in Q1 against Quarter 1.**

![Quarterly totals - Blank](https://img.chandoo.org/f/quarterly-totals-blank.png)

We can get the month from a date using MONTH() formula. If we divide the month by 3 and then round the value up to nearest integer we will get the Quarter.

So, A formula like `=ROUNDUP(MONTH(B4)/3,0)` should tell us the quarter for the month in the cell B4.

So the final formula for calculating sum of all the sales in Q1 is `=SUMPRODUCT((ROUNDUP(MONTH(B4:B15)/3,0)=1)*(C4:C15))`.

### How this formula works?

![Quarterly Totals from Monthly Data - Excel Formula Howtos](https://img.chandoo.org/f/quarterly-totals-from-monthly-data.png)

Well, the portion `ROUNDUP(MONTH(B4:B15)/3,0)=1` gives a bunch of 1 and 0s, one where the month belongs to Q1 and zero where it is not. When you multiply these ones and zeros with actual sales values in C4:C15, you get the total sales in Q1.

**Since [SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 has _magical powers_**, it just processes all these ranges of data without batting an eyelid.

### Download the example worksheet and play with this formula

Go ahead and [download the example workbook](https://img.chandoo.org/f/quarterly-totals-from-monthly-data.xls)
 and play with SUMPRODUCT formula to understand this better.

### How do you calculate Quarterly Totals from Monthly Data?

Do you know a better way to do such calculation? How do you usually do it? Please share your tricks and ideas using comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [34 Comments](https://chandoo.org/wp/quarterly-totals-from-monthly-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/quarterly-totals-from-monthly-data/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [group by quarter](https://chandoo.org/wp/tag/group-by-quarter/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [month](https://chandoo.org/wp/tag/month/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSUMIF works in 2D too \[quick tip\]](https://chandoo.org/wp/2d-sumif-formula/)

[NextQuarterly totals when you have multi-year data \[SUMPRODUCT again\]Next](https://chandoo.org/wp/quarterly-totals-multi-year-data/)

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