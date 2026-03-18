# Implementing Modular Spreadsheet Development - a walkthrough » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/msd-implementation-examples

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Implementing Modular Spreadsheet Development – a walkthrough
============================================================

*   Last updated on May 21, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This article is written by Michael Hutchens from [Best Practice Modelling](http://www.bestpracticemodelling.com/)
._

In the [first article on Modular Spreadsheet Development](http://chandoo.org/wp/2014/05/07/modular-spreadsheet-development-a-thought-revolution/ "Modular Spreadsheet Development – A Thought Revolution")
, we got a high level overview of Modular Spreadsheet Development principles. This article discusses the practical implementation of these principles in Excel.

A quick review
--------------

In my first article, I discussed the infinite potential provided by Modular Spreadsheet Development to improve the way spreadsheets are built, used, shared and communicated.

This is made possible by sub-dividing spreadsheets into _modules_, which can be re-used and linked like Lego® pieces, thereby reducing model build time and the risk of errors.

![profitability_model_modules - MSD Implementation in Excel](https://chandoo.org/wp/wp-content/uploads/2014/05/profitability_model_modules1.png)

These concepts were well received by Chandoo’s readers, although some concerns were raised about their practical implementation in Microsoft Excel. This article aims to address those concerns.

Overview of implementation methods
----------------------------------

From my experience using Modular Spreadsheet Development over the past decade, there are three increasingly-efficient methods of implementation in Microsoft Excel:

1.  Manual implementation;
2.  VBA automated implementation; and
3.  Commercial add-in implementation.

I will provide an overview of each of these methods and a summary of their advantages and disadvantages.

### 1\. Manual Implementation

The key to implementing Modular Spreadsheet Development is _standardization_, because it is the robust consistency created by standardized spreadsheets that makes it possible to interchange the modules within a spreadsheet.

There are numerous approaches to spreadsheet standardization (my organization uses the [Best Practice Spreadsheet Modeling Standards](http://www.bestpracticemodelling.com/standards/overview)
), but the key requirement of any standardized approach for Modular Spreadsheet Development purposes is _consistency_. Once this consistency is present, re-using and sharing modular content within spreadsheets becomes surprisingly easy.

Let’s consider an example ( ➡ [**download example files**](https://chandoo.org/wp/wp-content/uploads/2014/05/msd-examples.zip)
 ) in which a model developer has built a dynamic 3-way financial statement model. This model contains various modules, ranging from revenues and expenses through to financial statements and a dashboard module that looks as follows:

![financial_model_dashboard](https://chandoo.org/wp/wp-content/uploads/2014/05/financial_model_dashboard.png)

After completing this model, the model developer decides to add an equity valuation. Creating the equity valuation assumptions and outputs from scratch is a big job, and a risky one given the complexity of the discounted cash flow (DCF) valuation formulas required.

Luckily, the model developer has included an equity valuation in a prior model, and had the foresight to keep a copy of this _equity valuation module_ in a standalone workbook called _Equity Valuation.xlsb_. The composition of this module is shown below:

![equity_valuation_module_composition](https://chandoo.org/wp/wp-content/uploads/2014/05/equity_valuation_module_composition.png)

This _equity valuation module_ contains four components; an assumptions component, a calculation outputs component, an outputs summary component and a lookups component (to hold drop down box control lookup data).

From an Excel perspective, this module is a workbook with these four components placed on three sheets; one assumptions sheet, one outputs sheet and one lookups sheet, as shown below (the lookups sheet is to the right of the image):

![equity_valuation_toc_annotated](https://chandoo.org/wp/wp-content/uploads/2014/05/equity_valuation_toc_annotated.png)

Each of these components is comprised of blocks of entire rows that contain Excel content (such as constants, formulas, controls, hyperlinks, etc.) that together undertake an equity valuation. For example, the top sections of the equity valuation _assumptions component_ are shown below:

![equity_valuation_module_assumptions](https://chandoo.org/wp/wp-content/uploads/2014/05/equity_valuation_module_assumptions.png)

Rather than try to re-build all of this content into the financial model, the model developer decides to implement Modular Spreadsheet Development and insert this _equity valuation module_ into the financial model.

Two steps are required to do this:

1.  Collectively copy the sheets containing the _equity valuation module_ components into the financial model workbook from the workbook containing the _equity valuation module_; then
2.  Insert formulas into the equity module assumptions to link this module to the surrounding financial model outputs, and thereupon calculate the DCF equity valuation.

To copy the sheets containing the _equity valuation module_ components into the financial model workbook, the following actions are required:

1.  Activate the _Equity Valuation.xlsb_ workbook;
2.  Collectively select the three sheets containing the _equity valuation module_ components (i.e. the sheets named _Eq\_Val\_Ann\_TA_, _Eq\_Val\_Ann\_TO_ and _Eq\_Val\_LU_) and copy them to the end of the _Financial Model.xlsb_ workbook using the Excel Move or Copy sheets command, as shown below:  
    ![move_or_copy_sheets_dialog](https://chandoo.org/wp/wp-content/uploads/2014/05/move_or_copy_sheets_dialog.png)
3.  Click the OK button (or press/hold down the Enter key) each time you are asked to use the destination workbook version of a range name. This will happen quite a few times in this example, as range names have been used in the time series parts of the model to ensure consistency;
4.  Move the inserted sheets into their appropriate locations within the _Financial Model.xlsb_ workbook – i.e. move the sheet containing the equity valuation assumptions into the assumptions section of the workbook, etc.; then
5.  Update any necessary surrounding content within the financial model workbook, such as the table of contents, to reflect the inclusion of these sheets.

After doing this, the newly-inserted equity valuation module needs to be linked to other modules within the financial model in order to correctly calculate the DCF equity valuation. This is a complex example, but for those familiar with DCF valuations, the following data must be linked into the equity valuation module:

1.  Cash flow available to equity;
2.  Tax paid;
3.  Earnings before interest, tax, depreciation and amortization (EBITDA); and
4.  Closing debt balances.

You can learn more about DCF valuation theory from the [financial modelling resources on the Best Practice Modelling website](http://www.bestpracticemodelling.com/resources/knowledge/business_planning/outputs_other/dcf_valuation_theory)
.

After doing this, the financial model contains a DCF equity valuation, as shown below in the table of contents, which has been compacted to highlight the newly-added components:

![financial_model_with_equity_valuation_toc](https://chandoo.org/wp/wp-content/uploads/2014/05/financial_model_with_equity_valuation_toc.png)

Amazingly, this sophisticated equity valuation analysis was inserted into the financial model in minutes, with only a few formulas required to link it to the surrounding model outputs. As a result, assuming that the source _equity valuation module_ has integrity, the model developer instantly has confidence that the new equity valuation in the financial model is also reliable and correct.

As demonstrated by these steps, the manual implementation of Modular Spreadsheet Development is somewhat fiddly, but it is possible as long as the content within all workbooks and module files is sufficiently standardized to support interchanging components.

The implementation steps used in this simple example can be used to insert any pre-existing module into an existing modular spreadsheet, thereby greatly reducing model development time, cost and risk.

### 2\. VBA automated implementation

Excel users with intermediate to advanced VBA skills will probably have recognised while reading the manual implementation steps that VBA code can be written to automate to automate the majority of this process.

A full discussion and example VBA code is outside the scope of this article, but if you’re considering have a go at this here are some general tips:

1.  Use a user form containing list box control with its _MultiSelect_ property set to _fmMultiSelectMulti_ to allow users to select the sheets containing the module assumptions and outputs to be imported;
2.  Ensure that _Application.DisplayAlerts_ is set to _FALSE_ before running the code used to copy sheets to prevent prompts being displayed to users; and
3.  Use the VBA _Range.Replace_ function to redirect formula links after moving the imported module assumptions and outputs onto existing sheets.

These steps were in fact the steps that I first took when developing an add-in for our organization to automate the insertion of modules. 10 years later, this add-in is called [bpmModules](http://www.bestpracticemodelling.com/resources/bpmmodules)
, and I’ve provided an overview of it below.

### 3\. Commercial add-in implementation

When I first started implementing Modular Spreadsheet Development, I did it manually. It was fiddly, but as my colleagues and I built more complex modules, it soon became much quicker than re-building content from scratch in each model.

In 2004 we started refining a basic Excel add-in to automate the insertion and deletion of modules, and this once again saved us a lot of time and reduced the risks involved in these processes. But three main issues still haunted us:

1.  Models often differed in term – e.g. one model might be 5 years long while the next might be 10 years long;
2.  Every model required a different number of categories – i.e. one might require 3 revenue categories while the next might require 20 revenue categories; and
3.  Manually entering and removing formula links between modules before deletion and after insertion was tedious and error-prone.

So we set out to build a comprehensive add-in to make Modular Spreadsheet Development quick and easy within Excel. We called it [bpmModules](http://www.bestpracticemodelling.com/resources/bpmmodules)
, and thought it would take a couple of years to develop.

It ended up taking 10 years to develop, and only after we completed it did we realize that we’d effectively created a _modular content creation, management and sharing system for Excel_. It’s a mouthful, but that’s exactly what it is, and with it you can do things like:

1.  Create your own modules;
2.  Use and edit other people’s modules;
3.  Insert, delete and link modules;
4.  Automatically change the term of a model; and
5.  Automatically add and remove categories without manually editing formulas, etc.

bpmModules also allows you view and manage the modules within your spreadsheet via simple diagrammatic interfaces, such as the one below that shows all the modules in the underlying Excel workbook:

![bpmmodules_project_manager](https://chandoo.org/wp/wp-content/uploads/2014/05/bpmmodules_project_manager.png)

We’ve made the Lite version of this add-in free, and you can download thousands of free modules from[the downloads section of BPM’s website](http://www.bestpracticemodelling.com/downloads/excel_models)
. The software does become commercial once you start building larger models, but by this stage it is hopefully saving you enough time to justify the investment.

Comparison of approaches
------------------------

Modular Spreadsheet Development is an awesome concept capable of revolutionising the way spreadsheets are created, managed and shared. Unfortunately, Excel is not by default modular, so to implement Modular Spreadsheet Development you will need to standardize your spreadsheets and then use one of the three implementation methods discussed in this article.

I’ve provided a summary of the advantages and disadvantages of each of these implementation methods below:

1.  **Manual implementation** is free but requires rigid standardization and is somewhat fiddly, thereby creating risks of errors when inserting modules into workbooks;
2.  **VBA automated implementation** is free and less fiddly then manual implementation, but still requires rigid standardization and at least intermediate VBA skills to develop a reliable Excel add-in; and
3.  **Commercial add-in implementation** is not free for larger models but provides an automated mechanism for creating, re-using and sharing modular content in Excel.

Each of these methods provides the core efficiency gains resulting from Modular Spreadsheet Development, so your choice depends largely on your existing Excel skills and the time, cost and risk savings you estimate you would achieve via automation.

Source files
------------

[**Click here to download example workbooks**](https://chandoo.org/wp/wp-content/uploads/2014/05/msd-examples.zip)
 \[zip file\].

The following workbooks can be used to replicate the manual Modular Spreadsheet Development example provided in this article, and consist of the _financial model_ before and after the insertion of the _equity valuation module_, and the workbook containing this module:

*   Financial Model.xlsb
*   Equity Valuation Module.xlsb
*   Financial Model (with Equity Valuation).xlsb

The following workbooks can be used to demonstrate the automation of this process using the bpmModules Excel add-in:

*   Financial Model (bpmModules).xlsb
*   Equity Valuation.bpm
*   Financial Model (with Equity Valuation) (bpmModules).xlsb

Note that you will need to download and install a [trial of bpmModules](http://www.bestpracticemodelling.com/software/packages/30_day_trial)
 to insert the equity valuation module (with the file extension \*.bpm) into the bpmModules-created financial model.

More information
----------------

You can watch a range of Modular Spreadsheet Development movie tutorials via the following link:

[www.bestpracticemodelling.com/chandoo/msd](http://www.bestpracticemodelling.com/chandoo/msd)

Download thousands of modular Excel workbook examples from:

[www.bestpracticemodelling.com/downloads/excel\_models](http://www.bestpracticemodelling.com/downloads/excel_models)

Download thousands of modules from:

[www.bestpracticemodelling.com/downloads/modules](http://www.bestpracticemodelling.com/downloads/modules)

[Watch bpmModules build a financial model in less than 1 minute](http://www.bestpracticemodelling.com/tv/bpmModules)

### Added by Chandoo

Thanks Michael for writing these very detailed articles on Modular Spreadsheet Development to spread the awareness among our readers. With your help, I am sure many modeling professionals & analysts around the world can embark on the time-saving & fruitful journey of modular development.

_**If you enjoyed these articles,** Please take a minute and say thanks to Micheal._ Also please share your thoughts, implementation notes & experiences with us using comments.

### More on Modeling Best Practices:

*   [Best Practice Modeling – 5 changes to implement today](http://chandoo.org/wp/2012/08/29/best-practice-modeling-5tips/)
    
*   [Project Finance Modeling using Excel – Part 1](http://chandoo.org/wp/2011/02/08/introduction-to-project-finance-modeling-in-excel/)
     & [Part 2](http://chandoo.org/wp/2011/02/16/modeling-interest-during-construction/)
    
*   [Financial Modeling using Excel – Part 1](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    , [Part 2](http://chandoo.org/wp/2010/07/28/financial-model-layout-best-practices/)
    , [Part 3](http://chandoo.org/wp/2010/08/23/assumptions-financial-modeling-excel/)
    , [Part 4, Part 5](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
     & [Part 6](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
    
*   [Spreadsheet Risk Management Part 1](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    , [Part 2](http://chandoo.org/wp/2012/01/03/how-companies-can-manage-spreadsheet-risk/)
    , [Part 3](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
     & [Part 4](http://chandoo.org/wp/2012/02/08/spreadsheet-risk-management-software-review/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/msd-implementation-examples/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/msd-implementation-examples/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel Links – Delay in State migration visualization results edition](https://chandoo.org/wp/excel-links-delay-in-state-migration-visualization-results-edition/)

[NextCP009: Averages are Mean – Know these things before you make any more AVERAGE()sNext](https://chandoo.org/wp/cp009-averages-are-mean-part1/)

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
    
    [Reply](https://chandoo.org/wp/msd-implementation-examples/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/msd-implementation-examples/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/msd-implementation-examples/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ