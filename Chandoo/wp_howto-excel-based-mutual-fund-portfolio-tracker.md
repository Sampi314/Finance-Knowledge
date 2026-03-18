# Howto: Excel Based Mutual Fund Portfolio Tracker » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)
    

Howto: Excel Based Mutual Fund Portfolio Tracker
================================================

*   Last updated on February 3, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Instead of searching for the NAVs of all my funds at [MyIRIS](http://myiris.com/)
 or [MutualFundsIndia](http://mutualfundsindia.com/)
, I have developed a small excel sheet which will fetch the values for me and displays the current portfolio value at the click of a button. Here I am trying to share the “HOWTO” of the same.

1.  Create an excel workbook with 2 sheets. Call one as “NAVs” and the other as “Portfolio”.
2.  In the NAVs sheet, click at one of the top-left cells (I did on A2), and go to Data -> Import External Data -> New Web Query. \[For more information on using Web Queries, visit [Using Web Queries to Import Data to Excel](http://r1c1.blogspot.com/2006/09/using-web-queries-to-import-data-to.html "Using Web Queries to Import Data to Excel")\
     @ [R1C1](http://r1c1.blogspot.com/ "R1C1")\
    .\
3.  Now paste the url [http://finance.indiamart.com/markets/mutual\_funds/latest\_mf\_navs.html](http://finance.indiamart.com/markets/mutual_funds/latest_mf_navs.html)\
     in Address box and press go. You would see something like this.  \
    ![](https://chandoo.d.googlepages.com/portfolio_tracker1.JPG)  \
    Say “Import”. Essentially what you have done is, creating an automatically updatable NAV list in the NAVs sheet.\
4.  Now select all Schemes in the imported table and define a named range as “fund\_names” for it. \[[Creating Named Ranges in Excel](http://www.homeandlearn.co.uk/ME/mes9p2.html "Creating Named Ranges in Excel")\
    \]\
5.  Now, go to “Portfolio” sheet and create a table like this.  \
    [![](https://chandoo.d.googlepages.com/portfolio_tracker2.JPG)](http://chandoo.d.googlepages.com/portfolio_tracker2.JPG)\
      \
    **\[Click on it to Zoom\]**\
6.  Next select the Fundname column (I have 32 rows, you can have as many as you wish) and go to Data->Validation. Enter the settings like this.  \
    ![](https://chandoo.d.googlepages.com/portfolio_tracker3.JPG)\
7.  **_Formulas:_**  \
    \>>> For Purchase Value\[f3\]: “=e3\*d3”  \
    \>>> For Current Value\[h3\]: “=g3\*d3”  \
    \>>> For Current NAV\[g3\]: “=IF(C3=””,0,VLOOKUP(C3,NAVs!$A$6:$D$1634,3,FALSE))”  \
    essentially, looking up for the selected fund name in the NAVs sheet and returning the exact NAV to this cell **_only if_** a fund name is selected.  \
    \>>> Gain / Loss\[i3\]: “=IF(ISERROR((H3-F3)/F3),””,(H3-F3)/F3)”  \
    **_to avoid DIV 0 messages._**\
8.  At the end of the table you can add a TOTAL row and repeat the necessary formulas to get the total portfolio performance.\
9.  Now the portfolio tracker is done. Enter the fund data by selecting the fund name from drop down and number of units purchased, purchase NAV. Rest will be shown by the tracker.\
10.  **Remember:** everytime you open the workbook, go to “NAVs” sheet and refresh the data. \[Select anywhere in the table, right click and say **_Refresh Data_**\]\
\
Now this is a very basic portfolio tracker. I am thinking of adding some VBA / Macro so that everytime the table is refreshed, the new values are written in a separate sheet called “Historical NAV” so that we can track the fund performance over a period of time by selecting a date (instead of current date). Also, if we can import benchmark indices on runtime, you can get relative performance metrics. Plus, some more analysis of fund performances (instead of mere total return) would reveal the risk-returns of the portfolio. Lets see if I can build such a thing in my spare time.\
\
\[Just in case you do not have time for all this, then you can access the workbook that I have created here: [Portfolio Manager MFs India](http://chandoo.d.googlepages.com/Portfolio_Manager_MFs_India.xls "Portfolio Manager MFs India")\
 \]\
\
Facebook\
\
Twitter\
\
LinkedIn\
\
**Share this tip** with your colleagues\
\
![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)\
\
### Get FREE Excel + Power BI Tips\
\
Simple, fun and useful emails, once per week.  \
  \
**Learn & be awesome.**\
\
*   [5 Comments](https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker/#comments)\
    \
*   [Ask a question or say something...](https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker/#respond)\
    \
*   Tagged under [analysis](https://chandoo.org/wp/tag/analysis/)\
    , [finance](https://chandoo.org/wp/tag/finance/)\
    , [fun](https://chandoo.org/wp/tag/fun/)\
    , [India](https://chandoo.org/wp/tag/india/)\
    , [information](https://chandoo.org/wp/tag/information/)\
    , [iris](https://chandoo.org/wp/tag/iris/)\
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)\
    , [performance](https://chandoo.org/wp/tag/performance/)\
    , [searching](https://chandoo.org/wp/tag/searching/)\
    , [web](https://chandoo.org/wp/tag/web/)\
    \
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)\
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)\
    \
\
[PrevPreviousLessons in Pricing from Murugan Idli Shop](https://chandoo.org/wp/lessons-in-pricing-from-murugan-idli-shop/)\
\
[NextSweet NothingsNext](https://chandoo.org/wp/sweet-nothings/)\
\
![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)\
\
### Welcome to Chandoo.org\
\
Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  \
  \
[Read my story](https://chandoo.org/wp/about/)\
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)\
\
[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)\
\
[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)\
\
[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)\
\
Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.\
\
![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)\
\
Rebekah S\
\
Reporting Analyst\
\
[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)\
\
[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)\
\
[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)\
\
From simple to complex, there is a formula for every occasion. Check out the list now.\
\
[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)\
\
[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)\
\
Calendars, invoices, trackers and much more. All free, fun and fantastic.\
\
[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)\
\
[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)\
\
Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.\
\
[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)\
\
[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)\
\
Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.\
\
Recent Articles on Chandoo.org\
\
[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.\
\
[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)\
\
### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)\
\
[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)\
\
### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)\
\
[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
Best of the lot\
\
*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)\
    \
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)\
    \
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)\
    \
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)\
    \
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)\
    \
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)\
    \
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)\
    \
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)\
    \
\
Related Tips\
------------\
\
[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
Learn Excel\
\
### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
Excel Challenges\
\
### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
Excel Howtos\
\
### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)\
\
Excel Howtos\
\
### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)\
\
[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)\
\
Excel Howtos\
\
### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)\
\
[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)\
\
Excel Howtos\
\
### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)\
\
### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”\
\
1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:\
    \
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)\
    \
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.\
    \
    [Reply](https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker/#comment-2107616)\
    \
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)\
         says:\
        \
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)\
        \
        Good question. You can check for the =0 as countifs result. for example,  \
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  \
        should work in this case.\
        \
        PS: I have added this example to the article now.\
        \
        [Reply](https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker/#comment-2107623)\
        \
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)\
     says:\
    \
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)\
    \
    Hi there!\
    \
    Could i check if there was a way to return certain fields of the table only?\
    \
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).\
    \
    [Reply](https://chandoo.org/wp/howto-excel-based-mutual-fund-portfolio-tracker/#comment-2122498)\
    \
\
### Leave a Reply\
\
[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)\
\
 Name (required)\
\
 Mail (will not be published) (required)\
\
 Website\
\
  \
\
 Notify me of when new comments are posted via e-mail\
\
Δ