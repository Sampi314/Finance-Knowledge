# Building a simple timer using Excel VBA to track my Rubik's cube solving speed [case study] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Building a simple timer using Excel VBA to track my Rubik’s cube solving speed \[case study\]
=============================================================================================

*   Last updated on May 13, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Today, lets learn how to make a simple timer app using Excel.** First some background…,

![Rubik's Cube](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Rubik%27s_cube.svg/200px-Rubik%27s_cube.svg.png)Recently, I learned how to solve Rubik’s cube from my nephew. As a budding cuber, I wanted to track my progress. Initially I used the stopwatch in my iPhone. But it wont let me track previous times. So I thought, _**“Well, I can use Excel for this”.**_

So I made a small timer app using Excel. Its quite minimalistic. It has a single button. I press it and it tracks the start time (date & time stamp). If I press the button again, it records the duration.

This way, I can see my progress over next few weeks and may be plot the trend.

Demo of the Excel VBA timer
---------------------------

Here is a short demo. This is what we will be building.

![Building a simple timer using Excel VBA to track time - demo](https://img.chandoo.org/vba/excel-timer-demo.gif)

Tutorial to make a timer in Excel
---------------------------------

To make a timer app in Excel, first we need to understand the logic for this. If VBA apps can be defined on a scale of 1 to 10 (1 being easiest to develop and 10 being most complex), our timer app can be classified as 1.5. It is really simple. But nevertheless, it is a good idea to list down various ingredients and basic logic to follow.

So we need,

*   A table to store the time stamps & durations
*   A button (simple text box will do) to start & stop the timer

### Set up the timer worksheet

In a blank worksheet, make space for a 2 column table. Type Time stamp & Duration as column headings and make a table from these (CTRL+T to insert the table)

_Note: For the macro to work, you do not need a table. Any 2 column range will do. A table makes our timer app look sexy._

Also, insert a rounded rectangle and format it to look like a button (from Format Ribbon > Shape Styles, select something slick and pretty)

In a blank cell, type the word “Start”. Name this cell as _timer.button.label_

Now, click on the rounded rectangle button, go to formula bar and type _**\=timer.button.label**_

> 💡 Tip: Yes, you can assign names or cell references to shapes. This way, whatever text is in the cell will be shown inside the shape.

**Other names to make:**

Although we can write VBA code without creating these names, our code will be readable with these names. So here we go:

*   Select the header “Timestamp” of the table and name it as _time.stamp.start_
*   Name the table as _Durations_ from Table Design ribbon
*   In a blank cell, write the formula =COUNTA(Durations\[Timestamp\])
*   This counts how many timestamps are already inserted.
*   Now name this cell as _count.of.timestamps_

We are done. Lets roll in to VBA.

### Writing the VBA code for timer

Open VBE (Visual Basic Editor) and insert a new module in your timer workbook. There write this code.

  
`Sub startStopTimer()     If Range("timer.button.label") = "Start" Then         Range("time.stamp.start").Offset(Range("count.of.timestamps") + 1).Value = Now         Range("timer.button.label") = "Stop"     Else         Range("time.stamp.start").Offset(Range("count.of.timestamps"), 1).Value = Now - Range("time.stamp.start").Offset(Range("count.of.timestamps"))         Range("timer.button.label") = "Start"     End If End Sub`

**Assign this macro to the timer button**

Right click on timer button and choose “Assign macro”. Select the startStopTimer sub from the list and click ok.

Now go ahead and test it. Assuming you have used same names as per this post, your timer should work.

### How this macro works?

When you click on the timer button, you want one of the 2 things to happen.

1.  You want to start the timer
2.  You want to stop the timer

What you want to do can be checked with this logical check.

`Range("timer.button.label") = "Start"`

If this is true, then you want to start the timer.  
Else, you want to stop the timer.

**If you want to start the timer**

Then, we need to go to the last row of the table + 1 and insert current time (_now_) in that cell.

This is done by,

`Range("time.stamp.start").Offset(Range("count.of.timestamps") + 1).Value = Now`

Once we do that, we need to change timer button’s text to “Stop”.

This is done by,

`Range("timer.button.label") = "Stop"`

**If you want to stop the timer**

Then, we need to go to the last row’s 2nd column of the table and print the difference between latest time (_now_) and starting time (last row, first column value)

This is done by,

`Range("time.stamp.start").Offset(Range("count.of.timestamps"), 1).Value = Now - Range("time.stamp.start").Offset(Range("count.of.timestamps"))`

Once we do that, we need to change the button text to “Start” by using this code:

`Range("timer.button.label") = "Start"`

That’s all. Our VBA code is rather simple.

One last step, formatting the duration
--------------------------------------

If you look at the duration, it could read something like 0.0042354. This is because duration is displayed as a fraction of day. So 0.0042354 means the duration is 0.42% of a day.

Now, wouldn’t it be better if we can show this in minutes and seconds?

To do that, select the entire table column of durations, press CTRL+1

Then, set formatting as custom and type code as \[mm\]:ss

And you are done!

Download Simple Timer Excel VBA workbook
----------------------------------------

**[Click here to download Simple Timer Excel VBA workbook](https://img.chandoo.org/vba/simple-timer.xlsm)
**. Play with it. Use it to track your Sudoku, crossword or knitting times. Or even Rubik’s cube times. See what trends and patterns you can uncover.

### Do you use Excel for tracking time?

I know many companies use Excel based trackers to keep track of employee time. I personally use time tracking features of Excel for needs like this all the time.

**What about you?** Do you use Excel time functions like NOW, TODAY and VBA to track progress? What techniques you apply? _**Please share using comments.**_

### Like tracking? You will love these

If you track things with Excel, you are going to find below tutorials very useful.

*   [Tracking issues & risks – Project management](http://chandoo.org/wp/2009/09/08/issue-trackers/)
    
*   [Tracking to dos – Project Management](http://chandoo.org/wp/2009/06/25/todo-lists-project-tracking-tools/)
    
*   [Expense tracker using Excel](http://chandoo.org/wp/2010/07/16/download-expense-trackers/)
     – 7 templates
*   [Annual goals tracker](http://chandoo.org/wp/2010/03/01/employee-goal-tracker-excel/)
    
*   **Bonus: [Introduction to VBA – 5 part crash course](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    **

Note: Rubik’s cube image by [Booyabazooka](http://commons.wikimedia.org/wiki/User:Booyabazooka "User:Booyabazooka")
 thru [Wikimedia](http://en.wikipedia.org/wiki/File:Rubik%27s_cube.svg)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [28 Comments](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [now()](https://chandoo.org/wp/tag/now/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [timer](https://chandoo.org/wp/tag/timer/)
    , [timestamps](https://chandoo.org/wp/tag/timestamps/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousModular Spreadsheet Development – A Thought Revolution](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/)

[NextCP008: 6 Tips to handle workbooks made by someone else, #4 is something I struggle with too!Next](https://chandoo.org/wp/cp008-6-tips-to-handle-workbooks-made-by-someone-else-4-is-something-i-struggle-with-too/)

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
    
    [Reply](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ