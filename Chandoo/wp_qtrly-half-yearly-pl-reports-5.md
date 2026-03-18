# Quarterly & Half-Yearly Profit Loss Reports in Excel [Part 5 of 6]

**Source:** https://chandoo.org/wp/qtrly-half-yearly-pl-reports-5

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Quarterly & Half-Yearly Profit Loss Reports \[Part 5 of 6\]
===========================================================

*   Last updated on April 21, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**This is part 5 of 6 on Profit & Loss Reporting using Excel series**, written by _[Yogesh](http://www.yogeshguptaonline.com/)
_  
![Quarterly & Half-Yearly Profit Loss Reports](https://chandoo.org/img/ea/quarterly-half-yearly-profit-loss-reports-excel.png "Quarterly & Half-Yearly Profit Loss Reports")

[Data sheet structure for Preparing P&L using Pivot Tables](http://chandoo.org/wp/2010/02/04/profit-loss-reporting-in-excel-1/)
  
[Preparing Pivot Table P&L using Data sheet](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
  
[Adding Calculated Fields to Pivot Table P&L](http://chandoo.org/wp/2010/02/25/p-l-reports-calculated-fields-3/)
  
[Exploring Pivot Table P&L Reports](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/)
  
[](http://chandoo.org/wp/2010/03/24/qtrly-half-yearly-pl-reports-5/)
**Quarterly and Half yearly Profit Loss Reports in Excel**  
[Budget V/s Actual Profit Loss Report using Pivot Tables](http://chandoo.org/wp/2010/04/21/budget-v-actual-profit-loss-reports-6/)

This is continuation of our earlier post [**Exploring Profit Loss Pivot Reports**](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/)
.

We have learned how to change our P&L report on various data elements. We have seen how the P&L report can be changed with just few clicks.

**In this post we will be learning some grouping tricks in PivotTables.** We will cover grouping of dates, text fields and numeric fields. You will need to start with Monthly P&L report prepared in previous post.

### Grouping Profit Loss Report based on Dates

*   Right click on date field > Choose Group > Choose Quarters from dates grouping dialog box > click OK.
*   [Tutorial: Grouping Dates in Pivot Tables](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)
    .

Once done your quarterly P&L is ready, you can still filter it on any other filed. Checkout screen cast for quarterly P&L prepared and filtered on City filed to make Quarterly P&L for Amritsar City.

![Quarterly Profit Loss Report in Excel using Pivot Tables](https://chandoo.org/img/ea/grouping-by-quarter-pl-report.gif)

Not only this, you can also drag grouped data to page area and Geography field to column area of PivotTable. Now you can filter it on Qtr1 to make Geography wise P&L for Qtr1.

\[[Click here to see how to do this](http://chandoo.org/img/ea/profit-loss-reports-excel-grouping-2.gif)\
\]

This one is simple as it groups January to March period as Qtr1, April to June as Qtr2 and so on.

### Grouping Dates based on Apr-Mar Financial Year

**Most of the Indian companies follow April to March as Financial Year.** _**They start with April to June as Qtr1 and finish with January to March as Qtr4.**_ You will need different steps if you want make April to June as Qtr1 and January -March as Qtr4.

In our Data we have January 2009 to March 2009 period as Qtr 4 of 08-09 Financial Year. Grouping steps are as under

*   Select January to March month columns > right click on selected columns > Choose Group.
*   Rename Group1 as Q4.08-09
*   Follow similar steps to Group April 2009 to June 2009 as Q1.09-10 and so on.
*   \[[Click here to see how to do this](http://chandoo.org/img/ea/profit-loss-reports-excel-grouping-3.gif)\
    \]
*   Drag the grouped field out of PivotTable in case you want to remove grouping.

The final report looks like this:

![Grouping by Financial Year - Profit Loss Reports in Excel](https://chandoo.org/img/ea/grouping-dates-by-financial-year.png)

Many companies follow different Financial Year. In case your company follows May to April as Financial Year, you can select May June and July months and group them as Qtr1. You have the flexibility to select particular periods and group them. You can input name of the group as you want.

**In similar way you can group 6 months to make half yearly Profit Loss Report in Excel.**

### Grouping Profit Loss Report Based on Text Fields

You can group data on text fields. In Geography wise P&L you can group South and East column to make P&L for South East.

You can select non consecutive columns :- Click on East column > Press Ctrl > Click on South column while you keep Ctrl key pressed. You will see that you have both the columns selected.

Select East and South Column > Right Click > Choose Group > Rename Group1 as South East.

Drag the grouped field out of PivotTable in case you want to remove grouping.

\[[Click here to see how this is done](https://img.chandoo.org/ea/profit-loss-reports-excel-grouping-4.gif)\
\]

### Grouping Profit Loss Report based on Numbers

You can also group data on numeric fields. We will make a PivotTable P&L grouping stores based on their size. Prepare P&L on store sizes by dropping store area field into column area of PivotTable.

Right Click on Store Area filed > Choose Group > Enter grouping parameters in Group dialog box > Click OK

You have the P&L for stores grouped based on their size.

![Grouping by Store Size - Profit Loss Reports in Excel](https://chandoo.org/img/ea/grouping-numeric-fields-excel.gif "Grouping by Store Size - Profit Loss Reports in Excel")

### Putting it all together – Creating a Custom Profit Loss Report Layout in Excel:

You can explore your PivotTable P&L in any combinations discussed in this post and our previous post.

_**So how about making South East Geography P&L for Q1 only of stores sized 4000 – 4999, like this?**_

![Custom Profit Loss Report Layout in Excel](https://chandoo.org/img/ea/custom-profit-loss-report-layout.png)

It is just few clicks and your P&L will be ready , watch out screencast.

\[this is a heavy screencast, so [click thru](http://chandoo.org/img/ea/profit-loss-reports-excel-grouping-final.gif)\
 if you want to watch it\].

### Dealing with “Cannot group that selection” error:

While grouping fields in PivotTable you may get a message saying “Cannot group that selection”. This happens due to blank date / number field or text in date / number field. You may have some blank rows in the data causing this problem. Some time you may have second copy of date field shown as Month2 or date2. This is duplicate field created in PivotTable which is already grouped. You will need to un-group this before grouping date filed again differently if required.

### Download Excel file with all these example Pivot Reports:

[Download Profit Loss Report Excel file](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/ea/profit-loss-reports-excel-grouping.zip)
 and practice all these tricks on your own. \[[mirror download location](http://chandoo.org/img/ea/profit-loss-reports-excel-grouping.zip)\
\]

### What Next?

In the next part of this series, learn [how to prepare budget vs. actual profit-loss reports](http://chandoo.org/wp/2010/04/21/budget-v-actual-profit-loss-reports-6/)
.

Meanwhile, make sure you have read the first 4 parts of this series – [Data sheet structure](http://chandoo.org/wp/2010/02/04/profit-loss-reporting-in-excel-1/)
, [Preparing P&L Pivot Table](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
, [Adding Calculated Fields](http://chandoo.org/wp/2010/02/25/p-l-reports-calculated-fields-3/)
 and [Exploring Profit Loss Report Pivot](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/)

Also check out the [Excel Pivot Tables – Tutorial](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
, [Pivot Table Tricks](http://chandoo.org/wp/2010/01/27/pivot-table-tricks/)
, [Grouping Dates in Pivot Reports](http://chandoo.org/wp/2009/11/17/group-dates-in-pivot-tables/)
 articles to get more ideas.

### Added by PHD:

*   **Say thanks if you like the idea and want to learn more.**
*   Please share your feedback and ideas for this series using comments. _Yogesh_ and I will reply to your questions.
*   **[Sign-up for PHD E-mail newsletter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
    ** because you will get updates as new posts go online.

![Yogesh Gupta - CA, Excel Blogger](https://chandoo.org/img/ea/yogesh-profile-pic.png)**Yogesh** is an accountant with 13 years of experience in India and abroad. His specialties are budgeting and costing, supplier accounting, negotiation of contracts, cost benefit analysis, MIS reporting, employees accounting. He writes about excel at [http://www.yogeshguptaonline.com/](http://www.yogeshguptaonline.com/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/qtrly-half-yearly-pl-reports-5/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/qtrly-half-yearly-pl-reports-5/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [group by quarter](https://chandoo.org/wp/tag/group-by-quarter/)
    , [group ungroup](https://chandoo.org/wp/tag/group-ungroup/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [profit loss reports](https://chandoo.org/wp/tag/profit-loss-reports/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    , [yogesh](https://chandoo.org/wp/tag/yogesh/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousHow to Convert Text to Dates \[Data Cleanup\]](https://chandoo.org/wp/text-to-date-convertion/)

[NextMy First Podcast!!! – Listen to know some cool charting and dashboard stuffNext](https://chandoo.org/wp/my-first-podcast/)

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