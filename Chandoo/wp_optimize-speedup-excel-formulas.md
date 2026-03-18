# Top 10 Tips to Optimize, Speed-up Your Excel Formulas

**Source:** https://chandoo.org/wp/optimize-speedup-excel-formulas

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Speed up your Excel Formulas \[10 Practical Tips\]
==================================================

*   Last updated on April 14, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Excel formulas acting slow?**_ Today lets talk about optimizing & speeding up Excel formulas. Use these tips & ideas to super-charge your sluggish workbook. Use the best practices & formula guidelines described in this post to optimize your complex worksheet models & make them faster.

![Speed up Excel Formulas - 10 Practical Tips](https://chandoo.org/wp/wp-content/uploads/2012/03/SNAG-2595.png)

10 Tips to Optimize & Speed up Excel Formulas
---------------------------------------------

### 1\. Use tables to hold the data

![Excel Tables are great for holding data](https://chandoo.org/wp/wp-content/uploads/2018/01/insert-table-big-button.png)

Starting Excel 2007 you can keep all the related data in a table. For example call center data in [our recent dashboard](https://chandoo.org/wp/design-customer-service-dashboard/)
 is kept in a table. Tables can be used in formulas with structural references, can be used as a source for pivot tables etc. And since tables grow & shrink as you add / remove data, none of your formulas need to be dynamic. As an example, if you have table called **_cs_**, then the formula sum(cs\[column\_name\]) refers to sum of all values in the column\_name of table cs. Even if you add more data to CS, the formula still works.

**Resources to learn about Excel Tables:**

*   [Introduction to Excel Tables – what are they and how to use them?](https://chandoo.org/wp/data-tables/)
    
*   [Example: Customer Service Dashboard – Data & Calculations](https://chandoo.org/wp/calculations-for-customer-service-dashboard/ "Data and Calculations for our Customer Service Dashboard [Part 2 of 4]")
    

### 2\. Use named ranges, named formulas

By using names and named formulas, you can simplify your spreadsheet. Not only that, since named ranges & named formulas can hold arrays (ie lists of values), you can hold intermediate results or values that you need to refer many times in these named formulas. This will reduce the formula overhead and makes your workbooks faster.

**Resources to learn about named ranges & named formulas**:

*   [**Excel School Program**](http://chandoo.org/wp/training-programs/formula-crash-course/)
    : In this comprehensive course, I talk about how to think about and write better formulas for data analysis work.
*   [Musings on Live Calendar](http://www.excelhero.com/blog/2010/01/live-calendar-musings.html)
     \[Excel Hero\]
*   Examples of Named Formulas – [2023 Calendar in Excel](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2023/)
    

### 3\. Use Dynamic Arrays & Spill Ranges

Introduced in Excel 365, Dynamic Arrays allow us to build complex calculations with ease. I suggest incorporating new functions like:

*   FILTER to fetch a list of values that meet one or more criteria.
*   SORT to sort the values
*   UNIQUE to eliminate duplicate values on the fly
*   XLOOKUP to perform various lookups
*   VSTACK / HSTACK to combine datasets
*   TOCOL / TOROW to convert tables of data to single row or column formats
*   \# or Spill operator to manage spill ranges

**Learn more about Dynamic Array functions here:**

*   [Dynamic Array Functions – A deep introduction](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [Dynamic Array Functions – how to use them \[Video\]](https://youtu.be/8IV_W13VFkw)
    
*   [How to use XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
    

### 4\. Use Pivot Tables

Many times, even when we do not need formulas we use them, because we can. Pivot tables are an excellent way to calculate a lot of summary values with few clicks. Once the pivot is built, you can refer to the pivot values with GETPIVOTDATA or simple cell references. This will reduce a lot of unnecessary calculations. If you are changing the data, you can just go to DATA ribbon and refresh all pivots in one go. This process works smoothly when you use **tables to hold the data.**

One of the reasons for slow workbooks is **_lot of data._** Since, pivot tables are designed to work with lots of data, by using them, you can speed up your workbooks.

**Resources to learn Pivot Tables:**

*   [Introduction to Excel Pivot Tables](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    
*   [Examples, Details & Downloads on Excel Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    

### 5\. Sort your data

One of the reasons for sluggish performance is that you are searching for something in a lot of un-sorted data. You are making Excel look for a needle in a hay-stack. Many times we inherit un-sorted data thru data imports. By sorting the data & using correct operators in lookup formulas, we can instantly speedup a sluggish workbook. If you feel that sorting the data is a pain, you can even automate it with Power Query or a sort procedure (thru a simple VBA macro).

**Examples on Sorting:**

*   [Remove duplicates & sort a list using Pivot Tables](https://chandoo.org/wp/remove-duplicates-using-pivot-tables/)
    
*   [Use Power Query to pre-sort the data you are working with](https://chandoo.org/wp/power-query-tutorial/)
    

### 6\. Use Manual Calculation Mode

Speed is the hefty price you pay for complexity. But many times, we want our Excel workbooks to be complex, because only then they would reflect real world. In such cases, you can set formula calculations to manual mode.

![Manual calculation mode in Excel Formulas](https://chandoo.org/wp/wp-content/uploads/2023/04/SNAG-2594.png "Set Formulas to Manual Calculation Mode to Speedup / Optimize them")

Just press F9 whenever you want to run the formulas. Please note that Excel runs formulas whenever you save the file too.

### 7\. Use Non-volatile formulas

There are a class of formulas in excel called as _**volatile formulas.**_ These formulas are re-calculated whenever there is a change in the workbook. Examples of volatile formulas are RAND, NOW, TODAY, OFFSET etc. So when your worksheet has a lot of volatile formulas, any time you make a change all these formulas must be re-calculated. Thus, your worksheet becomes slow.

Solution? Simple, do not use volatile formulas. For example, instead of using OFFSET to construct a dynamic range, you can use INDEX. Since INDEX is non-volatile, it tends to be faster. Or better still, use a table.

**Resources to learn more:**

*   [Excel INDEX function](https://chandoo.org/wp/index-formula-usage-and-tips/)
    
*   [Volatile functions in Excel](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/)
    

### 8\. Keep formulas in a separate sheet

Formulas are the driving force behind any Excel workbook or model. By keeping all them in a separate worksheet(s), you minimize the chance of mistakes, omissions or repetitions.  Debugging or investigating slow performance becomes an easy task when all formulas are in same place. I usually keep all the formulas in one sheet whenever I am designing a dashboard or complex workbook. This structure also helps me in thinking thru various calculations and planning the formulas in a structured way.

### 9\. Write better formulas

Here are some guidelines that I follow when writing formulas.

*   Built-in formulas tend to better than your own version – for example SUMIFS is easier to write and just as fast as SUMPRODUCT.
*   Do not refer to entire column when you need just a few values. Do not write SUM(A:A), when you know values are only in A1:A10.
*   IFERROR instead of lengthy IF(ISERROR formulas. Use IFERROR to simplify your error checking.
*   Remove or Fix formula errors \[[how to](http://chandoo.org/wp?p=2109)\
    , [findout why formulas are not working](http://chandoo.org/wp?p=2613)\
    \]
*   Use newer Dynamic Array formulas instead of old clunky array formulas
*   Remove or Reduce references to other workbooks. Use Power Query instead.
*   Remove any named ranges that result in error or missing links.
*   Try to come up with alternative formulas: this not only sharpens your mind, but lets you discover better solutions.
*   Do not calculate something if you do not need it.
*   Do not calculate same thing twice. Use the first result second time too. Use LET for accomplishing this.

**Resources to write better formulas**:

*   [Introduction to SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
    
*   [Introduction to XLOOKUP formula](https://chandoo.org/wp/xlookup-examples/)
    
*   [How to use the new Dynamic Array functions in Excel](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [Introduction to SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   [Introduction to IFERROR formula](http://chandoo.org/wp?p=3240)
    
*   [Excel Formula Forensics](http://chandoo.org/wp/category/formula-forensics/)
    
*   [Excel School program](https://chandoo.org/wp/excel-school-program/)
    

### 10\. Desperate times need desperate measures

Sometimes, no matter what you do, the workbook remains slow. Here are a few whacky ideas that I try in such cases:

*   **Replace formulas with values.** I take a backup of the formulas. Then I select everything, CTRL+C, ALT+ESV (or CTRL Shift V). Done!
*   **Develop the workbook from scratch:** Sometimes it helps to design the workbook afresh.
*   **Replace external data links with actual data:** And import data by copy-pasting if needed.
*   **Reduce the functionality:** See if the end user can live with fewer features in the workbook.
*   **Find an alternative solution:** Trying to do everything in Excel is foolish. See if there is any external tool that can do this better & faster.

### BONUS: Learn new formulas & play with them

Optimization is not a one-shot exercise. It is an ongoing-business. So you need to constantly learn new formulas, new uses & play with them. This way, you see new ways to improve a sluggish workbook. To begin with, explore our [Formula homework](https://chandoo.org/wp/homework/)
 & [formula forensics pages](https://chandoo.org/wp/category/formula-forensics/)
 and see how you solve these problems.

How do you speed-up your Excel formulas?
----------------------------------------

So how do you optimize & speed-up your Excel formulas? What techniques do you use? **Please share using comments.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/optimize-speedup-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/optimize-speedup-excel-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [excel optimization](https://chandoo.org/wp/tag/excel-optimization/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [sorting](https://chandoo.org/wp/tag/sorting/)
    , [ssw](https://chandoo.org/wp/tag/ssw/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [volatile functions](https://chandoo.org/wp/tag/volatile-functions/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousA clever technique to simplify your long, nested IF formulas](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/)

[NextHow to Create a Dynamic Excel Dashboard in Just 5 StepsNext](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

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
    
    [Reply](https://chandoo.org/wp/optimize-speedup-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/optimize-speedup-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/optimize-speedup-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ