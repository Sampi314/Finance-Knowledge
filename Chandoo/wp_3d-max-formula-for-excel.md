# 3D Max Formula for Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/3d-max-formula-for-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

3D Max Formula for Excel
========================

*   Last updated on September 9, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know about the MAX formula. **But do you know about 3D Max?**

Sounds intriguing? Read on.

Lets say you are _the sales analyst_ at ACME Inc. Your job involves drinking copious amounts of coffee, creating awesome reports & helping ACME Inc. beat competition.

For one of the reports, you need to find out the maximum transactions by any customer across months.

But there is a twist in the story.

Your data is not in one sheet. _It is in multiple sheets, one per month._

_Like this:_

![3d max formula - what is the maximum of all months?](https://img.chandoo.org/f/3d-max-formula-what-is-the-maximum-of-all-months.png)

_**How to get the max value for all months?**_

### Using 3D MAX formula

We can [use 3D formulas](http://chandoo.org/wp/2010/02/19/excel-consolidate-data/)
 in such cases. 3D formula?!?

Lets say our transaction data is in column C, in range C5:C44 in all sheets (same cells in all sheets)

To calculate the max of all the transactions, we simply write:

\=MAX(Jan:Jun!C5:C44)

Notice the blue text? That is what makes our references 3D.

Aside: If row & columns make Excel 2D, sheets in a workbook act as 3rd dimension. Hence the name 3D reference.

This formula will go and fetch all the C5:C44 data from sheets Jan thru Jun and gives us the desired answer.

Related: [Consolidating data from multiple sheets using 3D references](http://chandoo.org/wp/2010/02/19/excel-consolidate-data/)
.

### What if you want to consider only specific months

The 3D formula approach is simple & powerful. But what if you want to consider data only in a specific list of sheets (or months in our case)?

For example, what formula would work if we want to **calculate maximum transactions in months Jan, Mar, Apr & Jun alone**?

Lets say the names of the sheets we want to consider is listed in a range called _**sheet.names**_

![Sheet names in a range - 3D max formula problem in Excel](https://img.chandoo.org/f/3d-max-formula-named-range-for-sheet-names.png)

Also, keep in mind that the data is in range C5:C44 in all the sheets.

Then the below formula gives us maximum value from the selected sheets.

`{=MAX(N(INDIRECT(ADDRESS(ROW(A5:A44),3,1,1, TRANSPOSE(sheet.names)))))}`

It is an array formula. So you must press CTRL+Shift+Enter to get the correct result.

PS: Thanks to _Pranay Shah_, whose question inspired me to write this formula.

### How does it work?

First lets figure out the logic we need to use.

*   We have a list of sheet names in the range _sheet.names_
*   For each sheet, get the data from cells C5:C44
*   Calculate the max of all this data

Now, lets take a look at the formula, inside out.

**ROW(A5:A44) portion:** This generates an array for numbers from 5 to 44 – {5;6;7;…;42;43;44}

**Transpose(sheet.names) portion:** This transposes the vertical sheet names array to horizontal. So {“Jan”;”Mar”;”Apr”;”Jun”} becomes {“Jan”,”Mar”,”Apr”,”Jun”}

**ADDRESS(ROW(),3,1,1,TRANSPOSE()):** This generates an array of cell addresses from rows 5 to 44, column 3 and sheets in sheet.names range. The result looks like this:

{“Jan!$C$5″,”Mar!$C$5″,”Apr!$C$5″,”Jun!$C$5”; “Jan!$C$6″,”Mar!$C$6″,”Apr!$C$6″,”Jun!$C$6”;  
“Jan!$C$7″,”Mar!$C$7″,”Apr!$C$7″,”Jun!$C$7”; “Jan!$C$8″,”Mar!$C$8″,”Apr!$C$8″,”Jun!$C$8”;  
“Jan!$C$9″,”Mar!$C$9″,”Apr!$C$9″,”Jun!$C$9”; “Jan!$C$10″,”Mar!$C$10″,”Apr!$C$10″,”Jun!$C$10”;  
…  
“Jan!$C$41″,”Mar!$C$41″,”Apr!$C$41″,”Jun!$C$41”; “Jan!$C$42″,”Mar!$C$42″,”Apr!$C$42″,”Jun!$C$42”;  
“Jan!$C$43″,”Mar!$C$43″,”Apr!$C$43″,”Jun!$C$43”; “Jan!$C$44″,”Mar!$C$44″,”Apr!$C$44″,”Jun!$C$44”}

**Why TRANSPOSE()?**

If we have not TRANSPOSE()ed either sheet.names or row numbers, we will not get full list of addresses. TRANSPOSE forces Excel to generate all combinations of addresses from given row numbers & sheet names.

For example, here is the result of the formula

ADDRESS(ROW(A5:A44),3,1,1, sheet.names)

_Notice the missing TRANSPOSE()_

{“Jan!$C$5″;”Mar!$C$6″;”Apr!$C$7″;”Jun!$C$8”;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A; #N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A; #N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A; #N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A;#N/A}

**INDIRECT(ADDRESS()) portion:** We have the addresses and we need values. This is exactly the purpose of INDIRECT formula. So we pass the list of addresses to INDIRECT to get the cell values.

This results in an array of numbers like this:

{1400,900,1225,1440; 1035,1300,850,1850; 990,2000,1140,775; 1520,870,1225,650; 1300,1000,1800,875; 1305,980,1085,1215; 750,1350,1000,1330; 1050,600,1125,1755; 990,735,1350,1600; 1215,1750,770,625; 1600,735,1305,1300; 960,1950,1480,1800; 1215,1365,1110,1395; 1320,910,750,1560; 1700,975,1125,1480; 900,1400,780,1300; 1485,1440,960,1300; 825,2125,1110,1215; 1000,945,810,1120; 1650,500,1170,990; 1440,1080,1110,840; 1035,840,1300,800; 1225,1330,1020,1560; 1100,690,1170,780; 600,700,1280,990; 1000,1000,1400,700; 1260,1520,875,1305; 1360,1260,925,1320; 810,1100,2000,1800; 825,690,750,1215; 1575,1560,1000,1900; 1190,1080,960,1400; 1200,1200,1160,980; 900,1665,575,500; 880,1000,1200,1550; 1000,950,1440,550; 1400,900,1000,1190; 750,1190,1110,700; 1710,805,800,1755; 1950,1365,660,1150}

Now, notice the 2 dimensional nature of this array. It has 4 items per row.

**N(INDIRECT()) portion:**

We just pass the array of numbers to N() so that they are force converted to numbers. This step ensures that we get correct results with MAX.

Note: Even without N() your array formula shows a result, but often this will be incorrect. I assume it is one of the quirks of Excel and we just have to use N().

Related: See how N() plays a vital role in situations like – [dynamic charts from non-contiguous data](http://chandoo.org/wp/2012/12/04/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/)
 & [String parsing](http://chandoo.org/wp/2013/07/17/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/)
.

**MAX(N()) portion:**

This will just tell us what the maximum number in that array. Make sure you press CTRL+Shift+Enter to get the correct result.

### Download Example Workbook

If all these MAX formulas are confusing, check out the [**example workbook**](https://img.chandoo.org/f/3d-max-formula.xlsx)
. It shows all these. Play with the formulas and examine the results to learn more.

### Do you use 3D references?

I rarely use them. This is because, most of the times, my data is in one place. If is it scattered across multiple sheets, I usually spend time writing a macro (or using Power Query) to consolidate the data to one place before attacking the analysis problems.

But I find 3D references & formulas a powerful way to answer questions like this.

**What about you?** Do you use 3D references in your formulas? When do you use them? Please share your thoughts & experiences using comments.

### Learn more

If this technique sounds interesting, check out below tutorials to learn more.

*   [MaxIF formula in Excel](http://chandoo.org/wp/2012/01/24/formula-forensics-no-008/ "Formula Forensics No. 008 – Elkhan’s MaxIf")
    
*   [Using INDEX formula in Excel](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
    
*   [Calculate maximum change – problem](http://chandoo.org/wp/2014/03/21/calculate-maximum-change-homework/)
     & [Solution](http://chandoo.org/wp/2014/03/26/maximum-change-solutions/)
    
*   [Calculating all-time high & trailing 12 months high values](http://chandoo.org/wp/2011/02/10/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/3d-max-formula-for-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/3d-max-formula-for-excel/#respond)
    
*   Tagged under [3d references](https://chandoo.org/wp/tag/3d-references/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [MaxIf](https://chandoo.org/wp/tag/maxif/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [N()](https://chandoo.org/wp/tag/n/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [transpose](https://chandoo.org/wp/tag/transpose/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousReplace formulas with values with a simple wiggle](https://chandoo.org/wp/replace-formulas-with-values-with-a-simple-wiggle/)

[NextPlease help me design our new course – “50 ways to analyze your data”Next](https://chandoo.org/wp/50-ways-to-analyze-data-poll/)

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
    
    [Reply](https://chandoo.org/wp/3d-max-formula-for-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/3d-max-formula-for-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/3d-max-formula-for-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ