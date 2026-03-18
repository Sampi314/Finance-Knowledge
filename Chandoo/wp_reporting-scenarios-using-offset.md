# Reporting Scenarios using Offset

**Source:** https://chandoo.org/wp/reporting-scenarios-using-offset

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Reporting Scenarios using Offset
================================

*   Last updated on February 14, 2012

![Picture of paramdeep@gmail.com](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=300&d=mm&r=g)

#### paramdeep@gmail.com

Share

Facebook

Twitter

LinkedIn

Project Managers often report financial numbers to the management. In a dynamic world, these numbers are usually based on a lot of factors that may or may not be under your control. So the top management demands that the numbers be reported as per different economic scenarios – Optimistic, Normal or Pessimistic.

It is important to report and present the numbers in a usable format to the top management. They should be able to toggle the scenarios comfortably and see the results. Offset function comes to your rescue to ensure a great looking model with the flexibility of reporting multiple scenarios.

**What is the offset function?**
--------------------------------

A few months back, I had written about the offset function and how it can be used to create [flexible models](http://chandoo.org/wp/2011/10/04/offset-function-to-calculate-irr-for-dynamic-range/)
. I had discussed at that point of time, why offset function is one of the most versatile functions and at the same point of time quite dangerous as well.

In this tutorial, we would see another usage (I feel simpler than last time!) of the offset function

If I were to borrow the signature of the function from my last post, the offset function reads something like: Offset( range, rows, columns, height, width )

[![offset function](https://chandoo.org/wp/wp-content/uploads/2012/01/table_thumb.jpg "offset function")](https://chandoo.org/wp/wp-content/uploads/2012/01/table.jpg)

I will use a similar example, but change the usage of the function a little bit!

[![offset example](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb.png "offset example")](https://chandoo.org/wp/wp-content/uploads/2012/01/image.png)

**_So in the illustrated example, it starts from the C3 cell, moves 1 rows and 3 columns and then gives the value (15 in this case)!_**

This time Offset is NOT returning an array. It is returning a single value!

\[Related: [OFFSET, VLOOKUP & MATCH explained in simple words](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)\
\]

**So how can this be useful?**
------------------------------

The offset function can move the reference of the cell by n rows and m columns. That means that if I structure the sheet with different economic possibilities in different rows, I can always move the scenarios using offset function.

[![Scenarios](https://chandoo.org/wp/wp-content/uploads/2012/01/Scnearios_thumb.gif "Scenarios")](https://chandoo.org/wp/wp-content/uploads/2012/01/Scnearios.gif)

**How was this achieved?**
--------------------------

**Step 1:** The layout of the sheet helps me achieve this objective very easily. The first part of the sheet to select the scenarios is achieved using form controls

[![form controls](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb1.png "form controls")](https://chandoo.org/wp/wp-content/uploads/2012/01/image1.png)

**Step 2:** The Scenarios are listed in sequential order, one after the other and the form control (combo box in this case) is linked to the name of the scenarios.

[![combo box](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb2.png "combo box")](https://chandoo.org/wp/wp-content/uploads/2012/01/image2.png)

**Step 3:** Depending on the scenario selected, the index number of the selection changes. This number is fed into the growth rate and cost selection using the offset function.

[![scenario](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb3.png "scenario")](https://chandoo.org/wp/wp-content/uploads/2012/01/image3.png)

**Step 4:** The model is linked to the selected scenario to report the P&L figures

[![profit and loss](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb4.png "profit and loss")](https://chandoo.org/wp/wp-content/uploads/2012/01/image4.png)

As I told you, offset function is quite versatile in nature and can help you achieve a lot of flexibility in your model

**Bonus Step**
--------------

From your PM career you would have known that preparing a nice looking report as important (if not more) as generating correct results! In our scenario selection model, we highlight the selected scenario (the pink colored row) to give clarity to the end user. This is achieved using

**Step A:** A simple formula in conditional formatting and

[![conditional formatting](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb5.png "conditional formatting")](https://chandoo.org/wp/wp-content/uploads/2012/01/image5.png)

**Step B:** Then using the $ referencing intelligently.

[![$ referencing](https://chandoo.org/wp/wp-content/uploads/2012/01/image_thumb6.png "$ referencing")](https://chandoo.org/wp/wp-content/uploads/2012/01/image6.png)

**What functions do you use in reporting?**
-------------------------------------------

I am sure that if you are generating flexible reports and dashboards for reporting, you would be using some interesting functions and tools in Excel. I use Offset, Index, Match, Indirect, Mod. Which ones do you use?

**Templates to download**
-------------------------

I have created a template for you, where the subheadings are given and you have to link the model! You can [download the same from here](https://chandoo.org/wp/wp-content/uploads/2012/01/Offset-Scenarios-Participant-Copy.xlsx)
. You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, [matches mine or not](https://chandoo.org/wp/wp-content/uploads/2012/01/Offset-Scenarios-Solution-Key.xlsx)
!

**Next Steps**
--------------

Chandoo and I are running a [**course on Excel for Project Managers**](http://chandoo.org/wp/training-programs/excel-for-project-managers/)
 to share with you the various tools and techniques in Excel that can make you an awesome Project Manager. We comprehensively cover aspects related to Planning, Tracking and Reporting apart from Basics of Finance and Advanced Techniques like Monte Carlo Simulation in Project Management in the course. If you are interested in learning more about the course, you can [**click here**](http://chandoo.org/wp/training-programs/excel-for-project-managers/)
.

For any queries regarding the using Excel for Project Management, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/reporting-scenarios-using-offset/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/reporting-scenarios-using-offset/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [combo box](https://chandoo.org/wp/tag/combo-box/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [scenarios](https://chandoo.org/wp/tag/scenarios/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousLearn Statistics & Probability using MS Excel](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/)

[NextUse Text Format to Preserve Leading Zeros in Excel \[Quick Tip\]Next](https://chandoo.org/wp/use-text-format-to-preserve-leading-zeros/)

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