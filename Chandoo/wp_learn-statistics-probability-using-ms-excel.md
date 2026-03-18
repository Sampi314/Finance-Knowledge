# Learn Statistics & Probability using MS Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/learn-statistics-probability-using-ms-excel

---

*   [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Learn Statistics & Probability using MS Excel
=============================================

*   Last updated on February 13, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

One of the most dreaded courses during my under-graduation is _**Probability, Statistics & Queuing Theory**_. We called it PSQT. I struggled to understand the significance and concept of this course as I could barely concentrate in the class. We had a professor, who is probably a genius, but the moment he started the class, I would magically fall in to one of my after-noon naps. When I woke up, we are either in the middle of an elaborate _t-test_ or going thru intricacies of a _Markovian queue_.

This was all 11 years ago. Later in life, I have embraced the world of probability & statistics. I still fear queues. May be I will get there one day. 😉

**A good understanding of statistics & probability theory is necessary if you want to model complex real-life problems using Excel or similar tools.** Naturally, Excel has several functions, features & supported add-ins to help you in this area.

Today, I want to share some of this with you. This article is broken down in to 3 parts.

1.  Learning Statistics & Probability using Excel
2.  Downloadable Excel Workbooks to understand
3.  Full blown models & simulations in Excel

#1 – Learning Statistics & Probability Concepts using Excel
-----------------------------------------------------------

### Using Excel RAND functions

Excel has several powerful functions (formulas) to generate random numbers, random data. You can combine these functions to generate data that has certain parameters – like a give mean, standard deviation or follows a certain type of distribution.

**Go thru [Using Excel’s Random Functions](http://chandoo.org/wp/2011/05/04/dummy-data-random-functions/)
 for a detailed overview these techniques.**

### Simulating Dice Throws in Excel

One of the fundamental ways to learn about Probability is to look at dice throws. A dice has 6 faces and on each throw, any of the 6 faces turning up is equally likely. So, we say, each face has 1/6th probability of showing up. If you want to simulate this in Excel, you can use the formula **RANDBETWEEN** like this, =RANDBETWEEN(1,6). On each run, this formula would throw up a random number between 1 & 6 (including both).

**For more, [Simulating Dice Throws in Excel](http://chandoo.org/wp/2008/08/13/simulate-dice-throws/)
**

### Shuffling a List of Values in Excel

Understanding permutations and combinations is essential when it comes to modeling many real-world problems. Using Excel’s RAND, VLOOKUP and SMALL formulas we can generate a random permutation of a given list of values (in other words – we can shuffle the list).

[![Shuffling a list of values in Excel](https://chandoo.org/wp/wp-content/uploads/2008/09/shuffling-list-of-items-excel-formulas.png "Shuffling a list of values in Excel")](http://chandoo.org/wp/2008/09/23/sort-in-random-order-excel-formulas/)

**To learn this read, [Shuffling a list of values in Excel](http://chandoo.org/wp/2008/09/23/sort-in-random-order-excel-formulas/)
**

### Generate Frequency Distribution from Data

Often, when you are analyzing data, you need to understand how the data is distributed. Again, Excel has just the right function for this sort of thing. FREQUENCY(). In this simple tutorial, learn how to use Excel’s FREQUENCY formula to generate frequency distribution of given data.

[![Calculating Statistical Frequency Distribution in Excel](https://img.chandoo.org/n/statistical-distributions-using-frequency.gif "Calculating Statistical Frequency Distribution in Excel")](http://chandoo.org/wp/2009/06/01/statistical-distributions/)

**Read [Frequency Distributions in Excel](http://chandoo.org/wp/2009/06/01/statistical-distributions/)
**

### Trend Analysis & Forecasting using Excel

One of the most common applications of statistics is **trend analysis & forecasting.** Again, Excel shines with a lot of powerful formulas, built-in features and charting tools to help you understand the data & predict future based on that.

Since this is a big topic, we have covered it in 3 parts –

[**Part 1- Introduction to Trend Analysis & Forecasting**](http://chandoo.org/wp/2011/01/24/trendlines-and-forecasting-in-excel/ "Introduction to Trend Analysis & Forecasting in Excel")
: In this, we will learn what is trend analysis & forecasting. We will see **manual forecasting** technique in Excel. We will use Excel charts to depict our analysis and results.

[![Trend Analysis & Forecasting using Manual Forecasting Technique in Excel](https://chandoo.org/wp/wp-content/uploads/2011/01/Trend_E01_mx+c.png "Trend Analysis & Forecasting using Manual Forecasting Technique in Excel")](http://chandoo.org/wp/2011/01/24/trendlines-and-forecasting-in-excel/)

[**Part 2 – Trend Analysis & Forecasting using Excel Functions**](http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/ "Trend Analysis & Forecasting using Excel Functions")

In this second part, we learn about Excel’s functions like LINEST, TREND, FORECAST, SLOPE, INTERCEPT, LOGEST and GROWTH. These powerful formulas can process lots of data and extract the trend information dynamically.

[![Trend Analysis and Forecasting using Excel's functions & charts](https://chandoo.org/wp/wp-content/uploads/2011/01/NL7.png "Trend Analysis and Forecasting using Excel's functions & charts")](http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/)

**[Part 3 – Trend Analysis & Forecasting using Charts & Macros](http://chandoo.org/wp/2011/01/27/trendlines-and-forecasting-in-excel-part-3/)
**

In the final part, we talk about how to use Excel chart’s trend analysis & forecasting features to estimate the trend & predict future values based on the data.

[![Trend Analysis & Forecasting using Excel Charts & VBA](https://chandoo.org/wp/wp-content/uploads/2011/01/tl3lin.png "Trend Analysis & Forecasting using Excel Charts & VBA")](http://chandoo.org/wp/2011/01/27/trendlines-and-forecasting-in-excel-part-3/)

We also learn how to use Macros (VBA) to augment Excel chart’s trend-lines with useful information.

### Visualizing Distribution of data with Box Plots

Box plots are an excellent way to understand the distribution of data. Unfortunately, there is no direct option to make a box plot from given data in Excel. That is where, this tutorial comes handy.

[![Box plots in Excel - How to](https://img.chandoo.org/c/boxplots-in-excel-how-to.png "Box plots in Excel - How to")](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

**[Learn how to create box plots in Excel](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)
.**

_[more on Box plots](http://chandoo.org/wp/tag/box-plots/)
._

#2 Downloadable Excel Workbooks
-------------------------------

### Learn Basic Statistics & Gaussian Distribution using this Excel Workbook

_Glen_, one of our long time readers shared this file with me. It lets you perform statistical analysis, quality control analysis, visualize Gaussian distribution based on the data you enter.

[**Click here to download the workbook**](https://img.chandoo.org/d/analyze-this-glen.xls "Analyze this - Basic Statistical Analysis, Quality Control & Gaussian Distribution of Data in Excel")
.

![Gaussian Distribution of Data in Excel](https://img.chandoo.org/c/gaussian-distribution-of-data-in-excel.png "Gaussian Distribution of Data in Excel")

**_Thanks Glen._**

### More Downloadable Workbooks

Almost all of the links in this page will take you to detailed articles on Chandoo.org, where you can also find downloadable workbook with examples. So just click thru and learn. 🙂

#3 Full blown models & simulations in Excel
-------------------------------------------

A full blown model lets you learn various statistical concepts, Excel features and how to bring them all together to mimic a real-life situation.

### Simulating Deal or No Deal game in Excel

In this simulation of Deal or No Deal, a popular television game, we use basic probability, permutations and Excel formulas features. You will learn how to assign random values to the suit-cases, how to use circular references, how to calculate the banker’s offer.

[![Simulation of Deal or No Deal game in Excel](https://chandoo.org/wp/wp-content/uploads/2008/10/excel-deal-or-no-deal-game-simulation-1.png "Simulation of Deal or No Deal game in Excel")](http://chandoo.org/wp/2008/10/03/download-excel-deal-or-no-deal-game-play/)

[**Simulation of Deal or No Deal game in Excel**](http://chandoo.org/wp/2008/10/03/download-excel-deal-or-no-deal-game-play/)

### Generating Housie / Bingo Tickets in Excel

Housie (Bingo) is a popular recreational game where the tickets contain 15 numbers between 1 to 90, arranged in 10 columns (3×10 grid). First column has numbers between 1 to 9, second column has 10 to 19 so on..

Generating a bingo ticket in Excel is a nice exercise in statistics, permutations and Excel formulas.

[![Generating Housie / Bingo tickets using Excel](https://chandoo.org/wp/wp-content/uploads/2008/07/generate-bingo-tickets-in-excel.gif "Generating Housie / Bingo tickets using Excel")](http://chandoo.org/wp/2008/07/16/bingo-housie-ticket-generator-excel/)

**Learn from [Bingo / Housie Tickets in Excel](http://chandoo.org/wp/2008/07/16/bingo-housie-ticket-generator-excel/)
**

### Data Tables & Monte Carlo Simulations in Excel

Excel has powerful features to let us do complex simulations of real world situations. One such feature is called as **data table**.

**The Data Table** allows a set of what if questions to be posed and answered simply, and is useful in sensitivity analysis, variance analysis and even Monte Carlo (Stochastic) analysis of real life model within Excel.

**The case of Blue Sky Mining Company**

To help you learn about data tables, Monte Carlo simulations, we have put together a fictional mining company – Blue Sky co. and analyzed its performance under various assumptions & simulations.

[![Data Tables & Monte-Carlo Simulations using Excel](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-13.png "Data Tables & Monte-Carlo Simulations using Excel")](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)

To learn about this, visit [**Data Tables & Monte-Carlo Simulations page**](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/ "Data Tables & Monte Carlo Simulations using MS Excel")
.

### Modeling & Scheduling a FIFO (First In First Out) Queue in Excel

FIFO queues are very common in life. You can see them at Airports, coffee shops, Apple stores; Except at Airports it is FIFOUYC (FIFO Unless You are Crew).

[**In this article, we model & schedule a FIFO queue using Excel**](http://chandoo.org/wp/2010/11/18/scheduling-variable-sources/ "Modeling & Scheduling a FIFO Queue in Excel")
.

### More Full Blown Models & Simulations in Excel

For more examples, check out these links.

*   [One more example of Data Table & Linest](http://chandoo.org/wp/2011/06/20/analyse-data-like-a-super-hero/)
    
*   [Simulating 3D dancing pendulums in Excel](http://chandoo.org/wp/2011/06/23/automating-repetitive-tasks/)
    
*   [Simulating Monopoly Board Game in Excel](http://chandoo.org/wp/2007/02/25/is-monopoly-fair/)
    

Do you use Statistical Concepts for your work?
----------------------------------------------

As a small business owner, a good portion of my work involves statistical analysis, forecasting and simulation. I run estimates for our website traffic, revenues. I run statistical tests (split tests etc.) to optimize our sales pages, website. I estimate when my kids wake up from their nap (based on past experience) and plan my work accordingly. Thankfully, for the last part, I do not use Excel 😀

**What about you?** Do you use statistical concepts for your work? What are the things you use and how does Excel help you in that? What are your favorite formulas, features and tips? **Please share using comments.**

Special thanks to Hui & Glen
----------------------------

Many thanks to Hui, our resident Excel ninja for writing many of the articles on statistics, simulation, forecasting & trend analysis.

Special thanks to Glen for sharing the _analyze-this_ file with us.

Say thanks to them if you enjoyed this.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [box plots](https://chandoo.org/wp/tag/box-plots/)
    , [data tables](https://chandoo.org/wp/tag/data-tables/)
    , [distributions](https://chandoo.org/wp/tag/distributions/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Forecasting](https://chandoo.org/wp/tag/forecasting/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Linest](https://chandoo.org/wp/tag/linest/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [monte carlo simulations](https://chandoo.org/wp/tag/monte-carlo-simulations/)
    , [rand()](https://chandoo.org/wp/tag/rand/)
    , [RANDBETWEEN()](https://chandoo.org/wp/tag/randbetween/)
    , [simulation](https://chandoo.org/wp/tag/simulation/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [trend lines](https://chandoo.org/wp/tag/trend-lines/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHow would you customize Excel after installing? \[poll\]](https://chandoo.org/wp/how-would-you-customize-excel-after-installing-poll/)

[NextReporting Scenarios using OffsetNext](https://chandoo.org/wp/reporting-scenarios-using-offset/)

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
    
    [Reply](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/learn-statistics-probability-using-ms-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ