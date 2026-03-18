# Excel SUMIFS formula: How to use it for quick data analysis ? sample file

**Source:** https://chandoo.org/wp/introduction-to-excel-sumifs-formula

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Introduction to Excel SUMIFS Formula
====================================

*   Last updated on September 2, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Excel SUMIFS function is used to calculate the sum of values that meet any criteria**. For example, you can calculate the **total sales** in _east zone_ for product _Pod Gun_ using SUMIFS formula.

In this article, you will learn:

*   What is SUMIFS function and how to use it?
*   Syntax for SUMIFS
*   Using SUMIFS() with tables and structural references
*   SUMIFS examples – simple, wild card
*   Using SUMIFS() with date & time values
*   Free sample file for SUMIFS formula
*   More formulas for data analysis

### How to write Excel SUMIFS Function?

Using SUMIFS you can find the sum of values in your data that meet multiple conditions.

So, to get the sum of all the **Blow Torch**es sold in **North**, we just write,

`=SUMIFS(D3:D16, B3:B16,"Blow Torch",C3:C16,"North")`

_**Similarly to find the podgun sales in East, just write,**_

![SUMIFS Excel function - Examples](https://chandoo.org/img/f/sumifs-excel-formula-demo.png)

### SUMIFS function – Syntax and explanation:

SUMIFS formula takes a range for summing the values and at least one criteria range and criteria. You can specify as many as 127 conditions for summing your data.

![SUMIFS Formula - Syntax](https://chandoo.org/img/f/sumifs-excel-formula-syntax.png)

Imagine asking _“how many spit bombs Hansolo sold in North region of Planet Naboo between long long ago and long ago that resulted in more than 25% profits?”_ and getting an instant answer.

**The beauty of SUMIFS formula is that it works with wildcards too**, just like its siblings – SUMIF and COUNTIF. So you can write formulas like,

`=SUMIFS(D3:D16,B3:B16,"Spit Bomb",C3:C16,"*th")` to get sum of spit bombs sold in Nor_**th**_ and Sou**_th_**.

### Using SUMIFS() with tables

You can write SUMIFS function on either a range of data or on a table. When using with tables, you can simply apply [structural references](https://chandoo.org/wp/introduction-to-structural-references/)
 – _ie_ TableName\[Column Name\] notation to specify the _criteria_ columns. _See this example:_

![SUMIFS Function syntax explained](https://chandoo.org/wp/wp-content/uploads/2018/05/sumifs-formula-explained.png)

### SUMIFS Examples

Let’s say you have a table named ACME as pictured above. See these examples to understand how the function works.

*   **Sales for Blow Torch in West**
    *   `=SUMIFS(acme[Sales], acme[Product], "Blow Torch", acme[Region], "West")`
*   **Total Sales above 150 in East**
    *   `=SUMIFS(acme[Sales], acme[Sales],">150",acme[Region],"East")`
*   **Sales of North for all _excluding_ Pod Gun**
    *   `=SUMIFS(acme[Sales], acme[Region],"North",acme[Product],"<>Pod Gun")`
*   **Sales of all products that _contain_ letter B**
    *   `=SUMIFS(acme[Sales], acme[Product], "*B*")`

### Using SUMIFS() with Date & time values

When you have a column of dates, you can apply special operators like >, <, =, <> to specify a date range.

For example, to count total sales between March 2018 and May 2018, we can use

`=SUMIFS(acme[Sales], acme[Sales Date],">=1-Mar-2018", acme[Sales Date], "<=31-May-2018")`

You can either type the date in the formula or bring it from a cell. If you have two cells containing start and end date for your window of dates, you can use this formula.

`=SUMIFS(acme[Sales], acme[Sales Date],">=" & start_date_cell, acme[Sales Date], "<=" & end_date_cell)`

_Replace start\_date\_cell and end\_date\_cell with actual cell references or names._

### Bonus:

Just like SUMIFS, there is COUNTIFS and AVERAGEIFS too in Excel. Once you know SUMIFS(), you can use all these other functions with ease.

### SUMIFS Examples – Sample Workbook

If you want to learn more about SUMIFS function and practice the formula, [**download Free SUMIFS Example workbook**](https://chandoo.org/wp/wp-content/uploads/2018/05/sumifs-examples.xlsx)
. Play with the formulas to learn more.

### Top 10 formulas for data analysis

Learning and using Excel formulas correctly is the key to success when it comes to your career as an analyst. If you enjoyed this post, check out my [**top 10 formulas for analysts page**](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
 for more tutorials.

### Additional resources on SUMIFS formula

Please refer to these other web pages as well to learn many uses of SUMIFS.

*   [SUMIFS and many uses](https://exceljet.net/excel-functions/excel-sumifs-function)
     \[exceljet\]
*   [SUMIFS syntax, examples and best practice](https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b)
     \[Microsoft documentation\]
*   [How to use SUMIFS function](https://www.techonthenet.com/excel/formulas/sumifs.php)
     \[techonthenet\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [216 Comments](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/#respond)
    
*   Tagged under [averageifs](https://chandoo.org/wp/tag/averageifs/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [data processing](https://chandoo.org/wp/tag/data-processing/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumif()](https://chandoo.org/wp/tag/sumif/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel formula showing as text instead of actual result – How to fix the problem](https://chandoo.org/wp/excel-formulas-are-not-working/)

[NextFIFA Worldcup 2018 Excel Tracker – FREE DownloadNext](https://chandoo.org/wp/fifa-worldcup-2018-tracker/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ