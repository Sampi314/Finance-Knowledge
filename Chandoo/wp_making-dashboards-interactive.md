# Making your dashboards interactive [Dashboard Essentials]

**Source:** https://chandoo.org/wp/making-dashboards-interactive

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Making your dashboards interactive \[Dashboard Essentials\]
===========================================================

*   Last updated on August 3, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Everyone likes to be in control.**_ Even my 2 year old daughter jumps with joy when she lays her hands on TV remote. _She pushes the buttons and assumes it is working._ It is another story that we rarely watch TV at home.

By adding an element of control, we can make our [dashboard reports](http://chandoo.org/wp/excel-dashboards/)
 fun. Interactive elements like form controls, slicers etc. invite users to play with your dashboard, get involved and understand data by asking questions. That is why I recommend making dashboards interactive.

_Today lets understand how you can make dashboards interactive._

**There are 2 aspects to interactivity:**

1.  What users see (controls, slicers etc.)
2.  How it works in background (formulas, pivots, tables etc.)

Section 1: Adding interactivity to your dashboards
--------------------------------------------------

There are many techniques to add interactivity to your dashboards.  Lets look at each of them closely.

Using Data Validation to add drop-downs to a cell
-------------------------------------------------

This is the easiest way to get started. Using data validation feature in Excel, we can restrict only a set of values in a cell. When you do this, Excel shows a small drop down box (combo-box) inside the cell so that you can pick one of the possible values. Like this:

![Data validation drop down list in Excel - Adding interactivity to dashboards](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-cell-data-combo-box-entry.png "Data validation drop down list in Excel - Adding interactivity to dashboards")

### Demo of what you can do:

An example report show casing flu trends in US, various states & cities between 2003 – 2009. For more, [click here](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/)
.

[![Flu trends dashboard in Excel - Data validation in play](https://chandoo.org/img/p/flu-trends-chart-demo.gif "Flu trends dashboard in Excel - Data validation in play")](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/)

### Learn how to use data validation drop-downs:

*   [Adding data validation drop downs in Excel – Introduction & Examples](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
    
*   [Cascading Drop downs – load values in 2nd list depending first list](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/)
    
*   [Making data validation list dynamic](http://chandoo.org/wp/2010/09/13/dynamic-data-validation-excel/)
    

### Example Dashboards with data validation drop downs

*   [Flu trends dashboard in Excel](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/)
    
*   [Visualizing Survey Results using Panel Charts](http://chandoo.org/wp/2010/04/01/incell-panel-chart/)
    
*   [Sales Analysis charts in Excel – lots of examples](http://chandoo.org/wp/2011/06/30/sales-analysis-charts-in-excel/)
    
*   [Personal Expense Trackers](http://chandoo.org/wp/2010/07/16/download-expense-trackers/)
    
*   [Sales Dashboards – lots of examples](http://chandoo.org/wp/2010/01/04/sales-dashboards/)
    
*   [Excel Salary Survey – Dashboards – lots or examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    

Using Form Controls to add interactivity
----------------------------------------

Almost all computer users are familiar with form controls. We see them every day – scroll bars, check boxes, option buttons, buttons – pretty much all programs in your computer are ripe with form controls. But do you know you can add the same controls to your Excel worksheet?

You can use these controls on worksheets to help select data. For example, drop-down boxes, list boxes, spinners, and scroll bars are useful for selecting items from a list. Option Buttons and Check Boxes allow selection of various options. Buttons allow execution of VBA code.

By adding a control to a worksheet and linking it to a cell, you can return a numeric value for the current position of the control. You can use that numeric value in conjunction with the Offset, Index or other worksheet functions to return values from lists.

![Excel form controls - adding interactivity to your dashboards](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-1.jpg "Excel form controls - adding interactivity to your dashboards")

### Demo of what you can do:

\[[Watch the demo on our YouTube channel](http://youtu.be/Qx9F-09-fGg)\
\]

###  Learn how to use form controls

*   [Introduction to various form controls & Examples](http://chandoo.org/wp/2011/03/30/form-controls/)
    
*   [Using check boxes with charts – example & tutorial](http://chandoo.org/wp/2010/08/31/dynamic-chart-with-check-boxes/)
    
*   [Using scroll bar control – simple mortgage payment calculator in Excel](http://chandoo.org/wp/2010/01/20/mortgage-payment-calculator/)
    

### Example dashboards using form controls

*   [KPI Dashboards using Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [Customer Service Dashboard in Excel](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
    
*   [Excel Salary Survey Dashboards – lots of examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    
*   [Sales Dashboards in Excel – lots of examples](https://chandoo.org/wp/making-dashboards-interactive/chandoo.org/wp/2010/01/04/sales-dashboards/)
    

Using Slicers to add interactivity
----------------------------------

Slicers, a new feature added in Excel 2010 can be used to add interactivity to your dashboards & reports. Slicers are like visual filters. So you can see all available options as small boxes and you can click which option you want.

### Demo of Slicers in action:

[![Using slicers as interactive elements - example - making dashboards interactive](https://chandoo.org/img/pivot/using-slicers-to-select-scenarios-demo.gif "Using slicers as interactive elements - example - making dashboards interactive")](http://chandoo.org/wp/2011/06/01/switch-scenarios-dynamically-using-slicers/)

### Learn how to use Slicers

*   [Using slicers to make a dynamic dashboard in Excel](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
    
*   [Overview of slicers & other new features in Excel 2010](http://chandoo.org/wp/2010/05/17/what-is-new-in-excel-2010/)
    
*   [Using slicers to select one of many scenarios in your models](http://chandoo.org/wp/2011/06/01/switch-scenarios-dynamically-using-slicers/)
    

### Example Dashboards using Slicers

*   [Dynamic Dashboard using Slicers](http://chandoo.org/wp/2010/12/08/dynamic-dashboard-video-tutorial/)
    
*   [Excel Salary Survey Dashboards – lots of examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    

Using Click-able cells as interactive elements
----------------------------------------------

With a few lines of VBA code, you can turn every cell in Excel in to a potential input option. When user clicks on a particular cell, you can treat that as interaction and modify your dashboard (or chart). This is a very powerful and intuitive way to use in dashboards. See below example.

### Demo of what you can do:

[![Grammy Bump Chart in Excel - Using click-able cells as interactive elements in your dashboards](https://img.chandoo.org/vp/grammy-bump-chart-replication-in-excel-demo.gif "Grammy Bump Chart in Excel - Using click-able cells as interactive elements in your dashboards")](http://chandoo.org/wp/2011/02/22/the-grammy-bump-chart-in-excel/)

###  Learn how to use click-able cells

*   [Showing details up on selecting a cell](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
    

### Example dashboards using click-able cells type of interactivity

*   [Interactive sales chart in Excel](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
    
*   [Displaying product reviews on demand](http://chandoo.org/wp/2011/04/06/show-average-and-distribution/)
    
*   [Grammy bump chart in Excel](http://chandoo.org/wp/2011/02/22/the-grammy-bump-chart-in-excel/)
    
*   [Customer service dashboard in Excel](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
    
*   [Excel Salary Survey Dashboards – lots of examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    

Using Hyperlinks to add interactivity
-------------------------------------

Many of you know that you can type any text in a cell and press CTRL+K to convert it to a hyperlink to another part in your workbook. But Hyperlinks can trigger macros upon mouse hover. This is a powerful technique first mentioned by [Jordan at OptionExplicitVBA](http://optionexplicitvba.blogspot.com/2011/04/rollover-b8-ov1.html)
.

By using this behavior, we can create an interactive report that gets updated upon mouse hover. See this demo:

### Demo of what you can do:

[![Interactive dashboard using hyperlinks - making interactive dashboards in Excel](https://img.chandoo.org/dashboards/interactive-dashboard-in-excel-demo.gif "Interactive dashboard using hyperlinks - making interactive dashboards in Excel")](http://chandoo.org/wp/2011/07/20/interactive-dashboard-using-hyperlinks/)

### Learn how to set up dynamic hyperlinks

*   [Interactive dashboards using Excel Hyperlinks – tutorial & explanation](http://chandoo.org/wp/2011/07/20/interactive-dashboard-using-hyperlinks/)
    
*   [Video tutorial on Interactive hyperlinks](http://chandoo.org/wp/2011/07/25/video-on-interactive-dashboard-using-hyperlinks/)
    
*   [Excel hyperlinks – basics, syntax & more](http://chandoo.org/wp/2011/03/31/excel-hyperlinks/)
    

### Example dashboards using interactive hyperlinks

*   [Excel Salary Survey Dashboards – lots of examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    
*   [Periodic table of elements in Excel](http://optionexplicitvba.blogspot.in/2012/06/period-table-of-elements-in-excel.html)
     \[Option Explicit VBA\]

Using VBA / Macros to add interactivity
---------------------------------------

Of course, you can add active x or VBA events to add interactivity to your dashboards. This gives you lot of control on what you want and enables you to do more. That said, using VBA to provide interactivity requires that your audience must enable macros when they view your work.

There are many ways to add interactivity thru VBA. Some popular methods are,

*   Adding buttons or assigning macros to drawing shapes, images
*   Overlapping buttons or shapes on maps, floor plans etc. and driving events on click
*   Using worksheet or active-x controls and adding events (like mouseover, click etc.)

_Note: Both click-able cells & interactive hyperlinks also require VBA to be enabled. But the amount of code they require is quite less._

### Demo of what you can do

[![Picture Calendar using Excel - Adding interactivity using VBA to your dashboards](https://img.chandoo.org/i/pictorial-calendar-demo.gif "Picture Calendar using Excel - Adding interactivity using VBA to your dashboards")](http://chandoo.org/wp/2012/01/02/picture-calendar-template/)

### Learn how to use VBA & Macros to add interactivity

*   [Introduction to VBA, Excel Macros](http://chandoo.org/wp/excel-vba/)
    
*   [Using VBA Macros to make a picture calendar](http://chandoo.org/wp/2012/01/02/picture-calendar-template/)
    
*   [Dynamic Pivot Chart using VBA Macros](http://chandoo.org/wp/2011/04/27/update-report-filter-macro/)
    

### Example Dashboards using VBA Macro based interactivity

*   [MLB Pitching Statistics Dashboard](http://chandoo.org/wp/2011/08/10/mlb-pitching-stats-dashboard/)
    
*   [India’s world cup cricket victory in a dashboard](http://chandoo.org/wp/2011/04/15/cricket-worldcup-dashboard/)
    
*   [Interactive Sales chart using Excel](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
    
*   [Sales analysis charts in Excel – multiple examples](http://chandoo.org/wp/2011/06/30/sales-analysis-charts-in-excel/)
    
*   [Excel Salary Survey dashboards – multiple examples](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")
    
*   [Visualizing Roger Federer’s Wimbledon victory – Excel VBA Dashboard](http://chandoo.org/wp/2012/07/09/visualizing-roger-federers-7th-wimbledon-win-in-excel/ "Visualizing Roger Federer’s 7th Wimbledon Win in Excel")
    

Using Timelines to add interactivity \[Excel 2013\]
---------------------------------------------------

Starting Excel 2013, Microsoft is introducing a new feature called as Time lines. Timelines allow you to interactively select a range of dates. I have not yet written any articles on this feature. But here is a short demo on how they work:

![using time lines to add interactivity to your dashboard reports](https://img.chandoo.org/dashboards/time-line-interactivity-demo-excel-2013.gif "using time lines to add interactivity to your dashboard reports")

Section 2: Behind interactivity – What you need to know in Excel
----------------------------------------------------------------

Now that you know various techniques for interactivity, lets understand various building blocks that help you get there.

### Use tables to hold your data

One of the premises of interactivity is that your data can change. When this is the case, I suggest you to set up all your data in tables. Tables allow you to keep data that can grow (or shrink) and write formulas referring to whole range.

[Learn how to use tables](http://chandoo.org/wp/2009/09/10/data-tables/)
 \[Excel 2007 and above only\]

### Use INDEX formula

INDEX formula helps you extract a portion (single cell, range) from a list of values that you want to use for further calculations or charting. The syntax is simple.

INDEX(range of values, row, column)

Example: INDEX(A1:A10,5) returns A5

_Note: Index returns a reference to A5, not the value itself. So you can use INDEX where ranges are expected. For ex. INDEX(A1:A10,5) : INDEX(A1:A10,9) same as A5:A9_

**Fore more on INDEX formula:**

*   [Using INDEX formula in your lookups](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    
*   [The imposing INDEX](http://www.excelhero.com/blog/2011/03/the-imposing-index.html)
     \[Excelhero\]

PS: You can also use OFFSET formula in this situations. Please keep in mind that OFFSET is volatile and hence can slow down your workbooks if you use it alot.

### Use lookup formulas

Interactive dashboards require formulas that dynamically lookup a set of values among heaps and return them to charts, summaries etc. This is where lookup formulas come handy. Check out our [LOOKUP page for comprehensive information on this](http://chandoo.org/wp/2012/03/30/comprehensive-guide-excel-vlookup/)
.

### Use SUMIFS, SUMPRODUCT

SUMIFS & SUMPRODUCT formulas will become your best friends when it comes to extracting summaries from mountains of data based on user interaction. Once you master these, you can analyze & visualize any amount of data with ease.

*   [Introduction to SUMIFS formula, examples & explanation](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    
*   [Introduction to SUMPRODUCT formula, examples & explanation](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula)
    
*   [Formula Forensics 007 – Sumproduct](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "FF 007")
    
*   [Advanced SUMPRODUCT examples](http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/)
    
*   More on [SUMPRODUCT](http://chandoo.org/wp/tag/sumproduct/)
    , [SUMIFS](http://chandoo.org/wp/tag/sumifs/)
    , [COUNTIFS](http://chandoo.org/wp/tag/countifs/)
    , [SUMIF](http://chandoo.org/wp/search?q=sumif)
    , [Array formulas](http://chandoo.org/wp/tag/array-formulas/)
    

### Use Picture links

Picture links are live snapshots of ranges of cells. If you create a picture link from cells A1:D5, then although it looks like a picture, it is a live image of the cells A1:D5. So when the cells change, the picture gets updated too, thus creating interactive effect.

**For more on picture links:**

*   [Introduction to picture links – examples, information & uses](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    
*   [Picture links in practice – example dashboards & charts](http://chandoo.org/wp/tag/picture-links/)
    

### Use Pivot tables

Pivot tables can process large volumes of data and give you desired summaries with in split seconds. They are by nature not dynamic (if data or criteria changes, you need to refresh them). Starting Excel 2010, you can use Slicers to interactively update pivot tables (hence pivot charts) . Even in earlier versions, you can use simple macros to automatically refresh pivot tables whenever users modify a form control or do something else. This allows for powerful dashboard reporting all the while keeping your calculation engine light weight.

**For more on pivot tables:**

*   [Introduction to Pivot Tables](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    
*   [More on pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
    

### Use conditional formatting

Conditional formatting plays an important role in interactive dashboards by highlighted changed portions of worksheet. This further improves the interactive feel and guides users attention.

**More on conditional formatting:**

*   [Introduction to conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    
*   [More on conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    

Do you make your dashboards interactive?
----------------------------------------

I love keeping my workbooks, models & dashboards interactive. Simple features like form controls, slicers can add a lot of wow factor to your workbooks.

**What about you?** Do you make interactive dashboards & charts? What are your favorite techniques? _**Please share using comments.**_

_Now, if you excuse me, I will go and resolve a fight between my daughter and son. They both want remote control the TV even though it is switched off._

**More on Dashboards:** Check out [Excel Dashboards page](http://chandoo.org/wp/excel-dashboards/)
 & [resources for making dashboards page](http://chandoo.org/wp/2011/03/25/resources-for-making-dashboards/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [28 Comments](https://chandoo.org/wp/making-dashboards-interactive/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/making-dashboards-interactive/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [examples](https://chandoo.org/wp/tag/examples/)
    , [excel 2013](https://chandoo.org/wp/tag/excel-2013/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [hyperlink()](https://chandoo.org/wp/tag/hyperlink/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [resources](https://chandoo.org/wp/tag/resources/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [time lines](https://chandoo.org/wp/tag/time-lines/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to make Box plots in Excel \[Dashboard Essentials\]](https://chandoo.org/wp/excel-box-plot-tutorial/)

[NextExcel Salary Survey Dashboards – Choose the winner \[poll\]Next](https://chandoo.org/wp/excel-salary-dashboards-voting/)

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
    
    [Reply](https://chandoo.org/wp/making-dashboards-interactive/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/making-dashboards-interactive/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/making-dashboards-interactive/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ