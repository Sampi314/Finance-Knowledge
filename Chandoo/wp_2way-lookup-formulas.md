# How to write 2 Way Lookup Formulas in Excel? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/2way-lookup-formulas

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to write 2 Way Lookup Formulas in Excel?
============================================

*   Last updated on November 9, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This article is part of our VLOOKUP Week. [Read more](http://chandoo.org/wp/tag/vlookup-week/ "VLOOKUP Week @ Chandoo.org - Learn tips on lookup formulas in Excel")
.

### Situation

So far we have seen [what VLOOKUP formula is](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 and [how to put it to some nifty uses](http://chandoo.org/wp/tag/vlookup-week/ "VLOOKUP Formula and its uses")
. Today, we will go one step further and learn how to do 2 Way Lookups.

**What is a 2 Way Lookup?**

![Data for this Example -](https://img.chandoo.org/f/vw/2-way-lookup-formulas-in-excel.png)

Lookup is when you find a value in one column and get the corresponding element from other columns. **2 Way Lookup is when you lookup value at the intersection corresponding to a given row & column values.**

For example, assuming you have data like below, and you want to findout how much sales _Joseph_ made in month of _March_, you are essentially doing a 2 way lookup.

**Data:**

![Data for this Example -](https://chandoo.org/img/f/vw/vloookup-from-multiple-columns-data.png)

### Solution

**While the problem may seem complicated, the solutions to two way lookups are surprisingly simple.** In this post, I will review 4 different ways to write 2 way lookup formulas.

### Keep this in mind:

*   I use various named ranges in the below examples. `valSalesPerson` and `valMonth` refer to the name of sales person & month we are looking for. `lstSalesPerson` and `lstMonth` refer to the list of sales persons (first column) and list of months (first row). `tblData` has the sales figures for everyone.

### Technique 1 – Using INDEX & MATCH Formulas

If you know the row number and column number in a given table, you can use INDEX formula to get the element at the intersection. And we can use MATCH formula to find the position of an value in a list. Combining both,

`=INDEX(tblData,MATCH(valSalesPerson,lstSalesPerson,0),MATCH(valMonth,lstMonth,0))` is the formula we use to get the sales amount of `valSalesPerson` for `valMonth`.

### Technique 2 – Using Named Ranges & Intersection (SPACE) Operator

Do you know that you can write `=range1 range2` to get the value(s) at the intersection of `range1` & `range2`? That is right, excel has an intersection operator. I will write more about this some other time. In the meanwhile, watch this short video to understand how you can use named ranges & intersection operator to perform 2 way lookups.

\[[Watch the video on Youtube](http://www.youtube.com/watch?v=_kF73uvOhA4)\
\]

However, you need to create named ranges for your data all the time. A simpler alternative is to [use Excel 2007 Tables feature](http://chandoo.org/wp/2009/09/10/data-tables/)
 so the names are created for you automatically.

### Technique 3 – Using SUMPRODUCT Formula

**This is an absolute beauty**. Thanks to [Vipul](http://bit.ly/vipulrawal)
 for teaching me this superb trick.

You can use SUMPRODUCT to get the value at intersection like this: `=SUMPRODUCT((lstSalesPerson=valSalesPerson)*(lstMonth=valMonth),tblData)`

How does it work? Simple, When you write `(lstSalesPerson=valSalesPerson)*(lstMonth=valMonth)`, _**SUMPRODUCT generates a lot of zeros and a one at the intersection**_. When you use `tblData` as second argument, the result is value at intersection.

### Technique 4 – Using VLOOKUP with MATCH Formula

A much simpler and easy to remember alternative. You can simply write `=VLOOKUP(valSalesPerson,$B$5:$N$17,MATCH(valMonth,lstMonth,0)+1,FALSE)` to fetch the value for a corresponding month.

### Review of 2 Way Lookup Techniques

**![Writing 2 way lookup formulas in MS Excel - 4 different examples](https://chandoo.org/img/f/vw/2way-lookup-formula-examples-excel.png)  
**

### Sample File

[Download Example File – 2 Way Lookup Formulas in Excel](https://img.chandoo.org/f/vw/2-way-lookup-formulas.xls)

Go ahead and download the above file. It contains all the examples. Play with them to learn the 2 way lookup formulas better.

PS: Also [download this beautiful example file](https://img.chandoo.org/f/vw/2way-lookup-demo-matias.xlsx)
 that [Matias](http://www.masemprendedor.com/)
 has kindly shared with me. It shows how to use INDIRECT formula along with Excel Tables to do 2way lookups.

### Special Thanks to

[Vipul](http://chandoo.org/wp/2010/10/05/bad-news-vlookup-contest/#comment-131421)
, [Spotpuff](http://chandoo.org/wp/2010/10/05/bad-news-vlookup-contest/#comment-131473)
, [judgepax](http://chandoo.org/wp/2010/10/05/bad-news-vlookup-contest/#comment-131483)
, [Bryan](http://chandoo.org/wp/2010/10/05/bad-news-vlookup-contest/#comment-131821)
 for the tip. (Click on the name to see their tip)

### Similar Tips

*   [Excel SUMPRODUCT Formula – What is it, how to use it & examples](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   [How to Lookup Values to the Left – Using INDEX + MATCH Formulas](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    
*   [Range lookup – finding the corresponding range for a value](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
    

[![VLOOKUP Week @ Chandoo.org - Learn tips on lookup formulas in Excel](https://cache.chandoo.org/images/f/vlookup-week-articles.png)](http://chandoo.org/wp/tag/vlookup-week/ "VLOOKUP Week @ Chandoo.org - Learn tips on lookup formulas in Excel")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [53 Comments](https://chandoo.org/wp/2way-lookup-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/2way-lookup-formulas/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [intersection operator](https://chandoo.org/wp/tag/intersection-operator/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [vlookup week](https://chandoo.org/wp/tag/vlookup-week/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousUsing Lookup Formulas with Excel Tables \[Video\]](https://chandoo.org/wp/using-lookup-formulas-with-excel-tables-video/)

[NextGetting the 2nd matching value from a list using VLOOKUP formulaNext](https://chandoo.org/wp/vlookup-second-value/)

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
    
    [Reply](https://chandoo.org/wp/2way-lookup-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/2way-lookup-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/2way-lookup-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ