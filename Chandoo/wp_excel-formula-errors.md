# Got an Excel formula error? Here is how you can fix it - Chandoo.org

**Source:** https://chandoo.org/wp/excel-formula-errors

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Formula Errors – Understand and Debug Them
================================================

*   Last updated on June 27, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Excel formula error checklist and how to fix excel errors](https://chandoo.org/wp/wp-content/uploads/2018/06/excel-error.png)Imagine carefully creating a workbook with several calculations and formulas only see errors. **What to do when you get an Excel formula error?** Of course, you can shake your head and ask, “Why, why would you do that?”, but that will not help.

![What to do when you have an Excel error like #NA or #REF](https://chandoo.org/wp/wp-content/uploads/2018/06/why-would-you-do-that.gif)

So in this article let’s **learn how to fix Excel formula error**. Those annoying #SOMETHING!s that you see when your [excel formulas](https://chandoo.org/wp/excel-formula-list/)
 have something wrong with them.

Excel Formula Error Checklist
-----------------------------

Use this checklist to quickly understand common formula errors, what they mean, when you would see them and how to fix them. Read on to know more about the errors.

| Error | What it means? | Most common reason | How to fix it? |
| --- | --- | --- | --- |
| #N/A | Not Applicable | When VLLOKUP can't find what you want | Make sure your list has the value you are looking for. Use IFERROR or IFNA to fix |
| #DIV/0! | Divide by Zero | Denominator is zero | Use IF formula to safe divide |
| #NAME? | Could not find the name | Spelling mistake / typo | Double check your formula and fix the error |
| ######### | Could not display or format | Cell too small | Adjust column width |
| #VALUE! | Invalid value | Converting non-dates or numbers | Make sure your dates are correctly formatted |
| #REF! | Reference missing | When you delete a row / column / cell | Check cell dependancies before deleting |
| #NUM! | Invalid number | Number too high or too low | Check your calculation |
| #NULL! | Missing or null value | Reference points to nothing | See if your references are right |

### #N/A Formula Error

This is one of the most frequent excel formula error you see while [using vlookup formula](https://chandoo.org/wp/vlookup-excel-formula/)
. The N/A error is shown when some data is missing, or inappropriate arguments are passed to the lookup functions (vlookup, hlookup etc.) of if the list is not sorted and you are trying to lookup using sort option. You can also generate a #N/A error by writing =NA() in a cell.

**How to fix #N/A error?**

Make sure you wrap the lookup functions with some error handling mechanism. For eg. if you are not sure the value you are looking is available, you can write something like =IFERROR(VLOOKUP(…), “Value not found”). This will print “value not found” whenever the vlookup returns any error (including #N/A)

Related: [Learn more about IFERROR formula](https://chandoo.org/wp/iferror-formula/)

### #DIV/0! Formula Error

This is the easiest of all. When you divide something with 0, you see this error. For eg. a cell with the formula =23/0 would return in this error.

**How to fix #DIV/0 error?**

Simple, use IF formula to safe divide, like this:

\=IF(A2=0, “”, A1/A2)

### #NAME? Formula Error

The most common reason why you see this error is because you misspelled a formula or table or named range. For eg. if you write =summa(a1:a10) in a cell, it would return #NAME? error. There are few other reasons why this can happen. If you forget to close a text in double quotes or omit the range operator :. All these examples should return #NAME? error. =sum(range1, UNDEFIED\_RANGE\_NAME), =sum(a1a10)

**How to fix #NAME? Error?**

*   Make sure you have mentioned the correct formula name. Use auto-complete when typing formulas. This way, when you type formulas or use names / structural references, you will not make any mistakes.
*   Make sure you have defined all the tables and named ranges you are using in the formula.
*   Make sure any user defined functions you are using are properly installed.
*   Double check the ranges and string parameters in your formulas.

### \###### Error

You see a cell full of # symbols when the contents cannot fit in the cell. For eg. a long number like 2339432094394 entered in a small cell will show ####s. Also, you see the ###### when you format negative numbers as dates.

**How to fix the ###### error?**

Simple, adjust the column width. And if the error is due to negative dates, make them positive.

### #VALUE! Excel Formula Error

Value error is shown when you use text parameters to a function that accepts numbers. For eg. the formula =SUM(“ab”,”cd”) returns #VALUE! error.

**How to fix the #VALUE! error?**

Make sure your formula parameters have correct data types. If you are using functions that work on numbers (like sum, sumproduct etc.) then the parameters should be numbers.

### #REF!  Formula Error

This is one of the most common error messages you see when you fiddle with a worksheet full of formulas. You get #REF! Excel formula error when one of the formula parameters is pointing to an invalid range. This can happen because you deleted the cells. For eg. try to write a sum forumla like =SUM(A1:A10, B1:B10, C1:C10) and then delete the column C. Immediately the sum formula returns #REF! error.

**How to fix the #REF! error?**

First press ctrl+Z and undo the actions you have performed. And then rethink if there is a better way to write the formula or perform the action (deleting cells).

### #NUM! Excel Error

This is number error that you see when your formula returns a value bigger than what excel can represent. You will also get this error if you are using iterative functions like IRR and the function cannot find any result. For eg. the formula =4389^7E+37 returns a #NUM! error.

**How to fix #NUM! error?**

Simple, make your numbers smaller or provide right starting values to your iterative formulas.

### #NULL! Formula Error

This is rare error. When you use incorrect range operators often you get this error. For eg. the formula =SUM(D30:D32 C31:C33) returns a #NULL! error because there is no overlap between range 1 and range2.

**How to fix the #NULL! error?**

Make sure you have mentioned the ranges properly.

### Formula not working – showing as text?

If you don’t see any error, but instead of seeing the result, all you see is your formula (like below), then check out [**Formulas not working**](https://chandoo.org/wp/excel-formulas-are-not-working/)
 page for information how to fix the problem.

[![excel formula showing as text - What to do when all you see is the formula, not result](https://chandoo.org/img/f/excel-formula-not-working.png)](https://chandoo.org/wp/excel-formulas-are-not-working/)

### Further Reading on Excel Formula Debugging

[Formula Debugging using F9 Key](http://chandoo.org/wp/formula-debugging-tips-excel/)

[Learn to work with Circular References](https://chandoo.org/wp/excel-circular-references/)

[Understand the difference between absolute and relative references](http://chandoo.org/wp/relative-absolute-references-in-formulas/)

[How to work with tables & structural references](https://chandoo.org/wp/introduction-to-structural-references/)

[Detect errors in your formulas \[Office.com\]](https://support.office.com/en-us/article/detect-errors-in-formulas-3a8acca5-1d61-4702-80e0-99a36a2822c1)

[How to use new ERROR.TYPE formula to work with errors](https://www.techonthenet.com/excel/formulas/error_type.php)

**Tell me how you debug formulas? What is the most common error you get?**  
What is the strangest and most confusing error you have seen? Please share in the comments so we can all have a laugh and find a way to fix the problem.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [33 Comments](https://chandoo.org/wp/excel-formula-errors/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formula-errors/#respond)
    
*   Tagged under [\# DIV error](https://chandoo.org/wp/tag/div-error/)
    , [\# NA error](https://chandoo.org/wp/tag/na-error/)
    , [\# NAME error](https://chandoo.org/wp/tag/name-error/)
    , [\# NULL error](https://chandoo.org/wp/tag/null-error/)
    , [\# REF error](https://chandoo.org/wp/tag/ref-error/)
    , [\# VALUE error](https://chandoo.org/wp/tag/value-error/)
    , [debugging](https://chandoo.org/wp/tag/debugging/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadcheats](https://chandoo.org/wp/tag/spreadcheats/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThere is an Easter Egg in this Post](https://chandoo.org/wp/easter-excel/)

[Nextand the Winner is…Next](https://chandoo.org/wp/budget-vs-actual-winner/)

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
    
    [Reply](https://chandoo.org/wp/excel-formula-errors/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formula-errors/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formula-errors/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ