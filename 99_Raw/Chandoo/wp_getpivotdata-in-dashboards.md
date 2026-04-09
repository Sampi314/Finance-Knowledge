# How to use GETPIVOTDATA - Excel Pivot Tables - Tutorial, examples and explanation

**Source:** https://chandoo.org/wp/getpivotdata-in-dashboards

---

*   [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

How to use GETPIVOTDATA with Excel Pivot Tables
===============================================

*   Last updated on May 8, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

[**Pivot tables**](http://chandoo.org/wp/excel-pivot-tables/)
 are very powerful analysis tools. They can summarize vast amounts of data with just few clicks. But they are lousy when it comes to output. Imagine the horror of putting a pivot table right inside your [beautiful dashboard](http://chandoo.org/wp/excel-dashboards/)
. One refresh could ruin the layout and create half-an-hour extra work for you.

How to combine the power of pivot tables with elegance of your dashboards?

The answer is: GETPIVOTDATA()

### What is GETPIVOTDATA?

As the name suggests, GETPIVOTDATA gets pivot table data. The best way to understand GETPIVOTDATA is by looking at an example.

Let’s say, you have a pivot table like the one below. And you want to know what is the Amount for Cust Area = Middle & Prod Category = Biscuits combination.

The below GETPIVOTDATA formula should work.

\=GETPIVOTDATA(“Amount”,$A$3,”Cust Area”,”Middle“,”Prod Category”,”Biscuits“)

![GETPIVOTDATA-explained](https://chandoo.org/wp/wp-content/uploads/2015/08/GETPIVOTDATA-explained.png)

As you can see GETPIVOTDATA has below syntax.

> GETPIVOTDATA(value field name, any cell reference in pivot table, \[field name 1, value1, field name 2, value 2 …\])

**Few more examples of GETPIVOTDATA:**

Check out below examples to understand how various parameters of the GETPIVOTDATA function behave:

| GETPIVOTDATA function | What it does | Value |
| --- | --- | --- |
| \=GETPIVOTDATA(“Amount”,$A$3,”Cust Area”,”South”,”Prod Category”,”Biscuits”) | Gets Amount for South & Biscuits combination | $609.50 |
| \=GETPIVOTDATA(“Amount”,$A$3,”Prod Category”,”Biscuits”) | Gets grand total for Biscuits | $5,251.10 |
| \=GETPIVOTDATA(“Amount”,$A$3,”Cust Area”,”South”) | Gets grand total for South | $4,342.20 |
| \=GETPIVOTDATA(“Amount”,$A$3) | Gets grand total of all amounts | $41,828.00 |
| \=GETPIVOTDATA(“Amount”,$A$1,”Cust Area”,”West”,”Prod Category”,”Snacks”) | Gives an error as $A$1 is not part of the pivot | #REF! |
| \=GETPIVOTDATA(“Amount”,$A$3,”Cust Area”,$P$2,”Prod Category”,$P$3) | Gets Amount for cust area = P2 and pro category = P3 cell values. | depends on variables |
| \=GETPIVOTDATA(“Amount”,$A$3,”Prod Category”,category\_name) | Gets grand total for category = category\_name value | depends on variables |
| \=GETPIVOTDATA($P$4&””,$A$3,”Cust Area”,$P$2,”Prod Category”,$P$3) | Gets P4 value field for Cust Area = P2 and Prod Category = P3.  <br>_Note: $P$4 &”” is used to convince GPD that P4 is a string not number._ | depends on variables |

### Using GETPIVOTDATA in dashboards

The idea is simple. Since GETPIVOTDATA can be parameterized  with variable cells or named ranges, we can use it in dashboards to get relevant data based on user input.

_**Sample this:**_

![getpivotdata-demo](https://chandoo.org/wp/wp-content/uploads/2015/08/getpivotdata-demo.gif)

_**Or this dashboard powered with GETPIVOTDATA**_

![sample-dashboard-powered-with-getpivotdata](https://chandoo.org/wp/wp-content/uploads/2015/08/sample-dashboard-powered-with-getpivotdata.png)

### Things to note when working with GETPIVOTDATA:

GETPIVOTDATA is a very useful function, but it does have a few quirks.

*   If your pivot table has **[slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)** linked to them, GPD will reflect the results based on slicer selection.
*   If your pivot table has **any items filtered** (say category Biscuits is filtered out), then GPD will return #REF error when you try to get any value corresponding to Biscuits.
*   If you **change the pivot table** structure, your GETPIVOTDATA functions may not work as you expect.
*   If you **turn off grand totals** or sub-totals, you can no longer get them thru GPD.
*   GPD requires that your original pivot tables remain intact and visible all the time.
*   If you want to completely **get rid of pivot tables and still get answers** to questions, then you should use CUBE formulas along with Workbook data model feature (more on this in a future post).
*   The best & **easiest way to write GPD** is by pressing = and referencing a cell inside the pivot. This will _automatically_ write the GPD for you. You can then customize the parameters as you need.
*   You can **turn-off GPD** by going to Pivot Table Analyze ribbon tab & unchecking “Generating GETPIVODATA” option from PivotTable options area.

### Download GETPIVOTDATA Examples workbook

[**Please click here to download the GETPIVOTDATA example workbook**](https://chandoo.org/wp/wp-content/uploads/2015/08/getpivotdata-examples.xlsx)
. Refer to various tabs & formulas to learn more. Don’t forget to play with the dashboard powered by GETPIVOTDATA.

### Learn more about Pivot Tables

If you are new to Pivot Tables, it’s high time you started using them. Check out below pages and get started.

*   [Introduction to Excel Pivot Tables – article](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
     , [Podcast](http://chandoo.org/wp/2014/08/21/cp018-intro-pivot-tables/)
    
*   [Comprehensive guide to Excel Pivot Tables](http://chandoo.org/wp/excel-pivot-tables/)
    
*   [Slicers – Introduction, what are they, advanced scenarios](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
    
*   [Building dashboards with Pivot Tables + Slicers](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
    
*   [Convert regular pivots to GETPIVOTDATA – 3 part tutorial from Mike Alexander](http://datapigtechnologies.com/blog/index.php/convert-regular-pivottables-to-getpivotdata-formulas-part-1/)
    , [part 2](http://datapigtechnologies.com/blog/index.php/convert-regular-pivottables-to-getpivotdata-formulas-part-2/)
     & [part 3](http://datapigtechnologies.com/blog/index.php/convert-regular-pivottables-to-getpivotdata-formulas-part-3/)
    

### How do you use GETPIVOTDATA?

Let me be honest. For my dashboards, I usually write direct cell references (=A7) instead of GPD. This keeps my formulas short. For dynamic / parameterized setups, I usually write INDEX / MATCH formulas that talk to Pivot Table data. But occasionally I use GETPIVOTDATA because it is very easy to setup and does what it says on the sticker.

**What about you?** How do you use GETPIVOTDATA? Please share scenarios in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/getpivotdata-in-dashboards/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/getpivotdata-in-dashboards/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [GETPIVOTDATA](https://chandoo.org/wp/tag/getpivotdata/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousSummarize only filtered values using SUBTOTAL & AGGREGATE formulas](https://chandoo.org/wp/summarize-filtered-values/)

[NextCP043: My favorite time saving features of Excel, Revealed.Next](https://chandoo.org/wp/top-time-saving-features-of-excel/)

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
    
    [Reply](https://chandoo.org/wp/getpivotdata-in-dashboards/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/getpivotdata-in-dashboards/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/getpivotdata-in-dashboards/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ