# Automatically Format Numbers in Thousands, Millions, Billions in Excel [2 Techniques]

**Source:** https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]
=======================================================================================

*   Last updated on July 22, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Ever wanted to automatically format values in thousands, millions or billions in Excel? In this article, let me show you two powerful techniques to do just that.

![automatic cell formatting in Excel to thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)

Technique 1: Using Custom Format Codes
--------------------------------------

![Before and after custom cell formatting in Excel\
](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0081.png)

We can use Custom Number Format codes in Excel to quickly turn the number to thousands, millions or billions. To do this:

1.  Select your numbers and go to Format Cells (Ctrl 1)
2.  From the number tab, select “Custom” for category and type the code below:

    [<1000]##,##0;[<1000000]#,###.0,"K";#,###.0,,"M"

3.  Press OK to see the magic.

![Adding "Custom" format code in Excel - auto format in thousands / millions\
](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0080.png)

How does it work?
-----------------

    [<1000]##,##0;[<1000000]#,###.0,"K";#,###.0,,"M"

The above custom format code has 2 rules and a default behavior, each separated by semicolon ;

*   **\[<1000\]##,##0** – This portion formats any values under 1,000 as usual numbers
*   **\[<1000000\]#,###.0,”K”** – Any numbers under 1 million will be formatted in thousands (the extra comma at the end rounds the numbers to thousands) and adds letter “K” at the end.
*   **#,###.0,,”M”** – And finally this is the default rule. Any other numbers (obviously more than 1 million) will be formatted in millions (2 extra commas at the end) and the letter “M” added at the end.

**[Learn more about custom cell format codes in Excel](https://chandoo.org/wp/custom-cell-formatting-in-excel-few-tips-tricks/)
.**

Limitations of Custom Format code
---------------------------------

While custom cell format is a great option, it has a few limitations.

*   **Supports only 3 rules:** The custom format codes can only accept up to 3 options. So if you want to have units, thousands, millions, billions (i.e. 4 levels), we can’t do that with custom format codes.
*   **Negative numbers not supported:** As a consequence of 3 rule limitation, we can’t do negative numbers with this approach. If you just want the “thousands” or “millions” formatting for both positive and negative numbers, you can use the below _alternative rule._

    'Format in thousands, works for both positive and negative numbers:
    
    [<-1000]-#,##0.0,"K";[<1000]#,##0;#,##0.0,"K"

Better Technique 2: Using Format Lookup Table
---------------------------------------------

A better option is to use a lookup table to decide the format code based on the size of your numbers and then automatically switching the format with TEXT function.

![Formatting using lookup table and text function in excel](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0083.png)

First set up a lookup table like this in your workbook. (I normally put this in hidden settings tab for my dashboards).

![format codes - lookup table](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0082.png)

Then, use the below formula to automatically lookup the value and format it in the corresponding format style based on the table.

    'Auto-format numbers based on the lookup table
    
    =TEXT(B5,LOOKUP(B5,$J$5:$J$11,$K$5:$K$11))

How does this formula work?
---------------------------

The formula has 2 key components: TEXT() & LOOKUP()

*   **LOOKUP() Function:** This will lookup the exact value or next lower value. For example, when we lookup the value 12,345 the lookup function (LOOKUP(12345,$J$5:$J$11,$K$5:$K$11)) will return the format code – **#,##,.0″K”**
*   **TEXT() Function:** Once we have the format code, we use TEXT function to convert the value in B5 to that format and return it as a string value. For example, 12345 when formatted in #,##,.0″K” will become 12.3K

How to auto-format Chart Labels?
--------------------------------

![formatted chart labels - demo](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0077.png)

We can use the same approach to auto-format chart labels as well. For example, above, I have shown a column chart with _dynamic chart labels_ that auto-format based on the value. To get this:

![Steps for applying custom number format code to chart labels](https://chandoo.org/wp/wp-content/uploads/2024/07/Snag_1fb9ba6a.png)

0.  Add “data labels” to your chart.
1.  Select the labels and go to “format labels” (press CTRL 1)
2.  From the label options tab, go to “Number” area
3.  Uncheck “Linked to Source” option.
4.  Type the format code as shown above in this article.
5.  Click on “Add”
6.  That is all. Your chart will now have dynamically auto-formatted labels.

Here is a quick demo of the process:

![demo - adding custom format codes to chart labels](https://chandoo.org/wp/wp-content/uploads/2024/07/2024-07-21_17-18-59.gif)

Using “Formula” approach with Chart Labels
------------------------------------------

![chart labels using "value from cells" option.](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0079.png)

If you have values all over the place and need thousands / millions / billions style format for your labels, you can also use “formula” approach, as discussed above. To do this:

![Steps for adding "value from cells" to chart labels in Excel](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0078.png)

1.  First calculate the labels with formula (lookup table) approach.
2.  Add labels to the chart and go to “format labels”.
3.  From the “label options” area, select “value from cells”.
4.  Select the formula label range.
5.  Uncheck original “values” from the labels.
6.  Done. Your chart now has dynamic labels that are fetched thru formula lookup method.

Why auto-format your numbers?
-----------------------------

Auto-formatting numbers helps in reducing clutter of your reports and makes them look professional. I always use this approach when creating [executive dashboards](https://chandoo.org/wp/excel-dashboards/)
 or [KPI reports](https://chandoo.org/wp/kpi-charts-dashbaords/)
 in Excel.

In Conclusion: Which method to use?
-----------------------------------

For simpler situations, use the custom cell format rule method.

But if you have data all over the place or need to go beyond more than 3 rules, use the formula approach.

Download Sample File – Auto format numbers
------------------------------------------

**[Here is a sample Excel workbook](https://chandoo.org/wp/wp-content/uploads/2024/07/auto-format-numbers-excel.xlsx)
** with all the examples above so you can understand this technique.

Video: Auto format numbers in Excel \[2 ways\]
----------------------------------------------

[Watch this video tutorial](https://youtu.be/w1uiQbONf1U)
 to learn how to use these two techniques.

https://youtu.be/w1uiQbONf1U

More creative ways to use custom cell formatting in Excel
---------------------------------------------------------

Learn more about Excel’s custom cell formatting feature using the articles below:

*   [Custom cell formatting – many examples](https://chandoo.org/wp/custom-cell-formatting-in-excel-few-tips-tricks/)
    
*   [Understand and make your custom format codes](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/)
    
*   [Show decimal point only if the number is below 1](https://chandoo.org/wp/show-decimal-points-if-needed/)
    
*   [Hide away cell contents with format code ;;;](https://chandoo.org/wp/hide-cell/)
    
*   [Automatically coloring cells with custom format codes](https://chandoo.org/wp/custom-number-formats-colors/)
    
*   [Get tick marks in cells with formatting](https://chandoo.org/wp/get-tick-marks-in-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/#respond)
    
*   Tagged under [custom cell formatting](https://chandoo.org/wp/tag/custom-cell-formatting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [lookup](https://chandoo.org/wp/tag/lookup/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [Text Format](https://chandoo.org/wp/tag/text-format/)
    , [text()](https://chandoo.org/wp/tag/text/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to compare two Excel sheets using VLOOKUP? \[FREE Template\]](https://chandoo.org/wp/compare-two-excel-sheets-using-vlookup/)

[NextHow to calculate WEEKNUMBER in Month / Quarter / Year with Excel?Next](https://chandoo.org/wp/how-to-calculate-weeknumber-in-month-quarter-year-with-excel/)

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
    
    [Reply](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ