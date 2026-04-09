# Simulating Dice throws - the correct way to do it in excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/simulate-dice-throws

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    

Simulating Dice throws – the correct way to do it in excel
==========================================================

*   Last updated on August 14, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![dice-throws-excel-simulating - correctly](https://chandoo.org/wp/wp-content/uploads/2008/08/dice-throws-excel-howto.png "dice-throws-excel-howto")If you ever had to simulate random outcomes in excel sheet, you might have already heard of about the spreadsheet function `rand()`, this little function generates a random fraction between 0 and 1 whenever you use it. So I usually write `=~round(rand()*12,0)~int(rand()*12)+1` if I need a random number between 0 to 12. Of course, if you have analysis tool pack installed like I do, then we can use `randbetween(0,12)` to do the same.

In order to simulate a dice throw, thus you can use `~round(rand()*5,0)~int(rand()*6)+1`.

So, what would you do if you need to simulate the face total when you throw 2 dice?

`~round(rand()*10,0)~int(rand()*11)+2` ?

**Wrong**

Why? Apparently a random number between 2 and 12 (1 is not possible as the minimum you can get when you throw two dice is 2) doesn’t simulate 2 dice throws properly.

**The CORRECT way to do this is instead generate 2 individual random numbers and add them up, like:**

`~round(rand()*5,0)~int(rand()*6) + 1 + ~round(rand()*5,0)~int(rand()*6) + 1`

Here is why this is correct way to simulate dice throws using random number generator functions:

I have ran these 2 random functions each for 2500 times and plotted the distribution:

![excel-simulate-dice-throw-distribution](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-simulate-dice-throw.png "excel-simulate-dice-throw")

As you can see, the left plot of `int(rand()*11)+2` tells that each of the 11 possibilities (2,3,4,5,6,7,8,9,10,11) are equally likely. But that is not what happens when you throw a dice, you see an awful lot more 5,6,7,8 than you see a perfect 12 or 2. And there is a reason for that, the distribution of 2 dice throws is actually a bell curve, and when you use `int(rand()*6) + int(rand()*6) + 2` the distribution is bell curvish.

**Update:** Thanks to Jon for pointing out that round() is not the choice if you want random integers, you should use int instead. See his explanation in the comments and the [illustration here](http://peltiertech.com/WordPress/wp-content/img200808/RandonDieTrials.png)
.

I have used this logic to [simulate monopoly board game and prove that it is not really that random](http://chandoo.org/wp/2007/02/25/is-monopoly-fair/)
.

**More on games:** [Bingo / Housie ticket generator excel sheet](http://chandoo.org/wp/2008/07/16/bingo-housie-ticket-generator-excel/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/simulate-dice-throws/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/simulate-dice-throws/#respond)
    
*   Tagged under [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [games](https://chandoo.org/wp/tag/games/)
    , [interesting](https://chandoo.org/wp/tag/interesting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [random](https://chandoo.org/wp/tag/random/)
    , [simulation](https://chandoo.org/wp/tag/simulation/)
    , [trivia](https://chandoo.org/wp/tag/trivia/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    

[PrevPreviousBeyond If and Sum, 15 really useful excel formulas for everyone](https://chandoo.org/wp/15-microsoft-excel-formulas/)

[NextPlot your data around the clock \[Excel charting idea\]Next](https://chandoo.org/wp/plot-time-series-data-excel/)

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