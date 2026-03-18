# Growing a Money Mustache using Excel [for fun] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/growing-a-money-mustache-using-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Growing a Money Mustache using Excel \[for fun\]
================================================

*   Last updated on August 22, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Mustache and Excel?!? Sounds as unlikely as 3D pie charts & Peltier.**_ But I have a story to tell. So grab a cup of coffee and follow me.

Few months ago, I chanced up on a highly entertaining blog on money, retirement & living a kick-ass life. Reading [Mr. Money Mustache](http://www.mrmoneymustache.com/)
 is much like I am talking to myself. Almost all of his money philosophies, values & hacks are similar to what we practice at Chandoo household. Immediately I got hooked. In a span of 2 weeks, I read more than 100 articles, often making Jo suspicious _what I was doing so much on her iPad_.

**_At this point, you must be thinking -“Dude, what has all this got to do with Excel?!?”_**

And I am coming to that. One of the ideas Mr. Money Mustache preaches is small regular expenses can add up to massive amounts of cash (or ‘stash as he calls it) over several years. Now that we do not have a full time job, live in a small town & crave little, we barely spend anything. But I can relate to his idea. For example, if you spend a few dollars everyday at local coffee shop, over 10 years, this could add up to more than $10,000. Money that could be used for other worthy goals like early retirement or starting your dream company. Mind you, I have nothing against coffee. In fact, I brew two cups of lovely cappuccino every morning so that Jo and I can savor it before the kids wake up and start the _hulk\_in\_the\_house program._ It is another thing that the last time I bought a cup of coffee is when I was in Australia in June. But the important idea here is that regular expenses should be carefully monitored and pruned.

_“What?!? You are talking about coffee and kids. Where is Excel?!?”_

Ok, I am done with the build up. So one fine morning, I emailed Mr. Money Mustache, introduced myself as _somewhat spreadsheet skilled_ and shared a file I created with him, using which community at his site can see how regular expense cuts can impact their savings. He was kind enough to publish it [here](http://www.mrmoneymustache.com/2012/07/15/two-fun-tools-from-the-mmm-software-department/)
.

A growing mustache chart
------------------------

Well, I am not sure what else to call it. So lets stick with growing mustache chart. Here is how it works:

1.  You enter a sufficiently large number _ie the money you want to accumulate to retire or do something equally awesome._
2.  You also enter your regular expenses (daily, weekly, monthly, annual or one time) and amounts.
3.  Then it magically calculates how much money you would save by cutting them.
4.  All this is shown in a [dynamic chart](http://chandoo.org/wp/tag/dynamic-charts/)
     that depicts your target and actual as _mustaches_

**See this demo:**

![Growing Money Mustaches - a Dynamic chart in Excel](https://img.chandoo.org/trackers/growing-mustache-demo.gif "Growing Money Mustaches - a Dynamic chart in Excel")

This is so cool, how is it made?
--------------------------------

There are 4 steps to our growing mustache Excel chart.

### 1\. Calculating future value of regular expenses

Question: If you consume $3.50 latte every day for next ten years, how much would you spend?

_Answer: Gee! Sounds like a big problem, let me grab a cup of coffee first!_

On a more serious note, the future value of these little expenses depends on _rate of return_ as well. That is, instead of gulping down $3.50 in a hurry, if you saved the money **the return you get on yearly basis**.

For our calculations, we can assume a 7% return.  This gives a future value of$18,498.

You can use the formula `=FV(7%/365,365*10,3.5)` to get this value.

So the multiplication factor is 5,285 (18,498 divided by $3.5)

For our calculations, we can use a simple multiplication factor table so that we can focus on growing mustache than financial mumb0-jumbo.

![Multiplication Factor Table - FV Calculations for regular expenses](https://img.chandoo.org/trackers/multiplication-factors-for-fv-calculations.png "Multiplication Factor Table - FV Calculations for regular expenses")

### 2\. Calculating Totals

Once we know the future values of all such regular expenses, we just need a small table like this that shows the totals:

![Mustache target vs. actual calculations for bubble chart](https://img.chandoo.org/trackers/mustache-target-actual-calculations-for-bubble-chart.png "Mustache target vs. actual calculations for bubble chart")

### 3\. Create a bubble chart

Next, we [create a bubble chart](http://chandoo.org/wp/2009/10/05/bubble-chart-tutorial/)
 with 2 bubbles. 1 for the actual mustache & 1 for target mustache.

### 4\. Convert bubbles to mustaches

_Hermione_ would know a great spell to instantly turn our boring bubbles to mighty mustaches (_bulla-mustacium ?)_. But since we are muggles, lets focus on Excel trickery.

We need the chart on right from our bubbles:

![Convert bubbles to mustaches in excel bubble chart](https://img.chandoo.org/trackers/convert-bubbles-to-mustaches-how-to.png "Convert bubbles to mustaches in excel bubble chart")

First get a nice handlebar mustache image from web, like this:

![Mustache images - bubble chart](https://img.chandoo.org/trackers/mustache-images.png "Mustache images - bubble chart")

1.  Then, copy the gray color mustache (ctrl+c)
2.  **Next, select outer bubble (target) and press paste (ctrl+v)**
3.  Now, the bubble becomes mustache!
4.  Repeat the steps for actual bubble too.

_**That is all!**_

Download Excel Mustache Chart
-----------------------------

**[Click here to download this chart](https://img.chandoo.org/trackers/growing-mustache.xlsx)
** and play with it. Examine the formulas in “Stash chart” sheet to see how it works.

Do you like the growing mustache chart?
---------------------------------------

I really liked how this turned out. Simple yet effective. Readers at Mr. Money Mustache site loved it too.

**What about you?** Did you enjoy this trick. Are you planning to cut any regular expenses after reading this?  _**Please share using comments.**_

More on Excel and your money
----------------------------

I believe in being frugal, consuming less and living a simple life. So naturally we talk about using Excel to keep track of your expenses, investments, understand the impact of small changes etc. Check out below links to see more on Excel & your money.

*   [Expense trackers in Excel](http://chandoo.org/wp/2010/07/16/download-expense-trackers/)
    
*   [Household Budget Tracker](http://chandoo.org/wp/2009/11/23/household-budget-spreadsheets/)
    
*   [Stock Portfolio Tracker](http://chandoo.org/wp/2010/06/02/excel-stock-quotes/)
    
*   [Excel retirement calculator](http://chandoo.org/wp/2009/07/29/excel-goal-seek-tutorial/)
    
*   [Interactive mortgage payment calculator](http://chandoo.org/wp/2010/01/20/mortgage-payment-calculator/)
    
*   [Mutual Fund Portfolio Tracker](http://chandoo.org/wp/2008/04/18/mutual-fund-portfolio-tracker-using-ms-excel/)
     \[for India only\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [30 Comments](https://chandoo.org/wp/growing-a-money-mustache-using-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/growing-a-money-mustache-using-excel/#respond)
    
*   Tagged under [bubble charts](https://chandoo.org/wp/tag/bubble-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel chart templates](https://chandoo.org/wp/tag/excel-chart-templates/)
    , [FV](https://chandoo.org/wp/tag/fv/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [personal finance](https://chandoo.org/wp/tag/personal-finance/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [trackers](https://chandoo.org/wp/tag/trackers/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHomework: Can you extract dates from text?](https://chandoo.org/wp/extract-dates-from-text/)

[NextFormula Forensics No. 027 – Remove Leading ZeroesNext](https://chandoo.org/wp/formula-forensics-no-027/)

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
    
    [Reply](https://chandoo.org/wp/growing-a-money-mustache-using-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/growing-a-money-mustache-using-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/growing-a-money-mustache-using-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ