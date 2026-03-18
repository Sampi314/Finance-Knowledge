# How to lookup in any column - Excel Formula Trick » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-lookup-in-any-column-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to lookup in any column – Excel Formula Trick
=================================================

*   Last updated on February 18, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you want to lookup in any column and return the result? Something like this:

![Lookup in any column - Excel trick\
](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)

In this article, learn how to write necessary Excel formulas to get the result.

Data Setup for looking up in any column
---------------------------------------

You need to set up your data in below structure. One column with the data you want to get and multiple columns with potential lookup value. For example, team name in column C, member names in columns D:J, as depicted below.

![data setup for looking in any column](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0093.png)

Lookup formula:
---------------

Let’s say we want to lookup “Leonard”, who is in the tea “Geeky Group”. Here is the formula.

    =XLOOKUP(1,BYROW(D5:J13,LAMBDA(row,COUNTIFS(row,"Leonard"))),C5:C13)
    
    'notes:
    'D5:J13 contains team member names
    'C5:C13 contains team names
    'this will return #N/A if none of the teams contain lookup value - ie Leonard

How does this formula work?
---------------------------

To understand how this lookup in any column formula is working, we need to first understand a few Excel concepts.

*   **BYROW:** This function let’s you define logic or operations that apply consistently for each row of the data. As we want to look in each row of team members and see if any of them is “Leonard”, BYROW is perfect for this operation.
*   **LAMBDA:** We can use Excel’s LAMBDA functions to create custom logic. As we need to check each row of the data to see if any of the members are “Leonard”, I created a LAMBDA to do that operation. LAMBDA(_row_, COUNTIFS(_row_, “Leonard”)) will return the count of “Leonard” in the input variable _row_

So now that you have the basic concepts ready, let’s understand the lookup in any column function. Here is the formula again.

    =XLOOKUP(1,BYROW(D5:J13,LAMBDA(row,COUNTIFS(row,"Leonard"))),C5:C13)
    
    'notes:
    'D5:J13 contains team member names
    'C5:C13 contains team names
    'this will return #N/A if none of the teams contain lookup value - ie Leonard

*   **BYROW(D5:J13,LAMBDA(row,COUNTIFS(row,”Leonard”))):** This formula portion tells us how many times “Leonard” appeared in each row of the data. It will be 0 if the team doesn’t contain lookup value and 1(or more) if the team contains the lookup value. For our sample data, this would be {0;0;0;0;0;1;0;0;0}
*   **XLOOKUP(1, BYROW(…), C5:C13):** Now that we know which team has the lookup value (Leonard), we just lookup for 1 (count) in the BYROW output and return the corresponding team name from the column C.

What if there are multiple matching values?
-------------------------------------------

By default XLOOKUP returns the first matching value whenever we have multiple matches. If you want to see all team names for a given person name (for example Amy is in two teams – “Geeky Group” and “99 Not Out”.

![Using FILTER() function to see all matching values with lookup in multiple columns](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0095.png)

In this case, we can use FILTER() function instead of XLOOKUP.

Using FILTER function to return all matching values
---------------------------------------------------

Here is the formula to see all team names for a given person.

    =FILTER(C5:C13,BYROW(D5:J13="Amy",OR))
    
    'notes:
    'D5:J13 contains team member names
    'C5:C13 contains team names
    'Here we are using an advanced variation of BYROW that applies OR operation on every row of comparison directly. The end result would be a bunch of TRUE or FALSE values, TRUE for teams that contain "Amy" and FALSE for rest of the rows.

This formula uses an advanced variation of the BYROW by doing a comparison directly and applying OR operation on each row of comparison. The result of BYROW would be an array of TRUE or FALSE values. TRUE for rows which contain Amy and FALSE for the rest.

When FILTER(C5:C13 …) sees this array of TRUE/FALSE values, it would return the matching items from C5:C13 for all TRUE values.

In this case, the output is shown below.

![FILTER formula output](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0096-1.png)

Further reading:
----------------

If you want to understand how the inner parts of this formula are working, refer to below articles / videos.

*   [How to use XLOOKUP function in Excel](https://chandoo.org/wp/xlookup-examples/)
    
*   [BYROW explained with examples](https://youtu.be/M_-5nwJnO3o)
    
*   [What is LAMBDA function in Excel](https://chandoo.org/wp/what-is-lambda-function/)
    
*   [How to use FILTER function in Excel](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [FILTER function in Excel – Video](https://youtu.be/JuTdj2j-9Kg)
    

Limitations of both formulas
----------------------------

Both of the above approaches (XLOOKUP and FILTER) only work with Excel 365 as BYROW is only available in that version of Excel. If you are using an older version of Excel (such as 2024, 2019 or 2016) you can’t use these approaches.

Alternative formula for older version of Excel
----------------------------------------------

There is no alternative for the FILTER() approach as older versions of Excel are not capable of _spilling values._ But there is an alternative to XLOOKUP() approach of returning the first matching value by looking up any column.

Here is the formula:

    =INDEX($C$5:$C$13,MATCH(1, MMULT((D5:J13="Leonard")*1,TRANSPOSE(COLUMN(D5:J13)^0)),0))
    
    'notes:
    'D5:J13 contains team member names
    'C5:C13 contains team names

Using MMULT to mimic BYROW operation
------------------------------------

Most of the above formula is easy to understand, but the bit with MMULT is the confusing part. So let me explain. Here is the MMULT portion: **_MMULT((D5:J13=”Leonard”)\*1,TRANSPOSE(COLUMN(D5:J13)^0))_**

*   **(D5:J13=”Leonard”)** checks every cell of the team member data and returns a bunch of TRUE or FALSE values. TRUE when the cell value is “Leonard” and FALSE otherwise. This is how that output looks like:

![boolean results of matrix comparison](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0097.png)

*   **(D5:J13=”Leonard”)\*1** turns this boolean array into a bunch of 0s & 1s (0 = false and 1 = true). So the output at this point would be:

![boolean values turned to 0s and 1s](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0098.png)

*   **_COLUMN(D5:J13)_** would return the the column numbers for columns D to J. This would be an array of {4,5,6,7,8,9,10}
*   **_TRANSPOSE(COLUMN(D5:J13)_** turns these numbers into a row-wise array. So the net result at this point is {4;5;6;7;8;9;10}
*   **_TRANSPOSE(COLUMN(D5:J13)^0_** takes all these numbers and makes them 1s as any number raised to the power of 0 would be. We just need a row-wise array of 1s same size as the number of columns in the team member array. So this is a long-winded way of getting there as older versions of Excel don’t have SEQUENCE formula. At this stage, our second part of MMULT operation has this array: {1;1;1;1;1;1;1}
*   Now, MMULT just multiplies these two matrices. Here they are again:

![mmult illustration](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0099.png)

*   When the matrix multiplication is done, we end up with a vertical (row-wise) array of 0s and 1s. 0 when the row doesn’t contain the lookup value (Leonard) and 1 otherwise. The result of this multiplication is:

![mmult output](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0100.png)

Let’s put everything together
-----------------------------

So now that we know how the MMULT magic is working, let’s put all the pieces together.

    =INDEX($C$5:$C$13,MATCH(1, MMULT((D5:J13="Leonard")*1,TRANSPOSE(COLUMN(D5:J13)^0)),0))
    
    'notes:
    'D5:J13 contains team member names
    'C5:C13 contains team names

INDEX($C$5:$C$13,MATCH(1, MMULT(…), 0)) simply looks for a 1 in the MMULT result and returns the corresponding value from range C5:C13.

Further reading on older Excel formulas:
----------------------------------------

Please refer to below pages for further learning on these formula techniques.

*   [INDEX + MATCH formula in Excel – explanation](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    
*   [SUMPRODUCT explained](https://chandoo.org/wp/excel-sumproduct-formula/)
    
*   [How to use boolean operations with arrays in Excel](https://chandoo.org/wp/advanced-sumproduct-queries/)
    
*   [MMULT examples](https://chandoo.org/wp/tag/mmult/)
    

Example Workbook: Lookup in any column
--------------------------------------

If you need a practice file to understand these formulas better, **[download it here](https://chandoo.org/wp/wp-content/uploads/2025/02/lookup-in-any-column.xlsx)
**.

In conclusion
-------------

While Excel’s lookup functions (XLOOKUP, VLOOKUP, FILTER, INDEX+MATCH) are great, they all suffer from one nagging limitation. They can only lookup in one place at a time (ie one column or row). But most of the time, our business data is not so tidy. We get data that can span multiple columns. In such cases, using the BYROW() to process one row at a time and then applying lookup or filter logic is a great alternative.

Moreover, if your data is structured vertically (ie team members are listed in rows instead of columns), we can use the same approach with BYCOL function. It applies the logic by column.

The BY functions (BYROW and BYCOL) are great addition to Excel and should be part of every analyst’s toolkit. Using them solves many tricky data problems easily.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/#respond)
    
*   Tagged under [byrow](https://chandoo.org/wp/tag/byrow/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic array formulas](https://chandoo.org/wp/tag/dynamic-array-formulas/)
    , [index](https://chandoo.org/wp/tag/index-2/)
    , [lambda](https://chandoo.org/wp/tag/lambda/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [match](https://chandoo.org/wp/tag/match-2/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mmult](https://chandoo.org/wp/tag/mmult-2/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFREE 4 Hours Complete Excel Course](https://chandoo.org/wp/complete-excel-course-free/)

[NextHow to freeze rows in excelNext](https://chandoo.org/wp/how-to-freeze-rows-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ