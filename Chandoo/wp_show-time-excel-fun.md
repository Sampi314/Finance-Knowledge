# It is show time baby - 3 creative ways to display time in excel sheets

**Source:** https://chandoo.org/wp/show-time-excel-fun

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

It is show time baby! – better designer clocks to display time in your spreadsheets
===================================================================================

*   Last updated on August 19, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

My [polar clock using donut charts in excel](http://chandoo.org/wp/2008/08/18/donut-clocks/)
 started a conversation and readers have been awesome enough to download the excel and create their own clocks to show time. Even though the idea of this blog is share the little that I know with you, it is amazing how much I have learned from you all. It just emphasizes that what ever you give away will come back to you in better shape.

So here are few ideas the readers have shared with me through mail / comments.

![animated-polar-clock-in-excel-donut-chart](https://chandoo.org/wp/wp-content/uploads/2008/08/animated-polar-clock-in-excel-donut-chart.gif "animated-polar-clock-in-excel-donut-chart")

### The polar chart with animation effect

Reader _**darone**_ commented that he created a macro to hit “f9” repetitively thus creating the animation effect. My friend Jon took it a step further created the animation using some nifty VBA and shared the spreadsheet [here](http://peltiertech.com/WordPress/wp-content/img200808/donut-clock-running.zip)
. Download and play with it to learn how to run a function periodically using VBA. The key part of the code is:

> `Application.OnTime Now + TimeValue("0:0:1"), Me.CodeName & "." & "**doThis**"`  
> The above line would tell MS-Office to run **doThis** after 1 second from NOW. If you include this line in the code of doThis() then every time it runs, it tells windows to relaunch the function after one second. Very neat and effective way to reduce processor overload that _darone_ faced.

Also read Jon’s comments on the original polar clock post at [time is on my side](http://peltiertech.com/WordPress/2008/08/18/time-is-on-my-side/)
.

![swiss-designer-chromachron-clock-excel-pie](https://chandoo.org/wp/wp-content/uploads/2008/08/swiss-designer-chroma-clock-excel.png "swiss-designer-chroma-clock-excel")

### Swiss designer Chromachron clock using Pie charts in Excel

**_Robert_**, another avid reader and an excel guru liked the polar clock idea and thought why not create the famous [chromachron clock](http://www.prismo.ch/chromachron/)
 in excel. For those of you who are unfamiliar with it, chromachron is a clock that tells time on a color-time-circle.

> On a chronometer time is shown by hands and numerals. Differently on Chromachron, the color-time-watch: Its face is not a dial but a color-time-circle, over which a black disk revolves with a piece cut out as large as a color segment. The disk revolves with the speed of one color area per hour. The disk cut-out indicates the time.

\[[read more](http://www.prismo.ch/chromachron/)\
\]

So _Robert_ took 2 pie charts, one with 12 colors to get the background. Another with 2 colors one black and another transparent to get the rotating disc effect. So when the time 12:00, you can see yellow portion alone, as you move towards 1:00 you will see more orange color. [Download and play with Robert’s sheet](https://chandoo.org/wp/wp-content/uploads/2008/08/chromachron.xls)
.

Both these files have VBA on them so you may want to enable it to get the desired results, but they are safe so go crazy 😀

After seeing this two fine examples I had to do one more clock. This time I choose the **grid based clock** and did it in an excel grid using conditional formatting to fill cells. How did I do it, well that is your home work. Go figure…

![grid-clock-using-conditional-formatting](https://chandoo.org/wp/wp-content/uploads/2008/08/grid-clock-using-conditional-formatting.png "grid-clock-using-conditional-formatting")

**Need more clock ideas?** Try the procrastinator’s clock or some other idea featured on the [10 creative ways to show time](http://www.smashingmagazine.com/2008/08/15/top-10-creative-ways-to-display-time/)

**More on Clocks:** [Give your time series data a twist, plot around clock](http://chandoo.org/wp/2008/08/14/plot-time-series-data-excel/)

**More on Visualization fun:** [Tag clouds in excel using VBA](http://chandoo.org/wp/2008/04/22/create-cool-tag-clouds-in-excel-using-vba/)
, [Square Pies in Excel, not everything is round](http://chandoo.org/wp/2008/07/10/partition-charts-visualization-fun/)
, [Olympic Medals on a map](http://chandoo.org/wp/2008/08/06/olympic-medal-country-year-excel-bubble-chart/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [2 Comments](https://chandoo.org/wp/show-time-excel-fun/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/show-time-excel-fun/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/visualization/)
    , [clock](https://chandoo.org/wp/tag/clock/)
    , [cool](https://chandoo.org/wp/tag/cool/)
    , [design](https://chandoo.org/wp/tag/design/)
    , [fun](https://chandoo.org/wp/tag/fun/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSwitch between firefox tabs using mouse scroll wheel](https://chandoo.org/wp/switch-between-firefox-tabs/)

[NextDell tells me to buy a finger print reader in order to have another color on the systemNext](https://chandoo.org/wp/dell-finger-print-reader/)

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