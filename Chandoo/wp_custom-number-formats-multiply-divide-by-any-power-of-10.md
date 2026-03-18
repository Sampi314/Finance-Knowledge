# Custom Number Formats (Multiply & Divide by any Power of 10)

**Source:** https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Custom Number Formats (Multiply & Divide by any Power of 10)
============================================================

*   Last updated on January 31, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In the past here at Chandoo.org and at many many other sites, people have asked the question “_How can I display a number **Multiplied** or **Divided** by 10, 100, 1000, 1000000 etc, but still have the cell maintain the original number for use in subsequent calculations_“.

Typically the answer has been limited to “_It can’t be done_” or “_It can only be done in multiples of 1000_”.

Well thanks to a tip I picked up from **Kyle** who responded to a [post](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/#comment-219751 "Post")
 here at **Chandoo.org** they are all wrong.

It is possible to Multiply or Divide any cell contents by any power of 10 using Custom Number Formats !

That is:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF1.png "CF1")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF1.png)

How does this work:
-------------------

When using custom number format we have two possibilities to modify the display number

1.  Use a Comma to divide by 1000; or
2.  Use a % to Multiply by 100

So using a combination of these any power of 10 can be obtained.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF2.png "CF2")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF2.png)

So using the correct combination of **,** and **%** can result in any power of 10 multiplier we require.

The problem is that using a **%** adds a **%** to the number!

The trick which Kyle added is that adding a **Ctrl J** to the Custom Number format allows us to hide the **%** signs on a second row of text, then by adjusting the cell to have word wrap and adjusting the row height the second row is not visible.

The **Ctrl J** must be added after the **,**’s and before the **%**’s

So using the examples above the table is:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF3.png "CF3")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF3.png)

The **Ctrl J** adds a Carriage Return, chr(10), to the Format String.

Finally after applying the Custom Number Format the Cell must be edited to enable **Word Wrap**.

Select the Cells with the custom Formats, **Ctrl 1, Alignment**

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF4.png "CF4")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF4.png)

You can see the hidden **%** symbols if you increase the Row Height.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF8.png "CF8")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF8.png)

Combination with Regular Custom Formats
---------------------------------------

These Custom Number Formats can of course still be combined with regular Custom Number Formats, just make sure that the Ctrl J is inserted before the % signs:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF5.png "CF5")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF5.png)

No Loss of the Cells Value
--------------------------

It is also worth noting that the original number is still maintained internally in the cell and that cells dependent on the cells don’t have to adjust for the display value.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF6.png "CF6")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF6.png)

**Multi Line Formats**
----------------------

By extension we can now use this technique to add multiple Lines of Text to a Custom Number Format

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CF7.png "CF7")](https://chandoo.org/wp/wp-content/uploads/2012/01/CF7.png)

Downloads
---------

You can download a file containing all the above example here: [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Custom-Number-Formats.xls "Custom Number Formats")

Other Links to Custom Number Formats
------------------------------------

Here:
-----

[http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/ "http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/")

[http://chandoo.org/wp/2011/11/02/a-technique-to-quickly-develop-custom-number-formats/](http://chandoo.org/wp/2011/11/02/a-technique-to-quickly-develop-custom-number-formats/ "http://chandoo.org/wp/2011/11/02/a-technique-to-quickly-develop-custom-number-formats/")

[http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/](http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/ "http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/")

[http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/](http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/ "http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/")

[http://chandoo.org/wp/tag/custom-cell-formatting/](http://chandoo.org/wp/tag/custom-cell-formatting/ "http://chandoo.org/wp/tag/custom-cell-formatting/")

### Elsewhere

[http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm "http://www.ozgrid.com/Excel/CustomFormats.htm")

[http://peltiertech.com/Excel/NumberFormats.html](http://peltiertech.com/Excel/NumberFormats.html "http://peltiertech.com/Excel/NumberFormats.html")

Thanx
-----

Just a quick final Thank You to **Kyle** for highlighting this Custom Number Format feature/trick last week

I look forward to your comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [61 Comments](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/#respond)
    
*   Tagged under [Custom Number Format](https://chandoo.org/wp/tag/custom-number-format/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousExcel Links – Live from Bangkok Edition](https://chandoo.org/wp/excel-links-live-from-bangkok-edition/)

[NextFormula Forensics No. 010 Count How Many Times a List of Values Occurs in a RangeNext](https://chandoo.org/wp/formula-forensics-no-010/)

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
    
    [Reply](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/custom-number-formats-multiply-divide-by-any-power-of-10/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ