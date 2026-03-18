# Putting It All Together - Our First VBA Application [Part 4 of 5 - Excel VBA Crash Course] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-vba-demo-application

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Putting It All Together – Our First VBA Application \[Part 4 of 5 – Excel VBA Crash Course\]
============================================================================================

*   Last updated on July 24, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This article is part of our VBA Crash Course.**_ Please read the rest of the articles in this series by clicking below links.

![What are Variables, Conditions & Loops are and how to use them in Excel VBA ](https://chandoo.org/img/vba/crash-course/excel-vba-crash-course.png)

1.  [What is VBA & Writing your First VBA Macro in Excel](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
2.  [Understanding Variables, Conditions & Loops in VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)
    
3.  [Using Cells, Ranges & Other Objects in your Macros](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/)
    
4.  **Putting it all together – Your First VBA Application using Excel**
5.  [My Top 10 Tips for Mastering VBA & Excel Macros](http://chandoo.org/wp/2011/09/06/top-10-tips-for-excel-vba/)
    

**In part 4 of our VBA Crash Course, we are going to create our very first VBA application using what we learned so far.**

Our first Application – What is it supposed to do anyway?
---------------------------------------------------------

Remember the “We Are Nuts” example. We are back to it. This time, we will create a daily sales tracker application that makes your job a breeze. But saying words like **_breeze_** when defining your next VBA application is a dangerous thing. **So lets list down all the things our little Excel VBA workbook should do.**  
![Sample Excel VBA Application - Demo - Excel VBA Crash Course](https://chandoo.org/img/vba/crash-course/sample-excel-vba-application-demo.png)

1.  The current method of using Inputboxes to capture 24 sale values and any reasons for deviation is tedious. So our application should instead process the values from already entered values and ask for reasons (thru inputbox) only when the sales are too low or too high.
2.  At the end of processing the sales, we want to see a short summary of how we did for the day. Something like this,  
    ![Summary Statistics shown in our application - Excel VBA Crash Course](https://chandoo.org/img/vba/crash-course/our-first-vba-application-summary-stats.png)
3.  Once we finish viewing the statistics a snapshot of the daily sales & along with summary statistics should be saved to current folder as PDF for later reference.

Designing our first VBA Application – Key Ingredients:
------------------------------------------------------

In this section, let us understand how our application should be designed and what goes in to it.

First, let us look at various things our application need to do, in a schematic. This types of diagrams are called as flow charts.

![Flow Chart for Our VBA Application - VBA Crash Course](https://chandoo.org/img/vba/crash-course/flow-chart-for-our-vba-application.png)

### Key Ingredients of our Daily Sales Tracker Application:

Lets look at each area of our application and understand what VBA technique or statement helps us to do it.

*   **Process one store sale at a time:** This is achieved with the FOR EACH statement \[Related: [What are VBA loops?](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)\
    \]
*   **Capture reasons for deviation:** Lets do InputBox() for this
*   **Calculate Summaries as we go:** Some variables to calculate the summaries as we go. And a few IIF() formulas to help us update the values where needed. (PS: IIF is Inline IF Formula)
*   **Display Summary Statistics:** We will use MessageBox() for this.
*   **Save a snapshot of the report:** This is done by Range.ExportAsFixedFormat() method. \[Related: [understanding cells, ranges & other VBA objects](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/)\
    \]

Demo of our Daily Sales Tracker VBA Application
-----------------------------------------------

Here is a quick demo of our Daily Sales Tracker Application

  

Download our Daily Sales Tracker VBA Workbook:
----------------------------------------------

[**Click here to download the Daily Sales Tracker VBA Workbook**](https://img.chandoo.org/vba/crash-course/our-first-vba-app-demo.xls)
. Enable macros, enter some values and play with it.

If you just want to examine code, [**see this page**](https://img.chandoo.org/vba/crash-course/our-first-vba-app-code.bas)
.

What Next – My top 10 tips for using VBA
----------------------------------------

**In final part of our VBA crash course, [Learn my top 10 tips for mastering VBA](http://chandoo.org/wp/2011/09/06/top-10-tips-for-excel-vba/)
.**

If you have not read, please read the first 3 parts of this series,

1.  [Introduction to Excel VBA – What is it & How to write your first VBA Macro](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    .
2.  [Understanding Variables, Conditions & Loops in VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/ "Understanding Variables, Conditions & Loops in VBA [Part 2 of 5]")
    
3.  [What are Excel VBA Objects and how to use them?](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/ "How to use Cells, Ranges & Other Objects in Excel VBA")
    

How do you like this VBA Application? How would you enhance it?
---------------------------------------------------------------

This application is one simple example of what you can do with VBA. Learning how to use Excel & VBA can enable you do several more awesome things at your work & life.

**Do you like this application?** How would you have designed it? _**Please share your ideas & tips using comments.**_

Join Our VBA Classes
--------------------

We run an online VBA (Macros) Class to make you awesome. This class offers 20+ hours of video content on all aspects of VBA – right from basics to advanced stuff. You can watch the lessons anytime and learn at your own pace. Each lesson offers a download workbook with sample code. If you are interested to learn VBA and become a master in it, please consider joining this course.

[**Click here to learn more and Join our VBA program**](http://chandoo.org/wp/vba-classes/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/excel-vba-demo-application/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-vba-demo-application/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [for loop](https://chandoo.org/wp/tag/for-loop/)
    , [if then statement](https://chandoo.org/wp/tag/if-then-statement/)
    , [iif](https://chandoo.org/wp/tag/iif/)
    , [inputbox](https://chandoo.org/wp/tag/inputbox/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [messagebox](https://chandoo.org/wp/tag/messagebox/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [vba classes](https://chandoo.org/wp/tag/vba-classes/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHow to use Cells, Ranges & Other Objects in Excel VBA](https://chandoo.org/wp/using-objects-in-vba-howto/)

[NextAnnouncing Online VBA Classes from Chandoo.org, Please Join TodayNext](https://chandoo.org/wp/online-vba-classes-join-today/)

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
    
    [Reply](https://chandoo.org/wp/excel-vba-demo-application/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-vba-demo-application/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-vba-demo-application/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ