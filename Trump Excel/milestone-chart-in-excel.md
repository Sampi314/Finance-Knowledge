# How to Create a Timeline / Milestone Chart in Excel

**Source:** https://trumpexcel.com/milestone-chart-in-excel

---

[Skip to content](https://trumpexcel.com/milestone-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/milestone-chart-in-excel/#below-title)

**Watch Video – Creating a Timeline / Milestone Chart in Excel**

In the projects I have worked so far, Milestone Charts (also known as timeline charts) are often one of the most discussed parts.

A commitment to delivering is as important as the project itself. A milestone chart is an effective tool to depict project scope and timelines.

In this post, I will show you a simple technique to quickly generate a Milestone chart in Excel.

Something as shown below:

![Timeline / Milestone chart in Excel Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20282'%3E%3C/svg%3E)

Steps to Create Milestone Chart in Excel
----------------------------------------

1.  Get the data in place. To create this, I have two columns of data (Date in B3:B10 and Activity in C3:C10) and three helper columns.  
    ![Timeline / Milestone Chart in Excel Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20362'%3E%3C/svg%3E)
2.  Go to Insert –> Charts –> Line Chart with Markers  
    ![Timeline / Milestone Chart in Excel - Line Chart with Markers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20219'%3E%3C/svg%3E)
3.  Go to Design –> Select Data
    *   In Select Data Source dialogue box, click on Add
    *   In the Edit Series Dialogue box
        *   _Series Name: Date_
        *   _Series Values: Activity Cells in Column F  
            __This inserts a line chart with X-Axis values as 1,2,3.. and Y-axis values as 0_
4.  In the Select Data Source dialogue box, click on Edit in Horizontal (Category) Axis Labels and select dates in Column E. This changes X-Axis values to dates.  
    ![Timeline / Milestone - Excel Line Chart Changing Horizontal Axis Values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20597%20156'%3E%3C/svg%3E)
5.  In Select Data Source dialogue box, click on Add
    *   In the Edit Series Dialogue Box
        *   _Series Name: Activity_
        *   _Series Values: Text Placement Cells in Column G_  
            _This inserts a haphazard line chart. Something as shown below:_  
            ![Timeline / Milestone - Combination Line Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20259'%3E%3C/svg%3E)
        *   Click on any of the Activity data-point, right-click and select a change chart type. In Change chart Type dialogue box, select the Column chart. This will change the haphazard Line chart into Column Chart  
            ![Timeline / Milestone Chart in Excel - Combo Chart Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20253'%3E%3C/svg%3E)
        *    This will change the haphazard Line chart into Column Chart  
            ![Timeline / Milestone Chart in Excel Line chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20259'%3E%3C/svg%3E)
6.  Right-click on data bars and select Format Data Series. In series option pane, select
    1.  *   _Plot Series on: Secondary Axis  
            __This would introduce a [secondary vertical axis](https://trumpexcel.com/add-secondary-axis-charts/)
             on the right of the chart. Click on it and delete it._
7.  Go to Design –> Select Data
    *   In Select Data Source Dialogue box, select Activity series and click on Edit in Horizontal (Category) Axis Labels box. In the Axis Labels dialogue box, select Activity cells in column F
8.  Select bars, right-click and select Add Data Labels
9.  Right-click on the data label and select Format Data Label
    1.  *   In format data label pane, select Category Name (and un-check any other). This adds activity names as data labels. Adjust the position to get activity name at the tip of the bar  
            ![Timeline / Milestone Chart in Excel - Data Label formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20137%20252'%3E%3C/svg%3E)
10.  Select and go to Design –> Add Chart Element –> [Error Bars](https://trumpexcel.com/error-bars-excel/)
     –> More Error Bar Options \[For 2010, this option is in Layout –> Analysis\]  
    ![Timeline / Milestone chart in Excel - Insert Error Bars in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20218%20265'%3E%3C/svg%3E)
11.  In the Format Error Bars Pane, make the following selections
    1.  *   _Vertical Error Bar: Minus_
        *   _End Style: No Cap_
        *   _Error Amount: Percentage – 100%_
12.  Right-click on bars and select Format Data Series. In Format Data Series Pane (in Fill and Line)
    1.  *   _Fill: No Fill_
        *   _Border: No Border_

That’s it!! Your Milestone Chart is ready. Garnish it and serve it hot 🙂

_**Try it Yourself.. Download the file from here**_  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Milestone-chart-in-Excel.xlsx)

**You May Also Like the Following Excel Tutorials:**

*   [Creating a Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [Creating a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Excel Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [How to Make a Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Employee Leave Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Free Excel Templates Download](https://trumpexcel.com/free-excel-templates/)
    .
*   [Creating a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    .
*   [Creating a Combination Chart in Excel](https://trumpexcel.com/combination-charts-in-excel/)
    .
*   [Creating an Area Chart in Excel](https://trumpexcel.com/area-chart/)
    .
*   [Advanced Excel Charts Examples](https://trumpexcel.com/advanced-charts/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “How to Create a Timeline / Milestone Chart in Excel + Free Template Inside”
-------------------------------------------------------------------------------------------

1.  Hello, this is just fantastic, love it. I was wondering if you knew (or if it was possible) to not include middle unused dates. I am making an evolutionary timeline, so jumping 100’s of millions of years is going to make the graph rather long..
    
    Thanks!
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-17045)
    
2.  Thanks sr, very nice and helpful for my project.
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-14519)
    
3.  If it’s messing up when you add new data entries, make sure everything is sorted according to date.
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-13298)
    
4.  Hi Sumit, what would the steps be to create a timeline like the first one shown, but using Excel for Mac 2011? My dialogue boxes are very different from your instructions, and I can’t quite figure it out!
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-11914)
    
5.  Is there a way to use a chart like this but to have subtasks? I’m driving myself crazy trying to learn how to add in a subtask. I was thinking i would resort to hand coloring each task one color then the subtask would match but be a little lighter. But this project will span several years and I really want to avoid and manually coloring each task. Any suggestions?
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-11007)
    
6.  Thanks for sharing Sumit! It works great…
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-10017)
    
7.  I found it extremely helpful and was able to successfully create it but later when I happen to add any additional date, activity, it messes up the graphic completely. Can I gracefully modify it when a new task/activity has to be added without messing up the graphic?
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-8696)
    
    *   Did you get ever work this out in the end? I’m currently having the same problem. Is there a way for me to insert new events onto the timeline without having to start over again?
        
        [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-8879)
        
        *   Hi, you can do this with the following steps:
            
            1\. Add the additional data to your table.  
            2\. Click on one of the long thin lines on the graph which points to the ‘Activity’.  
            3\. You should see that on the table, the data is highlighted in little coloured boxes. Simply drag this down to incorporate the additional data. Click anywhere on the sheet besides the table or graph when the new data has been highlighted to deselect them.  
            4\. Right click the chart and choose: ‘Select Data…’  
            5\. Select ‘Date’ in the left column (Legend Entries)  
            6\. Select ‘Edit’ in the right column (Horizontal Axis Labels) and select all dates, including the new dates.  
            7\. Select ‘Activity’ in the left column and repeat step 6, ensuring all activities are highlighted, including the new activities.  
            8\. Press OK to exit the Data Selection window.
            
            That should be it! Just adjust the new labels to be in the correct position and you should be good to go.
            
            Lew
            
            [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-9886)
            
8.  This is awesome! VERY useful and i shall implement it for my next project!!
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-1780)
    
    *   Thanks Amber.. Glad you found it useful 🙂
        
        [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-1784)
        
9.  Thanks for sharing the Template. I will now use this in creating project plans.
    
    [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-1640)
    
    *   Thanks Greg.. Glad you found it useful 🙂
        
        [Reply](https://trumpexcel.com/milestone-chart-in-excel/#comment-1785)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/milestone-chart-in-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK