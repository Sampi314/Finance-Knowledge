# Relative References in Excel Tables » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/relative-references-in-excel-tables

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Relative References in Excel Tables
===================================

*   Last updated on April 21, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel Tables have been around for a decade now (they are introduced in Excel 2007), and yet, very few people use them. They are versatile, easy and elegant. At Chandoo.org, we celebrate Tables all the time. If you have never used them, start with below tuts.

*   [Introduction to Excel tables](http://chandoo.org/wp/2009/09/10/data-tables/)
    
*   [How to use structured referencing](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/)
    
*   [Tables and Relationships in Excel](http://chandoo.org/wp/2013/07/01/introduction-to-excel-2013-data-model-relationships/)
    
*   [Using lookups and other formulas with Excel tables](http://chandoo.org/wp/2010/11/09/using-lookup-formulas-with-excel-tables-video/)
    
*   [Simple way to get absolute references in Tables](http://chandoo.org/wp/2011/05/23/preserve-table-references-while-copying-formulas/)
    
*   [Customizing table styles for awesome usability](http://chandoo.org/wp/2012/09/19/custom-zebra-lines-table-styles/)
    

**While tables are super helpful, they do come with some limitations.** Today let’s examine one such unique problem and learn about an elegant solution.

Table Relative Reference Problem
--------------------------------

Imagine you are the machine supervisor at Mighty Machine City Inc. Although your machines are mighty, sometimes they do fail. To keep track of which machines are under repair, you maintain a _repair log_ in Excel. Since you heard Tables are mighty, you thought,

‘_Gee whiz, I might as well use tables to maintain the repair log. Chandoo says tables are sweet’_

So, your Repair log looks like this:

![repair-log-data](https://chandoo.org/wp/wp-content/uploads/2017/04/repair-log-data.png)

After a few days of tracking the repairs, you wanted to know if same machines are failing successively. For example, in above picture, you notice that MACH-0038 failed twice in a row starting with 11th of March. Same goes for few other rows.

You are the kind of person who frowns upon manually highlighting yellow color in cells to flag such successive failures. So you want to write a formula.

So you add a new column called **Same?** and want to fill it up with a simple relative reference formula to check with Machine in row 1 matches machine in row 2.

Here is the formula you used:

\=\[@\[Machine ID\]\] = B6

_Note:_ Your table starts with Row 5.

Excel automatically filled down the formula for all rows of the table, _because tables are awesome like that._

![repair-log-relative-ref-done-wrong](https://chandoo.org/wp/wp-content/uploads/2017/04/repair-log-relative-ref-done-wrong.png)

You whistled your way to home that night.

Next day morning, as usual _Homer messed up something_ and you had a new repair to log. So you went to the bottom of _fail_ table and inserted a new row to add the failure details.

And you notice something unusual.

![table-relative-refs-gone-wrong](https://chandoo.org/wp/wp-content/uploads/2017/04/table-relative-refs-gone-wrong.png)

_**The formula for Same? column is WRONG!!!**_

As soon as you inserted a new row, Excel adjusted last row’s formula to something silly.

*   **Before:** Let’s say the last row formula reads =\[@\[Machine ID\]\]=B20
*   **After:** The last but one row (as you now have an empty row)’s formula reads =\[@\[Machine ID\]\]=**B21**

Now that is clearly wrong!

**What is going on here?**

Your relative referencing worked ok, until the last row. At this stage, Excel _understood_ the formula as **Current row value = value in _first cell below table_**

The part in green is what caused trouble. As soon as you add a new row to your table, _fist cell below table_ is moved down. So Excel adjusted that reference alone.

**How to fix this problem?**

The usual method to fix this:

*   Insert as many rows as you need and complete entering / pasting all data.
*   Select the formula in very first cell.
*   Fill it down all the way (you can double click on the bottom right corner of the cell)

_**But that is soooo not awesome.**_

You are right. This method is manual and error prone. It is the opposite of awesome.

**Problems when you delete too:** In fact, if you ever delete a row from your table, the formulas further down would show #REF! errors. So this method is not very effective in real life.

### An elegant way to get relative references in tables

Instead of using cell address based references, like B6, if you use pure structured references, then Excel will automatically adjust them as your table grows or shrinks.

But how?

Simple, we can use OFFSET function along with @ references.

To get next machine ID, you can use

\=OFFSET(\[@\[Machine ID\]\],1,0)

So, to check if same machine failed twice in a row, use

\=\[@\[Machine ID\]\]=OFFSET(\[@\[Machine ID\]\],1,0)

![relative-refs-in-tables-solution](https://chandoo.org/wp/wp-content/uploads/2017/04/relative-refs-in-tables-solution.png)

As this uses no cell references, whenever you add / change / remove table rows, Excel automatically scales the formula.

**But I heard OFFSET is volatile / dangerous / RDX / %#$&@#?**

Unless your table has a 200k+ rows or you plan to set up 100s of columns like this, don’t bother. for small, day to day tables, there is no change in performance. If you really hate OFFSET, try talking about it during your next therapy session. Jokes aside, you can also use a longer INDEX based formula to get similar result, but that is semi-volatile too.

Here is one such INDEX based formula.

\=INDEX(\[@\[Machine ID\]\]:INDEX(\[Machine ID\],COUNTA(\[Machine ID\])), 2)

It sure is a mouthful. You can shorten it by using a named formula for INDEX(\[Machine ID\],COUNTA(\[Machine ID\])) portion or the whole thing. Again, I wouldn’t recommend the INDEX based approach over OFFSET for smaller data sets. For larger datasets, see if you can fix the problem at source (for example, modifying your SQL to get offset values in a separate column) or using Power Query to mash the data (more on this in a next post).

So there you go, an elegant and simple way to deal with the relative reference problem in tables.

### Bonus tip: generating running numbers in tables

You can use this approach to generate running numbers (1,2,3…) in a table column that grow / change / shrink based on your table. This can be very useful in many scenarios.

To get running numbers in a table column, just use:

\=ROWS(fail\[\[#Headers\],\[Machine ID\]\]:\[@\[Machine ID\]\])-1

The pattern that you can use in any table goes like this:

\=ROWS(Table\_Name\[\[#Headers\],\[Col 1\]\]:\[@\[Col 1\]\])-1

### Bonus Bonus tip: If you have running numbers in a column …

You can then change the OFFSET based relative ref to INDEX like below.

\=INDEX(\[Machine ID\],\[@Running\]+1)

This method is 100% non-volatile, but does return #REF! error for the last row. So use it with IFERROR when nesting in other formulas.

Download Example Workbook
-------------------------

[**Click here to download an example workbook**](https://chandoo.org/wp/wp-content/uploads/2017/04/relatively-speaking.xlsx)
 showcasing all these techniques. Use the extra data to paste and test various methods.

### How do you write relative refs in tables?

The handful times when I had to use relative refs in a table, I resorted to cell refs (like B6 above). But this created too much headache further down. So I switched to OFFSET / INDEX approaches.

**What about you?** How do you write relative references in tables? Please share your stories & struggles in the comments section.

### Related Reading (no pun)…

If you are relatively free and want some relaxed reading  then check out below related reference links.

*   An intro to [Excel relative references](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)
    , [structured references](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/)
    
*   [INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
    , [OFFSET formula](http://chandoo.org/wp/2012/09/17/offset-formula-explained/)
    , [ROWS formula](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
    

Happy learning.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/relative-references-in-excel-tables/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/relative-references-in-excel-tables/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [references](https://chandoo.org/wp/tag/references/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    , [structured references](https://chandoo.org/wp/tag/structured-references/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousModelling Inventory Run Rate & Cash Flows using Excel](https://chandoo.org/wp/model-inventory-cash-flows-excel/)

[NextAvoid Hiring Boo-boos with Excel – COUNTIFS for the win Next](https://chandoo.org/wp/avoid-hiring-boo-boos-with-excel-countifs-for-the-win-video/)

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
    
    [Reply](https://chandoo.org/wp/relative-references-in-excel-tables/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/relative-references-in-excel-tables/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/relative-references-in-excel-tables/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ