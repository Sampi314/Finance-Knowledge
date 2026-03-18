# How to find duplicate values in two columns in Excel using formula » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to find duplicate values in two columns in Excel using formula
==================================================================

*   Last updated on February 25, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Let’s say you have two lists of values in Excel and want to find out all the common values (ie duplicates) and extract them. In this article, let me explain the formulas for this.

![](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0106.png)

Formula for counting number of duplicate values in two columns:
---------------------------------------------------------------

Here is the formula to count number of common values between two columns.

    =COUNT(XMATCH(D4:D20,B4:B16))
    
    'Generic formula pattern
    
    =COUNT(XMATCH(list2,list1))

### How does this formula work?

The XMATCH(list2, list1) finds the position of every item in **_list2_** in **_list1_**. Then it returns an array of these positions (or #N/As if the value is not in the other list).

COUNT(XMATCH(..)) simply counts the numbers in these positions. So the errors are ignored and we get the count of common values.

### Limitations of this formula

The above formula requires XMATCH function, which is available only in Excel 365 and Excel online. If you are using an older version of Excel, [refer to this page for alternative approaches](https://chandoo.org/wp/compare-two-tables/)
.

Extracting the duplicate values between two columns with Excel formula
----------------------------------------------------------------------

We can use the same approach to find all the duplicate values and extract them as a list. Here is the formula for that.

    =LET(arr, XLOOKUP(B4:B16,D4:D20,D4:D20,""),FILTER(arr, arr<>""))
    
    'generic formula pattern
    
    =LET(list1, <range goes here>, list2, <range goes here>, 
    arr, XLOOKUP(list1,list2,list2,""),FILTER(arr, arr<>""))

### Formula Explanation

Let’s go inside out.

*   **XLOOKUP(B4:B16,D4:D20,D4:D20,””):** This lookups every item in the first list against second list and returns the value from second list if found and blank space other wise. \[related: [learn more about XLOOKUP](https://chandoo.org/wp/xlookup-examples/)\
    \]
*   **LET(arr, XLOOKUP(..):** We store the xlookup output (which would be an array the size of first list) in to a variable called arr.
*   **FILTER(arr, arr <> “”):** We take the output of the xlookup, which is stored in the variable arr and remove any blank values (ie the value is not in the second list).

Here is the sample output of both of these formulas (counting duplicate values and extraction of duplicate values).

![](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0106.png)

Download Example Workbook
-------------------------

**[Click here to download the sample workbook](https://chandoo.org/wp/wp-content/uploads/2025/02/duplicate-in-two-columns-excel-formula.xlsx)
** with these formulas. Play with the data & formulas to learn how they work.

Other ways to extract duplicate values from two columns:
--------------------------------------------------------

You can also use Excel features like pivot tables, power query or conditional formatting to deal with this issue. Refer to below pages for the explanation of these powerful techniques.

*   [Extract common values between two tables with Power Query](https://chandoo.org/wp/compare-two-tables/)
    
*   [Extracting duplicate values using formulas in older Excel](https://chandoo.org/wp/unique-duplicate-missing-items-excel-help/)
    
*   [Compare two columns and highlight duplicate values](https://chandoo.org/wp/compare-lists-excel-tip/)
    
*   [Using Power Pivot to combine two columns (joins)](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    
*   [Counting unique values with a formula (older Excel)](https://chandoo.org/wp/formula-forensics-025/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [duplicates](https://chandoo.org/wp/tag/duplicates/)
    , [dynamic array formulas](https://chandoo.org/wp/tag/dynamic-array-formulas/)
    , [filter](https://chandoo.org/wp/tag/filter-2/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [let](https://chandoo.org/wp/tag/let/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    , [xmatch](https://chandoo.org/wp/tag/xmatch/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to freeze rows in excel](https://chandoo.org/wp/how-to-freeze-rows-in-excel/)

[NextNew vs. Returning Customers Analysis with DAX \[Easy Formulas\]Next](https://chandoo.org/wp/new-vs-returning-customers-dax/)

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
    
    [Reply](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-find-duplicate-values-in-two-columns-in-excel-using-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ