# Extract currency amounts from text - Power Query Tutorial » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Extract currency amounts from text – Power Query Tutorial
=========================================================

*   Last updated on July 27, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Let’s say you got some text values and want to extract the amounts from them. Something like this:

![extract-amounts-from-text](https://chandoo.org/wp/wp-content/uploads/2017/07/extract-amounts-from-text.png)

Note: Thanks to Monty for [posting this problem on our forum](http://forum.chandoo.org/threads/vba-extract-amt-from-string.35192/)
.

_**How to go about it?**_

We could use a variety of techniques to extract the values.

*   Formulas – not easy given the unstructured nature of data. But _almost_ possible. [See this for an example](http://chandoo.org/wp/2012/12/14/find-text-pattern/)
    .
*   VBA – possible, [read this forum discussion few ways to do it](http://forum.chandoo.org/threads/vba-extract-amt-from-string.35192/)
    .
*   Power Query – at first glance it might seem tricky, but PQ makes this all too easy. Read on.

### Extracting amounts from text items – Power Query Tutorial

1.  Specify a list of currency codes. Create a table in Excel and mention the codes. Something like below. Let’s name this table as **_codes_**   
    ![currency-codes](https://chandoo.org/wp/wp-content/uploads/2017/07/currency-codes.png)
2.  Load text data in to Power Query (Use Power Query > from Table or Data > from Table). We get this:  
    ![text-values-loaded-into-pq](https://chandoo.org/wp/wp-content/uploads/2017/07/text-values-loaded-into-pq.png)
3.  Now, let’s bring in currency codes as a cross join. To do this, just insert a new custom column. In the formula section, type  
    \= Excel.CurrentWorkbook(){\[Name=”_**codes**_“\]}\[Content\]
    
    ![addin-codes-table-to-text-data](https://chandoo.org/wp/wp-content/uploads/2017/07/addin-codes-table-to-text-data.png)
    
4.  This will bring a new column with all currency codes as tables. Expand the column to cross join both tables. See below demo.  
    ![expand-corss-join-two-tables](https://chandoo.org/wp/wp-content/uploads/2017/07/expand-corss-join-two-tables.gif)
5.  Now, add a conditional column to check which currency code is present in the text data. You can use below settings:
    
    ![conditional-column-on-codes](https://chandoo.org/wp/wp-content/uploads/2017/07/conditional-column-on-codes.png)
    
6.  At this stage, our PQ data looks like this:
    
    ![currency-codes-found](https://chandoo.org/wp/wp-content/uploads/2017/07/currency-codes-found.png)
    
7.  Now, let’s filter away any nulls in the Found? column.
8.  **Splitting each row by the currency code in next column:** this is the tricky part. We can use Text.Split() to split a text value by delimiter. But the result will be a list. We just want one of the items of that list. Simple, we can pass the result of Text.Split() to List.Last() to get that. Use below formula:=List.Last(Text.Split(\[String\],\[Custom.Codes\]))
    
    ![column-formula-to-extract-amount-from-text](https://chandoo.org/wp/wp-content/uploads/2017/07/column-formula-to-extract-amount-from-text.png)
    
9.  We get this:
    
    ![output-after-extracting-amounts-almost](https://chandoo.org/wp/wp-content/uploads/2017/07/output-after-extracting-amounts-almost.png)
    
10.  Now, convert the Amount column to decimal number. This will throw errors for incorrect values like .530.680268. Simply remove all these errors.
    
    ![amounts-after-converting-to-number](https://chandoo.org/wp/wp-content/uploads/2017/07/amounts-after-converting-to-number.png)
    
11.  Tidy up by removing unnecessary columns and renaming the rest. Load in to Excel. Here is a snapshot of cleaned data.
    
    ![final-output-amounts-from-text](https://chandoo.org/wp/wp-content/uploads/2017/07/final-output-amounts-from-text.png)
    

### Download Example Workbook

[**Click here to download sample workbook**](https://chandoo.org/wp/wp-content/uploads/2017/07/extract-currency-values.xlsx)
. Try cleaning the data in first tab yourself using PQ. You will realize how awesome and simple this approach is compared to either formula or VBA driven methods.

**How are you using Power Query?**

These days, PQ (or get data & transform as it is known in newer versions of Excel) has become my go to tool for most data polishing, cleanup and reshaping problems. What about you? Are you addicted to PQ yet? _Please share your experiences and wins in the comments section_.

**More ways to extract, clean and massage data with Power Query:**

If this looks interesting, check out below tuts to learn more about PQ.

*   [Introduction to Power Query – Podcast](http://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
    
*   [SUMPRODUCT Vs. Power Query](http://chandoo.org/wp/2017/06/15/sumproduct-vs-power-query/)
    
*   [Figuring out Employee Churn with Power Query \[HR Analytics\]](http://chandoo.org/wp/2017/03/13/figuring-out-employee-churn-with-power-query-hr-analytics/)
    
*   [Unpivot data quickly with Power Query \[tutorial\]](http://chandoo.org/wp/2015/09/29/unpivot-data-with-power-query/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/#respond)
    
*   Tagged under [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [extract](https://chandoo.org/wp/tag/extract/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousJoyplot in Excel](https://chandoo.org/wp/joyplot-in-excel/)

[NextUse File > Info to quickly unprotect multiple worksheets \[Quick tips\]Next](https://chandoo.org/wp/unprotect-multiple-worksheets/)

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
    
    [Reply](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ