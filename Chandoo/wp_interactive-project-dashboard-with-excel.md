# How to create a fully interactive Project Dashboard with Excel - Tutorial + FREE Download

**Source:** https://chandoo.org/wp/interactive-project-dashboard-with-excel

---

How to create a fully interactive Project Dashboard with Excel – Tutorial
=========================================================================

In this article & video series, learn how to create a **fully interactive Project Dashboard with Excel,** as demonstrated on the right. 

You will learn:

*   [Gantt charts for project planning](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#part1)
    
*   [Progress charts for status visualization](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#part2)
    
*   [Preparing final dashboard](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#part3)
    

![project management dashboard - finalized](https://chandoo.org/wp/wp-content/uploads/elementor/thumbs/project-management-dashboard-finalized-p8ej08ee7ywlmogq7wd302xeocv0az1zqmxe2k48hs.png "project management dashboard – finalized")

Part 1 - Project Gantt Chart
----------------------------

**Gantt chart** is a classic way to visualize a project’s plan & current status. That is why it forms the corner stone of any Project Management Dashboard. 

In Part 1 of this tutorial, let’s create an interactive, multi-level gantt chart using Excel. Here is a demo of what we shall create.

![gif - gantt chart demo](https://chandoo.org/wp/wp-content/uploads/2021/05/gif-gantt-chart-demo.gif)

### Resources for the Gantt Chart

### Excel files for practice

Use the below files to practice the concepts.

*   [Blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
    
*   [Completed Gantt Chart file](https://chandoo.org/wp/wp-content/uploads/2021/05/step-1-Gantt-Chart.xlsx)
    

### Gantt Chart - Video Tutorial

I made a fun & detailed video on how to create this Gantt chart with Excel. Watch it below or on [my YouTube channel](https://youtu.be/FXnyKU6xZeI)
.

### Getting the data

Any project is a combination of people & tasks. So in order to create a project plan gantt chart, you need both people & project activity data. Here is the data for our **Project Mega Something.** 

[Download the blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
.

Project Plan Data - Preview

![data - activities](https://chandoo.org/wp/wp-content/uploads/2021/05/data-activities.png)

Activities Table

![data - people](https://chandoo.org/wp/wp-content/uploads/2021/05/data-people.png)

People Table

### Set relationship between tables

Once we have the data ready, connect people & activity tables. You can create a relationship from Data ribbon > Relationships.

We want to connect Activities Owner column with People Person column.

![table relationships - project gantt chart](https://chandoo.org/wp/wp-content/uploads/2021/05/table-relationships.png)

Tip

No need to use X or VLOOKUPs anymore, you can connect tables on a column with Excel.

**[Learn more about Table Relationships in Excel](https://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
.**

### Calculations Worksheet

As our tables are related, we can now calculate all the _**necessary numbers**_ needed for our gantt chart.

In a new worksheet, 

*   Insert a pivot table (Excel will create the pivot from your table relationship data model)
*   Add Category & activity to row label area
*   Add start date and end date to values area
*   Set start date “summarize values by” to Min
*   For end date, set it to Max
*   Set up pivot table in outline format and add sub-totals on top.
*   Remove any grand totals.

Your final pivot table should be like below.

![pivot table to support gantt chart calculations](https://chandoo.org/wp/wp-content/uploads/2021/05/pivot-table-to-support-gantt-chart-calculations.png)

**Specify Gantt Start date**

In a blank cell in this new worksheet, define starting date for our gantt chart visual. You can use a formula like =TODAY()-14 or something else for this.

![gantt start date](https://chandoo.org/wp/wp-content/uploads/2021/05/gantt-start-date.png)

Name this start date cell as _**start.date**_

### Gantt Chart Worksheet

Add a new worksheet and name it Gantt Chart.

In this sheet, set up your gantt chart grid. We will use **67 columns** in this fashion.

![gantt chart set up - explanation](https://chandoo.org/wp/wp-content/uploads/2021/05/gantt-chart-set-up-exaplanation.png)

1.  Category name
2.  Activity
3.  Person assigned to the task
4.  Start
5.  End
6.  % done 
7.  % done

*   8 to 67 – Dates (narrow columns)

Load up values by either linking Pivot Table values a references or using lookup functions.

Tip

You can use XLOOKUP function to get the person & % done values.

**[All about XLOOKUP function](https://chandoo.org/wp/xlookup-examples/)
.**

### Gantt Chart Formulas

We need to set up a formula in our gantt chart grid to show TRUE when a date in the _**top row**_ is between **start** and **end** dates.

You can use AND formula for this. Fill this formula for the entire range.

_**In my spreadsheet I had 105 rows x 60 columns.**_

![grid formula for checking activity dates](https://chandoo.org/wp/wp-content/uploads/2021/05/grid-formula-for-checking-activity-dates.png)

				
					`=AND($F7<=J$3,$G7>=J$3)`
				
			

### Conditional Formatting Rules

Our gantt chart is nearly ready. We need to add two conditional formatting rules to highlight the project dates & current date.

*   Rule #1 : Highlight all TRUE values in the gantt grid
*   Rule #2 : Highlight the column that corresponds to TODAY()

Examine the rules from below screenshot.

![conditional formatting rules](https://chandoo.org/wp/wp-content/uploads/2021/05/conditional-formatting-rules.png)

Finally select the AND formula range and apply custom number format of ;;;

Tip

You can use hide values in a range of cells by applying the custom format code ;;;

**[How to hide values with number formats](https://chandoo.org/wp/hide-cell/)
.**

At this stage, your gantt chart should look like below:

![gantt-chart-after-addin-cf-rules](https://chandoo.org/wp/wp-content/uploads/2021/05/gantt-chart-after-addin-cf-rules.png)

**To add % done data bars:**

*   Select % done column and add data bars.
*   Set the bar rule to **show bar only**
*   In the 7th column (which has % done value duplicated), apply a cell icon of ![✔](https://s.w.org/images/core/emoji/13.0.1/svg/2714.svg) when the % done is 100% and no cell icon for rest.
*   Hide the contents of this column with custom code ;;;

Tip

Learn a few [more tricks about conditional formatting here](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/)
.

### Team selection slicer feature

Go back to the calculations sheet and add a **team slicer** on your pivot table.

Cut and move this slicer to the gantt chart page.

Your gantt chart is now interactive!!!

Tip

Excel slicers offer a great deal of interactivity in your reports. If you have not used them before, I suggest learning a bit about them. Use this handy guide.

[Excel slicers – complete guide](https://chandoo.org/wp/introduction-to-slicers/)
.

### The final gantt chart...

Here is the final gantt chart at this stage.

![gif - gantt chart demo](https://chandoo.org/wp/wp-content/uploads/2021/05/gif-gantt-chart-demo.gif)

### Excel files for downloading

Use the below files to practice the concepts.

*   [Blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
    
*   [Completed Gantt Chart file](https://chandoo.org/wp/wp-content/uploads/2021/05/step-1-Gantt-Chart.xlsx)
    

### More Gantt Charts for you...

*   [Gantt Chart with Drill-down feature](https://chandoo.org/wp/drill-down-gantt-chart-template/)
    
*   [Gantt Box Chart - for showing uncertainty in the project](https://chandoo.org/wp/gantt-box-chart-tutorial-template/)
    
*   [Gantt Charts + Other useful PM Templates by Chandoo](https://chandoo.org/pmt/pmt-index-1.html)
    

Part 2 - Beautiful Progress Charts
----------------------------------

In Part 2 of this tutorial, we will build beautiful project progress charts with Excel. 

![Project Management - Traffic Light - Demo](https://chandoo.org/wp/wp-content/uploads/2021/05/pm-traffic-light-demo-2.gif)There are 3 common ways to visualize a project progress. 

*   Traffic lights ![🚦](https://s.w.org/images/core/emoji/13.0.1/svg/1f6a6.svg)
*   Thermometer ![🌡](https://s.w.org/images/core/emoji/13.0.1/svg/1f321.svg)
*   Gauges ![🧭](https://s.w.org/images/core/emoji/13.0.1/svg/1f9ed.svg)

In this section, I will explain how to make a traffic light chart with Excel, as demoed on the right. In the video tutorial, you can learn how to make all 3 charts.

### Resources for Project Progress Charts

### Excel files for practice

Use the below files to practice the concepts.

*   [Blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
    
*   [Completed Progress Charts File](https://chandoo.org/wp/wp-content/uploads/2021/05/step-2-Progress-Charts.xlsx)
    

### Video Tutorial - Project Progress Charts

I made a video explaining how to make all three project progress charts. Watch it below or on **[my YouTube channel.](https://youtu.be/C0F_VKlTX1c)
**

### Project Traffic Light - Instructions

This will be the shortest part of the tutorial. Imagine you have the project progress value in the cell L3.

Use Conditional formatting on the cell to fill Red color if the value is under 50%, Amber color if the value is under 80% and GREEN else.

See below illustration to understand the rules setup.

![conditional formatting rules for traffic light](https://chandoo.org/wp/wp-content/uploads/2021/05/conditional-formatting-rules-for-traffic-light.png)

### Turning this cell to Traffic Light 🚦

Now that L3 can change colors, let’s make it a pretty traffic light.

First, make the % value in L3 disappear with custom cell format code of ;;;

Tip

You can use hide values in a range of cells by applying the custom format code ;;;

**[How to hide values with number formats](https://chandoo.org/wp/hide-cell/)
.**

Next, copy L3 and paste it as **[Picture Link](https://chandoo.org/wp/how-to-use-picture-links/)
.** This will give you a live snapshot of the traffic light cell.

As we now have a picture, we can apply picture format options to turn this rectangle to a circle shaped traffic light.

1.  Make the picture larger
2.  From Picture Format ribbon, crop > aspect ratio > 1:1
3.  You will get a perfect square
4.  Use crop > crop to shape > oval
5.  You will get a circle. If any of the edges look straight, just adjust your crop settings.
6.  Your traffic light is ready.

See this animated GIF to understand the process.

![creating a circle picture link for traffic light](https://chandoo.org/wp/wp-content/uploads/2021/05/creating-a-circle-picture-link-for-traffic-light.gif)

Finally, add a box behind the traffic light picture to frame it. Apply some shadow effect on the traffic light to get a nice look.

![formatting traffic light picture link](https://chandoo.org/wp/wp-content/uploads/2021/05/formatting-traffic-light-picture-link.png)

Group everything so you can move or position the traffic light where you need it.

### The finished project traffic light

Here is how my finished project traffic light looks.

![Project Management - Traffic Light - Demo](https://chandoo.org/wp/wp-content/uploads/2021/05/pm-traffic-light-demo-2.gif)

In the download file, you can find this and two other charts (thermometer and donut progress chart). Refer to my video above for instructions on that other two.

### More Project Status Charts for you

*   [Thermometer Chart](https://chandoo.org/wp/quick-thermometer-chart/)
    
*   [Gauge Chart with Excel](https://chandoo.org/wp/excel-speedometer-chart-download/)
    
*   [Burn down chart template](https://chandoo.org/wp/burn-down-charts/)
    
*   [Status Charts + Other useful PM Templates by Chandoo](https://chandoo.org/pmt/pmt-index-1.html)
    

Part 3 - The Dashboard
----------------------

So far we have created an interactive Gantt Chart and a traffic light progress chart. In the final part of this tutorial, we will fill missing gaps and complete the dashboard.

You will learn,

*   Colors, fonts & icons used in the dashboard design
*   Making a dynamic **upcoming activities / issues table**
*   Setting up dashboard tiles
*   Adding gantt chart snapshot
*   Creating resource loading information
*   Finalized project dashboard

### Resources for Part 3

### Excel files for practice

Use the below files to practice the concepts.

*   [Blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
    
*   [Completed Project Dashboard](https://chandoo.org/wp/wp-content/uploads/2021/06/step-3-Project-Dashboard-prep.xlsx)
    

### Video Tutorial - Part 3 of PM Dashboard

I created a detailed video tutorial explaining how the dashboard is constructed. Watch it below or [from my Youtube Channel](https://youtu.be/Exlj5qH0rhc)
.

### Colors, Icons & Fonts for the Dashboard

It is a good idea to decide the color scheme and visual design of your dashboard before you get too far. In our case, I used below.

![colors-fonts-icons used in the project management dashboard](https://chandoo.org/wp/wp-content/uploads/2021/06/colors-fonts-icons.png)

**Colors:**

*   Excel default color scheme +
*   #FF555A & #638EC6 for data bars in resource loading chart

**Fonts:**

*   Open Sans Extra Bold for headings
*   Calibri for everything else.

**Icons:** You can add FREE icons from Insert > Icons in Excel 365.

![Get free icons in Excel 365](https://chandoo.org/wp/wp-content/uploads/2021/06/free-icons-in-excel.png)

### Create Dashboard Sheet

Next, we will create a new worksheet, name it **dashboard.** Create a blank layout like below.

![pm dashboard - canvas](https://chandoo.org/wp/wp-content/uploads/2021/06/pm-dashboard-canvas.png)

We will fill this up with various charts & tables.

### Dynamic Activities / Issues Table

In this part of the tutorial, we will create an interactive Activities / Issues table, as shown below.

![demo-interactive-activities-issues-table](https://chandoo.org/wp/wp-content/uploads/2021/06/demo-interactive-activities-issues-table.gif)

**Step 1: Issue Tracker Table**

We already have activities table. Time to add **issues data** to our project file.  

![project-issues-table](https://chandoo.org/wp/wp-content/uploads/2021/06/project-issues-table.png)

This table is already available in the **[blank data file](https://chandoo.org/wp/wp-content/uploads/2021/05/Blank-Data-File.xlsx)
.** Just add it to data model by setting up a relationship between Issue\[Onwer\] and People\[Person\].

**Step 2: Set up a form control**![combo box form control is perfect for showing choices in dashboards](https://chandoo.org/wp/wp-content/uploads/2021/06/combo-box-form-control.png)

In the dashboard sheet, add a combo-box form control (Developer Ribbon > Form Controls) and set it to show one of these two values –

*   Activities
*   Issues 

Link this control to a cell in calculations worksheet (J8).

Tip

Form controls are great for making your charts & dashboards interactive. You can find them in the **Developer ribbon** of Excel.

[Learn more about Form Controls and how to use them](https://chandoo.org/wp/form-controls/)
.

**Step 3: Calculating Upcoming 10 Activities & Issues**

To calculate upcoming 10 activities / issues, we need this logic:

*   Activities: start date is after  today() 
*   Issues: close date of the issue is blank

We need to limit both lists to first 10 items.

We can use FILTER() formula to get such lists.

				
					`'note: $I$6 has TODAY() date 10 activities =INDEX(FILTER(activities,activities[Start Date]>$I$6),SEQUENCE(10),{1,2,4}) 10 issues =IFERROR(INDEX(SORT(FILTER(issues, issues[Date Closed]=""),4,1),SEQUENCE(10),{1,2,4}),"")`

				
			

**Step 4: Picking one of the lists based on form control input**

We can use IF formula to select either of these lists based on what user picked in the form control. Since **J8 cell in calculations** tells us what the choice is, we can use that to write our IF formula.

Once we have the results, just copy the values and paste them as reference in dashboard. Our dynamic activities / issues table will be ready.

![demo-interactive-activities-issues-table](https://chandoo.org/wp/wp-content/uploads/2021/06/demo-interactive-activities-issues-table.gif)

### Dashboard KPI Tiles

Next we will create the dashboard tiles.

Start by placing 4 rounded rectangles with fill color #404040 on the dashboard worksheet.

![pm-dashboard-kpi-tiles-setup](https://chandoo.org/wp/wp-content/uploads/2021/06/pm-dashboard-kpi-tiles-setup.png)

Next, copy paste the traffic light (part 2 of this tutorial) on first tile.

### Project KPI calculations

We need to calculate 3 numbers for the remaining tiles on the dashboard. They are, 

#### Days remaining

Number of days left to the project completion. This is the difference between last project activity End date and today.

				
					`=MAX(activities[End Date])-TODAY()`

				
			

#### On-going Activities

This is the number of activities that have already started and yet to reach completion.

				
					`=COUNTIFS(activities[Start Date],"<="&TODAY(), activities[% Done],"<1")`

				
			

#### Pending Issues

How many issues are yet to be closed.

				
					`=COUNTIFS(issues[Date Closed],"")`
				
			

### Adding KPI values to the dashboard tiles

On the dashboard, add three text boxes, one per each of the above three numbers. Using formula bar, link the text box value to the calculation worksheet values.

Adjust formatting of the text box. Also, add the icons to signify each KPI tile.

At this stage, our dashboard tiles will look like this:

![completed project dashboard kpi tiles](https://chandoo.org/wp/wp-content/uploads/2021/06/complted-project-dashboard-kpi-tiles.png)

### Bring in the Gantt Chart

We already created a fully interactive gantt chart in part 1 of this tutorial. Just head over to the gantt chart tab on the dashboard, copy a big enough range, go to the dashboard and paste it as **[linked picture](https://chandoo.org/wp/how-to-use-picture-links/)
.** 

This will give you a live snapshot of the gantt chart in the dashboard tab.

Adjust the size of the gantt chart picture and add any necessary border around it.

Cut & move the team slicer to the dashboard tab.

### The Resource Loading Chart

In the calculations worksheet, create a pivot table to show number of tasks & activities assigned to each person.

![pivot table with resource loading information](https://chandoo.org/wp/wp-content/uploads/2021/06/pivot-table-with-resource-loading-information.png)

Copy the pivot table data, go to dashboard and paste it as **link** in the correct place.

Adjust formatting and apply databars on issue & activity columns. 

Customize the data bar colors as per our color scheme.

And our dashboard is DONE!

The completed dashboard
-----------------------

![project management dashboard - finalized](https://chandoo.org/wp/wp-content/uploads/2021/06/project-management-dashboard-finalized.png)

Feel free to [download the full dashboard workbook from here](https://chandoo.org/wp/wp-content/uploads/2021/06/step-3-Project-Dashboard-prep.xlsx)
.

Also, [check out the video playlist](https://www.youtube.com/watch?v=FXnyKU6xZeI&list=PLmejDGrsgFyCS0n1GEXRuzxjK9wAXFNGo)
 to learn how I constructed this. The videos will give a ton of useful Excel tips as a bonus.

### More on Project Management...

Project Management is one of my passions and I talk about it extensively on my site & Youtube.

Please visit below pages to learn more about other cool PM stuff you can do with Excel.

*   [Budget vs. Actual analysis & charts](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [Making a Risk matrix with Excel](https://chandoo.org/wp/excel-risk-map-template/)
    
*   [Project Portfolio Dashboard with Excel](https://chandoo.org/wp/design-project-portfolio-dashboard/)
    

[![Project Portfolio Dashboard - Chandoo](https://chandoo.org/wp/wp-content/uploads/2021/05/project-portfolio-dashboard-small.png)](https://chandoo.org/pmt/pmt-index-1.html)

### [Ready to use Project Management Templates](https://chandoo.org/pmt/pmt-index-1.html)

Create awesome project management dashboards and reports using my templates. Trusted by 20,000+ project managers all over the world, these templates are designed to make you look awesome. Create Gantt charts, timelines, time sheets, issue trackers, risk trackers, project dashboards and portfolio dashboards using my templates.  
  
**[Click here to get them today.](https://chandoo.org/pmt/pmt-index-1.html)
**

Got something to say?

### 18 Responses to “How to create a fully interactive Project Dashboard with Excel – Tutorial”

1.  ![](https://secure.gravatar.com/avatar/b5864ba87ea958a92c86e2e610c883aacaf5b85dd1c368cf756943ea8e8e83a6?s=64&d=mm&r=g) Shweta Bandarkar says:
    
    [May 14, 2021 at 1:26 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-1999666)
    
    I'm not getting PowerBI pay dates since long . Please advice.
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-1999666)
    
2.  ![](https://secure.gravatar.com/avatar/9aad5c2c3c57f52397aa3d446b415bb35950cd34043557a8525c2101e6177526?s=64&d=mm&r=g) Rajnikant Katira says:
    
    [May 19, 2021 at 11:37 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2000794)
    
    Want to handle multiple projects which are going at multiple sites. Some activities are common and some are unique. HOW to Handle the same in one sheet at one place where multiple stakeholder can update the progress
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2000794)
    
3.  ![](https://secure.gravatar.com/avatar/90d42eef744d58566ab76eb37e19b620fae49e77be962639aff28e1f12b9371a?s=64&d=mm&r=g) Denise Z. says:
    
    [May 20, 2021 at 4:40 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2001236)
    
    Thank you! I appreciate all you do.
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2001236)
    
4.  ![](https://secure.gravatar.com/avatar/ccdcaeaad760a01d23a4b73de29db51611295c0c766fe5fcf25e0c9d82a4266c?s=64&d=mm&r=g) Martin Lewis says:
    
    [May 27, 2021 at 12:40 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2003532)
    
    Chandoo
    
    How do you get subtotals on top in a tabular pivot, I can only add to the bottom if I select tabular, on top if I use compact?
    
    Cheers
    
    Martin
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2003532)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [May 27, 2021 at 5:22 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2003629)
        
        Sorry for the confusion. I am also using OUTLINE layout.
        
        [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2003629)
        
5.  ![](https://secure.gravatar.com/avatar/c02c332b89c1d3fd8f9f92ee73345e22a0abd00485807f6e265046d735c0d163?s=64&d=mm&r=g) Sethumadhavan V S says:
    
    [May 31, 2021 at 5:11 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2004385)
    
    Hi Chandoo,  
    We have a attendance for civil labour at site. we need to maintain and give payment at the end of every week. the problem is, it the wages varies from Mason to Helper-1 , Helper-2 etc. Also we used to change the site as per the need. Now the task is we need to calculate their wages as per their presence and also need to site wise work detail. Can you help me in this regard.  
    Note: If required I can share the file.
    
    Regards,
    
    Sethumadhavan
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2004385)
    
    *   ![](https://secure.gravatar.com/avatar/3fd101f55d37f5462764bb8faa81476d50ff0d516a3c75ae8c9b99c28f5528c0?s=64&d=mm&r=g) SA Daniel says:
        
        [October 31, 2022 at 8:35 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2106023)
        
        Hi Sethumadhavan
        
        If not resolved till date, share me the file so that I may be of any use to your issue.
        
        Danny
        
        [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2106023)
        
6.  ![](https://secure.gravatar.com/avatar/1a3f1c666ea7857032bba1cf12e4e6f85ff214b0393157b3ae28a411b0a0e9f6?s=64&d=mm&r=g) Thierry Santhi says:
    
    [June 4, 2021 at 1:59 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2004860)
    
    Excellent and easy! Congrats
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2004860)
    
7.  ![](https://secure.gravatar.com/avatar/9a7b85d49c6b4e4b4cf6ce2f705aeefcdb916d165ae8756146f3fcf031394e42?s=64&d=mm&r=g) Tetonne says:
    
    [June 12, 2021 at 2:06 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2005874)
    
    great thanks a lot 🙂
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2005874)
    
8.  ![](https://secure.gravatar.com/avatar/ae6f87b41e2bb4a5eceb78e68aff9f2bf651639bb96b15c16840ddbc9fec9c4b?s=64&d=mm&r=g) [Daniel](https://computeexpert.com/)
     says:
    
    [June 13, 2021 at 3:38 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2005907)
    
    Thanks for the excel dashboard how-to pointers! Dashboard is indeed something important to learn if you want to visualize your data in excel
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2005907)
    
9.  ![](https://secure.gravatar.com/avatar/80d9c145308e6222f66c90276291a90739934a90cc075a7817259906d051dae3?s=64&d=mm&r=g) Med says:
    
    [June 28, 2021 at 7:08 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2008510)
    
    I recently attended an Excel training program here [https://www.ted.com.my/it-training/ms-excel-2013-2016-basic-intermediate/](https://www.ted.com.my/it-training/ms-excel-2013-2016-basic-intermediate/)
    . I didn't expect that you can actually create project management info using Excel or a spreadsheet. Good info!
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2008510)
    
10.  ![](https://secure.gravatar.com/avatar/f0c66d393ecc0b1ea541599288e1adc10165477b181db0e3545c7f60ba45f4ab?s=64&d=mm&r=g) Tom says:
    
    [August 14, 2021 at 9:14 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2021523)
    
    Dear Chandoo,
    
    Great dashboard!  
    I would like to add a dynamic progress S-curve for planned and actual progress from Gantt chart. Could you help with it?
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2021523)
    
11.  ![](https://secure.gravatar.com/avatar/7760f6789aadf53bc1debcad1b1e3505131cb94c86020f4eeba47abf2c66904e?s=64&d=mm&r=g) ArunKumar Subramanian says:
    
    [August 30, 2021 at 11:46 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2026602)
    
    Awesome Bro..
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2026602)
    
12.  ![](https://secure.gravatar.com/avatar/9112b414d87fcc31f1c1ed4cbea4b73ddce9e12d6390b2918ee95d022f1c82d2?s=64&d=mm&r=g) Ines says:
    
    [November 9, 2021 at 6:14 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2042205)
    
    Dear Chandoo  
    I have been following you since 2011.  
    THANK YOU for hour amazing work!!!
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2042205)
    
13.  ![](https://secure.gravatar.com/avatar/f64b2cd97275524b5821de08c43e7306829eb8ba74a4b72b04bc0dc8ba72dc36?s=64&d=mm&r=g) Benjawan says:
    
    [March 18, 2022 at 1:01 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2071607)
    
    Thank you so much for your sharing. It's useful a lot for me.
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2071607)
    
14.  ![](https://secure.gravatar.com/avatar/4634db202f52f36a12f9e7073ad14987c5bb091bafdc65b5fb2e0a0abbd71c90?s=64&d=mm&r=g) salim says:
    
    [November 27, 2023 at 7:48 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2154309)
    
    hi,  
    it gives me in porcentage this error #NAME?  
    how ?
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2154309)
    
15.  ![](https://secure.gravatar.com/avatar/5e3091873c7381597577bea3f538b9466169e47181b74bb1b32dcb3832334992?s=64&d=mm&r=g) Courtney says:
    
    [September 9, 2024 at 5:42 am](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2283437)
    
    In the Step 3 Project Dashboard Prep sheet, workbook 'Calculations', the formula in H16 is not calculating. I have been unable to repair in my copy. Do you have any suggestions, please?
    
    [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2283437)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [September 9, 2024 at 10:10 pm](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2283577)
        
        If you are getting a CALC error it means there are no upcoming activities as per your data. Either change the data (add some future activities) or change the cell I6 to an older date.
        
        [Reply](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#comment-2283577)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/interactive-project-dashboard-with-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ