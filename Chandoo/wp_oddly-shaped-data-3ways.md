# Rescue oddly shaped data - Battle between Formulas, VBA and Power Query » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/oddly-shaped-data-3ways

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Rescue oddly shaped data – Battle between Formulas, VBA and Power Query
=======================================================================

*   Last updated on April 11, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is inspired from a forum question by Chanthan [about messy data](https://chandoo.org/forum/threads/gather-all-messy-data-into-one-column.38071/)
._

Let’s say you have data like this in a spreadsheet. Don’t roll your eyes, I am 102% sure, right at this moment, someone is (ab)using Excel to create similar messy data.

![](https://chandoo.org/wp/wp-content/uploads/2018/04/oddly-shaped-data.png)

_**How do you reshape it to one column?**_

You could use formulas, VBA or Power Query. Let’s examine all these methods to see what is best. All these methods assume your data is in a range aptly named _**myrange**._

### Oddly shaped data vs. Formulas

ln response to Chantan’s question, Narayan, our forum ninja posted this beautiful, complex and almost cryptic formula.

    =IFERROR(INDIRECT("R" & SUBSTITUTE(TEXT(SMALL(IF(myrange <> "", ROW(myrange) + COLUMN(myrange)*0.00001), 
                 ROWS(A$1:A1)), "00000.00000"), ".", "C"), FALSE), "")

It is a bit too much to explain. But I will give it a go:

*   We want to find out the address of the cells that have some value in them.
*   Start by finding the row & column numbers of cells that are not empty – myrange<>””
*   Add these two to generate a decimal number in the format row.column\*0.00001
*   Reformat this in 00000.00000 format using TEXT
*   Replace decimal point with C and prefix R, so you get R00000C00000, _a la_ R1C1 notation
*   Use INDIRECT to get the corresponding cell value.
*   boom.

**My verdict:** Works beautifully, but you need serious Excel skills to either write it or change it. Also, volatile as it uses INDIRECT.

### Oddly shaped data vs. VBA Macros

VBA is so easy for things like this. You can just iterate thru myrange and copy non-blank values. Here is a simple VBA macro to do that. It will paste output from a cell named _**paste.here**_.

    
    Sub extract()
        Dim cell As Range, i As Long
        
        For Each cell In Range("myrange").SpecialCells(xlCellTypeConstants)
            Range("paste.here").Offset(i).Value = cell.Value
            i = i + 1
        Next cell
    End Sub
    

**My verdict:** Works like a charm. You just need entry level VBA skills to understand and use this. But requires re-running when data changes and permissions.

### Oddly shaped data vs. Power Query

Power Query is designed to mitigate pains like this. You just have to load the data to PQ and give it a good scrubbing to get shiny extract in a single row.

1.  Load myrange to Power Query (use Data > From Table or Power Query > From Range)
2.  Select all columns, right click and choose Merge Columns with separator as _**comma** (or any other symbol not present in your data)_
3.  Right click on the newly created column and split it by _**comma**_  in to _**rows**_.  
    ![](https://chandoo.org/wp/wp-content/uploads/2018/04/power-query-split-column.png)
4.  Filter away _null_ values
5.  Close and load the data.

**My verdict:** If you have Power Query (or Excel 2016) and not using it to slap some sense in to shapeless data, then you are punishing yourself. Power Query is for things like this people. So use it with abandon.

### Download oddly shaped data – done three ways

[**Click here to download the oddly shaped data workbook**](https://chandoo.org/wp/wp-content/uploads/2018/04/oddly-shaped-data-3ways.xlsm)
. Play with the formulas, VBA and PQ to learn each better.

### Improve your career odds – learn Excel

If you had enough of being the odd person out due to your pear shaped Excel skills, then its time you got in shape. Start with these free resources.

*   [Introduction to Power Query](https://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
    
*   [Introduction to VBA](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
*   [Introduction to Excel Basics](https://chandoo.org/wp/excel-basics)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    

### What is your verdict?

What do you think about these three techniques? Which one is better according to you? Please share your thoughts in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [30 Comments](https://chandoo.org/wp/oddly-shaped-data-3ways/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/oddly-shaped-data-3ways/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [text()](https://chandoo.org/wp/tag/text/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousMaths worksheets for your kids – teach addition, subtraction & multiplication with these](https://chandoo.org/wp/maths-worksheets-for-your-kids-teach-addition-subtraction-multiplication-with-these/)

[NextVisualizing Commonwealth games performance – Interactive chartNext](https://chandoo.org/wp/visualizing-commonwealth-games-data/)

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
    
    [Reply](https://chandoo.org/wp/oddly-shaped-data-3ways/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/oddly-shaped-data-3ways/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/oddly-shaped-data-3ways/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ