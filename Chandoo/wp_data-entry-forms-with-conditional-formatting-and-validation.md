# Make Awesome Data Entry Forms by using Conditional Formatting + Data Validation » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Make Awesome Data Entry Forms by using Conditional Formatting + Data Validation
===============================================================================

*   Last updated on February 7, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week we saw a really cool [holiday request form](http://chandoo.org/wp/2011/02/01/holiday-request-form-excel/)
 made by _Theodor_.

**This week, we will learn how to combine conditional formatting and data validation to create an awesome data entry form.**

### First see a demo to understand what I mean:

![Data Entry forms with Conditional Formatting & Data Validation - Demo](https://chandoo.org/img/cf/data-entry-forms-with-cf-and-dv-demo.gif)

### How to create such a data entry form?

Very simple, just grab a cup of coffee (or your favorite fried-nuts-crushed-and-brewed-with-hot-water) and follow my lead.

### Step 1: Set up Data Validation

Assuming you need to gather some inputs, like shown above. First thing to do would be setting up data validation rules in a cell so that your users can specify the type of data they are entering. For eg. they can choose card or paypal or other as payment mode and depending on that, enter further details.

To do this, just select the cell and go to Data > Validation. Choose “List” as the rule and give values.

![Data Validation Criteria for our form](https://chandoo.org/img/cf/data-validation-criteria.png)

### Step 2: Add conditional formatting rules.

Now, based on the selected value, we need to highlight a set of cells.

_Assuming all the data to be gathered in cells C4:G4,_

Select first two cells (C4:D4), go to Home > Conditional Formatting > New Rule

Here, we need to tell Excel **to highlight the C4 and D4 if the type of payment is Card**.

So choose the CF rule type as “Use a formula to determine which cells to format” and the check if $B4 is “card”.

![Conditional Formatting Rules to highlight cells based on payment mode](https://chandoo.org/img/cf/conditional-formatting-rule-to-highlight-cells.png)

![](https://cache2.chandoo.org/images/icons/tip-icon.png)**Tip:** We need to use $B4 since we want Excel to check column B even if we are applying formatting to C4 or D4. [Read more](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)
.

### Step 3: Add Conditional Formatting rules to other cells (E4:F4, G4)

Using the same logic.

### Step 4: Bask in glory!

That is all. There is no step 4. We are done. Finish the coffee or whatever you mixed with hot water. Just save the file and send it to your customer, vendor or boss. Bask in glory as there will be fewer data entry mistakes and more awesome.

### Home work: Get Creative and do more

**You can use some creativity and make the data entry form even more awesome.** For example, you could show a tick mark when the data entry is complete. Also you could highlight only when the cell is blank (ie if the data is already entered, there is no point highlighting)

See what I came up with:

![Data Entry form - Advanced Example](https://chandoo.org/img/cf/advanced-data-entry-form-example.png)

_**I am not going to tell you how to do the above. That is for you to figure out.**_

### Download Excel Files

[**Click here to download the excel file with the data entry form example**](https://img.chandoo.org/d/data-entry-forms-with-cf-and-dv-example.xls)
. Play with it to understand how to make similar forms. Become awesome!

And if you can not solve the homework problem, [download this file](https://img.chandoo.org/d/data-entry-forms-example-2.xlsx)
 and examine it.

### How do you make your data entry forms awesome?

I love [data validation](http://chandoo.org/wp/tag/data-validation/)
. It makes the whole process of gathering valid data dead simple. Also, it is an excellent way to change month or other settings in [dashboards](http://chandoo.org/wp/excel-dashboards/)
. ([example 1](http://chandoo.org/wp/2010/08/04/travel-site-dashboard-review/)
, [2](http://chandoo.org/wp/2010/11/01/mix-vlookup-with-data-validation-for-some-magic-vlookup-week/)
, [3](http://chandoo.org/wp/2010/04/01/incell-panel-chart/ "Visualizing Survey Results using Excel Panel charts")
)

**What about you?** How do you use Data Validation and other excel features to make your input forms both simple and awesome? **Please share your experiences and ideas using comments. Go!**

### Learn More About Data Validation & Conditional Formatting:

_As I said earlier, I really love data validation, conditional formatting features of Excel_. They are quite powerful and very useful when working with lots of data. We have very good information about these features on chandoo.org. Start with the below articles to learn more.

*   [What is Conditional Formatting and how to use it?](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
     \[[Video](http://chandoo.org/wp/excel-tutorial/using-conditional-formatting/ "Excel Conditional Formatting - Video Tutorial - Excel for Beginners")\
    \]
*   [How to create a simple data validation list?](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
    
*   [5 tips to become conditional formatting rock star](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
*   More tutorials & tips on [conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    , [data validation](http://chandoo.org/wp/tag/data-validation/)
    
*   **Recommended:** [**Join Excel School**](http://chandoo.org/wp/excel-school/)
     if you work with data often. You will save a ton of time.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/#respond)
    
*   Tagged under [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMy trip to Maldives…, \[travelogue + bonus Excel tip\]](https://chandoo.org/wp/maldives-travelogue/)

[NextIntroduction to Project Finance Modeling in ExcelNext](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ