# 6 Essential TEXT functions in Excel with 6 Everyday Examples » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/important-text-functions

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

6 Essential TEXT functions in Excel with 6 Everyday Examples
============================================================

*   Last updated on June 14, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel text functions are useful for cleaning up text / alphanumeric values, extracting parts of cell and presenting combined results in output pages. In this article, learn the most important TEXT Functions in Excel with 6 everyday examples.

![6 important Excel text functions](https://chandoo.org/wp/wp-content/uploads/2021/06/6excel-text-functions.jpg)

The 6 Important Text Functions
------------------------------

### LEFT Function

Use LEFT function to extract portion of text from left.  
  
**Examples:**

\=LEFT(“Chandoo”, 2) will be Ch  
\=LEFT(A1, 4) will be first 4 letters of A1 value

### RIGHT Function

Use RIGHT function to extract portion of text from right.

**Examples:**

\=RIGHT(“Chandoo”, 2) will be oo  
\=RIGHT(LEFT(A1, 4),2) will be two letters from the middle, starting from 3rd letter of A1.

### MID Function

Use MID function to extract portion of text from middle, from a specified starting point.

**Examples:**

\=MID(“Chandoo”, 5, 2) will be do  
\=MID(“Chandoo”, 4, 99) will be doo

### LEN Function

LEN function measures the length of a text in number of characters.

**Examples:**

\=LEN(“Chandoo”) will be 7  
\=LEN(A1) will be the length of contents in A1. If A1 is empty, this will be 0.

### FIND Function

Find the starting position of a text in another text using FIND function.

**Examples:**

\=FIND(“do”, “Chandoo”) will be 5

\=FIND(“DO”, “Chandoo”) will be error as find is a case-sensitive function

\=SEARCH(“DO”, “Chandoo”) will be 5. 

### TEXTJOIN Function

Combine (concatenate) a bunch of values with a specified delimiter.

**Examples:**

\=TEXTJOIN(“,”,FALSE, “Chandoo”,”Jon”,”Mike”) will be Chandoo,Jon,Mike

\=TEXTJOIN(” “, **TRUE**, A1:A10) will combine all non-empty values  in range A1:A10 with space as delimiter.

[Learn more about TEXTJOIN function](https://chandoo.org/wp/textjoin-examples/)
.

The 6 Everyday Examples
-----------------------

Now that you know the 6 important functions, let’s see them applied in 6 everyday situations.

For the purpose of these examples, we will use below sample tabular data & structural references.![text-functions-sample-data](https://chandoo.org/wp/wp-content/uploads/2021/06/text-functions-sample-data.png)

### 1) Gender code (M for male, F for female)

Use the formula =LEFT(\[@Gender\], 1) to get make the gender letter code.

### 2) Extract first name from name

Use the formula =LEFT(\[@Name\],FIND(” “,\[@Name\])-1) to get the first name.

FIND gets the position of space, left gets everything before that.

### 3) Extract last name from name

Try the formula =MID(\[@Name\],FIND(” “,\[@Name\])+1,99) to get the last name.

FIND gets the position of space, mid  gets everything after that.

### 4) Print name in Last name, First name format

The formula =MID(\[@Name\],  
FIND(” “,\[@Name\])+1,99)  
&”, “&LEFT(\[@Name\],FIND(” “,\[@Name\])-1)  
will convert value in Name column to last name, first name format.

It is a combination of the formulas shown in 2 & 3.

### 5) Combine all male staff names in to one cell

The formula =TEXTJOIN(“, “,TRUE, IF(staff\[Gender\]=”Male”, staff\[Name\],””))  
will return all male staff names in the table staff.

The IF formula generates a list of all male names or blanks. TEXTJOIN ignores the blanks (second parameter is TRUE) and combines the values with a comma as separator.

### 6) Word count of a sentence

Assuming you have sentence in cell D6, the formula

\=LEN(D6)-LEN(SUBSTITUTE(D6,” “,””))+1

will tell you its word count. 

The SUBSTITUTE formula removes any spaces (by subbing them with nothing) and LEN is used to measure the length.

Download the sample file
------------------------

[**Click here to download the sample file**](https://chandoo.org/wp/wp-content/uploads/2021/06/6-TEXT-functions.xlsx)
 and practice these functions.

Important Text Functions in Excel Video
---------------------------------------

If you want a video guide that explains these functions in detail, check it out below or _find_ it [on my YouTube channel](https://youtu.be/thvE8Eg-Pqg)
.

Need a text function? Tell me in comments
-----------------------------------------

Are you trying to make formula to get something done with text in Excel? Let me know in comments what you need and I will try to help.

Also, if you have a favorite Excel text formula trick or patterns, share it so we all learn from each other.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/important-text-functions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/important-text-functions/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)
    , [left](https://chandoo.org/wp/tag/left-2/)
    , [mid](https://chandoo.org/wp/tag/mid-2/)
    , [right()](https://chandoo.org/wp/tag/right/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    , [Textjoin()](https://chandoo.org/wp/tag/textjoin/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

[NextGetting Started with Power BI – Sales Dashboard in one hourNext](https://chandoo.org/wp/powerbi-intro-free-live-event/)

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
    
    [Reply](https://chandoo.org/wp/important-text-functions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/important-text-functions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/important-text-functions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ