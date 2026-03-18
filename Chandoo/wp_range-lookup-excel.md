# Range Lookup in Excel - Find matching Price Tier with Formulas

**Source:** https://chandoo.org/wp/range-lookup-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Range Lookup in Excel – How to lookup the pricing tier? \[Formulas\]
====================================================================

*   Last updated on December 17, 2022

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Here is a really tricky problem.**_ Recently I was given a data set like this (shown below) and asked to find the position of lookup value in the list. The only glitch is that, instead of values, the lookup table contained lower and upper boundaries of the values. See the below illustration to understand what I mean. ![Range Lookup Excel - Formula for looking up a value to match corresponding range](https://chandoo.org/img/f/range-lookup-excel.png) _**In simple words, we have to find the range that has the lookup value.**_ Now, the problem is similar to [between formula trick](https://chandoo.org/wp/between-formula-excel/)
 we discussed a few days back, yet very different. **We all know that,**

*   [XLOOKUP formula](https://chandoo.org/wp/xlookup-examples/)
     looks up a value in a table and returns the corresponding value in next column
*   [MATCH formula](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
     looks up a value and tells the position of it in a list

But neither seem to solve this problem. So I naturally turned to a cup of home brewed coffee (remember, I no longer work in a office, so I can’t rush to espresso machine) and stared long and hard out of the window (remember, I no longer go to office, that means I can sit in front of a window and work). _Added in December, 2022:_

We can use XMATCH:
------------------

Since we just want to know which row will contain the value, we can use XMATCH as shown below.

				
					`=XMATCH(1, (B6:B15<=C3)*(C6:C15>=C3))`
				
			

Ok, go ahead, I will give you a minute to soak in the awesomeness of that formula.
----------------------------------------------------------------------------------

Are you back?, well, lets explore what this formula does.

How this works:

*   C3 contains our lookup value
*   B6:B15 has the lower boundary
*   C6:C15 has the higher boundary
*   The (B6:B15<=C3)\*(C6:C15>=C3) returns a bunch of 1s or 0s. It will be 1 whenever C3 is between column B&C values and 0 otherwise.
*   XMATCH will match the first 1, _ie_ the first row that matches the range.

**Or even the SUMPRODUCT**
--------------------------

Then I thought, “may be [SUMPRODUCT formula](https://chandoo.org/wp/excel-sumproduct-formula/)
 would work for situations like these?!?”

After playing for a while, I got the perfect formula for this.

*   Assuming the value to be looked up is in cell `C3`
*   The start and end values are in `B6:B15` and `C6:C15` respectively,

We write,

				
					`=SUMPRODUCT((B6:B15<=C3)*(C6:C15>=C3),ROW(B6:B15))-5`
				
			

**There are 3 portions in that formula,**
-----------------------------------------

1.  **`(B6:B15<=C3)*(C6:C15>=C3)` part:** This is checking the range B6:B15 and C6:C15 to find that one set of start and end values that would contain the value in C3. The output would be a bunch of 0s with probably a single 1
2.  **`ROW(B6:B15)` part:** This just gives running numbers from 6 to 15. When you SUMPRODUCT this with above you get a single number corresponding the row in which the match occurred
3.  **`-5` part:** We reduce the output value by 5 since our value began in row 6, not row 1.

Use this to lookup date ranges too:
-----------------------------------

![Excel Vlookup Date Ranges - Excel Formula to lookup matching date ranges](https://chandoo.org/img/f/vlookup-date-ranges-excel.png)

As you can guess, you can easily use the above SUMPRODUCT formula to lookup matching date ranges too _a la **vlookup for date ranges**_.

### Download Range Lookup Example Workbook:

In the download workbook, you can find both examples (values and dates). Go ahead and download it. Play with it to understand range lookup formula better.

[**Click here to download the sample workbook**](https://chandoo.org/wp/wp-content/uploads/2022/12/range-lookup-formula-example.xlsx)
.

### Do you face range lookup problem?

Often, when working on project planning, I end up checking where a date falls between given set of start and end dates. Earlier, I used helper columns to solve such a problem. But the XMATCH (or SUMPRODUCT) solution above is much more elegant and scalable. Plus it is much more fun to write.

**What about you?**

Do you face range lookup problem often? How do you solve it? Share your techniques and tips using comments. Thank you 🙂

### More Excel Formula Magic:

*   [Average of top 5 values – Excel Formula Tutorial](https://chandoo.org/wp/average-of-top-5-values/)
    
*   [Count the number of unique values in a range](https://chandoo.org/wp/count-number-of-unique-cells/)
    
*   [Reverse a list of values using INDEX formula](https://chandoo.org/wp/reverse-a-list-in-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [147 Comments](https://chandoo.org/wp/range-lookup-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/range-lookup-excel/#respond)
    
*   Tagged under [between formula](https://chandoo.org/wp/tag/between-formula/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [xmatch](https://chandoo.org/wp/tag/xmatch/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious\#### in Excel cell](https://chandoo.org/wp/in-excel-cell/)

[NextMerry Christmas & Happy New Year 2023Next](https://chandoo.org/wp/merry-christmas-happy-new-year-2023/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ