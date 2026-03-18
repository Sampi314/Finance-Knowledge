# 10 Excel Formula Myths - Busted! » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-formula-myths

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

10 Excel Formula Myths – Busted!
================================

*   Last updated on June 7, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![10 Excel Formula Myths - Busted](https://chandoo.org/img/f/10-formula-myths-busted.png)**Many of us start using Excel to keep track of something**. And along way, we realize that Excel has a powerful feature called formulas, using which we can automate a lot of things. BOOM! Before we realize, we are in the thick of VLOOKUPs and SUMIFs.

But, along way, we also pick up a few bad habits or believe a few myths. **Today, lets bust 10 Excel formula myths that we hear often.**

1\. Shorter Formulas are Better
-------------------------------

I think it is human tendency to shorten and optimize things. We take great pride if we can shrink a task that takes 10 minutes to 12 seconds. But is it the case with Excel Formulas?

**In my opinion, any formula that does the job is better**. It does not matter how short or long the formula is. Often, we can come up with a reasonable formula in few minutes, but we waste several hours trying to shorten it. Time that could be used for better things like impressing your boss or shipping a product.

2\. IF Formulas are Bad
-----------------------

I dont know where this comes from, but I hear it often. Oh, why use IF formula, as if it is going to slow down the computer drastically. Well, for most cases, we are dealing with reasonably sized data and Excel is fast enough to calculate formulas whether they are IFs or REPTs or something else.

So go ahead and [use IF formula](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)
, if that is what you need to use.

3\. VLOOKUP is slower
---------------------

Ok, here is another one. For some reason people believe that VLOOKUP is slower than alternatives like INDEX+MATCH, OFFSET+MATCH, MATCH, Array formulas. Well, in my private tests, I found mixed results. VLOOKUP performance is almost same as that of other alternatives for small and medium (10000 rows) sized data sets.

Of course, if you have a workbook with million rows, then you should spend time looking for the fastest formula. Otherwise, just [use VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/ "What is VLOOKUP Formula & How to use it? [VLOOKUP WEEK]")
 and be done.

4\. Helper Cells, Helper Columns are Lame
-----------------------------------------

Again, another myth that has no reason to exist. Each Excel sheet has 17179869184 cells and there is no reason why we should not use a few to support us in our formulas or models. Use helper cells, they keep your worksheet simple and easy to understand.

5\. Formulas should start with = sign only
------------------------------------------

Do you know that you can start a formula with + or – sign too?

Well, you can type -SUM(1,2,3) to get -6 in a cell.  
Similarly, you can type +SUM(1,2,3) to get 6 in a cell.

PS: You can also begin a formula with @ sign. I am not sure if there are more…  
PPS: You can put ‘ before the formula if you just want to show the formula instead of running it. So if you write ‘=SUM(1,2,3), Excel would show =SUM(1,2,3) in a cell (instead of 6)

6\. Formulas cannot refer to other Excel Workbooks
--------------------------------------------------

Well, that is not correct. You can refer to data in other workbooks in an Excel formula. For eg.

\=SUM(sales.xlsx!q1Sales,2000,$H$2:$H$13)

will sum up the named range q1Sales in Sales.xlsx workbook, the value 2000 and the cells H2:H13

Remember, if your workbook is closed, you need to put the full path, like this:

\=SUM(‘C:\\full\\folder\\path\\sales.xlsx’!q1Sales,2000,$H$2:$H$13)

PS: Certain formulas do not work with closed workbooks.

7\. Formulas should be written in a cells only
----------------------------------------------

Well, this is wrong. You can use formulas in named ranges, conditional formatting, data validation. You can also assign formulas to drawing shapes, chart elements (like titles, labels etc.).

See these examples:

[5 ways to use formulas in Conditional Formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
  
Custom Data Validation with Excel Formulas: [Example 1](http://chandoo.org/wp/2010/05/04/either-or-data-validation/ "Either Or Data Validation in Excel")
, [Example 2](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/ "Advanced Data Validation Techniques - Excel")
, _**[More](http://chandoo.org/wp/tag/data-validation/)
**_  
[Make your charts smarter with Formulas](http://chandoo.org/wp/2010/04/08/smart-chart-legends/)

8\. We cannot copy a formula without changing references
--------------------------------------------------------

Of course you can. If you want to have the same formula as in the cell above, just press CTRL+’  
You will get the same formula and you can modify it as you want.

If you want to have the same formula elsewhere, just go to the formula cell, press F2, select everything (SHIFT+HOME), copy (CTRL+C).

Now go to the target cell and press F2 and paste (CTRL+V)

9\. Formulas cannot do ‘x’…
---------------------------

May be they cannot feed your cat or take your dog for walk or change a nappy. But there is a formula for almost everything. And Excel team at Microsoft is adding new formulas in each version. It wont be long before a =ChangeNappy(kidname, _<optional dispose nappy>_) appears. Well, may be.

But the best part is, you can create your own formulas, called as User Defined Functions. And once you start doing that, there is no limit to the possibilities. You can create a [CONCAT() to add up a bunch of text values](http://chandoo.org/wp/2008/05/28/how-to-add-a-range-of-cells-in-excel-concat/)
, a [NETWORKINGDAYS() to calculate working days based on a custom weekend setup](http://chandoo.org/wp/2009/06/09/networkingdays/ "Networkingdays() an improved version of networkdays formula")
 or anything. \[[More UDF Examples](http://chandoo.org/wp/tag/udf/)\
\]

10\. Formulas are difficult to learn
------------------------------------

_**Only if you think so.**_

Excel formulas are very powerful and very easy to learn. You need to start slow and go one step at a time. It might take a while to wrap your head around the [referencing styles](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/ "Relative vs. Absolute References in Formulas [spreadcheats]")
 and [various formulas](http://chandoo.org/excel-formulas/)
.

But once you learn a few simple formulas, rest of them will be easy to learn. And before you realize, you are in the thick of VLOOKUPs and SUMIFs.

_**Oh, wait, I said that already.**_ But then who says we cannot repeat. That is another myth!

What myths you hear about Excel Formulas?
-----------------------------------------

Thanks to all your emails, comments and forum discussions. I hear about a lot of myths and bad habits all the time, when it comes to Excel. I found that giving in to these myths limits our ability to do more.

**What about you?** What myths you have heard when you started learning Excel? **Please share using comments.**

Learn More About Excel & Excel Formulas
---------------------------------------

If you just started using Excel, then you are at the right place. Go thru below links to learn more.

1\. [Excel Tutorials for Beginners](http://chandoo.org/wp/excel-tutorial/)
 – 10 videos to start your Excel Journey  
2\. [Excel Formula e-book](http://chandoo.org/wp/excel-formula-helper-e-book/)
 – 75 Excel Formulas, explained in plain English  
3\. [Excel Formulas](http://chandoo.org/wp/tag/formulas/)
 – Examples & Demos – More than a 100 examples on Excel formulas  
4\. [Excel School](http://chandoo.org/wp/excel-school/)
 – Online Excel Training Program by Chandoo. With 23 hours of video lessons and downloadable excel files, you will master every aspect of Excel, very soon.

**PS: [Join our news letter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
.** You will get emails with Excel tips, tricks, tutorials and more, 3 times a week.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/excel-formula-myths/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formula-myths/#respond)
    
*   Tagged under [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousDo you want to attend an Excel Workshop in Singapore? \[Survey\]](https://chandoo.org/wp/singapore-workshop-survey/)

[NextHow to create a Win-Loss Chart in Excel? \[Tutorial & Template\]Next](https://chandoo.org/wp/win-loss-chart/)

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
    
    [Reply](https://chandoo.org/wp/excel-formula-myths/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formula-myths/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formula-myths/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ