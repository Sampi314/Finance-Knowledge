# Designing awesome financial metrics dashboard [tutorial] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/financial-dashboard-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Designing awesome financial metrics dashboard \[tutorial\]
==========================================================

*   Last updated on February 5, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is a guest post by Chandeep.** He won our recent dashboard contest and kindly agreed to share the technique and process for creating such an awesome dashboard with all of us._ 

Hi to all the awesome people at Chandoo.org

**Quick Intro** – My name is Chandeep Chhabra and I live in Gurgaon, India. Luckily **[Chandoo’s 2016 Dashboard contest](http://chandoo.org/wp/2016/06/24/visualize-multi-variable-data-contest/)
**, my Dashboard entry was picked up as **[a winning entry](http://chandoo.org/wp/2016/09/23/visualizing-financial-metrics-contest-winners/)
**. Thank you so much for all your appreciation and likes

A few days later I reached out to Chandoo asking him to let me write everything about this dashboard, right from the thought process I followed to finally making a ticked and tied dashboard.

**What I am going to cover in this post ?**
-------------------------------------------

Since we are talking about an entire dashboard here, this is going to be a long post (I mean really long). Here is what I plan to cover

1.  **How did I plan this Dashboard ?** – All my Dashboard pre-work is included here
2.  **How did I create the Dashboard** – This all about number crunching, formula writing, setting up things etc.. I am not going to discuss the formulas in detail but I will give you the overall logic and the formula behind it. To make things structured I have divided this part into 2 main sections
    1.  Screen 1 Calculations – Everything about the 1st screen (company comparison)
    2.  Screen 2 Calculations – All about screen 2 (overall market)
3.  **How did I format the Dashboard** – I discuss everything right from colors themes to the overall look and feel. Again the formatting is divided into 2 sections
    1.  Screen 1 Formatting
    2.  Screen 2 Formatting
4.  **How much time did I spend creating it** – Specific breakdown into hours for each section
5.  **Mistakes that could have been avoided** – A few mistakes that I personally found in my work that could have been avoided

Alongside this post, I have also put together a video to explain this dashboard [**you can get the video + resources here**](http://www.goodly.co.in/bonus-content-dbcontest/)

**Part 1 – How did I plan this Dashboard !**
--------------------------------------------

The first glance at the data made me feel comfortable, since I carry a finance background and have mostly played with financial data. So I came with 2 key objectives

1.  My dashboard has to answer all important questions that were relevant to the audience/management  
    The look and feel of the dashboard has to be simple and yet stunning
2.  I am going to breakdown the objective into concrete actionable steps that I took to finally complete this dashboard + throw in some general good practices that I personally follow

**Quick Tip:** I draw from **[Chandoo’s 10 step Dashboard Process](http://chandoo.org/wp/2014/07/10/cp014-create-awesome-dashboards/)** with a few tweaks of my own

**Gathering all important and relevant questions**

Chandoo did give us a good head-start about objectives of the dashboard

![Dashboard Objectives](https://chandoo.org/wp/wp-content/uploads/2017/02/Dashboard-Objectives.png)

I also reached out to a few friends and asked them, what additional things would they like to know from the data. The list got a bit bigger. This is exactly what I came up with

![Additional Dashboard Objectives](https://chandoo.org/wp/wp-content/uploads/2017/02/Additional-Dashboard-Objectives.png)

I then started quickly crunching numbers and doing analysis to find the answers to the above questions. Once I did all the meaningful calculations, I quickly made a rough sketch (mock) of the dashboard. This mock is to understand 2 things

1.  How am I going to fit all this data and analysis in the sheet?
2.  How the overall picture will look like?

**Below is how the mock up looked!**

![Dashboard Mock](https://chandoo.org/wp/wp-content/uploads/2017/02/Dashboard-Mock.png)

**Part 2 – How did I create this Dashboard ?**
----------------------------------------------

Even before I start showing the workings of the dashboard I strongly suggest you to **[download the Dashboard](https://img.chandoo.org/contests/mv2016/xl/chandeep-c.xlsx)
** and then follow the instructions discussed, it will a lot easier that way.

You can also [**get access to the explainer video + resources**](http://www.goodly.co.in/bonus-content-dbcontest/)

**Screen 1 Calculations – Performing a multiple criteria lookup**

Take a look at how the Visualisation and its backend is performing a 2 way lookup

1.  When you select a Company name (using a slicer), the pivot table stores the value of the slicer (company name) in a cell
2.  When the cost variable is selected (again using a slicer), the chart highlights that variable. But we are not exploring the chart as of now, We’ll keep that aside for a while

![Calculation P1](https://chandoo.org/wp/wp-content/uploads/2017/02/Calculation-P1.png)

Now here is the Lookup formula used to lookup values for cost variables. Total Variable Cost and Operating Leverage were calculated separately. Note that the formula

1.  Matches the company name (Company1)
2.  Matches the Variable Name
3.  And the year using the Columns Function

![3 Way Lookup Formula](https://chandoo.org/wp/wp-content/uploads/2017/02/3-Way-Lookup-Formula.png)

Once these values were calculated I directly plugged them in the Dashboard

Links for newbies to **[INDEX](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
, [MATCH](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
, [OFFSET](http://chandoo.org/wp/2012/09/17/offset-formula-explained/)** & **[COLUMNS](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)** Functions

\[One of the techniques used\] – How to use **[slicer without a Pivot Table](https://sites.google.com/site/e90e50fx/home/combine-slicers-with-dynamic-charts-and-dashboards)
**

**Screen 1 Calculations – How the Stacked Chart was made**

A regular stacked chart looks like this. One big problem – _too many colors!\\_

![A regular stacked chart](https://chandoo.org/wp/wp-content/uploads/2017/02/A-regular-stacked-chart.png)

Stacked Charts can get pretty hard to read because of multiple colors for each part. Highlighting the variables in the chart was the key to make it look simple to read. Here is how it was done!

Take a look at the logic

![Stacked Chart Logic](https://chandoo.org/wp/wp-content/uploads/2017/02/Stacked-Chart-Logic.png)

We needed a dummy calculation to support the highlighted section.

1.  Dummy = Sum (Values below the selected product)
2.  The dummy needed to be dynamic which changes as the user selected the product

![Dummy Calculation](https://chandoo.org/wp/wp-content/uploads/2017/02/Dummy-Calculation.gif)

Using these 2 calculations (Dummy & Highlighted section) a stacked chart was made

![Stacked Chart Output](https://chandoo.org/wp/wp-content/uploads/2017/02/Stacked-Chart-Output.png)

I wrote a pretty detailed post about how to **[highlight parts of a stacked chart](http://www.goodly.co.in/highlighting-parts-of-a-stacked-chart/)
**. Check it out if you want to get into more details.

**Screen 1 Calculations – How did I generate Comments ?**

![Comments](https://chandoo.org/wp/wp-content/uploads/2017/02/Comments.gif)

Notice the comments – Most words just stay the same and only a few words change. There were 2 comments with 2 different messages

1.  **Comment #1** : Shows the absolute change since 2011. Depending on the % change a text tag is added (for eg. moderate / considerable / drastic change etc..)
2.  **Comment #2 :** Compared to the previous year which year had the largest % change.This was a bit tricky and the reason why I chose to show it because we wanted to bring out interesting insights (drastic or alarming changes) from the 5 year trend. We needed the following ingredients for setting this up
    1.  Which year had the largest change (+/-) over the last year
    2.  How much change has happened (i.e. the exact %)
    3.  Tag (moderate / slight / no change etc..)

The first thing was to set up a Comments Reckoner table

![Change Reckoner](https://chandoo.org/wp/wp-content/uploads/2017/02/Change-Reckoner.png)

Nothing fancy about this, it is simple 2 columnar data with % change and an appropriate tag along with it. All this data was manually created! We will use this reckoner to lookup an appropriate tag for % change calculations

**Working for Comment #1**

![Comment 1 Calculations](https://chandoo.org/wp/wp-content/uploads/2017/02/Comment-1-Calculations.gif)

The calculations are pretty straight forward

1.  We calculating the absolute % change since 2011
2.  Using that % change we are looking up for a relevant comment tag in the comment reckoner. Since we are working with a range (between 90% – 50% = drastic change) **[the lookup method used is approximate match](http://www.excelguru.ca/content.php?251-Approximate-Matches-With-VLOOKUP)
    **
3.  After calculating % change and tags for all the variables we needed to narrow it down to only the variable selected

![Comment 1 final](https://chandoo.org/wp/wp-content/uploads/2017/02/Comment-1-final.png)

Which was done using a simple [**Index-Match formula**](http://chandoo.org/wp/2010/11/09/2way-lookup-formulas/)
 to find the % change and tag for the relevant variable selected

**Working for Comment #2**

![Comment 2 Calculations](https://chandoo.org/wp/wp-content/uploads/2017/02/Comment-2-Calculations.gif)

Let’s take a look at each of the 4 parts

1.  Finds the change over last year for each variable
2.  Finds the position of the maximum change. This position number will help us find that in which year the change happened
3.  Calculates the % change that happened
4.  Adds a tag relevant (from the comment reckoner) to the % change

Using the above calculations, now we lookup for the relevant variable selected

![Comment 2 Final](https://chandoo.org/wp/wp-content/uploads/2017/02/Comment-2-Final.png)

Just like the previous one a simple Index formula for looking up the relevant % change, tag and year

Then I concatenated all these calculations to write comments and used the **[camera tool](http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/)** to create a linked picture and pasted them in the Dashboard

![Comments Concatenated](https://chandoo.org/wp/wp-content/uploads/2017/02/Comments-Concatenated.gif)

Phew!! that was some work.

If you have reached till here you might be interested in taking a look at an **[explainer video + resources that I have put together](http://www.goodly.co.in/bonus-content-dbcontest/)
** on this Dashboard

**Screen 1 – Overall Layout !**

![frontend backend](https://chandoo.org/wp/wp-content/uploads/2017/02/frontend-backend.png)

Since I had to show comparison between 2 companies therefore both the frond end and back end calculations were set up in 2 blocks – **Left side for 1st Company Selected and Right Side for 2nd Company Selected**

This also made it easier for anyone to see my workings and understand how things are formed!

> _**Quick Tip:** It is important to layout your calculations clearly! It not only becomes easier for you but also for anyone else to understand your model_

**Screen 2 – Overall Market**

![Screen 2 overall](https://chandoo.org/wp/wp-content/uploads/2017/02/Screen-2-overall.png)

Setting up this screen was not complex apart from conditional formatting. There were 3 major things

1.  5 Pivot Tables for each year sorted in descending order (that will enable ranking)
2.  Slicer for selecting any company and pivot table to store the value
3.  Slicer for selecting any variable and pivot table to store the value. Note that the variable slicer was connected to all 5 pivot tables

**Screen 2 – The tricky part, Conditional formatting**

I applied 2 layers conditional formatting

1.  **Layer #1** The selected company should be highlight for all the years
2.  **Layer #2** Icon sets should display the change from last year has been positive, negative or no change

**Layer #1 – Conditional formatting for highlighting the Company**

![Conditional Formatting Layer 1](https://chandoo.org/wp/wp-content/uploads/2017/02/Conditional-Formatting-Layer-1.gif)

1.  I wrote a simple formula to equate the company selected in the slicer with the companies displayed
2.  Where ever the result was true the format set was blue color

**Layer #2 – Icons that display change from last year**

Since icon sets do not accept relative cell referencing so I had to play a trick. I first wrote a formula to find out last year’s value for the selected company and selected variable. This was the formula is copied down in 4 cells and pasted in each column containing values

A key thing to note is that the below formula also accounts for 2 additional factors

1.  **If the user selects Profit** – Green icon should be displayed when the profit is up from the last year and a red icon when the profit has dipped from last year
2.  **If the user selects any Cost Variable** – Green icons when the cost has gone down from the last year and red icons when the cost has increased from last year

![Conditional Formatting Layer 2 formula](https://chandoo.org/wp/wp-content/uploads/2017/02/Conditional-Formatting-Layer-2-formula.png)

Then I applied **[conditional formatting (icon sets)](http://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
** for each value separately and referred to each cell containing the above formula

![Conditional Formatting Layer 2](https://chandoo.org/wp/wp-content/uploads/2017/02/Conditional-Formatting-Layer-2.gif)

and that completed all the number crunching and setting up of the Dashboard! The next big thing was to format this beast and make it a beauty!

Wow..!! If you are still hanging around I would love to share with you an [**explainer Video + Resources that I have put together**](http://www.goodly.co.in/bonus-content-dbcontest/)
 for you. I think you’ll love it

**How did I format the Dashboard ?**
------------------------------------

**Screen 1 – Headline Bar**

![Headline Bar](https://chandoo.org/wp/wp-content/uploads/2017/02/Headline-Bar.png)

1.  I set up the headline bar in dark grey because I din’t want to overwhelm the dashboard with too many colors.
2.  I used Red for highlighting the chart and Blue for Company slicer
3.  Also in the past I have read many [reports from Bain & Co](http://www.bain.com/bainweb/PDFs/cms/Public/BB_Publishing_in_the_digital_era.pdf)
     and they use red with grey/black, so I knew that color combo looks pretty cool !

**Screen 1 – Slicers for Companies**

![Slicers Formating](https://chandoo.org/wp/wp-content/uploads/2017/02/Slicers-Formating.png)

1.  I spent a lot of time **[customising the look and feel of the slicers](http://www.goodly.co.in/slicer-formatting-tricks/)
    **
2.  Mostly removing the non essential elements and make them look seamless as if they are a part of a web based report
3.  If you want this same format
    1.  Just copy and paste this slicer in your workbook
    2.  You’ll find a new style created in slicer options
    3.  Now apply the style on your existing slicer and delete this slicer! Done

\[Related\] – **[Learn to work with slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
**

**Screen 1 – Formatting Stacked Chart**

![Formatting Stacked Chart](https://chandoo.org/wp/wp-content/uploads/2017/02/Formatting-Stacked-Chart.png)

1.  I wanted the charts to look simple and clean
2.  I included the vertical axis and not the data labels. Instead I highlighted the values (via conditional formatting) below
3.  The years (horizontal axis) was put on the top so that it becomes common label for the chart and the values below

**Screen 1 – Formatting Cost Variable Slicers, Values and Comments**

![Values and Comments formatting](https://chandoo.org/wp/wp-content/uploads/2017/02/Values-and-Comments-formatting.png)

1.  **Note a few things about Slicers**
    1.  Just to make sure that slicers look like clickable and yet NOT look like buttons I gave a little stick at left side in red. It was a trial and error exercise but it did the trick
    2.  Just to be more explicit I even wrote it on the top _“Pick a Cost”_
    3.  Arranged the slicers accurately so that they look seamless and appear as spreadsheet values
2.  **Formatting Values**
    1.  I applied 2 layers of conditional formatting
        *   Color the values in red for the cost variable selected
        *   If the total variable cost is select then apply bold formatting on Power, Other, Variable Cost and Freight & F
    2.  Other than that there was a slim border between each row
3.  **Formatting Comments** – There no major formatting done here. These are just linked pictures

**Screen 1 – Overall Formatting** – I did some overall formatting to tighten & secure the dashboard and make it look compact

1.  I protected the sheet (with no passwords)
2.  All objects (lines, charts, boxes / shapes) were locked
3.  The slicers were left unlocked, else clicking wouldn’t have happened
4.  The sheet name tab was removed
5.  The headings (column and row number) were hidden
6.  The formula bar was removed
7.  The extra rows and columns were hidden

\[Related\] **[Hiding Options in Excel](http://www.goodly.co.in/hiding-options-in-excel/)
**

**Screen 2 – Headline Bar**

![Headline Bar Screen 2](https://chandoo.org/wp/wp-content/uploads/2017/02/Headline-Bar-Screen-2.png)

1.  The slicers on screen 2 were exactly the same as screen 1.
2.  The 2 buttons interchanged appearances when clicked, which made it look like dynamic but technically it was just moving from one sheet to another

**Screen 2 – Slicers Formatting**

![Slicers Formating screen 2](https://chandoo.org/wp/wp-content/uploads/2017/02/Slicers-Formating-screen-2.png)

1.  Formatting of both slicers were consistent
    1.  Red for cost variables
    2.  And  Blue for Companies
2.  A label was put up on the top, just to make things more explicit

**Screen 2 – Formatting Years, Data and Legends**

![Years Data and Legends Formatting](https://chandoo.org/wp/wp-content/uploads/2017/02/Years-Data-and-Legends-Formatting.png)

1.  **Formatting Years**
    1.  They were slightly in a bigger font than the data
    2.  And I placed slim separators in between
2.  **Formatting Data/Values**
    1.  Most of this formatting came from Conditional formatting as explained above
    2.  I also left a column with a very narrow width in between each year as a separator
3.  **Formatting Legends**
    1.  The legends were pasted as a picture
    2.  The legends also depicted 2 inferences (for cost and profit separately)

**Screen 2 – Overall Formatting**

1.  I carried most of the formatting practices from screen 1
2.  Additionally I also made sure that the total width of Screen 1 is equal to Screen 2

**How much time did I spend in creating this Dashboard ?**
----------------------------------------------------------

1.  Dashboard Pre-Work – Planning, Rough work and Mock Dashboard **(1.5 Hour)**
2.  Number Crunching and Analysis – **(2 Hours)**
3.  Formatting and Creating the look and feel – **(2.5 hours)**

I gave 3 sittings over 3 days to finish this task 🙂 .  You can also watch a **[quick video explaining the entire dashboard](http://www.goodly.co.in/bonus-content-dbcontest/)
**

**Mistakes that could have been avoided**
-----------------------------------------

I found 2 mistakes that could have avoided.

1.  The variables were static (hard coded) and they did not link back to the data. That could have been a problem or could have required additional work when
    1.  The variables change completely
    2.  More variable were added. In those cases the Dashboard was not capable of adapting to the changes automatically
    3.  It could have been solved by a formula (to extract uniques) or by power query. **[Thanks Abhay](http://chandoo.org/wp/2016/08/30/visualizing-financial-metrics/)
        ** for pointing that out 🙂
2.  The Overall Market Sheet could have had some additional analysis on the overall trend or may be an infographic. The space utilisation was not optimum

With all that work put it, I finally closed the Dashboard and sent it to Chandoo! and it clicked 🙂

I have put together an **[Explainer Video + Some additional resources](http://www.goodly.co.in/bonus-content-dbcontest/)
** on this Dashboard. I sure you’ll love them

**Closing ..!**
---------------

If you have any questions, please put them down in the comment below. I’ll be glad to answer as many as I can.

**About the Author :** Chandeep comes from the Investment Banking background and has been an avid excel user since last 6.5 years. He now runs an excel/powerpoint blog (www.goodly.co.in) and  does training workshops for companies in India on Excel, PowerPoint Presentations, BI Dashboards, Financial Modelling.

Added by Chandoo: Thank you Chandeep
------------------------------------

Thank you Chandeep for such an insightful, detailed and awesome write up. I really enjoyed learning from this. I am sorry I took too much time to schedule this.

If you too liked this post and learned something from it, _please say thanks to Chandeep_.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [23 Comments](https://chandoo.org/wp/financial-dashboard-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/financial-dashboard-tutorial/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousRoad Trip Planner Template \[Excel Downloads\]](https://chandoo.org/wp/road-trip-planner-template-excel-downloads/)

[NextFind them and Extract them – VBA MacroNext](https://chandoo.org/wp/find-and-extract-results/)

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
    
    [Reply](https://chandoo.org/wp/financial-dashboard-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/financial-dashboard-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/financial-dashboard-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ