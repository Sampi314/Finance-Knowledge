# Charmed Price Problem » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/charmed-price-problem

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Charmed Price Problem
=====================

*   Last updated on October 6, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Here is a charming little problem to kick start your day._

Lets say you run a cute little bakery around the corner. Since you want your prices to look charming, you have a policy to round them down or up based on below rule.

> If the price ends with 0, 1 or 2 cents, round it down to 9 cents.
> 
> If the price ends with 3, 4 or 5 cents, round it up to 5 cents.
> 
> If the price ends with 6, 7, 8 or 9 cents, round it up to 9 cents.

**For example,**

![Charmed Price Problem - Rounding prices using Excel formulas](https://img.chandoo.org/f/charmed-price-problem-rounding-prices-using-excel.png)

_So how do you round to nearest charmed price?_ You could do it manually. But you would rather bake a few more of those Tiny Cup Cakes than waste time rounding the prices. So you want an automatic way to round prices. This is where Excel helps.

Formula for rounding to charmed price
-------------------------------------

There are many ways to write a formula for this.

### The first and most obvious method is to use IF formula

Assuming regular price is in cell C4, The formula for charmed price would look like this:

\=ROUNDDOWN(C4,1) + IF(MOD(C4,0.1)<=0.02,-0.01, IF(MOD(C4,0.1)<=0.05,0.05,0.09))

Go ahead and take a hard look at it.

The first that strikes us when you read it would be,

_‘Gee, Thats one long formula. I need a coffee.’_

**How it works:**

*   First we round down the price (in C4) to 10 cents with ROUNDDOWN(C4,1)
*   Then we add or subtract few cents to get the charmed price with IF formula.
*   IF the cents are less than or equal to 0.02, we subtract 1 cent
*   IF the cents are between 3 & 5, we add 5 cents.
*   Else, we add 9 cents.

So for example, if the actual price is $2.37, the formula gives $2.39 thru below process.

1.  Price rounded down to 10 cents will give $2.30
2.  MOD(2.37,0.1) gives 0.07
3.  This is falls in to the else portion of 2nd IF formula
    1.  IF(MOD(2.37,0.1)<=0.02,-0.01, IF(MOD(2.37,0.1)<=0.05,0.05,0.09))
4.  So we add 9 cents to the rounded down price.
5.  Hence the charmed price is $2.39

\[Related: [Introduction to IF formula](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)\
\]

### An improvement – CHOOSE formula

If the _IF formula_ is too long & difficult to write, we can choose _CHOOSE formula_.

It goes like this:

\=C4 + CHOOSE(MOD(INT(C4\*100),10)+1,-0.01,-0.02,-0.03,0.02,0.01,0,0.03,0.02,0.01,0)

This formula takes the price in C4 & adds or subtracts necessary cents to it to get the charmed price.

Examining it with $2.37 gives,

\=2.37 + CHOOSE(MOD(INT(C4\*100),10)+1,-0.01,-0.02,-0.03,0.02,0.01,0,0.03,0.02,0.01,0)  
\=2.37 + CHOOSE(8, \-0.01,-0.02,-0.03,0.02,0.01,0,0.03,0.02,0.01,0)=2.37 + 0.02  
\=2.39

\[Related: [Introduction to CHOOSE formula](http://chandoo.org/wp/2014/07/16/introduction-to-choose-function/ "CHOOSE() me, an introduction to Excel CHOOSE function")\
\]

### VLOOKUP & A mapping table

We can simplify our CHOOSE formula with a mapping table.

Lets say, somewhere in the workbook, we have set up a mapping table like this:

![Mapping Table 1 - Charmed Price Problem](https://img.chandoo.org/f/mapping-table-1-charmed-price-problem.png)

Then, we can use VLOOKUP formula to calculate charmed price:

\=C4+VLOOKUP(MOD(INT(C4\*100),10), mapping.table, 2 ,FALSE)

This formula is similar to CHOOSE formula.

**How it works?**

_Assuming actual price is $2.37,_

\=2.37 + VLOOKUP(MOD(INT(C4\*100),10), mapping.table, 2 ,FALSE)  
\=2.37 + 0.02 = 2.39

\[Related: [Introduction to VLOOKUP formula](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)\
\]

### VLOOKUP & A smaller mapping table

Using a combination of rounded down price & approximate lookup feature of VLOOKUP, we can come up with a smaller formula.

This requires a new mapping table like this:

![Mapping Table 2 - Charmed Price Problem - Excel formulas](https://img.chandoo.org/f/mapping-table-2-charmed-price-problem.png)

Our formula now looks like this:

\=ROUNDDOWN(C4,1) + VLOOKUP(MOD(INT(C4\*100),10),new.mapping,2)

**How it works?**

\=ROUNDDOWN(2.37,1) + VLOOKUP(MOD(INT(2.37\*100),10),new.mapping,2)  
\=2.3 + VLOOKUP(MOD(237,10),new.mapping,2)  
\=2.3 + VLOOKUP(7,new.mapping,2)  
\=2.3 + 0.09  
\=2.39

Download Example Workbook
-------------------------

[**Click here to download charmed price example workbook**](https://img.chandoo.org/f/charmed-price-problem.xlsx)
. Examine it to understand various formulas discussed in this article.

### Challenge for you – write another formula for charmed prices

**Here is a challenge for you.** Assuming the price is in C4, can you come up with another way to calculate charmed price? Please share your formulas in the comments section.

_Go ahead and charm us._

### Want to charm your boss? Learn these as well

Excel spreadsheets are like _transmogrification cloaks._ If you put on the right ones, you will instantly become incredibly charming. So learn how to weave powerful spreadsheets and charm everyone around you. Start with these:

*   [18.2 tips to rounding numbers in Excel](http://chandoo.org/wp/2012/09/28/round-numbers-excel-formulas/)
    
*   [Calculating new prices after % hike](http://chandoo.org/wp/2012/03/08/formula-forensic-no-015/)
    
*   [IF formula challenge for you](http://chandoo.org/wp/2012/04/25/if-formula-challenge-for-you/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/charmed-price-problem/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/charmed-price-problem/#respond)
    
*   Tagged under [choose()](https://chandoo.org/wp/tag/choose/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [INT()](https://chandoo.org/wp/tag/int/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [mround](https://chandoo.org/wp/tag/mround/)
    , [round](https://chandoo.org/wp/tag/round/)
    , [rounddown()](https://chandoo.org/wp/tag/rounddown/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousCP021: How to quickly compare 2 lists in Excel](https://chandoo.org/wp/cp021-how-to-quickly-compare-2-lists-in-excel/)

[NextA better chart to visualize “Best places to live” – Top 100 cities comparison Excel chartNext](https://chandoo.org/wp/top-100-cities-chart/)

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
    
    [Reply](https://chandoo.org/wp/charmed-price-problem/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/charmed-price-problem/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/charmed-price-problem/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ