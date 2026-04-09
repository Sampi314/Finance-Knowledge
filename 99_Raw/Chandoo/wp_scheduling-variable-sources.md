# Scheduling Variable Feed Sources in Excel

**Source:** https://chandoo.org/wp/scheduling-variable-sources

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Scheduling Variable Feed Sources
================================

*   Last updated on November 18, 2010

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In Manufacturing, Mining and many other industries, bulk commodities are received or delivered in batches or parcels of various sizes and with various properties.

Businesses are often required to schedule the usage of these commodities in quantities which differ from the deliveries. Often commodities are used on a First In First Out (**FIFO**) basis, or they may be scheduled to meet certain input qualities, ie: Constant or Min/Max of an input quality.

This post will give some basic ideas for this type of scheduling within Excel.

**Scheduling First in First Out Usage**
---------------------------------------

Unlike my previous posts, this post will not be walking the reader through the actual scheduling or setup of the worksheet, but will look at each section of the scheduling process and discuss the relevant points where appropriate with reference to the implementation in Excel.

The [Scheduling](https://chandoo.org/wp/wp-content/uploads/2010/11/Scheduling.xls)
 Workbook, Page Sched1 shows a simple FIFO schedule using an Iron Ore mine as an example.

Each section below is highlighted in the sample workbook.

### **Section 1. Inputs**

Various parcels of Iron Ore are presented in order of delivery to a plant or as mined.

Each parcel is of a different sizes (Tonnage) as well as having various qualities of 3 different properties, namely the Iron (Fe), Silicon (Si) and Aluminum (Al) content. These are expressed as percentages but could be Kg/t etc.

Parcels may further be categorized as High, Medium or Low Grade.

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Sched-Inputs.png "Sched Inputs")](https://chandoo.org/wp/wp-content/uploads/2010/11/Sched-Inputs.png)

From a production point of view it is important to know how much feed is required to meet a certain output from a process or what the quality of mixtures will be.

### **Section 2. Production Schedule**

The mine/plant has a production schedule, ie: a quantity of Iron Ore that it is expected to mine or process every month. The schedule may have ups/down to reflect shutdowns, holidays, changes in rosters/workforce  etc.

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Prod_Req.png "Schedule_Prod_Req")](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Prod_Req.png)

### **Section 3. Schedule**

This part does the mechanics of the actual scheduling, allocating parcels of each block until the monthly requirement is met.

In operation it takes the minimum of the size of each parcel minus what has already been processed from that parcel or the production requirement minus what has already been processed that month.

This is done using a simple Min and Sum formula.

Example: K18: =MIN($C18-SUM($I18:J18),K$6-SUM(K$9:K17))

Conditional formatting is used to highlight the cell as a scheduled cell (tonnes > 0)

Example: Conditional Formatting, Cell Value > 0

### **Section 4. Reporting**

Reporting can be prepared for Month by month production, Cumulative from the start or Remaining until the end.

Sum and Sumproduct formula are used to calculate weighted average for elemental grades as you have the quantity of each parcel, each month and the associated grades in the input areas.

Example: Cumulative %Fe in April 10, K36: =SUMPRODUCT(K$10:K$31,$E$10:$E$31)/K$35

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Report1.png "Schedule_Report1")](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Report1.png)

More complex Sumproduct formula are used to report by various classifications.

Examples:

Used High grade tonnage in march, J53: =SUMPRODUCT(1\*($D$10:$D$31=$I52),(J$10:J$31))

Used Medium grade %Fe in April 10, K59:  =IF(K58>0,SUMPRODUCT(1\*(($D$10:$D$31)=$I57)\*(K$10:K$31),($E$10:$E$31))/K$58,0)

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Report2.png "Schedule_Report2")](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Report2.png)

### **Section 5. Charting**

Having produced a schedule and associated reports you now have a large amount of data which can be plotted to suit requirements.

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Chart-e1289912005628.png "Schedule_Chart")](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule_Chart.png)

### **The Next Step**

Once a schedule has been achieved you can feed the production quantities directly into a budget or other downstream system as required.

**Scheduling Random or Planned Usage to Achieve Goals  
**
----------------------------------------------------------

Although the above example, Sched1, is simplistic, First In First Out schedules can and are used in real life. However often some degree of stockpiling is allowed.

This means that parcels can be used in a different order to which they are delivered.

Often this is done so that the input quality of the feed source is varied or maintained, ie Averaged at a level, maintained below or above a level or maximised or minimized according to constraints.

The [Scheduling](https://chandoo.org/wp/wp-content/uploads/2010/11/Scheduling.xls)
 example file, page Sched2 offers a simple manual way to account for this.

Sched2 varies from Sched1 in that it allows manual selection of the order in which parcels are processed.

This is done by simply allowing the user to specify which order parcels will be treated.

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule2.png "Schedule2")](https://chandoo.org/wp/wp-content/uploads/2010/11/Schedule2.png)

The spreadsheet then does all the work with the added benefit of tracking stockpile levels, as often these must be maintained at certain levels.

The spreadsheet has the same reporting and charting functions available as in Sched1.

Summary
-------

In both the examples the scheduling is done using simple, **Sum**’s, **Min** and **Max** formulas.

The actual scheduled production is highlighted using conditional formatting.

The reporting is done using **Sum** and **Sumproduct** formulas.

In both examples adjust the values in the various Yellow cells and watch the scheduled tonnages and qualities change.

Next
----

The purpose of this post was simply to introduce the reader to simple options for scheduling.

It is clear that you now have a simple process from which to derive inputs to a budget, tracking and prediction reports

The post doesn’t attempt to go anywhere near optimization of the schedule using linear programming or other techniques.

However you can see that the addition of Excel solver may be possible to attempt to balance or minimise or maximise outputs, but this is beyond this simple example.

Functions Used:
---------------

[Min](http://chandoo.org/excel-formulas/min.html "Min")
: =Min(Range) returns the Minimum number from the Range

[Max](http://chandoo.org/excel-formulas/max.html "Max")
: =Max(Range) returns the Maximum number from the Range

[Sum](http://chandoo.org/excel-formulas/sum.html "Sum")
: =Sum(Range) adds the values in the Range

[If](http://chandoo.org/excel-formulas/if.html "If")
: [\=If(Condition, Do this if condition is true, Do this if condition is false)](http://chandoo.org/excel-formulas/if.html)

Sumproduct: [http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/ "Sumproduct")

**How do you Schedule your production scenarios? Let us all know in the comments below:**

**Next week: Word Art – Yes it has a use !  
**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/scheduling-variable-sources/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/scheduling-variable-sources/#respond)
    
*   Tagged under [if()](https://chandoo.org/wp/tag/if/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [MIN()](https://chandoo.org/wp/tag/min/)
    , [optimise](https://chandoo.org/wp/tag/optimise/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousShow Months & Years in Charts without Cluttering](https://chandoo.org/wp/show-months-years-in-charts/)

[NextVLOOKUP Formula Cheat-sheet – FREE DownloadNext](https://chandoo.org/wp/download-vlookup-cheatsheet/)

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