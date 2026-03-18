# Advanced Data Validation Techniques in Excel - Switch lists, change lists etc.

**Source:** https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Advanced Data Validation Techniques in Excel \[spreadcheats\]
=============================================================

*   Last updated on August 29, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

[Data validation](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
 is a great way to keep your users informed about possible values in a cell and guide them to select something appropriate. As part of the [spreadcheats](http://chandoo.org/wp/tag/spreadcheats/)
 series, in this post we will discuss 2 advanced data validation techniques that can help you when you are modeling a complex worksheet.

Problem 1: You have 2 lists of possible values and you want a way to switch between both
----------------------------------------------------------------------------------------

_PS: Many thanks to Alex who proposed this idea and solution through e-mail._

You have a cell where user can enter any value from 2 lists. But you don’t want to overload the in-cell drop down list with tons of values, and rather prefer a simpler approach like this:

![data-validation-switch-lists](https://chandoo.org/wp/wp-content/uploads/2008/11/data-validation-switch-lists.gif "data-validation-switch-lists")

Solution: Use an IF() formula in validation criteria
----------------------------------------------------

![validation-criteria-if-formula](https://chandoo.org/wp/wp-content/uploads/2008/11/validation-criteria-if-formula.png "validation-criteria-if-formula")The solution is to use an if() formula to determine which one of the two ranges should be used to validate cell contents.

*   Select the cell where you want to have this type of validation
*   Go to menu > data > validation
*   In the criteria area, select “allow” as “list”
*   In the source area, specify a formula like this: `=IF($B$7="Full List",Full-list-range,Partial-list-range)`

That is all, you now have a data validation list that can change its source based on user preference.

Problem 2 : You would like to change a list’s values based on what is selected in another list
----------------------------------------------------------------------------------------------

![data-validation-change-lists](https://chandoo.org/wp/wp-content/uploads/2008/11/data-validation-change-lists.png "data-validation-change-lists")_PS: Many thanks to Catherine for asking this question through email_

You have a status tracking spreadsheet where each employee enters the status for each of the projects they are working on. They enter the status by first selecting the department and then selecting a project (from that department).

So how do you do this in Excel?

Solution: Use OFFSET and MATCH to determine which range to use
--------------------------------------------------------------

Remember the [offset() and match() formulas](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 we discussed in the last spreadcheats?  Assuming the list of projects for each department is in a range B10:C22 with column B having the department name and column C having the project name and the list is sorted on column B, we can use offset() and match() combination along with [countif](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
 (ahem!) to determine which range to use for project cell drop-down.

*   For the department cell, we can use simple list validation with values as “Marketing, Ops, Sales, IT”
*   For project cell, go to data validation (menu > data > validation) and specify a formula like this:  
    `=OFFSET(C9,MATCH($B$6,$B$10:$B$22,0),0,COUNTIF(B10:B22,$B$6),1`)
*   **What is above formula doing?** It is fetching a sub-range from the by finding where the first entry for the selected department is, returning x number of rows from that point, where x = no. of projects in that department.

That is all. You now have a list drop-down that changes values based on what is selected in an earlier cell.

Still having doubts?
--------------------

**Feel free to download this example workbook** containing a [tutorial on Advanced Data Validation in Excel](https://chandoo.org/wp/wp-content/uploads/2008/11/excel-data-validation-techniques.xls)
 and poke around to learn.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [113 Comments](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/#respond)
    
*   Tagged under [countif()](https://chandoo.org/wp/tag/countif/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [spreadcheats](https://chandoo.org/wp/tag/spreadcheats/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorial](https://chandoo.org/wp/tag/tutorial/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFun way to clean up modern art with visualization](https://chandoo.org/wp/fun-way-to-clean-up-modern-art-with-visualization/)

[NextPrevent users from scrolling away on your dashboards \[dirty little trick\]Next](https://chandoo.org/wp/excel-freeze-pane-tricks/)

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
    
    [Reply](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ