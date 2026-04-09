# How to analyze business data in Excel - 15 Quick & powerful ways

**Source:** https://chandoo.org/wp/how-to-analyze-business-data

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

15 Quick & powerful ways to analyze business data
=================================================

*   Last updated on February 26, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Here is a situation all too familiar._

You are looking at a spreadsheet full of data. You need to analyze and tell a story about it. You have little time. _**You don’t know where to start**_.

Today let me share **15 quick, simple & very powerful ways to analyze business data**. Ready? Let’s get started.

### 1\. Describe data with quick stats

You know…, the good old AVERAGE, COUNT, SUM, MIN, MAX, MEDIAN, and Range of the data.

You can calculate all of these with simple Excel formulas.

If you are lazy (or in a bit of hurry), you can use the Descriptive statistics feature of Data Analysis Tools add-in (this is available in Excel by default. You just need to enable it by going to File > Options > Add-ins > Manage Excel Add-ins > Go).

![Descriptive statistics in Excel using Data Analysis toolpack add-in](https://img.chandoo.org/analysis/descriptive-statistics-excel.png)

Related: [Going beyond AVERAGE to summarize data – Podcast part 1](http://chandoo.org/wp/2014/05/22/cp009-averages-are-mean-part1/)
 & [part 2](http://chandoo.org/wp/2014/05/30/cp010-averages-are-mean-part2/)

### 2\. Heatmap it

When you have a bunch of numbers, you can use heatmaps / color scales to to find what’s going with it in the quickest & most fun way.

Just select the numbers and go to Home > Conditional Formatting > Color-scales and pick a color scale you like.

See the numbers light up based on how high / low they are.

![Create a quick heatmap using conditional formatting color scales in Excel](https://img.chandoo.org/analysis/heatmap-excel-example.png)

### 3\. Spot the trend

Your data may have some trends buried in it. Uncovering these trends can be hard if you look at numbers alone. But with a simple line chart, you can quickly see how things are going, what has been the general direction of your numbers and _may be even predict_ what is going to happen next.

To spot the trend, simply select the data and create a line chart (or even a sparkline)

### 4\. 80 / 20 – Pareto Analysis

[Pareto analysis](http://chandoo.org/wp/2009/09/02/pareto-charts/)
 (also known as 80/20 analysis) refers to the idea that 80% of outcomes in many situations are governed by 20% factors.

For example, in a manufacturing company 80% of defects may be reported by just 20% of the process steps

or in a website, 80% of visitors may be going to 20% of the pages.

![Interactive Pareto Chart - part of 50 ways to analyze data course - Chandoo.org](https://lsns.chandoo.org/50w/img/demo-03-pareto-analysis.gif)

### 5\. Index the numbers

Let’s say you are looking at sales of various products. Product A sells between 4000 and 5000 units per month. Product B sells between 1000 and 1500 per month. How would you compare these two product performances?

You can index their sales to a common starting point, like 100 and then analyze relative performance with the help of [indexed charts](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
.

Something like this:

![Indexed charts - compare numbers that do not have same base - Excel data analysis & charting technique](https://img.chandoo.org/c/example-indexed-chart-in-excel.png)

### 6\. Weighted average it

**Pop quiz:** _If a cup of coffee at Joe’s Brew costs $4 on weekdays and $3 in weekends, what is the average cost of coffee over a week?_

Hint – the answer is not $3.5

![Weighted averages in Excel - how to & formula](https://chandoo.org/img/f/weighted-average-excel-formula.png)

When analyzing real-life data, calculating average may not cut it. You may have to calculate weighted average to get the true picture of your numbers.

Related: [learn more about weighted average formula](http://chandoo.org/wp/2010/06/15/weighted-average-excel/)
.

### 7\. Find the outliers

Quick story – A professor walked in to the freshmen class of an MBA program. She took out a blank sheet of A4 paper, placed a dot with red marker on it somewhere. Then she showed the paper to students and asked them “what do you see?”

Everyone said “a red dot”.

Not a single person said “a white paper”.

That’s because our focus is always on outliers (things that are not normal).

So next time you are looking at business data, find out those red dots.

### 8\. Slice & Chart it

If you create a chart from lots of data, then it looks cluttered.

But when you apply filters or [slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
 to original data, the chart will show only filtered data.

This is a quick & powerful way to slice your data and visualize sub-sets to spot trends or insights.

![Adhoc trend chart with slicers in Excel - demo](https://img.chandoo.org/analysis/slicer-chart-adhoc-analysis-demo.gif)

### 9\. Check out the distribution on this curve!

When you understand the shape of your data, you can tell better stories about it.

To quickly check the shape of your data,

*   Find the range of your data (min & max values)
*   Divide this range in _n_ equal ranges (start with n=10 and refine until you are happy)
*   Find out how many values fall in each of those n ranges (calculate the frequency using formulas like COUNTIFS)
*   Create a column chart with this frequency data (called as histogram)
*   Spot the shape from this histogram.

### 10\. Rank it / Sort it

Sort your data using Excel sort options or rank the data points against all values using RANK() formula. This will tell you where each value fits in.

Related: [Sort values using formulas in your dashboards](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)

### 11\. Top 5 it

Sometimes when you have too many items, it’s better to focus on just top 10 values or bottom 5 values. For example, if you are analyzing sales of 745 products, looking at all the 745 items is going to be very tiring. Instead you can filter the list down to top or bottom few values and then focus on these unique items.

![Top 10 items using Excel Pivot table filters](https://chandoo.org/img/dashboards/top-10-values-dashboards.png)

To do this, you can use

*   Regular data: Auto filter > Number filters > Top 10 option
*   Pivot tables: [Filter > Value filters > Top 10](http://chandoo.org/wp/2010/12/01/top-10-values-in-dashboards/)
    

Also, you can [use conditional formatting to highlight top or bottom _n_ items](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
. You can also highlight top or bottom _x%_ values.

### 12\. Got change?

When you have data for more than 1 year (or month), you can analyze % change year over year to spot valuable information.

![% change over time - display using conditional formatting in Excel](https://img.chandoo.org/dashboards/final-regional-summary-report.png)

These kind of % changes (YoY, MoM etc.) are very useful in companies that experience business cycles. For example, if you sell scarves, you can expect more sales in winter months. So when comparing % change, you should compare with last year same month values instead of previous month to understand how good the performance has been.

To visualize such changes, you can use conditional formatting > icons > arrows

Related: [Never use simple numbers in your dashboards](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/)

### 13\. Spot the the duplicates

When comparing two or more sets of data, often understanding how many values are duplicated (or not) in your lists can be helpful.

For example, if you are analyzing list of customers visiting your store this month & last month, you may want to know how many people visited your store both months (ie how many customers are loyal?)

To spot the duplicates quickly, you can use Conditional Formatting > Duplicates (related: [compare 2 lists in Excel](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)
).

![Compare 2 lists using Excel conditional formatting](https://chandoo.org/img/cf/compare-2-lists-conditional-formatting-qt.gif)

To count how many values are overlapping in 2 sets of data, you can use formulas.

### 14\. Find the rate of return

**Question time:** It was year 2015. Johnny is new to stock market. He bought company K’s shares for $500 in 1st of Jan 2015. Fast forward to July 2015. He wanted to find out how much his $500 investment is worth now. So he looked at company K’s share price data. Here is what he found.

The stock went up (or down) by -10%, 10%, -15%, 15%, -10%, 10% in first 6 months of the year.

_**So what is his investment worth now?**_

This is where ideas like FV (future value) come in to picture.

![FVSCHEDULE() Excel formula to calculate future value after a series of % changes](https://img.chandoo.org/analysis/fvschedule-demo.png)

You can use a formula like FVSCHEDULE() to quickly calculate how much the investment is worth after a series of % changes.

Related: [Calculating CAGR using Excel](http://chandoo.org/wp/2014/04/29/calculate-cagr-using-excel/)
.

### 15\. Count by occurrence

When analyzing textual data (like customer names, vendor IDs, part numbers etc.) you may want to know how many times each item has occurred in the list, what is the most frequent item etc. To get this quickly, just set up a pivot table. Add the customer name column to both row labels & value field area of the pivot table. Sort the pivot by value field, largest to smallest. And your report is ready.

Want more? 50 Ways to Analyze Data course is for you:
-----------------------------------------------------

If your job involves data analysis & story telling (to be honest _all_ jobs require these skills), then you are going to love **50 ways to analyze data** online course.

This course offers 50 case studies, each dealing with a specific type of business problem, analysis situation or modeling scenario and offers a variety of solutions using Excel. You will learn how to analyze data better, faster, and present the information more beautifully.

We are not accepting students in to this program. Check out 50 ways to analyze data program course page for more information and enrollment process.

[**Click here**](http://chandoo.org/wp/resources/50-ways-to-analyze-data/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [19 Comments](https://chandoo.org/wp/how-to-analyze-business-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-analyze-business-data/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousCP037: Error error on the wall, How do I fix you all? – Understanding & Fixing Excel Errors](https://chandoo.org/wp/cp037-excel-errors/)

[NextWhat is the coolest thing you made with Excel? \[weekend poll\]Next](https://chandoo.org/wp/coolest-thing-in-excel-poll/)

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introducing-advanced-excel-training-v1.png)](https://chandoo.org/wp/excel-school-program/)

Chandoo is an awesome teacher

__________ Rated 5 out of 5

_– Jason_

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Complete Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)

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
    

### 19 Responses to “15 Quick & powerful ways to analyze business data”

1.  ![](https://secure.gravatar.com/avatar/6c25b50e59b062bb28bd518a73fabe267c548a2239a48d766e17b80423f83190?s=64&d=mm&r=g) JP says:
    
    [July 1, 2015 at 1:25 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003099)
    
    This is just great Chandoo! Aspiring operation managers should be knowing these powerful analysis approach. Thank you for sharing.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003099)
    
2.  ![](https://secure.gravatar.com/avatar/d96ef26b2de8425f09190af469a15b28f851719c18f92a62fb0bff112639baa9?s=64&d=mm&r=g) syed nadeem abbas says:
    
    [July 2, 2015 at 1:37 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003432)
    
    It's very helpful stuff and I am expecting much more awsome in coming training program.  
    Thanks for sharing.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003432)
    
3.  ![](https://secure.gravatar.com/avatar/716281b63e6ba7290eab2a580fec35805313d57fc59e0956b5a65e781a0504ae?s=64&d=mm&r=g) Ndy says:
    
    [July 2, 2015 at 2:08 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003441)
    
    This awesome! I always enjoy their excel quick tricks!
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003441)
    
4.  ![](https://secure.gravatar.com/avatar/716281b63e6ba7290eab2a580fec35805313d57fc59e0956b5a65e781a0504ae?s=64&d=mm&r=g) Ndy says:
    
    [July 2, 2015 at 2:09 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003445)
    
    I meant 'your' texcel tricks
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003445)
    
5.  ![](https://secure.gravatar.com/avatar/1177b158bf8edeae34731c61d0c0400830ccf61478969817975886c8cecd4771?s=64&d=mm&r=g) SB says:
    
    [July 2, 2015 at 3:45 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003490)
    
    This is Fantastic.
    
    I use quite a few of them on a fairly regular basis. Now I will have a one stop location for a lot of the fire power I need for my analysis  
    Great help and thanks for sharing Chandoo.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003490)
    
6.  ![](https://secure.gravatar.com/avatar/291cc3739f719202b02dcda4d860f74097e3214164b5cac08ec654525aee8e63?s=64&d=mm&r=g) Sunadh says:
    
    [July 2, 2015 at 4:31 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003517)
    
    Thanks Chandoo!!!! You work "Hard" to put our lives at "Ease".......
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003517)
    
7.  ![](https://secure.gravatar.com/avatar/2e4a18b997827d19356581d777592af6c65a35528d4b8452f8ef77a1d81678fe?s=64&d=mm&r=g) [Rajat Kumar](http://www.indiakudos.com/)
     says:
    
    [July 2, 2015 at 8:25 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003624)
    
    Thank-you Chandoo. 🙂
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003624)
    
8.  ![](https://secure.gravatar.com/avatar/929d90419a21107c089bdf8785b272d7d0f8dc9ead598880f7f85f57e2d2c40f?s=64&d=mm&r=g) Prash says:
    
    [July 2, 2015 at 1:15 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003747)
    
    Thank you Chandoo! This came at a right time!
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003747)
    
9.  ![](https://secure.gravatar.com/avatar/bec3355cae7d36f1581e4004d7273c7335180c6d2ad0776f29ce9eebb170c79e?s=64&d=mm&r=g) Judie Lopez says:
    
    [July 2, 2015 at 1:42 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003755)
    
    Thank you chandoo!
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003755)
    
10.  ![](https://secure.gravatar.com/avatar/bec3355cae7d36f1581e4004d7273c7335180c6d2ad0776f29ce9eebb170c79e?s=64&d=mm&r=g) Judie Lopez says:
    
    [July 2, 2015 at 1:42 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003756)
    
    Superb!
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003756)
    
11.  ![](https://secure.gravatar.com/avatar/b6cc9213156f5cfa70d7afe4cb9d1b749bf5988df43ec8efc96be1fbd39563f7?s=64&d=mm&r=g) [v.rajan](http://nil/)
     says:
    
    [July 2, 2015 at 2:47 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003774)
    
    good.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003774)
    
12.  ![](https://secure.gravatar.com/avatar/b6cc9213156f5cfa70d7afe4cb9d1b749bf5988df43ec8efc96be1fbd39563f7?s=64&d=mm&r=g) [v.rajan](http://nil/)
     says:
    
    [July 2, 2015 at 2:47 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003775)
    
    good
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003775)
    
13.  ![](https://secure.gravatar.com/avatar/fffe83bc3e679b2fdfeae15bea5479f24c2dfed8b18593b4f3fc86b212b2856a?s=64&d=mm&r=g) fred fonda says:
    
    [July 2, 2015 at 6:13 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003860)
    
    simply awesome stuff. you got my attention can't wait for more.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003860)
    
14.  [How to analyze business data in Excel – 15 Quick & powerful ways | Chandoo.org – Learn Microsoft Excel Online | CompkSoft](http://compksoft.eu/?p=34311)
     says:
    
    [July 2, 2015 at 7:33 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003892)
    
    \[…\] [http://chandoo.org/wp/2015/07/01/how-to-analyze-business-data/](http://chandoo.org/wp/2015/07/01/how-to-analyze-business-data/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1003892)
    
15.  ![](https://secure.gravatar.com/avatar/1a7f6b0b2b07d3805460fec380f84e71db622e96ce7e429dc547dd6ea15d2bf8?s=64&d=mm&r=g) Lucho says:
    
    [July 4, 2015 at 1:53 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1004436)
    
    it\`s nice man! Thanks. I like it: brief explanations, powerful functions.
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1004436)
    
16.  ![](https://secure.gravatar.com/avatar/5264b5e865a8aece64c5ad7052e8b039793e63dc03a7b5bd529ce08a41fd25ed?s=64&d=mm&r=g) Abhishek says:
    
    [July 7, 2015 at 7:45 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1005566)
    
    hi, awesome.
    
    I want to join
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1005566)
    
17.  ![](https://secure.gravatar.com/avatar/f33949dd1ee9bddd9cc98439bbaf453d0e2a575ff4fe35795f06171488148aa1?s=64&d=mm&r=g) MingMong says:
    
    [August 28, 2015 at 1:49 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1032510)
    
    What's stopping me using powerpivot:  
    #link powerpivot tables on more than one criteria, e.g. Customer Name and postal code as they might have multiple delivery addresses.  
    #update names across multiple pivots (especially when grouping)  
    #grouping dates/number into non linear chunks, e.g 1-10, 10- 15, 15-28,28-31  
    #Quickly changing number format (i.e. rather than right click -> number format, click any cell and change the format for all numbers in that field, in that report.
    
    other things:  
    #fiscal calendar calcs -> 4/4/5 week vs calendar, P1= april? jan? September?  
    #mileage() -> variables are(Start point, end point, postal code/geocords, route option, route planner) output = mileage as per route planner (google/bing maps) and economic, fastest... etc  
    #Coffee() -> variables are (Number of drinks, mug size, type, milk, sugar, flavour, takeaway) -> obviously a joke, but well done for making it to the end...
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1032510)
    
18.  [#Excel Super Links #130 – shared by David Hager | Excel For You](https://dhexcel1.wordpress.com/2017/08/18/excel-super-links-130-shared-by-david-hager/)
     says:
    
    [August 18, 2017 at 11:43 am](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1498768)
    
    \[…\] [http://chandoo.org/wp/2015/07/01/how-to-analyze-business-data/](http://chandoo.org/wp/2015/07/01/how-to-analyze-business-data/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-1498768)
    
19.  ![](https://secure.gravatar.com/avatar/49e95c5c598132850a56f70f1f6baeb76cea7180418f8454f2e624ae994d63bf?s=64&d=mm&r=g) Chloe says:
    
    [January 15, 2023 at 3:49 pm](https://chandoo.org/wp/how-to-analyze-business-data/#comment-2119147)
    
    Hi Chandon,  
    I would like ask a question. I’m now warp ling with a project to analyse the Bottom 10 performance products with 6 parameters (like rating, no. Of clients etc). May I know if I can use proportion of each parameters and get score & 5 star rating for each of them?  
    Appreciate if you can help with this. Thanks!
    
    [Reply](https://chandoo.org/wp/how-to-analyze-business-data/#comment-2119147)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-to-analyze-business-data/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ