# Excel Tips Submitted by You [Part 3] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-by-you-3

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Tips Submitted by You \[Part 3\]
======================================

*   Last updated on May 12, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is the 3rd day of [Your week @ PHD](http://chandoo.org/wp/2009/05/08/your-week-your-tips/)
 and we have already posted some excellent array formulas, productivity hacks and other very useful tips. Just one more day is remaining, so if you want to share something with all of us, go ahead and [submit your tips for your week](http://spreadsheets.google.com/viewform?formkey=cjJSRkdlY25CdjJmZjlUUjRGdEoyQXc6MA..)
.

**Must read: [part 1 of excel tips shared by readers](http://chandoo.org/wp/2009/05/11/excel-tips-by-you-1/)
 | [part 2](http://chandoo.org/wp/2009/05/12/excel-tips-by-you-2/ "Part 2 - Excel Tips submitted by readers")
**

**Display file path in Excel using Web Toolbar** _by **Ang Kean**_

* * *

Excel by default not display the open workbook full path name.

Tips : add the web toolbar item  
1\. Right click at the toolbar area, choose “Customize…”  
2\. Browse “Categories:” to “Web” and “Commands:” to “Address”  
3\. Drag the “Address” Commands to toolbar area by holding left mouse key.

* * *

**Making VLOOKUP ranges dynamic** _by **Thuy**_

* * *

I use VLOOKUP a lot in my work and while it was great to use, I wanted a bit more ability to check my formula without having to click on every cell to do so.

Now, I use both the INDIRECT, MATCH, and named ranges in my VLOOKUP to help check the accuracy of my references quickly.

In this example, to get my scores for each region for q3\_12, my old VLOOKUP formula would be a simple:

\=VLOOKUP(W$29,’Data’!$A$1:$AZ$200,6,FALSE)

To

\=VLOOKUP(W$26,INDIRECT(“‘”&$Q29&”‘!a1:az200”),MATCH($R29,INDIRECT($S29),0),FALSE

I actually put the data range in a column Q29 on my spreadsheet and indicate the named Range of in the column.  In this case, my reference named range is “Data”.

For the column count, before using match, I would count manually but whenever there was a data change (as in, columns would get moved around), I would need to change the column manually.  It would get very confusing considering I use over 500 lookup formulas in my workbooks and not very accurate.

I use the MATCH function to help me locate the column that I needed the LOOKUP to look under.  First, I would name the row of my data reference sheet to something like DataCol:  =Data!$1:$1.

Then in my vlookup formula worksheet, I would put in column R29, put the heading of the column I was looking for in Column Q29, in this case it would be “q3\_12”.   In column S, I would indicate the named range of where to look for the match.  In this case it is “DataCol.”  
![Vlookup tweak - data format](https://chandoo.org/img/n/vlookup-tweak-data-format.png)

* * *

**R1C1 still makes sense** _by **Vishy**_

* * *

**What is R1C1 reference style**

_Instead of using letters for columns and numbers for rows (i.e. A1 reference style), R1C1 style enables using numbers for both rows and columns._

**Why should you know this**

*   You are working on a machine with such setting, so instead of getting flummoxed, you better understand it (or at least learn to revert to A1 style referencing)
*   Easy to construct “Indirect” addresses, “offset” references etc. (used in conjunction with Row, Column, Address, Rows, Columns functions)
*   Easy to write macro loops (since dealing with numbers instead of single/double letters)
*   The two styles are equivalent in power, but R1C1 style has an advantage when it comes to formula editing (eg. find/replace functionality)

**How to setup**

*   XL 2003 : Tools > Options > General > Settings > R1C1 reference style
*   XL 2007 : Office > Excel Options > Formulas > Working with formulas > R1C1 reference style

**How to use**

*   RxCy : absolute reference to xth row and yth column (any of x / y could be missing which then means “current”)
*   R2C10 refers to 2nd row 5th column (equivalent to E2 in A1 style)
*   RC5 refers to current row 5th column
*   R\[x\]C\[y\] : relative reference w.r.t. current cell to xth row down (up if x is -ve) and yth column right (left if y is -ve)
*   R\[2\]C\[-10\] refers to 2nd row down and 10th column left of current row
*   RxC\[y\] : mixing of absolute/relative reference

**Where should one not use this**

_While working on the sheet, relative reference may be far apart from current cell. If there is large number of such references, avoid R1C1 style._

_**Interesting Trivia (added by PHD)**_

_my twitter handle is [r1c1](http://twitter.com/r1c1)
, so are my reddit, digg and older blog’s handle_

* * *

### More resources to help you understand these tips better:

[Vlookup excel formula in plain English](http://chandoo.org/excel-formulas/vlookup.html)

[Vlookup tutorial](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)

**Thank you so much Ang Kean, Thuy and Vishy. You are \*really\* outstanding individuals.**

PS: We have only one more day people, so go ahead and [share your tips](http://spreadsheets.google.com/viewform?formkey=cjJSRkdlY25CdjJmZjlUUjRGdEoyQXc6MA..)
. Go!

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/excel-tips-by-you-3/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-by-you-3/#respond)
    
*   Tagged under [howtos](https://chandoo.org/wp/tag/howtos/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [r1c1 style formula references](https://chandoo.org/wp/tag/r1c1-style-formula-references/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [your week](https://chandoo.org/wp/tag/your-week/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Tips Submitted by You \[Part 2\]](https://chandoo.org/wp/excel-tips-by-you-2/)

[NextExcel Tips Submitted by You \[Part 4\]Next](https://chandoo.org/wp/excel-tips-by-you-4/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-3/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-by-you-3/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-3/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ