# FREE 2012 Calendar - Download and Print Year 2012 Calendar today - Excel Calendar Template [2012]

**Source:** https://chandoo.org/wp/download-free-2012-calendar

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

2012 Calendar – Excel Template \[Downloads\]
============================================

*   Last updated on December 27, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Here is a new year gift to all our readers – **free 2012 Excel Calendar Template.**

This calender has,

*   One page full calendar with notes, in 4 different color schemes
*   1 Mini calendar
*   Monthly calendar (prints to 12 pages)
*   Works for any year, just change _year_ in _**Full tab**_.

![FREE 2012 Calendar - Excel Template](https://chandoo.org/img/c/2012-calendar-excel-template.png)

Download 2012 Calendar – Excel File
-----------------------------------

[**Click here to download the file**](https://img.chandoo.org/d/2012-calendar-v1.xlsx)
. _For Excel 2003 compatible version, [click here](http://chandoo.org/img/d/2012-calendar-v1.xls)
._

We wish you an awesome New Year 2012.

How does this Calendar work?
----------------------------

This is the same file as [2011 calendar](http://chandoo.org/wp/2010/12/17/download-free-2011-calendar/)
 with the year changed. So,

*   The cell D3 in worksheet _**Full**_ has the year of calendar. I named this cell as year.
*   All the formulas for the calendar are written in the worksheet _**mini**_.  
    ![Free Mini Calendar Template - 2012](https://img.chandoo.org/c/2012-mini-calendar-free.png)
*   For this calendar, I took inspiration from Daniel’s **[Live Calendar example](http://www.excelhero.com/blog/2010/01/live-calendar-musings.html)
    ** (Recommended reading for formula enthusiasts).
*   **The first step to create a calendar is to generate a sequence of numbers 1 thru 42** (because calendar grid has 42 cells – 7 days per week x 6 weeks max, per month). I used a combination of INDIRECT, OFFSET and COLUMN to get this. The formula is `=COLUMN(OFFSET(INDIRECT("$A$1"),0,0,1,42))-1`. I mapped this formula to `daysAndWks` named range.
*   **Next step is to find the first date of each month** using a simple date formula like `=date(year,month,1)`. This formula is mapped to named range – `DateOfFirst`
*   For given month, the calendar is nothing but `=daysAndWks + DateOfFirst - WEEKDAY(DateOfFirst,2)`. This formula is mapped to named range – `calendar`.  
    ![Named Ranges in Excel Calendar Template](https://img.chandoo.org/c/named-ranges-excel-calendar.png)
*   Once the mini calendar is ready, I just created **12 named ranges m1\_, m2\_,…, m12\_ corresponding to each of the 12 months.**
*   Then, I used the same in individual calendar worksheets along with INDEX formulas to fetch the dates.
*   Finally, I formatted the calendars nicely. Design of this calendar is similar to that of [2010 calendar](http://chandoo.org/wp/2009/12/11/2010-calendar-excel-template-downloads/)
     & [2009 calendar templates](http://chandoo.org/wp/2008/12/04/free-excel-calendar-template-download/)
    .

Go ahead and enjoy the download. The file is unlocked. So poke around the formulas and named ranges. Learn some Excel.

**More Downloads:** [**Download Free Excel Templates**](http://chandoo.org/wp/free-excel-templates-download/)

**Techniques used:** [INDEX](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
 | [OFFSET](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
| [INDIRECT](http://chandoo.org/wp/tag/indirect/)
 | [Array Formulas](http://chandoo.org/wp/tag/array-formulas/)
 |  [Using Date & Time in Excel](http://chandoo.org/wp/tag/date-and-time/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [37 Comments](https://chandoo.org/wp/download-free-2012-calendar/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/download-free-2012-calendar/#respond)
    
*   Tagged under [2012](https://chandoo.org/wp/tag/2012/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [calendar](https://chandoo.org/wp/tag/calendar/)
    , [calendar template](https://chandoo.org/wp/tag/calendar-template/)
    , [column()](https://chandoo.org/wp/tag/column/)
    , [custom views](https://chandoo.org/wp/tag/custom-views/)
    , [date](https://chandoo.org/wp/tag/date/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [print areas](https://chandoo.org/wp/tag/print-areas/)
    , [printable calendar](https://chandoo.org/wp/tag/printable-calendar/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [weekday](https://chandoo.org/wp/tag/weekday/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMerry Christmas & Happy New Year 2012](https://chandoo.org/wp/merry-christmas-happy-new-year-2012/)

[NextPeople & Websites that Helped me in 2011 \[Thank you message\]Next](https://chandoo.org/wp/people-websites-that-helped-me-in-2011-thank-you-message/)

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
    
    [Reply](https://chandoo.org/wp/download-free-2012-calendar/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/download-free-2012-calendar/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/download-free-2012-calendar/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ