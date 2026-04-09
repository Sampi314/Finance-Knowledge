# A clever technique to simplify your long, nested IF formulas » Excel Tricks

**Source:** https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas

---

*   [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

A clever technique to simplify your long, nested IF formulas
============================================================

*   Last updated on April 10, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently I optimized a pretty long nested IF formula using a simple but elegant trick. I made it _**80% shorter!**_ In this article, let me explain the process and share the formulas.

![A technique to make long Excel formulas shorter](https://chandoo.org/wp/wp-content/uploads/2023/04/SNAG-2576.png)

The Situation: Discount Calculation
-----------------------------------

Imagine you have to calculate the appropriate discount using below rules.

![Example Discount Rules - for nested IF formula](https://chandoo.org/wp/wp-content/uploads/2023/04/SNAG-2578.png)

Picture 1: Rules for Discount Calculation

And you have transaction data like below:

![sample data - nested if formula](https://chandoo.org/wp/wp-content/uploads/2023/04/SNAG-2579.png)

_**How would we write the formula in column H?**_

Option 1: Long, Nested IFs
--------------------------

We can calculate the discount by writing a complex, lengthy and nested IF formula.

Here is one such formula:

				
					`=LET(cat, XLOOKUP(F5,products[Name], products[Category]),         IFS(OR(D5="India", D5="USA",D5="UK"),             IFS(AND(G5>=200, G5<=999),                  IF(OR(cat="Bars", cat="bites"),                         IF(E5="New",Rules!$F$7, Rules!$F$8),                     0),                 AND(G5>=1000, G5<=1999),                      IFS(cat="Bars",                              IF(E5="New",Rules!$F$11, Rules!$F$12),                          cat="Bites", Rules!$F$14,TRUE, 0),                 G5>=2000,                      IF(E5="New", Rules!$F$16,                         IFS(                             cat="Bars",Rules!$F$17,                              cat="Bites", Rules!$F$18,                              TRUE, 0)                     )                 )             )         )`
				
			

### What this formula is doing?

1.  We start by calculating the “category” of the product using XLOOKUP and storing it in the variable _cat_
2.  Then we check the rules (refer to picture 1 above)
3.  Once we reach the lowest level of the rule, we get the matching discount from the rules worksheet cells.
4.  If no discount applies, we return 0

What is wrong with this formula?
--------------------------------

### Long and error prone

Such formulas are too long to write correctly and errors are not easy to catch.

### Not easy to update

When the business rules change, the formulas become hard to edit.

### Hard to maintain

The formulas become a nightmare to maintain and document.

Option 2: A smart alternative
-----------------------------

What if we can rewrite the rules so that we can write shorter formulas?

**I suggest rewriting such business rules as a table like this:**

![Discount rules - rewritten as a table](https://chandoo.org/wp/wp-content/uploads/2023/04/SNAG-2580.png)

Once you have such a table, we can then rewrite our formula using SUMIFS & wildcard characters. Like below:

				
					`=LET(cat, "*"&XLOOKUP(F5,products[Name],products[Category])&"*",         SUMIFS( discount[Discount],                 discount[Country],"*"&D5&"*",                 discount[Category],cat, discount[Customer Type],"*"&E5&"*",                 discount[Quantity from],"<="&G5,                 discount[Quantity to],">="&G5))`
				
			

### How does this formula work?

1.  We start by calculating the “category” of the product using XLOOKUP, pad this with \* and store it in the variable _cat_
2.  Then we use SUMIFS to add up \[Discount\] column by 
    1.  Checking the country (in D5) against \[Country\] column of discount table
    2.  _cat_ against \[Category\] column
    3.  Customer type (E5) with \[customer type\] column
    4.  Quantity (G5) with the to & from ranges
3.  If there are no discounts then the SUMIFS would be 0
4.  Else it would tell us what the discount is.

Advantages of the SUMIFS approach
---------------------------------

### Easy to write & test

The formula is easier to write and test. Hence fewer errors.

### Easy to maintain & update

Whenever the business rules change or new products are added, updating the discount table is all you need to do.

### Scalable

Even when you have 100s of rules, this table approach is easy to scale and won't increase the formula size.

### Use FILTER to work with text

If you need to get a non-numeric value as the output, we can use FILTER() instead of SUMIFS.

Video Tutorial - Honey, I shrunk the formulas
---------------------------------------------

I made a video about this concept. See it below or [click here to watch it on my YouTube channel](https://youtu.be/HCEIzeIdiD0)
.

Try it yourself - Here is a sample file
---------------------------------------

Want to have a play with the data and see which formula is easier to write?

**[Click here to download the sample file](https://chandoo.org/wp/wp-content/uploads/2023/04/if-mess.xlsx)
.**

Your thoughts on this approach?
-------------------------------

What do you think about this approach? Leave a comment. 

Also, do check out below pages for more on other ways to make advanced Excel formulas.

*   [Introduction to SUMIFS](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
    
*   [Introduction + examples on XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
    
*   [Use LAMBDA to create new functions](https://chandoo.org/wp/what-is-lambda-function/)
    
*   [New Dynamic Array functions in Excel](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [Excel Formula Forensics](https://chandoo.org/wp/formula-forensics-homepage/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [ifs](https://chandoo.org/wp/tag/ifs/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Nested If](https://chandoo.org/wp/tag/nested-if/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousCreate a beautiful, elegant & interactive to-do list with Excel (FREE Template + Tutorial)](https://chandoo.org/wp/beautiful-to-do-list-excel-template/)

[NextSpeed up your Excel Formulas \[10 Practical Tips\]Next](https://chandoo.org/wp/optimize-speedup-excel-formulas/)

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
    
    [Reply](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/a-clever-technique-to-simplify-your-long-nested-if-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ