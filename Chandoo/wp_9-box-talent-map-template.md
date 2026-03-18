# 9 Box grid for talent mapping - HR for Excel - Template & Explanation

**Source:** https://chandoo.org/wp/9-box-talent-map-template

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

9 Box grid for talent mapping – HR for Excel – Template & Explanation
=====================================================================

*   Last updated on November 17, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

I learned about a new HR technique for talent mapping during a recent consulting project . It is called **9 box grid.** In this page, let me explain what it is and how you can create 9 box grid using Excel.

What is 9 Box Grid?
-------------------

9 Box grid is a talent mapping tool for Human Resources. This is used to map your staff on two scales – **performance** and **potential**. All staff are plotted on 3×3 grid with one side showing performance (from low to high) and another side with potential (low to high). 

**Here is a sample 9 Box Grid.**

![9 box grid explained](https://chandoo.org/wp/wp-content/uploads/2020/11/9-box-grid-explained.png)

[Learn more about 9 box grid methodology here](https://www.analyticsinhr.com/blog/9-box-grid/)
 \[analyticshr.com\]

How to create 9 box grid in Excel?
----------------------------------

If you have just a handful of staff then it is easier to create 9 box grid by typing the data in 3×3 range in Excel. But if you have a lot of people, then creating a **dynamic 9 box grid** is helpful. Something like below:

### Interactive 9 Box Grid in Excel - Demo

![9 box grid - interactive demo](https://chandoo.org/wp/wp-content/uploads/2020/11/9-box-grid-interactive-demo.gif)

Step by step instructions - Making 9 Box Grid template in Excel
---------------------------------------------------------------

I made a short video explaining the process for creating 9 box grid for talent mapping in excel. Watch it below (or [on my YouTube channel](https://youtu.be/MnsQhba0V9A)
) or read on for text instructions.

**Step 1: Gather data about performance and potential of your staff**

In a blank spreadsheet, gather the data about your staff. At the very least, you want staff name, performance and potential. Feel free to add things like department or team names.

This is how I structured my data:

It is all in a table named _**talent.**_ 

![data for 9 box grid - staff performance & potential](https://chandoo.org/wp/wp-content/uploads/2020/11/data-for-9-box-grid-staff-performance-potential.png)

**Step 2: Create the talent map 9 box grid visual**

You can do it in two ways. If you have Excel 365 and access to **dynamic array functions** like FILTER(), you can use formulas to generate the 3×3 talent map grid.

Else, you can use Pivot Tables to generate the talent map grid.

### Formula approach for Talent Map

_Note: this method requires Excel 365 with dynamic array functions._

Set up a 3×3 grid in a blank sheet. 

In the top left cell, use the below formula.

\=IFERROR(TEXTJOIN(“,”&CHAR(10),TRUE, SORT(FILTER(talent\[Candidate\],(talent\[Performance\]=E$8)\*(talent\[Potential\]=$D5)))),””)

The above formula assumes E$8 has the performance rating value and $D5 has potential.

**How does this formula work?**

We are using FILTER() function to filter down the talent table to all candidates who have given performance (E8) and potential (D5) values

SORT() function sorts these names in alphabetical order.

Finally TEXTJOIN() is used to combine all names to one big text with comma & new line character between names. 

*   [Learn more about FILTER & SORT functions](https://chandoo.org/wp/dynamic-array-functions/)
    .
*   [Learn more about TEXTJOIN function](https://chandoo.org/wp/textjoin-examples/)
    

### Pivot Table approach for Talent Map

_Note: this method requires Excel 2013 or above versions_

Here is a quick demo of the Pivot Table based 9 box talent map grid.

![9 box grid - pivot table demo](https://chandoo.org/wp/wp-content/uploads/2020/11/9-box-grid-pivot-table-demo.gif)

To create this,

*   Insert a pivot table from your talent data. During the insert pivot step, enable “add this to data model” option, as depicted below.

![data model option in pivot tables](https://chandoo.org/wp/wp-content/uploads/2020/11/data-model-option-in-pivot-tables.png)

[Read more about data model based pivot tables](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
.

*   Now add “performance” to column labels and “potential” to row labels area of the pivot.
*   We need to show the names of people instead of count in the values area. This can be done by using **measures.** 
*   Right click on the table in fields list area and select “Add measure” option.
    *   Name of the measure: List of names
    *   Definition: \=CONCATENATEX(‘talent mapping’, \[Candidate\],”, “,\[Candidate\],asc)

Add this measure to values area of the pivot and your 9 box talent map will be ready.

**What is this measure doing?**

This measure is concatenating all the staff names that have given performance and potential levels. It is also sorting such names in ascending order. 

9 box grid for talent mapping - FREE Excel Template
---------------------------------------------------

[**Click here to download my free 9 box grid talent mapping template**](https://chandoo.org/wp/wp-content/uploads/2020/11/9-box-grid.xlsx)
.  It has sample data of 100 employees and two different talent maps (one with formulas and another with pivot tables). Experiment with it to understand the process or use it for your work.

Work in HR and use Excel? More resources for you...
---------------------------------------------------

Here are a few more resources to help you with various HR data analysis and reporting challenges.

*   [Impressive vacation tracker and dashboard](https://chandoo.org/wp/employee-vacations-tracker-dashboard/)
    
*   [L & D tracker and dashboard](https://chandoo.org/wp/training-tracker/)
    
*   [Employee turnover (attrition) analysis with Power BI](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/)
    

General Excel resources to improve your data analysis

*   [Top 10 formulas for data analysis work](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
     
*   [Excel pivot tables – a complete intro and examples](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    
*   [Advanced Pivot Table examples](https://chandoo.org/wp/advanced-pivot-tables/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/9-box-talent-map-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/9-box-talent-map-template/#respond)
    
*   Tagged under [9 box grid](https://chandoo.org/wp/tag/9-box-grid/)
    , [concatenatex](https://chandoo.org/wp/tag/concatenatex/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel for HR](https://chandoo.org/wp/tag/excel-for-hr/)
    , [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)
    , [FILTER()](https://chandoo.org/wp/tag/filter/)
    , [measures](https://chandoo.org/wp/tag/measures/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sort](https://chandoo.org/wp/tag/sort/)
    , [Textjoin()](https://chandoo.org/wp/tag/textjoin/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious6 Must Know Line Chart variations for Data Analysis](https://chandoo.org/wp/line-chart-variations/)

[NextImage Lookup – How-to show dynamic picture in a cell \[Excel Trick\]Next](https://chandoo.org/wp/excel-image-lookup/)

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
    
    [Reply](https://chandoo.org/wp/9-box-talent-map-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/9-box-talent-map-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/9-box-talent-map-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ