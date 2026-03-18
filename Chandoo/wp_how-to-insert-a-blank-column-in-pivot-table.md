# How to insert a blank column in pivot table? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to insert a blank column in pivot table?
============================================

*   Last updated on April 15, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know [pivot table functionality](http://chandoo.org/wp/excel-pivot-tables/ "Guide to Excel Pivot Tables")
 is a powerful & useful feature. But it comes with some quirks. For example, we cant insert a blank row or column inside pivot tables.

So today let me share a few ideas on how you can insert a blank column.

### But first let’s try inserting a column

Imagine you are looking at a pivot table like this.

![insert-blank-columns-in-pivot](https://chandoo.org/wp/wp-content/uploads/2015/04/insert-blank-columns-in-pivot.png)

And you want to insert a column or row. Go ahead and try it. Here is what happens.

*   Excel gets mad thinking you are attempting anarchy and throws a stern, but very long & confusing warning message.

In fact the error message is so long, I can’t even fit it in one image on this blog. Here it goes, verbatim.

![pivot-table-insert-column-warning-message](https://chandoo.org/wp/wp-content/uploads/2015/04/pivot-table-insert-column-warning-message.png)

### So how DO we insert a column in the pivot

The answer is simple.

_**Don’t**_

Don’t bother inserting the columns in actual pivot table. Instead, follow this approach.

1.  Select any cell in the pivot
2.  Press Ctrl+Shift+8 – This selects the entire pivot
3.  Copy it by pressing CTRL+C
4.  Go to a new worksheet
5.  Paste as references – ALT+CTRL+V and L
6.  Select any cells containing 0 and press DELETE key
7.  Now, go ahead and insert any number of columns & rows in this new worksheet
8.  When your pivot changes (either due to refresh or new data), the copy worksheet changes too
9.  Bonus: You can format the new worksheet cells any way you want. It just works.

**Here is an example of what you can do.**

![example-pivot-with-blank-columns](https://chandoo.org/wp/wp-content/uploads/2015/04/example-pivot-with-blank-columns.png)

### But I want to insert a column in my pivot!!!

Okay, clearly you have a case of OCDIS (Obsessive Column Deletion / Insertion Syndrome).

Here is one way to _technically_ insert a column inside the pivot table.

Before understanding the process, let’s pause and ask, “why do you want to insert a column?”

Here are few possible reasons.

1.  Cosmetic / formatting reasons. A blank column makes things easy to read
2.  To add commentary / notes / extra data
3.  To perform intermediate calculations on the data

If your answer is 1, the above approach (copying pivot and pasting as references) gives you most control over the layout and formatting. Go for it.

If your answer is 2, again above approach is still good.

If your answer is 3, you can use calculated item / fields is your best option.

_If your answer is 3 & you are using Excel 2013 (or power pivot)_, you can use either Sets feature or MDX formulas to mimic blank rows. Unfortunately, I can’t explain this because squirrels know more MDX than me.

### Let’s say you want to calculate certain percentage or similar…

Okay, so want to calculate North / West % in below pivot.

![calculated-items-in-pivot-tables-explained](https://chandoo.org/wp/wp-content/uploads/2015/04/calculated-items-in-pivot-tables-explained.png)

In this case, you can use calculated items feature of pivot table like this.

1.  Select any region name in the column labels are of pivot
2.  Go to Home > Insert > Calculated Item
3.  Give your calculated item a name like “North by West %”
4.  Write the formula =North / West
    
    ![create-calculated-items](https://chandoo.org/wp/wp-content/uploads/2015/04/create-calculated-items.png)
    
5.  Click ok
6.  This new column will added to your pivot, like this:

![calculated-items-example](https://chandoo.org/wp/wp-content/uploads/2015/04/calculated-items-example.png)

As you can see, it works fine _**until we hit the grand total row**_. There our North / West % should be 96%. Instead it reads 386%. Clearly a number calculated by my 6 year old son.

**Why is the total wrong?** Because, pivot table grand totals are a simple sum of all the above values. So Excel went ahead and added up the four percentages.

**How to fix this?** One simple options is to turn off the grand totals. Note that even row level grand totals are off as the % was added to actual values.

If you must see the grand totals, then your best bet is to use Power Pivot. It allows you to define formulas (using DAX) and create powerful pivot tables.

*   [Introduction to Power Pivot](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/)
    
*   [Introduction to DAX formula writing](http://chandoo.org/wp/2013/01/28/introduction-to-dax-formulas-measures-for-power-pivot/)
    
*   [Learn Power Pivot online](http://chandoo.org/wp/resources/learn-power-pivot/)
    

### So no easy way to insert columns then?

It took us a few minutes to get here, but that is the answer. There is no simple work around to this problem. Instead, here is a 4 step process you should follow.

1.  Take a few deep breaths
2.  Insert your favorite expletive in this sentence “\_\_\_\_\_\_ pivot tables” and shout it.
3.  Use Power Pivot
4.  If Power Pivot cant be used, copy the pivot as references and manipulate the layout as you wish.

Happy pivoting.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/#respond)
    
*   Tagged under [calculated items](https://chandoo.org/wp/tag/calculated-items/)
    , [formatting](https://chandoo.org/wp/tag/formatting/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Links – PASS BA 2015 Edition](https://chandoo.org/wp/excel-links-pass-ba-2015-edition/)

[NextFind and Highlight all blank cells in your data \[Excel tips\]Next](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/)

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
    
    [Reply](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ