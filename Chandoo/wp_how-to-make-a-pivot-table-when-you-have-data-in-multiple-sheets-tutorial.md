# How to make a pivot table when you have data in multiple sheets [Tutorial]

**Source:** https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to make a pivot table when you have data in multiple sheets \[Tutorial\]
============================================================================

*   Last updated on September 26, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently I had to create a [Pivot report](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
 from monthly data. But there is a twist. The data is spread across multiple sheets, one for each month. Let me explain how I built the pivot for that scenario.

![One Pivot Table from Multiple Sheets of Data](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2968.png)

Step 1: Load Monthly Data File to Power Query
---------------------------------------------

We can [use Power Query](https://chandoo.org/wp/power-query-tutorial/)
 and _automatically_ combine all the individual sheets to one big table. For this, you need a monthly workbook that has one tab (sheet) per month. If you need sample data, [check out this file](https://chandoo.org/wp/wp-content/uploads/2023/09/monthly-workbook.xlsx)
.

*   Create a “NEW” Excel workbook. We will use this file to combine all the monthly worksheets.
*   Go to Data Ribbon and click on Get Data > From File > From Excel

![Load "Monthly Excel" file to Power Query](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2969.png)

*   Select your monthly workbook with all the individual sheets
*   In the navigator screen, select any one sheet and click on “Transform” to go to Power Query Editor.

![Select any one sheet and "Transform" to enter the PQE](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2970.png)

Step 2: Combine & Clean-up Data
-------------------------------

Once you are in Power Query Editor (PQE), we can quickly _**combine all monthly sheets**_ and clean-up the data.

*   Using the “Query Settings” panel on the right, delete all the steps except “Source” step. You can use the ❌ mark next to the step to delete the step.

![Delete steps in Power Query](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2973.png)

*   In the query view, expand the “Data” column so we can get all the monthly data in one big table.

![expand monthly worksheets to one table](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2971.png)

### But the data is not clean...!

![Data Quality Issues with Combined Sheet Data - Power Query](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2974.png)

When you “Expand” the data column, we get all the data, but a ton of problems too. Here is a summary of the key issues.

1.  Incorrect headers
2.  Repeated header rows (one per month)
3.  Incorrect data types (dates, numbers treated as Alpha-numeric by Power Query)
4.  Unwanted columns
5.  Null values or blank rows
6.  Something else?!? 😱

Fortunately, Power Query can solve all these problems quite easily.

1.  Set first row as headers using Home Ribbon > First Row as Headers option
2.  To fix nulls & repeated header rows, use filter on a column like “Sales Person” and filter away the null & title words. See this demo:

![Removing repeated header rows & null values](https://chandoo.org/wp/wp-content/uploads/2023/09/2023-09-26_19-06-34.gif)

3.  Right click on the columns and use “Change Type” to set the correct data type.
4.  Using Home ribbon > Choose Columns select the columns you want.

Step 3: Load the Data to Excel
------------------------------

Once all the clean-up is done, rename your query to something like “Combined data” and use the Close & Load button in Home ribbon to load this data to Excel.

![Close & Load the data to Excel grid](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2972.png)

### Pro Tip

Use the "Load to" options to load the data just to your data model instead of Excel grid. This is helpful if you just want to make pivots and don't need to "see" the data.

Step 4: Create Pivot Table(s)
-----------------------------

Now that all the data is in one place, you can create a pivot report easily in Excel. Just select the “combined data” table and use Insert > Pivot Table to add the reports you want.

![Creating a pivot report from consolidated monthly data](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2976.png)

Step 5: How to update when you have "NEW" data?
-----------------------------------------------

Come next month, you may have another sheet in the “monthly file”. Just save the file and open the consolidated workbook (with all your pivots) and use the “Data” ribbon > Refresh All button to refresh the queries. You may need to press this twice to update the pivots too.

![Refresh all pivots and queries - Excel](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2977.png)

VIDEO: How to create a pivot table from multiple sheets of data?
----------------------------------------------------------------

Check out this video tutorial to understand how to make a pivot table from multiple sheets of data. ([see it on my channel](https://youtu.be/gi-DSWEUC-A?si=iT4VhtLY1Weel21h)
)

📂 Sample File
--------------

[**Download the sample data file**](https://chandoo.org/wp/wp-content/uploads/2023/09/monthly-workbook.xlsx)
 (monthly data) to practice this concept on your computer.

What to do when you have an error? ⛔
------------------------------------

While this trick works most of the time, you can still get some errors. Use below tips to debug / fix the problems.

*   **Save & Close the Monthly file:** The refresh / update process may throw errors if your file is not closed. So, save and close the workbook.
*   **Monthly tabs should be consistently formatted:** The headers and number of columns in your monthly file should match across tabs. If you have different headers or number of columns, then the combined file may have errors or incorrect values. 
*   **Missing Data:** If you notice that some data (a month for ex.) is missing in your consolidated file or pivots, try refreshing the file a few times. If that doesn’t work, go to “Query” ribbon and “Edit” the query. Once you are in PQ Editor, backtrack and locate the step that might be causing the problem.
*   **Any other problem?** Leave a comment with the issue you faced so I can offer some guidance.

Learn More 👩‍💻
----------------

You can use Pivot Tables + Power Query to do so many awesome things in Excel. Check out below tutorials to master the concepts.

*   [Introduction to Pivot Tables in Excel](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    
*   [I don’t use Pivot Tables anymore, I use this other thing instead…](https://youtu.be/SPFQX82X03Q?si=65vo3ZcieyrWarDf)
    
*   [How to use Power Query (with 4 real-world examples)](https://chandoo.org/wp/power-query-tutorial/)
    
*   [Combine data with Power Query when the headers don’t match](https://www.youtube.com/watch?v=ECtJQDc8uF8)
    

💥 Complete Excel + Pivot Tables + Power Query course from Chandoo
------------------------------------------------------------------

If you want to learn all the necessary Excel functionalities and how to apply them for work in one place, [check out my Excel School program](https://chandoo.org/wp/excel-school-program/)
. 

Trusted by more than 20,000 people around the world, Excel School is the #1 course to help you slay Excel for good. 

[Click here to know more and secure your spot](https://chandoo.org/wp/excel-school-program/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Pivot Table](https://chandoo.org/wp/tag/pivot-table/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousPython is in Excel! – Here is a complete getting started guide for you](https://chandoo.org/wp/introduction-to-python-in-excel/)

[NextCalculating Critical Path using Excel Formulas \[Project Management\]Next](https://chandoo.org/wp/critical-path-excel-template/)

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
    
    [Reply](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ