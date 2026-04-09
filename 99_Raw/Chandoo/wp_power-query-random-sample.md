# Howto get random sample with Power Query - Step by step tutorial

**Source:** https://chandoo.org/wp/power-query-random-sample

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to get a random sample of data with Power Query
===================================================

*   Last updated on September 22, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This [_Power Monday_](https://chandoo.org/wp/tag/power-mondays/)
 trick is about **random sample with Power Query**. This is based on my experience of working with large volumes of data.

The other day I have been building a hotel dashboard (more on this later). As part of the dashboard, I wanted to show a random sample of user reviews. Reviews database had quite a few rows, so I wanted to **extract a randomized sample of 100 reviews** and show them in the report. When you refresh the report (Data > Refresh), then a new set of reviews will be fetched and shown.

_![howto get random sample in power query](https://chandoo.org/wp/wp-content/uploads/2018/08/random-sample-power-query-howto.png)_

Let’s learn how to generate a random sample with Power Query in this article.

_This tutorial works in Power Query for Excel or Power BI._ In case of Excel, the output sample will be either loaded as table or to data model. In case of Power BI, output goes to your data model.

_If you want to [**get random sample with Excel formulas, read this**](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/)
._

5 Steps to create random sample with Power Query
------------------------------------------------

### Step 1: Get your data to Power Query

Simple. Grab the data you want to sample and bring it to PQ. At this point, you will get something like this:

_![random sample with power query - data](https://chandoo.org/wp/wp-content/uploads/2018/08/power-query-sample-howto-data.png)_

### Step 2: Add Random Numbers as a column

Go to “Add Column” > Custom Column and add this formula.

> \=Number.Random()

Remember: Power Query formulas are case-sensitive. So type exactly. Name this column “Random”

### But Power Query gives same random number in all rows …

That is right. As Power Query is a _parallel_ language, each row gets same random number (unlike Excel’s RAND() filled down a column).

_Note: your experience with Number.Random() could be different, but as you build transformations, at some point PQ will replace all numbers with same value._

So how to get different numbers per row? Simple, we force PQ to evaluate something per row. A simple thing like index number column will do. This will force PQ to run random formula for all rows.

_Hat tip to [Gil Raviv](https://datachant.com/)
 for suggesting this technique [in a forum post](https://social.technet.microsoft.com/Forums/en-US/81ca82f3-fa9f-4e49-935b-33b42b257e41/random-number-being-changed-to-the-same-number-for-all-rows?forum=powerquery)
._     

### Step 3: Add Index Number column & Sort the random numbers

Go to “Add column” > Index number. Now that we have index numbers in a column, this will force PQ to regenerate the random number per row.

_![add an index number column](https://chandoo.org/wp/wp-content/uploads/2018/08/index-column-power-query.png)_

Select the **random number column and sort** it.

Note: You may need to switch Steps 2 & 3 if the random numbers are same all the way thru.

### Step 4: Keep top _100_ rows

Go to Home > Keep Rows > Keep Top Rows. Enter the sample size you want (100) and Click OK. Your sample is ready.

_![keep top random rows](https://chandoo.org/wp/wp-content/uploads/2018/08/keep-top-rows-random-sample-pq.png)_

### Step 5: Remove the Random & Index columns

Now that our sample is ready, let’s remove the random & index number columns. We do not need them in the final output (or model). Click on Save & Load (or Close & Apply).

Enjoy the sample.

How to get random sample with repetitions?
------------------------------------------

The above technique gives a sample without repetitions. What if you need a sample with repetitions (ie memory-less sampling). For example, a series of dice throws or coin tosses?

We can use Power Query to get such samples too. This is slightly complicated compared to first technique, but fun to try.

1.  Load your source to PQ
2.  Group the data so you can get row count (while still keeping the data). Like this:  
    _![Advanced grouping in Power Query for random sampling with repetitions](https://chandoo.org/wp/wp-content/uploads/2018/08/advanced-grouping-power-query-sample-with-repetitions.png)_
3.  Add a custom column with a list of _100_ numbers =List.Numbers(1,100)
4.  Expand the list to new rows
5.  Add a column with random number  between 0 & row count-1 \=Number.RandomBetween(0,\[Count\]-1))
6.  Add index column
7.  Change random number to whole number
8.  Extract the random row number from \[Data\] to a new column \=\[Data\]{\[Random\]}
9.  Remove all other columns except this new column in #8
10.  Expand the column
11.  Your sample with _possible_ repetitions is ready.

Here is the full M code for you to customize.

>     let
>         Source = Excel.CurrentWorkbook(){[Name="myData"]}[Content],
>         #"Grouped Rows" = Table.Group(Source, {}, {{"Count", each Table.RowCount(_), type number}, 
>     {"Data", each _, type table}}),
>         #"Added Custom" = Table.AddColumn(#"Grouped Rows", "List", each List.Numbers(1,100)),
>         #"Expanded List" = Table.ExpandListColumn(#"Added Custom", "List"),
>         #"Added Custom1" = Table.AddColumn(#"Expanded List", "Random", 
>     each Number.RandomBetween(0,[Count]-1)),
>         #"Added Index" = Table.AddIndexColumn(#"Added Custom1", "Index", 0, 1),
>         #"Changed Type" = Table.TransformColumnTypes(#"Added Index",{{"Random", Int64.Type}}),
>         #"Added Custom2" = Table.AddColumn(#"Changed Type", "Custom", each [Data]{[Random]}),
>         #"Removed Columns" = Table.RemoveColumns(#"Added Custom2",{"Data"}),
>         #"Removed Columns1" = Table.RemoveColumns(#"Removed Columns",{"Count", "List", "Random", "Index"}),
>         #"Expanded Custom" = Table.ExpandRecordColumn(#"Removed Columns1", "Custom", {"Review Text", "Rating"},
>      {"Review Text", "Rating"})
>     in
>         #"Expanded Custom" 

Answers to your questions about sampling…
-----------------------------------------

### How to get another sample?

Simple. Just refresh your Power Query connection. You will get another sample.

### How to change the sample size?

In the M code, where it says _100_ replace with another number or parameter.

**Use Excel Cell to tell Power Query how big a sample you want…**

You can even use an Excel named cell to tell PQ what sample size you want. Assuming named cell _sample.size_ has the size, use this M code  =Excel.CurrentWorkbook(){\[Name=”_**sample.size**_“\]}\[Content\]\[Column1\]{0} to get the value in your query. Use it as part of other steps and bingo, your sample size changes.

### Other questions…?

_Struggle sampling some sensible set?_ Post your sample problem in comments so I or one of our excellent readers can help you.

Download sample file and get your samples…
------------------------------------------

Excuse the pun, but [**here is a sample file with all the M code for making your own**](https://chandoo.org/wp/wp-content/uploads/2018/08/power-query-random-sample.xlsx)
 _**samples**._ Examine the queries to learn how this is done.

### How do you sample?

Excel’s Rand() is my favorite way to sample. But now that I am spending more time with Power Query & Power BI, I needed another way to sample the data. This post outlines my preferred approach (unless I am dealing with _very large volumes of data)_ For large volumes of data, I suggest sampling at server-side thru SQL.

**What about you?** How do you sample? Share your approach or troubles in the comments.

**[New to Power Query? Check out this introduction tutorial](https://chandoo.org/wp/resources/introduction-to-power-query/)
.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/power-query-random-sample/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-query-random-sample/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [power mondays](https://chandoo.org/wp/tag/power-mondays/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [random](https://chandoo.org/wp/tag/random/)
    , [sampling data](https://chandoo.org/wp/tag/sampling-data/)
    , [statistics](https://chandoo.org/wp/tag/statistics/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousMake funky and creative hand-drawn chart in Excel – Quick tutorial](https://chandoo.org/wp/hand-drawn-charts-excel/)

[NextWhat is Power BI, Power Query and Power Pivot?Next](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)

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
    
    [Reply](https://chandoo.org/wp/power-query-random-sample/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/power-query-random-sample/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/power-query-random-sample/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ