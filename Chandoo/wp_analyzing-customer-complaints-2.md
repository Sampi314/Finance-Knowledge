# Analyzing half a million customer complaints - Regional Trends [Part 2 of 3] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/analyzing-customer-complaints-2

---

*   [3D Maps (Power Maps)](https://chandoo.org/wp/category/3d-maps-power-maps/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Analyzing half a million customer complaints – Regional Trends \[Part 2 of 3\]
==============================================================================

*   Last updated on October 10, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is part two of our three part series on **how to analyze half a million customer complaints.**_ [Read part 1 here](https://chandoo.org/wp/analyzing-consumer-complaints-1/)
.

![regional-trends-customer-complaint-vis](https://chandoo.org/wp/wp-content/uploads/2016/02/regional-trends-customer-complaint-vis.png)

This is the second part of 3 part series on this theme. Please use below links to access other parts.

1.  [What do they complain about – Part 1](https://chandoo.org/wp/analyzing-consumer-complaints-1/)
    
2.  **Regional trends – Part 2**
3.  [My bank vs. your bank in a scorecard – Part 3](https://chandoo.org/wp/customer-satisfaction-scorecard/)
    

Analyzing Regional Trends
-------------------------

As introduced in [part 1](http://chandoo.org/wp/2016/02/16/analyzing-consumer-complaints-1/)
, our complaints dataset has geographical information too. We know the state & _zip code_ for each complaint. Please note that _zip codes_ are partial or missing for a 10% of the data.

In this article, let’s explore three ways to analyze regional trends.

1.  Regional trends by state, product & issue
2.  Complaints per million by state
3.  Complaints by zip code

1. Regional trends by state, product & issue
--------------------------------------------

First, we need to identify the goals for this analysis. You can define any number of goals for this data set. Let’s start with these goals,

*   Understand yearly trend by state between 2012 & 2015 (we don’t have full data for 2011 or 2016)
*   Explore 2015 monthly trend to understand patterns
*   Understand top 3 issues bothering the customers
*   Look at the trends at whole or by any individual product
*   Don’t let bigger states hijack the report
    *   This means we need to [index the data](http://chandoo.org/wp/2012/10/09/indexed-charts-in-excel/)
        .
*   Rearrange the report so we can focus on states that require most attention.

Feel free to add your own goals and analyze data to fulfill them.

### Mockup for our visual analysis

Given the geographical nature of this data, we would be tempted to go with a _maps_ based visualization. Unfortunately, maps tend to distort the data, as bigger states get more space. So for this analysis, let’s stick with good old tables, lines & dots.

Here is a mockup of the analysis we are trying to achieve.

![regional-trends-mockup](https://chandoo.org/wp/wp-content/uploads/2016/02/regional-trends-mockup.png)

### From raw data to analysis – the journey

I will be honest here. The journey from raw data with 500,000 rows to the analysis we need is not an easy one. As I wanted to analyze this data with tools & features native to Excel 2010 (so that maximum readers can enjoy this), I had to say no to Power Pivot, VBA, Power Maps, Timelines etc.

**What about formulas?**

Using formulas like SUMIFS, INDEX, MATCH, VLOOKUP or SUMPRODUCT is also a no-no as we have too much data. So what to do?

**Here is the process:**

*   Remove un-necessary columns from the raw data. We end up with just 7 columns (from 16)
*   Create pivot tables from raw data
    *   Pivot 1 – Complaint count by Year, Month, State, Product
    *   Pivot 2 – Complaint count by Product, Issue, State for the year 2015
    *   Pivot 3 – Complaint count by Issue, State for the year 2015
*   Build calculations that talk to pivot tables to fetch the numbers we want
    *   Define named ranges for the pivot table data, row & column labels so that we can easily access them in our formulas
    *   Get the numbers we need using [GETPIVOTDATA](http://chandoo.org/wp/2015/08/26/getpivotdata-in-dashboards/)
        , [INDEX](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
         & [SUMIFS](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
        
*   Define [form controls](http://chandoo.org/wp/2011/03/30/form-controls/)
     to capture user choices for product, sort order & indexed data
*   Sort data by given criteria using [LARGE formula](http://chandoo.org/excel-formulas/large.shtml)
    *   [Use deduplication technique to avoid ties](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
        
*   Plug the calculations to output worksheet.
*   Set up a [scrollbar form control](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
     to show 12 states at a time, as we have limited space on the screens.
*   Show trend [using sparklines](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
    
*   [Show alert icon](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/)
     for states with >20% increase in complaint volume using conditional formatting.
*   Tidy up the output

### Regional trend analysis – final output

Here is the final output of the regional analysis report.

[![regional-trends-analysis-customer-complaints-data](https://chandoo.org/wp/wp-content/uploads/2016/02/regional-trends-analysis-customer-complaints-data.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/regional-trends-analysis-customer-complaints-data.png)

2\. Complaints per million by state
-----------------------------------

Of course, as the data has geographical component, I am tempted to try some map based visualizations to analyze it. So for this & next type of analysis, I have used new Excel 2016 feature – **3D Maps** (known as Power Maps in earlier versions).

If we chart the complaint data directly, bigger states (like CA, FL etc.) will hijack the map. So I downloaded 2015 population estimates ([from Wikipedia](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population)
) and combined this information to calculate a new metric **_complaints per million._** 

I created two map layers – one with complaints per million in 2015 & another to mark states with above average complaint rate.

Check out the visualization below. For more, download the 3D maps workbook.

![state-level-trends](https://chandoo.org/wp/wp-content/uploads/2016/02/state-level-trends.png)

3\. Complaints by zip code
--------------------------

While many of us think zip codes are actual geographical regions (ie polygons), they are not. They are simply postal routes. So gathering population by zip code is hard. Fortunately, I found a [Population by zipcode – 2010 – dataset here](http://blog.splitwise.com/2013/09/18/the-2010-us-census-population-by-zip-code-totally-free/)
. It is for year 2010, but the data is a good proxy for our analysis.

In our dataset, zip code data is not available for roughly 10% records. So I eliminated them and analyzed the rest. When calculating the _**complaints per thousand**_ metric, I noticed another anomaly. Certain zipcodes have very little population (~ 3,000 zipcodes have less than 500 people). So if they have even 1 complaint in 2015, their CPT (complaints per thousand) will be very high.

**Here is the first visualization – Complaints per thousand by Zipcode**

![trends-by-zip-1](https://chandoo.org/wp/wp-content/uploads/2016/02/trends-by-zip-1.png)

To avoid the too little population problem, I have applied a filter in 3D maps so that if a ZIP code has less than 10 complaints, we don’t show them on the map.

**Here is the second visualization**

![trends-by-zip-2](https://chandoo.org/wp/wp-content/uploads/2016/02/trends-by-zip-2.png)

Quick demo of the visualizations
--------------------------------

In case you are unable to download the files or want to just peek at these awesome visualizations, see below video.

You can also [see this on our YouTube Channel](https://youtu.be/l40X0iovf0M)
.

Download the workbooks
----------------------

There are two workbooks for this article.

*   [Regional trends dashboard – compatible with Excel 2010 or above](https://files.chandoo.org/50w/consumer-complaints-vis-2.xlsx)
    
*   [Regional trends maps – Opens in Excel 2016](https://files.chandoo.org/50w/consumer-complaints-3dmap.xlsx)
     (2013 with Power Maps, but not tested)

### How would you analyze the complaint data?

**Go ahead and play with this data yourself.** How would you analyze it? Please share your ideas, analysis & charts in the comments section. _**If you wish to publish a chart,**_ email it to chandoo.d@gmail.com with the subject “Half a million complaints”. I will add your chart at the end of this post.

### Learn more about data analysis & reporting

I cover this topic and 50 other case studies in my online class **50 ways to analyze data.** If you are keen to learn advanced analytics and data science thru Excel, I highly recommend 50 ways course. [**Check it out here**](https://chandoo.org/wp/resources/50-ways-to-analyze-data/)
.

For something less intense, but still as much fun and detailed, check out Excel School program. This course teaches intermediate to advanced Excel with specific focus on Dashboard Reporting. [**Check out Excel School here**](https://chandoo.org/wp/excel-school-program/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [3 Comments](https://chandoo.org/wp/analyzing-customer-complaints-2/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analyzing-customer-complaints-2/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [condtional formatting](https://chandoo.org/wp/tag/condtional-formatting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [GETPIVOTDATA](https://chandoo.org/wp/tag/getpivotdata/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [maps](https://chandoo.org/wp/tag/maps/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [power maps](https://chandoo.org/wp/tag/power-maps/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [3D Maps (Power Maps)](https://chandoo.org/wp/category/3d-maps-power-maps/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousAnalyzing half a million consumer complaints \[Part 1 of 3\]](https://chandoo.org/wp/analyzing-consumer-complaints-1/)

[NextAnalyzing half a million complaints – Customer Satisfaction Scorecard \[Part 3 of 3\]Next](https://chandoo.org/wp/customer-satisfaction-scorecard/)

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
    

### 3 Responses to “Analyzing half a million customer complaints – Regional Trends \[Part 2 of 3\]”

1.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [February 18, 2016 at 2:00 pm](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134005)
    
    The size of the file named as "consumer-complaints-3dmap.xlsx" is 66.1 MB. It is too big. Isn't it?  
    Would you like to shrink the size to 55.9 MB. Saving more than 15% is possible by saving the same file with XLSB extention instead of XLSX extention.
    
    [Reply](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134005)
    
2.  ![](https://secure.gravatar.com/avatar/e9b7fcc88dc631a72c1314fd96b86794b238a37875d57b3b884c8e85adffa719?s=64&d=mm&r=g) Daniel says:
    
    [February 19, 2016 at 8:12 am](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134285)
    
    Hi, I have Excel 2013 Prof Plus, but I dont find Power Maps under the Com Add Ins - any idea? Thanks and best regards, Daniel
    
    [Reply](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134285)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 21, 2016 at 2:49 am](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134911)
        
        @Daniel  
        It is an addin that has to be added  
        It doesn't come standard with Excel  
        Visit microsoft: [https://www.microsoft.com/en-us/download/details.aspx?id=38395](https://www.microsoft.com/en-us/download/details.aspx?id=38395)
        
        [Reply](https://chandoo.org/wp/analyzing-customer-complaints-2/#comment-1134911)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/analyzing-customer-complaints-2/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ