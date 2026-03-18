# Histograms & Pareto charts in Excel - tutorial, tips and downloadable template » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/histograms-pareto-charts-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Histograms & Pareto charts in Excel – tutorial, tips and downloadable template
==============================================================================

*   Last updated on October 5, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Time for some statistics and charting fun. Let’s learn **all about histograms and Pareto charts** in Excel 2016. You will learn

*   What, why and when?
*   How to set up and customize histograms
*   How to use Pareto charts?
*   How to create dynamic histograms?
*   Creating histograms in old Excel (2013 or earlier versions)

Sounds interesting? Let’s get started then.

### What is a histogram and why use it?

**Histogram chart shows distribution of data by grouping it in to bins (range of values).** Let’s say you run a customer care center. You have the call log from last month and you want to know how long customers talk to your representatives. If you just average all call lengths, you might get some value like 90 seconds. But this will not tell you the story. If you visualize the distribution of calls by duration like below, you will get a better picture. That is what a histogram is.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-outliers-grouped.png)

_**Histograms are a great way to explore the underlying distribution of values**_.

### So how to create a histogram in Excel?

Prior to Excel 2016, making histograms involved an intermediate calculation step. This is where you take raw data and calculate the frequencies by bins. But in Excel 2016, Microsoft introduced various new charts including Histograms and Pareto charts. Using these you can quickly make a histogram and understand the frequency distribution and outliers.

_Skip ahead to last section of this post if you want to know how to make Histograms in Excel 2013, 2010, 2007 or earlier versions._

To create histogram in Excel, you need some data. Let’s say you have data like this and you want to understand call duration distribution.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-data.png)

**To create histogram:**

1.  Select the call duration column
2.  Go to Insert > Statistic Chart > Histogram
    
    ![](https://chandoo.org/wp/wp-content/uploads/2017/10/insert-histogram-excel.png)
    
3.  You will get histogram of call duration with default binning ([using Scott’s normal reference rule](https://en.wikipedia.org/wiki/Histogram#Scott.27s_normal_reference_rule)
    )

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-default.png)

### Customizing Histograms

The histogram chart offers very few customization options (compared to other charts like column / scatter plot etc.). That said, you can customize the most important thing – _how Excel bins data._

To customize the bins, select the category / horizontal axis and press CTRL+1 to launch formatting options. You can also right-click on axis and choose format axis options. From here, you can choose how you want to bin your data.

**Options for binning and what they do:**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-binning-options.png)

*   **Automatic:** This is the default option. It bins your data by dividing it in to bins of width _h_, where `h= (3.5 * _sample standard deviation_) / (n1/3)`.
*   **Bin width:** If you know more about your data, you can set a custom bin width to analyze frequency by that. For our call center data, bin width of 15 or 30 seconds or even 60 seconds might be interesting.
*   **Number of bins:** You can specify number of bins and let Excel decide the width.
*   **By category:** Use this if you want to bin data by a category value. To use this option, you need to set category axis to some labels. For example, you can explore number of calls by representative this way.
*   **Overflow and Underflow settings:** Use this to set limits on values to bunch at both edges of your distribution range.

### Example Histograms

Check out below example histograms to understand how each of the binning settings work.

**Default Histogram – Calls by duration**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-default.png)

**Histogram – Calls by duration, bin width = 15 seconds**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-custom-bin-width.png)

**Histogram – Calls by duration, number of bins = 10**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-custom-bin-count.png)

**Histogram – Calls by duration, bin width = 15 seconds, outliers grouped.**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-outliers-grouped.png)

**Histogram – Calls by Representative – bins grouped by category**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-bins-by-category.png)

### Create interactive histogram

You can combine histograms with interactive features in Excel like slicers or form controls to create amazing histograms. Check out below demo:

![](https://chandoo.org/wp/wp-content/uploads/2017/10/dynamic-histogram-tip.gif)

To create an interactive histogram, follow below instructions.

1.  Make sure your data is formatted as table.
2.  Add a slicer on the column you want filter. Use Insert > Slicer option.
3.  Insert histogram as usual
4.  Now, if you operate the slicer, the histogram gets filtered too and shows distribution only for sliced values.

_**Related:**_

*   [Everything you ever wanted to know about Excel slicers – in this handy guide](https://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
    .
*   [Using form controls in Excel charts – Example](https://chandoo.org/wp/2013/11/05/gender-equality-gap-interactive-chart/)
    

### What is a Pareto Chart then?

A Pareto chart is a special kind of Histogram. In this chart, bins are arranged in descending order of frequency. Cumulative frequency is shown on secondary axis. Using this chart, you can understand which bins / categories contribute most.

**Here is an example of Pareto chart:**

![](https://chandoo.org/wp/wp-content/uploads/2017/10/pareto-chart-with-amount-bins.png)

### How to create Pareto charts in Excel?

The process is same as Histogram. Select a column containing values, _optionally_ include column with category information. Go to Insert > Statistic chart > Pareto chart. Here is an example Pareto chart of purchase amounts by representative.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/pareto-chart-category-bins.png)

**You can use custom bin settings too.** Just select the chart’s horizontal axis and customize. Here is an example Pareto chart on number of calls by amount with bin size = $25.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/pareto-chart-with-custom-bin-size.png)

### How to make histograms in older versions of Excel

If you do not have Excel 2016, you can still create histograms. You just need an intermediate step to convert raw data to frequencies by bin. You can use either formulas or data analysis tools to achieve this. Another simple way to achieve this is to use Pivot Tables > Grouping option.

**Creating histograms with Pivot tables:**

1.  Insert a pivot from your raw data
2.  Add numbers you want to bin to row label area.
    
    ![](https://chandoo.org/wp/wp-content/uploads/2017/10/old-excel-histogram-pivot.png)
    
3.  Add some text value or anything else to values area and summarize by count.
4.  Right click on row labels and choose group
5.  Set up bin size to group the numbers.

See this demo to understand the process.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histogram-in-old-excel-demo.gif)

_**The final result looks like this:**_

![](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-with-pivot-grouping.png)

### Download Histogram and Pareto Chart Examples

**[Click here to download workbook](https://chandoo.org/wp/wp-content/uploads/2017/10/histograms-in-excel-tips.xlsx)
** with histogram and Pareto chart examples. It has all the charts you saw in this tutorial. Examine the charts and settings to learn more.

### Do you create histograms & Pareto charts?

I make histograms all the time. They are excellent visualizations to understand your data. I used to make them with pivot / formulas in earlier versions. Now that they are available as charts in Excel 2016, I use them even more.

**What about you?** Do you create histograms? How do you make them? How do you like the new histogram and Pareto chart options in Excel 2016? Please share your thoughts in comments.

_**More tips for analyzing distribution of your data**_

*   [Show average and distribution to explain your data better](https://chandoo.org/wp/2011/04/06/show-average-and-distribution/)
    
*   [Box plots in Excel Dashboards – tutorial](https://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)
    
*   [Pareto Charts in Excel – Tutorial](https://chandoo.org/wp/2009/09/02/pareto-charts/)
    
*   [Introduction to Statistical analysis using Excel](https://chandoo.org/wp/2012/02/13/learn-statistics-probability-using-ms-excel/)
    
*   [15 quick and powerful ways to analyze business data](https://chandoo.org/wp/2015/07/01/how-to-analyze-business-data/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/histograms-pareto-charts-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/histograms-pareto-charts-in-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel 2016](https://chandoo.org/wp/tag/excel-2016/)
    , [histograms](https://chandoo.org/wp/tag/histograms/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pareto charts](https://chandoo.org/wp/tag/pareto-charts/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousFind out if a number has repetitive digits \[formula homework\]](https://chandoo.org/wp/number-has-repetitive-digits-formula/)

[NextConditional Formatting – Chart Data LabelsNext](https://chandoo.org/wp/conditional-formatting-chart-data-labels/)

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
    
    [Reply](https://chandoo.org/wp/histograms-pareto-charts-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/histograms-pareto-charts-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/histograms-pareto-charts-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ