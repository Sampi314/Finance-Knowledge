# How-to create an Excel Tracker that is elegant, fun & user-friendly - Tutorial » Chandoo.org

**Source:** https://chandoo.org/wp/create-an-excel-tracker

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

How-to create an elegant, fun & useful Excel Tracker – Step by Step Tutorial
============================================================================

*   Last updated on March 17, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Do you want to create a simple, elegant and useful tracker using Excel?** You can make trackers with features like tables, data validation rules and conditional formatting. In this page, I will explain the process for creating an Excel tracker. 

Demo of the Excel tracker we will be creating...
------------------------------------------------

![Excel tracker - quick demo](https://chandoo.org/wp/wp-content/uploads/2020/03/Excel-tracker-demo.gif)

[](https://chandoo.org/wp/wp-content/uploads/2020/03/How-to-create-a-tracker-demo.xlsx)

### [Download the tracker demoed here](https://chandoo.org/wp/wp-content/uploads/2020/03/How-to-create-a-tracker-demo.xlsx)

[**Click here to download the Excel Tracker**](https://chandoo.org/wp/wp-content/uploads/2020/03/How-to-create-a-tracker-demo.xlsx)
 explained in this page. Use it to understand the process or change it to suit your needs.

Purpose of the tracker
----------------------

> You can't track what you don't know...
> 
> Someone wise [Tweet](https://twitter.com/intent/tweet?text=You+can%27t+track+what+you+don%27t+know...+%E2%80%94+Someone+wise&url=https%3A%2F%2Fchandoo.org%2Fwp%2Fwp%2Fcreate-an-excel-tracker%2F&via=r1c1)

Let’s say you want to build a tracker to keep track of the visitors to the corporate office of Big Large Inc. You need to capture below details for compliance purpose.

*   Name
*   Type of person (Full time, Temporary or Visitor)
*   Department visiting (one of the 7 departments if the person is Full time or Temporary)
*   SOP status (Not started, read, read  & signed)

It is a fairly straight forward tracker, except for this bit:

_If the person is a visitor, then no need to get “department”._ 

**_Thanks to_ Colette**, who emailed me with a description of this template. 

Steps for creating Excel tracker
--------------------------------

### Step 1: Create a table with below columns.

Just type the headings, select them and press CTRL+T. 

![step 1 - create a table for excel tracker](https://chandoo.org/wp/wp-content/uploads/2020/03/step-1-create-a-table-for-tracker.png)

[](https://chandoo.org/wp/data-tables/)

### [Learn more about Excel Tables](https://chandoo.org/wp/data-tables/)

Excel tables can help you build trackers, plans, lists or data. They make data analysis, charting or pivoting a breeze too. If you are new to this powerful feature, check out this [getting started with tables guide](https://chandoo.org/wp/data-tables/)
.

### Step 2: Set up data validation rules

This is the important bit. We don’t want garbage data in our tracker. So set up simple rules on each column.

**Data validation rule for Type column:**

This is rather simple. Just select the Type column, go to Data > Validation and set up the validation type as “List”. Type out the possible values – Full time, Temporary, Visitor and click ok. Here is a screenshot of the process.

![data validation rules for type column](https://chandoo.org/wp/wp-content/uploads/2020/03/step-2-data-validation-rules-for-type-column.png)

[](https://chandoo.org/wp/excel-add-drop-down-list/)

### [Learn more about Data Validation Drop Down List](https://chandoo.org/wp/excel-add-drop-down-list/)

Data validation makes it easy to set up a list of allowed values for a cell or table column. [Learn more about setting up data validation list](https://chandoo.org/wp/excel-add-drop-down-list/)
.

**Data validation rule for Department column:**

_Now this is a tricky one._ We want to show a list of departments if type  = Full time or Temp. Else we want to leave it blank.

Start by setting up a list of departments in a range and give it a name like _lstDepts_ 

![List of departments](https://chandoo.org/wp/wp-content/uploads/2020/03/step-2-dv-rules-list-of-departments.png)

Now, we will create a **dynamic named range** that will return either lstDepts or blank depending on what is picked in \[@Type\] (the current row’s type value).

We can use the trusty IF formula for this.

\=IF(Table1\[@Type\]<>"Visitor",lstDepts,"NA")

Create **availableDepts** named range (Formulas > Define Name) like this:

![step 2 - conditional named range for departments](https://chandoo.org/wp/wp-content/uploads/2020/03/step-2-conditional-named-range-for-departments.png)

Once the named range is created, use it as **List** for data validation on the Department column as shown below.

![Data validation rule for department column](https://chandoo.org/wp/wp-content/uploads/2020/03/step-2-dv-rule-for-department-column.png)

**Data validation rule for “SOP Status” column:**

This is similar to the rule for “Type” column.

### Step 3: Highlight what matters with conditional formatting

Let’s say Big Large Inc. is fussy about the SOP status and want to quickly monitor anyone not starting the SOP process or half-done it.

You can use conditional formatting to easily spot these. 

Just set up rules to highlight the Status column based on what matters to you.

For example, if you want to highlight all “Read” statuses, you can use below rule.

![conditional formatting rule to highlight "Read" values](https://chandoo.org/wp/wp-content/uploads/2020/03/step-3-conditional-formatting-for-status-column.png)

Here are few more rules. 

![more CF rules for excel tracker](https://chandoo.org/wp/wp-content/uploads/2020/03/step-3-all-CF-rules.png)

That is all. Our tracker is ready. Go ahead and roll it out.

[](https://chandoo.org/wp/conditional-formatting-top-tips/)

### [Learn more about Conditional Formatting](https://chandoo.org/wp/conditional-formatting-top-tips/)

Conditional formatting is a great way to keep an eye on important bits of information. You can set up rules to highlight missed deadlines, top 5 values or values meeting a criteria. [Getting started with conditional formatting](https://chandoo.org/wp/conditional-formatting-top-tips/)
.

Video - How-to create an Excel tracker
--------------------------------------

If you are still fuzzy over the details of how to create a tracker in Excel (or you just want an earful of my sweet voice) you can watch below video. I explain the process with greater detail on the data validation rules. 

You can also [watch this video on Chandoo.org YouTube channel](https://youtu.be/e0s9xdx5FF8)
.

Download Excel tracker - Demo file
----------------------------------

[**Click here to download the Excel Tracker**](https://chandoo.org/wp/wp-content/uploads/2020/03/How-to-create-a-tracker-demo.xlsx)
 explained in this page. Use it to understand the process or change it to suit your needs.

Tips for creating AWESOME trackers
----------------------------------

Trackers are a big part of spreadsheet life. Here are my top tips for creating long-lasting, friendly and useful trackers.

*   **Use Tables for inputs:**  Tables are natural for keeping data like this. So use the liberally.
*   **Apply validation rules:** to prevent unwanted data from getting in. You can use data validation to allow lists, valid dates or even complex conditions. See this demo.

[![Either or condition in data validation](https://i0.wp.com/chandoo.org/img/dv/either-or-data-validation.gif)](https://chandoo.org/wp/either-or-data-validation/)

[Either or condition in data validation](https://chandoo.org/wp/either-or-data-validation/)

*   **For large trackers, create a settings tab:** If you have a large tracker with several columns and rules, create a separate worksheet to maintain the rule data (like validation lists, boundaries for valid values etc.)
*   **Apply conditional formats:** People like to know when their inputs are right. So use conditional formatting features like icons to highlight (in)valid data entries. See this demo.

[![using conditional formatting to highlight valid and invalid data entries](https://i2.wp.com/chandoo.org/img/cf/advanced-data-entry-form-example.png?resize=631%2C95)](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/)

[Awesome data entry forms with conditional formatting + data validation](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/)

*   **Consider Excel Forms instead of shared workbooks:** If you need multiple people to access the tracker to update or input data, consider using Excel Forms. This online features works great for collecting data in a secure manner. [Click here for more info](https://support.office.com/en-us/article/surveys-in-excel-hosted-on-the-web-5fafd054-19f8-474c-97ec-b606fcda0ff9)
    .

More Excel trackers for you
---------------------------

*   [Annual Calendar & Daily To do list template](https://chandoo.org/wp/free-2020-calendar-daily-planner-template/)
    
*   [Goal tracker](https://chandoo.org/wp/employee-goal-tracker-excel/)
    
*   [Project Plan & Gantt Chart](https://chandoo.org/wp/gantt-charts-project-management/)
    
*   [To-do list template](https://chandoo.org/wp/todo-list-with-priorities/)
    
*   [Meeting Agenda Template](https://chandoo.org/wp/agenda-template-excel/)
    
*   [20 Excel Templates & Trackers for you](https://chandoo.org/wp/free-excel-templates-download/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/create-an-excel-tracker/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/create-an-excel-tracker/#respond)
    
*   Tagged under [custom data validation](https://chandoo.org/wp/tag/custom-data-validation/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [tables](https://chandoo.org/wp/tag/tables/)
    , [trackers](https://chandoo.org/wp/tag/trackers/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousAdvanced Pivot Table Tricks for you](https://chandoo.org/wp/advanced-pivot-tables/)

[Next18 Tips to Make you an Excel Formatting ProNext](https://chandoo.org/wp/excel-formatting-tips/)

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
    
    [Reply](https://chandoo.org/wp/create-an-excel-tracker/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/create-an-excel-tracker/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/create-an-excel-tracker/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ