# How Companies Can Manage Spreadsheet Risk [Part 2 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How Companies Can Manage Spreadsheet Risk \[Part 2 of 4\]
=========================================================

*   Last updated on April 24, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This series of articles will give you an overview of how to manage spreadsheet risk. These articles are written by _**Myles Arnott**_ from [Excel Audit](http://www.excelaudit.co.uk/)

*   Part 1: [An Introduction to managing spreadsheet risk](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    
*   **Part 2: How companies can manage their spreadsheet risk**
*   Part 3: [Excel’s auditing functions](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
    
*   Part 4: Using external software packages to manage your spreadsheet risk

![Introduction to Spreadsheet Risk Management](https://chandoo.org/img/g/spreadsheet-risk-management.png)

In the first article in this series we highlighted the risks that poorly managed spreadsheet solutions can introduce to a business. In this article we will demonstrate how companies can manage this risk.

A formal governance framework
-----------------------------

The first, and arguably most important step is to ensure that the senior management team buy into the need for a robust spreadsheet risk management framework, and that they define and effectively communicate their spreadsheet risk management policy.

Spreadsheets identified and catalogued
--------------------------------------

It is impossible to know the level of spreadsheet risk in an organization without first identifying and then risk assessing all of the spreadsheets. It is therefore necessary to create a catalog of all of the spreadsheets and then to gather the key information about each spreadsheet to enable a risk assessment to be carried out.

The two key factors for determining the spreadsheet risk are the probability of there being an error and the impact that that error could have.

Risk = Probability of an error  X  impact if an error were to occur

The **probability** of error is related to the complexity of the spreadsheet. Complexity attributes differ across companies but include:

*   Spreadsheet size (Mbs)
*   Spreadsheet design (hard coded numbers in formulae, poor model structuring etc)
*   The number of users
*   The use of complex formulae (particularly array formulae, nested formulae etc)
*   The number of cells populated
*   The number of internal and external links
*   The use of VBA

The **impact** of the error is related to how critical the spreadsheet is within the business. Each company will have a slightly different definition of the impact levels of spreadsheets, but generally:

*   A spreadsheet is low impact if it is not used as part of a critical business process and an error would not have a material impact on the business.
*   A spreadsheet is medium impact if it contains confidential information and an error could have a material impact on the business.
*   A spreadsheet is high impact if it contains highly confidential information and an error would have a significant impact on the business. Spreadsheets used within processes that fall under external regulation (such as Sarbanes-Oxley and Solvency II) are deemed to be of high impact.

Finally, the spreadsheets should be placed in order of risk. Those identified as business critical and high risk should be prioritized for detailed review and placed under control.

This is clearly an on-going process. As new spreadsheets are developed they will need to pass through the risk assessment process as defined by the company’s spreadsheet risk management policy. A periodic review should also be carried out to ensure that all spreadsheets have been correctly categorized.

A best practice standard
------------------------

The company should define its own best practice spreadsheet development standard that is applied to spreadsheets deemed to be medium or high impact. The standard should clearly outline the standards and conventions to which a spreadsheet should be built. New developments can then be reviewed to ensure that they adhere to the standard.

We advocate the use of the Excel Best Practice Standard from the [Spreadsheet Standards Review Board](http://www.ssrb.org/index.html)
 (‘SSRB’).

We also recommend that tailored schedules are added to the standard to reflect your specific design standards. For example this could be a specific color scheme, use of logo or the use of specific text within the header or footer (e.g. document security levels).

Testing
-------

A fundamental, but often overlooked step in the Excel model development cycle is testing. All spreadsheets (but especially business critical spreadsheets) need to be first peer reviewed and then rigorously tested.

It helps to consider the steps that an IT department would take to ensure that something they deliver is correct. It will pass through stages of unit and system testing prior to quality assurance and finally user acceptance testing. So why should a spreadsheet being used for a critical process be any different?

The fact is that no matter how hard we try, humans make errors. The purpose of testing is to identify them and get them resolved before the model goes into the live environment.

Remember that in the first article we highlighted the fact that 94% of spreadsheets and 5% of all formulae within spreadsheets contain errors.

Here is [Scott Adams’ view on spreadsheet testing in Dilbert](http://dilbert.com/strips/comic/2004-12-26/)

Training
--------

All staff should be trained so that they have sufficient Excel knowledge for their role and to use the spreadsheets that they are responsible for. As part of the induction process all staff should also be taught the company’s best practice standard.

Whilst this sounds obvious, research has shown that few companies prioritize investment in spreadsheet training.

**Documentation**
-----------------

A key risk with spreadsheets is that they are often built and used by one individual within a team (often referred to as a “key man dependency”). If this person is ill or leaves unexpectedly the other members are totally reliant on the documentation left behind. From experience this rarely exists.

Each spreadsheet that is used within a process should as a bare minimum have documentation stating:

*   the purpose of the spreadsheet;
*   how the spreadsheet fits within the process;
*   the source of all inputs for the spreadsheet;
*   all key assumptions and drivers;
*   key calculations;
*   distribution list for outputs.

Spreadsheets that are part of as critical business process should have detailed documentation. This should include a technical specification and user notes.

**Security**
------------

All business critical and confidential spreadsheets should be subject to access control. Security controls can be implemented across three levels:

*   Directory level: Only specific individuals have access to key directories
*   File level: Confidential and critical spreadsheets should be password protected to restrict access
*   Cell level: Non-input cells should be password protected

Change control, backups and archives
------------------------------------

To minimize the risk of losing the current version of a spreadsheet and ensuring that the correct version is being used at all times, all business critical spreadsheets should be backed up, archived and subject to change control procedures.

So, in summary..,
-----------------

_**the characteristics of a well-managed environment are:**_

*   a formal governance framework, sponsored by the senior management team, is in place for all spreadsheet development;
*   a catalog of spreadsheets is maintained and prioritized by risk profile;
*   a best practice standard is applied to the development of all new spreadsheets;
*   all new spreadsheets pass through a formal risk assessment, are peer reviewed and formally tested;
*   staff are provided with sufficient training to carry out their roles;
*   all spreadsheets and their associated processes are well documented;
*   access to critical spreadsheets is subject to security controls;
*   spreadsheets are subject to change control and are regularly backed up and archived.

What next?
----------

In the next article we will look at the [built in Excel functions that can help you to manage spreadsheet risk](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
.

### What about you?

How do you (or your company) manage spreadsheet risk? What best practices & guidelines you follow? _**Please share using comments.**_

### Thank you Myles

Many thanks to _Myles_ for writing this series. Your experience in this area is invaluable. If you enjoy this series, drop a note of thanks to Myles thru comments. You can also reach him at [Excel Audit](http://www.excelaudit.co.uk/)
 or [his linkedin profile](http://uk.linkedin.com/in/clarityconsultancyservicesma)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [9 Comments](https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk/#respond)
    
*   Tagged under [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [risk management](https://chandoo.org/wp/tag/risk-management/)
    , [spreadsheet audit](https://chandoo.org/wp/tag/spreadsheet-audit/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFree Picture Calendar Template – Download and make a personalized calendar today!](https://chandoo.org/wp/picture-calendar-template/)

[NextQuick Update about VBA Classes & Discount Expiry!Next](https://chandoo.org/wp/quick-update-about-vba-classes-discount-expiry/)

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
    
    [Reply](https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-companies-can-manage-spreadsheet-risk/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ