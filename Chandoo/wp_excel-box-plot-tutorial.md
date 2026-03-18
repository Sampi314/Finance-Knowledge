# How to make Box plots in Excel - Detailed Tutorial & Download

**Source:** https://chandoo.org/wp/excel-box-plot-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

How to make Box plots in Excel \[Dashboard Essentials\]
=======================================================

*   Last updated on August 1, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Whenever we deal with large amounts of data, one of the goals for analysis is,

> _How is this data distributed?_

**This is where a Box plot can help**. According to Wikipedia, a box plot is _a convenient way of graphically depicting groups of numerical data through their five-number summaries: the smallest observation (sample minimum), lower quartile (Q1), median (Q2), upper quartile (Q3), and largest observation (sample maximum)_ \[[more](http://en.wikipedia.org/wiki/Box_plot)\
\]

### Quartile?!? What is that like?

When we say $ 39,000 is the lower quartile of salaries paid in Acme inc. it means, 25% of people make less than or equal to $39,000

Like that Median (Q2) means half the samples are lower than median & the other are more than median.

Example Box Plot
----------------

Here is an example box plot depicting salaries of all _analysts_ in _USA_ as per our [recent Excel Salary Survey](http://chandoo.org/wp/2012/05/25/how-much-salary-excel-survey/ "Do you work on Excel? How much salary you make? [Surveys]")
.

![How to make Box plots in Excel - Detailed Tutorial & Download](https://img.chandoo.org/dashboards/bp/box-plot-in-excel-how-to.png)

The box shows distribution of middle half of data (salaries) while the lines (called as whiskers) show minimum and maximum salaries.

As you can see, 50% of the analysts make between $46,000 to $75,000 while the min is $10k and max is $160k.

Why use Box plots?
------------------

Box & whisker plots are an excellent way to show distribution of your data without plotting all the values. They are easy to understand. We can use them whenever we have lots of data or dealing with samples drawn from larger population.

Creating Box plots in Excel – 9 step tutorial
---------------------------------------------

Despite their utility, Excel has no built-in option to make a box plot. Of course you can make a 3D pie chart or stacked horizontal pyramid chart. Lets save them for your last day at work and understand how to create box plots in Excel.

### Step 1: Calculate the number summaries

Assuming your data is in _list_ use formulas MIN, MAX & PERCENTILE to calculate summaries like below:

![Data for box plot in excel](https://img.chandoo.org/dashboards/bp/data-for-box-plot-in-excel.png)

To calculate 25th percentile (Q1) use = PERCENTILE(list, 25%)

### Step 2: Make a bar chart from Q1, Median & Q3

Just select the 25th percentile, median & 75th percentile values and create a bar chart.Make sure that your chart shows 3 different colored bars not 3 bars in one color.

![Make bar chart from Q1, Median & Q3 data points](https://img.chandoo.org/dashboards/bp/box-plot-step2.png)

### Step 3: Set series overlap to 100%

Select any bar, press CTRL+1 (right click > format series) and adjust series overlap to 100%

![Set series overlap to 100% - Box plot in Excel](https://img.chandoo.org/dashboards/bp/adjust-chart-series-overlap.png)

### Step 4: Adjust series order so that you can see all the bars

If you cannot see all the bars, right click on chart, click on “Select data”.

Now, adjust the series order using arrow keys so that you can see all the bars. See this demo:

![Adjust series order so that you can see all the bars](https://img.chandoo.org/dashboards/bp/adjusting-chart-series-order-box-plot-in-excel.gif)

### Step 5: Make 25th percentile (Q1) bar invisible

Select the bar corresponding to Q1 and fill it with white color. If you make it transparent, it will not work. So make it all white.

### Step 6: Add error bars to Q1 & Q3 series

Just select Q1 (25th percentile) bar and add error bar (any type) from layout ribbon.

![Adding error bars for a chart - from layout ribbon](https://img.chandoo.org/dashboards/bp/adding-error-bars-box-plot-in-excel.png)

Repeat for Q3 series as well.

![Add error bars to Q1 & Q3 series](https://img.chandoo.org/dashboards/bp/box-plot-with-error-bars.png)

### Step 7: Set up error values in your data

Add an extra column in your data area and use simple formulas to calculate error values, like below:

![Calculating error values - excel box plot tutorial](https://img.chandoo.org/dashboards/bp/box-plot-error-calcualtions.png)

### Step 8: Set up custom error values for Q1 & Q3

![Set up custom error values for Q1 & Q3](https://img.chandoo.org/dashboards/bp/error-bar-settings-excel-box-plots.png)  
Select the error bar for Q1 (25th percentile) and,

1.  Press CTRL+1 to format them
2.  Enable only minus (negative) error bar with no cap.
3.  Select Custom as error amount and point to the calculated value.

Repeat for Q3, but choose positive error bar instead.

### Step 9: Format the box plot to your taste

Remove any legend, axis, labels that you do not need. Change colors to suit your taste and mood. Make the whiskers subtle and knock off the grid lines. You are good to go.

![How to make Box plots in Excel - Detailed Tutorial & Download](https://img.chandoo.org/dashboards/bp/box-plot-in-excel-how-to.png)

Making Box plots interactive
----------------------------

Since box plots are very useful to understand distribution of values, we use them in dashboards etc. Naturally, you are interested to know how values are distributed for various things.

In this example, we may want to know how analyst salaries compare with manager salaries.

To make things complicated, we have 10 different job types, thus enabling 45 possible comparisons (10c2)

This is where interactive box plots can help. See this demo to understand:

Interactive Box plot in Excel – a Demo
--------------------------------------

![Interactive Box plot in Excel - a Demo](https://img.chandoo.org/dashboards/bp/interactive-box-plots-in-excel-demo.gif)

How to make interactive box plot in Excel
-----------------------------------------

Construction of box plot is same as mentioned above. The difference is in adding interactivity.

### Step 1: Use combo box form controls to capture comparison criteria

_Excuse the tongue twister._ Using Developer ribbon > Insert > Form controls, add 2 combo box controls and point them to the list of job types.

Lets assume that these combo boxes are linked to cells D1, D2.

\[Related: [Introduction to Excel Form Controls](http://chandoo.org/wp/2011/03/30/form-controls/)\
\]

### Step 2: Calculate 5 number summaries using MINIF, MAXIF and PERCENTILEIF formulas

Don’t rush to type the formulas yet. There is no such formula as MINIF (or MAXIF or PERCENTILEIF). Assuming your list of jobs are in _joblist_, write

\=MIN(IF(joblist=”Analyst”, list\_of\_values,””))

and press CTRL+Shift+Enter

Using MAX(IF(…)) and PERCENTILE(IF(…)) you can calculate remaining 4 summaries.

![Interactive box plot in excel - calculations](https://img.chandoo.org/dashboards/bp/interactive-box-plot-calculations.png)

### Step 3: Based on combo box selection, fetch any two sets of values

Using INDEX formula, we can fetch values corresponding to each combo box selection to a set of cells, like this:

![Fetch any two sets of values from calculations using INDEX formula - Excel box plot tutorial](https://img.chandoo.org/dashboards/bp/interactive-box-plot-data.png)

### Step 4: Connect these values to your box plots

That simple!

### Step 5: Format and interact

Format the charts. Play with combo boxes to interactively compare one set of distribution with another. Show it to your boss or client and see them fall off a chair.

Download Box plot tutorial workbook
-----------------------------------

[**Click here to download the workbook**](https://img.chandoo.org/dashboards/bp/box-plots-in-excel.xlsx)
 containing these examples. Play with it. Check out various formulas and chart settings. Learn.

Do you use Box plots?
---------------------

I love box plots. I have used them several times. Few examples are here: [Excel age survey results](http://chandoo.org/wp/2011/02/25/excel-age-survey-results/)
, [Gantt box chart](http://chandoo.org/wp/2010/07/12/gantt-box-chart-tutorial-template/)
 and [more](http://chandoo.org/wp/tag/box-plots/)
.

**In our [Excel salary survey contest](http://chandoo.org/wp/2012/07/30/excel-salary-survey-contest-results/ "Visualize Excel salaries around world with these 66 Dashboards")** too, many people have used box plots to clearly compare compensation composition. Checkout the entries by Aditya, Allred, Anchalee, Anup, Bryan, Jeanmarc, Joerg, Kostas, Luke, Michael, Nathan, Sergey and Vishwanath. Especially Jeanmarc used interactive version of box plots to allow comparison on demand.

_**What about you?**_ Do you use Box plots often? How do you prepare them? What is your experience like? **Please share using comments.**

### Create Box plots often? Use Jon’s Add-in

If you need to create box plots often and find the above process tedious, then please consider getting a copy of Jon Peltier’s Box Plot add-in for Excel. It works like a charm and produces what you need. All in a few clicks. [Click here to know more](https://www.e-junkie.com/ecom/gb.php?ii=373023&c=ib&aff=49044&cl=84674)
.

PS: Link to Jon’s add-in is an affiliate link. It means, when you buy it from Jon thru this link, I will get a few bucks too. I recommend it because I know it is awesome and perfect for box plots.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [22 Comments](https://chandoo.org/wp/excel-box-plot-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-box-plot-tutorial/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [box plots](https://chandoo.org/wp/tag/box-plots/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MaxIf](https://chandoo.org/wp/tag/maxif/)
    , [minif](https://chandoo.org/wp/tag/minif/)
    , [percentile()](https://chandoo.org/wp/tag/percentile/)
    , [percentileif](https://chandoo.org/wp/tag/percentileif/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousVisualize Excel salaries around world with these 66 Dashboards](https://chandoo.org/wp/excel-salary-survey-contest-results/)

[NextMaking your dashboards interactive \[Dashboard Essentials\]Next](https://chandoo.org/wp/making-dashboards-interactive/)

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
    
    [Reply](https://chandoo.org/wp/excel-box-plot-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-box-plot-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-box-plot-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ