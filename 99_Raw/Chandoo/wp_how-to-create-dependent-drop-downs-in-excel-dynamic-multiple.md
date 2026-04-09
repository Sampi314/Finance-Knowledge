# How to make Dynamic Dependent Drop-down in Excel (any levels)

**Source:** https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How-to create Dependent Drop Downs in Excel \[Dynamic & Multiple\]
==================================================================

*   Last updated on February 14, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you want to **create a dynamic dependent drop down list** in Excel like below? You can use XLOOKUP and data validation to set this up quickly. It is fully dynamic and works across a full column too.

![multiple dependent dropdowns in excel - demo](https://chandoo.org/wp/wp-content/uploads/2024/02/dependent-drop-downs-in-excel-demo.gif)

Steps to Create Multiple Dependent Dropdown List in Excel
---------------------------------------------------------

Dependent or cascading dropdowns are a valuable way to make your workbooks error free and improve the user experience. Follow these steps to set them up.

### Step 1: Set up your validation list data.

In a blank area of your workbook, set up the data validation lists. **_If you have just two-levels,_** use the structure as depicted below.

![data layout for setting up the validation list](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3169.png)

If you have 3 or more levels, just set up the first two-levels as shown above. Then for each additional level, create a structure like above.

### Step 2: Create Data Validation Rules for the Drop-downs

Now, you will need to create data validation rules for each of the levels.

### For the main or first category,

![Data validation rule for first or main category](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3171.png)

1.  Select the entire column of cells
2.  Go to Data ? Data Validation
3.  Change the validation type to “List”
4.  Specify Source as the range of cells containing the main or first category.

### For the next category items

The process for all these other items is same. We are going to use [XLOOKUP function](https://chandoo.org/wp/xlookup-examples/)
, which can return multiple values for the search criteria.

**_Related: [Learn more about XLOOKUP function in Excel](https://chandoo.org/wp/xlookup-examples/)
._**

![XLOOKUP formula for creating dependent drop down list\
](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3172.png)

1.  Select the entire column
2.  Make a note of the first cell of previous column. In this case, that is D5.
3.  Go to Data ? Data Validation
4.  Set the rule type as “List”
5.  For source, write the XLOOKUP formula with below pattern.

    =XLOOKUP(SELECTED_CATEGORY, CATEGORY_NAMES, SUB-CATEGORY_NAMES)

For example, in my case, _selected category_ is in D5, category names are in J4:N4 and product names are in J5:N15. So my XLOOKUP formula looks like this.

    =XLOOKUP(D5, $J$4:$N$4, $J$5:$N$15)

Refer to below illustration to understand how these rules work.

![explanation of xlookup logic and illustration for cascading drop down](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3170-1.png)

### Step 3: Using the Dependent Drop Downs

Now that you have set up both main category and sub-category (or product) level rules, you can start to use the data validation drop downs like below.

1.  Select a category in the first column.
2.  When you go to the next column, you will see all the sub-category items there.
3.  Pick a selection from the list.
4.  Go back to first column to add a new item.

![multiple dependent dropdowns in excel - demo](https://chandoo.org/wp/wp-content/uploads/2024/02/dependent-drop-downs-in-excel-demo.gif)

How does this work? – The details
---------------------------------

This key ingredient of this Dependent Drop-down technique is [XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
. Previously, I’ve [used INDIRECT formula](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/)
 with pre-defined names or even [OFFSET](https://chandoo.org/wp/offset-formula-explained/)
 formulas. But now that XLOOKUP returns the full range of values, we can simplify the process.

**_Here is how this works:_**

1.  When you select a category in D5, the data validation rule runs the XLOOKUP formula to get the matching values for that category in the range J4:N4.
2.  Then, as the return value for XLOOKUP is the range J5:N15, it returns the rows (or product names) corresponding to selected category.
3.  For example, if you picked “Bites” category in D5, then XLOOKUP will return the product values for Bites category – _ie_ the range K5:K15
4.  This list is then fed to the data validation drop-down.

**_But what about all the blank values at the end…?_**

Excel 365 automatically removes any duplicate items in the data validation list. So it would remove all the blank cells and replace them with a single blank value.

Works with 3 Levels too…
------------------------

The beauty of XLOOKUP based approach is, your formulas and data set up are exactly same even if you need 3 levels or 4 levels or even more. Here is a demo of how my drop-downs work when used with 3 levels (in a table).

![Demo of dependent drop down list Excel with 3 levels ](https://chandoo.org/wp/wp-content/uploads/2024/02/3-level-cascading-drop-down-demo.gif)

Video Instruction: Dependent Dropdown Lists in Excel
----------------------------------------------------

I made a video explaining how to create such a dependent drop down list in Excel. You will also see how the XLOOKUP really works. Watch the video below or [on my channel](https://youtu.be/kjD3z_OWWpE)
.

?Sample File – Excel Dependent Drop Down Validation
---------------------------------------------------

Please grab my sample workbook with all the formulas for both two-level and three-level scenarios. Refer to the data validation rules to understand the formula syntax.

**[Click here to download the workbook](https://chandoo.org/wp/wp-content/uploads/2024/02/dependent-drop-downs-demo.xlsx)
.**

Limitations of this approach for cascading dropdowns
----------------------------------------------------

*   **Compatibility:** The biggest limitation of this technique is you need **Excel 365** or **2019**+. So if you are your clients use an older version of Excel, you can’t rely on this technique. You can still use the [OFFSET formula based approach we discussed here](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/)
    .
*   **You need to set up formulas:** If you are not familiar with Excel formulas, this technique will be hard for you. Fortunately the formulas themselves are not that complex.

More ways to create Dependent Drop-downs in Excel
-------------------------------------------------

If you want to make dependent drop-downs using another way, check below resources:

*   [Cascading Drop-downs in Excel – using INDEX & COUNTA functions](https://chandoo.org/wp/cascading-drop-down/)
    
*   [Multi-level option for older versions of Excel](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/)
    
*   [Using INDIRECT and named ranges](https://www.contextures.com/xldataval02.html)
     \[Contextures\]

Alternatives to Dependent Drop-down Lists
-----------------------------------------

You can use a [two-level data validation list](https://chandoo.org/wp/two-level-drop-downs/)
 instead. These are easy to setup and don’t require any complex formulas.

[![two-level data validation list](https://chandoo.org/wp/wp-content/uploads/2024/02/image.png)](https://chandoo.org/wp/two-level-drop-downs/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/#respond)
    
*   Tagged under [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousVLOOKUP(), MATCH() and INDEX() – explained in plain English](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)

[NextLoan Amortization Schedule in Excel – FREE TemplateNext](https://chandoo.org/wp/loan-amortization-schedule-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ