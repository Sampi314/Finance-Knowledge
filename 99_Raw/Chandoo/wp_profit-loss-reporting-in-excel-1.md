# Profit & Loss Reporting using Microsoft Excel - Accounting & Excel - Part 1 of 6

**Source:** https://chandoo.org/wp/profit-loss-reporting-in-excel-1

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

P&L Reporting using Excel \[Part 1 of 6 on Excel & Accounting\]
===============================================================

*   Last updated on April 21, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is a guest post by [Yogesh](http://www.yogeshguptaonline.com/)
**, a chartered accountant and excel blogger._

![P&L Reporting using Excel [Part 1 of 6 on Excel & Accounting]](https://chandoo.org/img/ea/excel-accounting-pl-reports-1.png "P&L Reporting using Excel [Part 1 of 6 on Excel & Accounting]")**With this post we are starting a new series on how to do basic accounting in Microsoft Excel.**

In this and next 5 posts, we will aim to setup Profit & Loss account reporting for multi-location retail company.

During this series we will learn how to make P&L reports on various criteria with just few clicks.

Many users find it difficult to manage their P&L reporting for Multi Location organization.

We will be using Pivot Tables for our reporting purpose and will take example of a Retails chain with multiple locations divided into various regions. It is recommended that you be familiar with the [concept of pivot tables](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
 and also familiar with [basic accounting terms](http://www.a-systems.net/accounting-terms.htm)
.

### Topics covered in this series:

[](http://chandoo.org/wp/2010/02/04/profit-loss-reporting-in-excel-1/)
**Data sheet structure for Preparing P&L using Pivot Tables**  
[Preparing Pivot Table P&L using Data sheet](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
  
[Adding Calculated Fields to Pivot Table P&L](http://chandoo.org/wp/2010/02/25/p-l-reports-calculated-fields-3/)
  
[Exploring Pivot Table P&L Reports](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/)
  
[Quarterly and Half yearly Profit Loss Reports in Excel](http://chandoo.org/wp/2010/03/24/qtrly-half-yearly-pl-reports-5/)
  
[Budget V/s Actual Profit Loss Report using Pivot Tables](http://chandoo.org/wp/2010/04/21/budget-v-actual-profit-loss-reports-6/)

**Do not think that series is not only about the Profit and Loss Account. _This is also about Pivot Tables._** We will cover many Pivot Table tricks during our series. I hope you will be able to use those tricks elsewhere too.

### Data sheet structure for Preparing P&L using Pivot Tables

Data is most important part of the entire reporting requirements. You should plan your reporting needs in advance and collect data accordingly. Initial investments in organizing data properly will help you in long run for your reporting requirements.

Data needs to be in table format on separate sheet. First row of the data should be table headers and following rows to contain the data.

![Data sheet structure for Preparing P&L using Pivot Tables](https://chandoo.org/img/ea/data-layout-excel-accounting-1.png "Data sheet structure for Preparing P&L using Pivot Tables")

You need to have all the possible dimensions in your data. This will help you to quickly change your P&L report on different dimensions.

_**A dimension is defined as**_ “…a data element that categorizes each item in a data set into non-overlapping regions” [according to Wikipedia](http://en.wikipedia.org/wiki/Dimension_%28data_warehouse%29)
.

The above data structure will give us flexibility to prepare P&L report by,

1.  Geography-wise
2.  State-wise
3.  City-wise
4.  Store-wise
5.  Month-wise – This can be further grouped on Quarterly / Six Monthly / Yearly reporting

Calendar related data points should be entered as date. You can see that the month column in the data is showing Jan.2009 but it is actually entered as date January 31, 2009 then formatted as MMM.YYYY

This gives you flexibility to group data by quarterly / Six Monthly / Yearly for reporting. \[[learn more about grouping dates in pivot reports](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)\
\]

**It is advisable to have it as last date of the month**; this gives you further flexibility to do calculations based on number of days during the month.

There is no need to have calculated data in your data table, you may notice that I do not have calculated figures in the data sheet. **Data points like Gross Margins, Margin % , Operating Profit and Operating Profit % will be calculated in Pivot Table [using calculated field option](http://chandoo.org/wp/2010/01/27/pivot-table-tricks/#calculated_fields)
**.

During this series we will cover how to make P&L report on these dimensions using sample data. You can download sample data for practice along with our posts.

### Download this Data:

[Click here to download this data file in .xls format](https://img.chandoo.org/ea/data-profit-loss-reporting-1.zip)
. We will use this data in next part to prepare our initial pivot table.

This data is prepared using RANDBETWEEN function of Excel for usage in this series.

### What Next?

In the next part of this series, learn [how to make a pivot table for Profit Loss Reporting using this data](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
.

### Added by PHD:

*   I know as much about accounting as a cow knows about pie charts. So I asked _Yogesh_, a CA with vast experience and passion for excel, to write for us. I am very thankful to him for accepting this offer and sharing his knowledge.
*   Please share your feedback and ideas for this series using comments. _Yogesh_ and I will reply to your questions. Also, say thanks if you like the idea and want to learn more.
*   **[Sign-up for PHD E-mail newsletter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
     so that you don’t miss any new posts**

![Yogesh Gupta - CA, Excel Blogger](https://chandoo.org/img/ea/yogesh-profile-pic.png)**Yogesh** is an accountant with 13 years of experience in India and abroad. His specialties are budgeting and costing, supplier accounting, negotiation of contracts, cost benefit analysis, MIS reporting, employees accounting. He writes about excel at [http://www.yogeshguptaonline.com/](http://www.yogeshguptaonline.com/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [16 Comments](https://chandoo.org/wp/profit-loss-reporting-in-excel-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/profit-loss-reporting-in-excel-1/#respond)
    
*   Tagged under [accounting](https://chandoo.org/wp/tag/accounting/)
    , [data](https://chandoo.org/wp/tag/data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [profit loss reports](https://chandoo.org/wp/tag/profit-loss-reports/)
    , [RANDBETWEEN()](https://chandoo.org/wp/tag/randbetween/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [yogesh](https://chandoo.org/wp/tag/yogesh/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousExcel Keyboard Shortcuts – Open Thread](https://chandoo.org/wp/excel-keyboard-shortcuts-2/)

[NextBest Month Ever (and a charting tip inside)Next](https://chandoo.org/wp/best-month-jan2010/)

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