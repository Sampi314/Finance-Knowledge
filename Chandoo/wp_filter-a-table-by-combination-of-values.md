# Quickly filter a table by combination of selected cell values using VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/filter-a-table-by-combination-of-values

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Quickly filter a table by combination of selected cell values using VBA
=======================================================================

*   Last updated on July 15, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Filtering is one of the most used feature in Excel.** It is a quick way to take lots of data and narrow down to the subset we want.

Naturally, there are many powerful ways to work with filters. To name a few,

*   Using CTRL+Shift+L shortcut to quickly turn on / off the filters
*   [Right clicking on a cell value and choosing filter > filter by selected cell’s value](http://chandoo.org/wp/2010/12/22/filter-by-selected-value/)
    
*   [Using advanced filters to set up complex filtering conditions](http://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
    

_**But here is one common filtering scenario that is slow as snail**_.

_Imagine you are looking at some sort of sales data (if you can’t imagine, look at the below demo)._

Now, you want to filter this list for a combination like, gender=male, profession=self-employed, product category = chocolates and  quantity = 1.

If you use the right click, filter > filter by selected value approach, this will take several clicks.

Wouldn’t it be cool if you can select the entire combination and say filter?

Unfortunately, no such feature exists in Excel.

But you are not aiming to be _ordinary_ in Excel.  You are aiming to be **_awesome_** in Excel. That means, you don’t take no for answer.

Fortunately, we can quickly write a [VBA](http://chandoo.org/wp/excel-vba/)
 macro that filters a list by selection. So let’s do that. Here is what you will learn to create:

![filter-by-selected-cell-combination-macro-demo](https://chandoo.org/wp/wp-content/uploads/2015/07/filter-by-selected-cell-combination-macro-demo.gif)

Filtering a table by selected combination of values using VBA
-------------------------------------------------------------

### What we need to achieve?

Our goal is simple. User (that is you) selects a range of cells depicting the conditions for filtering. Something like this.

After selection, we fire up the filtering macro and instantly our list is filtered.

We can select a single-range or multiple cells (using CTRL+select technique)

Just to keep things simple, let’s assume the **data is always in a table.**

### Algorithm / Steps for the VBA macro

Whenever you attempt to write VBA code, it is a good idea to start by writing down the steps in plain English. This is called as algorithm. By writing down the steps, we force our mind to think clearly about the problem at hand and come up with best possible solution.

Here are the steps for filtering the table by selected combination

1.  Make sure user has selected some values in a table
2.  Check if more than one row is selected. If so, exit as we don’t want to filter based OR conditions, we just want to filter based on AND conditions.
3.  For each cell in the selection
    1.  Find out the corresponding column number
    2.  Apply filtering on the table for corresponding column number with the cell’s value
4.  Repeat for next cell
5.  Done

### VBA code – Filtering based on selected combination

Here is the VBA code for filtering based on selected combination. First examine the code. Then, we will understand key segments of it.

  

    
    Sub combinationFilter()
        Dim cell As Range, tableObj As ListObject, subSelection As Range
        Dim filterCriteria() As String, filterFields() As Integer
        Dim i As Integer
        
        'If the selection is in a table and one row height
            
        If Not Selection.ListObject Is Nothing And Selection.rows.Count = 1 Then
            Set tableObj = ActiveSheet.ListObjects(Selection.ListObject.Name)
            
            i = 1
            ReDim filterCriteria(1 To Selection.Cells.Count) As String
            ReDim filterFields(1 To Selection.Cells.Count) As Integer
            
            ' handle multi-selects
            
            For Each subSelection In Selection.Areas
                For Each cell In subSelection
                    filterCriteria(i) = cell.Text
                    filterFields(i) = cell.Column - tableObj.Range.Cells(1, 1).Column + 1
                    i = i + 1
                Next cell
            Next subSelection
            
            With tableObj.Range
                For i = 1 To UBound(filterCriteria)
                    .AutoFilter field:=filterFields(i), Criteria1:=filterCriteria(i)
                Next i
            End With
            Set tableObj = Nothing
        End If
    End Sub
    

### How does the `combinationFilter()` macro work?

**Checking if selected cells are inside a table**

We start by checking if the selection is inside a table by checking if the `Selection.ListObject` is not nothing. (Aside: there is no direct way to ask if there is a listobject. So we ask indirectly, by saying `Not Selection.ListObject Is Nothing`.)

Once we know that Selection is inside a table, we grab the table object and set it to the variable `tableObj`.

**Finding out what to filter**

To set filters on a table, we need to know the field number (ie column number inside the table) and filter criteria.

Filter criteria is denoted by cell values in the selection.

We are extracting filter criteria values & determining the column numbers for each of the selection’s cells using a simple For Each loop.

**Setting up the filters**

Once all the filter criteria are determined, we simply loop thru the criteria and set the filters on table using `tableObj.Range.AutoFilter` method.

### How to use this macro for your data?

This macro is designed to work with any table. I have tested it in Excel 2010 & Excel 2013 and it seems to work alright.

To use it with your data, follow below steps.

1.  Open your personal macros file
2.  Copy the combinationFilter() macro and paste it in your Personal Macros workbook in a module
3.  Save and close personal macros file.
4.  Add this macro to Excel ribbon or quick access toolbar (QAT)
    1.  To add to ribbon: Refer to below picture.![adding-macros-to-ribbon-tabs-howto](https://chandoo.org/wp/wp-content/uploads/2015/07/adding-macros-to-ribbon-tabs-howto.png)
    2.  To add to Quick Access Toolbar – [click here for instructions](http://chandoo.org/wp/2010/06/08/add-macros-to-excel-toolbars/)
        .
5.  Once you select the combination to filter, click on the ribbon / QAT button.
6.  Done!

### Download Selected Combination Filter Macro

**[Please click here to download the example workbook](https://chandoo.org/wp/wp-content/uploads/2015/07/filter-selection.xlsm)
**. Play with the macro to understand it better.

### New to VBA? Learn how to exploit its awesome power

If you are new to VBA, you might find above example both awesome & hard to digest. But don’t worry. Start with this [simple crash course on VBA](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
. Check out [more VBA examples](http://chandoo.org/wp/excel-vba/examples)
. Very soon you will be automating parts of your work and impressing your boss. All the best.

### Do you find the combination filter useful?

When I first thought about this macro, I feared the code might be too long or confusing. But I am happy with the outcome. It is a crisp, simple and powerful macro that I can use often when working with lots of data.

_**What about you?**_ Do you find this macro useful? How are you planning to deploy it for your work situations. Let me know in the comments area.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/filter-a-table-by-combination-of-values/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/filter-a-table-by-combination-of-values/#respond)
    
*   Tagged under [advanced filters](https://chandoo.org/wp/tag/advanced-filters/)
    , [data filters](https://chandoo.org/wp/tag/data-filters/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [for loop](https://chandoo.org/wp/tag/for-loop/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCP038: Data to Ink Ratio – What is it, How to optimize it, Techniques & Discussion](https://chandoo.org/wp/cp038-data-to-ink-ratio/)

[NextHow to find out if a text contains question? \[Excel formulas\]Next](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/)

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
    
    [Reply](https://chandoo.org/wp/filter-a-table-by-combination-of-values/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/filter-a-table-by-combination-of-values/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/filter-a-table-by-combination-of-values/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ