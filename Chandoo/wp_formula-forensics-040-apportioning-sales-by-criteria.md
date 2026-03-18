# Formula Forensics 040 - Apportioning Sales by Criteria » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics 040 – Apportioning Sales by Criteria
======================================================

*   Last updated on February 15, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

A few weeks back in the [Chandoo.org Forum](http://forum.chandoo.org/threads/apportioning-sales-based-on-division-and-status-to-the-current-sales-by-store.27768/#post-166173)
 Melvin asked about Apportioning Sales based on Division and Status to the current sales by store.

Today we will examine how this works and how to develop a solution for the problem.

### **Apportion/ing**

Apportion means to assign or distribute.

In a court the Judge may apportion blame for an accident eg: 50% to the driver, 30% to mechanical failure and 20% to the road conditions, The Judge is assigning or distributing the blame as he deams appropriate.

This is what Melvin wanted to do with his sales. He wanted the sales distributed according to Division and Status based on the current sale by store.

Lets start simple and look at how we can distribute sales on a simple model first.

Let say we have a Distributorship and we buy and sell oranges.

We buy oranges from a supplier and distribute them to 3 stores, Store A, Store B & Store C

We received 1,000 oranges and they were sold as follows

[![FF40f](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40f.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40f.png)

We can see that each store received differing percentages of the original supply:

[![FF40g](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40g.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40g.png)

50% = 500/1000

30% = 300/1000

etc

A week later the supplier give us another 200 oranges and we want to distribute them based on the previous sales

So the new batch of 200 oranges will be distributed according to these previous percentages

[![FF40h](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40h.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40h.png)

100 = 200 x 50%

60 = 200 x 30%

etc

That is as simple and as complicated as apportioning is.

### Melvin’s Problem

When we look at Melvin’s problem he has a more complex set of data

You can follow along using a sample file: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/02/FF-40.xlsx)

[![FF40a](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40a.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40a.png)

We can see that Melvin has 14 stores located in 4 Divisions (N, S, W & C) and each can have a status of Open or Open1

But if we simplify this and look at one set of data we can devise a formula which will adjust to each set of data

Lets develop a formula for cell **F11** which is dealing with **Store 1** in the **N Division** and has a **Status of Open**

We see it has sales of **100** (Cell E11)

Total sales of Division N and status Open are **600** (100+100+100+150+150) highlighted below (Lower table)

Looking at the Upper Table we can see that we need to distribute **200** units based on the **Division N** and **Status Open** (Cell C4)

[![FF40b](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40b.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40b.png)

So we need to distribute **200** units across the 5 stores with Total sales of **600**

We know that Store  1. had sales of 100 in cell E11

The Total Sales of Stores in Division N and Status Open can be obtained using a Sumifs function

\=SUMIFS($E$11:$E$24, C11:$C$24, $C$11, $D$11:$D$24, D11)

\=600

So the proportion of Store 1’s sales 100 to Total Sales ( Division N and Status Open ) 600 is 100/600 = 16.66%

This is calculated by

\=E11/SUMIFS($E$11:$E$24, $C$11:$C$24, C11, $D$11:$D$24, D11)

\=0.1667

\=16.67%

Note: We leave the references to  C11, D11 & E11 variable, so that when the formula is copied down it will refer to the next row

We can use an index/match formula to get the 200 based on the criteria from row 11

\=INDEX($C$4:$D$7, MATCH(D11,$B$4:$B$7,0), MATCH(C11,$C$3:$D$3,0))

What this is doing is doing a 2D Lookup in the Range $C$4:$D$7

It is looking up the Division Row no. MATCH(D11,$B$4:$B$7,0)  

and looking in the Status Column No. MATCH(C11,$C$3:$D$3,0)

Note: Once again we leave the references to  C11 & D11 variable, so that when the formula is copied down it will refer to the next row

So the proportion of the 200 sales attributable to Store 1 is:

\=Distribution Qty \* Actual Sales / Total Sales

\=INDEX($C$4:$D$7, MATCH(D11, $B$4:$B$7, 0), MATCH(C11, $C$3:$D$3, 0)) \* E11 / SUMIFS($E$11:$E$24, $C$11:$C$24, C11, $D$11:$D$24, D11)

\= 33.33

[![FF40c](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40c.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40c.png)

We can now copy this down to all the cells matching our criteria of Division **N** and Status **Open**

[![FF40d](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40d.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40d.png)

Notice that the total matches the total to be distributed **200** showing that the formula is working

Although we copied the formula down to the cells that had matching criteria each part of the formula was setup to work on the appropriate criteria for the store in the current row

If we now copy F11 down to the other stores you will see that in fact all the stores sales have been apportioned according to the correct criteria.

[![FF40e](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40e.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/FF40e.png)

eg: If we look at Stores 7, 8 & 9 we can see that they are in the **W Division** and have a **Status of Open1**

The distributed Proportions are each 16.67, totaling 50, which matches the distribution in the Upper table.

You may also notice that Division C has not been accounted for.

I assume that Melvin has sent us a subset of the data and that is why it is missing.

Download
--------

You can download a copy of the above file and follow along, [Download Sample File.](https://chandoo.org/wp/wp-content/uploads/2016/02/FF-40.xlsx)

A Challenge
-----------

Can you solve the problem another way ?

Post your solutions in the comments below.

**[Other Posts in this Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensuics Homepage")
  
**
---------------------------------------------------------------------------------------------------------------------

The Formula Forensics Series contains a wealth of useful solutions and information specifically about how Normal Formula and specifically Array Formula work.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

If you have a formula and you want to understand how it works contact [Hui](http://chandoo.org/wp/about-hui/)
 and it may be featured in future posts.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousNot so wild lookups](https://chandoo.org/wp/not-so-wild-lookups/)

[NextAnalyzing half a million consumer complaints \[Part 1 of 3\]Next](https://chandoo.org/wp/analyzing-consumer-complaints-1/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ