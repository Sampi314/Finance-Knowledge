# Spreadsheet Risk Management Software Reviews - Which tool to use for Auditing / Risk Management of Excel Spreadsheets

**Source:** https://chandoo.org/wp/spreadsheet-risk-management-software-review

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Using external software packages to manage your spreadsheet risk \[Part 4 of 4\]
================================================================================

*   Last updated on February 8, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This series of articles will give you an overview of how to manage spreadsheet risk. These articles are written by _**Myles Arnott**_ from [Excel Audit](http://www.excelaudit.co.uk/)

*   [Part 1: An Introduction to managing spreadsheet risk](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    
*   [Part 2: How companies can manage their spreadsheet risk](http://chandoo.org/wp/2012/01/03/how-companies-can-manage-spreadsheet-risk/)
    
*   [Part 3: Excel’s auditing functions](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
    
*   **Part 4: Using external software packages to manage your spreadsheet risk**

![Introduction to Spreadsheet Risk Management](https://chandoo.org/img/g/spreadsheet-risk-management.png)

**Background – Spreadsheet Risk Management**
--------------------------------------------

In the [Managing Spreadsheet Risk series](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/ "Introduction to Spreadsheet Risk Management")
 so far we have looked at the concept of spreadsheet risk and how to manage it both at a company level and at a spreadsheet level using Excel functionality. In this final article we are going to have a quick look at an example of spreadsheet auditing software.

What to look for in a Spreadsheet Risk Management Software
----------------------------------------------------------

First off I should state that there is a wide range of spreadsheet auditing solutions in the marketplace of different types and styles and at a variety of costs. In this section I would like to take a little time to explain the criteria we applied when we were sourcing auditing software.

**These were our requirements:**

*   Robust, well proven software rated by its existing users and the industry
*   A stand-alone solution rather than an Excel add-in
*   Functionality:
    *   Produce a list of spreadsheets within a directory and provide details of their key attributes to enable prioritization by complexity profile
    *   Perform the core audit checks and provide facility to record audit notes
    *   Compare two spreadsheets in order to identify changes

### Our Recommendation

Based on these requirements we chose [EXChecker from Finsbury Solutions](http://www.finsburysolutions.com/products-exchecker.htm)
. The functionality and screen shots below are of EXChecker being used to audit the spreadsheet that we reviewed in part 3 of this series. ([Download Part 3 Excel Workbook](https://img.chandoo.org/g/excel-risk-management/Managing%20Spreadsheet%20Risk%20Illustration.xlsm)
)

Auditing software in action
---------------------------

The first thing to note is that EXChecker opens a copy of the spreadsheet within the EXChecker program and stores your audited version in a specified directory, the original is untouched.

Once you open the spreadsheet the software automatically un-hides hidden rows and columns and hidden (and very hidden) workbooks. This can be seen in row 15 which the software has unhidden and highlighted in red:

![Unhide all rows & columns - Spreadsheet Risk Management](https://img.chandoo.org/g/excel-risk-management/unhide-rows-columns-excel-risk-management.png "Unhide all rows & columns - Spreadsheet Risk Management")

**EXChecker enables you to carry out a wide range of auditing tests such as**: identifying errors; spreadsheet links; macros; numbers stored as text; hard coded numeric; high risk functions; and duplicated formulas.

We will focus on three pieces of functionality so that we can compare them to the Excel functions that we used in [Part 3 of this series](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/ "Excel's Auditing Functions - Spreadsheet Risk Management")
.

Map cell Input/Outputs
----------------------

Selecting “Map cell Input/Outputs” applies a color format to the cells containing constants and formulas as we achieved via my macro in Part 3. The formatting is applied to all worksheets automatically.

![Map Cell Inputs and color them accordingly](https://img.chandoo.org/g/excel-risk-management/map-cell-inputs-outputs.png "Map Cell Inputs and color them accordingly")

Highlight Formulas
------------------

Selecting “Highlight formulas” identifies the cells containing formulas as achieved by my macro but also applies different textures to indicate where a formula is not consistent with those around it:

![Highlight Formulas in an Excel Workbook](https://img.chandoo.org/g/excel-risk-management/highlight-formulas.png "Highlight Formulas in an Excel Workbook")

Workbook Summary
----------------

The Workbook Summary function performs a full audit of the spreadsheet and then outputs the results in a separate spreadsheet that can be incorporated into the audit report.

This is a comprehensive set of audit checks and a very powerful tool. It very quickly provides you with essential information that would take considerably more time to achieve manually.

![Workbook Summary as displayed by EXChecker - Spreadsheet Risk Management](https://img.chandoo.org/g/excel-risk-management/workbook-summary.png "Workbook Summary as displayed by EXChecker - Spreadsheet Risk Management")

One important check within the Workbook Summary function that I would draw your attention to is the **“Show all invisible/masked cells”** analysis. This returns all of the cells that have been made invisible in some way. The comment against cell U5 below should set alarm bells ringing: **“Font + Cell colours match”.**

I’ve purposefully avoided the “F word” so far in this series as the vast majority of spreadsheet errors are just that, errors. Some people do innocently hide cell contents using white on white formatting (please don’t!) but this is a strong indicator for potential fraud and worth reviewing in further detail.

Conclusion
----------

Hopefully this series has given you an insight into the potential risks that spreadsheets pose and also some methods for mitigating those risks. Whilst the articles have only been a brief introduction to the topic of spreadsheet risk management, I would like to think that it has given you the tools to implement a safer spreadsheet environment and the appetite to learn more about the subject.

### What about you?

Do you use any external tools or software to manage spreadsheet risk? What is your experience with them? How do you use these tools? **Please share your recommendations & tips thru comments.**

### Thank you Myles

Many thanks to _Myles_ for writing this series. Your experience in this area is invaluable. If you enjoy this series, drop a note of thanks to Myles thru comments. You can also reach him at [Excel Audit](http://www.excelaudit.co.uk/)
 or [his linkedin profile](http://uk.linkedin.com/in/clarityconsultancyservicesma)
.

### Disclosure

_Chandoo.org is not affiliated with Finsbury Solutions. Our review of EXChecker is purely based on what Myles thought about it._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/spreadsheet-risk-management-software-review/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/spreadsheet-risk-management-software-review/#respond)
    
*   Tagged under [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [risk management](https://chandoo.org/wp/tag/risk-management/)
    , [spreadsheet audit](https://chandoo.org/wp/tag/spreadsheet-audit/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousComparing 2 Lists with a Twist](https://chandoo.org/wp/comparing-2-lists-with-a-twist/)

[NextFormula Forensics 011. Lykes FormulaNext](https://chandoo.org/wp/formula-forensics-011/)

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