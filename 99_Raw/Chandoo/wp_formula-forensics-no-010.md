# How many times does a list of values occurs within a Range

**Source:** https://chandoo.org/wp/formula-forensics-no-010

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics No. 010 Count How Many Times a List of Values Occurs in a Range
=================================================================================

*   Last updated on February 3, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

A few weeks ago Gewilson asked on the **[Chandoo.org Forums](http://chandoo.org/wp/forums/topic/sumif-then-subtract?replies=6#post-16288 "How Can I Simplify my Formula")
, “**_Can I simplify my formula?_ **“**

_\=176 – (SUMIF($B10:$AF10,”PD”,$B11:$AF11) +SUMIF($B10:$AF10,”FA”,$B11:$AF11) +SUMIF($B10:$AF10,”PS”,$B11:$AF11) +SUMIF($B10:$AF10,”PN”,$B11:$AF11) +SUMIF($B10:$AF10,”F1″,$B11:$AF11) +SUMIF($B10:$AF10,”P1″,$B11:$AF11) +SUMIF($B10:$AF10,”F7″,$B11:$AF11))_

SirJB7 responded with a nice Sumproduct solution:

_\=176 – SUMPRODUCT(((B$10:AF$10)=({“PD”;”FA”;”PS”;”PN”;”F1″;”F7″})) \*(B$11:AF$11))_

So Today we will pull this apart to see what inside, I think what we find may surprise you.

SirJB7’s Formula
----------------

_\=176 – SUMPRODUCT(((B$10:AF$10)=({“PD”;”FA”;”PS”;”PN”;”F1″;”F7″})) \*(B$11:AF$11))_

To Simplify things I am going to use a Truncated set of data and adjust the formula accordingly

We will examine:

_\=176 – SUMPRODUCT(((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”})) \*(B$11:I$11))_

This problem has a smaller Range B10:I10 instead of B10:AF10

as well as 2 less possible solutions _{“PD”;”FA”;”PS”;”PN”} instead of {“PD”;”FA”;”PS”;”PN”;”F1″;”F7″}_

The reason for this will soon become evident.

As usual you can download a Sample File to follow along with. [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Sample-File.xls "Download Sample File")
.

### Lets go:

_\=176 – SUMPRODUCT(((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”})) \*(B$11:I$11))_

We can see above that the formula is subtracting the result of a Sumproduct from a Fixed Number 176. So we really only need to focus on the Sumproduct part of the formula.

As we saw In [Formula Forensics 007 – Sumproduct](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "Sumproduct")
, Sumproduct adds up the products of the constituent arrays.

In this case

SUMPRODUCT(((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”;})) \*(B$11:I$11))

Has only 1 constituent array. The array does consist of 2 components

SUMPRODUCT(((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”})) \*(B$11:I$11))

These is a Logic component ((B$10:AF$10)=({“PD”;”FA”;”PS”;”PN”}))

and a Numerical Component (B$11:I$11)

Which are then multiplied together.

Looking at the Logical Component first

((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”}))

The formula is checking the Range B10:I10 against an Array of possible solutions {“PD”;”FA”;”PS”;”PN”}

That is, it is checking each value in our list {“PD”;”FA”;”PS”;”PN”}, against each cell in the range B10:I10.

If we type the above equation\=((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”})) into a spare cell **C14**, and press F9

Excel returns \={FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}

What the …

If we look closely at the above array we will see that it contains a lot of True/Falses separated by ,’s and a few ;’s

\={FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}

Specifically there are 4 blocks of 8 True/Falses separated by ,’s, each block is separated by a ;

In Total 4 x 8 = 32 Values

What this is, is an array representing the multiplication of the 8 cells in the range B10:I10 with each element of the possible solution array

Each row of the Array is separated from the next by a ;

Each element in each row is separated by a ,

This is best displayed like:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Cap1.png "Cap1")](https://chandoo.org/wp/wp-content/uploads/2012/01/Cap1.png)

You can see why I simplified the size of the original problem.

So we have an Array of True/Falses \={FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}

Which is now multiplied by the next component of the Sumproduct

({FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}) \*(B$11:I$11)

In a spare cell, say **C23** enter

\=({FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE;FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE;FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}) \*(B$11:I$11) and press F9

Excel returns

\={0,0,0,0,10,0,0,0;0,10,0,0,0,0,0,0;0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0}

Note that this array has the same 8 column x 4 Row layout as above, except that all the True have been replaced by the values in the Score cells B11:I11

Sumproduct now kicks in and adds these up

\=Sumproduct({0,0,0,0,10,0,0,0;0,10,0,0,0,0,0,0;0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0})

To get 20

Which is subtracted from our original number

\=176 – SUMPRODUCT(((B$10:I$10)=({“PD”;”FA”;”PS”;”PN”})) \*(B$11:I$11))

\= 176 – Sumproduct({0,0,0,0,10,0,0,0;0,10,0,0,0,0,0,0;0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0})

\= 176 – 20

\= 156

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Sample-File.xls "Example File")
.

Other Posts In This Series
--------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series:](http://chandoo.org/wp/tag/formula-forensics/ "Taruns problem")

We Need Your Help
-----------------

I have received a few more ideas since last week and these will feature in coming weeks.

I do need more ideas though and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained but don’t want to write a post also send it in to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
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

*   [21 Comments](https://chandoo.org/wp/formula-forensics-no-010/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-010/#respond)
    
*   Tagged under [Array](https://chandoo.org/wp/tag/array/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousCustom Number Formats (Multiply & Divide by any Power of 10)](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/)

[NextComparing 2 Lists with a TwistNext](https://chandoo.org/wp/comparing-2-lists-with-a-twist/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-010/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-010/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-010/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ