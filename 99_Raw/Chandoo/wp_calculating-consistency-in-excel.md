# Who is the most consistent seller? [BYOD] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculating-consistency-in-excel

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Who is the most consistent seller? \[BYOD\]
===========================================

*   Last updated on February 18, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week, I asked my email newsletter readers to submit “one data analysis problem you are struggling with”. We called it BYOD – Bring your own data. More than 100 people have emailed various interesting (and often very difficult) problems. This week (between 16th of February to 20th of February), let’s take a look at some of these problems and solve them.

_This problem is sent by Robot Mak._ 

### Who is the most consistent of all?

Imagine you are a category manager at a large e-commerce company. Your site offers various products, but you don’t really make these products. You list products made by other vendors on your site. Every day, these vendors would send you invoices for the amount of product they have sold. Here is a snapshot of such invoices.

![who-is-the-most-consistent-seller-data](https://chandoo.org/wp/wp-content/uploads/2015/02/who-is-the-most-consistent-seller-data.png)

Looking at this list, you have a few questions.

1.  Who is the best seller?
2.  Who is the most active seller?
3.  Who is the most consistent seller?
4.  Which seller has fewest invoices?

Let’s go ahead and answer these using Excel. Shall we?

### But first, what is consistency?

Consistency is the kind of word that means different things to different people. So when we analyze a set of data to find _most consistent item_, the first thing we need is a _consistent_ definition of consistency.

Let’s look it up in the dictionary.

> **con·sis·ten·cy:** Reliability or uniformity of successive results or events

The keyword is uniformity. So in our case, we can say a seller is consistent, if they are sending invoices fairly regularly.

We have 11 days of data in the data-set.

We can calculate **consistency %** for a seller using this:

\=number of days on which invoice is sent / 11

**So who would be _most_ consistent?**

Let’s say 2 sellers have sent invoices on each of those 11 days. Then who is _most_ consistent? Both of them have consistency = 100%.

May be we can calculate _weighted consistency %?_

**Weighted consistency?!?**

Since for this e-commerce business, the most important factor is revenues (well, it should be profits, but we don’t have that data here), we can calculate weighted consistency by adding a fraction that depends on the value of total invoice amount.

Something like this:

\=consistency % + (0.000001)\*rank of seller based on invoice amount in ascending order

_note: if your data has more than 1000 sellers, multiply with a smaller number like 0.00000001_

**Alternative ways to figure out weights:**

Instead of revenue rank, we can use below alternatives too:

*   Standard deviation of invoice amounts per day
*   Standard deviation of number of invoices per day
*   Rank of total invoice count in ascending order

### Option 1. Using Pivot Tables

The easiest way to answer all the questions is to [use Pivot Tables](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
. Just follow below steps:

1.  Insert a pivot table from the invoice data.
2.  Then add “Date” to row label area
3.  Add “Seller” to column label area
4.  Add “value” to values area
5.  Just looking at the below report, we can answer questions 1 & 4

![calculating-most-consistent-seller-using-pivot-table](https://chandoo.org/wp/wp-content/uploads/2015/02/calculating-most-consistent-seller-using-pivot-table.png)

6.  To answer question 3 (most consistent seller), we have to see which sellers have invoices against maximum number of dates. Both SELLER2 & SELLER6 qualify. Since SELLER6 has higher amount, we can say she is most consistent (based on our definition of _most consistent_ above)
7.  To answer question 2 (most active seller), replace “value” with “reference” in pivot table and find out the seller with maximum count

### Option 2. Using formulas

While the pivot table approach works, it is ad-hoc. That means, we can’t extract the names of sellers automatically. We can use Excel formulas to answer all these questions elegantly.

Let’s assume all the data is in a table named _**sales**_

In your workbook, calculate all of these:

![calculations-for-most-consistent-seller-explained](https://chandoo.org/wp/wp-content/uploads/2015/02/calculations-for-most-consistent-seller-explained.png)

Now we just need a few doses of [INDEX+MATCH formulas](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/ "How to Lookup Values to Left?")
 to answer the questions.

\[Related: [How to count unique values in a range?](http://chandoo.org/wp/2009/08/06/count-number-of-unique-cells/)\
 | [Using SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/ "What is Excel SUMPRODUCT formula and how to use it?")\
\]

**Who is the best seller?**

\=INDEX($H$12:$H$20,MATCH(MAX($I$12:$I$20),$I$12:$I$20,0))

Note: Column H has the seller names & I has the seller amounts

**Who is the most active seller?**

\=INDEX($H$12:$H$20,MATCH(MAX(J12:J20),J12:J20,0))

_Note: Column J has invoice count_

**Who is the most consistent seller?**

\=INDEX($H$12:$H$20,MATCH(MAX(M12:M20),M12:M20,0))

_Note: Column M has weighted consistency %_

**Who is the seller with fewest invoices?**

\=INDEX($H$12:$H$20,MATCH(MIN(J12:J20),J12:J20,0))

### Download Example Workbook

**[Click here to download example workbook with all these calculations](https://chandoo.org/wp/wp-content/uploads/2015/02/consistent-seller-byod.xlsx)
**. Examine the formulas & pivot table to learn more.

### How do you measure consistency?

I will be honest. This is the first time I calculated consistency. But I find it interesting. Consistency can be used to understand your data better & make informed decisions. Few common situations where it can really help,

*   Identifying consistent customers to reward them
*   Finding consistent assembly line in a set of them
*   Optimizing re-ordering pattern of inventories based on how consistently orders are placed

**What about you?** Do you measure consistency of your data? What techniques do you use? _**Please share your techniques & tips in the comments section**_.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/calculating-consistency-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/calculating-consistency-in-excel/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [byod](https://chandoo.org/wp/tag/byod/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [unique](https://chandoo.org/wp/tag/unique/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousRevenue vs. Commission growth – Getting the message across \[BYOD\]](https://chandoo.org/wp/revenue-vs-commission-growth-getting-the-message-across-byod/)

[NextCP030: Detecting fraud in data using Excel – 5 techniques for youNext](https://chandoo.org/wp/cp030-detecting-fraud-in-data-using-excel-5-techniques-for-you/)

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
    
    [Reply](https://chandoo.org/wp/calculating-consistency-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/calculating-consistency-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/calculating-consistency-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ