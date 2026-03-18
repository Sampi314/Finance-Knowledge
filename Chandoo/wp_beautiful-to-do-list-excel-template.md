# Create a beautiful, elegant & interactive to-do list with Excel (FREE Template + Tutorial) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/beautiful-to-do-list-excel-template

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

Create a beautiful, elegant & interactive to-do list with Excel (FREE Template + Tutorial)
==========================================================================================

*   Last updated on March 27, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![To-do list in Excel - Demo & Free template](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2558.png)

In this hands-on tutorial learn how to create a simple, elegant and functional to-do list to track your projects and tasks.

Download FREE To-Do List Excel Template
---------------------------------------

Don’t want to make your formulas and formatting? You can download my ready-to-use To-Do List file and change the data as per your project.

**[Click here to download the template](https://chandoo.org/wp/wp-content/uploads/2023/03/todo-list-template.xlsx)
.**

Step 1: Set up your To-do data tables
-------------------------------------

We need two tables of data to begin with.

**Table1:** this is our to-do activity data table. It should have activity, _optional due date_ and status columns at the minimum.

![To do activity data table](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2559.png)

**Table 2:** This table lists all the possible status options. You can load them with below values (or come up with your own statuses).

![to do status options](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2560.png)

Step 2: Link Status options to the todo Table
---------------------------------------------

Once we link the “status” and “todo” tables, we can easily update the todo status, as demoed below:

![](https://chandoo.org/wp/wp-content/uploads/2023/03/demo-todo-marking-an-acivity-as-done.gif)

To do this (excuse the pun), ![defining a name in excel for our todo status options](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2561.png)

1.  Select the “todo status” column in our second table
2.  Use “Formula” ribbon > Define Name button (ALT M M), and create a name for this column. I named mine **status\_options**
3.  Go back to the “Todo” table and select the status column.
4.  Go to Data ribbon > Data Validation and set up a List validation with source as _**status\_options**_

Now our status column is linked with the options we have defined.

Step 3: Create the CANVAS for visual To-Do List
-----------------------------------------------

Let’s setup the canvas for our todo list. Add a blank sheet and,

1.  Make three columns wide enough to show the todo activities
2.  Add a title and format it nicely. I used the “shapes” in insert ribbon for this.
3.  Add a footer and do the same.
4.  Add background colors and tidy up as needed.

Here is a high-speed show-reel of my formatting setup.

Step 4: Formula Time
--------------------

Time for some number crunching. We need to use two formulas to get the ongoing activity list and structure it for our output page.

Add another sheet for the calculations and set up below two formulas.

![](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2562.png)

### The formulas

Our first formula (set up in cell B3 in the calculation worksheet) fetches all the ongoing activities and sorts the data using [FILTER & SORT functions](https://chandoo.org/wp/dynamic-array-functions/)
.

				
					`=SORT(FILTER(todo[[Activity]:[Due-date?]],(todo[Status]="Ongoing")+(todo[Status]="")),2,1)`
				
			

The second formula rearranges this data in to a single column using the TOCOL() function.

				
					`=TOCOLO(B3#)`
				
			

LAST STEP: Bring everything together to make the To-Do List
-----------------------------------------------------------

Go the canvas todo list we created in step 3 and get first 12 rows of our TOCOL() output for first column, next 12 rows for the middle column and the next 12 rows for the last column.

Tidy up and format as needed.

Tadaaaa, our To-Do List is ready!

![To-do list in Excel - Demo & Free template](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2558.png)

Video Tutorial - How to make a To-Do List in Excel?
---------------------------------------------------

If you need more help with these instructions, check out the video tutorial I made below or [on my YouTube Channel](https://www.youtube.com/watch?v=mA93MQgKRTc)
.

Download FREE To-Do List Excel Template
---------------------------------------

Don’t want to make your formulas and formatting? You can download my ready-to-use To-Do List file and change the data as per your project.

**[Click here to download the template](https://chandoo.org/wp/wp-content/uploads/2023/03/todo-list-template.xlsx)
.**

**Ready to use Project Management Templates**

Create Gantt charts, Project Dashboards, Burn Down Charts and Risk Trackers with your data in just minutes.

Get my ready to use Excel Project Management Bundle [from here](https://chandoo.org/pmt/pmt-index-1.html)
.

![Project Management Templates - Excel Pack by Chandoo](https://cache.chandoo.org/images/pm/img/purchase-pm-templates.png)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/beautiful-to-do-list-excel-template/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/beautiful-to-do-list-excel-template/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [FILTER()](https://chandoo.org/wp/tag/filter/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sort()](https://chandoo.org/wp/tag/sort-2/)
    , [to do list](https://chandoo.org/wp/tag/to-do-list/)
    , [to do list with excel](https://chandoo.org/wp/tag/to-do-list-with-excel/)
    , [tocol()](https://chandoo.org/wp/tag/tocol/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousSend Email from Excel with Office Scripts & Power Automate](https://chandoo.org/wp/send-email-from-excel-with-office-scripts-power-automate/)

[NextA clever technique to simplify your long, nested IF formulasNext](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/)

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
    
    [Reply](https://chandoo.org/wp/beautiful-to-do-list-excel-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/beautiful-to-do-list-excel-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/beautiful-to-do-list-excel-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ