# How to import web data to Excel using Power Query » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/import-web-data-power-query

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to import web data to Excel using Power Query
=================================================

*   Last updated on August 19, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Power Query offers many ways to get data to Excel. One of them is to Web Data import feature. Let’s understand how this works by importing world stock exchange closing data from [Google Finance website](https://www.google.com/finance)
.

\[Related: [Introduction to Power Query](http://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)\
\]

### Importing web data in to Excel – Step by step tutorial

Note: You need Power Query for this tutorial. Install Power Query on Excel 2013 ([how to](https://www.microsoft.com/en-in/download/details.aspx?id=39379)
) and continue reading.

1.  Open a blank workbook. Go to Power Query ribbon & click on **From Web** button. Enter the URL of the webpage from which you want to import the data.  
    ![web-data-button-power-query-ribbon](https://chandoo.org/wp/wp-content/uploads/2015/08/web-data-button-power-query-ribbon.png)
2.  Your web page will be loaded in to Navigator pane. If there are any tables or other sections of the page that can be readily embedded in Excel, they will show up in the navigation tree structure. Hover on any table to see if that is the data you want. Once you identify what you need, click on Load to get this data in to Excel. If you want to pre-process the data before loading in to Excel, click on Edit.  
    ![preview-of-webdata-power-query](https://chandoo.org/wp/wp-content/uploads/2015/08/preview-of-webdata-power-query.png)
3.  Let’s say you have taken Table 0, which contains stock market closing data around the world. When this is edited in Power Query window, it looks like this.  
    ![webdata-loaded-to-pq-window](https://chandoo.org/wp/wp-content/uploads/2015/08/webdata-loaded-to-pq-window.png)
4.  As you can see, there are 2 problems with this data. (1) Column headers are missing (2) Column 3 should be splitted in to 2 columns.
5.  **Renaming columns:** Simply double click on column headers and write whatever header you want.
6.  **Splitting a column:** Select column 3 and Click on home > split column button in Power Query window. Specify the delimiter (in our case space should work) and click ok.  
    ![split-column-space-as-delimiter-power-query](https://chandoo.org/wp/wp-content/uploads/2015/08/split-column-space-as-delimiter-power-query.png)
7.  Once column is spitted, our new set up looks like below. Column 3.2 needs further cleaning. We need to remove the brackets ( ).  
    ![data-after-splitting-column-power-query](https://chandoo.org/wp/wp-content/uploads/2015/08/data-after-splitting-column-power-query.png)
8.  **Removing the brackets:** Select column 3.2 and click on Home > Replace values button. Replace ( with nothing. Repeat the replacement, but this time replace ) with nothing.  
    ![replace-brackets](https://chandoo.org/wp/wp-content/uploads/2015/08/replace-brackets.png)
9.  Almost done. Our data is clean. Just change the column titles and we get this:  
    ![processed-web-data-power-query](https://chandoo.org/wp/wp-content/uploads/2015/08/processed-web-data-power-query.png)
10.  Finally load this data to Excel by clicking on “Close & Load” button. Instantly, all this web data will be loaded to Excel as a new table.  
    ![load-data-to-Excel](https://chandoo.org/wp/wp-content/uploads/2015/08/load-data-to-Excel.png)

### How to refresh the imported data?

Simple. Do one of the below:

*   Click on “Refresh all” button in Data ribbon of Excel
*   Right click on Excel table with web data and choose “Refresh”
*   Activate workbook queries pane (from Power Query ribbon) and refresh the query by clicking on the refresh icon at right.

### Download Power Query web data – Example workbook

[**Please click here to download the workbook with Power Query web data extraction example**](https://chandoo.org/wp/wp-content/uploads/2015/08/power-query-web-data-example.xlsx)
. Right click on the query in workbook queries pane and edit it to understand the pre-processing steps better.

### What awesome things can you do with web data in Excel?

Integrating your own data with publicly available sources can lead to interesting analysis situations. Power Query, Power BI & **[Power Pivot](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/)
** offer several ways to connect to web data (Facebook, Azure market place, Google Analytics etc.) and analyze it in Excel.

**Have you tried importing web data to Excel?** What has been your experience like? **_Please share your tips & thoughts in the comments section._**

### More ways to analyze web data in Excel:

Learn more about analyzing web data in Excel

*   [Find nearby zipcodes using WEBSERVICE() Excel function](http://chandoo.org/wp/2013/03/18/finding-nearby-zipcodes-using-excel-formulas/)
    
*   [Import stock quotes to Excel using VBA](http://chandoo.org/wp/2010/06/02/excel-stock-quotes/)
    
*   [Import mutual fund data in to Excel and build a tracker \[case study\]](http://chandoo.org/wp/2009/12/28/mutual-fund-tracker-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/import-web-data-power-query/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/import-web-data-power-query/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [refresh](https://chandoo.org/wp/tag/refresh/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousDashboard best practice: Highlight user selection](https://chandoo.org/wp/dashboard-selection-highlight/)

[NextSave time & paper with print areas in ExcelNext](https://chandoo.org/wp/print-areas/)

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
    
    [Reply](https://chandoo.org/wp/import-web-data-power-query/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/import-web-data-power-query/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/import-web-data-power-query/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ