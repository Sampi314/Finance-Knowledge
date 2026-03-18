# Clean up Incorrectly Formatted Phone Numbers using Microsoft Excel - Download and use this Free VBA UDF (User Defined Function)

**Source:** https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel

---

*   [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Clean up Incorrectly Formatted Phone Numbers using Excel
========================================================

*   Last updated on September 30, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![cleanup-phone-numbers-using-excel-howto](https://chandoo.org/wp/wp-content/uploads/2008/09/cleanup-phone-numbers-using-excel-howto.png "cleanup-phone-numbers-using-excel-howto")In our Utopian imaginations all the data would have been standardized and shareable across systems and people. But alas, the reality is totally different. We seldom get data in the format / way we desire it to be. In other words, the ingredients are all there, but for us to prepare the dinner, you must pre-process them.

**Often this pre-processing or cleaning up the data takes quite an amount of time it self leaving very little to do the actual work.** That is when you can use excel’s powerful data cleaning techniques to handle the situations.

One common problem with corporate data is incorrectly formatted phone numbers. Most of us are used to a standard 10 digit phone number format like 123-123-1234 or (123) 123 1234, but when you get that customer data, very few phone numbers in it are formatted like above. Instead you might see phone numbers like 1231231234, 12312 31234, (123)123-1234 etc.

It is not really difficult to clean up the phone numbers if we know before hand how they are formatted. For eg. **you can easily convert a phone number like 1231231234 to 123-123-1234 using excel text formatting functions like `=TEXT(1231231234,"000-000-0000")`.** But it is a rare case in which we have control over the incoming format and quickly you will have to use a slew of format / text processing functions to clean up the data.

To simplify the whole thing, I have written **a small VBA UDF** (User Defined Function) which you can add to your excel add-ins list and use **to clean up virtually any phone number format to standard phone number.**

Function cleanPhoneNumber(thisNumber As String) As String
    ' this function aspires to clean any phone number format
    ' to standard format (+9999) 999-999-9999 or 999-999-9999
    ' works with almost all phone number formats stored in text

Dim retNumber As String

For i = 1 To Len(thisNumber)
    If Asc(Mid(thisNumber, i, 1)) >= Asc("0") And Asc(Mid(thisNumber, i, 1)) <= Asc("9") Then
        retNumber = retNumber + Mid(thisNumber, i, 1)
    End If
Next
If Len(retNumber) > 10 Then
    ' format for country code as well
    cleanPhoneNumber = Format(retNumber, "(+#) 000-000-0000")
Else
    cleanPhoneNumber = Format(retNumber, "000-000-0000")
End If
End Function

The above function is pretty straight forward and simple. It scans the input text for any numeric ASCII codes and saves them to another text field. Once the scanning is complete the function will format the final number to 999-999-9999 format if the number has 10 or less digits, otherwise to (+9999) 999-999-9999 format (with country code).

**Like this? Learn these other data cleaning / processing tips:**

[Handling spelling mistakes in your data](http://chandoo.org/wp/2008/09/25/handling-spelling-mistakes-in-excel-fuzzy-search/)
  
[Splitting text using excel formulas](http://chandoo.org/wp/2008/09/08/split-text-excel-functions/)
  
[Generating initials from names using excel](http://chandoo.org/wp/2008/09/02/get-initials-from-name-excel-formula/)
  
[Adding a range of cells using Concat()](http://chandoo.org/wp/2008/05/28/how-to-add-a-range-of-cells-in-excel-concat/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [66 Comments](https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel/#respond)
    
*   Tagged under [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [data](https://chandoo.org/wp/tag/data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel add-ins](https://chandoo.org/wp/tag/excel-add-ins/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [productivity](https://chandoo.org/wp/tag/productivity/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to WOW your customers with tracking – Dominos pizza example](https://chandoo.org/wp/dominos-pizza-wow-tracking/)

[NextSimple Todo List application using Excel – Download and become productiveNext](https://chandoo.org/wp/simple-todo-list-using-excel/)

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
    
    [Reply](https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/clean-up-incorrectly-formatted-phone-numbers-using-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ