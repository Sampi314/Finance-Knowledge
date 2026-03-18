# Highlight Row & Column of Selected Cell using VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Highlight Row & Column of Selected Cell using VBA
=================================================

*   Last updated on July 11, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

When looking at a big table of analysis (or data), **it would make our life simpler if the selected cell’s column and row are highlighted**, so that we can instantly compare and get a sense of things. _Like this:_

![How to Highlight row & column of a selected cell using Excel & VBA](https://img.chandoo.org/vba/highlight-row-column-demo.gif "Highlight row & column of a selected cell using Excel & VBA")

_**Who doesn’t like a little highlighting**_. So lets learn how to do highlighting today.

### Step 1: Identify the area for highlighting

This is simple, unless you are AUI (analyzing under influence). Lets assume that we are dealing with a range of cells in B4:I14

### Step 2: Use 2 cells to capture the selected row & column details

Outside our highlight range, lets set aside 2 cells (E17 & E18 in this case) for keeping the details of which row & column needs to be highlighted.

We can call these cells selRow & selCol.

### Step 3: Unleash the VBA magic

*   Right click on the sheet name & choose ‘view code’.
*   Choose Worksheet & Selection Change from the drop-downs.
*   Excel would add a blank `Worksheet_SelectionChange()` sub
*   Write the below lines of code.
    *   `[selRow] = Target.Row`
    *   `[selCol] = Target.Column`
*   Done. So much simpler than using floo network or transmogrifying muggles.

![VBA code to capture selected cell's row & column ](https://img.chandoo.org/vba/vba-code-to-caputure-selected-cells-row-column.png "VBA code to capture selected cell's row & column ")

### Step 4: Add conditional formatting to highlight selected cell’s row & column

Now that we know which row & column should be highlighted, it is a simple matter of switching on Excel’s highlighting charm – _Conditional Formatting._  
![Conditional formatting rules to highlight row & column of a selected cell](https://img.chandoo.org/vba/conditional-formatting-rule-to-highlight-row.png "Conditional formatting rules to highlight row & column of a selected cell")  
Select the entire range (B4:I14) and go to conditional formatting > new rule

Select the rule type as **_Use a formula_**… and use a below rules.

*   `=ROW(B4) = selRow`
*   Apply formatting
*   _Repeat the steps & this time use the rule_ `=COLUMN(B4) = selCol`

### Step 5: Show off.

**Incorporate this technique in to your dashboard or weekly report.** Watch the socks knocked off your boss’. Bask in the glory. _Repeat and enjoy._

### Bonus Tip: Use similar technique to enhance user inputs

You can use similar idea to conditionally show messages on your worksheets. See this demo.

![Enhance user inputs with message display in Excel - demo](https://img.chandoo.org/vba/enhance-user-inputs-with-message-display.gif "Enhance user inputs with message display in Excel - demo")

I am not telling you how to do this. But I **know** you are awesome enough to figure this out.

### Download Example File

[**Click here to download example file**](https://img.chandoo.org/vba/highlight-row-column-demo.xlsm)
 & understand how to use this technique.

### Do you use highlighting techniques in your reports & analysis?

I always use conditional formatting & light-weight VBA to enhance my dashboards and analysis. Especially conditional formatting is almost a magical way to make stunning reports & show off things that are important.

**What about you?** Do you use these techniques often? what is your experience like? Please share your tips & ideas using comments. I am all ears.

### Transmogrify your boring work to awesome – Check out!

*   [Interactive sales chart using Excel](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
    
*   [Show details on demand using simple VBA](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
    
*   [Highlight points in scatter & line charts](http://chandoo.org/wp?p=2938)
    
*   [Display alert symbols in dashboards to grab attention](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/)
    
*   [Highlight top 10 values using conditional formatting](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
    

Also see [**introduction to conditional formatting**](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
 & [**VBA**](http://chandoo.org/wp/excel-vba/)
 to understand to get the basics right.

For more potent magic, [**please consider joining our Online VBA Classes**](http://chandoo.org/wp/vba-classes/)
.  You are going to leave everyone spellbound.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [70 Comments](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/#respond)
    
*   Tagged under [column()](https://chandoo.org/wp/tag/column/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Highlight](https://chandoo.org/wp/tag/highlight/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousVisualizing Roger Federer’s 7th Wimbledon Win in Excel](https://chandoo.org/wp/visualizing-roger-federers-7th-wimbledon-win-in-excel/)

[NextFormula Forensics 024. Is this number a Prime Number ?Next](https://chandoo.org/wp/formula-forensics-024/)

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
    
    [Reply](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ