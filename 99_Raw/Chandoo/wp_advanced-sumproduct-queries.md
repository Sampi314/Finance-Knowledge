# Advanced Sumproduct Queries

**Source:** https://chandoo.org/wp/advanced-sumproduct-queries

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Advanced Sumproduct Queries
===========================

*   Last updated on January 2, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

The use of the [Sumproduct function](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 for doing multiple criteria Sum If’s is possibly one of the greatest extensions of an Excel function beyond what it was primarily designed for. Maybe it was actually designed with that in mind ?

However Sumproduct can be extended even further through use 2D Ranges together with carefully constructed queries.

The examples below are included in the [Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Sumproduct.xlsx "Advanced Sumproduct")
, [Excel 2003 Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Sumproduct.xls "Excel 97-2003 Example File")
.

**Scenario 1: Lookup a value within a 2D Range matching 2 criteria  
**
-----------------------------------------------------------------------

You have a table of Dates and Fruit Sold and Number Sold each Day

How many Bananas did I sell on the 4thMay?

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP1.png "SP1")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP1.png)

In the above I have setup 3 Named Ranges

Named ranges are used as it makes the reading of forthcoming formulas easier.

**Fruit**:                     C2:H2

**Dates**:                   B3:B12

**FruitData**:            C3:H12

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP2.png "SP2")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP2.png)

So, How many Bananas did I sell on the 4th May?

Using the equation =SUMPRODUCT((Fruit=D16)\*(Date=D15)\*FruitData)

Returns the correct answer **31**

**Related:** [Doing 2way lookups in Excel](http://chandoo.org/wp/2010/11/09/2way-lookup-formulas/ "How to write 2 Way Lookup Formulas in Excel?")

**Scenario 2:** **Sum all** ****values within a 2D Range matching 2 criteria****
--------------------------------------------------------------------------------

You have a table of Dates and Cars Sold and Number Sold each Day. There are multiple entries for on various days, possibly from various salesmen.

How many Holden cars did I sell on the 3rd May?

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP3.png "SP3")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP3.png)

So, How many Holden cars did I sell on the 3rd May?

Using the equation =SUMPRODUCT((Dates=D17)\*(Cars=D18)\*CarData)

Returns the correct answer **9 = (1 + 5 + 3)**

**Scenario 3:** **Sum** ****values within a 2D Range matching multiple unordered criteria****
---------------------------------------------------------------------------------------------

You have a table of Dates and Cars Sold and Number Sold each Day, There are multiple Entries for on various days.

How many Ford and Suzuki cars did I sell on the 10th May?

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP4.png "SP4")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP4.png)

So, How many Ford and Suzuki cars did I sell on the 10th May?

Using the equation =SUMPRODUCT((Dates=D24)\*((Cars=D25)+ (Cars=E25))\*CarData)

Returns the correct answer **13 = (4 + 5 + 3 + 1)**

**Note that this can be extended to add additional queries where the Car Type can be entered in any cell in the Range D25:H25**

\=SUMPRODUCT((Dates=D24)\*((Cars=D25)+ (Cars=E25) + (Cars=F25) + (Cars=G25) + (Cars=H25))\*CarData)

**Scenario 4:** **Sum** ****values within a 2D Range matching multiple ordered criteria****
-------------------------------------------------------------------------------------------

You have a table of Dates and Cars Sold and Number Sold each Day, There are multiple Entries for on various days.

How many Toyota and Holden cars did I sell on the 10th May?

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP5.png "SP5")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP5.png)

How many Toyota and Holden cars did I sell on the 10th May?

Using the equation =SUMPRODUCT((Dates=D30)\*(Cars=D31:H31)\*CarData)

Returns the correct answer **21 = (3 + 6 + 6 + 6)**

**Note that this can be extended to allowing additional queries but the Car Type must be entered into the same position as in the Header Row.**

**How Does This Work?**
-----------------------

The above techniques is using matrix arithmetic to setup a conjunctive truth table within the Sumproduct formula.

Using =SUMPRODUCT((B4:B6=D10)\*(C3:E3=D9)\*(C4:E6))

The conjunctive truth table logic (B4:B6=D10)\*(C3:E3=D9) is simply saying make a matix of elements that are true when the conditions are met and false otherwise

Sumproduct then takes this and multiplies and it by the data values and accumulates the values to get the sum of the matching values.

It is important to note that the Width and Height of the Criteria Row and Column must match the Width and Height of the data area or a #Value! error is returnd.

### The Maths

To understand and explain how this works I will use a simple model with 3 rows and 3 columns see below

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP6.png "SP6")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP6.png)

The formula: =SUMPRODUCT((B4:B6=D10)\*(C3:E3=D9)\*(C4:E6)), shown above consists of 3 areas

**(B4:B6=D10)** is a 3 Rows x 1 Column range

**(C3:E3=D9)** is a 1 Row x 3 Columns range

**(C4:E6)** is a 3 Row x 3 Column range

**Breaking the formula into components**

\=SUMPRODUCT(**(B4:B6=D10)\*(C3:E3=D9)**\*(C4:E6))

**(B4:B6=D10)\*(C3:E3=D9)** is the same as multiplying 2 arrays, representing the 2 areas as shown below

You can see that where the components are True I have put a 1 and a 0 where they are false

Where the Date was 3-May Excel evaluates this to 1 and similarly where the Fruit was a Banana, Excel evaluates this to 1.

Where the criteria isn’t met Excel evaluates this to a 0

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP7.png "SP7")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP7.png)

The multiplication of a 3 x 1 and a 1 x 3 array is a 3 x 3 array

Representing the **(B4:B6=D10)\*(C3:E3=D9)** part of the equation

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP8.png "SP8")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP8.png)

Next this is multiplied by the data area

\=SUMPRODUCT(**(B4:B6=D10)\*(C3:E3=D9)**\***(C4:E6)**)

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP9.png "SP9")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP9.png)

This is the same as multiplying two 3×3 arrays which produces a 3 x 3 array, below:

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/SP11.png "SP11")](https://chandoo.org/wp/wp-content/uploads/2011/05/SP11.png)

**Sumproduct** then adds up all the array components to get the final answer of **3**.

### Modifications

The Data Area can be included in the Truth Table Logic or as a seperate component of Sumproduct.

\=SUMPRODUCT((B4:B6=D10)\*(C3:E3=D9)\***(C4:E6)**) and =SUMPRODUCT((B4:B6=D10)\*(C3:E3=D9), **(C4:E6)**) are both equal

Multiple “OR” crietria can be added by use of the+ operator within criteria

In Scenario 3 above, we sum the number of Ford or Suzuki cars sold on the 10th May.

SUMPRODUCT((Dates=D24)\***(**(Cars=D25) **+** (Cars=E25) **+** (Cars=F25) **+** (Cars=G25) \+ (Cars=H25)**)**\*CarData)

The Or logic is added to the criteria by use of the + operator above within the criteria for Cars

the And logic is added by use of the \* between the Dates and Cars criteria

### Other Logic Elements

You can add Greater Than (>), Less Than (<) etc and other logic elements to the queries to suit your requirements.

****Sample File  
****
----------------------

The examples below are included in the [Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Sumproduct.xlsx "Advanced Sumproduct")
, [Excel 2003 Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Sumproduct.xls "Excel 97-2003 Example File")
.

**What do you think of the above technique ?**
----------------------------------------------

What do you think of the above technique ?

_**Let us know in the comments below.**_

**More Tips & Resources:**
--------------------------

*   [Introduction to SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   [Introduction to SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/ "Introduction to Excel SUMIFS Formula")
    
*   [More on SUMPRODUCT formula – tips & examples](http://chandoo.org/wp/tag/sumproduct/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [102 Comments](https://chandoo.org/wp/advanced-sumproduct-queries/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/advanced-sumproduct-queries/#respond)
    
*   Tagged under [2D](https://chandoo.org/wp/tag/2d/)
    , [and()](https://chandoo.org/wp/tag/and/)
    , [Array](https://chandoo.org/wp/tag/array/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [Conjunctive Truth Table](https://chandoo.org/wp/tag/conjunctive-truth-table/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Matrix](https://chandoo.org/wp/tag/matrix/)
    , [Matrix Arithmetic](https://chandoo.org/wp/tag/matrix-arithmetic/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Or](https://chandoo.org/wp/tag/or/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousMod() function in excel to Implement Escalation Frequency \[Financial Modeling Tutorials\]](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/)

[NextHow Would You Visualize Product Sales Data? \[Excel Challenges #2\]Next](https://chandoo.org/wp/product-sales-visualization-challenge/)

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
    
    [Reply](https://chandoo.org/wp/advanced-sumproduct-queries/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/advanced-sumproduct-queries/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/advanced-sumproduct-queries/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ