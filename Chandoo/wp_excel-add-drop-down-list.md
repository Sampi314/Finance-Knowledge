# Excel Basics: How to add drop down list to a cell to validate data

**Source:** https://chandoo.org/wp/excel-add-drop-down-list

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Basics: How to add drop down list to validate data
========================================================

*   Last updated on September 28, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Excel Dropdown lists - demo](https://chandoo.org/wp/wp-content/uploads/2019/09/excel-drop-down-lists-demo.gif)

Validating your data as you type can prevent any surprises when you are doing analysis / follow-up on the data. Thankfully, excel has the right tools to do it. **Excel drop down list can assist you in picking up a value** from a valid list to enter in a cell. Here is a short how-to guide to get you started on data validation in excel.

Howto set up Drop Down list in Excel?
-------------------------------------

1.  First, set up a list of valid values in range of cells. Say your valid list of entries is in A1:A6.
2.  Now go the cell where you want to validation drop down to appear.
3.  Go to Data ribbon and click on Validation
4.  Set up “List” as allowed values and enter =A1:A6 as Source (see below picture)
5.  Done. Now you can see the drop-down in your cell.

![Excel Data Validation - Drop-down settings](https://chandoo.org/wp/wp-content/uploads/2019/09/data-validation-drop-down-settings.png)

Data Validation Settings

Video – How to create Drop Down List in Excel & Best Practice Tips
------------------------------------------------------------------

I made a video with a real world example of drop down lists. Please watch it below to understand the set up process & how to customize the validation rules.

Sample workbook to Practice Data Validation Drop Downs
------------------------------------------------------

**[Click here to download the sample workbook](https://chandoo.org/wp/wp-content/uploads/2021/09/excel-basics-drop-down-lists.xlsx)
** to practice data validation drop down lists.

How-to ignore duplicates while setting up validation list?
----------------------------------------------------------

If you want to use a source list that has duplicates and want to ignore them when setting up validation drop-down, then you have two options. Something like this:

![drop-down in Excel without duplicates](https://chandoo.org/wp/wp-content/uploads/2019/09/drop-down-without-duplicates.png)

Data Validation drop-down without duplicates

1.  Use Excel Dynamic Arrays (works in Excel 365)
2.  Use Pivot Tables (works in all versions of Excel)

Let’s say your list of inputs is in customers\[Education\] column.

### Using Dynamic Arrays

_Note: This works only in Excel 365 with dynamic array feature. Not all 365 users will have access to DA now, but everyone of them will get Dynamic Arrays soon._

Just go to an empty cell (preferably in a separate worksheet like settings tab) and type **=SORT(UNIQUE(customers\[Education\]))**

**Excel will spill your data down** to next few cells depending on how many unique values are in your data.

Let’s say your formula is in cell A1

Now, go to Formulas > Define Name and create a name for validation options as,

![Dynamic array approach to get drop-down list without duplicates](https://chandoo.org/wp/wp-content/uploads/2019/09/dynamic-array-name-dropdown-without-duplicates.png)

Use # to tell Excel you want the entire spill range for the name

**Finally, use myOptions as list source for data validation.**

### Using Pivot Tables for drop down without duplicates

This is most compatible option as it works in all versions of Excel.

1.  In a new sheet or blank range, insert a pivot table from your data.
2.  Add the Education field to row labels area
3.  Remove any grand, sub-totals
4.  Let’s say the first item in the pivot is in cell A2.

![Pivot table method for creating data validation dropdown without duplicates](https://chandoo.org/wp/wp-content/uploads/2019/09/using-pivot-tables-for-data-validation-without-duplicates-v1.png)

Pivot table with list of education values

Now, create a name with myOptions and use the formula

\=OFFSET($A$2,0,0, COUNTA($A$2:$A$21), 1)

this will make a _dynamic named range_ with how many ever education options are there in that pivot table.

_Note: Change $A$21 to a cell address_ further down if you will have more options.

Finally, use myOptions as the list source for data validation.

Your drop-down list without duplicates will be ready.

Drop-down list without duplicates – Video
-----------------------------------------

I made a video explaining how to make dropdowns without duplicate values. You can see a cameo from Nishanth (my son) in the video. Check it out if you want to understand how Dynamic Array method and Pivot Table method can be setup. Watch it below or [visit my YouTube Channel](https://youtu.be/4Rv5twNqrGM)
.

Best Practice for Drop-downs
----------------------------

Drop-downs are very useful for data analysis, charting and reporting work. They are user friendly and easy to set up. That said, keep these ideas in mind when implementing them.

*   **Use named ranges:** Instead of hard-coding cell addresses, use named ranges for setting up validation lists. This will also enable you to connect data validation list to table columns thru structural references.
*   **Source lists in a separate tab**: Whenever possible, set up all your source lists in a separate tab. I call mine “Settings”. This will make any changes easy for you.
*   **Don’t have too many options:** If your drop-down is having more than 50 options, consider [two-level cascading drop-downs](https://chandoo.org/wp/cascading-drop-down/)
     or some other way to gather inputs.
*   **Try Form controls or Slicers too:** Drop-downs are great, but they are just one of the many ways to add _interactive abilities_ to your workbooks. Consider [form controls](https://chandoo.org/wp/form-controls/)
     and [Slicers](https://chandoo.org/wp/introduction-to-slicers/)
     too.

Download Practice Workbook
--------------------------

I made a workbook with simple and “avoiding duplicates” examples. **[Please download it here](https://chandoo.org/wp/wp-content/uploads/2019/09/data-validation-without-duplicates.xlsx)
** and practice to learn more about these techniques.

More Data Validation Tricks
---------------------------

Here is a collection of useful tricks and ideas with Data Validation. Check them out to learn more.

*   [Using OFFSET or Table Refs to set up dynamic validation lists](https://chandoo.org/wp/dynamic-data-validation-excel/)
    
*   [Switch between short & long lists with IF formula in validation list](https://chandoo.org/wp/advanced-data-validation-techniques-in-excel-spreadcheats/)
    
*   [Use dropdown list to make a dynamic chart](https://chandoo.org/wp/interactive-charts-tutorial/)
    
*   [Make AWESOME Data Entry form with validation rules – Case Study](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [43 Comments](https://chandoo.org/wp/excel-add-drop-down-list/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-add-drop-down-list/#respond)
    
*   Tagged under [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic arrays](https://chandoo.org/wp/tag/dynamic-arrays/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [how to](https://chandoo.org/wp/tag/how-to/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sort](https://chandoo.org/wp/tag/sort/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [technology](https://chandoo.org/wp/tag/technology/)
    , [unique](https://chandoo.org/wp/tag/unique/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousZelda Stamina Wheel Chart](https://chandoo.org/wp/zelda-stamina-wheel-chart/)

[NextImpress with Tornado Charts in ExcelNext](https://chandoo.org/wp/excel-tornado-chart/)

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
    
    [Reply](https://chandoo.org/wp/excel-add-drop-down-list/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-add-drop-down-list/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-add-drop-down-list/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ