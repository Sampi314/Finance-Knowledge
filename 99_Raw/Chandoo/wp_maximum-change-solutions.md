# Calculating Maximum Change [solutions & discussion] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/maximum-change-solutions

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    

Calculating Maximum Change \[solutions & discussion\]
=====================================================

*   Last updated on March 26, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Maximum change problem - Solutions, Discussion & Video](https://img.chandoo.org/hw/maximum-change-problem-solutions-and-video.jpg)

Last Friday, we had a fun little Excel challenge – [Calculate Maximum Change](http://chandoo.org/wp/2014/03/21/calculate-maximum-change-homework/)
. More than 170 people commented and shared their solutions to this problem.

_**And the best part?**_

The best part is the **variety of solutions & thinking displayed by our community**. So if you are one of those 170, puff your chest & pat yourself on the back. Go ahead, I will wait.

Today, lets take a look at some of these awesome formulas and understand how they work. Read on and watch the video you below to gain few awesomeness pounds.

### First, lets understand the problem

Here is a look at the problem:

![Calculate maximum change - formula problem](https://chandoo.org/wp/wp-content/uploads/2014/03/fc-calculate-max-change.png)

We need more information to answer this question.

*   Are we talking about positive change, negative change or absolute change?
*   Are we talking about % change or value change?

In the original problem, even though I did not mention it, most people assumed that we want absolute change of value (ie the answer is 40, for Product 2).

But in real life, you may want to understand the problem a little more before writing any formulas.

_Note: The data is in C3:C8 for last month and D3:D8 for this month._

### Solution #1: Using MAX array formula

This is the solution most people got.

#### The array formula:

\=MAX(C3:C8-D3:D8)

press CTRL+Shift+Enter after typing.

#### How it works?

**C3:C8-D3:D8 portion:**  This gives the result {-20;40;15;21;0;-25} in array form.**MAX(…) portion:** This simply calculates the maximum value of above array and returns **40** as answer.

**Why press CTRL+Shift+Enter (CSE)?**

We need to press CTRL+Shift+Enter because MAX() is not capable of handling arrays. If you write MAX({-20;40;15;21;0;-25}) you would get **40**, but the same array when calculated by doing math on ranges will not work. To force MAX to treat arrays, we need to press CTRL+Shift+Enter.

### Solution #2: Using MAX+ABS array formula

Quite a few people figured out that the formula needs to work even when the change is negative. And that is where this new solution comes handy.

#### The array formula:

\=MAX(ABS(C3:C8-D3:D8))

press CTRL+Shift+Enter after typing.

#### How it works?

**ABS() portion:** converts the change values {-20;40;15;21;0;-25} to positive {20;40;15;21;0;25}

Rest of the formula is same as solution #1.

### Solution #3: Using INDEX to avoid Ctrl+Shift+Enter

The thing with Ctrl+Shift+Enter is that you have to remember it. If you accidentally press Enter instead of CSE, the formula stops working. One way to avoid this is to route the calculation thru an Excel function that can natively process arrays. This is where INDEX (or SUMPRODUCT etc.) come handy.

**The formula:**

\=MAX(INDEX(C3:C8-D3:D8,0))

or

\=MAX(INDEX(ABS(C3:C8-D3:D8),0))

**How it works?**

Same as Solution #1, except for this formula you do not have to press Ctrl+Shift+Enter. The INDEX will automatically calculate the array and send numbers to MAX. Then MAX feels mighty comfortable dealing with those numbers and spits out the answer as **40.**

**Learn more:**

*   [INDEX formula and how it works](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
    
*   [SUMPRODUCT formula and how it works](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/ "What is Excel SUMPRODUCT formula and how to use it?")
    

### Solution #4: Using AGGREGATE

AGGREGATE() is a new function introduced in Excel 2010. This too, like INDEX & SUMPRODUCT can process arrays natively (provided you are using one of the aggregates like LARGE). _Kyle_, one of our commenters shared 2 brilliant solutions that involve AGGREGATE.

#### The formula:

\=AGGREGATE(14,4,(C3:C8)-(D3:D8),1)

#### How it works?

**14, 4 portion:** This tells AGGREGATE that you want to calculate LARGE value (14) and you want to consider all cells (4). To understand more about AGGREGATE see the links below.

**(C3:C8)-(D3:D8) portion:** As seen above, this just gives an array – {-20;40;15;21;0;-25}

**1 portion:** This tells AGGREGATE that you want **1st** largest number.

#### Learn more:

*   [How to use AGGREGATE() in Excel](http://exceluser.com/excel_help/functions/function-aggregate.htm)
    
*   [How LARGE formula works?](http://chandoo.org/excel-formulas/large.shtml)
    
*   [A video on AGGREGATE function](https://www.youtube.com/watch?v=MQNVEieXnSg)
    

### Solution #5: Using MMULT and AGGREGATE

Now this is what I call a scary formula. It can potentially waste your entire afternoon when you try to understand it first time. But once you get it, you feel awesome. This too is posted by _Kyle._

#### The formula:

\=AGGREGATE(14,4,MMULT(C3:D8,{1;-1}),1)

#### How it works?

Watch the video. Explaining how this works in text is difficult.

#### Learn more:

I am still trying to understand MMULT(). It can be as complex and deep as string theory (or recipe of making bread at home). Go thru below links to learn more about it. Make sure you put on your helmet, cause it will blow your mind.

*   [MMULT example #1](http://chandoo.org/wp/2013/07/22/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/)
    
*   [MMULT example #2](http://chandoo.org/wp/2013/11/26/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/)
    

### More ways to get maximum change + Bonus problem

Watch below video to understand how to solve the maximum change problem and another related problem.

[**Click here to watch if you can’t see the video above**](https://www.youtube.com/watch?v=eTJEM7GoUnw)

### Download Answer workbook

[**Click here to download answer workbook**](https://img.chandoo.org/hw/max-change-problem.xlsx)
 and examine the formulas to learn more.

### What did you learn from this formula challenge?

I learned how to use AGGREGATE, Array SUMIFS and got a better handle on MMULT.

**What about you?** What did you learn thru this challenge. _Please comment and let us all know._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/maximum-change-solutions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/maximum-change-solutions/#respond)
    
*   Tagged under [abs()](https://chandoo.org/wp/tag/abs/)
    , [aggregate()](https://chandoo.org/wp/tag/aggregate/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MMult()](https://chandoo.org/wp/tag/mmult/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    

[PrevPreviousWhy you should close down Excel completely](https://chandoo.org/wp/why-you-should-close-down-excel-completely/)

[NextCP003: Business Intelligence for Masses – Interview with Mike AlexanderNext](https://chandoo.org/wp/cp003-business-intelligence-for-masses-interview-with-mike-alexander/)

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
    
    [Reply](https://chandoo.org/wp/maximum-change-solutions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/maximum-change-solutions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/maximum-change-solutions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ