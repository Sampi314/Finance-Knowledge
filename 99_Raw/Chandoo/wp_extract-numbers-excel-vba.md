# Extract Numbers from Text using Excel VBA - How to?

**Source:** https://chandoo.org/wp/extract-numbers-excel-vba

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Extract Numbers from Text using Excel VBA \[Video\]
===================================================

*   Last updated on June 26, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week we discussed [how to extract numbers from text](http://chandoo.org/wp/2012/06/19/extract-numbers-from-text-excel/)
 in Excel using formulas. In comments, quite a few people suggested that using VBA (Macros) to extract numbers would be simpler.

**So today, lets learn how to write a VBA Function to extract numbers from any text**.

![Extract numbers from text using Excel VBA](https://img.chandoo.org/vba/extract-numbers-from-text-using-excel-vba.png "Extract numbers from text using Excel VBA")

Using VBA Function to Extract Numbers from Text in Excel
--------------------------------------------------------

When using VBA to scan a text for number, the basic approach is like this:

1.  Read each character in a given text
2.  See if it is number

1.  If so, extract it

4.  Continue with next character
5.  Convert the extracted characters to a number
6.  Return that number

_While this works fine, it also has some limitations._

For example, with above approach, A text value like “US $313,00.00”  will be extracted as _**3,130,000 not as 31,300.00**_

Depending on your data, you may have many such peculiarities. For example, here are 4 situations I ran in to:

![Extracting numbers from text using VBA - various situations](https://img.chandoo.org/vba/extract-numbers-using-vba-scenarios.png "Extracting numbers from text using VBA - various situations")

Handling decimal points & thousand separators during extraction
---------------------------------------------------------------

When it comes to decimal points & thousand separators there are 2 conventions:

1.  61,000.30 (Regular)
2.  61.000,30 (European)

We do not need special treatment for regular format (61,000.30) as Excel & VBA are capable of dealing with these numbers by default.

To check if a text has European format number, we have to see if . occurs before ,

(Note: this method is not fool-proof, but should work well for most situations)

This can be done by using LIKE statement,

`if text like "*.*,*" then   european = true   else   european = false   end if`

Writing our getNumber() VBA Function
------------------------------------

Once we put all these ideas together, we will have our getNumber() function. Watch below video to understand how to extract numbers from text using Excel VBA.

\[[Watch this video on our Youtube channel](http://www.youtube.com/watch?v=U1rD9gajClk)\
\]

Download Number Extraction VBA Function
---------------------------------------

[**Click here to download the Extract Numbers using VBA workbook**](https://img.chandoo.org/vba/extracting%20numbers.xlsm)
.

View code module to understand how getNumber function works.

Do you use VBA to extract numbers?
----------------------------------

I often use VBA to clean raw data. Earlier I mentioned about [cleaning phone numbers](http://chandoo.org/wp/2008/09/30/clean-up-incorrectly-formatted-phone-numbers-using-excel/)
 & [spelling mistakes](http://chandoo.org/wp/2008/09/25/handling-spelling-mistakes-in-excel-fuzzy-search/ "Handling Spelling Mistakes using Excel Fuzzy Search")
. I think simple functions like getNumber() can save us tons of time & let us focus on the important task – analyzing data.

_**What about you?**_ Do you use VBA to clean data? What techniques & ideas you rely on? **Please share your thoughts using comments.**

New to Excel VBA? Take our crash course
---------------------------------------

Are you new to Excel VBA? If so, go thru below links to take our FREE VBA Crash course.

1.  [What is VBA & Writing your First VBA Macro in Excel](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
2.  [Understanding Variables, Conditions & Loops in VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)
    
3.  [Using Cells, Ranges & Other Objects in your Macros](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/)
    
4.  [Putting it all together – Your First VBA Application using Excel](http://chandoo.org/wp/2011/09/02/excel-vba-demo-application/)
    
5.  [My Top 10 Tips for Mastering VBA & Excel Macros](http://chandoo.org/wp/2011/09/06/top-10-tips-for-excel-vba/)
    

### If you want more,

I know you are thirsty for more. Why not join our Online VBA Classes and learn Excel VBA in step-by-step manner. [**Click here to know more**](http://chandoo.org/wp/vba-classes/ "Online VBA & Excel Macro Classes from Chandoo.org")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [32 Comments](https://chandoo.org/wp/extract-numbers-excel-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-numbers-excel-vba/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [if then statement](https://chandoo.org/wp/tag/if-then-statement/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [like statement](https://chandoo.org/wp/tag/like-statement/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousVisualize Excel Salary Data & You could win XBOX 360 + Kinect Bundle \[Contest\]](https://chandoo.org/wp/excel-salary-data-contest/)

[NextCheck if a list has duplicate numbers \[Quick tip\]Next](https://chandoo.org/wp/check-list-for-duplicate-numbers/)

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
    
    [Reply](https://chandoo.org/wp/extract-numbers-excel-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-numbers-excel-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-numbers-excel-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ