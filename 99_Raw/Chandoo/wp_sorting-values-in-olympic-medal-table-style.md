# Sorting values in Olympic Medal Table style [Quick Tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/sorting-values-in-olympic-medal-table-style

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Sorting values in Olympic Medal Table style \[Quick Tip\]
=========================================================

*   Last updated on August 2, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is Olympic season. Everyone I know is tracking the games and checking their country’s performance. One thing that we notice when looking at medal tally is,

> A single Gold medal is worth more than any number of Silver medals. Like wise, a single Silver medal is worth more than any number of Bronze medals.

So, when you look at the ranking of countries, you see countries with single Gold medal higher up than countries with lots of Silver and Bronze medals (but no Gold).

![Sorting values in Olympic Medal Table style - Excel Tips](https://img.chandoo.org/q/sorting-in-olympic-medal-style-in-excel.png)

So how do we sort our data in Olympic medal table style?
--------------------------------------------------------

It is simpler than it looks. All you have to do is use _**custom** **sort**_ feature in Excel.

1.  Select your data
2.  Go to Home > Sort & Filter > Custom Sort
3.  Now specify the sort levels and sort orders.
4.  Click ok and you are done!

![](https://chandoo.org/wp/wp-content/uploads/2021/08/custom-sort-order-excel.png)

Using SORTBY() formula to sort the table
----------------------------------------

Excel 365 introduced a new formula to sort data by multiple-levels using formulas. **SORTBY**

Assuming your medal data is in the table named **_medals_** you can sort with below formula.

    =SORTBY(medals, medals[Gold],-1, medals[Silver], -1, medals[Bronze],-1,
    medals[Team / NOC],1)

The -1 parameter tells SORTBY to sort in **descending order.**

[**Learn more about SORTBY function**](https://chandoo.org/wp/dynamic-array-functions/)
 & other new formulas in Excel 365.

What if your version of Excel does not have **_SORTBY_**
--------------------------------------------------------

Well, there is a work around. Add an extra column in your data and calculate sort order using a formula, as shown below.

![Using sort order calculation in Excel](https://img.chandoo.org/q/using-a-sort-order-calculation-in-excel.png)

Once you calculate sort order, sort on this column in descending order and you are done.

Video – Sorting Excel data in Olympic medal table style
-------------------------------------------------------

Watch this short & fun video to learn the sorting technique outlined in this page.

Example file – Olympics Medal Table style sorting in Excel
----------------------------------------------------------

**[Please download this Excel file](https://chandoo.org/wp/wp-content/uploads/2021/08/olympic-medal-sorting.xlsx)
** if you want to practice the custom sort or SORTBY() approach.

Do you use custom sort?
-----------------------

Custom sorting is very useful when you 2-3 levels in your data. For example, sorting all projects by department & % completed or sorting all products by region & sales volume. I use it often to understand how my data is.

**What about you?** Do you use custom sort? What is your experience like? _Please share your tips & thoughts using comments._

More Quick Tips on Sorting & Filtering
--------------------------------------

If you find yourself constantly sorting and filtering, then check out below tips. I am sure you will learn something new.

*   **Sorting:**
*   [Custom sorting in Pivot tables](http://chandoo.org/wp/custom-sort-pivot-tables/)
    
*   [Which formula to use to check if a list is sorted?](http://chandoo.org/wp/check-sort-order-of-a-list/)
    
*   [Formula 1 style sorting in Excel](http://chandoo.org/wp/sorting-tricks-1/)
    
*   [How to round and then sort data in Excel](http://chandoo.org/wp/excel-formulas-round-sort/)
    
*   [Sorting text values using formulas!](http://chandoo.org/wp/sorting-text-in-excel-using-formulas/)
    
*   [Shuffling a list in random order in Excel](http://chandoo.org/wp/sort-in-random-order-excel-formulas/)
    
*   [How to sort across columns (_ie_ change sort orientation)](http://chandoo.org/wp/change-sort-orientation-excel-columns/)
    
*   **Filtering:**
*   [Filtering values using advanced filters](http://chandoo.org/wp/how-to-use-advanced-filters/)
    
*   [How to filter odd or even rows only?](http://chandoo.org/wp/how-to-filter-odd-or-even-rows-only-quick-tips/)
    
*   [Right click to filter fast…](http://chandoo.org/wp/filter-by-selected-value/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/sorting-values-in-olympic-medal-table-style/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/sorting-values-in-olympic-medal-table-style/#respond)
    
*   Tagged under [custom sorting](https://chandoo.org/wp/tag/custom-sorting/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [sorting](https://chandoo.org/wp/tag/sorting/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to use Date & Time values in Excel – 10 + 3 tips](https://chandoo.org/wp/date-time-tips-ms-excel/)

[NextHow to write complex Excel formulas (hint: it’s a lot like LEGO)Next](https://chandoo.org/wp/how-to-write-complex-excel-formulas/)

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