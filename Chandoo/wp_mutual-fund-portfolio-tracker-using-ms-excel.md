# Free Mutual Fund Tracker using Excel - Download and Tutorial

**Source:** https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

Mutual Fund Portfolio Tracker using MS Excel
============================================

*   Last updated on July 6, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2018/07/mutual-fund-tracker-excel.png)

**Would you like to spend next 5 minutes learning how to create an mutual fund tracker excel sheet?**  Make a live, updatable mutual fund portfolio tracker for Indian markets to keep track of your investments using this example.

* * *

**[Download the mutual fund tracker – India](https://chandoo.org/wp/wp-content/uploads/2018/07/mutual-fund-tracker-India.xlsx)
 now.**

* * *

_**NOTE: File updated on 7 July 2018 to fix errors. Download again if you need to.**_

### How to use this mutual fund tracker Excel workbook?

1.  Download and save the file to a folder on your computer (do not leave it in the downloads folder)
2.  Open the file in Excel (you need Excel 2016 / Office 365 to use this file. If you are using older version of Excel, you need free Power Query add-in)
3.  If prompted, enable “External connections”
4.  Go to Data and click on Refresh all
5.  This will fetch updated funds list and latest NAV (Net Asset Value) from AMFI India website.
6.  On the My Funds page, specify the funds you own, units, purchase price and purchase date
7.  The tracker will calculate your return, CAGR (Compounded annual growth rate of funds) and simple return of your portfolio and display it
8.  When you want to see updated value of your portfolio, simply refresh the tracker (Data > Refresh All or press CTRL+ALT+F5)

### How this mutual fund tracker is made?

We will use 3 simple excel features to achieve this – **[Power Query](https://chandoo.org/wp/resources/introduction-to-power-query/)
, [Cascading Drop downs](https://chandoo.org/wp/cascading-drop-down/)
** and **[vlookup()](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
**

1.  First, **lets put a tabular format for our portfolio:** We can have fund name, # of units, purchase NAV (Net Asset Value, the cost of unit for your when you bought it), purchase date, total value at purchase (units \* purchase NAV), current NAV (we will pull this data from internet), value as of now (units \* current NAV), Profit / loss amount and profit / loss % as our table columns. Once you learn how to do this, you can add more columns depending on what / how you want to track your MF portfolio.When you finish creating the table, it would look something like this:[![Mutual fund tracker excel - portfolio view (click to enlarge)](https://chandoo.org/wp/wp-content/uploads/2018/07/snapshot-of-mutual-fund-tracker-excel.png)](https://chandoo.org/wp/wp-content/uploads/2018/07/snapshot-of-mutual-fund-tracker-excel.png)
    
2.  Next we will use Power Query to automatically fetch the funds and latest fund value from AMFI website. This site maintains updated funds and values and publishes the list as TXT file at URL- https://www.amfiindia.com/spages/NAVAll.txt We can connect to this page as web URL from PQ and setup some simple rules to clean the data and extract the relevant bits we need. The result looks like this in Power Query editor.[![Mutual funds list from AMFI - view in Power Query](https://chandoo.org/wp/wp-content/uploads/2018/07/view-of-funds-data-in-power-query-editor.png)](https://chandoo.org/wp/wp-content/uploads/2018/07/view-of-funds-data-in-power-query-editor.png)
    
3.  Once we load this data to Excel, we can build a simple 2 level cascading drop-down system to capture details on the “my funds” page. That way, our drop down will be small and easy to use. [Please read cascading drop downs page](https://chandoo.org/wp/cascading-drop-down/)
     for details on how to do this.
4.  Finally, based on the fund name, we fetch the NAV and NAV date using, you guessed it – [VLOOKUP formula](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    . The rest is easy to calculate.
5.  Now as you input fund names and refresh data, your portfolio gets updated.![](https://chandoo.org/wp/wp-content/uploads/2018/07/power-query-and-refresh.png)

**Few ideas on how you can enhance this:**

*   Add graphs to see visually how the funds are doing
*   Build some VBA to store previous NAV values of your funds so that you can see historical dates

### Problems with MF Tracker?

*   **I cannot refresh data:** You need internet connection. You also need Power Query for Excel (this is available by default in Excel 2016 or above, Office 365. If you have an older version of Excel, [download Power Query add-in](https://www.microsoft.com/en-nz/download/details.aspx?id=39379)
     for free.
*   **I see some error during download / refresh:** The AMFI people have been inconsistent with their file formatting. It could be a weekly issue (ie every Friday they might be publishing some extra data.) Try again in a day or two. If the problem persists, post a comment so I can suggest a work around.
*   **Some other problem:** Please post a comment so I can look in to this for you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [275 Comments](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [how to](https://chandoo.org/wp/tag/how-to/)
    , [investing](https://chandoo.org/wp/tag/investing/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [mutualfunds](https://chandoo.org/wp/tag/mutualfunds/)
    , [personal finance](https://chandoo.org/wp/tag/personal-finance/)
    , [portfolio tracker](https://chandoo.org/wp/tag/portfolio-tracker/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [stock](https://chandoo.org/wp/tag/stock/)
    , [technology](https://chandoo.org/wp/tag/technology/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

[PrevPreviousPlay spreadsheet soccer with Excel Penalty Game \[VBA\]](https://chandoo.org/wp/excel-penalty-game/)

[NextCalculate travel time and distance between two addresses using Excel + Maps APINext](https://chandoo.org/wp/distance-between-places-excel-maps-api/)

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
    
    [Reply](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/mutual-fund-portfolio-tracker-using-ms-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ