# Introduction to VBA & Excel Macros - What are they & Writing your First Macro using Excel

**Source:** https://chandoo.org/wp/introduction-to-vba-macros

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

What is VBA & Writing your First VBA Macro in Excel \[VBA Crash Course Part 1 of 5\]
====================================================================================

*   Last updated on July 24, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This article is part of our VBA Crash Course.**_ Please read the rest of the articles in this series by clicking below links.

![Introduction to VBA & Excel Macros - What are they & Writing your First Macro using Excel](https://chandoo.org/img/vba/crash-course/excel-vba-crash-course.png)

1.  **What is VBA & Writing your First VBA Macro in Excel**
2.  [Understanding Variables, Conditions & Loops in VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)
    
3.  [Using Cells, Ranges & Other Objects in your Macros](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/)
    
4.  [Putting it all together – Your First VBA Application using Excel](http://chandoo.org/wp/2011/09/02/excel-vba-demo-application/)
    
5.  [My Top 10 Tips for Mastering VBA & Excel Macros](http://chandoo.org/wp/2011/09/06/top-10-tips-for-excel-vba/)
    

Introduction to Excel VBA
-------------------------

Everyone has a language. My mother tongue is Telugu. But I also speak Hindi, English and Cutish (that is the language my 2 year old kids speak). You may be fluent in English, Spanish, French, German or Vietnamese.

Just like you and I, **Excel has a language too, the one it can speak and understand. This language is called as VBA (Visual Basic for Applications)**.

When you tell instructions to Excel in this VBA language, Excel can do what you tell it. Thus enabling you to program Excel so that you can automate a boring report, format a big&ugly chart, clean-up some messy data or just play some random noises.

### What is a Macro then?

A macro is nothing but a set of instructions you give Excel in the VBA language.

Writing Your First Macro
------------------------

Note: If you are new computer programming, watch our **[Introduction to Programming Video](http://chandoo.org/wp/2011/05/13/introduction-to-programming/)
** before proceeding.

In order to write your first VBA program (or Macro), you need to know the language first. This is where Excel’s tape recorder will help us.

_**Tape Recorder?!?**_

Yes. Excel has a built-in tape recorder, that listens and records everything you do, in Excel’s own language, _ie_ VBA.

Since we dont know any VBA, we will use this recorder to record our actions and then we will see recorded instructions (called as _code_ in computer lingo) to understand how VBA looks like.

### Our First VBA Macro – MakeMeRed()

Now that you understand some VBA jargon, lets move on and write our very first VBA Macro. The objective is simple. When we run this macro, it is going to color the currently selected cell with Red. Why red? Oh, red is pretty, bright and awesome – just like you.

_**This is how our macro is going to work when it is done.**_

![Demo of your first macro using Excel VBA - A button to make any cell red](https://chandoo.org/img/vba/crash-course/your-first-macro-demo-vba-crashcourse.gif)

6 steps to writing your first macro
-----------------------------------

**I don’t see Developer Ribbon. Now what?** 

If you do not see Developer ribbon, follow these instructions.

**Excel 2007:**

1\. Click on Office button (top left)  
2\. Go to Excel Options  
3\. Go to Popular  
4\. Check “Show Developer Tab in Ribbon” (3rd Check box)  
5\. Click ok.

**Excel 2010:**

1\. Click on File Menu (top left)  
2\. Go to Options  
3\. Select “Customize Ribbon”  
4\. Make sure “Developer tab” is checked in right side area  
5\. Click ok.

**Step 1: Select any cell & start macro recorder**

This is the easiest part. Just select any cell and go to Developer Ribbon & click on Record Macro button.

![Recording a Macro using Excel Macro Recorder - Crash Course in Excel VBA](https://chandoo.org/img/vba/crash-course/recording-a-macro-in-excel.png)

**Step 2: Give a name to your Macro**

Specify a name for your macro. I called mine MakeMeRed. You can choose whatever you want. Just make sure there are no spaces or special characters in the name (except underscore)

Click OK when done.

**Step 3: Fill the current cell with red color**

This is easy as eating pie. Just go to Home ribbon and fill red color in the current cell.

**Step 4: Stop Recording**

Now that you have done the only step in our macro, its time to stop Excel’s tape recorder. Go to Developer ribbon and hit “stop recording” button.

![Stopping Excel's Macro Recorder - Excel VBA Crash Course](https://chandoo.org/img/vba/crash-course/stopping-macro-recorder.png)

**Step 5: Assign your Macro to a button**

Now go to Insert ribbon and draw a nice rectangle. Then, put some text like “click me to fill red” in it.

Then right click on the rectangle shape and go to Assign Macro. And select the MakeMeRed macro from the list shown. Click ok.

![Assigning Macros to Buttons - Excel VBA Crash Course](https://chandoo.org/img/vba/crash-course/assigning-macro-to-a-button.png)

**Step 6: Go ahead and play with your first macro**

That is all. Now, we have linked the rectangle shape to your macro. Whenever you click it, Excel would drop a bucket of red paint in the selected cell(s).

Go ahead and play with this little macro of ours.

Understanding the MakeMeRed Macro Code
--------------------------------------

Now that your first macro is working, lets peek behind the scenes and understand what VBA instructions are required to fill a cell with red.

To do this, right click on your current sheet name (bottom left) and click on View code option. (You can also press ALT+F11 to do the same).

This opens Visual Basic Editor – a place where you can view & edit various VBA instructions (macros, code) to get things done in Excel.

### Understanding the Visual Basic Editor:

Before understanding the MakeMeRed macro, we need to be familiar with VBE (Visual Basic Editor). See this drawing to understand it.

![Understanding Excel Visual Basic Editor - Crash Course in Excel VBA](https://chandoo.org/img/vba/crash-course/visual-basic-editor-introduction.png)

### Viewing the VBA behind MakeMeRed

1.  Select Module 1 from left side area of VBE (called as Project Explorer).
2.  Double click on it to open it in Editor Area (top right, big white rectangle)
3.  You can see the VBA Code behind MakeMeRed

_**If you have followed the instructions above, your code should look like this:**_

> `Sub MakeMeRed()   '   ' MakeMeRed Macro   '   With Selection.Interior   .Pattern = xlSolid   .PatternColorIndex = xlAutomatic   .Color = 192   .TintAndShade = 0   .PatternTintAndShade = 0   End With   End Sub`

_So much for a simple red paint!!!_

Well, what can I say, Excel is rather verbose when it is recording.

### Understanding the MakeMeRed VBA Code

Lets go thru the entire Macro code one line at a time.

*   **Sub MakeMeRed():** This line tells Excel that we are writing a new set of instructions. The word SUB indicates that the following lines of VBA are a sub-procedure (or sub-routine). Which in computer lingo means, a group of related instructions meant to be followed together to do something meaningful. The Sub-procedure ends when Excel sees the phrase “End Sub”
*   **Lines starting with a single quote (‘):** These lines are comments. Excel will ignore anything you write after a single quote. These are meant for your understanding.
*   **With Selection.Interior:** While filling a cell with Red color may seem like one step for you and I, it is in fact a lot of steps for your computer. And whenever you need to do a lot of operations on the same thing (in this case, selected cell), it is better to bunch all of them. This is where the WITH statement comes in to picture. When Excel sees _With Seletion.Interior,_ Excel is going to think, “_ok, I am going to do all the next operations on Selected Cell’s Interior until I see End With line_“
*   **Lines starting with .:** These are the lines that tell Excel to format the cell’s interior. In this case, the most important line is **.Color = 192** which is telling Excel to fill Red color in the selected cell.
*   **End With:** This marks the end of With block.
*   **End Sub:** This marks the end of our little macro named MakeMeRed().

### Few Tips to understand this macro better:

Once you are examining the macro code, here are a few ways to learn better.

*   **Change something:** You can change almost any line of the macro to see what happens. For example, change **.color = 192** to **.color = 62** and save. Then come back to Excel and run your macro to see what happens.
*   **Delete something:** You can remove some of the lines in the macro to see what happens. Remove the line **.PatternColorIndex = xlAutomatic** and run again to see what happens.

Download Example Workbook to learn VBA
--------------------------------------

[**Click here to download the example workbook with MakeMeRed Macro**](https://img.chandoo.org/vba/crash-course/our-first-macro.xlsm)
.  
[Excel 2003 Compatible Version here](https://img.chandoo.org/vba/crash-course/our-first-macro.xls)
.  
Play with the code & understand this better.

What Next – Understanding Variables, Conditions & Loops
-------------------------------------------------------

In the part 2 of this tutorial, Learn about [variables, conditions & loops – basic programming structures of VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)
.

Do you write VBA Code? Share your experience?
---------------------------------------------

Thanks to my college education & job experience. I am trained to be a programmer. So I find VBA quite intuitive and easy to use. But that may not be the case for many of you who latch on to VBA without any formal education.

I would like to know how you learn VBA and what experiences you had when you wrote that first macro. Please share using comments.

Join Our VBA Classes
--------------------

**We run an online VBA (Macros) Class to make you awesome.** This class offers 20+ hours of video content on all aspects of VBA – right from basics to advanced stuff. You can watch the lessons anytime and learn at your own pace. Each lesson offers a download workbook with sample code. If you are interested to learn VBA and become a master in it, please consider joining this course.

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

*   [91 Comments](https://chandoo.org/wp/introduction-to-vba-macros/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-vba-macros/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [programming](https://chandoo.org/wp/tag/programming/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [vba classes](https://chandoo.org/wp/tag/vba-classes/)
    , [with statement](https://chandoo.org/wp/tag/with-statement/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel School Prices Going up from 29th August, Join Now to save!](https://chandoo.org/wp/excel-school-prices-going-up-join-now/)

[NextUnderstanding Variables, Conditions & Loops in VBA \[Part 2 of 5\]Next](https://chandoo.org/wp/variables-conditions-loops-in-vba/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-vba-macros/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-vba-macros/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-vba-macros/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ