# Excel's Spreadsheet Auditing Functions & How to use them?

**Source:** https://chandoo.org/wp/excel-auditing-functions

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel’s Auditing Functions \[Spreadsheet Risk Management – Part 3 of 4\]
========================================================================

*   Last updated on April 24, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This series of articles will give you an overview of how to manage spreadsheet risk. These articles are written by _**Myles Arnott**_ from [Excel Audit](http://www.excelaudit.co.uk/)

*   Part 1: [An Introduction to managing spreadsheet risk](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    
*   Part 2: [How companies can manage their spreadsheet risk](http://chandoo.org/wp/2012/01/03/how-companies-can-manage-spreadsheet-risk/)
    
*   **Part 3: Excel’s auditing functions**
*   Part 4: [Using external software packages to manage your spreadsheet risk](http://chandoo.org/wp/2012/02/08/spreadsheet-risk-management-software-review/)
    

![Introduction to Spreadsheet Risk Management](https://chandoo.org/img/g/spreadsheet-risk-management.png)

In the first two articles in this series we highlighted the risks that poorly managed spreadsheet solutions can introduce to a business and outlined the steps companies can take to manage this risk. This article works through the application of some of Excel’s built in auditing functions:

*   Error checking (Background and stepping through each error)
*   Trace Error
*   Circular Reference
*   Go To Special

Let’s have a look at an example spreadsheet that is riddled with issues.

[**Download Example file first**](https://img.chandoo.org/g/excel-risk-management/Managing%20Spreadsheet%20Risk%20Illustration.xlsm)
.

The spreadsheet contains four tabs: a simple front page; an Example tab with the report that we wish to audit; a Resolved tab with the corrected report; and a Notes tab which details all of the issues contained within the spreadsheet (if you print the Resolved tab, all of the comments will also be printed for your reference).

_If you are up for a challenge you could download the file and work through the report in the Example tab to see how many of the errors you can find yourself._

First off let’s identify the obvious issues
-------------------------------------------

### Circular reference

On opening the file you are presented with this warning message:

![Circular Reference Warning - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/01-circular-reference-warning.png "Circular Reference Warning - Excel's Auditing Functions")

Click OK to continue opening the file. Here is how the report looks:

![Excel Report Snapshot Risk Management - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/02-excel-report-snapshot-risk-management.png "Excel Report Snapshot Risk Management - Excel's Auditing Functions")

Excel helpfully gives you the location of the first circular reference (Q30) in the bottom left corner of the screen:

![Circular Reference Status - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/03-circular-reference-status.png "Circular Reference Status - Excel's Auditing Functions")

An alternative approach to locating circular references is to select Error Checking > Circular References on the Formulas tab of the Ribbon:

![Highlight Circular Refs - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/04-highlight-circular-refs.png "Highlight Circular Refs - Excel's Auditing Functions")

By clicking into the formula on cell Q30 you will see that the formula is `=AVERAGE(M30:N30,P30:Q30)`. This average formula is including the cell Q30, hence the circular reference.

\[Related: [Understanding & Using Excel Circular References](http://chandoo.org/wp/2010/09/16/excel-circular-references/)\
\]

### #REF error

The next obvious issue is that cells I13, J13, J33, S13, S18 & S33 contain the #REF error. The #REF error is a warning that the formula contains an invalid cell reference (this usually happens when the user deletes a cell/row/column/worksheet that is being referenced by a formula).

To trace the cell originating this error select any cell containing the error (I chose S33 as this would appear to be the main report total), and select Error Checking > Trace Error on the Formulas tab of the Ribbon:

![Trace Formula Errors - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/05-trace-formula-errors.png "Trace Formula Errors - Excel's Auditing Functions")

This highlights that cell I13 is the source of the error:

![Formula Error Arrows - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/06-formula-error-arrows.png "Formula Error Arrows - Excel's Auditing Functions")

Cell I13 contains the formula =3109+#REF!. To remove the error simply remove the +#REF! within the formula.

It is also however important to try to understand what cell was referenced by the formula originally. The best way to do this would be to talk to the user/previous user (if they are still there) and look back through archived versions of the report (if they exist).

Now that the obvious issues have been identified we are now going to employ some of Excel’s other auditing tools to see if there are any hidden errors.

\[Related: [**Understanding & fixing Excel Formula Errors**](http://chandoo.org/wp/2009/04/20/excel-formula-errors/)\
\]

Excel’s error checking function
-------------------------------

I’m sure that you will have noticed the small green triangles in the top left hand corner of some of the cells. This is Excel’s background error checking function warning you that these cells break one of the predetermined rules.

![Excel Error Checking Example - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/07-excel-error-checking-example.png "Excel Error Checking Example - Excel's Auditing Functions")

Firstly let’s have a look at the errors that are being checked for. To open the Error Checking options select File > Options> Formulas (2010) or Office button> Excel options>Formulas (2007).

Below is the default set up:

![Formula Editing Options Excel - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/08-formula-editing-options-excel.png "Formula Editing Options Excel - Excel's Auditing Functions")

When reviewing a spreadsheet for errors it is always worth a quick check to ensure that the above is set up as you would like it to be. I always also tick the “Formulas referring to empty cells” rule.

Click OK to return to the spreadsheet.

The most systematic way to walk through all of the issues identified by the error checking function is to run Error Checking on the Formulas tab of the Ribbon:

![Error Checking From Ribbon - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/09-error-checking-from-ribbon.png "Error Checking From Ribbon - Excel's Auditing Functions")

This launches the Error checking dialogue box and allows you to review each error in turn:

![Error Checking Example - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/10-error-checking-example.png "Error Checking Example - Excel's Auditing Functions")

I will leave you to run through the errors one by one to see what Excel picks up.

Please note that this is not a fool proof check as it is simply checking against the predefined rules. This function will not highlight cells that comply with the rules but contain other errors. It can also highlight cells as an error when they are not (eg P13, in this case click on “Ignore Error”). A very useful starting point nonetheless.

Reviewing the report structure
------------------------------

A crucial step to ensuring that a spreadsheet is error free is to understand its structure, and then to ensure that this structure is correct and consistent.

The simplest way to do this is to identify the different types of cells and their relative positions within the worksheet. For this simple example we are looking to identify:

*   Input cells (Numbers)
*   Input cells (Text)
*   Formula cells
*   Formula cells returning an error

To achieve this quickly and simply I have built a basic macro which is within the spreadsheet and can be run from the “RUN” button in the Example tab.

This colors each cell type as follows:

![Cell Style Types - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/11-cell-style-types.png "Cell Style Types - Excel's Auditing Functions")

This very quickly identifies some structural issues in the spreadsheet:

![Using Cell Styles To Highlight Issues - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/12-using-cell-styles-to-highlight-issues.png "Using Cell Styles To Highlight Issues - Excel's Auditing Functions")

### So how does this work?

The macro above uses Excel’s Go To Special function which helps you to quickly select cells of different types.

To launch Go To Special, click on Find and Select> Go To Special on the Home tab of the Ribbon:

![Goto Special Formula Debugging - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/13-goto-special-formula-debugging.png "Goto Special Formula Debugging - Excel's Auditing Functions")

(Alternatively press F5 or Ctrl + G to launch the Go To dialogue box and then click on Special…)

![Goto Special Highlighting Numbers - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/14-goto-special-highlighting-numbers.png "Goto Special Highlighting Numbers - Excel's Auditing Functions")

For example, selecting Constants and leaving just Numbers ticked will highlight all numbers on the current worksheet:

![Goto Special Highlighted Cells With Number Formulas - Excel's Auditing Functions](https://img.chandoo.org/g/excel-risk-management/15-goto-special-highlighted-cells-with-number-formulas.png "Goto Special Highlighted Cells With Number Formulas - Excel's Auditing Functions")

It is worth playing with the options on Go To Special as there are some great functions that I sadly don’t have time to cover here (the precedents, Dependents and Row/Column differences functions are particularly useful).

\[Related: [**More uses of Go To Special in Excel**](http://chandoo.org/wp/tag/goto-special/)\
\]

And Finally…
------------

As valuable as these initial tests are there are still some issues in the spreadsheet that only a detailed investigation will highlight.

So I’ll leave you to grab a coffee and see if you can find them (they are covered in the Notes and in the Resolved tab).

In the final article of the series we will have a quick look at an example of spreadsheet auditing software.

Also, we are planning to write an article explaining [other useful features of Go To Special dialog](http://chandoo.org/wp/2012/03/12/go-to-special/)
.

### What about you?

Do you use Spreadsheet auditing functions? What is your experience with them? What are your favorite features? _**Please share using comments.**_

### Thank you Myles

Many thanks to _Myles_ for writing this series. Your experience in this area is invaluable. If you enjoy this series, drop a note of thanks to Myles thru comments. You can also reach him at [Excel Audit](http://www.excelaudit.co.uk/)
 or [his linkedin profile](http://uk.linkedin.com/in/clarityconsultancyservicesma)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/excel-auditing-functions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-auditing-functions/#respond)
    
*   Tagged under [\# REF error](https://chandoo.org/wp/tag/ref-error/)
    , [circular references](https://chandoo.org/wp/tag/circular-references/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [errors](https://chandoo.org/wp/tag/errors/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [goto special](https://chandoo.org/wp/tag/goto-special/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [spreadsheet audit](https://chandoo.org/wp/tag/spreadsheet-audit/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFormula Forensics. 009 – Pradhishnair’s Chainage Problem](https://chandoo.org/wp/formula-forensics-no-009-2/)

[NextFormula Forensics No. 008 – Elkhan’s MaxIfNext](https://chandoo.org/wp/formula-forensics-no-008/)

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
    
    [Reply](https://chandoo.org/wp/excel-auditing-functions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-auditing-functions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-auditing-functions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ