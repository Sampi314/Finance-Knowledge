# Convert unevenly spaced list to table [Data from Hell] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/d4h-unevenly-spaced-pq

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Convert unevenly spaced list to table \[Data from Hell\]
========================================================

*   Last updated on August 30, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Introducing Data from Hell:**

Watch out, its data from hell. In this new video series, we are going to look at some nutty, frustrating and fun data reshaping challenges and solve them using Excel. We will use Power Query, Formulas, VBA or other features as needed to free this data from damnation.

For our first installment, _let’s reshape unevenly spaced list of values to a table_.

### Unevenly Spaced List -> Tabular format

Let’s say you have a list with some values. They are separated by blank cells. You want to convert this to a table, so related values are on same row. But the table can have any number of columns depending on how big the chunks are.

_**Something like this:**_

![d4h-unevenly-spaced-list-to-table-power-query](https://chandoo.org/wp/wp-content/uploads/2017/08/d4h-unevenly-spaced-list-to-table-power-query.png)

### Enter Power Query (Get & Transform Data)

You guessed right. This data is too much out of whack for formula based solution. So let’s reshape it using Power Query _aka_ Get & Transform Data.

The process goes like this:

1.  Load the data in to query editor
2.  Replace nulls (blank cells) with something that is not part of your data, like %^%
3.  Using Text.Combine, concatenate all values to a single value, separated by some symbol that is not part of data, like =
4.  Convert this single value to a table and split by the symbol used in step 2.
5.  Calculate number of = symbols in each row using Text.Length and Text.Replace functions in to a new column
6.  Figure out the maximum of this new column as a variable. Name it as _MaxCols_
7.  Remove the extra column created in step 5
8.  Split the first column by delimiter set in step 3 with number of columns set to _MaxCols._
9.  Load data back to Excel.

### Data from Hell – Convert unevenly spaced list to table – Power Query tutorial

As this process requires a bit of tinkering with Power Query functions and a few false starts, I made a tutorial. I woke at 4AM to record this. _Just kidding, I woke up because my nose was all blocked up and couldn’t go back to sleep._ So I opened up Excel for some play and recorded this.  Check it out below.

**You can also [watch this video on our YouTube Channel](https://www.youtube.com/watch?v=sUUr7fOo7TU)
.**

### Download Example Workbook

_**[Click here to download the example workbook](https://chandoo.org/wp/wp-content/uploads/2017/08/d4h-spaced-unevenly.xlsx)
**_ for this Power Query tutorial. Try reshaping the data yourself first, you will learn a lot about PQ and how to use it for your advantage.

### More Power Query Recipes for you

**Power Query** (or Get & Transform Data as it is called in newer versions of Excel) **is an incredibly powerful tool to extract, reshape and merge your data sets**. Check out below tutorials and recipes for more.

*   [Introduction to Power Query – Podcast](http://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
    
*   [SUMPRODUCT Vs. Power Query](http://chandoo.org/wp/2017/06/15/sumproduct-vs-power-query/)
    
*   [Figuring out Employee Churn with Power Query \[HR Analytics\]](http://chandoo.org/wp/2017/03/13/figuring-out-employee-churn-with-power-query-hr-analytics/)
    
*   [Unpivot data quickly with Power Query \[tutorial\]](http://chandoo.org/wp/2015/09/29/unpivot-data-with-power-query/)
    
*   [More on Power Query](http://chandoo.org/wp/category/power-query/)
     & [Data Cleaning](http://chandoo.org/wp/tag/cleanup-data/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/d4h-unevenly-spaced-pq/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/d4h-unevenly-spaced-pq/#respond)
    
*   Tagged under [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [data from hell](https://chandoo.org/wp/tag/data-from-hell/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [get and transform data](https://chandoo.org/wp/tag/get-and-transform-data/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousCopy Paste Visible Cells only (Two more ways to do it)](https://chandoo.org/wp/copy-paste-visible-cells-only-two-more-ways-to-do-it/)

[NextIntroducing Power BI Play Date online class \[Details inside\]Next](https://chandoo.org/wp/introducing-power-bi-play-date/)

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
    
    [Reply](https://chandoo.org/wp/d4h-unevenly-spaced-pq/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/d4h-unevenly-spaced-pq/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/d4h-unevenly-spaced-pq/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ