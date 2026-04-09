# Formula Forensics No. 041 - Convert a Roman Numeral to a Number » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics No. 041 – Convert a Roman Numeral to a Number
===============================================================

*   Last updated on September 12, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week in the [Chandoo.org Forums](http://forum.chandoo.org/threads/convert-roman-numerals-to-numbers.31196/)
 a user asked a question

“How do I convert a Roman Numeral to a Number eg: MMMCCCLVII to 3357”

User Xlstime presented the solution of:

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

Today we are going to look at how and why that simple formula works

As always at Formula Forensics you can follow along using a sample file: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman-to-Number.xls)

Solution
--------

Excel has a Roman function wherein \=Roman(3357, 0) will return **MMMCCCLVII**

I knew there was no such reverse Roman function prior to Excel 2013 and so my initial thought was to look at a VBA Solution.

See notes on the Arabic Excel function at the end of the post.

However Xlstime presented \=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

How does this work?

lets start by pulling it apart from the inside out

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

The Indirect Function simply takes its inputs and converts them to a Range, in this case 1:3999.

We will study why 3999 later

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

The next function working out is Row()

Excel will convert the function ROW(INDIRECT(“1:3999”)) to an array of Row Numbers

\={1;2;3;4;5;6;7;8;9;10;11; …. 3995;3996;3997;3998;3999}

You can see this if you goto cell D7 in the Sample File, press F2 and then F9

I limited the numbers to 300 as Excel cannot display more than 8,192 digits

Stepping out one more function:

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

The Roman() function converts its inputs into Roman Numbers

eg: Roman(58) will return LVIII

But as we are feeding it an array of numbers from 1 to 3999 Excel handles all these and converts them to an Array of Roman Numbers

Goto  D9 in the sample file \=ROMAN(ROW(INDIRECT(“1:300”))) press F2 and then F9

Excel returns an array of roman numbers

\={“I”;”II”;”III”;”IV”;”V”;”VI”;”VII”;”VIII”; … “CCXCVI”;”CCXCVII”;”CCXCVIII”;”CCXCIX”;”CCC”}

_We have limited the example to 300 as Excel cannot display more than 8,192 characters when processing  a Function using F9._

Stepping out one more function

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

The Excel Index() function is taking the Array of Roman Numerals and Converting it into a single Column array

This isn’t technically needed but it simplifies the solution

If you goto cell D11 in the sample file \=INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0) press F2 and then F9

Excel returns an array of roman numbers

\={“I”;”II”;”III”;”IV”;”V”;”VI”;”VII”;”VIII”; … “CCXCVI”;”CCXCVII”;”CCXCVIII”;”CCXCIX”;”CCC”}

This is exactly the same as the previous output from the Roman() function above, Except that it is now a Single Vertical Array.  This is important for the next function.

Stepping out one more function

\=MATCH(A2,INDEX(ROMAN(ROW(INDIRECT(“1:3999”))),0),0)

We can see here that the Array of Roman Numerals is now being fed into a Match() function.

Match uses the Syntax **\=Match(Lookup value, Lookup Array, Match Type)**

Match returns the position of the Lookup value within the array

So in our example

The Lookup value is A2 or our Roman Numeral MMMCCCLVII

The Lookup Array is an array of Roman Numerals from 1 to 3999

\={“I”;”II”;”III”;”IV”;”V”;”VI”;”VII”;”VIII”; … “MMMCMXCV”; “MMMCMXCVI”; “MMMCMXCVII”; “MMMCMXCVIII”; “MMMCMXCIX”}

and the Match Type is 0 or an exact Match

So the Match function will lookup the value MMMCCCLVII in the array and find it in position number 3357, which happens to correspond to the Number of the Roman Numeral and Return 3357 as the result.

### Why are we limited to 3999 numbers.

The Excel Roman() function is limited to numbers up to 3999

[![roman01](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman01.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman01.png)

Why 3999?

Because in Roman Numerals there is no Letter for 5,000 and 4,000 would be shown as M before the Letter for 5,000.

### **Why did we need the Index() function?**

If you goto D17 in the sample file you will see the formula:

\=MATCH(A2,ROMAN(ROW(INDIRECT(“1:3999”))),0)

It is the same formula as above but without the Index() function

You will see that it is returning a #VALUE! error

If you edit the formula with F2 and then press F9 to process the function you will see it now shows 3357

What s happening here?

Pressing F9 is the same as Array Entering the Function

so if you edit the function pressing F2 and now Array Enter the function by pressing Ctrl+Shift+Enter, excel now returns 3357

The Index() function puts a wrapper around the array for processing by the Match() function and so Array Entering is avoided.

Most array formulas that require Ctrl+Shift+Enter can be rewritten incorporating an INDEX wrapper and will not require the Ctrl+Shift+Enter confirmation.

### The Excel Arabic Function

In 2013, Microsoft introduced the Arabic function to Excel

To use simply use =Arabic(A2) or =Arabic(“MMMCCCLVII”)

You can read about the Syntax of the function in the Excel Help.

[![roman03](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman03.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman03.png)
[![roman04](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman04.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman04.png)

Download
--------

You can download a copy of the above file and follow along, [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/09/Roman-to-Number.xls)
.

A Challenge
-----------

Can you solve the problem another way ?

Post your solutions in the comments below.

**[Other Posts in this Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensuics Homepage")
  
**
---------------------------------------------------------------------------------------------------------------------

The Formula Forensics Series contains a wealth of useful solutions and information specifically about how Normal Formula and specifically Array Formula work.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

If you have a formula and you want to understand how it works contact [Hui](http://chandoo.org/wp/about-hui/)
 and it may be featured in future posts.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number/#respond)
    
*   Tagged under [Arabic()](https://chandoo.org/wp/tag/arabic/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Roman](https://chandoo.org/wp/tag/roman/)
    , [row()](https://chandoo.org/wp/tag/row/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousSara’s Copy Shop – Break even analysis and what-if modeling in Excel \[Videos\]](https://chandoo.org/wp/saras-copy-shop/)

[NextStacked Bar/Column Chart with Indicator Arrows – AdvancedNext](https://chandoo.org/wp/stacked-barcolumn-chart-with-indicator-arrows-advanced/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-041-convert-a-roman-numeral-to-a-number/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ