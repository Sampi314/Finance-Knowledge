# A technique for developing Custom Number Formats in Excel

**Source:** https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

A Technique to Quickly Develop Custom Number Formats
====================================================

*   Last updated on November 4, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In the past Chandoo has written about custom Number Formats for cells:

[http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/ "Custom cell formatting")

[http://chandoo.org/wp/tag/custom-cell-formatting/](http://chandoo.org/wp/tag/custom-cell-formatting/ "Custom Cell Formatting")

and I have written about Custom Number Formats for Charts:

[http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/](http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/ "Selective Custom Formatting")

[http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/](http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/ "Selective Custom Formatting 2")

This post examines a technique for quickly developing Custom Number Formats for Cells, Charts or any other Number location in Excel.

A Technique for Quickly Developing Custom Number Formats
--------------------------------------------------------

Instead of Selecting the cell, chart axis etc, **Ctrl 1, Format Cells/Properties, Number Tab, Custom** and then entering a Custom Format and Apply, only to find out that the format is incorrect, try this simple technique below.

### **1\.** **Enter a few Numbers in 3 cells**

Enter 3 numbers, a positive, zero and negative which have values you will expect to receive in your model.

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat1.png "CustomFormat1")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat1.png)

### **2\.** **Add a Custom Format Cell**

In D3 I have entered **##,;-(##,);”Zero”**

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat2.png "CustomFormat2")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat2.png)

### **3\. Display Numbers using the custom Format**

Each Number to a display cell with a simple **\=Text(B3,$D$3)**

Copy down

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat3.png "CustomFormat3")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat3.png)

This will display the 3 numbers using the Custom Format in Cell D3

### **4\.** **Develop Your Custom Format**

Play around with your own Custom Number Formats to your hearts content

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat4.png "CustomFormat4")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat4.png)

### **5\.** **Use your new format**

Once you have completed your new Custom Number Format, copy the cell contents of D3 in this case.

Select your cells/or other Excel Numbers,

**Ctrl 1,**

**Format Cells/Properties,**

**Number Tab, Custom**

Enter the Custom Format and Apply.

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat5.png "CustomFormat5")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat5.png)

### **6.** Extending the Technique

This technique can be extended by adding several more rows with a larger range of values.

The values are all evaluated at the same time

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat7.png "CustomFormat7")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat7.png)

### **LIMITATIONS**

The above technique does not show the effects of the Color Modifiers in the test cells

[![](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat6.png "CustomFormat6")](https://chandoo.org/wp/wp-content/uploads/2011/10/CustomFormat6.png)

But I think it is a safe bet that you will understand what the Modifier \[Red\] will do

There are also reserved characters such as **E**

So in the above example if I had used **Zero** instead of **“Zero”**

It would have displayed **Ze1900ro**, where the E in Zero is taken as 10^x and x=0 so Excel interprets e as 0 or 1900, a date?

You can avoid this by using the code **“Zero”** or **Z\\ero**

DOWNLOAD
--------

You can download the worked [Example File](https://chandoo.org/wp/wp-content/uploads/2011/10/Quick-Custom-Number-Formats.xls "Sample File")
 used above.

**NUMBER FORMATS**
------------------

For more on Number Formats check out the above links or those below:

[http://www.ozgrid.com/Excel/excel-custom-number-formats.htm](http://www.ozgrid.com/Excel/excel-custom-number-formats.htm)

[http://www.ozgrid.com/Excel/CustomFormats.htm](http://www.ozgrid.com/Excel/CustomFormats.htm)

[http://peltiertech.com/Excel/NumberFormats.html](http://peltiertech.com/Excel/NumberFormats.html)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/#respond)
    
*   Tagged under [Custom Number Format](https://chandoo.org/wp/tag/custom-number-format/)
    , [text()](https://chandoo.org/wp/tag/text/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousUsing an Array Formula to Find and Count the Maximum Text Occurrences in a Range](https://chandoo.org/wp/using-array-formulas-to-find-count/)

[NextFancy Posts – using HTML Display Codes in Chandoo.org PostsNext](https://chandoo.org/wp/fancy-posts-using-html-display-codes/)

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
    
    [Reply](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ