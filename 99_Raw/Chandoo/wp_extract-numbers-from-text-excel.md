# Extract numbers from text in excel - How to & Tutorial

**Source:** https://chandoo.org/wp/extract-numbers-from-text-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Extracting numbers from text in excel \[Case study\]
====================================================

*   Last updated on June 19, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Often we deal with data where numbers are buried inside text and we need to extract them.** Today morning I had such task. As you know, we recently ran a [survey asking how much salary you make](http://chandoo.org/wp/2012/05/25/how-much-salary-excel-survey/ "Do you work on Excel? How much salary you make? [Surveys]")
. We had 1800 responses to it so far. I took the data to Excel to analyze it. And surprise! the numbers are a mess. Here is a sample of the data.

![Extract numbers from text in Excel - How to?](https://img.chandoo.org/f/extract-numbers-from-text-excel-howto.png "Extract numbers from text in Excel - How to?")

_**Now, how do I extract the salary amounts from this without typing the values?**_

My first thought is to write a user defined function to extract the number from text. But I usually shy away from VBA. So I wanted to see if there is a formula based approach to extract the number from text.

Using formulas to extract number from text
------------------------------------------

![Extracting numbers from text using Excel formulas - process](https://img.chandoo.org/f/extract-numbers-from-text-in-excel.png "Extracting numbers from text using Excel formulas - process")

To extract number from a text, we need to know 2 things:

1.  Starting position of the number in text
2.  Length of the number

For example, in text **US $ 31330.00** the number starts at 6th letter and has a length of 8.

So, if we can write formulas to get 1 & 2, then we can combine them in MID formula to extract the number from text!

### Finding the starting position of number in text

To find the starting position, we need to find the first character which is a number (0 to 9). In other words, if we can find the positions of 0 to 9 inside the given text, then the _minimum of all such positions would be starting position._

Sounds complicated?!? Well, in that case look at the formula and then you will understand why this works.

Assuming the text is in A1 and the range lstNumbers contains 0 to 9, below formula finds starting position

**{=MIN(IFERROR(FIND(lstNumbers,A1),””))}**

You need to array enter it (CTRL+SHIFT+Enter)

**How this formula works?**

**FIND(lstNumbers, A1) portion:** This part finds where each of the numbers 0 to 9 occur in the text in A1. If a match is found, the position is returned. Else we get an error. For **US $ 31330.00** the values would be,

{10;7;#VALUE!;6;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}

Meaning, 0 occurs at 10th position, 1 occurs at 7th position, 3 occurs at 6th position and everything else (2,4,5,6,7,8,9) do not occur in the number.

**IFERROR(…,””) portion:** Then, we replace errors with empty spaces so that MIN could work its magic.

At this stage, the result would be, {10;7;””;6;””;””;””;””;””;””}

Related: [IFERROR Formula – syntax & examples](http://chandoo.org/wp/2011/03/11/iferror-formula/)

**{=MIN(…)} portion:** This would find the minimum of {10;7;””;6;””;””;””;””;””;””} **which is 6.** The starting position of number inside text.

_Because we are finding multiple items, we need to array enter the formula to get correct result._

### Finding the length of number

Once we find starting point, next we need to know the length of the number. There are many ways to do this. Depending on the variety in your input data, you can choose a technique that works best.

### Approach 1 – counting number of digits in text

My first approach is to count number of digits in the text and use it as length. For this, we can break the text in to individual characters and then see if each of them is a number or not.

Assuming the text is in A1, the number of digits in it are,

\=SUMPRODUCT(- -ISNUMBER(MID(A1,ROW($A$1:$A$200),1)+0))

**MID(A1,ROW($A$1:$A$200),1) + 0 portion**: This breaks the text in A1 in to individual characters (assumes the max length is 200) and then adds 0 to them.

At this stage, you have 200 values some of them numbers, others errors.

**ISNUMBER(…) portion:** This checks all the 200 values for numbers. After this, we will have 200 true or false values.

**— ISNUMBER (…) portion:** This converts the true, false values to 0s and 1s. (by double negating Excel will convert boolean values to number equivalents).

**SUMPRODUCT(…) portion:** This finally sums up all 1s thus giving us the number of digits in the text.

#### Does it work?

While this approach works well for some numbers, it fails in other cases. For example, a text like **US $ 31330.00** has number portion **with 8 characters** (31330.00) **where as our formula would say the length is 7** (because decimal point . is not a number and hence ISNUMBER() would give false for that).

So I had to move on to next approach.

### Approach 2 – counting number of digits, commas & decimal points in text

The next approach is to count not only numbers, but also commas & decimal points in the text. For this, first I placed all the digits (0 to 9) and comma & decimal point in a range called as **_lstDigits_.**

Below formula counts how many of _lstDigits_ are in text in A1.

\=SUMPRODUCT(COUNTIF(lstDigits,MID(A1,ROW($A$1:$A$200),1)))

**COUNTIF(lstDigits, MID(…)) portion:** This checks how many times each of the 200 characters appear in lstDigits.

This would be an array of counts. For example {0;0;0;0;0;1;1;1;1;1;1;1;1;…} for **US $ 31330.00**, indicating that first 5 are not in _lstDigits_ and then we have 8 in _lstDigits_.

**SUMPRODUCT(…) portion:** just sums all the numbers, hence we get **length as 8**.

Related: [SUMPRODUCT Formula – examples & explanation](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)

![Extract numbers from text in excel - results explained](https://img.chandoo.org/f/extract-numbers-from-text-results.png "Extract numbers from text in excel - results explained")

### Extracting numbers from text

Once we have starting position of number & its length, we can combine them in a MID formula to extract the number. Here is the result for our sample data set.

As you can see, this method works well, but fails in some cases like,

*   European number formats (, for decimal point and . for thousands)
*   Text with multiple numbers

Fortunately, in my data set, we had only a few incidents like these. So I have decided to manually adjust them than work out even more complicated formula.

Using Macros to extract numbers from text
-----------------------------------------

As you can guess, we can use a simple macro (or UDF) to extract numbers from a given text. We will learn how to do this next week.

Download Example Workbook
-------------------------

[**Click here to download example workbook**](https://img.chandoo.org/f/extracting%20numbers.xlsx)
 with all these formulas. Examine the formulas to understand how you can extract numbers from text in Excel.

How do you Extract numbers from Text?
-------------------------------------

Often I deal with data like this. I use a mix of techniques. Apart from the one mentioned above I also use,

*   getNumber() UDF to extract numbers from text (more on this next week)
*   Use SUBSTITUTE to clear formatting (replace dots with empty spaces and commas with dots to convert from European format to standard format)
*   Use VALUE to extract the number (works when number is shown as text)
*   Use +0 to force convert numbers from text (works when number is shown as text)

**What about you?** How do you extract numbers from text? What are your favorite techniques? _**Please share using comments.**_

Tips on cleaning data using Excel
---------------------------------

If you use Excel to clean data, go thru these articles to learn some powerful techniques.

*   [Clean up dates & convert text to dates](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    
*   [Remove Duplicates using Excel using formulas](http://chandoo.org/wp/2008/11/06/unique-duplicate-missing-items-excel-help/)
     or [using Excel features](http://chandoo.org/wp/2008/12/29/excel-2007-review/)
    
*   [Extract phone numbers from data](http://chandoo.org/wp/2008/09/30/clean-up-incorrectly-formatted-phone-numbers-using-excel/)
    
*   [Quickly fill blank cells with data](http://chandoo.org/wp/2011/10/17/fill-blank-cells-in-a-table/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [65 Comments](https://chandoo.org/wp/extract-numbers-from-text-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-numbers-from-text-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [find](https://chandoo.org/wp/tag/find/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MIN()](https://chandoo.org/wp/tag/min/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousUse MAX to find latest date in a list \[Quick tip\]](https://chandoo.org/wp/use-max-to-find-latest-date-in-a-list/)

[NextJoin our Financial Modeling Class before fee hike \[Quick update\]Next](https://chandoo.org/wp/join-our-financial-modeling-class-before-fee-hike/)

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
    
    [Reply](https://chandoo.org/wp/extract-numbers-from-text-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-numbers-from-text-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-numbers-from-text-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ