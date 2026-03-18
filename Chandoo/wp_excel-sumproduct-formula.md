# Excel SUMPRODUCT formula - Syntax, Usage, Examples and Tutorial

**Source:** https://chandoo.org/wp/excel-sumproduct-formula

---

*   [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

What is Excel SUMPRODUCT formula and how to use it?
===================================================

*   Last updated on December 7, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Today we will learn a new and exciting excel formula – the all powerful SUMPRODUCT.

At the outset SUMPRODUCT formula may not seem like all that useful. But once you understand how excel works with  lists (or arrays) of data, the SUMPRODUCT’s relevance becomes crystal clear.

### SUMPRODUCT formula – syntax and usage

![Excel SUMPRODUCT formula - tutorial](https://chandoo.org/img/n/excel-sumproduct-formula-tutorial.png)The sum-product formula syntax is very simple. It takes 1 or more arrays of numbers and gets the sum of products of corresponding numbers.

The syntax is `=SUMPRODUCT (list 1, list 2 ...)`

![Excel SUMPRODUCT formula - examples](https://chandoo.org/img/n/sumproduct-formula-example.png)So, for ex: if you have data like {2,3,4} in one list and {5,10,20} in another list, and if you apply SUMPRODUCT, you will get 120 (because 2\*5 + 3\*10 + 4\*20 is 120).

At this point it might seem like an almost useless function. But all that will change in the next 2 minutes, keep reading.

### SUMPRODUCT and Arrays

Lets say you have a list of sales data with columns Name, Region, Product and Sales. Now, you want to know how many units the sales person named “Luke” sold. This is simple, you will write a [SUMIF formula](http://chandoo.org/excel-formulas/sumif.html)
 \[[examples](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)\
\] and use the Name column as “criteria range” and Sales column as “sum range”.

But, wait a second, you want to find how many units sales person “Luke” sold in the region “west”.

Hmm…. we have 2 options,

*   Use an array formula
*   Use a pivot table \[[what is a pivot table?](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)\
    \]

Actually, there is a hidden third option, use SUMPRODUCT.

That is right, my friend, we can use SUMPRODUCT to do just this (and much more).

### Using SUMPRODUCT as an array formula

Assuming, the data is in range A1:D10, with Name in column A, Region in B, Product in C and Sales in D, the SUMPRODUCT formula is,

`=SUMPRODUCT(--(A1:A10="Luke Skywalker"),--(B1:B10="West"),D1:D10)`

Okay, lets take a minute and try to understand WTF (what the formula) is doing.

*   The portion `--(A1:A10="Luke Skywalker")`is looking for Luke Skywalker across planetary systems in all universes 😉 It is going to give us a bunch of ONEs and ZEROs, one if the cell has Luke, Zero if the cell has something else.
*   The portion `--(B1:B10="West")`is doing the same, but gets 1s when the value is “West”.
*   The portion `D1:D10` is just returning all the sales figures.
*   When you put everything together and multiply, it just works. _**Why?**_ That is your home work to figure out.

![Excel SUMPRODUCT formula example and explanation](https://chandoo.org/img/n/sumproduct-tutorial-and-help.png)

### Share your SUMPRODUCT formula Tips & Tricks

SUMPRODUCT formula can do much more once you understand how it works. This post is meant to open the door for you. Go ahead and explore the possibilities, then come back and share your tips with us.

### Recommended Reading

I suggest reading the [excel array formula examples](http://chandoo.org/wp/tag/array-formulas/)
, [sumif with multiple conditions](http://chandoo.org/wp/2009/07/22/sumif-with-multiple-conditions/)
 and other [excel formula tutorials](http://chandoo.org/wp/tag/formulas/)
.

_This post is part of our [spreadcheats](http://chandoo.org/wp/tag/spreadcheats/)
 series_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [254 Comments](https://chandoo.org/wp/excel-sumproduct-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-sumproduct-formula/#respond)
    
*   Tagged under [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [illustrations](https://chandoo.org/wp/tag/illustrations/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadcheats](https://chandoo.org/wp/tag/spreadcheats/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumif()](https://chandoo.org/wp/tag/sumif/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousPHD Gets a Facelift (again)](https://chandoo.org/wp/phd-gets-a-facelift-again/)

[NextChart this Sales Data and get an iPod Touch \[Visualization Challenge #2\]Next](https://chandoo.org/wp/visualizing-salesdata-challenge/)

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
    
    [Reply](https://chandoo.org/wp/excel-sumproduct-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-sumproduct-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-sumproduct-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ