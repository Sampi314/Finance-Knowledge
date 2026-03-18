# How can you analyze 1mn+ rows data - Excel Interview Question - 02 » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/more-than-million-rows-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Interview Questions](https://chandoo.org/wp/category/interview-questions/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How can you analyze 1mn+ rows data – Excel Interview Question – 02
==================================================================

*   Last updated on October 3, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![How-to handle more than million rows in Excel](https://chandoo.org/wp/wp-content/uploads/2019/09/how-to-handle-more-than-one-million-rows-in-excel.png)

As part of our **[Excel Interview Questions series](https://chandoo.org/wp/category/interview-questions/)
**, today let’s look at another interesting challenge. **How-to handle more than million rows in Excel?**

You may know that Excel has a _physical_ limit of 1 million rows (well, its 1,048,576 rows). But that doesn’t mean you can’t analyze more than a million rows in Excel.

**The trick is to use Data Model.**

Excel data model can hold any amount of data
--------------------------------------------

Introduced in Excel 2013, Excel Data Model allows you to store and analyze data without having to look at it all the time. Think of Data Model as a black box where you can store data and Excel can _quickly_ provide answers to you.

Because Data Model is held in your computer memory rather than spreadsheet cells, it doesn’t have one million row limitation. You can store any volume of data in the model. The speed and performance of this just depends on your computer processor and memory.

How-to load large data sets in to Model?
----------------------------------------

Let’s say you have a large data-set that you want to load in to Excel.

If you don’t have something handy, [here is a list of 18 million random numbers](https://1drv.ms/u/s!AnSMwNaW4GO2hhYIKVHNH6kI_O5H?e=XNLBvq)
, split into 6 columns, 3 million rows.

### Step 1 – Connect to your data thru Power Query

Go to Data ribbon and click on “Get Data”. Point to the source where your data is (CSV file / SQL Query / SSAS Cube etc.)

![Get data > Get & Transform Data options](https://chandoo.org/wp/wp-content/uploads/2019/09/get-data-power-query.png)

### Step 2 – Load data to Data Model

In Power Query Editor, do any transformations if needed. Once you are ready to load, click on “Close & Load To..” button.

![Close & Load to... options in Power Query](https://chandoo.org/wp/wp-content/uploads/2019/09/close-load-to.png)

Tell Power Query that you want to make a connection, but load data to model.

![Load data to Data Model in Excel](https://chandoo.org/wp/wp-content/uploads/2019/09/load-data-to-data-model.png)

Now, your data model is buzzing with more than million cells.

### Step 3 – Analyze the data with Pivot Tables

Go and insert a pivot table (Insert > Pivot Table)

Excel automatically picks Workbook Data Model. You can now see all the fields in your data and analyze by calculating totals / averages etc.

You can also build measures (thru Power Pivot, another powerful feature of Excel) too.

How to view & manage the data model
-----------------------------------

Once you have a data model setup, you can use,

*   **Data > Queries & Connections:** to view and adjust connection settings
*   **Relationships:** to set up and manage relationships between multiple tables in your data model
*   **Manage Data Model:** to manage the data model using Power Pivot

![How to manage Data model in Excel - various options](https://chandoo.org/wp/wp-content/uploads/2019/09/how-to-manage-data-model-in-excel.png)

Alternative answer – Can I not use Excel…
-----------------------------------------

Of course, Excel is not built for analyzing such large volumes of data. So, if possible, you should try to analyze such data with tools like Power BI \[[What is Power BI?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)\
\] This gives you more flexibility, processing power and options.

Watch the answer & demo of Excel Data Model
-------------------------------------------

I made a video explaining the interview question, answer and a quick demo of Excel data model with 2 million rows. Check it out below or **[on my YouTube Channel](https://youtu.be/5u7bpysO3FQ)
**.

Resources to learn about Excel Data Model
-----------------------------------------

*   [How to set up data model and connect multiple tables](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    
*   [A quick but detailed introduction to Power Query](https://chandoo.org/wp/resources/introduction-to-power-query/)
    
*   [Create measures in Excel Pivot Tables](https://chandoo.org/wp/top-5-with-above-average/)
     – Quick example
*   [Create data model in Excel](https://support.office.com/en-us/article/create-a-data-model-in-excel-87e7a54c-87dc-488e-9410-5c75dbcb0f7b)
     – Support.Office.com
*   [How to use Data Model in Excel](https://gorilla.bi/excel/make-data-model/)
     – GorillaBI.com

How do you analyze large volumes of data in Excel?
--------------------------------------------------

**What about you?** Do you use the data model option to analyze large volumes of data? What other methods do you rely on? Please post your tips & ideas in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/more-than-million-rows-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/more-than-million-rows-in-excel/#respond)
    
*   Tagged under [data model](https://chandoo.org/wp/tag/data-model/)
    , [excel interview questions](https://chandoo.org/wp/tag/excel-interview-questions/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Interview Questions](https://chandoo.org/wp/category/interview-questions/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPrevious#awesome trick – Extract word by position using FILTERXML()](https://chandoo.org/wp/extract-words-with-filterxml/)

[NextZelda Stamina Wheel ChartNext](https://chandoo.org/wp/zelda-stamina-wheel-chart/)

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
    
    [Reply](https://chandoo.org/wp/more-than-million-rows-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/more-than-million-rows-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/more-than-million-rows-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ