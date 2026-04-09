# Marketing Charts in Excel - Segmentation Chart Template for Download

**Source:** https://chandoo.org/wp/market-segmentation-charts-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Market Segmentation Charts using Conditional Formatting
=======================================================

*   Last updated on February 18, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Trust _**Peltier**_ to come up with solutions for even the most impossible looking charts. Today he shares a [marimekko chart tutorial](http://peltiertech.com/WordPress/marimekko-charts/)
.

![](https://chandoo.org/img/c/marimekko-chart-pts.png "Market Segmentation Charts - PTS")_**What in the name of unindented VBA code is a Marimekko Chart ?**_

**It is a variable width stacked chart.** It is a good way to depict how various segments have performed wrt a set of products, essentially a market segmentation chart. See a sample chart that Jon created to the right.

I couldn’t sit still after seeing his post. So here comes market segmentation charts or marimekko charts using, <drum roll> [conditional formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
.

See it for yourself, a market segmentation chart drawn in a 20×20 range of cells.

![](https://chandoo.org/img/c/market-segmentation-charts.png "Market Segmentation Charts in Excel")

Here is a brief tutorial on how I created this. With little time and a strong coffee you can build a market segmentation chart too.

### 1\. Adjust the data of your market segments and products

While Jon’s data ([image](http://peltiertech.com/images/2009-02/MarimekkoDataOrig.png)
) is oriented such that products are in columns and segments are in rows, I created the below structure as it directly maps to how the chart is drawn (segments in columns and products in rows)

![Product and Segments Data for your Market Segmentation Charts](https://chandoo.org/img/c/product-segment-data.png)

I have derived the below table using formulas. It uses the number 20 (which is the size of one side of our conditional chart) and some rudimentary formulas to derive the numbers 0,8,14,18 from 40%,30%,20%,10% and so on. _How ?_ Now would be the good time to take a sip of that strong coffee and think hard looking out of the window.

### 2\. Create a simple 20X20 grid and start writing formulas

Ok, this is the tricky part. Ideally when the chart is ready we want to have 4 colored regions in each of the 4 segments (this can change if you have more products or more segments). Imagine you were to just write numbers in that grid such that for first product we write number “1” in each segment cells and second product, number “2” so on. Then, color all 1s, 2s, 3s and 4s differently using conditional formatting, then this is how it would look.

![Market Segment Chart - Raw](https://chandoo.org/img/c/segment-chart-formulas-cf.png)

Now, we need to just figure out a simple formula that can automatically determine whether to output 1 or 2 or 3 or 4. ENTER THE STRONG COFFEE (or your favorite drink), slurp, slurp…

Ok, did you see those running numbers in the first column and row ? Good, We need to use those numbers to figure out certain things for us.

I have written the following formula in first cell in the 20×20 grid and copy pasted it all over the range.

`=CHOOSE(MATCH(I$4,$C$13:$F$13,1), MATCH($H24,$C$14:$C$17,1), MATCH($H24,$D$14:$D$17,1), MATCH($H24,$E$14:$E$17,1), MATCH($H24,$F$14:$F$17,1))`

**What is it doing ?** It is checking which segment the current cell belongs to by matching the top-row number with derived table’s first row (0,8,14,18). So for cell 1 this would be 1, for cell 12 this would be 3. Then, [CHOOSE formula](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)
 uses this information to determine which [MATCH formula](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 to run, there are 4 match formulas, each for one segment. All of them check the first-column running number with product-wise start numbers derived in the table 2 above. Slightly lost? Well, me too. Sip once more and read from beginning until it makes some sense.

### 3\. Finally, apply the conditional formatting

Ok, now select the 20×20 grid and [apply conditional formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
. Since I have created this in Excel 2007, I could define 4 rules, one for each number. But You can do similar using Excel 2003 (just define 3 rules, one for each number and apply 4th color to the entire range)  
![Conditional Formatting Rules - Excel 2007 - Market Segmentation Charts](https://chandoo.org/img/c/segment-chart-cond-format.png)

![Custom Format Code for Making Cells Invisible - Microsoft Excel](https://chandoo.org/img/c/custom-format-make-cell-invisible.png)  
Also, hide the cell contents in the 20×20 grid by applying custom format code like this.

Thats all, you are now all set to show off your market segment chart. Go flaunt.

**Download the [market segment charts template](http://chandoo.org/img/c/market-segmentation-chart-template.zip "market segment charts template-Microsoft Excel 2007")
 and play around.** \[_Excel 2007 File_\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/market-segmentation-charts-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/market-segmentation-charts-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/visualization/)
    , [cool](https://chandoo.org/wp/tag/cool/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel 2007](https://chandoo.org/wp/tag/excel-2007/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [marimekko charts](https://chandoo.org/wp/tag/marimekko-charts/)
    , [market segmentation charts](https://chandoo.org/wp/tag/market-segmentation-charts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousGoogle Spreadsheets Introduces Data Validation, Sweet!](https://chandoo.org/wp/google-spreadsheets-introduces-data-validation-sweet/)

[NextWelcome Robert & ClearlyAndSimply.com to BloggingNext](https://chandoo.org/wp/clearly-and-simply-robert-blog/)

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
    
    [Reply](https://chandoo.org/wp/market-segmentation-charts-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/market-segmentation-charts-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/market-segmentation-charts-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ