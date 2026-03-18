# How to use Excel Data Model & Relationships » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

How to use Excel Data Model & Relationships
===========================================

*   Last updated on February 6, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Have you ever been in a VLOOKUP hell?**_

Its what happens **when you have to write a lot of vlookup formulas before you can start analyzing your data**. Every day, millions of analysts and managers enter VLOOKUP hell and suffer. They connect table 1 with table 2 so that all the data needed for making that pivot report is on one place. If you are one of those, then you are going to love Excel’s data model & relationships feature.

![Table relationships & Data model feature of Excel - cartoon](https://chandoo.org/wp/wp-content/uploads/2020/02/table-relationships-and-data-model-excel.png)

In simple words, this feature helps you _**connect one set of data with another set of data so that you can create combined pivot reports.**_

### Practical Example – V(X)LOOKUP hell vs. Data Model heaven

Lets say you are looking sales data for your company. You have transaction data like below.

![Example data](https://img.chandoo.org/rt/sales-transaction-data.png)

And you want to find out how many units you are selling by product category and customer’s gender.

Unfortunately, you only have product ID & customer ID.

**With VLOOKUP Hell,**

1.  You first fetch all the customer and product data and place them in separate ranges.
2.  Then write a vlookup formula to fetch product category, another to fetch customer gender.
3.  Then fill down the formulas for entire list of transactions.
4.  Now make a pivot table.

Assuming you have 30,000 transactions, you have to _**write 60,000 VLOOKUP formulas to create this one report**!!!_

**With Data Model heaven,**

1.  Create relationships between Sales, Products & Customer tables
2.  Create a pivot table

### Creating a relationship in Excel – Step by Step tutorial

1.  ![Relationship feature in Excel 2013 data ribbon tab](https://img.chandoo.org/rt/relationships-ribbon-button.png)
    
    First set up your data as tables. To create a table, select any cell in range and press CTRL+T. Specify a name for your table from design tab. Read [introduction to Excel tables](https://chandoo.org/wp/data-tables/)
     to understand more.
2.  Now, go to data ribbon & click on relationships button.
3.  **Click New** to create a new relationship.
4.  Select Source table & column name. Map it to target table & column name. It does not matter which order you use here. Excel is smart enough to adjust the relationship.  
    
    ![Creating a new relationship in Excel 2013 - how to?](https://img.chandoo.org/rt/establishing-a-relationship-in-excel-2013-howto.png)
    
5.  Add more relationships as needed.

### Using relationships in Pivot reports & analysis

1.  Select any table and insert a pivot table (Insert > Pivot table, [more on Pivot tables](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    ).
2.  Make sure you check the “Add this data to data model” check box.  
    
    ![Adding a pivot table with data model in Excel 2013](https://img.chandoo.org/rt/creating-a-pivot-report-with-relationships.png)
    
3.  In your pivot table field list, check “ALL” instead of “ACTIVE” to see all table names.
4.  Select fields from various tables to create a combined pivot report or pivot chart

### Example: Category & Gender Sales Report

1.  Add category to row labels
2.  Add gender to column labels
3.  Add quantity to values
4.  and your report is ready!

![Example Pivot report made with Excel data model](https://img.chandoo.org/rt/example-pivot-table.png)

### Things to keep in mind when you using relationships

*   **Same data types in both columns:** Columns that you are connecting in both tables should have same data type (ie both numbers or dates or text etc.)
*   **One to one or One to many relationships only:** Excel 2013 supports only one to many or one to one relationships. That means one of the tables must have no duplicate values on the column you are linking to. (for example products table should not have duplicate product IDs).
*   **You can add slicers too:** You can slice these pivot tables on any field you want (just like normal pivot tables). For example, you can further slice the above report on customer’s profession or product’s SKU size.

### Benefits of Data Model based Pivot Tables

Once you have a data model in spreadsheet, you will enjoy several benefits (apart from multi-table pivots that is). They are,

*   **Distinct counts:** This simple but often tricky to calculate number is easy to get once you have data model based pivot. Just go to value field settings and change the summary type to “Distinct count”. Here is a tip explaining **[how to get distinct counts in Excel pivots](https://chandoo.org/wp/distinct-count-pivot-tables/)
    **.
*   **Measures & DAX:** Once you have a Data Model, you can unleash the full Power Pivot features on your workbook. You can create measures (using DAX language) and calculate things that are otherwise impossible with regular Excel. Here is an example of **[percentage of something calculation with DAX & Data Model](https://chandoo.org/wp/percentage-of-another-value-pivot-table/)
    **, to get started.
*   **Pivots from data in other files & databases**: You can combine data model with the abilities of Power Query to create pivots from data in other places. For example, you can make a pivot from sales data in SAP with customer data in CRM system. Here is an overview of [what is Power Query?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)
    
*   **Pivots from more than 1mn rows of data:** You can connect to very large datasets and make pivots from them with the help of data model. [Here is a demo of how to set up data model for 1+mn rows of data](https://chandoo.org/wp/more-than-million-rows-in-excel/)
    .
*   **Convert Pivot Tables to formulas:** Once you have a data model based pivot table, you can turn it in to a set of formulas. You can access this feature from “Analyze” ribbon. This will replace your pivot with a bunch of CUBE formulas. [Here is an overview of CUBE formulas](https://excelgorilla.com/excel/excel-cube-formulas/)
    .

### Drawbacks of Data Model:

Of course, its not all cup cakes and coffee with Data Model. There are a few drawbacks of data model based pivot tables.

*   **Compatibility:** Data model & relationship feature is available only in Excel 2013 or above. This means, you cannot create or share such pivot reports with people using _older versions of Excel._
*   **Not able to group data:** In regular Pivot Tables, you can group numeric, data or text fields. But with data model pivot tables, you can no longer group data. You must create another table with the group mapping and use it as a relationship.

### Download Example File

[**Click here to download Excel data model demo file**](https://img.chandoo.org/rt/excel-2013-data-model-demo.xlsx)
. It contains 3 different tables and a combined pivot report (with slicer) to show you what is possible.

### Do you use relationships?

Ever since discovering PowerPivot, I kind of stopped using VLOOKUP (or XLOOKUP) for most of my own analysis. Now that relationships are part of main Excel functionality, I am using them even more.

**What about you?** Are you using relationships & data model in Excel? What cool things are you doing with it? Share your tips with us using comments.

### Want even more? Try PowerPivot

If you want even more out of your reports, then try PowerPivot. It is a new feature in Excel 2013 (available as add-in in Excel 2010) that can let you do lots of powerful analysis on massive amounts of data. Here is an [introduction to PowerPivot](https://chandoo.org/wpintroduction-to-power-pivot/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [41 Comments](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/#respond)
    
*   Tagged under [data model](https://chandoo.org/wp/tag/data-model/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel 2013](https://chandoo.org/wp/tag/excel-2013/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [relationship](https://chandoo.org/wp/tag/relationship/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPrevious5 Keyboard shortcuts for writing better formulas](https://chandoo.org/wp/5-keyboard-shortcuts-for-writing-better-formulas/)

[NextWhat do you use Tables for? \[poll\]Next](https://chandoo.org/wp/what-do-you-use-tables-for/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ