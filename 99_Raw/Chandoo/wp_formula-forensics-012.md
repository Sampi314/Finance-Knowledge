# Perform a nested If or Vlookup with a Sumproduct formula.

**Source:** https://chandoo.org/wp/formula-forensics-012

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics 012. – A Neat Formula
=======================================

*   Last updated on February 18, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In early February Sujit asked a question at Chandoo.org, [original post](http://chandoo.org/wp/2011/06/01/switch-scenarios-dynamically-using-slicers/)
.

I require a formula stating criteria \[0%-25% output will be 0, 26%-50% output will be 0.1, 51%-75% output will be 0.2, 76%-100% output will be 0.3 & 100% + output will be 0.4\]

Kyle, responded with a neat Sumproduct formula

\=SUMPRODUCT((B3>{0.25,0.5,0.75,1})\*0.1)

I think it is so neat that it is worthy of sharing and detailing here at Formula Forensics:

So today we will pull Kyle’s answer apart to see what’s inside.

**Kyle’s Formula**
------------------

As usual we will work through this formula using a sample file for you to follow along. [Download Here](http://chandoo.org/img/huis/ff12/kyles_formula.xls)
.

Kyle’s formula is a Sumproduct based formula

\=SUMPRODUCT((B3>{0.25,0.5,0.75,1})\*0.1)

Lets look at cell **C3** as our example.

![Chandoo.org](https://chandoo.org/img/huis/ff12/KF01.png);

In **C3** we see the formula: \=SUMPRODUCT((B3>{0.25,0.5,0.75,1})\*0.1)

Which consists of a Sumproduct function and a formula inside the sumproduct.

We know from [Formula Forensics 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)
 that Sumproduct, Sums the Product of the Arrays, and that when there is only 1 array it simply sums the array elements.

In this case the Sumproduct only has a single array as an element

\=SUMPRODUCT((B3>{0.25,0.5,0.75,1})\*0.1)

and so the (B3>{0.25,0.5,0.75,1})\*0.1 component must return an Array of elements for the Sumproduct to sum.

If we now look at the (B3>{0.25,0.5,0.75,1})\*0.1 component.

We can see that it consists of a comparison B3>{0.25,0.5,0.75,1}

The result of the comparison is Multiplied by 0.1.

Sujit’s orginal question asked: _0%-25% output will be 0, 26%-50% output will be 0.1, 51%-75% output will be 0.2, 76%-100% output will be 0.3 & 100% + output will be 0.4_

And Kyles formula is using B3>{0.25,0.5,0.75,1} to work out which category the value in B3 belongs to.

We can see this if in a blank cell say **C5**: we enter the following:

\= B3>{0.25,0.5,0.75,1} press **F9** not Enter.

Excel will respond with \={TRUE,TRUE,TRUE,FALSE}

This is showing us that the 1st, 2nd and 3rd elements in the formula: B3>{0.25,0.5,0.75,1}, are True

In our example the value in **B3** is 80% which is 0.8 which is Greater than 0.25 and Greater than 0.5 and Greater than 0.75, but Not Greater than 1.0.

The next part of Kyle’s formula is (B3>{0.25,0.5,0.75,1})\*0.1

In a blank cell say **C7**: enter the following:

\= B3>{0.25,0.5,0.75,1}\*0.1 press **F9** not Enter.

Excel will respond with \={0.1,0.1,0.1,0}

This is showing us the result of

\=(B3>{0.25,0.5,0.75,1})\*0.1

\={TRUE,TRUE,TRUE,FALSE} \*0.1

\={0.1,0.1,0.1,0}

Sumproduct now only has to add up the Array

\=Sumproduct({0.1,0.1,0.1,0})

Which it does returning **0.3**.

### **The Neat Part**

The neat part of this is that Kyle has used the 0.1 Multiplier to Force the array to an array of Numbers for Sumproduct to sum.

Had Kyle used:  \=SUMPRODUCT((B3>{0.25,0.5,0.75,1}))\*0.1

Excel would have returned an answer of **0**

This is because as we saw in [Formula Forensics 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)
, Sumproduct doesn’t know what to do with the array of True/False, they need to be converted to numerical equivalents for Sumproduct to operate on.

In a spare cell, say **C9**, enter: \=SUMPRODUCT((B9>{0.25,0.5,0.75,1}))\*0.1

Excel will respond with 0

Of course that can be fixed by using a double degative of a 1\* inside the formula

In a spare cell, say **C10**, enter either:

\=SUMPRODUCT(1\*(B9>{0.25,0.5,0.75,1}))\*0.1

or

\=SUMPRODUCT(- -(B9>{0.25,0.5,0.75,1}))\*0.1

Excel will respond with **0.3** as it should

Except that the formula is longer and now has to do 1 more multiplication.

**Download**
------------

You can download a copy of the above file and follow along, [Download Here](http://chandoo.org/img/huis/ff12/kyles_formula.xls "Download Sample File")
.

**Formula Forensics “The Series”**
----------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series:](http://chandoo.org/wp/tag/formula-forensics/ "Formula Forensics")

**We Need Your Help**
---------------------

I have received a few more ideas since last week and these will feature in coming weeks.

I do need more ideas though and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained but don’t want to write a post also send it to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
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

*   [20 Comments](https://chandoo.org/wp/formula-forensics-012/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-012/#respond)
    
*   Tagged under [Nested If](https://chandoo.org/wp/tag/nested-if/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousUse Text Format to Preserve Leading Zeros in Excel \[Quick Tip\]](https://chandoo.org/wp/use-text-format-to-preserve-leading-zeros/)

[NextFormula Forensics 013. – On VacationNext](https://chandoo.org/wp/formula-forensics-013-on-vacation/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-012/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-012/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-012/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ