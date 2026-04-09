# Show Decimal Points if needed [Quick Tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/show-decimal-points-if-needed

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Show Decimal Points if needed \[Quick Tip\]
===========================================

*   Last updated on September 5, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Sometimes you want to turnoff decimal points if the value after point is 0. _**Mireya**_, Chandoo.org member had one such situation. She writes:

> I am a complete beginner in excel, how can I keep the zeros when I am working with decimals and remove them when are not required, ie
> 
> Thanks for your kind help.

Easy way: Use General Formatting
--------------------------------

The default cell formatting in Excel is General. When you set a cell’s formatting to **General**, you are telling Excel,

_Don’t bother me. Just figure it out._

![General Formatting in Excel - Use it to simplify your cell formatting needs](https://img.chandoo.org/q/general-formatting-in-excel.png "General Formatting in Excel - Use it to simplify your cell formatting needs")

And being a good Samaritan, Excel shows decimal point if there is something after it, else omits it.

See the demo aside to understand this.

![General formatting in Excel - demo](https://img.chandoo.org/q/general-formatting-demo-excel-number-formats.gif "General formatting in Excel - demo")

What if your numbers are results of a calculation?
--------------------------------------------------

It doesn’t matter. General formatting takes good care of the cells. It shows and hides decimal point depending on the result of your formulas.

What if you want something fancy like accounting format, but turn off decimal values
------------------------------------------------------------------------------------

Now you are talking. The **General Formatting** option shows numbers as typed (or calculated). So 124578395 would look like 124578395 instead of $ 12,45,78,395.

_**So how do you show $1,245 and $1,246.34?**_

**Aside:** You should always show decimal points if some values have them and others don’t. The below technique is useful when data is a result of calculation. For example: In a dynamic KPI report, for certain KPIs you may want to show decimal points, and omit for others.

![Show decimal values only if needed - Excel cell formatting using conditional formatting](https://img.chandoo.org/q/show-decimal-points-if-needed-demo.gif "Show decimal values only if needed - Excel cell formatting using conditional formatting")

### To show decimal point if there is something after it

![Conditional formatting rule to show decimal point if needed](https://img.chandoo.org/q/conditional-formatting-rule-show-decimal-point-if-needed.png)  
Just follow below steps:

1.  Select the cell(s) where you want this formatting.
2.  Go to Conditional Formatting > New rule from home ribbon.
3.  Select rule type as “Use a formula…”
4.  Check if there is a value after decimal point using a formula like =Mod(A1,1)>0
5.  Click the format button
6.  Go to “Number” tab and Apply formatting with 2 decimal places.
7.  Click OK & You are done!

Now, if the cell has a decimal value, it shows, otherwise the decimal point is omitted.

Related: [Conditional formatting Basics](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/ "Excel conditional formatting basics")

Do you deal with such situations when formatting numbers?
---------------------------------------------------------

Often when making reports (or dashboards), I have a cell where any data can go, based on user selection. In such cases, I use conditional formatting to define how it looks based on the data. Sometimes, I also use TEXT formula to format the data. This is more suitable when data is displayed in a text box rather than a cell.

_**What about you?**_ Do you face situations like this? How often you rely on General formatting? **Please share your experience and tips using comments.**

More on Number formatting in Excel
----------------------------------

Understanding how Excel formats numbers (and other values) can save you lots of time when you are designing dashboards, reports or workbooks that need to presented. Check out below articles to get few more tips.

*   [Introduction to number formatting in Excel](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/)
     and 10 tips
*   [Preserving leading zeros in a number using formatting](http://chandoo.org/wp/2012/02/15/use-text-format-to-preserve-leading-zeros/)
    
*   [Display decimals only if the value is less than 1](http://chandoo.org/wp/2008/10/02/excel-number-formatting-tip-showing-decimals-conditionally/)
    
*   [How to hide “0” in chart axis labels?](http://chandoo.org/wp/2009/12/14/how-to-hide-0-in-chart-axis/)
    
*   [How to hide cell’s contents using format codes?](http://chandoo.org/wp/2009/06/05/hide-cell/)
    
*   [Adding colors to your chart labels using custom format](http://chandoo.org/wp/2009/01/29/colors-in-excel-chart-labels-trick/)
    
*   [Showing Indian Currency Format in Excel](http://chandoo.org/wp/2010/07/26/indian-currency-format-excel/)
     \[and [more on this](http://chandoo.org/wp/2012/01/31/custom-number-formats-multiply-divide-by-any-power-of-10/)\
    \]
*   [Develop & understand custom number formats](http://chandoo.org/wp/2011/11/02/a-technique-to-quickly-develop-custom-number-formats/)
    
*   [Chart Axis formatting – Part 1](http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/)
     & [Part 2](http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/show-decimal-points-if-needed/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/show-decimal-points-if-needed/#respond)
    
*   Tagged under [custom cell formatting](https://chandoo.org/wp/tag/custom-cell-formatting/)
    , [Custom Number Format](https://chandoo.org/wp/tag/custom-number-format/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [number formatting](https://chandoo.org/wp/tag/number-formatting/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousExcel Links – Going to Togo Edition](https://chandoo.org/wp/excel-links-going-to-togo-edition/)

[NextFormula Forensics No. 028 – It’s Just a Jump to the LeftNext](https://chandoo.org/wp/formula-forensics-no-028/)

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