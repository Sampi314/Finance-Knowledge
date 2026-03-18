# List.Accumulate() to replace multiple values in a text » Power Query Tips

**Source:** https://chandoo.org/wp/multiple-find-replace-list-accumulate

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Multiple Find Replace with Power Query List.Accumulate()
========================================================

*   Last updated on May 14, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Imagine you have a paragraph of text and you want to replace all occurrences of {four, normal, mysterious, nonsense} with {six, casual, confounding, handbags}. **How would you do that?**

You could use SUBSTITUTE() formula, but you need to nest four of them (as we need to replace four values with another four). But what if you have larger set of find / replacements?

Worry not, you can use Power Query to transform original text to new one by replacing all matching values.

In this page, learn how to do that with the excellent **List.Accumulate()** Power Query function.

![multiple find replace text values - using Power Query's List.Accumulate() function](https://chandoo.org/wp/wp-content/uploads/2020/05/multiple-find-replace-text-values.jpg)

The set up for multiple find / replace
--------------------------------------

Let’s start with two tables – **mytext** with the original text values and **replacements** with rules for replacement.

I have included a snapshot of these tables below.

[](https://chandoo.org/wp/wp-content/uploads/2020/05/original-text-for-many-find-replace.png)
[](https://chandoo.org/wp/wp-content/uploads/2020/05/find-replace-mapping-table.png)

Power Query transformations
---------------------------

Start by loading both of these tables to Power Query. We will _transform_ mytext table to add a column with replaced text.

Before we could do the transformations, **you must learn 3 key concepts**.

They are,

1.  List.Accumulate() Function
2.  Getting Lists from Table columns
3.  How to access individual list items

If you know these three concepts, skip ahead to next section. Else, read on.  

Key concepts for multiple find replace

### List.Accumulate() Function

**List.Accumulate()** function allows us to perform same action on items on a list and return a combined value.

A simple example for this is,

Imagine you have a list of 10 numbers {1..10}

You want to calculate the total of these numbers.

You can use List.Accumulate() to add them up. _Of course, you can also use List.Sum() function, but this is a demo of List.Accumulate() dear._

Assuming the original list is in **source,** we can use List.Accumulate() to add up items like this:

\=List.Accumulate(Source, 0, (state, current) => state+current)

The output of this step will be 55, sum of list with first 10 numbers.

🤯🤯🤯

**What’s going on here?**

List.Accumulate() is a **cumulative function.** It takes a list and a starting value (in our case these are **source** and **0**) and applies a function on each of the list items while modifying the **initial value.**

Let’s see what that means for our list.

*   We start with 0 (call this starting **state**)
*   For each item in the list
    *   Update state to state + current (_ie_ 0+1 initially, then 1+2, 3+3, 6+4…45+10)
*   At the end of the list, it returns the final state value, _ie_ 55.

**How to write the third argument of List.Accumulate()?**

The third argument of List.Accumulate() is a function with two parameters – state, current. 

*   **State**: this will be initially set to 2nd parameter of the function and changes every time List.Accumulate() moves down the list.
*   **Current**: this will the value of current list item

Power Query functions are written in this fashion.

(parameter1, parameter2…) => function definition

So, for example (state, current) => state+current is a function that takes 2 parameters and returns their sum.

**To learn more about List.Accumulate():**

*   Watch the video that accompanies this article. You will get clarity about List.Accumulate()
*   Read [Datachant’s excellent List.Accumulate examples page](https://datachant.com/2016/06/02/power-query-list-accumulate-unleashed/)
    .

### Getting Lists from Table columns

If you have a table named **replacements** with columns \[Find\] and \[Replace\] in Power Query, you can use below syntax to extract a table column as list.

**replacements\[Find\]**

tablename\[Column name\]

### How to access individual list items

If you have a list named **source** in Power Query with 10 items, you can access 5th item of the list with this syntax.

**source{4}**

So, for example, if you want to get 3rd item of the \[Find\] column in replacements table, use:

\=replacements\[Find\]{2}

_Note: Power Query uses 0 base for lists. So first item of the list will be list{0}_

Using List.Accumulate for mass Find / Replace
---------------------------------------------

Now that you are familiar with key concepts necessary, let’s do some replacements.

Go to **mytext** query and insert a custom column. In this column, we will generated replaced text.

Write this formula:

List.Accumulate(
    List.Numbers(0, Table.RowCount(replacements)), 
    \[Text\], 
    (state, current) => 
        Text.Replace(state, 
            replacements\[Find\]{current},
            replacements\[Replace\]{current}))

**How does this formula work?**

1.  We create a list of numbers from 0. The size of this list will be same as number of rows in replacements table. 
    1.  _For our sample data, we get {0,1,2,3}_
2.  We start with input \[Text\] column value 
3.  We replace first replacements\[Find\] value with replacements\[Replace\] in \[Text\]
4.  We repeat 3 step three, while updating the **state** 
5.  At the end of this process, we end up with \[Text\] that _**successively**_ replaced all words in replacements table.

I know this formula is tricky to get your head around, but once you understand it, you will see the potential for other cool applications.

Download Multiple Find Replace Example file

[Please click here to download the multiple find replace example file](https://chandoo.org/wp/wp-content/uploads/2020/05/multiple-find-replace.xlsx)

List.Accumulate explained - Video
---------------------------------

If you are still 😕 and not sure how List.Accumulate magic works, then please watch this video. It goes in to greater detail about this _beautiful M function._ See it below or [visit my YouTube channel for it](https://youtu.be/YWAMaas_1AU)
.

More on Power Query...
----------------------

Please check out below pages to learn more about List.Accumulate() in particular and PQ in general.

**List.Accumulate examples:**

*   [List.Accumulate unleashed – several examples](https://datachant.com/2016/06/02/power-query-list-accumulate-unleashed/)
     \[Datachant\]
*   [Running totals with List.Accumulate](https://www.excelguru.ca/blog/2016/03/08/running-totals-using-the-list-accumulate-function/)
     \[ExcelGuru blog\]
*   [List.Accumulate syntax and reference page](https://docs.microsoft.com/en-us/powerquery-m/list-accumulate)
     \[PowerQuery Doc on MS\]

**Power Query examples for data cleanup:**

*   [Oddly shaped data – rescued with PQ](https://chandoo.org/wp/oddly-shaped-data-3ways/)
    
*   [Combine multiple files with different formats using PQ](https://chandoo.org/wp/combine-excel-files-using-power-query/)
    
*   [Extract common values from two tables with Power Query joins](https://chandoo.org/wp/compare-two-tables/)
    
*   [_More Power Query topics_](https://chandoo.org/wp/category/power-query/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/multiple-find-replace-list-accumulate/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/multiple-find-replace-list-accumulate/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [find replace](https://chandoo.org/wp/tag/find-replace/)
    , [list functions](https://chandoo.org/wp/tag/list-functions/)
    , [list.accumulate](https://chandoo.org/wp/tag/list-accumulate/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousHow to show positive / negative colors in area charts? \[Quick tip\]](https://chandoo.org/wp/positive-negative-colors-in-area-chart/)

[NextHighlight due dates in Excel – Show items due, overdue and completed in different colorsNext](https://chandoo.org/wp/highlight-due-dates-excel/)

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
    
    [Reply](https://chandoo.org/wp/multiple-find-replace-list-accumulate/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/multiple-find-replace-list-accumulate/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/multiple-find-replace-list-accumulate/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ