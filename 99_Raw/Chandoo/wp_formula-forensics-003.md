# Extracting a list of items from a mixed list by criteria

**Source:** https://chandoo.org/wp/formula-forensics-003

---

*   [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Luke](https://chandoo.org/wp/category/luke/)
    , [Posts by Luke](https://chandoo.org/wp/category/posts-by-luke/)
    

Formula Forensics No. 003 – Lukes Reward
========================================

*   Last updated on November 13, 2014

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Hello everyone. My name is [Luke M](http://chandoo.org/forums/profile/luke-m "Luke M.")
, and I’ve been coming to Chandoo’s site for about a year now.

I love solving problems, and helping people out on the [forums](http://chandoo.org/forums/ "Chandoo.org Forums")
.

Due partly to Hui’s challenge about submitting articles, and 3G’s comment the other day about this particular formula, I decided to try my hand at writing an article.

I Hope it helps explain some cool Excel tricks that I like to use. 🙂

The Problem
-----------

Often, I see a request from an individual asking for a formula that will be able to generate a list based off of some criteria, with no spaces/blanks.

As Chandoo & Hui have often pointed out, there’s not much Excel can’t do if you know the right functions to use.

Today, we’ll take a look at how we can accomplish this particular task.

[![](https://chandoo.org/wp/wp-content/uploads/2011/11/Luke2.png "Luke2")](https://chandoo.org/wp/wp-content/uploads/2011/11/Luke2.png)

Suppose I want to be able to generate a list of all the Vegetables.

In cell E2, I put this array formula:

\=IF(COUNTIF(A:A,$D$2) < ROWS($E$2:E2), “”,  INDEX(B:B,  SMALL( IF($A$2:$A$10 =$D$2, ROW( $A$2:$A$10)), ROW(A1))))

Remember, array formulas need to be confirmed using **Ctrl**+**Shift**+**Enter**, and will have curly brackets { } around the formula if done correctly.

I then copy the cell downward as far as I think will ever be necessary to display all the records (i.e. E7).

Lets Look Inside
----------------

Let’s take a closer look at how the formula works.

### Front Half

First, let’s look at the IF function’s logic check.

\=IF(COUNTIF(A:A,$D$2)<ROWS($E$2:E2),””, INDEX(B:B, SMALL( IF($A$2:$A$10 = $D$2, ROW($A$2:$A$10)), ROW(A1))))

We’re using the COUNTIF function to determine the total number of records that meet our criteria. We’re then comparing this to a ROWS function. The ROWS function simply returns the number of rows given in the argument. Note that the first part of the range callout uses an absolute reference and will not change, while the latter part is relative and will change as the formula is copied down. Thus, in the first cell, the ROWS function evaluates to 1. The next cell, it will evaluate to 2, then 3, and so on. So, the IF statement is checking to see if the number of records returned so far (i.e., formula used) is greater than the total number of possible records. If this is true, return a blank (i.e., “”).

### Back Half

The latter half of the formula is where things get tricky.

For this part, let’s work our way from the inside out.

We start off with another IF function:

INDEX(B:B,SMALL**(**IF($A$2:$A$10=$D$2, ROW($B$2:$B$10)), ROW(A1))))

This section compares A2:A10 with our criteria given in cell D2. So, the array if A2:A10 starts off looking like this:

{Fruit, Fruit, Vegetable, Vegetable, Fruit, Vegetable, “”, “”, “”}

When we compare it with the criteria, it becomes this:

{False, False, True, True, False, True, False, False, False}

Looking at the return values in our IF function, we see that only a True result is stated, the ROW.

INDEX(B:B,SMALL(IF($A$2:$A$10=$D$2, ROW($A$2:$A$10))**,** ROW(A1))))

So, each True value from the array above will be replaced with the corresponding Row value.

This causes the array to become this:

{False, False, 4, 5, False, 7, False, False, False}

Now that we have a nice array with some numbers in it, this gets fed into the SMALL function.

INDEX(B:B,SMALL(IF($A$2:$A$10=$D$2, ROW($A$2:$A$10)), ROW(A1))))

The ROW function at the end will serve as a type of counter.

In E2, where we initially place the formula, this will evaluate to 1, thus telling the SMALL function to return the 1st smallest number.

In E3, it will evaluate to 2, and the SMALL function will return the 2nd smallest number, and so.

So, taking the 1st smallest number from our array, we get the number 4.

We then take this to the INDEX function

INDEX(B:B,SMALL(IF($A$2:$A$10=$D$2, ROW($A$2:$A$10)), ROW(A1))))

Note that we need to callout the entire column, since we are plugging in row numbers.

The 4th row in column B leads us to the value “Broccoli”.

The next formula will return the 5th row, “Spinach”.

The 3rd formula will return the 7th row, “Peas”.

This method can be adapted for use with multiple criteria. We would just need to expand the IF function logic checks so that only the correct rows are returned.

PS. If it gets too confusing, the first part of the formula can be omitted.

\=IF(COUNTIF(A:A,$D$2)<ROWS($E$2:E2),””, INDEX(B:B, SMALL( IF($A$2:$A$10 = $D$2, ROW($A$2:$A$10)), ROW(A1))))

It is just there to hide any unwanted #NUM errors after all the pertinent records have been displayed.

EXTENSION
---------

To see how this technique can be extended to use multiple criteria please read the follow up post at:

[http://chandoo.org/wp/2014/11/10/formula-forensics-no-003b-lukes-reward-part-ii/](http://chandoo.org/wp/2014/11/10/formula-forensics-no-003b-lukes-reward-part-ii/ "http://chandoo.org/wp/2014/11/10/formula-forensics-no-003b-lukes-reward-part-ii/")

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2011/11/Luke-1a.xls "Luke Example File")
.

**OTHER POSTS IN THIS SERIES**
------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic 001](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/ "Taruns problem")
 – Tarun’s Problem

[Formula Forensic 002](http://chandoo.org/wp/2011/11/07/formula-forensics-002/ "Joyces' Question")
 – Joyce’s Question

THANK-YOU and a CHALLENGE
-------------------------

Firstly a Congratulations to **Luke M** on taking up the challenge and on your First Post at Chandoo.org.

Thank-you for explaining to us all how this formula, which has appeared a number of times on the [Chandoo.org Forums](http://chandoo.org/forums/ "Chandoo.org Forums")
, works.

The contents of the Post are published as Luke submitted it with only minor formatting changes.

My Challenge to you is this:

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post as Luke Did above.

If you have a formula that you would like explained but don’t want to write a post also send it in to Chandoo or Hui.

Send it to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [62 Comments](https://chandoo.org/wp/formula-forensics-003/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-003/#respond)
    
*   Tagged under [countif()](https://chandoo.org/wp/tag/countif/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [small](https://chandoo.org/wp/tag/small/)
    
*   Category: [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Luke](https://chandoo.org/wp/category/luke/)
    , [Posts by Luke](https://chandoo.org/wp/category/posts-by-luke/)
    

[PrevPreviousMaking Small Multiples in Excel \[Charting Technique\]](https://chandoo.org/wp/small-multiples-charts-in-excel/)

[NextAdd Data to Charts with Copy Paste \[Quick Tip\]Next](https://chandoo.org/wp/add-data-to-charts-with-copy-paste/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-003/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-003/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-003/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ