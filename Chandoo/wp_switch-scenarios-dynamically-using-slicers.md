# Switch Scenarios Dynamically using Slicers » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/switch-scenarios-dynamically-using-slicers

---

*   [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Switch Scenarios Dynamically using Slicers
==========================================

*   Last updated on June 2, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Slicers are my new favorite feature in Excel. Introduced in Excel 2010, Slicers are like visual filters.

A simple example of slicers:
----------------------------

Let us say you have a sales report (pivot) for multiple salespersons. Since you want to show the report by one person at a time, you used [report filters](http://chandoo.org/wp/2011/04/20/pivot-table-report-filters/ "What are Pivot Table Report Filters and How to use them?")
 in pivot tables to display this. But you find that switching between regions is a pain using the report filter.

_**Enter slicers.**_

Now, you can just click the region name to show the report for that region, like this:

![Using Slicers to dynamically show sales report by person](https://chandoo.org/img/14/slicers-in-pivot-tables.gif)

Using Slicers to Switch between Scenarios Dynamically:
------------------------------------------------------

Now, we can use slicers creatively to make an interactive scenario manager in Excel, some thing like this:

![Using Slicers to Switch Scenarios in Excel](https://chandoo.org/img/pivot/using-slicers-to-select-scenarios-demo.gif)

This technique gives the same outcome as the [Display and Select Scenarios using VBA](http://chandoo.org/wp/2010/09/24/displaying-selecting-a-scenario-using-vba-modeling-in-excel/)
 article, but easier to implement

How to use slicers to switch between scenarios?
-----------------------------------------------

### Step 1: Set up various scenarios in a table

You need to define various scenarios in a table, like this:

![Scenario-wise data - setup](https://chandoo.org/img/pivot/data-for-scenarios.png)

### Step 2: Create a pivot table from your scenario data

Select the table you created in step 1 and [insert a pivot table](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/ "Excel Pivot Table Tutorial")
. Use variable name as row label and variable value in value field area.

### Step 3: Insert a slicer for the scenarios

Select anywhere inside the pivot. Now, from options tab, click on Insert Slicer button. Click on Scenarios field to insert a slicer.

![Add a slicer to select scenario](https://chandoo.org/img/pivot/adding-a-slicer.png)

### Step 4: Create your model, in our case a break-even model

_I will skip the explanation of model creation as that is not relevant here._

Once the model is set up, just refer to the pivot table for each of the variable values.

### Step 5: Move slicer to Model

Go to the pivot table worksheet and Select the slicer, click CTRL+X to cut it.

Go back to your model worksheet and paste the slicer.  
![Disabling Slicer Heading and Clear Filter Button](https://chandoo.org/img/pivot/disable-slicer-heading-howto.png)

### Step 6: Format the slicer

Excel slicers by default show an option to remove the filtered slicer. You can get rid of this button by,

1) Right click on the slicer  
2) Go to slicer settings  
3) Un-check Display Header option

See aside.

### Step 7: Use the slicer to interactively switch scenarios

That is all, our smart scenario switching slicer is ready. Now, you can extend this in many ways. For example, you can write some clever formulas to handle selection of multiple slicers. You can compare between one scenario and another when more than one option is chosen from the slicer. So much more is possible. But I will let your imagination run wild.

Download Example Excel File:
----------------------------

I have made a simple example to demonstrate this technique.

**[Please download the file](https://img.chandoo.org/pivot/slicers%20for%20scenarios%20-%20demo.xlsx "Using Slicers to Switch Scenarios - Example Workbook")
** and open it in Excel 2010.

Examine the worksheets “Scenario Pivot” and “Model” to understand how the slicer is setup and how this works.

Do you slice?
-------------

As I said, Slicers are my new favorite feature in Excel. I have been using them as much as possible because they are simple to use and very powerful.

**What about you?** Do you slice often? What is your experience like? Please share your ideas and tips using comments.

### More examples on Slicers & Pivot Tables:

1) [Creating a Dynamic Dashboard in Excel using Slicers](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
  
2) [Creating a Dynamic Chart using Pivot Table Report Filters](http://chandoo.org/wp/2011/04/27/update-report-filter-macro/)
  
3) [Remove Duplicates and Sort a list using Pivot Tables](http://chandoo.org/wp/2010/09/27/remove-duplicates-using-pivot-tables/)
  
4) _**More on [Pivot Tables](http://chandoo.org/wp/excel-pivot-tables/ "Guide to Excel Pivot Tables")
 & [Modeling](http://chandoo.org/wp/tag/financial-modeling/)
**_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [35 Comments](https://chandoo.org/wp/switch-scenarios-dynamically-using-slicers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/switch-scenarios-dynamically-using-slicers/#respond)
    
*   Tagged under [breakeven model](https://chandoo.org/wp/tag/breakeven-model/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 2010](https://chandoo.org/wp/tag/excel-2010/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [scenarios](https://chandoo.org/wp/tag/scenarios/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousHow Would You Visualize Product Sales Data? \[Excel Challenges #2\]](https://chandoo.org/wp/product-sales-visualization-challenge/)

[NextDo you want to attend an Excel Workshop in Singapore? \[Survey\]Next](https://chandoo.org/wp/singapore-workshop-survey/)

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