# Excel Tips Submitted by You [Part 2] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-by-you-2

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Tips Submitted by You \[Part 2\]
======================================

*   Last updated on May 11, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is [Your Week @ PHD](http://chandoo.org/wp/2009/05/08/your-week-your-tips/)
. You get to see all the [excel tips](http://chandoo.org/wp/category/excel/)
 shared by PHD readers like you. I am very excited about this. Today I rushed home from work and opened the google docs to see the tips submitted by you, and found several new and fun things. You can be part of this excitement too: [just click here to share your tips with us](http://spreadsheets.google.com/viewform?formkey=cjJSRkdlY25CdjJmZjlUUjRGdEoyQXc6MA..)
.

Here is the [part 1 of the series](http://chandoo.org/wp/2009/05/11/excel-tips-by-you-1/)
.

**The first and foremost chart construction tip** _by [**Jon Peltier**](http://peltiertech.com/WordPress/)
_

> Before you take any steps towards constructing a chart, get the data right. This will save time and effort, reduce frustration, and amaze your boss, clients, and that cute young thing in accounting. Well, your boss and clients anyway.
> 
> Consider it as a set of data extracted from a database: each row is a record, each column is a field, the first row is the field names.
> 
> First row of the data range: series names as column headers.  
> First column of the data range: category labels or X values.  
> Intersection of first row and first column: overcome your natural tendency for order and uniformity, and leave this cell blank.  
> _Data is Series in columns._

**A Flurry of Keyboard Shortcuts and Productivity Hacks** _by **Barbara**_

> **I use several shortcuts**
> 
> *   F12 for ‘Save As’
> *   F2 for ‘Edit’
> *   F4 to switch between absolute and relative formula references, whilst in edit mode.
> *   Control & 1 (using the number keys not the number pad) for ‘format cells’
> 
> **If you want to copy part of a spreadsheet to a powerpoint:**  
> Highlight the area, hold shift, click edit in the menu, copy picture, choose ‘as shown on screen’ or ‘as shown when printed’.  Paste into the powerpoint slide.
> 
> **If you put the insert rows, insert columns & group icons in you toolbar you can use them for the opposite function as well.** Press & hold the shift key, then click on one of the tools, it will do the opposite.  This not only saves space in your toolbar, but I find it useful as I can not easily tell the difference between the insert & delete or group & ungroup icons.

**Several ways to search text using formulas** _by **Vishy**_

> [Download these examples](http://chandoo.org/img/n/Advanced_Lookup.zip)
>  and play with them.  
> **Lookup into Substring**
> 
> Let’s say you want to find Age in Column D by referring to Part of First Name in cell G3 as below  
> First Names are in B3:B7  
> Ages are in D3:D7  
> Part of First Name Reference in G3  
> { =INDEX($D$3:$D$7,MATCH(TRUE,FIND(G3,$B$3:$B$7)>0,0)) } Must be entered as an array (Ctrl + Shift + Enter)  
> 
> **Use SEARCH instead of FIND for case-insensitive lookup**  
> You can also use regular expressions – [Download the examples](http://chandoo.org/img/n/Advanced_Lookup.zip)
>   
> \* refers to any number of characters, including null (i.e. no character)  
> ? refers to exactly one character, not null  
> 
> **Multiple Criteria Lookup**  
> Let’s say you want to find Age in Column D by referring to First Name in cell G4 and Last Name in H4 as below  
> First Names are in B3:B7  
> Last Names are in C3:C7  
> Ages are in D3:D7  
> First Name Reference in G4  
> Last Name Reference in H4  
> { =INDEX($D$3:$D$7,MATCH(1,($B$3:$B$7=G4)\*($C$3:$C$7=H4),0)) } Must be entered as an array (Ctrl + Shift + Enter)

### Some Resources to help you understand these tips:

[Introduction to Excel Array Formulas](http://chandoo.org/wp/2009/03/25/using-array-formulas-example1/)

[INDEX Excel Formula – Learn by Example](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
 (Used to construct a dynamic chart)

[MATCH Excel Formula – Tutorial & Examples](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)

[Absolute and Relative Formula References – A Beginner Guide](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)

**Jon, Barbara and Vishy, You are truly amazing human beings. We at PHD love you for these wonderful tips.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/excel-tips-by-you-2/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-by-you-2/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [find](https://chandoo.org/wp/tag/find/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [productivity](https://chandoo.org/wp/tag/productivity/)
    , [search](https://chandoo.org/wp/tag/search/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousA Good Chart is a Story \[Charting Principles\]](https://chandoo.org/wp/charts-are-stories/)

[NextExcel Tips Submitted by You \[Part 3\]Next](https://chandoo.org/wp/excel-tips-by-you-3/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-2/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-by-you-2/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-2/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ