# 15 Quick and Powerful ways to Analyze Business Data » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/resources/15-ways-to-analyze-business-data

---

15 Quick and Powerful ways to Analyze Business Data
===================================================

Smart tips for awesome analysts
-------------------------------

_Here is a situation all too familiar._

You are looking at a spreadsheet full of data. You need to analyze and tell a story about it. You have little time. _**You don’t know where to start**_.

Today let me share **15 quick, simple & very powerful ways to analyze business data**. Ready? Let’s get started.

1\. Describe data with quick stats

You know…, the good old AVERAGE, COUNT, SUM, MIN, MAX, MEDIAN, and Range of the data.

You can calculate all of these with simple Excel formulas.

If you are lazy (or in a bit of hurry), you can use the Descriptive statistics feature of Data Analysis Tools add-in (this is available in Excel by default. You just need to enable it by going to File > Options > Add-ins > Manage Excel Add-ins > Go).

![Descriptive statistics in Excel using Data Analysis toolpack add-in](https://img.chandoo.org/analysis/descriptive-statistics-excel.png)

Related: [Going beyond AVERAGE to summarize data – Podcast part 1](http://chandoo.org/wp/2014/05/22/cp009-averages-are-mean-part1/)
 & [part 2](http://chandoo.org/wp/2014/05/30/cp010-averages-are-mean-part2/)

2\. Heatmap it

When you have a bunch of numbers, you can use heatmaps / color scales to to find what’s going with it in the quickest & most fun way.

Just select the numbers and go to Home > Conditional Formatting > Color-scales and pick a color scale you like.

See the numbers light up based on how high / low they are.

![Create a quick heatmap using conditional formatting color scales in Excel](https://img.chandoo.org/analysis/heatmap-excel-example.png)

3\. Spot the trend

Your data may have some trends buried in it. Uncovering these trends can be hard if you look at numbers alone. But with a simple line chart, you can quickly see how things are going, what has been the general direction of your numbers and _may be even predict_ what is going to happen next.

To spot the trend, simply select the data and create a line chart (or even a sparkline)

4\. 80 / 20 – Pareto Analysis

[Pareto analysis](http://chandoo.org/wp/2009/09/02/pareto-charts/)
 (also known as 80/20 analysis) refers to the idea that 80% of outcomes in many situations are governed by 20% factors.

For example, in a manufacturing company 80% of defects may be reported by just 20% of the process steps

or in a website, 80% of visitors may be going to 20% of the pages.

![Interactive Pareto Chart - part of 50 ways to analyze data course - Chandoo.org](https://lsns.chandoo.org/50w/img/demo-03-pareto-analysis.gif)

5\. Index the numbers

Let’s say you are looking at sales of various products. Product A sells between 4000 and 5000 units per month. Product B sells between 1000 and 1500 per month. How would you compare these two product performances?

You can index their sales to a common starting point, like 100 and then analyze relative performance with the help of [indexed charts](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
.

Something like this:

![Indexed charts - compare numbers that do not have same base - Excel data analysis & charting technique](https://img.chandoo.org/c/example-indexed-chart-in-excel.png)

6\. Weighted average it

**Pop quiz:** _If a cup of coffee at Joe’s Brew costs $4 on weekdays and $3 in weekends, what is the average cost of coffee over a week?_

Hint – the answer is not $3.5

![Weighted averages in Excel - how to & formula](https://chandoo.org/img/f/weighted-average-excel-formula.png)

When analyzing real-life data, calculating average may not cut it. You may have to calculate weighted average to get the true picture of your numbers.

Related: [learn more about weighted average formula](http://chandoo.org/wp/2010/06/15/weighted-average-excel/)
.

7\. Find the outliers

Quick story – A professor walked in to the freshmen class of an MBA program. She took out a blank sheet of A4 paper, placed a dot with red marker on it somewhere. Then she showed the paper to students and asked them “what do you see?”

Everyone said “a red dot”.

Not a single person said “a white paper”.

That’s because our focus is always on outliers (things that are not normal).

So next time you are looking at business data, find out those red dots.

8\. Slice & Chart it

If you create a chart from lots of data, then it looks cluttered.

But when you apply filters or [slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
 to original data, the chart will show only filtered data.

This is a quick & powerful way to slice your data and visualize sub-sets to spot trends or insights.

![Adhoc trend chart with slicers in Excel - demo](https://img.chandoo.org/analysis/slicer-chart-adhoc-analysis-demo.gif)

9\. Check out the distribution on this curve!

When you understand the shape of your data, you can tell better stories about it.

To quickly check the shape of your data,

*   Find the range of your data (min & max values)
*   Divide this range in _n_ equal ranges (start with n=10 and refine until you are happy)
*   Find out how many values fall in each of those n ranges (calculate the frequency using formulas like COUNTIFS)
*   Create a column chart with this frequency data (called as histogram)
*   Spot the shape from this histogram.

10\. Rank it / Sort it

Sort your data using Excel sort options or rank the data points against all values using RANK() formula. This will tell you where each value fits in.

Related: [Sort values using formulas in your dashboards](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)

11\. Top 5 it

Sometimes when you have too many items, it’s better to focus on just top 10 values or bottom 5 values. For example, if you are analyzing sales of 745 products, looking at all the 745 items is going to be very tiring. Instead you can filter the list down to top or bottom few values and then focus on these unique items.

![Top 10 items using Excel Pivot table filters](https://chandoo.org/img/dashboards/top-10-values-dashboards.png)

To do this, you can use

*   Regular data: Auto filter > Number filters > Top 10 option
*   Pivot tables: [Filter > Value filters > Top 10](http://chandoo.org/wp/2010/12/01/top-10-values-in-dashboards/)
    

Also, you can [use conditional formatting to highlight top or bottom _n_ items](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
. You can also highlight top or bottom _x%_ values.

12\. Got change?

When you have data for more than 1 year (or month), you can analyze % change year over year to spot valuable information.

![% change over time - display using conditional formatting in Excel](https://img.chandoo.org/dashboards/final-regional-summary-report.png)

These kind of % changes (YoY, MoM etc.) are very useful in companies that experience business cycles. For example, if you sell scarves, you can expect more sales in winter months. So when comparing % change, you should compare with last year same month values instead of previous month to understand how good the performance has been.

To visualize such changes, you can use conditional formatting > icons > arrows

Related: [Never use simple numbers in your dashboards](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/)

13\. Spot the the duplicates

When comparing two or more sets of data, often understanding how many values are duplicated (or not) in your lists can be helpful.

For example, if you are analyzing list of customers visiting your store this month & last month, you may want to know how many people visited your store both months (ie how many customers are loyal?)

To spot the duplicates quickly, you can use Conditional Formatting > Duplicates (related: [compare 2 lists in Excel](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)
).

![Compare 2 lists using Excel conditional formatting](https://chandoo.org/img/cf/compare-2-lists-conditional-formatting-qt.gif)

To count how many values are overlapping in 2 sets of data, you can use formulas.

14\. Find the rate of return

**Question time:** It was year 2015. Johnny is new to stock market. He bought company K’s shares for $500 in 1st of Jan 2015. Fast forward to July 2015. He wanted to find out how much his $500 investment is worth now. So he looked at company K’s share price data. Here is what he found.

The stock went up (or down) by -10%, 10%, -15%, 15%, -10%, 10% in first 6 months of the year.

_**So what is his investment worth now?**_

This is where ideas like FV (future value) come in to picture.

![FVSCHEDULE() Excel formula to calculate future value after a series of % changes](https://img.chandoo.org/analysis/fvschedule-demo.png)

You can use a formula like FVSCHEDULE() to quickly calculate how much the investment is worth after a series of % changes.

Related: [Calculating CAGR using Excel](http://chandoo.org/wp/2014/04/29/calculate-cagr-using-excel/)
.

15\. Count by occurrence

When analyzing textual data (like customer names, vendor IDs, part numbers etc.) you may want to know how many times each item has occurred in the list, what is the most frequent item etc. To get this quickly, just set up a pivot table. Add the customer name column to both row labels & value field area of the pivot table. Sort the pivot by value field, largest to smallest. And your report is ready.

Want more? Masterclasses in Australia – 2018

If your job involves data analysis & story telling (to be honest _all_ jobs require these skills), then you are going to love my **2018 Australian Masterclasses**.

It gives me great pleasure to invite you to my 2018 round of Excel & Power BI masterclasses in Australia. This year, we are doing masterclasses on two exciting themes:

*   Advanced Excel & Dashboard Reporting
*   Power BI, Power Pivot and Power Query

Both courses are packed with lots of insight, hands-on exercises, tips and awesomeness. Each Master Class is for 2 days and you can go for either or both. It is available in Sydney, Melbourne, Brisbane and Perth. I am running these course in partnership with Plum Solutions. 

We are taking bookings now and there are limited spots available. [**Click here to know more and sign up for the Australian Masterclasses**](https://plumsolutions.com.au/chandoo/)
.