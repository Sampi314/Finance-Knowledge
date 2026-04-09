# Case Sensitive VLOOKUP - How to write case sensitive lookup formulas in Excel

**Source:** https://chandoo.org/wp/case-sensitive-lookups

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Case Sensitive Lookups
======================

*   Last updated on September 7, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know that [VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 (and its cousins MATCH, HLOOKUP and LOOKUP) are great for finding information you want. But they are helpless when you want to do a case-sensitive lookup.

![case-sensitive-vlookup-in-excel](https://chandoo.org/wp/wp-content/uploads/2015/09/case-sensitive-vlookup-in-excel.png)

_**So how do we write case sensitive VLOOKUP formulas?**_

Simple. We can use **EXACT** formula.

### What exactly is the EXACT formula?

EXACT formula checks if 2 cells have exactly the same value. And it is very SenSITive.

For example, `=EXACT("this","THIS")` will be false , where as =”this”=”THIS” will be true.

### Using EXACT formula to do case sensitive lookups

Let’s say the value you are looking up is in cell F4, the lookup range is B5:C11 (column B has lookup value and column C has value you want).

You can use EXACT formula along with INDEX + MATCH or SUMPRODUCT to do case sensitive lookup. Let’s look at each of these variations:

**Using EXACT & INDEX + MATCH formulas to do case sensitive lookups:**

**Formula:** `{=INDEX($C$5:$C$11,MATCH(TRUE,EXACT($F$4,$B$5:$B$11),0))}`

**How it works?** 

Let’s go from inside out.

**`EXACT(F4, B5:B11)` portion:** This will return an array of TRUE & FALSE values. Something like this:

`{FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE}   `  
**`MATCH(TRUE, EXACT(...), 0)` portion:** Now we look for TRUE in all the values EXACT has returned. This will be 3 (since 3rd value in the array is true).

**`INDEX(C5:C11, MATCH(...))` portion:**  This will simply return the 3rd value in the column C, _ie an exact match._

**`{INDEX(...)}`:**  Because this is an array formula, you must press CTRL+Shift+Enter after typing it. The {} indicates this.

Related: [Learn about INDEX+MATCH combination](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
.

**Using EXACT + SUMPRODUCT formula:**

If the lookup result is a number (or date) and there is only matching value, you can use SUMPRODUCT to do case sensitive lookups.

**Related:** [Introduction Excel SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
.

**Formula:**`=SUMPRODUCT(EXACT($F$4,$B$5:$B$11) * ($C$5:$C$11))`

**How it works?**

The `EXACT(F4, B5:B11)` portion returns a bunch of TRUE & FALSE values.

When you multiply these TRUE & FALSE values with column C (which contains numbers), the end result will be the value you are looking for.

This is possible because in Excel, TRUE is 1 and FALSE is 0. So when you multiply a list of logical values (true / false) with a list of numbers, everything that corresponds to false becomes 0.

So we get,

`{0;0;30;0;0;0;0}`

SUMPRODUCT simply adds up these numbers and returns 30 as result.

Note: This formula won’t work if you have text values in column C or more than one TRUE in EXACT result (ie multiple values match the lookup criteria).

**For advanced users:** [SUMPRODUCT – Advanced scenarios](http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/)

### Download case sensitive lookup – example workbook

[**Please click here to download case sensitive lookup example workbook**](https://chandoo.org/wp/wp-content/uploads/2015/09/case-sensitive-lookups.xlsx)
. Examine the formulas to learn more about this technique.

### More ways to lookup:

*   [2 Way lookups](http://chandoo.org/wp/2010/11/09/2way-lookup-formulas/)
     – lookup in top row & left column and find matching value.
*   [Wild lookups](http://chandoo.org/wp/2010/11/01/using-wildcards-with-vlookup/)
     – lookup a value that starts with Som & ends with ne.
*   [Range lookup](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
     – find a value inside the lower & upper boundary
*   [Last lookup](http://chandoo.org/wp/2015/08/11/vlookup-the-last-value/)
     – find the last value in a list of multiple matches.
*   [Multi-condition lookups](http://chandoo.org/wp/2014/10/28/multi-condition-vlookup/)
     – lookup based on multiple conditions
*   [Take our VLOOKUP Quiz](http://chandoo.org/wp/2013/03/22/how-well-do-you-know-your-lookups-quiz/)
     – how well do you know VLOOKUP?

**Get The VLOOKUP Book:** If you are always looking for help about VLOOKUP, look no further. Get my book, it’s going to make you awesome in VLOOKUP, INDEX+MATCH, multi-condition lookups, 2 way lookups and more. **[Click here to order your copy](http://chandoo.org/wp/resources/the-vlookup-book/)
**.

### How do you write case sensitive lookups?

Let me be honest. I haven’t had a single case sensitive lookup scenario in last year. But email from a reader prompted me to research this problem.

**What about you?** Do you often deal with case-sensitive data? How do you write case sensitive lookups? Please share your tips & formulas in comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/case-sensitive-lookups/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/case-sensitive-lookups/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [EXACT()](https://chandoo.org/wp/tag/exact/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousWeekend poll: Formulas or Pivot Tables?](https://chandoo.org/wp/formulas-or-pivot-tables-poll/)

[NextCropped chart: when some values are too big to fitNext](https://chandoo.org/wp/cropped-chart/)

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
    
    [Reply](https://chandoo.org/wp/case-sensitive-lookups/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/case-sensitive-lookups/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/case-sensitive-lookups/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ