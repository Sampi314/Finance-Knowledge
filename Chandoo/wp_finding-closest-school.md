# Finding the closest school [formula vs. pivot table approach] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/finding-closest-school

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Finding the closest school \[formula vs. pivot table approach\]
===============================================================

*   Last updated on November 18, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**First a quick personal update:** There has been a magnitude 7.8 earth quake in NZ on 14th November 2016 early morning. It is centered in Kaikoura, which is about 250 km away from Wellington. We did feel several shakes and after shocks. It has been an interesting and often scary experience. But my family is safe. I feel very sad for the all the damage and the loss for families in NZ. If you suffered from this quake, My prayers and thoughts are with you._

Yesterday, a friend asked me an interesting question. He has school distance data, like below. He wants to know which is the closest school for each school.

![school-data](https://chandoo.org/wp/wp-content/uploads/2016/11/school-data.png)

There are a few ways to answer this question. Let’s examine two approaches – [formulas](http://chandoo.org/wp/2013/01/16/top-10-formulas-for-aspiring-analysts/)
 & [pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
 and see the merits of both.

Formulas to find closest school
-------------------------------

All the distance data is in a table named _dist._ 

Assuming you have school names & types in cells H5, I5, we want to find out the closest school of any type and same type in adjacent columns, as shown  below.

![closest-school-calc](https://chandoo.org/wp/wp-content/uploads/2016/11/closest-school-calc.png)

Let’s take a look at the formulas first. All of these are array formulas. So press CTRL+Shift+Enter after typing.

*   J5: **Closest School Distance (Any type):** \=MIN(IF(dist\[From\]=H5,dist\[Distance\]))
*   K5: **Closest School Name (Any type):** =INDEX(dist\[To\],MATCH(H5&J5,dist\[From\]&dist\[Distance\],0))
*   L5: **Closest School Distance (Same type):** \=MIN(IF(dist\[From\]=H5,IF(dist\[To Type\]=I5,dist\[Distance\])))
*   M5: **Closest School Name (Same type):** \=INDEX(dist\[To\],MATCH(H5&L5,dist\[From\]&dist\[Distance\],0))

### How do these formulas work?

Let’s examine them one at a time.

**Closest School Distance (Any type)**

**Formula:** \=MIN(IF(dist\[From\]=H5,dist\[Distance\]))

**How it works:** 

*   We check if From school is same as the one in H5 and get the corresponding distances only.
*   This will return a bunch of distances and FALSE values. Distances will be listed only for the schools that match H5, for all others, the IF() gives FALSE.
*   We then pass this list to MIN formula to find the minimum distance.

As we are using arrays inside IF formula, we must press Ctrl+Shift+Enter to get correct results.

Related: [Learn more about MAXIF & MINIF formulas](http://chandoo.org/wp/2012/01/24/formula-forensics-no-008/)
.

**Closest School Distance (Same type)**

**Formula:** \=MIN(IF(dist\[From\]=H5,IF(dist\[To Type\]=I5,dist\[Distance\])))

**How it works:** 

*   We check if From school is same as the one in H5 and if the \[To Type\] is same as I5 and get the corresponding distances only.
*   This will return a bunch of distances and FALSE values. Distances will be listed only for the schools that match H5 and of type I5, for all others, the IF() gives FALSE.
*   We then pass this list to MIN formula to find the minimum distance.

**Finding the corresponding school name:**

Once we know the minimum school distance, we just use array MATCH to find corresponding school number and get the name of the school with an INDEX().

\=INDEX(dist\[To\],MATCH(H5&J5,dist\[From\]&dist\[Distance\],0))

As we are concatenating two lists in the MATCH formula, we need to press Ctrl+Shift+Enter to get correct results.

We use same logic to fetch school name for the distance in column L too.

Related: [Learn about multi-condition lookups](http://chandoo.org/wp/2010/11/02/multi-condition-lookup/)

### Formula approach – comments

While the formula approach gives answers we want, it is very tricky to write these formulas. The MIN(IF(…)) structure is not easy to master.

As the formulas check entire data, they can be very slow on large sets.

Pivot table to find closest school
----------------------------------

First create a pivot table from the _dist_ table with below settings:

*   Add From and From type to row labels area
*   Add To and To type to column labels area
*   Add distance to values area, summarize it by SUM
*   Remove sub totals & grand totals
*   Set up pivot in tabular layout

We get this.

![school-distances-pivot](https://chandoo.org/wp/wp-content/uploads/2016/11/school-distances-pivot.png)

At this stage, finding closest school gets easy. We simply use SMALL formula on each pivot table row to find 2nd smallest value (because smallest value is 0 and we should ignore it.) to get the distance. Finding school name is a simple matter of [using INDEX + MATCH](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
.

Of course, finding the distance for closest school of same type still requires using array version of [SMALL](http://chandoo.org/excel-formulas/small.shtml)
 with SMALL(IF(…)) structure. But this formula would be significantly faster as we don’t process all the 10000 rows of data.

### Comments on Pivot Table approach

Pivot table approach simplifies the problem and helps us answer the questions faster. You can also apply conditional formatting on top of Pivot Table to instantly highlight closest school(s).

Download example workbook
-------------------------

[**Click here to download the closest school example workbook**](https://chandoo.org/wp/wp-content/uploads/2016/11/closest-school-v1.xlsx)
. Play with the formulas & pivot table to learn more. Examine the conditional formatting rules for some cool techniques.

### How would you find the closest school?

By asking your neighbors, _of course_. Jokes aside, how would you find the closest school for a given school? Would you use formulas or pivot tables or some other approach? Please share your thoughts in the comments.

### Need to learn, here is your closest school

If you need to master Excel, look no farther. Excel School, your closest and most awesome online class makes you, well, awesome in Excel. Learn from basics to advanced concepts, all from the comfort of your office or home. There are over 50 lessons and dozens of sample workbooks to make you an Excel pro.

[**Check out Excel School program and join us today**](http://chandoo.org/wp/excel-school/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/finding-closest-school/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/finding-closest-school/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [minif](https://chandoo.org/wp/tag/minif/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousCan you solve this blood pressure problem? \[IF Formula Homework\]](https://chandoo.org/wp/bp-category-problem/)

[NextWe Want Your IdeasNext](https://chandoo.org/wp/we-want-your-ideas-2/)

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
    
    [Reply](https://chandoo.org/wp/finding-closest-school/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/finding-closest-school/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/finding-closest-school/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ