# Comprehensive Guide to VLOOKUP & Other Lookup Formulas » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/comprehensive-guide-excel-vlookup

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Comprehensive Guide to VLOOKUP & Other Lookup Formulas
======================================================

*   Last updated on November 25, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Excel VLOOKUP - a comprehensive guide](https://img.chandoo.org/f/vw/excel-vlookup-comprehensive-guide.png "Excel VLOOKUP - a comprehensive guide")

This week many Excel bloggers are [celebrating VLOOKUP week](http://vlookupweek.wordpress.com/)
. So I wanted to chip in and give you a comprehensive guide to VLOOKUP & Other lookup formulas. Read on …,

What is VLOOKUP Formula & how to use it?
----------------------------------------

I tell my [excel school](http://chandoo.org/wp/excel-schoo/)
 students that learning VLOOKUP formulas will change your basic approach towards data. You will suddenly feel that you have discovered a superman cape in your attic. It is that awesome.

**What does VLOOKUP really do?**

Imagine you have a list of data and you want answer a question like, “How many sales did Jimmy make?”

VLOOKUP is one of the formulas you can use in this situation. **VLOOKUP searches a list for a value in left most column and returns corresponding value from adjacent columns.**

![What is VLOOKUP formula and how to use it?](https://chandoo.org/img/i/formulas/vlookup.png "What is VLOOKUP formula and how to use it?")

**Read more – [What is VLOOKUP formula and how to use it?](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
**

Introduction to VLOOKUP, MATCH & OFFSET formulas
------------------------------------------------

VLOOKUP may not make you tall, rich and famous, but learning it can certainly give you wings. It makes you to connect two different tabular lists and saves a ton of time. In my opinion understanding VLOOKUP, OFFSET and MATCH worksheet formulas can transform you from normal excel user to a data processing beast.

![Introduction to VLOOKUP, MATCH & OFFSET formulas](https://chandoo.org/wp/wp-content/uploads/2008/11/vlookup-match-offset-help-thumb.png)

**Read more – [VLOOKUP, MATCH & OFFSET explained in plain English](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
**

How to do wildcard searches with VLOOKUP?
-----------------------------------------

Often we need our lookup formulas to go wild. Not in the sense of go-wild-and-chomp-a-few-kilo-bytes-of-data sense. But wild like wild cards. For eg. In the below data, we may not remember the full name of sales person, but we know that her name starts with _**jac**_. Now how do you get the sales amount for that person?

You can use wildcard characters \* and ? with VLOOKUP & several other Excel formulas.

![How to use VLOOKUP with wildcards?](https://img.chandoo.org/f/vw/vlookup-wildcard-operator-examples.png)

**Read more – [Using wildcards with VLOOKUP formulas](http://chandoo.org/wp/2010/11/01/using-wildcards-with-vlookup/)
**

Making VLOOKUPS dynamic with data validation
--------------------------------------------

Sometimes we don’t know what we want. If this happens when I am in a bar, I usually order a cocktail. Just a mix of everything. The same will work in Excel too.

For eg. If you have lots of data, but the value you want to look up needs to change based on whims and fancies of your users, then you can resort to a cocktail. A mix of VLOOKUP with Drop down lists (Data validation).

![Making VLOOKUPS dynamic with data validation](https://chandoo.org/img/f/vw/vlookup-mixed-with-data-validation-demo.gif)

**Read more – [Use data validation with VLOOKUP to lookup anything you want](http://chandoo.org/wp/2010/11/01/mix-vlookup-with-data-validation-for-some-magic-vlookup-week/)
**

How to lookup values to the left?
---------------------------------

There is no argument that VLOOKUP is a beautiful & useful formula. But it suffers from one nagging limitation. **It cannot go left.**

Let me explain, Imagine you have data like below. Now, if you want to find-out who is the sales person who made $2,133 in sales, there is no way VLOOKUP can come to rescue. This is because, once you search a list using VLOOKUP, you can only return corresponding items from the column at right, not at left.

![How to lookup values to the left?](https://chandoo.org/img/f/vw/vlookup-cannot-return-values-from-left.png)

**Read more – [How to use INDEX + MATCH combination to fetch values from left](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
**

How to lookup based on multiple conditions?
-------------------------------------------

Not always we want to lookup values based on one search parameter. For eg. Imagine you have data like below and you want to find how much sales Joseph made in January 2007 in North region for product “Fast car”? Read more to find how to solve this.

**Read more – [How to lookup based on multiple conditions?](http://chandoo.org/wp/2010/11/02/multi-condition-lookup/)
**

How to get values from multiple columns with VLOOKUP?
-----------------------------------------------------

VLOOKUP is great for extracting information from a huge data table based on what you are looking for. But what if you need to extract more than one column of information? For eg. Lets say you have salesperson’s name in left most column, and monthly sales figures in next columns, one for each month. Now, you want to find the total sales made by a given sales person. How do you go about it?

**Read more – [How to get values from multiple columns with VLOOKUP?](http://chandoo.org/wp/2010/11/08/vlookup-array-formula/)
**

Using VLOOKUP formula with tables
---------------------------------

Excel Tables, a newly introduced feature in Excel 2007 is a very powerful way to manage & work with tabular data. I really like tables feature and use them often. If you are new to tables, read up [Introduction to Excel Tables](http://chandoo.org/wp/2009/09/10/data-tables/)
. In this short video, understand how to use tables with VLOOKUP formulas.

**Watch the video – [Using VLOOKUP formula with tables](http://chandoo.org/wp/2010/11/09/using-lookup-formulas-with-excel-tables-video/)
**

Doing 2 way lookups in Excel
----------------------------

So far we have seen what VLOOKUP formula is and how to put it to some nifty uses. Lets go one step further and learn how to do 2 Way Lookups.

**What is a 2 Way Lookup?**

Lookup is when you find a value in one column and get the corresponding element from other columns. **2 Way Lookup is when you lookup value at the interesection of a given row & column values.**

![Doing 2 way lookups in Excel](https://img.chandoo.org/f/vw/2-way-lookup-formulas-in-excel.png)

**Read more – [2 way lookup formula in Excel](http://chandoo.org/wp/2010/11/09/2way-lookup-formulas/)
**

Getting 2nd matching value from a list using VLOOKUP
----------------------------------------------------

We know that VLOOKUP formula is useful to fetch the first matching item from a list. So what would you do if you need 2nd (or 3rd etc.) matching item from a list?

**Read more – [Getting 2nd matching value using VLOOKUP](http://chandoo.org/wp/2010/11/10/vlookup-second-value/)
**

Range lookups in Excel
----------------------

Here is a really tricky problem. Recently I was given a data set like this (shown below) and asked to find the position of lookup value in the list. The only glitch is that, instead of values, the lookup table contained lower and upper boundaries of the values. See the below illustration to understand the situation. In this case, how do you lookup?

![Range lookups in Excel](https://chandoo.org/img/f/vlookup-date-ranges-excel.png)

**Read more – [Doing range lookups in Excel](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
**

6 VLOOKUP tips
--------------

Ok, you have learned how to write vlookup formulas. You have also seen some pretty interesting examples of it.

But how do you write better VLOOKUP formulas?

**Read more – [6 VLOOKUP tips](http://chandoo.org/wp/2010/11/02/excel-vlookup-tips/)
**

FREE VLOOKUP cheat sheet – Download today
-----------------------------------------

Please download **free VLOOKUP formula cheat-sheet**. This cheat-sheet is prepared by **Cheater John** specifically for our readers. I hope you enjoy the one page help on VLOOKUP.

[**Download FREE VLOOKUP cheat sheet**](https://img.chandoo.org/d/Cheater_John_Excel_VLOOKUP_Chandoo.zip)

Your Favorite VLOOKUP Tips?
---------------------------

When I am working with data, not a day goes by without using some sort of lookup function. I use VLOOKUP, MATCH, INDEX, OFFSET, SUMIFS, SUMPRODUCT, GETPIVOTDATA in most of my dashboards & reports. These are easy to use once you understand the syntax and technique.

What about you? What are your favorite tips on VLOOKUP? How do you use lookup formulas? **Please share using comments.**

Want to Learn More Formulas? Get my VLOOKUP book
------------------------------------------------

If you want to learn VLOOKUP and other Excel lookup functions, then consider getting my VLOOKUP book.

|     |     |
| --- | --- |
| [![The VLOOKUP Book - Definitive guide to Excel lookup functions & tricks](https://img.chandoo.org/f/vw/the-vlookup-definitive-guide-to-excel-lookup-functions.png)](http://chandoo.org/wp/resources/the-vlookup-book/) | **Comprehensive and easy to understand**  <br>This is a book for everyone who uses Vlookup. Most of us think… Oh.. I already know the function. But this book will open your eyes to some brilliant techniques. – By Dr. Nitin Paranjape<br><br>**Solid introduction to lookup functions**  <br>This books does a wonderful job of taking each of the lookup functions available in Excel, breaking them down to a simple, easy-to-understand level. – by Lucas Moraga<br><br>[Get your copy](http://chandoo.org/wp/resources/the-vlookup-book/ "The VLOOKUP Book - Definitive guide to Excel lookup functions & tricks") |

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [39 Comments](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [vlookup week](https://chandoo.org/wp/tag/vlookup-week/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFormula Forensics 016. Suzannes DJIA Average](https://chandoo.org/wp/formula-forensics-016-suzannes-djia-average/)

[NextUsing Excel As Your DatabaseNext](https://chandoo.org/wp/using-excel-as-your-database/)

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
    
    [Reply](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ