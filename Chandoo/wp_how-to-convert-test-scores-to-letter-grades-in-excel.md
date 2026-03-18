# Calculate Letter Grades (A+ or F) from Test Scores with Excel

**Source:** https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to convert test scores to letter grades in Excel?
=====================================================

*   Last updated on March 20, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We can use Excel’s LOOKUP function to quickly convert exam or test scores to letter grades like A+ or F. In this article, let me explain the process and necessary formulas. I will also share a technique to calculate letter grades from test scores using _percentiles._

![how to convert test scores to letter grades using Excel formulas?](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0057.png)

Step 1: Set up a Mapping Table for Letter Grade & Scores
--------------------------------------------------------

In your workbook, set up a mapping (or lookup) table like this to map out each of the letter grades to the test score boundary.

![example letter grade mapping table](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0061.png)

*   When setting up the mapping table, make sure to start from lower score to higher score (for ex: 0 to 100)
*   For each grade, just specify the lower boundary value. So for example, Grade F begins from 0, Grade B- begins from 65

Step 2: Calculate the letter grades using LOOKUP function
---------------------------------------------------------

![LOOKUP function to calculate the letter grade](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0056.png)

For this you need all the test scores for your students. Let’s say you have the test scores in column C, from cell C4. In an adjacent column, you can calculate the letter grade using the below LOOKUP formula.

    =LOOKUP(C4,$G$6:$G$16,$F$6:$F$16)

In this formula:

*   First value (C4) refers to the score for which you need the letter grade
*   Second value ($G$6:$G16) is the “scores from” column of your mapping table set up in Step 1.
*   Third value ($F$6:$F$16) is the “letter grade” column of your mapping table.

Once you have a result for the first test score, drag the formula down to see letter grades for all students.

How to get Letter Grades from Percentiles (relative grading)
------------------------------------------------------------

Sometimes you may want to calculate the letter grade from the percentile of the test score. This sort of thing is also called relative grading (RG). To do this, we can use the PERCENTILERANK functions of Excel.

Here is a 3 Step process for that:

### Step 1: Set up a percentile-wise mapping table for letter grades

In your worksheet, set up a mapping table for letter grades like this:

![mapping table for percentile based letter grades](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0058.png)

### Step 2: Calculate the Percentiles for each test score

![percentile calculation formula](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0059.png)

Let’s say you have test scores in column C, in the range C4:C43.

In column D, write the formula \=PERCENTRANK.INC($C$4:$C$43,C4) to calculate the percentile of test score in first cell against all scores. The result of this would be a percentile from 0% to 100% (both inclusive).

When you get the result for first cell, drag the formula down to fill up the rest.

**Tip:** If you want to calculate the percentile by excluding 0th and 100th percentiles, use the PERCENTILE.EXC function instead.

### Step 3: Convert Percentiles to Letter Grade

![letter grades (A+ to F) from percentile exam scores](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0060.png)

For this, we can use the LOOKUP function again. In column E use the below function:

    =LOOKUP(D4,$H$6:$H$16,$G$6:$G$16)

In the above formula:

*   First value (D4) refers to the percentile we calculated in step 2.
*   Second value ($H$6:$H16) is the “percentile from” column of your mapping table set up in Step 1.
*   Third value ($G$6:$G$16) is the “letter grade” column of your mapping table.

Download Test Score to Letter Grade Calculation Template
--------------------------------------------------------

I made a quick Excel template to calculate letter grades from your test / exam marks. Just plug-in your values and see the results instantly. **[Download the template here.](https://chandoo.org/wp/wp-content/uploads/2024/03/letter-grade-calculator.xlsx)
**

Bonus: These formulas work in Google Sheets too!
------------------------------------------------

That is right. All these formulas will work exactly same with Google sheets too. [Here is a Google Sheets template](https://docs.google.com/spreadsheets/d/1LySEIeAHR1MtsodF6Mwit9zupoZZjHssNKYTG4OwPck/edit?usp=sharing)
 if you need some help.

Things to keep in mind when calculating letter grades
-----------------------------------------------------

Do take these cautions when calculating alphabetic letter grades from your exam marks.

*   **Mapping table setup:** your letter grade mapping table needs to be from lowest marks / scores to highest. Just specify the lower boundary for each letter grade.
    *   For example, if grade F is from exam score 0 to 35, then write 0.
    *   If grade B+ is from 80 to 85, then write 80
*   **Clean up your data:** If your test score data has missing values (for example, absent or hyphens) then the LOOKUP formula will give #N/A error. So clean up your data before you apply the LOOKUP function.

Next steps:
-----------

Now that you have calculated the letter grades, you may want to see the distribution of your student grades or understand which students are failing and need help. Use below Excel concepts & resources to do that.

*   [Understand the distribution of your data in Excel](https://chandoo.org/wp/statistical-distributions/)
    
*   [Create a histogram in Excel](https://chandoo.org/wp/histograms-pareto-charts-in-excel/)
    
*   [Using conditional formatting in Excel to highlight top 10 values](https://chandoo.org/wp/highlight-top-10-values-conditional-formatting/)
    
*   [How to use Excel Pivot Tables to understand and explore your data](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [lookup](https://chandoo.org/wp/tag/lookup/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [teachers](https://chandoo.org/wp/tag/teachers/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to calculate the Gender Pay Gap using Excel Formulas? (Free Calculator Template)](https://chandoo.org/wp/gender-pay-gap-calculator/)

[NextCompound Interest Formula in ExcelNext](https://chandoo.org/wp/compound-interest-formula-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ