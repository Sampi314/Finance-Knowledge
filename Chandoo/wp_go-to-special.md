# Go to Special - Detailed Tutorial on how to use this Excel feature

**Source:** https://chandoo.org/wp/go-to-special

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

What is so special about Go To Special? \[15 tips\]
===================================================

*   Last updated on March 12, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This article is written by _**Myles Arnott**_ from [Excel Audit](http://www.excelaudit.co.uk/)

I briefly covered Excel’s Go To Special function in the [Managing Spreadsheet Risk](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/ "Introduction to Spreadsheet Risk Management")
 series of articles and both Chandoo and I felt that it deserved a post all of its own.

What is Go To Special?
----------------------

Go To Special is a tool within Microsoft Excel that enables you to quickly select cells of a specified type within your Excel worksheet. Once you get to grips with this function and what it can be used for you will wonder how you ever lived without it.

Where do I find Go To Special?
------------------------------

**Shortcut:** F5 or CTRL + G and then click on Special…  
**2003:** Edit > Go To  
**2007 & 2010:**Home > Find & Select > Go To Special on the Ribbon

(Note: a cut down selection of the most useful options in Go To Special can be selected directly under Find & Select on the Ribbon in 2007 & 2010.)

Lets look at Go To Special in action
------------------------------------

[**Firstly download this workbook**](https://img.chandoo.org/g/GoTo%20Special%20Example.xlsm)
. This is more or less the same workbook that we used in the Managing Spreadsheet Risk series, modified slightly to allow us to cover all elements of the Go To Special function. (Note that it therefore includes a lot of errors)

Here are the options on the Go To Special dialogue box:

![Excel Go to Special - What is it and how to use it?](https://img.chandoo.org/g/excel-goto-special.png "Excel Go to Special - What is it and how to use it?")

Lets run through each of the Go to special options.

### Comments

**Action:** Selects all cells with comments

**Benefit:** A quick way of finding all cells with comments, particularly useful if you want to clear all comments from your worksheet

### Constants

**Action:** Selects all cells containing constants

**Options:**

**Numbers**: Selects all cells with constants that are numbers

**Text**: Selects all cells with constants that are text

**Logicals:** Selects all cells with constants that are logicals (TRUE or FALSE)

**Benefit:** The number constants in your spreadsheet should all be inputs. Highlighting all constants is a great way of checking the structure of your spreadsheet. I normally format inputs with a white background and blue font.

_A great tool for auditing – select all constants and change the fill colour. This instantly gives you visibility of your model inputs and flags any inconsistencies._

### Formulas

**Action:** Selects all cells containing formulas

**Options:**

**Numbers**:Selects all cells with formulas that return numbers

**Text:** Selects all cells with formulas that return text

**Logicals:** Selects all cells with formulas that return logicals (TRUE or FALSE)

**Benefit:** Highlighting all of the formulas within your spreadsheet is a great way of checking the structure and consistency of your spreadsheet.

### Blanks

**Action:** Selects all blank cells

**Benefit:** A quick way to select all blank cells. This is useful if you want to quickly format all blank cells or as a way of identifying cells that look blank but actually contain a constant or formula (i.e. with white on white formatting).

(Related: [Fill Blank Cells](http://chandoo.org/wp/2011/10/17/fill-blank-cells-in-a-table/)
 )

### Current region

**Action:** Selects the current region

**Comment:** I would recommend using the shortcut CTRL + \* instead

### Current array

**Action:** Selects the entire array if the active cell is within an array

**Comment:** I have never used this option but would be very interested to hear if anyone has.

### Objects

**Action:** Selects all objects (shapes, images, charts etc)

**Benefit:** A simple way to select all objects. This could be useful if you wanted to quickly delete all objects in the worksheet.

### Row differences

**Action:**

**Single row**: Selects the cells that are different from the active cell within the selected row

**Multiple rows**: The comparison is made for each row independently. The cell used for comparison for each row is the cell in the same column as the active cell.

**Benefit:** This is a very useful auditing tool for highlighting inconsistent formulas in a row.

It also offers a quick and easy way to [spot differences across multiple rows](http://chandoo.org/wp/2011/02/14/compare-data-row-differences/)
.

(Note: You can change the active cell within a selected row by pressing enter)

### Column differences

**Action:**

**Single column**: Selects the cells that are different from the active cell within the selected column

**Multiple columns**: The comparison is made for each column independently. The cell used for comparison for each column is the cell in the same row as the active cell.

**Benefit:** This is a very useful auditing tool for highlighting inconsistent formulas in a column. It also offers a quick and easy way to spot differences across multiple columns.

### Precedents

**Action:** Selects the cells that feed into the selected cell(s)

**Options:**

**Direct only:** First level precedent only

**All levels:** All levels of cell precedents

**Benefit:** Provides an alternative to Trace Precedents in the formula auditing bar. Personally I prefer using this tool to select and then colour-fill the precedent cells as it allows you to select the precedents for a range of cells rather than just one. I also find that the arrows in Trace Precedents can get a little messy.

### Dependents

**Action:** Selects the cells that the selected cell(s) feed into

**Options:**

**Direct only:** First level dependents only

**All levels:** All levels of cell dependents

**Benefit:** As above this provides an alternative to Trace Dependents in the formula auditing bar.

### Last cell

**Action:** Selects the last used cell within your worksheet (containing data or formatting)

**Benefit:** A quick way to locate your last cell. This is a very effective way of identifying the range of cells used of the worksheet.

If your simple spreadsheet suddenly becomes very large in MB terms this can be due to Excel incorrectly thinking that you are using a lot more of the cells than you actually are . A good indicator of this is that the right hand scroll bar slider becomes very small. Using Go To Special Last cell lets you quickly identify the last cell Excel thinks you are using.

### Visible cells only

**Action:** Selects cells that are not hidden (& therefore are visible)

**Benefit:** Useful if you only want to change the non-hidden cells and leave the hidden cells unchanged

### Conditional formats

**Action:** Selects all of the cells with conditional formatting applied

**Options:**

**All:** Selects all cells with conditional formatting applied

**Same:** Selects all cells that have the same conditional formatting as is applied to the active cell

**Benefit:** An easy way to quickly identify all of the cells with conditional formatting applied to them. A useful tool for understanding the formatting applied to a spreadsheet.

You need to be aware that, depending on the conditional formatting set, you may not be able to highlight the cells using a fill colour as the conditional formatting may override it.

**Comment:** The manage rules option within the conditional formatting menu also enables you to identify cells with conditional formatting applied.

### Data validation

**Action:** Selects all of the cells with data validation applied

**Options:**

**All:** Selects all cells with data validation applied

**Same:** Selects all cells that have the same data validation as is applied to the active cell

**Benefit:** An easy way to quickly identify all of the cells with data validation applied to them. This is particularly useful from an auditing perspective or if you want to clear the validations in these cells.

Some considerations for Go To Special
-------------------------------------

*   Go To Special only selects cells in the current worksheet rather than the whole workbook.
*   Go To Special searches within the selected range, if you want to select the entire worksheet ensure that only one cell is selected

Putting this in to practice
---------------------------

In order to give you some examples of how to use the Go To Special tools covered above I have put together a list of actions for you to run over the attached spreadsheet. Have a play and see what you discover:

(note that the action “Select cell A1” is simply to clear the current range selected. Failing to do this will restrict the new search to the currently selected range)

### 1) Look for cells containing data validation and conditional formatting

Select cell A1, Go To Special, Data validation (All)

Select cell A1, Go To Special, Conditional formatting (All)

### 2) Check the structure of the spreadsheet

Select cell A1, Go To Special, Constants ,text, fill the selection in brown

Select cell A1, Go To Special, Constants ,numbers, fill the selection in blue

Select cell A1, Go To Special, Constants ,errors, fill the selection in purple

Select cell A1, Go To Special, Formulas (leave all options ticked), fill the selection in green

Select cell A1, Go To Special, Formulas, errors, fill the selection in red

(Note: any cells with conditional formatting will not be changed by the fill colours above)

I have recorded the above steps into a macro to give you a useful audit macro that could be adapted for future use. Click on the button on the Info tab to run the macro.

See these pages for information on macros.

*   [Introduction to Macros & VBA](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
*   [Excel VBA section on Chandoo.org](http://chandoo.org/wp/excel-vba/)
    

### 3) Check the range C9:S9 for any inconsistent formulas

Select the range C9:S9, Go To Special, Row differences, fill the selection in yellow

### 4) Review the precedents for the formulas in row 25

Select the range C25:S25, Go To Special, Trace Precedents, Direct only

### 5) See if there are any charts in the spreadsheet

Select cell A1, Go To Special, Objects

### 6) Find the last cell

Select cell A1, Go To Special, Last cell

Added by Chandoo:
-----------------

### Do you use Go to Special?

I use go to special (both dialog box and keyboard shortcuts) all the time. It is a really easy way to navigate a complex workbook and quickly select what you want. My favorite uses of Go to special are, selecting blank cells, finding data validations, locking formula cells, formatting input cells (constants). To find conditional formatting I usually go to home > conditional formatting > manage rules and see all the formatting rules in current worksheet. For formula auditing I rely on audit toolbar & manual inspection of the workbook.

**What about you?** Have you used Go to Special? What are your favorite features? _**Please share using comments.**_

### Thanks to Myles

Many thanks to Myles for compiling all the tips & sharing this with us. If you have enjoyed this article, please say thanks to Myles. You can also reach him at [Excel Audit](http://www.excelaudit.co.uk/)
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

*   [30 Comments](https://chandoo.org/wp/go-to-special/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/go-to-special/#respond)
    
*   Tagged under [blank rows](https://chandoo.org/wp/tag/blank-rows/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [goto special](https://chandoo.org/wp/tag/goto-special/)
    , [guest](https://chandoo.org/wp/tag/guest/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [spreadsheet audit](https://chandoo.org/wp/tag/spreadsheet-audit/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousFormula Forensic No. 015 – Cornelia’s Price Rises](https://chandoo.org/wp/formula-forensic-no-015/)

[NextData and Calculations for our Customer Service Dashboard \[Part 2 of 4\]Next](https://chandoo.org/wp/calculations-for-customer-service-dashboard/)

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
    
    [Reply](https://chandoo.org/wp/go-to-special/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/go-to-special/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/go-to-special/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ