# Adding Calculated Fields to Pivot Table P&L [part 3 of 6] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/p-l-reports-calculated-fields-3

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Adding Calculated Fields to Pivot Table P&L \[part 3 of 6\]
===========================================================

*   Last updated on April 21, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**This is part 3 of 6 on Profit & Loss Reporting using Excel series**, written by _[Yogesh](http://www.yogeshguptaonline.com/)
_

[Data sheet structure for Preparing P&L using Pivot Tables](http://chandoo.org/wp/2010/02/04/profit-loss-reporting-in-excel-1/)
  
[Preparing Pivot Table P&L using Data sheet](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
  
[](http://chandoo.org/wp/2010/02/25/p-l-reports-calculated-fields-3/)
**Adding Calculated Fields to Pivot Table P&L**  
[Exploring Pivot Table P&L Reports](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/)
  
[Quarterly and Half yearly Profit Loss Reports in Excel](http://chandoo.org/wp/2010/03/24/qtrly-half-yearly-pl-reports-5/)
  
[Budget V/s Actual Profit Loss Report using Pivot Tables](http://chandoo.org/wp/2010/04/21/budget-v-actual-profit-loss-reports-6/)

![Adding Calculated Fields to Profit & Loss (P&L) Pivot Report](https://chandoo.org/img/ea/calculated-fields-in-profit-loss-report-3.png)This is continuation of our earlier post [Preparing Pivot Table P&L using Data](http://chandoo.org/wp/2010/02/10/profit-loss-reports-excel-2/)
. We have learned to prepare Pivot Table P&L. The report prepared in last post has all the major data to prepare a P&L but it is not a complete P&L report. Now we will add calculated fields to make it a complete P&L. We will also format data points to make it a complete P&L report.

### We need the following extra values in our P&L

*   Gross Margin = Sales – Cost of Goods Sold
*   Gross Margin % = Gross Margin / Sales
*   Operating Expenses = Rent + Personnel Cost + Utilities + Consumables + Misc Exp
*   Operating Profit = Gross Margin – Operating Expenses
*   Operating Profit % = Operating Profit / Sales

### Making these extra fields in Pivot Table using Calculated Fields Features:

Click on PivotTable Tools > Calculated Items to define a new calculated field. \[tutorial: [how to add calculated fields to pivot tables](http://chandoo.org/wp/2010/01/27/pivot-table-tricks/#calculated_fields)\
\]

Check out below screencast. Just replace the Field Names and Formulas to add the rest of the calculated fields.

![Adding Calculated Fields in Pivot Tables - Ex. Gross Margin Calculation in P&L](https://img.chandoo.org/ea/add-calculated-fields-pivot-table.gif)

Once you have added all the calculated fields to Pivot Table, these will start showing at the end of PivotTable. You will need to drag them to their respective position on P&L

![Drag Fields inside Pivot Table](https://img.chandoo.org/ea/drag-data-in-pivots.gif)

Now you are almost ready with your P&L report, only few steps more to format data are required. _**You may have noticed that % Fields are showing as zero as of now.**_ This is because they are formatted as numbers instead of _percentages_.

Do not use standard cell formatting to format them, instead **use Value Field Setting Option to format pivot table fields**. This one is useful as it will show data always as per the format set for particular field. Use Percentage format for % fields and Accounting Format for other value fields.

![Number Format - Pivot Table Fields](https://img.chandoo.org/ea/number-format-from-field-settings.png)

Few More steps like formatting certain fields as bold and italics and your PivotTable P&L is ready, you can play with is as any other pivot table and start presenting on various dimensions with few clicks

Make sure that you have correctly setup “Preserve Cell Formatting on update” option under pivot table options. This will help you retain the same format while you play with your PivotTable P&L.

![Enable Preserve Cell Formatting Setting in Pivot Report](https://img.chandoo.org/ea/preserve-cell-formatting-pivots.png)

### The Final Profit & Loss Pivot Report

Once you finish all the formatting and settings, this is how the final report should look like:

![profit-loss-report-with-calculated-fields](https://chandoo.org/img/ea/profit-loss-report-with-calculated-fields.png)

### Download the profit and loss report excel file

[Download the excel file](https://img.chandoo.org/ea/adding-calculated-fields.xls)
 and play with it to understand the techniques discussed in this post.

### What Next?

In the next part of this series, we [explore this pivot table further, Continue reading](http://chandoo.org/wp/2010/03/03/explore-profit-loss-reports-4/ "Exploring Profit Loss Pivot Reports")
.

### Added by PHD:

*   Please share your feedback and ideas for this series using comments. _Yogesh_ and I will reply to your questions. Also, say thanks if you like the idea and want to learn more.
*   **[Sign-up for PHD E-mail newsletter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
    ** because you will get updates as new posts are live.

![Yogesh Gupta - CA, Excel Blogger](https://chandoo.org/img/ea/yogesh-profile-pic.png)**Yogesh** is an accountant with 13 years of experience in India and abroad. His specialties are budgeting and costing, supplier accounting, negotiation of contracts, cost benefit analysis, MIS reporting, employees accounting. He writes about excel at [http://www.yogeshguptaonline.com/](http://www.yogeshguptaonline.com/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/p-l-reports-calculated-fields-3/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/p-l-reports-calculated-fields-3/#respond)
    
*   Tagged under [calculated fields](https://chandoo.org/wp/tag/calculated-fields/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [formatting](https://chandoo.org/wp/tag/formatting/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [profit loss reports](https://chandoo.org/wp/tag/profit-loss-reports/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [yogesh](https://chandoo.org/wp/tag/yogesh/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousUse Paste Special to Speed up Chart Formatting \[Quick Tip\]](https://chandoo.org/wp/paste-special-chart-formatting/)

[NextSachin Tendulkar ODI Stats – an Excel Info-graphic PosterNext](https://chandoo.org/wp/sachin-tendulkar-odi-poster/)

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
    
    [Reply](https://chandoo.org/wp/p-l-reports-calculated-fields-3/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/p-l-reports-calculated-fields-3/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/p-l-reports-calculated-fields-3/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ