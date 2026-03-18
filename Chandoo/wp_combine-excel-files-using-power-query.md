# Combine multiple Excel files using Power Query [Full example + download] » Power Query Case Studies

**Source:** https://chandoo.org/wp/combine-excel-files-using-power-query

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Combine multiple Excel files using Power Query \[Full example + download\]
==========================================================================

*   Last updated on August 26, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Say you want to combine multiple Excel files, but there is a twist. Each file has few tabs (worksheets) and you want to combine like for like, _ie ,_ all Sheet1s to one dataset, all Sheet2s to another dataset…

To make matters interesting each sheet has a different format.

What now?

Of course Power Query to the rescue.

![power query man](https://chandoo.org/wp/wp-content/uploads/2019/05/power-query-man.png)

This is an advanced example of Power Query. If you are a beginner, start with these pages.

*   [Introduction to Power Query](https://chandoo.org/wp/power-query-tutorial/)
    
*   [What is Power BI, Power Query and Power Pivot?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)
    

Combine multiple Excel files – the problem
------------------------------------------

Imagine you work in Finance. Your job involves paying employees for their business travel expenses. Every time someone goes on a business trip, they submit a trip expense report. **This is an Excel template with two tabs.**

*   Travel details tab: for gather personal and travel details
*   Expense details tab: for itemized expense details

As you have a lot of employees, you don’t want to manually scan the files and combine the data. **_Here is a sample of how these files look._**

![personal details & travel details - sample data](https://chandoo.org/wp/wp-content/uploads/2019/05/travel-details-sample-data.png)

Tab 1 – Travel details

![expense details - itemized - sample data](https://chandoo.org/wp/wp-content/uploads/2019/05/expense-details-sample-data.png)

Tab 2 – Expense Details

**You want to combine all the expense files** in to one big, consolidated & refreshable travel expense workbook.

![combine multiple files using power query](https://chandoo.org/wp/wp-content/uploads/2019/05/combine-multiple-files-with-power-query.png)

Using Power Query to combine files
----------------------------------

!["from folder" - Power query](https://chandoo.org/wp/wp-content/uploads/2019/05/from-folder-power-query.png)

Some of you may already know **Power Query’s “Get data from Folder” feature**. This helps us easily get & combine multiple excel files in a folder. Unfortunately, this alone **will not be helpful** for us as our file has two different tabs and we need to combine them separately 😉

Here is the process we need to follow.

Start by placing all the expense reports in to one folder. This can be a folder on your computer or on a network / shared drive.

Now go to “Get Data > From File > Folder”

![folder path screen - power query](https://chandoo.org/wp/wp-content/uploads/2019/05/folder-path-power-query.png)

Point to the folder path and Power Query will show all the files in that folder.

Once satisfied with the list of files (don’t worry if you need to exclude some files, you can do that while editing the query by applying filters), click on “Combine & Edit”.

![combine and edit option - files list](https://chandoo.org/wp/wp-content/uploads/2019/05/combine-and-edit-files-power-query-1.png)

Now you will get another screen asking you choose which tabs / tables you want to bring. As we have two sets of consolidations, let’s start with the first one – travel details tab. Select that and proceed.

![combine files screen with sample data from one file - power query combine files](https://chandoo.org/wp/wp-content/uploads/2019/05/combine-edit-files-sample-data-preview.png)

At this point, Power Query will create a folder called “Transform sample” and places a few things in it. PQ will also create a query for all the merged data. This is how your Power Query window could look.

![editing transform sample - powerquery combine files](https://chandoo.org/wp/wp-content/uploads/2019/05/editing-transform-sample-power-query.png)

### Editing the Transform sample query

As you can see, the default combined query data can be useless for our situation. So let’s proceed by editing “Transform sample file from reports” query.

### **What is Transform sample really?**

In this sample query, you can make any changes and PQ will apply them to all the files in the folder before combining them to one gain data set.

### Steps to turn travel details to a table

Our travel details sample needs to become one row table so that we can effectively merge multiple files. To do so, follow these steps:

1.  Remove blank / heading rows on the top.
2.  Remove any nulls or unnecessary rows from column 1
3.  Transpose the table
4.  Promote first row to headers

This is how the output would look after the process.

![transforming travel details to a tabular format - steps required](https://chandoo.org/wp/wp-content/uploads/2019/05/steps-to-transform-data-power-query.png)

### Combine all files

Now that we have edited transform sample, time to go back to the “reports” query to see the output. If you are happy with it, rename the query and load it in to Excel (or Power BI).

**Combined travel details**

![combined data ](https://chandoo.org/wp/wp-content/uploads/2019/05/merged-data-travel-details.png)

### Combining expense details

The process is same for expense details consolidation. Start by creating a fresh “from folder” query. As expense details are in a table, there is no need to do any additional changes to the transform sample. Simply combine everything from “expenses” tables and you are done.

  
**Combined expense details**

![combined data - expenses](https://chandoo.org/wp/wp-content/uploads/2019/05/merged-data-expense-details.png)

Download sample files to practice this
--------------------------------------

Power Query can be tricky to explain with blog posts alone. That is why I made few sample files and consolidated workbook. **[Click here to download everything](https://files.chandoo.org/pq/combined-data.zip)**.

Try to merge the files in “reports” folder using your own logic / transformation steps. Share your story / tips in the comments.

### I get an error when merging data from files

There are many reasons why Power Query may show an error when connecting to a folder. Here is a check list to help you.

*   **Make sure the folder path is valid and accessible**. If you created the query on one computer and try to refresh it from another, chances are it won’t work. Use shared network drives or change path in Power Query steps before refreshing.
*   **Files are loaded, but merged query errors.** This can happen if you edited the transform sample. Usually Power Query adds “Changed type” steps automatically after you do something. These changed type steps refer to column names in the query and change data types. If you edit the transform sample and alter the column structure of table, then the query will fail. The solution? Simple, delete all the _automatically_ added changed type steps.
*   **Some files should not be loaded, but they load and mess up the results**. Before making any transformations, set up filters based on file type or names. This way you can prevent loading unnecessary files.

Do you merge / combine files with Power Query?
----------------------------------------------

I do this all the time. My recent win was to merge 24 PDF credit card statements (2 types of cards over last 12 months) to one big table of data so that I can see trends and find out where I spend most.

What is your experience with combine multiple Excel files / folder query feature? What are some of your favorite tricks with this? **Please post them in the comments section.**

_This article is inspired from a comment by [Sourav](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#comment-1649749)
._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/combine-excel-files-using-power-query/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/combine-excel-files-using-power-query/#respond)
    
*   Tagged under [combine files](https://chandoo.org/wp/tag/combine-files/)
    , [consolidation](https://chandoo.org/wp/tag/consolidation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [get and transform data](https://chandoo.org/wp/tag/get-and-transform-data/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [transform sample](https://chandoo.org/wp/tag/transform-sample/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousHow to trace precedents in Excel formulas? \[tip+music from Prague\]](https://chandoo.org/wp/how-to-trace-precedents-in-excel/)

[NextShould finance people learn Power BI?Next](https://chandoo.org/wp/should-finance-people-learn-powerbi/)

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
    
    [Reply](https://chandoo.org/wp/combine-excel-files-using-power-query/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/combine-excel-files-using-power-query/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/combine-excel-files-using-power-query/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ