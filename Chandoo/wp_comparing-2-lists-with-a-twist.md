# Comparing 2 Lists with a Twist » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/comparing-2-lists-with-a-twist

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Comparing 2 Lists with a Twist
==============================

*   Last updated on February 6, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**We love to compare.**_ The instinct to compare leaves no one. Even my two year old twins compare their toys with each other (and fight).

It would make Excel hugely popular if Microsoft builds a handy data comparison tool right in to it. Alas, they have _customizable ribbon, 3d effects & equation editor…_

Since comparison is one of the main uses of Excel, we have written extensively about it here.

\[Read: [Compare 2 lists quickly](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)\
, [Compare 2 lists – detailed tutorial](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/)\
\]

But there is always one more interesting comparison problem. Today, I want to share one such problem, based on a comment left by [N-Man](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/#comment-219337)
.

The Problem – Compare 2 lists with another 2 lists
--------------------------------------------------

> I have to do a comparison between to sets of staff lists, where name that are highlighting in the first list who do not appear in the second list have left the firm, and people highlighting in the second list who do not appear in the first are new arrivals.
> 
> To further muddy the issue, when I say ‘list’, what I actually have is one column for 1st names and another for surnames in both instances.

Assuming N-Man managed the cast of Harry Potter movies, may be he was talking about something like this:

![Comparing first name, last name with a list in Excel](https://img.chandoo.org/cf/comparing-2-lists-in-excel-with-a-twist.png)

The Solution – SUMPRODUCT, Conditional Formatting & Coffee
----------------------------------------------------------

Lets bring our most important ingredient for this problem first – coffee.

Once you pour yourself a strong cup of this, the solution for our problem should become apparent.

1.  The first step is to give names to all the four lists. While this is not mandatory, it simplifies our solution and reduces our blood pressure.
2.  So lets call them list1, list 2, list 3 & list4.
3.  Now, we need to highlight all items in list1 & list2, whenever they do not appear in list3 & list4. (and _vice-versa_)
4.  This is where [SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
     comes in to picture.
    1.  Assuming the lists are in columns B,C, E,F and starting from row 6,
    2.  \=SUMPRODUCT(–(list3&list4=$B6&$C6))=0 will be TRUE if the fist item _Minister Rufus Scrimgeour_ does not appear in second set of lists.
    3.  As you can see, we are exploiting the power of SUMPRODUCT to concatenate both lists (list3, list4) dynamically and check in that for the name in B6&C6.
    4.  So the portion (list3&list4=$B6&$C6) gives us a bunch of TRUE, FALSE values based on the comparison of B6&C6 with in list3&list4.
    5.  The double negative sign — is used to convert a set of logical (boolean) results to numbers (1s and 0s) as SUMPRODUCT is meant to work with numbers, not boolean values.
    6.  Then, we see if the result is 0 (SUMPRODUCT(–(list3&list4=$B6&$C6))=0), to see if there were no matches. _Had there been at least one match, the SUMPRODUCT would return a positive number._

### But wait, We need to highlight

Since we want to highlight the missing items in each list, we need to [use Conditional Formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
 and feed this SUMPRODUCT formula to it.

So, select the first 2 lists (list1, list2), go to Conditional Formatting > Add rule.

Select the rule type as **_use a formula to determine which cells to format_**

Now, type the formula **\=SUMPRODUCT(–(list3&list4=$B6&$C6))=0**

![Conditional Formatting rule to compare firstname, last name with another list](https://chandoo.org/img/cf/conditional-formatting-rule-compare-lists.png)

And set the formatting to whatever you want.

Click OK and we are done!

_Apply the same formatting rules for List3 & List 4, but this time the rule becomes_ **\=SUMPRODUCT(–(list1&list2=$E6&$F6))=0**

That is all.

Download Example Workbook
-------------------------

[**Click here to download the example workbook**](https://img.chandoo.org/d/comparison%20with%20twist.xlsx)
 to understand this technique better. Examine the CF rules to learn more.

How would you compare?
----------------------

The problem posed by N-Man mimics many real world comparison problems. You want to compare 2 lists, but subject to some condition. For example you want to see which customer product combinations are new in a particular month (compared to previous month, say). While we can use helper columns & then write simple [COUNTIF formula](http://chandoo.org/excel-formulas/countif.html)
 to do the same, using SUMPRODUCT allows us to extend this model in many more ways.

**What about you?** Do you face similar comparison problems at work? How do you solve them? **Please share your techniques and ideas using comments.**

Learn More ways to Compare
--------------------------

If your work involves fair bit of comparison & related data analysis, check out these articles to learn more.

*   [Compare 2 lists quickly using Conditional Formatting](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)
    
*   [Compare 2 lists – detailed tutorial](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/)
    
*   [Compare 2 lists – a special scenario](http://chandoo.org/wp/2011/10/27/compare-2-lists-visually-and-highlight-matches/)
    
*   [Learn how to use Excel Conditional Formatting for comparison and more](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
*   [Introduction to Excel SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   More on [comparison](http://chandoo.org/wp/tag/comparison/)
    , [SUMPRODUCT](http://chandoo.org/wp/tag/sumproduct/)
     & [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    

Want to Learn More Formulas? Join Our Crash Course
--------------------------------------------------

If you want to learn SUMPRODUCT and 40 other day to day formulas, and how to use them in situations like this, then consider my Excel Formula Crash Course. It has 31 lessons split in to 6 modules and makes you awesome in Excel formulas.

[![Excel Formula Crash Course from Chandoo.org](https://cache2.chandoo.org/content/cc/excel-formula-crash-course-join-today-v1.png)](http://chandoo.org/wp/training-programs/formula-crash-course?utm_source=chandoo.org&utm_medium=fp)

Now, if you excuse me, I have a comparison problem to solve. My daughter is comparing her hello kitty toy with my son’s scooter and now they are fighting!

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/comparing-2-lists-with-a-twist/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/comparing-2-lists-with-a-twist/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [comparison](https://chandoo.org/wp/tag/comparison/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFormula Forensics No. 010 Count How Many Times a List of Values Occurs in a Range](https://chandoo.org/wp/formula-forensics-no-010/)

[NextUsing external software packages to manage your spreadsheet risk \[Part 4 of 4\]Next](https://chandoo.org/wp/spreadsheet-risk-management-software-review/)

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
    
    [Reply](https://chandoo.org/wp/comparing-2-lists-with-a-twist/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/comparing-2-lists-with-a-twist/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/comparing-2-lists-with-a-twist/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ