# Excel formula to convert calendar format to table » Excel Functions & Formulas

**Source:** https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel formula to convert calendar format to table
=================================================

*   Last updated on September 3, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Ever have data in a calendar format and just wished you can get it in to tabular format? Something like this:

![Calendar data to tabular format - Excel formula](https://chandoo.org/wp/wp-content/uploads/2020/09/calendar-data-to-tabular-format-formula.png)

You can use Excel formulas or [Power Query](https://chandoo.org/wp/power-query-tutorial/)
 to do this. In this article, let’s review formula based approach with two excellent choices.

Calendar to Table Formulas – Video
----------------------------------

If you want to understand the formulas, watch below video or read on.

Using SUMIFS formula
--------------------

We can use the [SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
 to easily get data for any date, as [it works with 2D ranges too](https://chandoo.org/wp/2d-sumif-formula/ "SUMIFS formula for 2d ranges")
.

Let’s say our calendar data is in the range B5:H16,

Use the formula =SUMIFS(**B6:H16**, _B5:H15_, “1-Aug-2020”) to get value corresponding to 1-Aug-2020.

Notice the difference between **Sum range** and _Criteria range_.

We move the **sum range** one row down so that we can look at dates above and get the corresponding value from below.

### Limitations of SUMIFS approach:

*   **Works only for numbers**. If you have text values against each date, then this method will not work.
*   **Can be wrong**. Let’s say one of the values is 44044. Which is the number representation of 1-Aug-2020 (as Excel dates are just numbers. More on [working with date & time here](https://chandoo.org/wp/date-time-tips-ms-excel/)
    ) Then our SUMIFS result will be wrong.

[Learn more about SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
.

Using INDEX formula
-------------------

We can use [INDEX formula](https://chandoo.org/wp/index-formula-usage-and-tips/)
 to access any item in a range by specifying row & column numbers.

For example, =INDEX(A1:D10, 3,2) will return the value in 3rd row & 2nd column of A1:D10, _ie_ B3 value.

So if we can calculate the row & column co-ordinates for a given date from our calendar, we can easily get the answer.

**Column number:** As our data is in a calendar format, each date will only fall in the column corresponding to the weekday number. We can use =WEEKDAY(input\_date, 2) to get the column number, given that our calendar is from Monday to Sunday.

**Row number:** Once we know the column number, we can extract the entire column and look for given date in that column with MATCH function. This will give us the row number too. The below formula works fine.

\=MATCH(input\_date, **INDEX(calendar\_data, , WEEKDAY(input\_date, 2))**, 0)

Note: the internal INDEX() formula returns entire column as we omitted _row parameter._ [Read up more on this functionality of INDEX formula](https://chandoo.org/wp/index-formula-usage-and-tips/)
.

**Final formula:**

Here is our final formula (with calendar in range B5:H16)

\=INDEX($B$5:$H$16,
   MATCH(_input\_date_,INDEX($B$5:$H$16,,WEEKDAY(_input\_date_ ,2)),0)+1,
   WEEKDAY(_input\_date_, 2))

Related: [Learn more about INDEX formula](https://chandoo.org/wp/index-formula-usage-and-tips/)
.

Download Example Workbook
-------------------------

**[Please click here to download the example file](https://chandoo.org/wp/wp-content/uploads/2020/09/calendar-to-table-formula-v1.xlsx)
** with calendar data to table format formulas. Examine the formulas or write your own to understand this technique.

Other ways to convert calendar format data
------------------------------------------

*   **You can use Power Query** to do this job. I **highly recommend** using PQ, if you deal with calendar style data often. Here is a [primer on Power Query](https://chandoo.org/wp/power-query-tutorial/)
    .
*   I have previously written about this problem (with SUMIFS solution) and asked my readers to share their formulas. You can see [many other interesting & creative solutions here](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/)
    
*   **VBA**: You can use a simple macro to quickly reshape the data. This is a preferred option only if you can’t use Power Query. [Here is a tutorial with such macro](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/)
    . The comments on this link also feature many Power Query based transformations.

How would you deal with calendar style data?
--------------------------------------------

For something quick and easy, I will use formulas. For an on-going situation, I will use Power Query.

**What about you?** How would you deal with calendar style datasets? Please share your thoughts in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [index](https://chandoo.org/wp/tag/index-2/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousPower Query Tutorial – What is it, How to use, Full examples, Tips & Tricks](https://chandoo.org/wp/power-query-tutorial/)

[NextTwo-level Data Validation \[Excel Trick\]Next](https://chandoo.org/wp/two-level-drop-downs/)

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
    
    [Reply](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ