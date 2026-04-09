# How to "auto" generate calendar tables with Power Query - The best method » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/power-query-calendar-table-best-method

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to “auto” generate calendar tables with Power Query – The best method
=========================================================================

*   Last updated on December 30, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![automatic calendar table with power query](https://chandoo.org/wp/wp-content/uploads/2023/08/automatic-CALENDAR-TABLE-POWERBI.jpg)

Calendar (or date) table is crucial for performing _**date intelligence**_ calculations in Power BI. 

Normally, you would find a reasonable calendar table in most data models. But occasionally I come across models where there is no calendar table. 

So I present to you, the **ultimate & best way to generate calendar table using Power Query.**

How to create the perfect calendar table with Power Query?
----------------------------------------------------------

Start by creating a new “blank query” connection in Power BI.

![blank query option in Power BI (PQ)](https://chandoo.org/wp/wp-content/uploads/2023/08/SNAG-2885.png)

Then use the =List.Dates() function to generate the dates you want.

For example, to get the calendar dates for year 2025 use below code:

				
					`= List.Dates(#date(2025,1,1),365, #duration(1,0,0,0))`
				
			

This will generate a list of all the dates in 2025. 

Now, convert the list to a table using the List Tools > Transform ribbon. 

![convert list of dates to a table](https://chandoo.org/wp/wp-content/uploads/2023/08/SNAG-2886.png)

Once you have the dates in a table format, you can use the “add column” ribbon and “Date” options to introduce many date related columns.

For example you can add:

*   Year (4 digit year value)
*   Month number
*   Month name
*   Weekday name
*   Weekday number
*   Start of month
*   End of month
*   Start of week
*   Quarter of the year
*   Days in a month

![Adding date calculations with Power Query](https://chandoo.org/wp/wp-content/uploads/2023/08/SNAG-2887.png)

Additional "smart" date columns
-------------------------------

Apart from all the columns above, I normally add these two columns to my calendar tables.

*   Year month (a 6 digit representation like 202308 for ex.)
*   Type of month (current month, previous month, next month)

Let’s look at the Power Query (M) code for these columns.

### Year Month (yyyymm):

				
					`= Table.AddColumn(#"Inserted Start of Month", "Year Month", each [Year] * 100 + [Month])`
				
			

### Type of Month:

For this we need to do use conditional logic and isinmonth functions of M. Here is the M code for tagging dates as “previous month”, “this month” and “next month”

				
					`= Table.AddColumn(#"Added Custom", "Month Type", each if Date.IsInCurrentMonth([Date]) then "This Month" else if Date.IsInPreviousMonth([Date]) then "Previous Month"  else if Date.IsInNextMonth([Date]) then "Next Month"  else "Other Month")`
				
			

Full M Script for generating the 2025 calendar table
----------------------------------------------------

Use this M script to generate the calendar table for year 2025. 

To apply this, create a blank query in PQ and then go to View > Advanced Editor and paste the code there. Adjust the year in source step (step 1) to get the calendar for any year.

				
					`let     Source = List.Dates(#date(2025,1,1),365, #duration(1,0,0,0)),     #"Converted to Table" = Table.FromList(Source, Splitter.SplitByNothing(), null, null, ExtraValues.Error),     #"Renamed Columns" = Table.RenameColumns(#"Converted to Table",{{"Column1", "Date"}}),     #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Date", type date}}),     #"Inserted Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),     #"Inserted Month" = Table.AddColumn(#"Inserted Year", "Month", each Date.Month([Date]), Int64.Type),     #"Inserted Month Name" = Table.AddColumn(#"Inserted Month", "Month Name", each Date.MonthName([Date]), type text),     #"Inserted Day of Week" = Table.AddColumn(#"Inserted Month Name", "Day of Week", each Date.DayOfWeek([Date]), Int64.Type),     #"Inserted Day Name" = Table.AddColumn(#"Inserted Day of Week", "Day Name", each Date.DayOfWeekName([Date]), type text),     #"Added Conditional Column" = Table.AddColumn(#"Inserted Day Name", "Is Weekend?", each if [Day of Week] = 6 then "Yes" else if [Day of Week] = 0 then "Yes" else "No"),     #"Inserted Start of Month" = Table.AddColumn(#"Added Conditional Column", "Start of Month", each Date.StartOfMonth([Date]), type date),     #"Added Custom" = Table.AddColumn(#"Inserted Start of Month", "Year Month", each [Year] * 100 + [Month]),     #"Added Custom1" = Table.AddColumn(#"Added Custom", "Month Type", each if Date.IsInCurrentMonth([Date]) then "This Month" else if Date.IsInPreviousMonth([Date]) then "Previous Month"  else if Date.IsInNextMonth([Date]) then "Next Month"  else "Other Month") in     #"Added Custom1"`
				
			

Perfect Calendar with Power Query - Video
-----------------------------------------

Check out this video to understand the process better.

How to customize the Calendar Query for other years?
----------------------------------------------------

You can change the “Source” step and replace the year number or number of days to generate the calendar for whatever year you need. For example, to make the 2 years calendar for years 2026 and 2027, use this code:

				
					`= List.Dates(#date(2026,1,1),730, #duration(1,0,0,0))`
				
			

**To make the calendar for next “n” years:**

We can use additional date functions in Power Query M language to generate the calendar for next “n” years from a start date. For example, if you change the source step to below code, you will get next 5 years calendar from 1-Jan-2025.

				
					`= let start_date = #date(2025,1,1), number_of_years = 5, end_date = Date.AddYears(start_date,number_of_years), total_days = Duration.Days(end_date - start_date) in List.Dates(start_date,total_days, #duration(1,0,0,0))`
				
			

More ways to make the calendar table
------------------------------------

Check out below tutorials from other Power BI / Excel folks to see different Power Query scripts.

*   [All in one script for calendar table – Radacad](https://radacad.com/all-in-one-script-to-create-date-dimension-in-power-bi-using-power-query)
    
*   [Parameterized Date Tables – BI Gorilla](https://gorilla.bi/power-query/date-table/)
    
*   [Auto generate calendar table with MonkeyTools add-in](https://monkeytools.ca/calendar-monkey/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/power-query-calendar-table-best-method/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-query-calendar-table-best-method/#respond)
    
*   Tagged under [calendar table](https://chandoo.org/wp/tag/calendar-table/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousTop 10 Accounting KPIs and How to Calculate them in Excel?](https://chandoo.org/wp/top-10-accounting-kpis-excel/)

[NextCP03: The Ugly Truth About Power BI (actually, 4 of them)Next](https://chandoo.org/wp/cp03-the-ugly-truth-about-power-bi/)

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
    
    [Reply](https://chandoo.org/wp/power-query-calendar-table-best-method/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/power-query-calendar-table-best-method/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/power-query-calendar-table-best-method/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ