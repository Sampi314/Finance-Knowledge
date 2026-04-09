# How do Business Analysts use Microsoft Excel - Examples & Tips

**Source:** https://chandoo.org/wp/business-analysts-excel

---

*   [interviews](https://chandoo.org/wp/category/interviews/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How do Business Analysts use Excel \[Guest Post from a Rock-star BA\]
=====================================================================

*   Last updated on February 3, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**On Jan 4, I received this email from Matt,**_

> Thank you for sharing all of your knowledge on such an incredible website. Your site has such an incredible array of useful tips, tricks, and solutions to every day problems, I don’t know what I would do without it! It’s the only place I go to look for help when I’m stumped with excel. Thanks to you, I’ve become an “excel wizard,” and have been able to show coworkers mind blowing new things with excel they never knew about. I even taught a 4 week training class at my old job! Over the past 3 years, tips I’ve learned from your site have been appreciated all the way in Seattle, Washington, at an internet marketing company, a newspaper, and a food website.

While the mail is flattering, I was more interested to know how Matt uses Excel in his day to day work. So I asked him to write a small guest post sharing his experiences. He gladly accepted the offer and here were are, with a post full of tips & ideas to help you. I am sure many business analysts, analysts and managers out there can co-relate to Matt’s experience.

————————————————————————————–

_**Guest Article by Matt Decuir**_

![How do business analysts use Excel - Experience of a Rockstar BA](https://chandoo.org/img/g/rockstar-business-analyst-with-excel.jpg)

At [Allrecipes.com](http://allrecipes.com/)
 we use excel for a variety of purposes. Analyzing site trends, forecasting traffic, charts, dashboards, and slide shows; you name it, we use excel for it. That’s why Chandoo’s tips have been so helpful – because we use excel every day. Thanks to chandoo.org, I’ve developed a reputation as an “excel wizard” and even taught a 4 week excel training class!

Most of your colleagues are probably like mine – they’ve got a pretty good understanding of excel. They use formulas and charts regularly, occasionally experimenting with Pivot Tables. As a Chandoo reader, you’re probably already an excel expert or well on your way to becoming one. But even more important than your excel expertise is the ability to communicate helpful tips to others. Regardless of your audience, complicated formulas can be difficult to explain. If you can point out tips that are within your colleagues’ comprehension, you will quickly become an excel rock star. The trick is to know your audience.

**Here are a few simple tips that will wow your colleagues:**

*   **Autofill:** Instead of wasting time scrolling and dragging a formula all the way down the page, your colleagues will be amazed that double clicking on the **AutoFill** icon will automatically do it for them.
    *   One co-worker affectionately calls this the “[double click trick](http://chandoo.org/wp/2009/06/12/excel-mouse-tricks/)
        “
*   **Transpose:** Need to change how your data is oriented? Not sure exactly how to phrase what you’re trying to do? Just [**Paste Special**](http://chandoo.org/wp/2008/07/02/17-excel-paste-special-tricks/)
     and check the **Transpose** box and your data will magically be transformed from horizontal to vertical.
*   **Keyboard Shortcuts:** Scrolling is the enemy. Nobody wants to waste their whole day scrolling to the bottom of a spreadsheet. Here are a few [keyboard shortcuts](http://chandoo.org/wp/2010/02/22/complete-list-of-excel-shortcuts/)
     that will save time:
    *   **CTRL + down arrow**:To get to the bottom row of your data set
    *   **CTRL +up arrow**: To get the top row of your data set
    *   **CTRL + right arrow**: To get to the last column of your data set
    *   **CTRL + left arrow**: To get to the first column of your data set
    *   **CTRL + Home**: To get to the first cell (top left) in your data set
    *   **CTRL + End:** To get to the last cell (bottom right) in your data set
    *   Bonus: Holding **SHIFT** down while using any of the above shortcuts will select that entire range

*   **Charts:** Charts are confusing. They never do what you want them to do. Most people have used charts before, but are in no way experts. You’ll win points if you can explain how to:
    *   Add a secondary axis
    *   [Create a combination chart](http://chandoo.org/wp/2009/07/02/secondary-axis-combination-charts-howto/)
         with both bar and line graphs

*   [**Pivot Tables**](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    **:** Pivot Tables are daunting to most people who don’t use them regularly. If you can help your colleagues navigate the treacherous waters of Pivot Tables, they will definitely appreciate it. Keep it simple though, as the flexibility can get overwhelming to new users very quickly.
    *   Start by creating a Pivot Table to answer 1 question. Then explain how to filter and sort the data. By doing this, your colleagues will slowly warm to Pivot Tables, making them less overwhelming.

**Now that you’ve got some simple tips in your repertoire, here are the formulas and tools I use the most:**

### Lookup and Text Formulas:

*   [**SUMIFS**](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    **, AVERAGEIFS, and COUNTIFS**: Like SUMIF on steroids. Useful for looking up any non-text values with multiple criteria
    *   Great for recreating the functionality of a Pivot, but allowing you to format the output however you would like
    *   Makes month over month calculations extremely easy, especially with named cells.

*   [**VLOOKUP**](http://chandoo.org/wp/2010/11/02/excel-vlookup-tips/)
    **,** [**INDEX, and MATCH**](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    **:** Useful for looking up any text values
    *   Always make sure to end your VLOOKUP with **FALSE** to return the exact match

*   **IFERROR:** Replaces errors with a different value
    *   i.e. IFERROR(A1/B1,0) replaces errors with zeroes

*   **LEFT, MID, RIGHT, and SEARCH**: Useful for parsing specific parts out of URLs

### Date Formulas:

*   **TODAY():** Automatically calculates today’s date
*   **DATE:** Useful for calculating specific days in the year
    *   i.e. DATE(YEAR(TODAY()),1,1) calculates the first day of the year (“1/1/2011”)
*   **EDATE:** Increments a date by X number of months. Negative numbers also work to go backwards.
    *   i.e. EDATE(A1,1) increments a date by 1 month (“2/1/2011”)
*   **TEXT:** Converts a value to any date format you would like
    *   i.e. TEXT(A1,”dddd”) converts a date into day of the week (“Monday”)
    *   i.e. TEXT(A1,”mmmm”) converts a date into a month (“January”)
*   **WEEKDAY:** Returns the day number in the week.
    *   i.e. WEEKDAY($A1,2)>5 returns TRUE for weekends

### Charts:

*   [**Dynamic Chart Ranges**](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/)
    **:** Use OFFSET and named ranges to only chart cells that have values. This saves time because you don’t have to update chart data ranges each month
    *   Alternatively, returning errors (#N/A) when values are blank will also exclude empty cells from line and bar charts
*   [**Rolling Chart Data Ranges**](http://chandoo.org/wp/2010/04/06/rolling-months/)
    **:** Set a static number of months and use SUMIFS to populate values automatically
*   [**Dynamic Chart Data Labels**](http://chandoo.org/wp/2010/05/05/change-data-labels-in-charts/)
    : Great for showing month over month % change, instead of default data labels

### Other Tools:

*   **Named ranges:** Useful for referencing calculated dates, lookup formulas, data validation lists, creating dashboards, etc…
    *   **CTRL + F3**: shows all the named ranges in your spreadsheet
*   [**Data Validation**](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/)
    **:** For creating drop down lists
    *   Named ranges allow you to reference a list of values in a separate tab
*   [**Conditional Formatting**](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    **:** For formatting everything!
    *   **Highlight Cell Rules**: Highlights positive values in green, negative values in red
    *   **Custom Formula Rules**: Useful for shading weekends in gray when looking at a whole month’s data by day (i.e. WEEKDAY($A1,2)>5)
    *   **Data Bars**: Shows a tiny bar chart within the cell. Good for showing trends within a data table

I hope these tips help you become a rock star among your friends and colleagues!

Matt Decuir  
Business Analyst, Allrecipes.com  
(decuirm at gmail dot com)

————————————————————————————–

### Thank you Matt

Thanks for sharing your experiences and ideas so openly. This proves that to be a successful analyst, good understanding of numbers and tools is necessary.

_**If you like this article, say thanks to Matt.**_ Also tell us how you are using Excel to become awesome at work. Go ahead and leave a comment.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [25 Comments](https://chandoo.org/wp/business-analysts-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/business-analysts-excel/#respond)
    
*   Tagged under [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [interviews](https://chandoo.org/wp/tag/interviews/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [interviews](https://chandoo.org/wp/category/interviews/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHoliday Request Form in Excel \[Awesome Ways our Readers are using Excel\]](https://chandoo.org/wp/holiday-request-form-excel/)

[NextA Huge Collection of Spreadsheets for Teachers \[What Excel Can Do\]Next](https://chandoo.org/wp/spreadsheets-for-teachers/)

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
    
    [Reply](https://chandoo.org/wp/business-analysts-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/business-analysts-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/business-analysts-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ