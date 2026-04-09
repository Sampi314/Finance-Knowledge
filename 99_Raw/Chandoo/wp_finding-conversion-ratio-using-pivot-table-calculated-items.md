# Finding Conversion ratio using Pivot Table Calculated Items » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items

---

*   [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

Finding Conversion ratio using Pivot Table Calculated Items
===========================================================

*   Last updated on March 6, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Today, lets understand how to use Calculated items feature in [Pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
**. We will use a practical problem many of us face to learn this feature – _ie calculating conversion ratio from a list of sales calls._

This is inspired from a question [posted by Nicki in our forums](http://chandoo.org/forums/topic/calculated-fields-in-pivot-tables "Calculated fields - forum question")
,

> I have a spreadsheet source data full of sales enquiries which have the Status – Lost, Booked or Pending. Each sales enquiry relates to a particular location. I have created a pivot table which counts the enquiries and displays them with the Locations in rows and the Status in the columns. I have got a row total showing the total number of sales enquiries for each location. I also want my table display the sales conversion number, ie the booked enquiries as a % of the total enquiries. How do I do this?

### A look at the data

Lets say, you have some data like this and you want to understand what is the conversion ratio by location.

![Calculating conversion ratios from sales enquiry data](https://img.chandoo.org/pivot/conversion-ratio-calculation-data.png)

### Setup a pivot table

The first step is to just create a pivot table from this data. Put locations in row labels area, status in column labels are and ID in values area. Now you will have a count of items for each status in each location. Something like this:

![Frist version of pivot table - showing distribution of items by status](https://img.chandoo.org/pivot/initial-pivot-table.png)

### Add a calculated item to get conversion ratio

Now we want to calculate how much percentage is “booked” status items in all items for a location. To do this,

1.  Select any column label item in the pivot table.
2.  Click on Pivot Options > Fields, Items & Sets > Calculated item  
    ![Inserting calculated item from pivot table options ribbon](https://img.chandoo.org/pivot/insert-calculated-item-excel.png)
3.  Give your calculated item a suitable name like Conv. %
4.  Write the formula = Booked / (Booked + Pending + Lost)  
    ![Calculated item for conversion percentage - Excel pivot tables](https://img.chandoo.org/pivot/creating-calculated-item-in-excel-pivot-tables.png)
5.  Click ok.

Now you should see another column in your pivot table with calculated item – Conversion %.

![Conversion ratio calculated - but shown as number...!](https://img.chandoo.org/pivot/conversion-ratio-calculated-1.png)

### Formatting Conversion % in Percentage format

While we got what we wanted, it is not looking alright. We need to format the conversion % so that it looks alright. For this,

1.  Right click on any value in pivot table
2.  ![Custom number formatting rule to show conversion ratios in %s](https://img.chandoo.org/pivot/custom-number-format-rule-conversion-ratio.png)Go to value field settings
3.  Click on number format
4.  Select custom
5.  Type the custom formatting rule \[>=1\]0;\[<1\]0%;””
6.  This will automatically transform all numbers smaller than 1 (ie all conversion %s) to percentage format while keeping everything else normal.
7.  Done!

**Resource: [Learn more about custom number formatting](http://chandoo.org/wp/tag/custom-cell-formatting/)
**

A video tutorial explaining this & more
---------------------------------------

Since calculated items can be somewhat tricky, I made a short video explaining how this works. In the video you can also see how to use Power Pivot measures to calculate conversion ratios easily. Watch it below (or on [our youtube channel](http://youtu.be/KOtJgRVtej8)
).

Download Example workbook
-------------------------

**[Click here to download example workbook](https://files.chandoo.org/power-pivot/conversion-ratio.xlsx)
.** It has both regular and powerpivot based calculations. Go ahead and examine them. Enjoy.

### Do you use Calculated items?

I find calculated items to be very tricky to work with. In most cases, I try to add extra calculations to original data table or use formulas instead. But this example is a good case where calculated item is perfect.

**What about you?** Do you use Calculated items? In what situations you use them? _**Please share your experiences and tips using comments.**_

### Convert your self to a Pivot table pro…

If you are use Excel pivot tables & data analysis features, then you will find below resources very useful.

*   [Pivot table tips & tricks](http://chandoo.org/wp/2010/01/27/pivot-table-tricks/)
    
*   [Grouping data in Pivot tables](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)
    
*   6 part tutorial: [Using pivot tables for financial reporting](http://chandoo.org/wp/2010/02/04/profit-loss-reporting-in-excel-1/)
    
*   [Using report filters in pivot tables](http://chandoo.org/wp/2011/04/20/pivot-table-report-filters/)
    
*   [Using slicers in Excel 2010 pivot tables to create powerful dashboards](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
    
*   [Introduction to Power Pivot](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/ "What is Power Pivot – an Introduction ")
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [calculated items](https://chandoo.org/wp/tag/calculated-items/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [powerpivot](https://chandoo.org/wp/tag/powerpivot/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

[PrevPreviousWork with several Excel files everyday? – Save them as a workspace \[Quick tip\]](https://chandoo.org/wp/excel-workspace-tip/)

[NextHow to remove all cells containing John (or anything else) \[Quick tip\]Next](https://chandoo.org/wp/remove-all-rows-with-specific-value-excel/)

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
    
    [Reply](https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/finding-conversion-ratio-using-pivot-table-calculated-items/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ