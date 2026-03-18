# Calculating average of every nth value [Formula tips] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Calculating average of every nth value \[Formula tips\]
=======================================================

*   Last updated on September 5, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Lets say you have a large list of numbers, and you want to **calculate the average of every _nth_ value**. Not the average of all numbers, but just every _nth_ number.

That is what we will learn in next few minutes.

### Few assumptions

Before we jump in to any formulas, first lets assume that all your data is in a table, conveniently named as _tbl._ Lets say this table has below structure.

![Average of every nth value - calculating using Excel formulas.](https://img.chandoo.org/f/average-of-every-nth-value-excel-formulas.png)

Also, the value of n is a named cell **N**.

Average of every nth value
--------------------------

### Approach 1: Using helper columns

![Average of every nth value - calculated using Helper column](https://img.chandoo.org/f/average-of-every-nth-value-using-helper-column.png)If you have no allergies towards nuts, dairy or helper columns, then this approach is easiest.

We just add an extra column to our _tbl_ , called as _helper._

In the helper column, write this formula.

\=MOD(\[@ID\], N)=0

This will fill the helper column with TRUE & FALSE values, TRUE for all nth values, FALSE for everything else. See aside.

Once we have the helper column, calculating average of every nth value is easy as eating every slice of a cake.

We use AVERAGEIF to do this.

\=AVERAGEIF(tbl\[Value\],tbl\[Helper\],TRUE)

### Approach 2: Not using helper columns

Now things get interesting. Lets say you want to calculate average, but not use any helper columns.

**First the formula:**

\=AVERAGE(IF(MOD(tbl\[ID\], N)=0,tbl\[Value\]))

_Array entered._

**Lets understand how it works:**

We want the average of every nth item of tbl\[Value\] column.

In other words, we want average of every item of tbl\[Value\] column, whose corresponding tbl\[ID\] value is _perfectly_ divisible by n.

How do we know when a value is perfectly divisible by another?

Don’t worry. You don’t have to do the long division on paper now. Instead we use Excel’s MOD function.

When a value is perfectly divisible by another, the reminder is **zero.**

So, MOD(value1, value2) = 0 means, value2 divides value1 perfectly.

**That means…**

We want the average of tbl\[Value\] when MOD(tbl\[ID\], N) = 0

Lets write that in Excel formula lingo.

\=AVERAGE( IF(MOD(tbl\[ID\], N) = 0, tbl\[Value\]) )

This formula results in a bunch of values and FALSEs. Assuming N=3, this is what we get (for sample data):

\=AVERAGE({FALSE;FALSE;15;FALSE;FALSE;18;FALSE;FALSE;18;FALSE;FALSE;15;FALSE;FALSE;14; …})

Since AVERAGE formula ignores any logical values, it will calculate the average of {15, 18, 18, 15, 14 … } and returns the answer you are expecting.

As this formula is processing arrays instead of single values, you need to array enter it (CTRL+SHIFT+Enter after typing the formula).

### Bonus scenario: Average of FEBRUARY values only!

Here is a bonus scenario. Lets say you want to calculate the average sales of FEB alone… Then you can use AVERAGEIF (or AVERAGEIFS, if you want to have multiple conditions).

\=AVERAGEIF(tbl\[value\], tbl\[month\], “FEB”)

![Averageif() formula example - average of February values alone](https://img.chandoo.org/f/average-of-february-values.png)

Download example workbook:
--------------------------

[**Click here to download the example workbook**](https://img.chandoo.org/f/average-of-every-nth-value.xlsx)
. It contains all the techniques explained in this post. Play with the data & formulas to understand better.

### Time for some challenges…

If you think averaging every nth value is not mean enough, try below challenges. Post your answers using comments.

1.  Write a formula to calculate average of every nth value, _**starting at row number ‘t’**_.
2.  Write a formula to calculate average of every nth value, assuming your table has only value column (no ID column).

Go ahead. Show off your formula skills. Post your answers in comments section.

### Improving your Excel batting average

Calculating averages predates slice bread. Folklore says that when first neanderthal figured out how to express numbers and carved 2 of them on a cave wall, his manager walked by and asked “What is the average of these two? Eh?” and thumped her chest.

Although caves & wall carvings are replaced by cubicles & spreadsheets, we are still calculating averages, almost 2.9 million of them per hour.

So it pays to learn a few tricks about Excel Average formulas. Check out below to improve your average:

*   [Calculating Moving Average](http://chandoo.org/wp/2009/04/28/calculate-moving-average/)
    , [Weighted Average](http://chandoo.org/wp/2010/06/15/weighted-average-excel/)
    
*   [Average of top 5 values](http://chandoo.org/wp/2010/06/04/average-of-top-5-values/)
    
*   [Show averages & distribution in your charts](http://chandoo.org/wp/2011/04/06/show-average-and-distribution/)
    
*   [Using SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
     (same tricks apply to AVERAGEIF, AVERAGEIFS too)

If your boss is the kind who thumps her chest and mocks you for your poor Excel skills, don’t cave in. Fight back. [**Enroll in Excel School**](http://chandoo.org/wp/excel-school/)
 and show that you can evolve.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [16 Comments](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [average()](https://chandoo.org/wp/tag/average/)
    , [averageifs](https://chandoo.org/wp/tag/averageifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousSort by Birthday \[Quick tip\]](https://chandoo.org/wp/sort-by-birthday-quick-tip/)

[NextFormula Forensics No. 34. Extract words from a cell, where they occur in a list of words.Next](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/)

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
    
    [Reply](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ