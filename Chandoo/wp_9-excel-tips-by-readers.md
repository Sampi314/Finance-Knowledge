# 9 Excel Tips & Downloads Submitted by Our Readers [Reader Awesomeness Week] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/9-excel-tips-by-readers

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

9 Excel Tips & Downloads Submitted by Our Readers \[Reader Awesomeness Week\]
=============================================================================

*   Last updated on August 10, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Reader Awesomeness Week - Excel Tips & Downloads submitted by our readers](https://img.chandoo.org/raw/reader-awesomeness-week.png)

**Last week I [announced Reader Awesomeness Week](http://chandoo.org/wp/2010/08/02/reader-awesomeness-week/)
 to celebrate the passion, attitude and knowledge of our little community here.** I got 9 interesting and beautiful entries from our readers. In this post you can see 9 tips & downloads submitted by our readers. Click on the below links to jump any one or read all of them.

1.  [VLOOKUP to the left – using OFFSET and MATCH](https://chandoo.org/wp/9-excel-tips-by-readers/#vlookup-left)
     by _Michael Pennington_
2.  [FREE Ebook on Making Better Charts](https://chandoo.org/wp/9-excel-tips-by-readers/#charting-ebook)
     by _Vivek Singh_
3.  [Remove Blanks using this Macro](https://chandoo.org/wp/9-excel-tips-by-readers/#remove-blanks)
     by _Arti A_
4.  [Dynamic Charts using OFFSET Formula](https://chandoo.org/wp/9-excel-tips-by-readers/#dynamic-charts)
     by _Jon_
5.  [Format Filter Alternative for Excel 2003](https://chandoo.org/wp/9-excel-tips-by-readers/#format-filter)
     by _Lucasini_
6.  [FREE Project Plan, Dashboard Template](https://chandoo.org/wp/9-excel-tips-by-readers/#project-plan)
     by _Cyril ZEKSER_
7.  [Show Dynamic Messages based on Select Cells (Macro)](https://chandoo.org/wp/9-excel-tips-by-readers/#dynamic-messages)
     by _Tom_
8.  [Create Maps with Excel & Google Earth](https://chandoo.org/wp/9-excel-tips-by-readers/#create-maps)
     by _Drew Kesler_
9.  [PowerPoint Dashboards](https://chandoo.org/wp/9-excel-tips-by-readers/#ppt-dashboards)
     by _Erin_

**_plus, these 3 were already shared with you last week._**

1.  [Immigrants in Denmark – Excel Info-graphic](http://chandoo.org/wp/2010/08/03/immigrants-in-denmark/)
     by _Faheem_
2.  [Travel Site Dashboard – Review & Download](http://chandoo.org/wp/2010/08/04/travel-site-dashboard-review/)
     by _Francis_
3.  [12 Rules for Making Better Spreadsheets](http://chandoo.org/wp/2010/08/05/better-spreadsheets-12-rules/)
     by _Larry_

VLOOKUP to the left – using OFFSET and MATCH
--------------------------------------------

by _Michael Pennington_

It is really just a tip that I picked up somewhere in the last few years and I use it all the time to do Vlookups that can go to the left instead of just the right. Simply an offset and match combined for the purposes of replicating a left looking vlookup. I used a nice add in to create sample data and linked to the add in within my workbook. I find myself using this instead of always reworking data sets that I receive. Feel free to use the workbook however you want, if you want to present it in another fashion or know a better way, I look forward to your input. Thanks for running such a brilliant blog.

**Download Links:**

[reverse-vlookup.xls](http://cid-a0e1b3262186c132.office.live.com/view.aspx/Public/Reverse%20Vlookup.xlsx)

**Related Info:**

[Introduction to VLOOKUP, OFFSET and MATCH formulas](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)

FREE Ebook on Making Better Charts
----------------------------------

by _Vivek Singh_ \[[URL](http://www.allaboutpresentations.com/ "Vivek Singh")\
\]

Creating charts in excel is a skill but presenting it is also a skill. A lot of hard work that goes into making a chart will get wasted if your chart looks bad or confuses others. I have written a small e-book which can help a lot of people make the most of charts they have prepared. It contains 14 tips explained in simple language.

**Download Links:**

[making-better-charts-14-tips-ebook](http://www.slideshare.net/singhvivek6/14-tips-to-present-awesome-charts-2071447/)
 | [Mirror Download Link](http://www.allaboutpresentations.com/2009/09/recap-of-14-tips-to-present-awesome.html)

**Related Info:**

[Select right chart based on your data](http://chandoo.org/wp/2010/04/19/chart-selection-process/)
 | [Chandoo.org Charting Pages](http://chandoo.org/wp/category/visualization/)

Remove Blanks using this Macro
------------------------------

by _Arti A_

If you are into data crunching the way I am, you are probably running queries on databases and copy-pasting the results back into your spreadsheet. The annoying part is when there are blank spaces in a table, making it difficult to use the ctrl+up/down shortcuts to get around the table or ctrl+shift+up/down to make selections. Here’s a simple macro to take care of it. All you have to do is this, 1) Insert a new module in your Personal.xlsb file and copy-paste the macro below 2) Select several rows/columns of data containing a few blank cells 3) On your keyboard, press the following key combination – “Ctrl+Shift+E’. The blank cells in your selection should now contain zeros. Note: You can replace the blank cells with any character you want, for example a “N/A” or “-” for text-heavy tables.

`Sub ReplaceZeros()   ' ReplaceZeros Macro   ' Keyboard Shortcut: Ctrl+Shift+E   With Selection.Cells   .SpecialCells(xlCellTypeBlanks) = 0   End With   End Sub`

**Related Info:**

[Delete Blank Rows in Excel](http://chandoo.org/wp/2010/01/26/delete-blank-rows-excel/)

Dynamic Charts using OFFSET Formula
-----------------------------------

by _Jon_

We have a large group of people that we collate information around and run numerous graphs on. It was once “death by graphs” until=OFFSET(Data!C5,VLOOKUP($B$2,$A$63:$B$67,2,FALSE),’Graph Data’!$A$1)Where the vlookup looks at a table that gives exact number of rows to move down based on the selection. Result, graph is now interactive and the big cheese’s only see what they want.

**Related Info:**

[Using OFFSET formula to make Dynamic Chart Ranges](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/)

Format Filter Alternative for Excel 2003
----------------------------------------

by _Lucasini_ \[[URL](http://lucasiniworldcup2010.webs.com/index.htm "Lucasini")\
\]

Format Filter Technique without VBA – All Excel versions!!!!

Who said that you can’t color filter in Excel 2003 without using VBA???? In fact, you can do more than that; you can filter by font format, number format, border type, fill color, and so on with the Search and Replace Format Filter Technique. This is a fairly simple operation that can save you hours of work.  
How it works? –Simple, just make a copy of the column that you want to format filter and paste it as an additional column in your data. Then, select the new column and do a Search and Replace with the Format Options activated. Type the text you want to search (special search characters allowed “?” “\*”), select the format of the cell you want to search (all cell format attributes are supported) and replace the contents with some text that Excel can actually filter with the autofilter feature. Next, select autofilter and filter by that column using the replaced text.

Wow!!! A Format Filter Technique without VBA for ALL Excel versions with all cell format attributes available.Using this approach you have all the cell format parameters to play with, border styles, font styles, number styles, cell colors, even alignment and protection options.  
Hope this helps you, greetings from Panamá.  
SE HABLA ESPAÑOL!!! Y EXCEL TAMBIÉN!!!!

**Download Links:**

[word doc with screenshots of this technique](http://lucasiniworldcup2010.webs.com/Format%20Filter%20Technique%20without%20VBA.doc)

**Related Info:**

[Change Cell Formats quickly with Find Replace](http://chandoo.org/wp/2008/04/04/change-cell-formats-with-find-replace-in-excel/)

FREE Project Plan, Dashboard Template
-------------------------------------

by _Cyril ZEKSER_

Here is my submission. This is a Gantt Tasks planner, including tracking of days spent on tasks.

I use it on my everyday job, and I build it using a lot of your techniques as well as Fernando’s (for the gantt planning)… So many thanks for this (end of compliments)It comes with a Dashboard, a Tasks tab and a remaining tab. All others tabs are either calculations or not really used. To use It you have to follow the steps:  
**Initialization and planning :**  
1\. Fill the tab TASKS.(lines 1 to 23) – Enter the description and the targets (lots, versions…) in the orange cells – Enter the milestones and the versions.  
2\. Enter the tasks. (lines below 25). – fill field from column A to O. – fill header manually on line 25 from column P (be sure to match start date of project in I3) – Only DEV tasks are tracked in the burn down chart – add a number in column A only if you wish to follow the task in the dashboard.  
3\. Fill the theoretical production capacity of the team in tab CALCULOUS, line 10, from column C, in days. This is the reference of the burn down

**DURING PROJECT :**  
4\. In the dashboard, enter the reference date (mostly CTRL+; )  
5\. Enter the days spent on each task in the appropriate column of tab TASKS  
6\. If a task is done before the normal day, or need more days, adjust remaining of this task on Tab REMAININGS  
7\. Follow the dashboard.If you need any information, don’t hesitate to drop me a line.

PS : works only in 2007+ macros. Lots of conditional formats.

**Download Links:**

[project-plan-and-dashboard.xlsm](http://www.zekser.net/pub/chandoo/DEV_Tasks_Planner.xlsm)

**Related Info:**

[FREE Gantt Chart Template](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
 | [Excel Project Management – Information & Resources](http://chandoo.org/wp/project-management/)

Show Dynamic Messages based on Select Cells (Macro)
---------------------------------------------------

by _Tom_

My tip is a “tip”-sheet. Based on the selected cell some help is offered to the user. In a way a more flexible way than the classic ‘input message’ in the data validation option of excel.

**Download Links:**

[show-message-based-on-cell.xls](http://cid-ad0cb788decc47cc.office.live.com/view.aspx/.Documents/MessageBasedonselectedcell.xls)

Create Maps with Excel & Google Earth
-------------------------------------

by _Drew Kesler_ \[[URL](http://www.totallyawesomemapping.com/ "Drew Kesler")\
\]

Excel has allowed me to create powerful maps which make my analysis much more visual and user-friendly for upper management. When I first began using Excel for mapping, I was skeptical, as I thought the value of a map was just a pushpin in a wall. But by creating some tools to convert spreadsheet data into Google Earth maps, I began to see how powerful this analysis can be.As you can see in my workbook, Excel allows me to categorize my locations by certain characteristics. In my workbook, I have categorized In-N-Out Burger locations by year-over-year sales. I can categorize these locations into different folders so that I can narrow my view to “only locations with a year-over-year increase between 0 and 10 percent.”I can also assign my locations to different color icons. In my workbook, I assigned the In-N-Out Burger locations with Red, Orange, Yellow, and Green, according to their year-over-year sales results. When looking at my map, it is simple to pick out the high performing locations vs. other sites.The last way I have used Excel in creating this visual analysis is to embed my data into the map. In Google Earth, when you click on a location, a bubble will appear. You can embed any data you like into this bubble. So, I can not only embed the address information, but I can also add location-specific phone numbers, hours, or any other data points I have, such as sales. You can see that I have embedded all this data into my map using Excel.

In building this map, I have used a few key functions in Excel:VLookup, Concatenating or Joining Cells, If-Then Statements

Thanks to a respected William H. Gates for transforming our world with Excel! Once the Excel Template Gizmo is complete, you can upload it at _TotallyAwesomeMapping.com_ to create your map.

**Download Links:**

[excel-map-creation-template](http://www.totallyawesomemapping.com/gizmo/In-N-Out-Gizmo.xls)
 | [upload map here](http://www.totallyawesomemapping.com/)

**Related Info:**

[Maps in Excel \[Clearly and Simply\]](http://www.clearlyandsimply.com/clearly_and_simply/2009/06/choropleth-maps-with-excel.html)

PowerPoint Dashboards
---------------------

by _Erin_

Here are two PPT presentations I’ve setup as shows so that when a user clicks on the files it opens them up in full screen format. The charts are somewhat old and are kind of lame, but I haven’t seen anything on your site re: this technique for dashboarding.

The less elaborate show I created from scratch, the more elaborate one I used a template from DDMat (I think) and just modified it with some additional animation, slides, etc.

**Download Links:**

[powerpoint-dashboard-1](http://dl.dropbox.com/u/3169677/Clinician%20Productivity%20Dashboard.pps)
 | [powerpoint-dashboard-2](http://dl.dropbox.com/u/3169677/Daily%20Dashboard%20for%20Air%20Card%20ROI.pps)

**Related Info:**

[FREE Excel Dashboard Templates, Resources and Examples](http://chandoo.org/wp/excel-dashboards/)

Thanks Everyone
---------------

Thank you each and everyone of you for making this a success. I have learned a great deal of excel and charting stuff over the last week and I am sure you too would have benefited some. Please drop a note of thank you if you have enjoyed any of these tips.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/9-excel-tips-by-readers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/9-excel-tips-by-readers/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [e-books](https://chandoo.org/wp/tag/e-books/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [maps](https://chandoo.org/wp/tag/maps/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [powerpoint](https://chandoo.org/wp/tag/powerpoint/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [reader awesomeness week](https://chandoo.org/wp/tag/reader-awesomeness-week/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousDownload Excel Wedding Planner Today](https://chandoo.org/wp/download-free-excel-wedding-planner-today/)

[NextWinner of Excel Expense Tracker Contest – RomeoGNext](https://chandoo.org/wp/winner-of-excel-expense-tracker-contest/)

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
    
    [Reply](https://chandoo.org/wp/9-excel-tips-by-readers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/9-excel-tips-by-readers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/9-excel-tips-by-readers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ