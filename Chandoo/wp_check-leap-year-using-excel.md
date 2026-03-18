# Check if an year is leap year, using Excel Formulas

**Source:** https://chandoo.org/wp/check-leap-year-using-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

14 ways to check if an year is leap year, using Excel \[just for fun\]
======================================================================

*   Last updated on February 29, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Today is February 29th, and that means, this year we have one more day to be awesome.** So lets celebrate it in Excel style!

Lets learn 14 different ways to tell if an year is leap year, using Excel Formulas.

### Why 14? because, we are awesome like that.

Why 14 methods to just find the year in cell D4 is leap year or not? Because, we all know that by learning different ways to solve a problem, we become smarter, more awesome and have more fun. So lets roll.

![Check if an year is leap year or not using Excel](https://img.chandoo.org/f/checking-if-an-year-is-leap-year-using-excel.png "Check if an year is leap year or not using Excel")

### Before we start..,

Since all the 14 methods rely on certain calculations, I have created some names. See below:

![Named Ranges and Formulas used to check for leap year](https://img.chandoo.org/f/named-ranges-and-formulas-leap-test.png "Named Ranges and Formulas used to check for leap year")

All the names are self-explanatory, except the **_febDays_**. So lets take a look at it.

**febDays formula**

For one of the methods, we need to have all the dates in February in a list. If we want the first of Feb as a date, we can use =DATE(year,2,1). But we want all dates in February. That means, we need to use a list (array) in third parameter of DATE like this:

\=DATE(year,2,{1,2,3,4,….,28,29})

Instead of typing all the 28/29 numbers, we can [use ROW formula](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/ "Use ROWS() and COLUMNS() formulas to generate numbers in a sequence [quick tip]")
 to generate these, like:

\=ROW($A$1:$A$29) would give me a numbers from 1 thru 29.

But the problem is in many years Feb has only 28 days, and for rest, it has 29 days. So we modify the second part of row formula and use the last DAY of the Feb, like this:

\=ROW($A$1: INDEX($A$1:$A$29,DAY(EOMONTH(feb1st,0))))

To get the last day of a month, we use = DAY(EOMONTH(1st date, 0))

I think you can put the rest of pieces together to solve this puzzle.

Moving on,

### #1 – The year has 366 days

This is the obvious one. We use =DATE(year+1,1,1)-jan1st=366 to check if there are 366 days between January 1st of next year and this year.

### #2 – February 29th is not March 1st

[Because in Excel all dates are numbers](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
, when we use a formula like =DATE(2011,2,29), Excel gives us the date of March 1st, even though we wanted 29th Day of February in 2011.  _**So a simple leap year check is to see if February 29 is March 1st or not!**_

\=DATE(year,2,29)<>mar1st

### #3 – February has 29 days

This is another obvious test. In a leap year, February has 29 days. So=DAY(EOMONTH(feb1st,0))=29 will be true for leap years.

### #4 – February 1st and March 1st are not on same day of week

In non leap years, Feb has 28 days (a multiple of 7), so both Feb and March start on same day of week. So, =WEEKDAY(feb1st)<>WEEKDAY(mar1st) will be TRUE for leap years.

### #5 – Adding 365 to January 1st does not change year

Well, that is obvious too. =YEAR(jan1st)=YEAR(jan1st+365) is TRUE for leap years.

### #6 – 30th Day of February is March 1st

If an year is leap year, 30th day of February \[DATE(year,2,30)\] is same as March 1st. So, =DATE(year,2,30)=mar1st is TRUE for leap years.

### #7 – 0th Day of March is Feb 29th

In real world there is no zeroth day for any month. But in Excel, since all dates are numbers, 0th day refers to last day of previous month. So, =DAY(DATE(year,3,0))=29 will be TRUE in leap years.

### #8 – April 1st and January 1st are on same day of week

In leap years, there are 91 days between January 1st and April 1st. And since 91 is a multiple of 7, both April 1st and January 1st start on same day of week. Hence, =WEEKDAY(jan1st)=WEEKDAY(apr1st) will be true for leap years.

### #9 – Only 2 more months start on same day of week as January

In leap years, both April and July start on same day of week as January. (Where as in non-leap years, Only October starts on same day of week as Jan).

To test this, we will of course use the [SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
. like this:

\=SUMPRODUCT(–(WEEKDAY(DATE(year,ROW($A$2:$A$12),1))=WEEKDAY(jan1st)))=2

The portion WEEKDAY(DATE(year,ROW($A$2:$A$12),1)) gives all the first day of weeks from February to December. And then we just check how many of these are same as January 1st’s week day.

### #10 – Next year’s February 1st and this year’s February 2nd are NOT  on same day of week

In non-leap years, there are 364 days between February 2nd and next year’s February 1st. Since 364 is a multiple of 7, both of these days are on same day of week. Which is not the case in leap years (as the difference becomes 365). So, =WEEKDAY(feb1st+1)<>WEEKDAY(EDATE(feb1st,12)) will be TRUE for leap years.

### #11 – February 1st’s day of week occurs 5 times in that month

This a bit tricky to test, but then again we have SUMPRODUCT. So, =SUMPRODUCT(–(WEEKDAY(febDays)=WEEKDAY(feb1st)))=5 will be TRUE for leap years. The name **_febDays_** has all dates in February. I think the rest is easy to understand.

### #12 – February starts and ends on same day of week

29 days means both 1st and 29 are on same weekday. So, =WEEKDAY(feb1st)=WEEKDAY(EOMONTH(feb1st,0)) will be true for leap years.

### #13 – Spreadsheet day (October 17) and February 1st are on same day of week

_**Debra**_, who is a well known Excel blogger & author started the whole spreadsheet day thing. She says, we should celebrate [October 17 as spreadsheet day](http://spreadsheet-day.com/blog/about/)
. I love that idea, mainly because, it is just 3 days before my birthday and I like celebrations. And I also like Excel 🙂 So blame her if you do not like this way of testing for leap years.

In leap years, there are 259 days between February 1st and October 17. And since 259 is a multiple of 7 (and 37), we know that they are both on same day of week. So, =WEEKDAY(feb1st)=WEEKDAY(DATE(year,10,17)) is true for leap years.

### #14 – Finally, the year is divisible by 4 and if it is divisible by 100, then also by 400

Finally, we are going to test the whole “an year is leap year if it is divisible by 4 and if it is divisible by 100, then it is also divisible by 400” thing. This is a slightly tricky one to test. The formula, =((MOD(year,4)=0)\*((MOD(year,100)<>0)+(MOD(year,400)=0))=1) will be TRUE for leap years and false for non-leap years.

### Download Leap Year Test Workbook

[**Click here to download the workbook**](https://img.chandoo.org/d/leap-test.xlsx)
 with all these 14 examples. Play with the formulas, named ranges to understand these techniques.

### How do you check it is a leap year?

If you are working and you get paid on first day of a month, then one clear way of knowing leap year is that you get your salary one day later. Other than this, what method would you use to find if an year is leap year. Go ahead and be creative. **Share your ideas and formulas using comments.** Next leap day is 4 years away. _**Go**_

### Want to learn how to Dates & Times in Excel – Read these:

If you deal with data that has a lot of date / time stuff, then understanding various Excel features in this area is a must. Read below pages to learn more.

*   [10 tips on working with dates & times in Excel](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
    
*   [Calculate difference between 2 dates](http://chandoo.org/wp/2009/09/22/elapsed-time-excel/)
    
*   [Find thanksgiving day for any year](http://chandoo.org/wp/2009/11/25/findout-thanksgiving-date/)
    
*   [Check if 2 ranges of dates overlap](http://chandoo.org/wp/2010/06/01/date-overlap-formulas/)
    
*   [Rolling months in Excel](http://chandoo.org/wp/2010/04/06/rolling-months/)
    
*   [How to convert text to dates](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    
*   **[Even more on Excel dates & times](http://chandoo.org/wp/tag/date-and-time/)
    **

### Want to master Date & Other Excel Formulas?

If you want to learn how various formulas in this post work and know more about everyday Excel formulas, please consider joining my Excel Formula crash course. It has detailed video tutorials on more than 40 everyday Excel formulas and teaches you all the powerful techniques to become a formula ninja.

[**Click here to join our Excel Formula Crash Course**](http://chandoo.org/wp/training-programs/formula-crash-course/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [30 Comments](https://chandoo.org/wp/check-leap-year-using-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/check-leap-year-using-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [date](https://chandoo.org/wp/tag/date/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [day()](https://chandoo.org/wp/tag/day/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [eomonth](https://chandoo.org/wp/tag/eomonth/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [leap year](https://chandoo.org/wp/tag/leap-year/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [month](https://chandoo.org/wp/tag/month/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [weekday](https://chandoo.org/wp/tag/weekday/)
    , [year](https://chandoo.org/wp/tag/year/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to add your own Macros to Excel Ribbon \[quick tip\]](https://chandoo.org/wp/how-to-add-your-own-macros-to-excel-ribbon/)

[NextFormula Forensic 014 – Faseeh’s FormulaNext](https://chandoo.org/wp/formula-forensic-014/)

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
    
    [Reply](https://chandoo.org/wp/check-leap-year-using-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/check-leap-year-using-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/check-leap-year-using-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ