# Automating Repetitive Tasks in Excel

**Source:** https://chandoo.org/wp/automating-repetitive-tasks

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Automating Repetitive Tasks
===========================

*   Last updated on June 23, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

[https://chandoo.org/wp/wp-content/uploads/2011/06/Huis\_Excel\_Dancing\_Pendulums.mp4](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Dancing_Pendulums.mp4)

Podcast: [Play in new window](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Dancing_Pendulums.mp4 "Play in new window")
 | [Download](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Dancing_Pendulums.mp4 "Download")

Subscribe: [Apple Podcasts](https://itunes.apple.com/us/podcast/chandoo.org-podcast-become/id835954043?mt=2&ls=1#episodeGuid=http%3A%2F%2Fchandoo.org%2Fwp%2F%3Fp%3D3510 "Subscribe on Apple Podcasts")
 | [Spotify](https://open.spotify.com/show/1wr79nj0tmxFMqxzxnPnEY "Subscribe on Spotify")
 | [RSS](https://chandoo.org/wp/feed/podcast/ "Subscribe via RSS")

Three week ago I visited the Newton Excel Bach web site where I spotted the Dynamically Defined Dancing Pendulums [NewtonExcelBach](http://newtonexcelbach.wordpress.com/2011/05/25/dancing-pendulums-2/)
.

Having noticed that Doug had done a nice animation in Strand7 (a Finite Element Analysis program) [Strand7](http://www.strand7.com/)
, I thought “I can do that in Excel” and so I did.

This post will not go through the logic of constructing and animating the pendulums in Excel as I have described that over at [Excelhero.com](http://www.excelhero.com/blog/ "http://www.excelhero.com/blog/")
 and readers who are interested are encouraged to visit there and explore the techniques used.

During the Pendulum project I came across two sub-projects which I felt are worthy of a post here at **Chandoo.org** as they are a great demonstration of some basic VBA techniques as well as demonstrating the ability of VBA to quickly simplify repetitive tasks.

Sample files are attached for [Excel 97-2003](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Hero_Pendulum_Side_Projects_97.xls "Excel 97-03 Sample File")
 and [Excel 2007/10](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Hero_Pendulum_Side_Projects_07.xlsm "Excel 2007/10 Sample File")
 users to follow through the examples.

**PENDULUM SIDE PROJECTS**
--------------------------

The Pendulum project consists of 16 Pendulums. Each Pendulum requires 4 Named Formulas, meaning that the projects needs 64 Named Formulas for the 16 Pendulum, as well as adding 16 Series to the chart.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend1.gif "Pend1")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend1.gif)

[Huis\_Excel\_Dancing\_Pendulums](https://chandoo.org/wp/wp-content/uploads/2011/06/Huis_Excel_Dancing_Pendulums.mp4)

(The above animated GIF is a very poor representation of the smooth scrolling achieved in the Excel animation)

I thought it would be a great idea to see if these jobs could be automated and hopefully save some time during the process.

The result was 2 simple VBA routines which will be described below:

**NAMED FORMULAS**
------------------

Each Pendulum in the project was based around 4 Named Formulas

### **Named Formula for each Pendulum**

**p1Len** =’1′!$B$9                                                   The Length is stored on the worksheet.

**p1o** =OMax\*SIN(SQRT(g/p1Len)\*t)      Current angular position of Pendulum 1 at time t

**p1x** \=p1Len\*SIN(p1o)\*{0;1}                      Current orthogonal X position of Pendulum 1 at time t

**p1y** \=-p1Len\*COS(p1o)\*{0;1}                   Current orthogonal Y position of Pendulum 1 at time t

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Maths.png "Maths")](https://chandoo.org/wp/wp-content/uploads/2011/06/Maths.png)

The only difference between the formulas for Pendulum 1 and Pendulum 2 etc is the replacement of the names of p1 with p2 in the various Named Formulas and of the associated formulas.

On a worksheet **Named Formulas** a number of formulas were written which display the Named Formulas as required above. Then a small VBA routine was written which loads the Named Formulas.

### **How**

On the Named Formulas worksheet, I have added two columns of formulas for the various Named Formulas required.

For the Pendulum Length Named Formulas

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend1.png "Pend1")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend1.png)
  

For the Pendulum Angular Position Named Formulas

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend2.png "Pend2")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend2.png)
  

For the Pendulum X Position Named Formulas

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend3.png "Pend3")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend3.png)
  

For the Pendulum Y Position Named Formulas

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend4.png "Pend4")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend4.png)

  

When the formula above are copied down they adjust for the various pendulums numbered 1 to 16 based on the row numbers.

I then setup a VBA routine, **Load\_Named\_Ranges**, shown below which loads the Named Formulas.

### **To Use**

Select some or all of the required Named Formulas from the Name Column. That is the code will only load the **Selected** Named Formulas, allowing the user to load 1 or 2 Named Formulas, for testing purposes, or all the Named Formulas if you choose.

Then Execute the **Load\_Named\_Ranges** subroutine either using the Big Red Button or directly within the VBA Editor.

The following will load Named Formulas **p3Len** to **p7Len**.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend4a.png "Pend4a")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend4a.png)

The **Load\_Named\_Ranges** subroutine is shown below:

_Sub Load\_Named\_Ranges()_

_Dim c As Range_

_For Each c In Selection_

_ActiveWorkbook.Names.Add Name:=c.Text, RefersTo:=c.Offset(, 1).Text_

_Next_

_End Sub_

**What does the code do?**

The code:

1\. Defines the start and name of the subroutine,

_Sub Load\_Named\_Ranges()_

2\. Defines a variable c as a Range object,

_Dim c As Range_

3\. It then loops through each cell in the selection and assigns it to the variable ‘c’;

_For Each c In Selection_

4\. It then adds a new Named Formula,extracting the Name from the Text Value of ‘c’ and extracts the formula from the cell directly to the right of cell ‘c’;

_ActiveWorkbook.Names.Add Name:=c.Text, RefersTo:=c.Offset(, 1).Text_

The Name and Formula (RefersTo) both use the Text of the cell, which is what is displayed.

5\. It then loops through each cell in the selection until it has done them all;

_Next_

6\. Defines the end of the subroutine;

_End Sub_

### **Lets Test It**

To test the subroutine we will first delete all the Named Formulas beginning with “p”

Goto the Formula Ribbon Bar and select Name Manager

Select all the Named Formulas that begin with “P” and press the delete button

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Name-Mgr.png "Name Mgr")](https://chandoo.org/wp/wp-content/uploads/2011/06/Name-Mgr.png)

Accept any warnings

Try and Run the Pendulum’s

Nothing happens as there are no formulas

**Ensure the Pendulum are turned off, as the code is still running behind the scenes.**

Now Goto the Named Formulas Page

Select all the Named Formula Names in Name Column; B3:B66

Click the Load Named Formulas, button

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Load-Named-Ranges.png "Load Named Ranges")](https://chandoo.org/wp/wp-content/uploads/2011/06/Load-Named-Ranges.png)

Go back to Page **1** and try and run the Pendulums now.

**ADD CHART SERIES**
--------------------

The second sub-project was the addition of 16 Chart series to the Chart, 1 for each Pendulum.

Using the logic of the Named Formulas VBA code above, the 16 Chart Series Names, X Values and Y values were developed using formulas on the **Add Cht Series** worksheet and then loading into a chart using a simple VBA routine.

The **Add\_Cht\_Series** subroutine is in the **Add Cht Series** sheet object in the VBA editor.

**How**
-------

On the **Add Cht Series** worksheet, I have added three columns of formulas for the various Named Formulas required.

For the Pendulum Name, X Range and Y Range.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend5.png "Pend5")](https://chandoo.org/wp/wp-content/uploads/2011/06/Pend5.png)

When these formulas are copied down they adjust for the various pendulums numbered 1 to 16.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/B1112.png "B1112")](https://chandoo.org/wp/wp-content/uploads/2011/06/B1112.png)

I have then setup a VBA routine, **Add\_Chart\_Series**, shown below which loads the Named Formulas.

To use Select some or all of the required Chart Series from the Pendulum Name column.

Then Execute the **Add\_Chart\_Series** subroutine using the big red button.

The **Add\_Chart\_Series** subroutine is shown below:

_Sub Add\_Cht\_Series()_

_Dim sNumb As Integer_

_Dim c As Range_

_Worksheets(“1”).ChartObjects(“Chart 5”).Activate_

_For Each c In Worksheets(“Add Cht Series”).Range(“B19:b20”)_

_sNumb = ActiveChart.SeriesCollection.Count + 1_

_ActiveChart.SeriesCollection.NewSeries_

_ActiveChart.SeriesCollection(sNumb).Name = c.Text_

_ActiveChart.SeriesCollection(sNumb).XValues = c.Offset(, 1).Text_

_ActiveChart.SeriesCollection(sNumb).Values = c.Offset(, 2).Text_

_Next_

_End Sub_

**What does the code do?**

The code:

1\. Defines the start and name of the subroutine,

_Sub Add\_Cht\_Series()_

2\. Defines a variable sNumb as an integer,  and a variable c as a Range object

_Dim sNumb As Integer_

_Dim c As Range_

3\. It then activates the Chart containing the pendulum

_Worksheets(“1”).ChartObjects(“Chart 5”).Activate_

4\. It then loops through each cell in the Range defined by the Range, in this case _B19:B20_ and assigns it to the variable ‘c’;  You can adjust the Range to suit.

_For Each c In Worksheets(“Add Cht Series”).Range(“B19:B20”)_

5\. It then counts how many existing series are in the chart and sets the next Series Number sNumb to that value + 1.

_sNumb = ActiveChart.SeriesCollection.Count + 1_

6\. The next 4 lines add a new series to the chart and setup the new series Name, X Value and Y Values. The Name, X Value and Y Values are retrieved from the Text of the cell c and the adjacent two cells using a Range Offset modifier

_ActiveChart.SeriesCollection.NewSeries_

_ActiveChart.SeriesCollection(sNumb).Name = c.Text_

_ActiveChart.SeriesCollection(sNumb).XValues = c.Offset(, 1).Text_

_ActiveChart.SeriesCollection(sNumb).Values = c.Offset(, 2).Text_

7\. It then loops through each cell in the selection until it has done them all;

_Next_

8\. Define the end of the subroutine;

_End Sub_

**Lets Test It**

To test the subroutine we will first delete a few of the Chart Series

Select the Chart

Select two Pendulums noting the series Number of the Bobs eg: 9 & **10**

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/DeleteBob.png "DeleteBob")](https://chandoo.org/wp/wp-content/uploads/2011/06/DeleteBob.png)

Goto the Add Chart Series Worksheet

Note the Range Corresponding to the 2 missing Pendulum B11:B12

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/B1112.png "B1112")](https://chandoo.org/wp/wp-content/uploads/2011/06/B1112.png)

Goto the VBA Editor

Adjust the Line

_For Each c In Worksheets(“Add Cht Series”).Range(“B11:B12”)_

_[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Code.png "Code")](https://chandoo.org/wp/wp-content/uploads/2011/06/Code.png)
  
_

With your cursor in the Subroutine press F5 once only

Go back to Page 1 and you should now have 2 New Pendulum

Run the Pendulums now.

You will have to manually set the shape of the Bobs to a Circle and size 15 and re-arrange the order of the series to ensure they are in order, but you can practice that manually.

**SUMMARY**
-----------

The post has shown how using some very simple VBA and a bit of lateral thinking to put together some simple tools to simplify 2 common and repetitive tasks.

In the Named Formulas case, the code took less than 2 minutes for me to write and then another 5 minutes to do the formulas for the Named Formulas. I didn’t try but I am sure it would have taken a good 20+ minutes to enter 64 Named Formulas.

Writing this post took much longer than doing the whole Pendulum Project.

Two examples during my working career, where VBA code has been used to save massive amounts of time and money:

In the first case I wrote some code to combine data from several hundred workbooks with varying numbers of sheets up to 30 and differing quantities of data on each sheet, a task that could have taken weeks manually with the included opportunity for errors to be introduced, into a subroutine which took 30 minutes to run and gave a printout of the results including what files, sheets and rows of data were included in the import.

In a second case a Number of Workbooks, a Word template and some VBA code was used to replace a person whose sole job was to manage that data. This job saved the company $50k+ per annum and the task was given to a clerical person who could now do the task in their spare time.

**LINKS**
---------

Huis Excel Hero Pendulum: [http://www.excelhero.com/blog/](http://www.excelhero.com/blog/ "http://www.excelhero.com/blog/")

Pendulum Physics: [http://hyperphysics.phy-astr.gsu.edu/hbase/pend.html](http://hyperphysics.phy-astr.gsu.edu/hbase/pend.html)

Newton Excel Bach: [http://newtonexcelbach.wordpress.com/2011/05/25/dancing-pendulums-2/](http://newtonexcelbach.wordpress.com/2011/05/25/dancing-pendulums-2/)

**What could your simplify by using automation within** ****Excel**** **?**
---------------------------------------------------------------------------

What could you simplify or speedup using Excel automation?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [19 Comments](https://chandoo.org/wp/automating-repetitive-tasks/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/automating-repetitive-tasks/#respond)
    
*   Tagged under [Automation](https://chandoo.org/wp/tag/automation/)
    , [chart](https://chandoo.org/wp/tag/chart/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousWe Want Your Ideas](https://chandoo.org/wp/we-want-your-ideas/)

[NextExcel Links – Updates on Singapore Workshop EditionNext](https://chandoo.org/wp/excel-links-singapore-workshop-edition/)

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
    
    [Reply](https://chandoo.org/wp/automating-repetitive-tasks/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/automating-repetitive-tasks/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/automating-repetitive-tasks/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ