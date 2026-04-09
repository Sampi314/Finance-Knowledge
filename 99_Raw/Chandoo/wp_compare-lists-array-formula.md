# Comparing Lists of Values in Excel using Array Formulas  » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/compare-lists-array-formula

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Comparing Lists of Values in Excel using Array Formulas
=======================================================

*   Last updated on June 14, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week, we had a home work on [Calculating Donation Summaries using Excel Formulas](http://chandoo.org/wp/2011/06/10/amount-donated-vs-pledged-hw/)
. This is a good case where array formulas can help us. So today, we will learn how we can use Array Formulas to compare lists of values and calculate summaries. Towards the end of this post, you can see a video that explains the solution to Donation Summary Calculation problem.

Comparing List of Values – Different Scenarios
----------------------------------------------

There are 2 scenarios when we compare lists of values.

1.  Comparing a list of values with a single value (or condition)
2.  Comparing a list of values against another list (array comparison)

Comparing a list of values with a single value (or condition):
--------------------------------------------------------------

This is the most common and easiest comparison. Examples of this are – count of all values > 20, sum of values between 5 and 23, count of employees in purchasing department etc.

We have built in formulas in Excel to help us do this easily.

|     |     |
| --- | --- |
| **Formula** | **What it does?** |
| COUNTIF | Counts all the values in a range that meet a criteria.  <br>Example: COUNTIF(A1:A10,”>10″)  <br>_Count of all values in A1:A10 more than 10_ <br><br>[Help](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/ "COUNTIF Formula Help") |
| SUMIF | Sums all the values in a range that meet a criteria  <br>Example: SUMIF(A1:A10,”>10″,B1:B10)  <br>_Sum of all values in B1:B10 where corresponding value in A1:A10 is more than 10_ <br><br>[Help](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/ "SUMIF Formula Help") |
| COUNTIFS\* | Counts all the values in a range that meet multiple criterion  <br>Example: COUNTIFS(employees, “a\*”,departments, “Purchasing”)  <br>_Counts the number of employees in Purchasing department whose name starts with letter a._ <br><br>[Help](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/ "COUNTIFS Formula Help") |
| SUMIFS\* | Sums all the values in a range that meet multiple criterion  <br>Example: SUMIFS(salaries, employees, “a\*”,departments, “Purchasing”)  <br>_Sums up the salary of employees in Purchasing department whose name starts with letter a._ <br><br>[Help](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/ "SUMIFS Formula Help") |
| SUMPRODUCT | Gives the sum of product of various lists. This formulas is very robust and can be used to compare lists and check against multiple conditions  <br>Example: SUMPRODUCT(salaries, departments=”Purchasing”, join\_date>datevalue(“1-May-2009”),join\_date<=datevalue(“1-May-2011”))  <br>_Sums up the salary of employees in Purchasing department who joined between 1-May-2009 and 1-May-2011._ <br><br>[Help](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/ "SUMPRODUCT Formula Help") |
| AVERAGEIF\* | Average of all the values in a range that meet a criteria  <br>Example: AVERAGEIF(A1:A10,”>10″,B1:B10)  <br>_Average of all values in B1:B10 where corresponding value in A1:A10 is more than 10_ |
| AVERAGEIFS\* | Average of all the values in a range that meet multiple criteria  <br>Example: AVERAGEIFS(salaries, employees, “a\*”,departments, “Purchasing”)  <br>_Average salary of employees in Purchasing department whose name starts with letter a._ |

\* these formulas do not work in Excel 2003 or earlier versions.

Comparing a list of values with another list (array compare):
-------------------------------------------------------------

This is where it gets interesting. You have 2 lists of values, like in our last week’s problem. And you want to calculate some value, for eg. Sum of all donations where Amount Donated < Amount Pledged.  
How do you go about this?

_**Well, this is where we use Array Formulas.**_

In the above case, assuming we have amount donated in lstGiven and amount pledged in lstPledged,

We can use the array formula =SUM((lstGiven)\*(lstGiven<lstPledged)) to find the sum of all donations such that amount donated is less than amount pledged.  
Note: You must press CTRL+SHIFT+Enter to get this formula work

### How does this formula work?

1.  The formula checks for lstGiven < lstPledged and returns a bunch of TRUE, FALSE values.
2.  When you multiply this with lstGiven, Excel would convert TRUE, FALSE to 1 and 0 and then multiply.
3.  Since 0 multiplied by anything would 0, we end up with a bunch of donation values where donated amount is less than pledged amount.
4.  Once all the values are there, the SUM would just add them up.

More examples & Illustration:
-----------------------------

Look at below image to understand how we can compare lists of values in Excel using Array formulas.

![Array Formulas to Compare Lists in Excel - Examples](https://chandoo.org/img/hw/array-formulas-to-compare-lists.png)

Solution to Donation Summary Calculation Problem:
-------------------------------------------------

I have made a video explaining how you can solve [the last week’s homework](http://chandoo.org/wp/2011/06/10/amount-donated-vs-pledged-hw/)
. See it below or on [our Youtube Channel](http://www.youtube.com/watch?v=RPoFpbM_8Rs&feature=channel_video_title)
.

Download the Excel Workbook for this.
-------------------------------------

**[Click here to download the Workbook with partial solution as shown in the video](https://img.chandoo.org/hw/formula-homework-donations-calculations-part-sol.xls)
.**

[Click here to download the solution workbook](https://img.chandoo.org/hw/formula-homework-donations-calculations-sol.xlsx)
 and play with the formulas to learn more.

Share your tips on Array Formulas
---------------------------------

Array formulas are quite powerful and robust. I use them all the time and love to learn more. _So please share your tips and ideas using comments. Go!_

Learn More about Excel Array Formulas:
--------------------------------------

*   [Advanced SUMPRODUCT Queries in Excel](http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/)
    
*   [Calculating Sum of Digits in a Number](http://chandoo.org/wp/2011/03/18/calculating-sum-of-digits-in-a-number/)
    
*   [Check if a List is sorted or not using Array Formulas](http://chandoo.org/wp/2011/01/07/check-sort-order-of-a-list/)
    
*   [Lookup Second Occurrence of a Value in a List](http://chandoo.org/wp/2010/11/10/vlookup-second-value/)
    
*   [Find the Second Highest Number in a List that Meets a criteria](http://chandoo.org/wp/2010/10/08/large-if-array-formula-tutorial/)
    
*   … [_**More Array Formula Examples & Tutorials**_](http://chandoo.org/wp/tag/array-formulas/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/compare-lists-array-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compare-lists-array-formula/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    , [sumif()](https://chandoo.org/wp/tag/sumif/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousAmount Donated vs. Pledged \[Excel Formula Homework\]](https://chandoo.org/wp/amount-donated-vs-pledged-hw/)

[NextWin Loss Chart from a Series of Win, Loss DataNext](https://chandoo.org/wp/win-loss-chart-improved/)

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
    
    [Reply](https://chandoo.org/wp/compare-lists-array-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compare-lists-array-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compare-lists-array-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ