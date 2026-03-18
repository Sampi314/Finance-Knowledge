# How to use Excel date values - Guide to Date, time functions

**Source:** https://chandoo.org/wp/date-time-tips-ms-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to use Date & Time values in Excel – 10 + 3 tips
====================================================

*   Last updated on July 28, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Using date & time values in Excel](https://chandoo.org/wp/wp-content/uploads/2021/07/using-date-and-time-values-in-Excel.png)

Knowing **how to use Excel date values** can help you save a ton of time in your day to day spreadsheet chores. Let us prepare for your date with the sheet using these 10 handy tips.

Before jumping on to the tips, it helps to know how excel represents the date and time.

> **Microsoft Excel stores dates as sequential numbers** … January 1, 1900 is serial number 1, and 28 July, 2021 is serial number 44405 because it is 44,405 days after January 1, 1900. Excel stores times as decimal fractions because time is considered a portion of a day.

So you see, Date and Time are in fact numbers in Excel. Just enter a date in your excel sheet and format it as number to see its equivalent numeric value. If a date is `29-July-2021` and Excel represents it as `44406`.

Similarly, 9PM on 29-July-2021 is represented as 44406.875

How-to use Excel date values and formulas
-----------------------------------------

Now that you know the little secret behind date / time, lets move to the 10 tips.

### 1\. Test whether a date is future or past

You can find whether a date is past or future or today using simple if formula like: `=if(this_date=today(),"Today",if(this_date < today(),"Past","Future"))`

`today()` is the spreadsheet function using which you can find today’s date.

### 2\. Find the number of days between two dates

Since dates are represented as sequential numbers in excel, in order to find out how many days are between any given 2 dates, just subtract one from another. For eg. you can use `=today()-date(1947,8,15)` to find how many days since India’s independence (August 15, 1947).

### 3\. Formatting dates

Having date / time in the sheet is not enough if you can not make it look like the way you want. For eg. you may want to show date as “Wednesday, 28 July, 2021”. You can use cell formatting to do this. Just select the cell with date and hit ctrl+1 and in the “Number” tab select “Custom” as category and mention “dddd, dd mmmm, yyyy” as format string.

Try these other date formats as well.

![formatting date and time values in Excel](https://chandoo.org/wp/wp-content/uploads/2021/07/formatting-date-time-values-in-excel.png)

Learn more about [custom cell formatting](http://chandoo.org/wp/custom-cell-formatting-in-excel-few-tips-tricks/)
.

### 4\. Auto-filling only weekdays

![Fill weekdays when entering days](https://chandoo.org/wp/wp-content/uploads/2018/06/weekends-when-filling-dates.png)

We all know that in order to fill a series of dates in Excel sheet, you just need to enter first few dates and then select the range and drag to auto fill the selection with rest of the dates. But what if you need to fill only weekdays?

You can do that easily with Auto fill option – “weekdays only” as shown on the right. [learn more](http://chandoo.org/wp/skip-weekends-while-autofill-dates-in-excel-howto/)
.

### 5\. Find out the day of week from a given date

Finding whether a day is weekend or weekday is useful if you are making project plans or resource allocation sheets. You can do this by simply using `weekday()` function. For eg. `=weekday("07/28/2021")` would return 4 (Excel, by default starts the week at Sunday, hence Wednesday is indicated as 4).

If you would like to start the week with Monday like most of us do, use `=weekday("07/28/2021",2)`.

### 6\. Highlight weekends using conditional formatting

Often when you are making project plans or reports, it helps if the weekends or after office hours can be grayed out. You can do this easily with conditional formatting as shown below:

![highlight weekends](https://chandoo.org/wp/wp-content/uploads/2021/07/highlight-weekends.png)

In order to do this, we can test whether a given a day is weekend or not in conditional formatting by `=WEEKDAY(this_date,2)>5` as weekday() returns 6 and 7 for Saturday and Sunday.

You can use similar logic to highlight after office hours (before 9AM or after 5PM) for time values. [Learn these 5 tips to master conditional formatting](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/)
.

### 7\. Adding / Subtracting dates

Since Excel dates are nothing but numbers, you can find out the difference between two given dates by just subtracting one from another. For eg. `=DATE(2021,7,31)-DATE(2021,7,1)` will return `30`

In order to add n number of days to a given date, you can just add that number to given date. For eg. `="07/20/2021"+26` will return `08/15/2021`

### 8\. Ensuring a valid date or time is entered in a cell

When sharing your sheets with others to enter some data, it may be useful if you can restrict them to enter only valid date values in cells that require date value. You can do that using cell data validation feature in excel. Just select the cell to which you want to apply date / time validation, go to data ribbon > validation and set type as “Date” or “Time” and specify criteria.

![data validation rule to allow dates only in 2021 (any year)](https://chandoo.org/wp/wp-content/uploads/2021/07/date-validation-rule.png)

For example, you can specify criteria like the one above to ensure that date entered is in year 2018. What more, using message option of data validation settings you can even show messages like this:

![date rule for data validation - error message](https://chandoo.org/wp/wp-content/uploads/2021/07/error-message-please-enter-a-date-in-the-year-2021.png)

### 9\. Insert today’s date, current time using key board shortcuts

Just go to the cell where you want to insert date and press ctrl+;

To get current time, use ctrl+shift+; ( thus ctrl+: )

Btw, if you are planning to get today’s date or current time using formulas, you can use today() and now(). [Also learn these 11 very useful excel keyboard shortcuts](http://chandoo.org/wp/excel-keyboard-shortcuts/)
.

### 10. Top Date functions for you

Excel has many Date & Time functions. Here is a list of some of the most important ones to help you use date values in Excel.

Date & Time formulas
--------------------

| To get | Use this | Example Result | Function used |
| --- | --- | --- | --- |
| Day of week number | WEEKDAY(date) | 4   | WEEKDAY() |
| Month number | MONTH(date) | 7   | MONTH() |
| Year | YEAR(H3) | 2021 | YEAR() |
| Day number | DAY(date) | 28  | DAY() |
| Name of the month | TEXT(date,"MMMM") | July | TEXT() |
| Same day, next month | EDATE(date,1) | 28 August 2021 | EDATE() |
| End of the month | EOMONTH(date,0) | 31 July 2021 | EOMONTH() |
| Current date | TODAY() | 28 July 2021 | TODAY() |
| 7 days from today | TODAY()+7 | 4 August 2021 | TODAY()+7 |
| Gap between two dates | TODAY()-DATE(2021,1,1) | 208 | \- (minus) |
| 5 working days from now | WORKDAY(TODAY(),5) | 4 August 2021 | WORKDAY() |
| Number of working days in a month | NETWORKDAYS(DATE(2021,7,1),DATE(2021,7,31)) | 22  | NETWORKDAYS() |

**That is all, with these 10 tips I hope I made your date with that spreadsheet is made little exciting.**

3 Important Date formulas for finance & accounting people
---------------------------------------------------------

If you work in finance or accounting professions, using dates is an important part of your job. Apart from all the above tips, you also need to learn how to calculate:

1.  Quarter from a date (both calendar & financial)
2.  First working day of a month
3.  Last working day of a month

See this short video to understand how to calculate these ([watch it on my YouTube channel](https://youtu.be/NIvTVKZqmM0)
)

**[Download the file demoed in the video](https://chandoo.org/wp/wp-content/uploads/2021/07/3-must-know-date-calculations-for-accountants.xlsx)
**.

Common problems when working with dates in Excel
------------------------------------------------

When using date & time related values or formulas in Excel, often you might notice some problems. Use this check list to fix the problem.

1.  **Excel shows ##### instead of date or time values  
    **This can happen if your cell is too small to show the value. Try adjusting column width.  
    This can also happen if you use incorrect values as date & time. For example, if you try to format negative numbers as date, you will see #####
2.  **Excel cannot understand my date  
    **When trying to convert a cell or value to date, sometimes Excel cannot understand your input. This is because Excel relies on your regional settings to understand dates. So if your usual date format is mm/dd/yyyy, then Excel expects the cells (or values) to have same format in order to convert them to dates. If you have dd/mm/yyyy values, then Excel may not convert the dates. To fix the problem, read [extract dates from text tutorial](https://chandoo.org/wp/text-to-date-convertion/)
    

Download Date How-to & Tutorial Workbook
----------------------------------------

[**Click here download example workbook**](https://chandoo.org/wp/wp-content/uploads/2021/07/date-howto-tutorial-2021.xlsx)
 with several date calculations and format detail. Play with it to learn more.

### Learn more about Excel Date & Time functions

*   [42 tips for Excel time travelers](https://chandoo.org/wp/excel-date-time-tips/)
    
*   [Rounding time to nearest hour or 15 minutes](https://chandoo.org/wp/rounding-time-in-excel/)
    
*   [How many _Mondays_ are between two dates](https://chandoo.org/wp/count-mondays-between-two-dates/)
    
*   [How to highlight overdue dates](https://chandoo.org/wp/overdue-items/)
    

### Got a problem working with dates? Post it in comments

If you have any date or time related issues, please post a comment so our community or I can help you. Got an interesting tip or formula about working with dates? Please do share it so I can learn from you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [99 Comments](https://chandoo.org/wp/date-time-tips-ms-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/date-time-tips-ms-excel/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [how to](https://chandoo.org/wp/tag/how-to/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [productivity](https://chandoo.org/wp/tag/productivity/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousGetting Started with Power BI – Sales Dashboard in one hour](https://chandoo.org/wp/powerbi-intro-free-live-event/)

[NextSorting values in Olympic Medal Table style \[Quick Tip\]Next](https://chandoo.org/wp/sorting-values-in-olympic-medal-table-style/)

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
    
    [Reply](https://chandoo.org/wp/date-time-tips-ms-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/date-time-tips-ms-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/date-time-tips-ms-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ