# IFERROR Excel Formula - What is it, syntax, examples and howto

**Source:** https://chandoo.org/wp/iferror-formula

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

IFERROR Excel Formula – What is it, syntax, examples and howto
==============================================================

*   Last updated on March 11, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![IFERROR Excel Formula - What is it, syntax, examples and howto](https://chandoo.org/img/f/cat-fight-stock-pic-s.jpg)**If `IFERROR()` were to be a person, I would hug her so hard that Jo (my wife) would get in to a cat fight with her.** I know many a woman (and man) who get in to a fight with Excel formulas often. But thankfully, we avoid that as IFERROR is not a real person. It is, however a darned useful formula.

Since I cannot hug a formula anymore than I can get my son to sit tight, I will go ahead and sing an ode to her, in my style – by writing about how useful and powerful IFERROR formula is.

What is IFERROR() Formula & How does it work?
---------------------------------------------

Introduced since Excel 2007, IFERROR() formula checks a formula (or expression) and returns the value of formula if there is no error, otherwise a custom formula.

![IFERROR Excel Formula - What is it, syntax, examples and howto - Chandoo.org](https://chandoo.org/img/f/iferror-excel-formula-example-syntax.png)  
For eg:

`=IFERROR(1/0,"Try splitting an atom instead!")`

will give the message Try splitting an atom instead! because the expression 1/0 returns an error (DIV/0 error)

Where as,

`=IFERROR(0/1,"Try splitting an atom instead!")`

will give the value 0 since 0 divided by 1 is 0.

How does IFERROR help me?
-------------------------

_**Archimedes**_ once said, _“Give me enough data and a spreadsheet, I can make any formula return an error.”_

May be he was too confident, but errors are everywhere. And that is why IFERROR is useful. It provides an elegant and simple way to tackle the errors in your workbook.

### Several common uses of IFERROR are,

1.  1\. While writing lookup formulas like VLOOKUP, INDEX+MATCH it is common to search for values that do not exist in your data. You can wrap such formulas in IFERROR for peace of mind.  
    Ex: `=IFERROR(VLOOKUP(...),"Not found")`
2.  2\. While using reference formulas like INDEX, OFFSET, frequently, we try to fetch the data that is not in the list of values. This returns #REF errors. You can fix them with IFERROR easily.  
    Ex: `=IFERROR(INDEX(...),"")`
3.  3\. While using arithmetic, numeric expressions, usually we end up dividing by 0. You can fix such things by using IFERROR.  
    Ex: `=IFERROR(AVERAGE(...),"0")` — Returns 0 when the list has zero values.

Things to keep in mind while IFERRORing:
----------------------------------------

**Please note that IFERROR is oblivious to the type of error.** That means, no matter what the error is (DIV/0, #NAME, #N/A, #REF… etc.), IFERROR treats all of them equally and shows the same value. In other words, IFERROR is like “Catch all” in programming world.

How to handle errors if you are using Excel 2003 or below?
----------------------------------------------------------

In earlier versions of Excel, we have a formula called as ISERROR() that can check an expression or formula for error and return TRUE if so. This formula is not same as IFERROR, but we can use it along with IF() formula to get the same result. For eg.

`=IF(ISERROR(VLOOKUP(...)),"Not found",VLOOKUP(...))`

works same as, `=IFERROR(VLOOKUP(...),"Not found")`

Notice that the ISERROR approach evaluates VLOOKUP formula twice!.

Do you IFERROR?
---------------

**To err is human, to IFERROR is awesome.**

Ever since discovering the IFERROR feature in Excel 2007, I have been using it so often. I use it to keep my output sheets clean and my formulas simple.

_**What about you?**_ Do you use IFERROR? What is your experience like? Would you also give it a hug? If so, would your spouse get in to a cat fight with it? If so can you post some pics of it on [our facebook page](http://facebook.com/chandoo.org)
?

**Please share your experiences and tips on using IFERROR() thru comments.**

### Related awesomeness:

1\. [How to understand and handle Excel formula errors](http://chandoo.org/wp/2009/04/20/excel-formula-errors/)
  
2\. [Excel formulas not working? What to do?](http://chandoo.org/wp/2010/04/12/excel-formulas-are-not-working/)
  
3\. [Handling errors and 5 other tips for writing better VLOOKUP formulas](http://chandoo.org/wp/2010/11/02/excel-vlookup-tips/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [67 Comments](https://chandoo.org/wp/iferror-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/iferror-formula/#respond)
    
*   Tagged under [errors](https://chandoo.org/wp/tag/errors/)
    , [excel 2007](https://chandoo.org/wp/tag/excel-2007/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [iserror()](https://chandoo.org/wp/tag/iserror/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Challenge #1 – Make Nuts without Going Nuts](https://chandoo.org/wp/ec1-machine-scheduling-in-excel/)

[NextConvert ISERROR formulas to IFERROR formulas \[macro\]Next](https://chandoo.org/wp/convert-iserror-formulas-to-iferror-formulas-macro/)

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
    
    [Reply](https://chandoo.org/wp/iferror-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/iferror-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/iferror-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ