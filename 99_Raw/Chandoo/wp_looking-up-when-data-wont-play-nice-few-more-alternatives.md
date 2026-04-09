# Looking up when data won't play nice - few more alternatives » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Looking up when data won’t play nice – few more alternatives
============================================================

*   Last updated on November 12, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently, we discussed about the [case of unwieldy data and how we lookup what we want](http://chandoo.org/wp/2014/11/04/looking-up-when-the-data-wont-co-operate-case-study/ "Looking up when the data won’t co-operate (case study)")
 using formulas like SUMIFS. Today, let us learn few more ways to solve the same problem.

### First, a re-cap of the problem:

Here is a data-set:

![2D Lookup problem - Example dataset](https://img.chandoo.org/f/2d-lookup-problem-data-structure.png)

### The problem – build a lookup formula

And the problem. Oh, simple. Write a lookup formula to find how many customer walk-ins we have on any given day.

In the [previous article](http://chandoo.org/wp/2014/11/04/looking-up-when-the-data-wont-co-operate-case-study/ "Looking up when the data won’t co-operate (case study)")
, we discussed how to use [SUMIFS](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/ "Introduction to Excel SUMIFS Formula")
 to solve this problem. There were several amazing & awesome solutions shared by our readers in the comments section too.

### Suitable structure spawns simple solutions

Poorly structured is the 2nd biggest problem of analysts. The first one is _not enough coffee._ That is why there is a dictum in the data analytics world.

> Structure is everything

So, we can _easily_ solve our lookup problem, if our data were to magically re-arranged in 2 column fashion – Data & Value.

![Transforming data to solve problem easily - Example](https://img.chandoo.org/f/transforming-2d-data-using-formulas-or-vba.png)

This transformation can be done in 2 ways:

### Option #1: Transforming Data – Using Formulas

We can use data fetching formulas like [OFFSET](http://chandoo.org/wp/2012/09/17/offset-formula-explained/ "OFFSET formula – Explained")
 or [INDEX](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
 to re-arrange data in 2 columns.

Assuming,

*   Our 2D data is in a named range _data_,
*   There are running numbers starting with 0 in the cell J5

We can use below formula to fetch first column:

`=IFERROR(INDEX(data,2*(INT(J5/7))+1,MOD(J5,7)+1),"")`

for the second column, below formula works:  
`   =IFERROR(INDEX(data,2*(INT(J5/7)+1),MOD(J5,7)+1),"")`

**How does this formula work?**

I will explain the formula for first column. Deciphering 2nd column formula is your homework.

Here is the formula again: `=IFERROR(INDEX(data,2*(INT(J5/7))+1,MOD(J5,7)+1),"")`

Before understanding the formula, let’s take a minute to examine the structure of  our raw data.

*   Odd rows contain dates
*   Even rows contain values
*   There are 7 columns in total
*   So to get the first date, we need to go to row 1 (first odd number), column 1
*   To get the first value, we need to go to row 2 (first even number), column 1
*   But to get 8th date, we need to go to row 3(2nd odd number), column 1
*   So on

Let’s go from inside out.

*   **`2*(INT(J5/7))+1` portion:** This gives row number (_ie odd number_). J5 refers to running number and its value is 0. So we get 2\*(INT(0/7))+1 = 1
    *   This will be 3 when J5 becomes J12 (ie 8th date)
*   **`MOD(J5,7)+1` portion:** This gives column number. It will result in values 1 thru 7 in a cyclical fashion. Thanks to [MOD](http://chandoo.org/excel-formulas/mod.shtml)
    .
*   **`INDEX(data, ..., ...)` portion:** Now that we have both row & column numbers, INDEX formula kicks in and gets the corresponding date.
*   **`IFERROR(INDEX(...),"")` portion:** This is to help in case we ran out of all dates & values in our INDEX formula. Read [about IFERROR here](http://chandoo.org/wp/2011/03/11/iferror-formula/ "IFERROR Excel Formula – What is it, syntax, examples and howto")
    .

Once you have the formulas for first date & value, simply drag them to get rest of the values.

### Option #2: Transforming data – Using VBA

**[VBA Macros](http://chandoo.org/wp/excel-vba/)
** are perfect for scenarios like this. Usually transformation is something you need to do every-time you import data from external systems. So simply write a macro that can do this automatically.

Assuming our data is in the range _data_ and the first cell of our extraction range is _startHere,_ you can use below macro:

    
    Sub rearrangeData()
        'takes the values in DATA named range and rearranges them
        'from the named cell startHere
    
        Dim cell As Range, i As Long, j As Long, evenRow As Boolean, firstRow As Long
        
        i = 0
        j = 0
        firstRow = Range("data").Cells(1).Row
        
        For Each cell In Range("data")
            evenRow = (cell.Row - firstRow + 1) Mod 2 = 0
            If evenRow Then
                Range("startHere").Offset(j, 1).Value = cell.Value
                j = j + 1
            Else
                Range("startHere").Offset(i, 0).Value = cell.Value
                i = i + 1
            End If        
        Next cell
    End Sub
    

**How does this macro work?**  
Before jumping in to the lines of code and demystifying the logic, Let’s understand what we need to do:

1.  For each cell of data,
    1.  If it is in odd row, put the cell data in Date column at end
    2.  Else, put the cell data in Value column at end
2.  Repeat

This is what our code is trying to do.

Let’s examine the For Each loop, as this is the most critical part of our macro.

*   For each cell in the range _data_
*   We check if we are in evenRow using simple arithmetic on row numbers
*   If we are in evenRow then
    *   We put the cell value in row j (number of values so far), column 2
    *   We increment j
*   Else
    *   We put the cell value in row i (number of dates so far), column 1
    *   We increment i
*   Close the IF condition
*   We check for next cell in the _data_ range

### Advantages of Transformation over SUMIFS approach

Both options for transforming data have few advantages:

*   They work with any type of data (unlike SUMIFS, which works only for numeric lookups and has few other issues)
*   Once data is restructured, you can do other types of analysis like creating pivot tables, adding extra calculated columns etc. easily.

Download Example Workbook
-------------------------

[**Click here to download example workbook**](https://img.chandoo.org/f/2d-data-lookup-formula-alternatives.xlsm)
 that shows original SUMIFS solution, both options for transforming data & few other formulas. Play with it to learn more. Check out the code by pressing ALT+F11.

### How would you transform data?

My favorite techniques for transforming data are – VBA, formulas, Power Query, pivot tables & SQL. Depending on the situation, time availability, where my data is, I choose one of these options to scrub my data.

**What about you?** How do you clean up / scrub data like this? Please share you thoughts & tips with us in comments.

### Instructions for washing your dirty data

If your work involves scrubbing dirty data, check out below tutorials too:

*   [Extract numbers from text using VBA](http://chandoo.org/wp/2012/06/26/extract-numbers-excel-vba/)
     and [formulas](http://chandoo.org/wp/2012/06/19/extract-numbers-from-text-excel/)
    
*   [Filling blank cells with above values in tables](http://chandoo.org/wp/2011/10/17/fill-blank-cells-in-a-table/)
    
*   [Cleaning up in-correctly formatted dates](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    
*   [Fixing in-correctly formatted phone numbers](http://chandoo.org/wp/2008/09/30/clean-up-incorrectly-formatted-phone-numbers-using-excel/)
    
*   [Reverse a list using INDEX formula](http://chandoo.org/wp/2009/11/19/reverse-a-list-in-excel/)
    
*   [Transpose a table using formulas](http://chandoo.org/wp/2013/02/01/transpose-table-excel-formula/)
    

  

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [9 Comments](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [for loop](https://chandoo.org/wp/tag/for-loop/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [INT()](https://chandoo.org/wp/tag/int/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousFormula Forensics No. 003b – Lukes Reward – Part II](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/)

[NextDownload today – Introducing Excel Dashboard Templates from Chandoo.orgNext](https://chandoo.org/wp/introducing-excel-dashboard-templates/)

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
    
    [Reply](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ