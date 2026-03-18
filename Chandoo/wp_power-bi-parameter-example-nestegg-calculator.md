# Making a nest egg calculator- Power BI Parameter Example

**Source:** https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

Nest Egg Calculator using Power BI
==================================

*   Last updated on August 6, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_![](https://chandoo.org/wp/wp-content/uploads/2018/08/power-mondays-logo.png)**Welcome to Power Mondays.** Every Monday, learn all about Power BI, Power Query & Power Pivot in full length examples, videos or tips. In the first installment, let’s take a look at something we all can related to – Money._ 

We all know that Power BI is good for creating awesome visual experiences. Today let me share another **fun way to use Power BI – to build a calculator**. Learn how to create nest egg calculator in this Power BI parameter example tutorial.

This is what our output looks like:

![Power BI parameter example - Nest egg calculator](https://chandoo.org/wp/wp-content/uploads/2018/08/nest-egg-calculator-powerbi-demo.gif)

Ready to learn how to do this in Power BI? Read on then…

Creating a nest egg calculator with Power BI Parameters – Step by step tutorial
-------------------------------------------------------------------------------

![Nest egg - retirement savings calculator - Power BI Tutorial](https://chandoo.org/wp/wp-content/uploads/2018/08/nest-egg-calculator-power-bi.png)

We will use a very interesting and little known feature of Power BI – what-if _parameters_ to build our nest egg calculator.

If you are new to Power BI, check out this [excellent tutorial](https://chandoo.org/wp/introduction-to-power-bi/ "Introduction to Power BI")
 before reading rest of this.

### Step 1: Defining goals for the nest egg calculator

Just as building a large nest egg requires patience and planning, our nest egg calculator too needs some planning. But what planning you say? Just thinking out loud what our calculator should look like and what it should do is enough. So on that note, let’s define some goals:

*   We have two kinds of savings – regular (monthly) and one time (already invested)
*   The expected rate of return is different for each type of saving
*   We want to see how the nest egg will grow over time, for example, next 30 years

Let’s say we want to figure out future value of 3 monthly investments and an existing investment. Each has their own expected rate of return.

We need to calculate value of investment at the end of year for next 30 years. _ie Future value of our investment._

### Step 2: Set up Power BI parameters to capture inputs

As each of our inputs can change, we need something that let’s us toy with the inputs. Guess what? We will use **Parameters.** This feature of Power BI let’s you add a what-if parameter to your workbook.

When you add a what-if parameter, Power BI does two things:

*   Creates a table with all possible parameter values
*   Creates a harvester measure that tells you which value is selected by user

**To insert a parameter:**

![What if parameters in Power BI](https://chandoo.org/wp/wp-content/uploads/2018/08/what-if-parameter-powerbi.png)

Open blank Power BI workbook and using what-if parameter button in the modeling tab, insert a parameter, as below.

#### Power BI Parameter Example – Demo

![Power BI Parameters explained](https://chandoo.org/wp/wp-content/uploads/2018/08/what-if-parameter-explained.png)

Now, repeat this step for 7 more times, so that we end up with 8 parameter tables, as described below.

![List of parameters required for Power BI retirement savings calculator](https://chandoo.org/wp/wp-content/uploads/2018/08/parameters-to-create-powerbi-nest-egg-calculator.png)

At the end of this step, we will have 8 tables and 8 measures.

Lay out the parameter slicers like this on the canvas:

_Note: You need to **enable slider** for the slicers._

![Power BI Parameter example - sliders layout on the canvas](https://chandoo.org/wp/wp-content/uploads/2018/08/parameter-slicers-nest-egg-calculator.png)

### Step 3: Create a table for forecast

![Forecast years table generated thru Power Query](https://chandoo.org/wp/wp-content/uploads/2018/08/projection-years-table-power-query.png)We want to forecast the future value of investments for next 30 years. That means, we need to know the future value for each of those 30 years. If only, we had a table with numbers 0 to 30, then we can write some sort of DAX formula to calculate the FV.

To start off, let’s generate a table with numbers 0 to 30 (31 rows). You can do this in either Power Pivot (using GENERATESERIES() DAX formula) or in Power Query using the query ={0..30}

Let’s do this in Power Query. To create the forecast table in PQ:

1.  Go to home > get data > blank query
2.  When a blank query is created in PQ, in the formula bar type ={0..30} and press enter
3.  PQ will create a series of 31 numbers (starting from 0 and ending at 30) as a list
4.  Convert this list to a table using List tools > Transform ribbon.
5.  Add any other columns (derived) if you want.
6.  Name this query as Projection and load it to Power BI.

If you are new to Power Query, check out this [beginner how to](https://chandoo.org/wp/resources/introduction-to-power-query/ "Introduction to Power Query")
 to understand how it works.

### Step 4: Calculate forecast values

Now that our parameters and forecast table are ready, we can calculate future values of each investment. If you have this data in Excel, you can use FV() function to calculate the value. Unfortunately, Power Pivot doesn’t have FV() DAX formula. So how?

Simple, we can write the actual algebra.

The equation for future value of **P** payment for **n** periods at **r** interest rate is:

FV = P\*(((1+r)^n – 1) / r)

For example, for \[Amount 1 Value\] of $100 invested at \[Growth 1 Value\] for 5 years would be:

\=\[Amount 1 Value\] \* (((1+\[Growth 1 Value\])^5 – 1)/\[Growth 1 Value\])

**But wait, we are investing monthly…**

As we are investing _monthly_ instead of yearly, we need to to change r & n to r/12 and n\*12.

So the final formula for future value after 5 years will be:

\=\[Amount 1 Value\] \* (((1+\[Growth 1 Value\]/12)^(5\*12) – 1)/(\[Growth 1 Value\]/12))

Replacing the division with DIVIDE() DAX formula, we get:

\= \[Amount 1 Value\] \* DIVIDE(((1+\[Growth 1 Value\]/12)^(5\*12)-1),(\[Growth 1 Value\]/12),1)

**Calculating for all years**

The above DAX formula works only for 5th year. How to calculate for any year?

Simple, we create a measure called as \[selected year\] which when used in a visual (like chart or table) will return different years. Something like =MAX(Projection\[year\]) should do.

Replacing 5 with \[selected year\], we get:

Amount 1 FV := \[Amount 1 Value\] \* DIVIDE(((1+\[Growth Pct 1 Value\]/12)^(\[selected year\]\*12)-1),(\[Growth Pct 1 Value\]/12),1)

Create 2 more such measures for Amount 2 FV and Amount 3 FV.

**Calculating Future Value of \[Amount have\]:**

In case of starting amount (existing investments), we can use compound interest logic to calculate future value.

The future value of amount **P** invested at **r** interest over **n** periods is given by this formula:

\=P\*(1+r)^n

Here is the measure for same:

Already have FV := \[Already have Value\]\*(1+’Growth Pct (have)'\[Growth Pct (have) Value\])^\[selected year\]\*1000

Remember, already have value is entered in $000s, so we must multiply the result with 1000.

### Step 5: Visualize the result

And now comes the best part. We visualize all the yummy results calculated by our measures.

Start by inserting a stacked area chart. This is perfect for our calculator.

Add years as axis. Add \[Amount 1 FV\], \[Amount 2 FV\], \[Amount 3 FV\] and \[Already have FV\] as values. Your chart is ready.

![Forecast visual - stacked area chart - nest egg calculator](https://chandoo.org/wp/wp-content/uploads/2018/08/forecast-visual-nest-egg-calculator.png)

When you put years on X axis of this visual, Power BI (thru Power Pivot) calculates the future value of all 4 investments for each year and shows the output as a stacked area chart. Cool no?

Now as you play with the sliders, the future amounts change. Go ahead and find out how much your nest egg will be worth. And then start working towards it.

See all of it in action – Live retirement savings calculator
------------------------------------------------------------

Want to play with this but not near Power BI? Just use the embedded Power BI visual below to play and find out how much your nest egg will be worth.

<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">?</span>

### Download Nest Egg calculator Power BI workbook

[**Click here to download the PBIX file**](https://files.chandoo.org/pbix/nest-egg-calculator.pbix)
 for this. Play with it to learn more.

Note: This is made with July 2018 release of PBI, but should work in any recent version. If you notice anything funny, drop a comment so I can help.

### Want more Power? Check out these amazing examples

If you like Power BI, please check out these examples to see other creative ways to use it.

*   [Which countries did better – Commonwealth Games 2018 dashboard in Power BI](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/)
    
*   [Homer Simpson in Power BI – D’oh counter](https://chandoo.org/wp/doh-powerbi/)
    
*   [Bitcoin what-if calculator in Power BI](https://datachant.com/2018/01/26/bitcoin-calculator-power-bi-2/)
     \[Data Chant\]
*   [Visual flair with custom backgrounds](https://powerpivotpro.com/2018/07/adding-visual-flare-in-power-bi-with-background-colors/)
     \[Power Pivot Pro\]
*   [Collapsible slicer pane for your Power BI Reports](https://dataveld.com/2018/04/30/build-collapsible-slicer-pane-power-bi/)
     \[Data Veld\]

**_Excited about Power Mondays? Tell me what you want to see more?_**

I am super excited about Power Mondays. Every Monday, you will see the mighty magic of various Power tools. If you think I should talk about a certain business problem or concept, please post your suggestion in the comments. I will research and write about it on the blog in a subsequent Power Monday episode.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/#respond)
    
*   Tagged under [dax](https://chandoo.org/wp/tag/dax/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [future value in Power BI](https://chandoo.org/wp/tag/future-value-in-power-bi/)
    , [FV](https://chandoo.org/wp/tag/fv/)
    , [measures](https://chandoo.org/wp/tag/measures/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power mondays](https://chandoo.org/wp/tag/power-mondays/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [selectedvalue()](https://chandoo.org/wp/tag/selectedvalue/)
    , [what-if analysis](https://chandoo.org/wp/tag/what-if-analysis/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousExcel School v2.0, blogging schedule, personal life – a quick update](https://chandoo.org/wp/excel-school-v2-0-blogging-schedule-personal-life-a-quick-update/)

[Next12 Steps to learn Excel and become awesome @ work in 2018Next](https://chandoo.org/wp/12-ways-to-learn-excel/)

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
    
    [Reply](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/power-bi-parameter-example-nestegg-calculator/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ