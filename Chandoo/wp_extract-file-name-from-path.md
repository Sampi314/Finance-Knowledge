# Even faster ways to Extract file name from path [quick tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-file-name-from-path

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Even faster ways to Extract file name from path \[quick tip\]
=============================================================

*   Last updated on October 25, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

The best thing about Excel is that _you can do the same thing in several ways._ Our yesterdays problem – **[Extracting file name from full path](http://chandoo.org/wp/2012/10/23/extract-file-name-from-full-path-using-formulas/ "Extract file name from full path using formulas")
** is no different. There are many different ways to do it, apart from writing a formula. Learn these techniques to be a data extraction ninja.

1\. Using Find Replace
----------------------

Suggested by Iain in the comments yesterday, I love this technique for its simplicity and awesomeness.

1.  Select all the file paths
2.  Press CTRL+H
3.  Type \*\\ in find field
4.  Leave the replace field empty.
5.  Click on Replace all.
6.  Done!

It is that simple. Do not believe me? See this demo.

![Extract file name from full path using find replace - Excel tip](https://img.chandoo.org/f/extract-by-find-replace-demo.gif "Extract file name from full path using find replace - Excel tip")

_Thanks Iain for teaching us this trick._

2\. Using Text to columns utility
---------------------------------

Buried inside heap of features in Excel is this beautiful Text to columns utility, that can take any text and convert it in to many columns based on the delimiter you specify. \[[more uses of text to columns](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)\
\]

This is how we can use it:

1.  Select all the file path cells
2.  Go to Data > Text to columns
3.  Chose “Delimited” in step 1 and click next.
4.  Specify delimiter as \\![Text to columns settings for extracting file name from full path - Excel](https://img.chandoo.org/f/text-to-columns-settings.png "Text to columns settings for extracting file name from full path - Excel")
5.  Click Finish
6.  You will get all folders in to separate cells and file name in last cell.
7.  Now use a formula like =INDEX($C3:$O3,COUNTA($C3:$O3)) to extract the last cell’s value _ie_ file name
8.  Done!

![Extracting file name from path using text to columns utility and formulas - how to?](https://img.chandoo.org/f/extract-file-names-from-path-using-text-to-columns-how-to.png)

3\. Using UDFs
--------------

While our formula method tends to be very long or very complicated, we can use 1-2 line VBA to get the file name from a full path. There are many ways to skin this cat in VBA, but 2 easiest methods are,

For both methods below, you first need to insert a new module and add the code in that.

### Using InStrRev

As suggested by Daniel Ferry in the comments.

`Public Function ParseFile(sPath As String) As Variant   ParseFile = Array(Mid$(sPath, 1 + InStrRev(sPath, “\”)), Mid$(sPath, 1 + InStrRev(sPath, “.”)))   End Function`

Note: this UDF returns an array for file name & extension. So you need to enter it in 2 cells together.

The InStrRev() built in function searches for \\ in the sPath from end and returns the first occurrence’s position.

### Using split

As suggested by PPH in comments,  
`   Function ExtractFileName(filepath) As String`

`   Dim x As Variant   x = Split(filepath, Application.PathSeparator)   ExtractFileName = x(UBound(x))   `

`End Function`

What is your favorite method?
-----------------------------

For most of my data cleaning needs, I use a mix of text to columns, find-replace or VBA. In rare cases, I rely on a formula. This is because data cleaning or extraction is usually one time step and figuring out a complex formula is not good idea in such cases.

**What about you?** How do you go about extracting filenames, dates, numbers etc. buried in text? What method do you use often? _**Please share with us in comments.**_

More tips on Data Extraction:
-----------------------------

*   [Extract numbers from text using formulas](http://chandoo.org/wp/2012/06/19/extract-numbers-from-text-excel/)
     \[[and using macros](http://chandoo.org/wp/2012/06/26/extract-numbers-excel-vba/)\
    \]
*   [Extract dates from text with formulas](http://chandoo.org/wp/2012/08/17/extract-dates-from-text/)
     & [with text to columns](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    
*   [Extract user names from email addresses](http://chandoo.org/wp/2010/01/19/usernames-from-email-formulas/)
    
*   [Extract duplicates or unique values from a list](http://chandoo.org/wp/2008/11/06/unique-duplicate-missing-items-excel-help/)
    
*   [Extract data from multiple files & place in one sheet](http://chandoo.org/wp/2012/04/09/consolidate-data-from-different-excel-files-vba/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/extract-file-name-from-path/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-file-name-from-path/#respond)
    
*   Tagged under [find replace](https://chandoo.org/wp/tag/find-replace/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [split](https://chandoo.org/wp/tag/split/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    , [text to columns](https://chandoo.org/wp/tag/text-to-columns/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    , [wildcards in excel](https://chandoo.org/wp/tag/wildcards-in-excel/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExtract file name from full path using formulas](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/)

[NextDesigning a Project Portfolio Dashboard \[Part 1 of 2\]Next](https://chandoo.org/wp/design-project-portfolio-dashboard/)

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
    
    [Reply](https://chandoo.org/wp/extract-file-name-from-path/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-file-name-from-path/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-file-name-from-path/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ