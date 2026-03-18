# How windy is Wellington? - Using Power Query to gather wind data from web » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How windy is Wellington? – Using Power Query to gather wind data from web
=========================================================================

*   Last updated on February 22, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Let’s take a whirlwind trip to coolest little capital – Wellington.** It is a windy place, so hold on to your hats and spreadsheets.

Almost everyone who spends more than 2 days in Wellington would agree that it is a _windy_ place. But how windy is Welly? In this two part series, we will use Power Query, Excel charts and coffee to answer that question.

But, first let’s start with a joke.

_**What happens when you throw a boomerang in Frank Kitts Park?**_

You will have to buy another one, coz you are not getting that one back.

Extracting the wind data
------------------------

In order to understand how windy Wellington is, we need to get average wind speeds by day for last several days. Let’s get the data for last 2+ years (ie from 1 Jan 2016 to 21 Feb 2018).

There are many places where you can collect latest wind data. But when it comes to historical wind data, surprisingly few resources are available. We can use [The National Climate database – CliFlo](https://cliflo.niwa.co.nz/)
, to gather wind data. But the interface is confusing and I could only locate gust speeds, rather than average wind speeds over time.

We can use [wunderground.com](https://www.wunderground.com/history/airport/NZWN/)
 to fetch weather data for up to 13 months at a time.

_**But we need data for almost 26 months.**_

Very simple, we can query wunderground twice (or thrice), once per each year.

The historical data query URL looks like this:

https://www.wunderground.com/history/airport/NZWN/**2016**/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=**2016**&req\_city=&req\_state=&req\_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=

All we had to do is, change **2016** to 2017 & 2018 to get respective data.

The actual data set will be a web page. But we can use power query to extract the portion of page that contains weather information.

On to Power Query – Building our Weather Data Extractor
-------------------------------------------------------

Note: This is a slightly advanced tutorial on PQ. If you are a beginner, start with [Introduction to Power Query](https://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
 and work thru examples on [PQ tag](http://chandoo.org/wp/tag/power-query)
 page before reading any more.

### Getting data from the web – building URL in parts

Open Excel and go to Data > New Query > From Other Sources > Web

![](https://chandoo.org/wp/wp-content/uploads/2018/02/get-data-from-web-power-query.png)

_For Power BI, this would be Edit Queries > New Source > Web_ 

Switch to “Advanced” mode and enter the URL as parts like below. We will switch the _**2016**_ part to parameters soon, so we could get data for any year easily.

![](https://chandoo.org/wp/wp-content/uploads/2018/02/url-with-parts-power-query.png)

In the navigation pane, select “Table 1” which is the weather table.

### Set up a parameter for Year

How would we get data for 2017 or 2018? Simple, we use parameters. These are like variables which can be plugged in to any part of your Power Query process.

In Power Query Editor, go to Home > Manager Parameters > New Parameter and call it Year. Enter the default value as 2016.

Now, go back and edit the source settings for the query and replace 2016s with parameter Year.

![](https://chandoo.org/wp/wp-content/uploads/2018/02/parameterized-query.png)

### Cleaning the weather table

Turns out the weather data table is not clean. Although there are 366 days in 2016 (leap year), Wunderground adds headers for each month. So we end up with 378 rows (excluding the header). Each header contains month name and repeat of all the column names. We can extract the month name & combine that with date and **_year parameter_** to create the date for each row.

![](https://chandoo.org/wp/wp-content/uploads/2018/02/extra-rows-weather-data.png)

**Here is a quick illustration of what we need to do.**

![](https://chandoo.org/wp/wp-content/uploads/2018/02/cleaning-weather-data-steps-needed.png)

### But first, rename the very first column

Notice the first column? It is called as 2016. This is ok if we are interested in just 1 year of data. But if we re-run this query with Parameter=2017, our column heading will change. If you have dabbled with Power Query a few times, you will quickly realize that PQ will get in to a nasty fit anytime column headers change and impact downstream steps.

Simple, we shall rename it as FirstCol.

When you apply the new name, PQ will write this M instruction.

#”Renamed Columns”= Table.RenameColumns(Data1,{{“2016”, “First col”}})

This is not a fool proof solution, as when we change parameter to 2017, there won’t be a 2016 column in that new table.

So, instead, we can ask PQ to rename _first_ column of the table.

You can do this by:

*   Note: You need “Formula Bar”. Enable “Formula Bar” by clicking View > Formula bar. This way you can actually see all the M code PQ is cranking up whenever you perform some actions on your data.![](https://chandoo.org/wp/wp-content/uploads/2018/02/add-steps-fx-button-power-query.png)
*   Click on _fx_ button on the formula bar to insert a step. Simply type = Table.RenameColumns(Data1,{{Table.ColumnNames(Data1){0}, “First col”}})
*   Press Enter
*   Bingo, you have renamed the first column of your query to “First col”. This has no reference to 2016 or any year, so it should work on any table you fetch from that weather data page.

### Cleaning the weather data – steps

Just follow these steps to clean the weather data.

1.  Add a custom column called Month and write this formula = if Text.Length(\[First col\]) > 2 then \[First col\] else null![](https://chandoo.org/wp/wp-content/uploads/2018/02/custom-column-to-extract-month-names-power-query.png)
2.  Select Month column and Fill Down (Transform > Fill >Down)![](https://chandoo.org/wp/wp-content/uploads/2018/02/power-query-fill-down.png)
3.  Select First col and change its type to whole number. This will make all month names as _Error_
4.  Remove errors from First col (Right click on column header and choose Remove Errors)
5.  Add a custom column called Date with the formula = Text.From(\[First col\])&”-“&\[Month\]&”-“&_**Year**_
6.  Change this column to date type.
7.  Keep only Temp. (°C)2, Wind (km/h), Wind (km/h)2, Wind (km/h)3, Events, Date columns and remove all other
8.  Rename first four columns to Avg. Temp, Wind Max, Avg. Wind, Wind Gust

At this stage we have one year of wind and temperature data for Wellington. Time to create getWeatherData() function.

Making getWeatherData function in Power Query
---------------------------------------------

Now that we have a parameterized query, just right click on the query and choose “Convert to Function”

PQ will build the function that can take **_year_** as input and return a table of weather data for that year (provided Wunderground.com co-operates)

Now, we just need to run this function three times, once each for 2016, 2017 and 2018 to get all the data.

### Go back to Excel

Save your queries, but don’t load them yet. If PQ prompts about data load, select “Connection only” and jump to Excel.

*   Create a table with 3 rows and type 2016, 2017 and 2018 in that. Call this table Years.
*   Load this table to Power Query (Data > From Table)
*   Go to Add Column > Invoke Custom Function and invoke getWeatherData function for each year.
*   Expand the weather data tables.
*   Done!

At this stage, we have data for all 3 years. You can add some data clean up steps if you want. But all the wind & temperature data is here for us to analyze and visualize.

Download Example Workbook
-------------------------

[**Click here to download the Wellington Wind workbook**](https://chandoo.org/wp/wp-content/uploads/2018/02/wellington-wind-v2.xlsx)
. As you can see, I have added few more steps in PQ to clean up the data and include a “Is it windy?” conditional column.

**Please note that this workbook is designed in Excel 2016.** It may not work in older versions of Power Query. You can replicate most of the steps. Try doing it so that you will learn more about Power Query.

In the next part – Wind in Wellington – few visualizations
----------------------------------------------------------

In the next part of this tutorial, we will build some visualizations to understand how windy Wellington gets and what is the best time to enjoy the beautiful outdoors.

Stay tuned.

**How are you using Power Query?** Please post about your power query escapades in the comments section. Also tell me how you went about re-creating the steps in this tutorial. I am all ears.

_Why there are no undercover cops in Wellington?_ Their cover was always getting blown. That is why.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousThis year, become a Very Table Genius](https://chandoo.org/wp/this-year-become-a-very-table-genius/)

[NextStay on top of money with this awesome household budget spreadsheet \[downloads\]Next](https://chandoo.org/wp/budget-spreadsheet-download/)

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
    
    [Reply](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ