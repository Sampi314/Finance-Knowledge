# Excel Dynamic Array Functions - What are they, how to use them, Examples and FAQs » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/dynamic-array-functions

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Dynamic Array Functions – What are they, how to use them, Examples and FAQs
=================================================================================

*   Last updated on May 11, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Excel Dynamic Array Functions are a true game changer.** These newly introduced DA functions can filter, sort, remove duplicates and do much more. The output of these functions can go to a range of cells. Hence the name – _**dynamic array functions.**_ 

#### Table of Contents

How Dynamic Array Functions differ from normal functions?
---------------------------------------------------------

*   Normal functions return value in ONE cell, where as DA functions return output to a range of cells
*   New ways to work with data - FILTER, SORT, extract UNIQUE items and generate SEQUENCE of numbers or random values
*   Can be use alone or with existing Excel functions

*   Available in Excel 365 only

What are the newly introduced DA functions?
-------------------------------------------

As of April 2020, Microsoft introduced below 6 new functions under Dynamic Array category.

1.  **FILTER:** to filter a range of cells (or table) based on input criteria
2.  **UNIQUE:** to extract unique items from a a range of cells (or table)
3.  **SORT:** to sort a list by a specified column. 
4.  **SORTBY:** to sort a list by another list
5.  **SEQUENCE:** to generate a sequence of numbers in a range of rows and (or) columns.
6.  **RANDARRAY:** to generate a range of random numbers

**Here is a TLDR version of the Dynamic Array functions.**

![New Excel Dynamic Array functions - explained in one GIF](https://cache.chandoo.org/images/f/dynamic%20array%20functions%20-%20explained%20in%20one%20GIF.gif)

Apart from these new functions, DA capability enables these extra features in Excel.

*   You can use # operator to refer to a range of cells spilled by Dynamic Array functions. For example, if A1 has a DA function that returns 10×1 range (A1:A10), you can refer to this dynamic range by using the reference A1#
*   Most array formulas will now simply spill into a range of cells. No need to press CTRL+SHIFT+Enter.
*   Newly introduced formulas like XLOOKUP can also spill producing an entire row of matching result.
*   Any formula or name that refers to more than one value will automatically spill. For example, if you **type =data in a cell, it will return the entire table** in a spilled range.

Sample Data
-----------

I am using the below Employee data to demonstrate new Dynamic Array functions. This is in a table named “data”.

![sample data - DA functions](https://chandoo.org/wp/wp-content/uploads/2020/04/sample-data-DA-functions.png)

[Download Example Workbook](https://chandoo.org/wp/wp-content/uploads/2020/04/DA-Examples-1.xlsx)

Please go thru below fact sheets to learn more about DA functions.

FILTER() Fact Sheet
-------------------

**What does FILTER() do?**

FILTER() function filters a table or list of data based on conditions.

**Show me a demo of FILTER?**

![Filter dynamic array function - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/filter-function-demo.gif)

**What is the syntax of FILTER function?**

\=FILTER(your data, conditions, _if empty value_)

**Give me few examples of FILTER function?**

Here are a few more examples of FILTER function:

*   FILTER(data, data\[manager\]=”Ian”)  
    Shows all **data** where manager is **Ian.**
*   FILTER(data, (data\[age\]>30)\*(data\[department\]=”Website”))  
    All **data** where age > 30 **AND** department is Website.
*   FILTER(data\[name\], (data\[age\]>30)+(data\[department\]=”Website”))  
    Show **names** where Age > 30 **OR** department is Website.
*   FILTER(data, (data\[Manager\]<>”Ian”)\*(data\[gender\]=”Female”))  
    Show **female staff data** where manager is **NOT** Ian

UNIQUE() Fact Sheet
-------------------

**What does UNIQUE() do?**

UNIQUE() function generates a list of unique items from input. You can use it to remove duplicates from a list.

**Show me a demo of UNIQUE?**

![UNIQUE dynamic array function - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/unique-function-demo.gif)

**What is the syntax of UNIQUE function?**

**Simplified syntax:**

\=UNIQUE(list)

**With options:**

\=UNIQUE(list, _data is across the columns?, do you want values occurring just once?)_

**Give me few examples of UNIQUE function?**

Sure. Here are few more practical examples of UNIQUE function.

*   UNIQUE(data\[department\])  
    List out all department, just one row per department.
*   UNIQUE(FILTER(data\[department\], data\[age\]>30))  
    List out all departments where **staff aged >30 work**.
*   UNIQUE({1;1;2;3;4;4;5;6;7;7;7;8;9;0;0}, FALSE, **TRUE**)  
    Return the numbers that occurred just once – _ie_  {2;3;5;6;8;9}

SORT() Fact Sheet
-----------------

**What does SORT() do?**

SORT() function sorts a list or data by the column number specified in ascending or descending order.

**Show me a demo of SORT?**

![SORT function - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/sort-function-demo.gif)

**What is the syntax of SORT function?**

**Common usage:** 

\=SORT(list)

**With options:**

\=SORT(list, column number, ascending or descending order, do you want to sort across the columns instead?)

**Give me few examples of SORT function?**

Here are a few more examples of SORT function:

*   SORT(data\[name\])  
    Sorts all the names in data in ascending order (the default order)
*   SORT(data, **6**, **\-1**)  
    Sorts all **data** by **salary** (column 6)  in **descending order** (-1)
*   SORT(FILTER(data, data\[manager\]=”Carla”),4)  
    Shows all staff data that report to **Carla** in **ascending order of age** (column 4).

**How does SORT break ties?**

Let’s say you are sorting the staff data by age with the formula SORT(data, 4). In this case, if two employees have same age, then SORT will present them in the order as per original data. So if Bill and Jill both are 19, but they are listed Bill first in data, that is how SORT will show the result too.

**How to use another column to break ties when SORTing?**

In such cases, you can use the next function – **SORTBY.** This accepts multiple criteria to break ties.

SORTBY() Fact Sheet
-------------------

**What does SORTBY() do?**

SORTBY() sorts a list (or table) by a set of criteria lists. You can use this to break ties or defined multi-level sorting criteria (for ex: sort by department and age).

**Show me a demo of SORTBY?**

![SORTBY dynamic array function - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/sortby-function-demo.gif)

**What is the syntax of SORTBY function?**

SORTBY(list, criteria list 1, sort order 1, criteria list 2, sort order 2…)

**Give me few examples of SORTBY  function?**

SORTBY opens up lots of possibilities to analyze and present data in meaningful manner. Here are few real-world scenarios.

*   SORTBY(data, data\[Department\],1, data\[Salary\],-1)  
    Sort **data** by **department** in A-Z order and then **Salary in descending** order.
*   SORTBY(data\[name\], data\[Department\],1, data\[Salary\],-1)  
    Sort data by department in A-Z order and then Salary in descending order, but just show the **names**.
*   SORTBY(data, **data\[Department\]=”HR”**, -1, data\[Name\],1)  
    Shows all employees in HR department on top and rest underneath in alphabetical order. 

SEQUENCE() Fact Sheet
---------------------

**What does SEQUENCE() do?**

SEQUENCE() function generates a sequence of numbers in rows or columns or both. You can use this to make running numbers. While this may not seem _all that helpful,_ SEQUENCE opens up doors for creating elegant and powerful solutions for your data analysis needs.

**Show me a demo of SEQUENCE?**

![SEQUENCE dynamic array function - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/sequence-function-demo.gif)

**What is the syntax of SEQUENCE function?**

**Common usage:** 

\=SEQUENCE(count)

**With options:**

\=SEQUENCE(row count, column count, starting number, step by)

**Give me few examples of SEQUENCE function?**

Here are a few more examples of SEQUENCE function:

*   SEQUENCE(10)  
    Generates numbers 1 to 10 and spills them in to 10 cells.
*   SEQUENCE(100)<=10  
    Generates 100 values, with first 10 as TRUE and others as FALSE
*   FILTER(SORT(data, 6, -1), SEQUENCE(100)<=10)  
    Shows data for top 10 employees by salary. 
*   SORTBY(data, SEQUENCE(100), -1)  
    Prints data in reverse order (by sorting the sequence of 100 numbers in descending order)

RANDARRAY() Fact Sheet
----------------------

**What does RANDARRAY() do?**

RANDARRAY() makes a list of random numbers. Just as SEQUENCE(), RANDARRAY() too doesn’t seem like a useful function, _**until you need it.**_ 

**Show me a demo of RANDARRAY?**

![RANDARRAY dynamic array function demo](https://chandoo.org/wp/wp-content/uploads/2020/04/randarray-function-demo.gif)

**What is the syntax of RANDARRAY function?**

**Common usage:**

RANDARRAY(count)

**With options:**

RANDARRAY(row count, column count, starting number, ending number, do you want just random integers?)

**Give me few examples of RANDARRAY function?**

Here are a few real-world examples of RANDARRAY.

*   RANDARRAY(10,,1,100,TRUE)  
    Generate 10 random integers between 1 to 100
*   UNIQUE(RANDARRAY(10,,1,100,TRUE))  
    Generates 10 random integers between 1 to 100 and removes any duplicates in them.
*   SORTBY(data, RANDARRAY(100))  
    Shuffles the data in random order

How Dynamic Arrays interact with other Excel features?
------------------------------------------------------

DA functions and spill ranges play well with most Excel functionalities. I have made a few notes and comments about individual features below.  

### Spill Ranges in other formulas

**You can refer** to spill ranges (output generated by Dynamic Array functions) **using the # operator**.

For example, let’s say you have a formula in cell B7 to filter all salaries of people reporting to Carla.

You can refer to the entire spilled range in other situations using # operator like this.

*   **SUM(B7#)** – sums up all salaries listed in the cell B7 and down. This formula will automatically adjust if either data or filter conditions change.
*   **AVERAGE(B7#)** – similar to SUM, but calculates average salary
*   **COUNTIFS(B7#, “>100000”)** – counts number of values in the spill range (B7#) greater than $100,000

_**See this illustration to understand how to work with spill ranges in other formulas.**_

![how to use spill ranges in other formulas - Excel illustration](https://chandoo.org/wp/wp-content/uploads/2020/04/spill-ranges-and-other-formulas-illustration.png)

### Named ranges and DA Functions

**You can create named ranges that refer to Spill range.** You can also use named ranges inside DA functions. Everything works just as smoothly.

For example,

1.  We can create a named range called HighPerformers that refers to the formula =FILTER(data, data\[Rating\]>=5). See this illustration.
    
    ![creating a named range with FILTER function](https://chandoo.org/wp/wp-content/uploads/2020/04/creating-a-named-range-with-FILTER-function.png)
    
2.  We can then use this named range in other formulas (or situations). To count number of high performers, we can use =ROWS(HighPerformers)
    
    ![Using Dynamic Array functions with named ranges - demo](https://chandoo.org/wp/wp-content/uploads/2020/04/Using-Dynamic-Array-functions-with-named-ranges-demo.png)
    

When you combine the DA functions with array processing power of INDEX, you can solve some gnarly business problems easily.

[](https://chandoo.org/wp/index-formula-usage-and-tips/)

[Learn more about the versatile INDEX function.](https://chandoo.org/wp/index-formula-usage-and-tips/)

### Conditional Formatting Dynamic Arrays

**As of April 2020, Conditional formatting doesn’t _really_ recognize dynamic spill ranges**. This means, when you create a CF rule to be applied to an entire spill range, even though Excel let’s you enter B7#, it will automatically convert the range to physical address (for eg. $B$7:$B$19). 

So if your data or formula changes, the CF rules won’t automatically extend.

### Dynamic Arrays in Data Validation

**You can use # operator when referring to dynamic array range with data validation rules.**

For example, you can set a data validation drop down list in a cell to show all department names in ascending order using below method:

1.  In an empty cell (say AH6), write the formula =SORT(UNIQUE(data\[Department\]))
2.  Now, select the cell where you want to apply data validation, go to Data > Validation and select the type as List.
3.  Set list source as $AH$6#
4.  You can select departments from your validation list.

See this illustration on how this can be useful.

![data validation rules with dynamic arrays](https://chandoo.org/wp/wp-content/uploads/2020/04/data-validation-rules-with-dynamic-arrays.png)

### Charting & Dynamic Arrays

**As of April 2020, Excel charts do not recognize spill range operators**. This means, when you create a chart from spilled range, it will not automatically extend if the data / formula changes.

Here is a quick demo of this broken chart behavior.

![demo of charts with dynamic array functions](https://chandoo.org/wp/wp-content/uploads/2020/04/demo-of-charts-with-dynamic-array-functions.gif)

Dynamic Array Functions - Full Introduction Video
-------------------------------------------------

I created a detailed video explaining how dynamic array functions work, how to get started and what to do when you get errors. Check out the video below or [visit Chandoo.org youtube channel](https://youtu.be/ONaS7IMKJPM)
.

Dynamic Array Functions - Masterclass
-------------------------------------

I ran a live YouTube stream on Dynamic Array formulas recently. You can watch the video below. This covers all the concepts of Dynamic Arrays in great detail.

Example Workbook
----------------

I made a full example workbook with sample data, several formulas, interaction details and more. Please use below button to download the file.

Note: It will work ONLY if you have Dynamic Array feature in Excel 365. 

[Download Example Workbook](https://chandoo.org/wp/wp-content/uploads/2020/04/DA-Examples-1.xlsx)

Additional Resources on DA Functions
------------------------------------

Please check out below links and videos to learn more about DA functions.

*   [Dynamic Arrays in the traditional Excel world](https://support.microsoft.com/en-us/office/dynamic-array-formulas-in-non-dynamic-aware-excel-696e164e-306b-4282-ae9d-aa88f5502fa2)
     \[Microsoft\]
*   [Overview of Dynamic Array functions](https://www.excelcampus.com/functions/dynamic-array-formulas-spill-ranges/)
     \[Excel Campus\]
*   [Excel Dynamic Arrays – Straight to the point](https://www.mrexcel.com/products/excel-dynamic-arrays-straight-to-the-point-2nd-edition/)
     – Book by Bill Jelen \[MrExcel\]
*   [Joe McDaid, Program Manager at Microsoft Explains the DA functionality](https://www.youtube.com/watch?v=BsUTlhib4Tw)
     – Video
*   Also [learn about XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
     – another cool new function

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/dynamic-array-functions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dynamic-array-functions/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic array functions](https://chandoo.org/wp/tag/dynamic-array-functions/)
    , [FILTER()](https://chandoo.org/wp/tag/filter/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [randarray](https://chandoo.org/wp/tag/randarray/)
    , [sequence](https://chandoo.org/wp/tag/sequence/)
    , [sort](https://chandoo.org/wp/tag/sort/)
    , [sortby](https://chandoo.org/wp/tag/sortby/)
    , [unique](https://chandoo.org/wp/tag/unique/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThere are 20 Easter Eggs in this Workbook](https://chandoo.org/wp/easter-eggs-2020/)

[NextAdd slope line to XY chartsNext](https://chandoo.org/wp/add-slope-line-to-xy-charts/)

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
    
    [Reply](https://chandoo.org/wp/dynamic-array-functions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dynamic-array-functions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dynamic-array-functions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ