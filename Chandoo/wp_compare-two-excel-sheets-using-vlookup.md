# How to compare Two Excel Sheets with VLOOKUP (FREE file)

**Source:** https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to compare two Excel sheets using VLOOKUP? \[FREE Template\]
================================================================

*   Last updated on July 3, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

You are the boss of ACME Inc. And one day, both of your accountants Sara and James come to you with two versions of the customer payment data. How do you compare these two Excel sheets and reconcile the data? We can use VLOOKUP to do just that. In this article, let me explain the step-by-step process.

Step 1: Set up data in two Excel sheets
---------------------------------------

Copy both sets of data to two sheets in an Excel file. For example, here I have two sheets – one with Sara’s data and another with James’ data. Both datasets have identical columns, but the data is not same.

![Compare two Excel sheets with VLOOKUP\
](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0063-2.png)

Step 2: Start with the first sheet and write the VLOOKUP formula
----------------------------------------------------------------

Go to the first sheet. Here, we are going to use VLOOKUP (or XLOOKUP, if you have Excel 365) to get the matching value from second sheet.

For the purpose of this exercise, you need a unique identifier column like Customer ID or invoice number.

In the adjacent column we are going to write the VLOOKUP function to get the corresponding values for the customer ID’s from second sheet. The set up should look like this:

![Spreadsheet set up for comparing two sheets](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0064.png)

Step 3: The LOOKUP formula
--------------------------

Write the VLOOKUP formula like this:

    =VLOOKUP(B3,'James Sheet'!$B$3:$C$32,2,FALSE)

### VLOOKUP Formula Explanation:

*   VLOOKUP formula finds matching value from a range. For example, here we can use it to search for the customer ID and get their payment details.
*   B3: refers to the cell with customer ID
*   ‘James Sheet’!$B$3:$C$32: is the range of data in second Excel sheet which we are trying to match
*   2: is the column number of the “Amount paid” column in second sheet.
*   FALSE: ensures that VLOOKUP will look for an exact match in the second sheet.
*   [Learn more about VLOOKUP function](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    .

Or if you prefer to [use XLOOKUP formula](https://chandoo.org/wp/xlookup-examples/)
, use this:

    =XLOOKUP(B3,'James Sheet'!$B$3:$B$32,'James Sheet'!$C$3:$C$32, "ID missing")

![VLOOKUP formula for comparing two sheets](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0065.png)

Fill this formula down so you can see the matching values from second sheet.

At the end of this step, your first sheet should look like this:

If you have any missing IDs, those cells should have #N/A.

![#N/A error in VLOOKUP when the ID is missing in the second worksheet](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0066.png)

Step 4: Reconcile the values
----------------------------

Now that you have the matching value from second Excel sheet, let’s reconcile both to see which values matched and which values are different.

For this, we can use IF formula. Here is the formula:

    =IF(ISERROR(D3),"ID Missing", IF(D3<>C3,"Not matching", "Matching"))

![Using IF formula to reconcile the results of two sheet comparison](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0067.png)

This formula compares the first sheet value with the second sheet value and tells us if they are same or different. It also checks for the #N/A error and flags those records as “Missing ID”.

Fill the formula down and you will have reconciliation information for your data.

![Completed reconciliation of the data](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0068.png)

Now you can use FILTERS in Excel to see all matching or not matching records easily.

Step 5: Conditional format the non-matching records
---------------------------------------------------

![Using conditional formatting to highlight unmatched values](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0070.png)

This optional step helps us quickly spot all the non-matching and missing ID values quickly.

To do this,

1.  Select the entire range of data (for example: B3:E32)
2.  Go to Home ribbon > Conditional Formatting and click on “**new rule”**
3.  Select the rule type as “Use a formula to determine the…”
4.  Type the rule as =$E3 = “Not matching” (refer to the below image)
5.  Set the formatting to highlight the non-matching records
6.  Click OK to add the rule.
7.  Add one more rule for “ID missing” highlight and repeat steps 3 to 6

![conditional formatting rule](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0069.png)

When you finish, your data will highlight all the non-matching and missing ID values in different color so you can easily identify them.

Related: [Learn more about Excel conditional formatting feature](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/)
.

FREE Comparison & Reconciliation Template
-----------------------------------------

If you need a quick template to compare two Excel sheets and reconcile the data, **[download my sample file here](https://chandoo.org/wp/wp-content/uploads/2024/07/free-compare-two-excel-sheets-template.xlsx)
**.

Other techniques to reconcile and compare two Excel sheets:
-----------------------------------------------------------

While using VLOOKUP is a quick and elegant way to compare two spreadsheets, Excel also offers few more options. These are:

*   **Power Query:** We can use Power Query to compare two sheets or two workbooks of data and reconcile the differences between values. Power Query also makes it easy to compare when you have multiple ID columns (for example: Customer ID & Date as the criteria for comparison). Refer to my [Power Query tutorial page](https://chandoo.org/wp/power-query-tutorial/)
     for more information on how to combine data with it.
*   **Using XLOOKUP instead of VLOOKUP:** As demoed above, we can use the new XLOOKUP function in Excel to perform the comparison. This allows for built-in error handling so we can see “Missing IDs” easily. **[Read more about XLOOKUP function here](https://chandoo.org/wp/xlookup-examples/)
    **.
*   **Using Conditional formatting:** Excel’s conditional formatting also offers a powerful and simple way to compare two lists of values. [See this page for details](https://chandoo.org/wp/compare-lists-excel-tip/)
    .
*   **Using formulas vs. Power Query:** I discuss the approaches for comparing two Excel sheets with formulas and PQ in [my YouTube video here](https://youtu.be/kfeFcyDrcvQ)
    .
*   **Using Pivot Tables:** Excel Pivot tables can link two tables of data on a key column (like customer ID) so you can easily compare values from both in one view. This feature is called **_relationships._** _[Learn more about Table Relationships in Excel here](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    ._

In conclusion…
--------------

Comparing two Excel sheets is an easy task once you know how to use the VLOOKUP (or XLOOKUP) function in Excel. I have used this exact approach countless times when dealing with multiple versions of files or different versions of truth. The process is easy, and the results are actionable.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/#respond)
    
*   Tagged under [comparison](https://chandoo.org/wp/tag/comparison/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [reconcile](https://chandoo.org/wp/tag/reconcile/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousSales Analysis Dashboards with Power BI – 30+ Alternatives](https://chandoo.org/wp/sales-dashboards-power-bi/)

[NextAutomatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]Next](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ