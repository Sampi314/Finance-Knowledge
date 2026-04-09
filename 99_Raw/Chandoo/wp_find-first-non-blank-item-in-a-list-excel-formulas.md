# Find first non-blank item in a list with formulas » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas

---

*   [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Find first non-blank item in a list with formulas
=================================================

*   Last updated on January 15, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**_Blank cells are an invisible pain in the analysis._** Dealing with them is frustrating, time-consuming and often very complex. At chandoo.org, we are not big fans of blank cells. That is why we wrote:

*   [How to delete blank cells & rows?](http://chandoo.org/wp/2010/01/26/delete-blank-rows-excel/)
    
*   [Dealing with blanks – case study](http://chandoo.org/wp/2010/02/23/find-and-remove-blank-cells/)
    
*   [Quickly filling blank cells in a table](http://chandoo.org/wp/2011/10/17/fill-blank-cells-in-a-table/)
    
*   [Extracting non-blank data from a list](http://chandoo.org/wp/2012/03/01/formula-forensic-014/)
    

Today, lets talk about one more scenario. **Lets say you want to find out the first non-blank item in a list. How would you do it?**

![Lookup first non blank cell using Excel formulas](https://chandoo.org/wp/wp-content/uploads/2014/01/lookup-first-non-blank-cell-formulas.png)

Finding first non-blank item in a list
--------------------------------------

Lets say our list is in the range **B3:B100**.

_**Without using formulas**_

If you just want to get the first non-blank item in a list and do not want to use formulas, then you can [remove all the blank items from the list](http://chandoo.org/wp/2010/01/26/delete-blank-rows-excel/)
. To do this:

1.  Select entire list
2.  Press F5, click on [special](http://chandoo.org/wp/2012/03/12/go-to-special/)
    
3.  Choose blanks, click ok.
4.  Press CTRL –
5.  Remove rows (or shift cells up as needed).
6.  Done!

Now that the blank cells are gone, just refer to B3 to get the first non-blank item in the list.

### Using formulas

Although the non-formula approach works, it is manual. That means every time your data changes, you must repeat the steps. Not very cool, especially if you call yourself awesome. So, lets use a powerful formula to get that first non blank item in our list.

**First see the formula:**

`=VLOOKUP("*", B3:B100, 1,FALSE)`

**How it works?**

We want to lookup for first cell that contains something. It does not matter what that value is.

That is what \* does. \* is a wild card in Excel. When you ask [VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 to find \*, it finds the first cell that contains anything.

NOTE: This approach finds first cell that contains any TEXT. So if the first non-blank cell is a number (or date, % or Boolean value), the formula shows next cell that contains text.

### How to find first non-blank value (text or number)?

If you want to find first non-blank value, whether it is text or number, then you can use below array formula.

`=INDEX(B3:B100, MATCH(FALSE, ISBLANK(B3:B100), 0))`

_Make sure you press CTRL+Shift+Enter after typing this formula._

#### How this formula works?

**ISBLANK(B3:B100) portion:** This gives us list of TRUE / FALSE values depending on the 98 cells in B3:B100 are blank or not. It looks like this:

`{TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE; ...}`

**MATCH(FALSE, ISBLANK(…), 0) portion:** Once we have the TRUE / FALSE values, we just need to find the first FALSE value (ie, first non-blank cell). That is what this MATCH function does. It finds an _exact_ match of FALSE value in the list.  (Related: [Using MATCH Formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
)

**INDEX(B3:B100, MATCH(…)) portion:** Once we know which cell is the first non-blank cell, we need its value. That is what INDEX does. (Related: [Introduction to INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
)

Home work for you
-----------------

If you like this formula and want some challenge, read on.

For these home work problems, use the range B3:B100 or named range _list_ in your formulas.

1.  Can you think of some other formulas to find first non-blank cell?
2.  What formula gives 2nd non-blank cell value?
3.  What formula gives last non-blank cell value?

**Go ahead and post your answers using comments.**

Drawing a blank when working on lookups?
----------------------------------------

If you are giving blank stares whenever your boss asks for lookup related stuff, then you are going to love this. My latest publication, **The VLOOKUP Book**is a comprehensive guide to VLOOKUP, INDEX, MATCH, LOOKUP and other techniques to lookup any data and answer questions with confidence.

*   [Get The VLOOKUP Book from Amazon](http://www.amazon.com/dp/B00GA9HSOG/?tag=poinhairdilb-20)
    
*   [Get The VLOOKUP Book & Video combo pack](http://chandoo.org/wp/resources/the-vlookup-book/ "The VLOOKUP Book")
    

|     |     |
| --- | --- |
| [![The VLOOKUP Book - Definitive guide to Excel lookup functions & tricks](https://img.chandoo.org/f/vw/the-vlookup-definitive-guide-to-excel-lookup-functions.png)](http://chandoo.org/wp/resources/the-vlookup-book/) | **Comprehensive and easy to understand**<br><br>This is a book for everyone who uses Vlookup. Most of us think… Oh.. I already know the function. But this book will open your eyes to some brilliant techniques. – By Dr. Nitin Paranjape<br><br>**Solid introduction to lookup functions**<br><br>This books does a wonderful job of taking each of the lookup functions available in Excel, breaking them down to a simple, easy-to-understand level. – by Lucas Moraga<br><br>[Get your copy](http://chandoo.org/wp/resources/the-vlookup-book/ "The VLOOKUP Book - Definitive guide to Excel lookup functions & tricks") |

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [blank rows](https://chandoo.org/wp/tag/blank-rows/)
    , [goto special](https://chandoo.org/wp/tag/goto-special/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [isblank()](https://chandoo.org/wp/tag/isblank/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [wildcards in excel](https://chandoo.org/wp/tag/wildcards-in-excel/)
    
*   Category: [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousQuickly combine text in multiple cells using this trick! \[Formulas\]](https://chandoo.org/wp/combine-text-values-quick-tip/)

[NextBig trouble in little spreadsheetNext](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/)

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
    
    [Reply](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ