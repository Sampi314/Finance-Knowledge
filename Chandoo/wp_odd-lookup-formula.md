# An odd lookup problem [Formulas] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/odd-lookup-formula

---

*   [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

An odd lookup problem \[Formulas\]
==================================

*   Last updated on December 6, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Let’s say you have some employee data in employee name, manager name format. But the data is all in one column, with odd rows containing employee names & even rows containing manager names. Something like this.

![odd-lookup-problem](https://chandoo.org/wp/wp-content/uploads/2016/12/odd-lookup-problem.png)

_**And you want to find out who is the boss for a given employee. Say, “Andrea Nichols”.**_

Your regular MATCH() formula for Andrea over the data range returns wrong answer as it will find first occurrence of Andrea (which in this case happens to be on even row, _hence_ a manager record).

_**So how would you write the lookup formula?**_

### Odd Lookup formula:

Let’s assume your data starts at B4 and goes for 200 cells (_ie_ 100 employee and 100 manager names), and the employee name you want to lookup is in cell F4.

We can find the position of the employee using below MATCH formula. (Array formula, so press Ctrl+Shift+Enter after typing it)

`=MATCH(F4,T(OFFSET($B$4,ROW($A$1:$A$100)*2-2,,1,1)),0)`

This will give us the position of employee (ie 3 for Andrea Nichols in the sample data image above).

Once we have the position, we can use below INDEX formula to get the manager’s name.

`=INDEX($B$4:$B$203,_position_*2)`

**How do these formulas work?**

The INDEX formula is fairly obvious. So let’s dig deep in to the MATCH formula.

1.  **First we extract all the odd cells** in the range B4:B203 using `OFFSET($B$4,ROW($A$1:$A$100)*2-2,,1,1))` part. The `ROW(A1:A100)` portion generates an array of numbers from 1 to 100 which we then convert to even numbers using simple arithmetic.
2.  **We then use `T()` formula** to convert the odd cell values in to an array of text values.
3.  Finally MATCH() looks for the employee name in F4 against this list to find the matching position.

Please refer to [OFFSET tutorial](http://chandoo.org/wp/2012/09/17/offset-formula-explained/)
 & [INDEX formula tutorial](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 to understand the syntax and array usages.

**How to make these formulas generic:**

In our formulas above, we use a fixed range A1:A100 to generate the even numbers. If you have different sized list, you can use below generic version of the ROW formula.

_Assuming your list is named **list**:_

Replace the ROW() formula above with below version:

`ROW($A$1:OFFSET($A$1,COUNTA(list)/2,,))`

### Download example workbook

[**Click here to download example workbook for odd lookup problem**](https://chandoo.org/wp/wp-content/uploads/2016/12/lookup-odd-rows-only.xlsx)
. Play with the formulas in cells F5 & F6 to learn more.

### How would you lookup odd values…

Bad data is everywhere. Recently, I have come across a data set that is precisely like this. I ended up using the above pattern to find the answer quickly.

_**What about you?** How would you lookup odd values?_ Please share your approach in the comments section.

### Even more odd data problems? We got you covered

Don’t let dirty data drag you down. Check out below resources to learn more.

*   [Introduction to Excel VLOOKUP formula](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
    
*   [Multi-condition lookups](http://chandoo.org/wp/2014/10/28/multi-condition-vlookup/)
    
*   [VLOOKUP second or third (or nth) match](http://chandoo.org/wp/2010/11/10/vlookup-second-value/)
    
*   [Lookup the answer in matrix](http://chandoo.org/wp/2014/11/04/looking-up-when-the-data-wont-co-operate-case-study/)
    
*   [Lookup discounted pricing tier](http://chandoo.org/wp/2015/12/01/pricing-tier-lookup-formula/)
    
*   [Range lookup – find out which range contains the answer](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/odd-lookup-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/odd-lookup-formula/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [t()](https://chandoo.org/wp/tag/t/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSorting to your Pivot table row labels in custom order \[quick tip\]](https://chandoo.org/wp/pivot-table-custom-sort-order/)

[NextMerry Christmas & Happy New Year 2017 \[Holiday Greeting\]Next](https://chandoo.org/wp/2017-holiday-greeting/)

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
    
    [Reply](https://chandoo.org/wp/odd-lookup-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/odd-lookup-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/odd-lookup-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ