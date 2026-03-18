# How to Create a Gantt Chart in Excel - FREE Template

**Source:** https://trumpexcel.com/gantt-chart-in-excel

---

[Skip to content](https://trumpexcel.com/gantt-chart-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/gantt-chart-in-excel/#below-title)

Last week I wrote an article on how to create a [Dynamic Pareto Chart](https://trumpexcel.com/dynamic-pareto-chart-in-excel/ "Dynamic Pareto Chart in Excel – The 80/20 Phenomenon")
 in Excel. With the charting fever still riding high, today I will show you how to create a Gantt Chart in Excel.

Gantt Chart is a simple yet powerful project management tool that can be used for creating a schedule or tracking the progress.

Let’s say Bruce Wayne ([Batman](https://en.wikipedia.org/wiki/Batman)
) wants a new [Batsuit](https://en.wikipedia.org/wiki/Batsuit)
 and instructs Alfred (the butler and his confidante) to get it made. Alfred, who is an avid project management student, comes up with a simple Gantt Chart in Excel to get the plan ready. And this is what he shows Mr. Wayne when asked for a status report:

![Gantt Chart in Excel - Building a BatSuit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20349'%3E%3C/svg%3E)

_**Follow Along.. Download the Example File**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Gantt-Chart.xlsx)

#### Creating a Gantt Chart in Excel

Here are the steps to quickly create this Gantt Chart in Excel:

1.  Get the Data in place. Here we need three data points:
    *   Activity Name
    *   Start Date
    *   Number of Days it takes to complete the activity![Gantt Chart in Excel - Activity List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20272'%3E%3C/svg%3E)
2.  Go to Insert –> Charts –> Bar Chart –> Stacked Bar. This will insert a blank chart in the worksheet.![Gantt Chart in Excel - Insert Bar Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20190'%3E%3C/svg%3E)
3.  Select the Chart and go to Design tab. In the Design Tab, Go to Data Group and click on Select Data.![Gantt Chart in Excel - Select Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20275%20114'%3E%3C/svg%3E)
4.  In Select Data Source dialogue box, click on Add. In the Edit Series dialogue box, enter the following data:
    *   Series Name: Start Date
    *   Series Values: =’Gantt Chart’!$B$2:$B$12![Gantt Chart in Excel - Start Date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20165'%3E%3C/svg%3E)
5.  Again click on Add in Select Data Source dialogue box and use the following data:
    *   Series Name: Number of Days
    *   Series Values: =Sheet1!$C$2:$C$12![Gantt Chart in Excel - Select Data- Number of Days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20165'%3E%3C/svg%3E)
6.  In the Select Data Source dialogue box, in the right half of the pane titled Horizontal (Category) Axis Labels, click on Edit.![Gantt Chart in Excel - Edit Horizontal Series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20297'%3E%3C/svg%3E)
7.  In the Axis Labels dialogue box, select the range that has all the activities names.![Gantt Chart in Excel - Axis Labels](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20334%20121'%3E%3C/svg%3E)
8.  Now your chart would look something as shown below. You would notice that the activities are in the reverse order (for example, Test for Survival is the first one).![Gantt Chart in Excel - Mid-way](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20298'%3E%3C/svg%3E)
9.  To correct the order of activities, right click on the vertical axis (that has activity names) and select Format Axis. In Format Axis Pane, under Axis Options, click on the checkbox – ‘Categories in Reverse Order’![Gantt Chart in Excel - Categories in Reverse Order](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20262%20442'%3E%3C/svg%3E)
10.  As of now, your horizontal Axis (which has dates) is at the top. Right click on the Horizontal Axis (which has dates) and select Format Axis. In the Format Axis Pane make the following changes:
    *   In Axis Options, change the Minimum to 2/25/2015 (you can also type 42060, which is the number that represents this date) _\[This ensures that your chart starts at 2/25/2015\]_
    *   In Labels, change Label Position to High![Gantt Chart in Excel - Setting Minimum](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20563%20445'%3E%3C/svg%3E)
11.  Now your Gantt Chart is almost ready. Just select the blue bars and remove the color fill and border color.
12.  Change the Title, do some formatting to make it look awesome (and it makes you look awesome).![Gantt Chart in Excel - Building a BatSuit](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20349'%3E%3C/svg%3E)

Gantt Chart is so powerful, even Batman uses it 🙂

**_Try it Yourself.. Download the Example File_**[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/02/Gantt-Chart.xlsx)

I would love to learn from you. Let me know how you use Gantt Chart and/or other project management tools. Leave your footprints in the comments section below!

**You May Also Like the Following Excel Tutorials:**

*   [Employee Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Dynamic Pareto Chart – The 80/20 phenomenon](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Actual Vs Target Charts in Excel](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    .
*   [Milestone Chart Template](https://trumpexcel.com/milestone-chart-in-excel/)
    .
*   [Creating a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [10 Advanced Excel Charts that You Can Use In Your Day-to-day Work](https://trumpexcel.com/advanced-charts/)
    
*   [Employee Leave Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “How to Create a Gantt Chart in Excel – Batman Style”
-------------------------------------------------------------------

1.  HI,  
    I CANNOT COMPLETE THE 4TH STEP.  
    ITS SHOWING ERROR .=’Gantt Chart’!$B$2:$B$12  
    MY DATA RANGES FROM a2 TO a14
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-12050)
    
2.  Plz guide how to make gantt chart with predecessor
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-9714)
    
3.  Dear Sumit,
    
    If you dont mind, please also teach us tutorial on how to create these kind of gantt chart:
    
    [http://excelhawk.com/gantt+chart+excel+template.html](http://excelhawk.com/gantt+chart+excel+template.html)
    
    Thanks,
    
    Stuart
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-3164)
    
4.  Thanks Sumit for this fantastic idea.  
    I have other question. I’m trying to make a combination with two graphics. One is similar to this, and the other is one update with real start date and percentage (I have transformed to days). But the only way I have found is to make the second transparent and move exactly over the first one.  
    Can I make in other way? THANKS!
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-2573)
    
5.  Sumit,  
    Thank you for posting this training, will you be posting more about grant charts?
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-1840)
    
    *   Thanks for commenting Dan.. I plan to post more tutorials on Project Management using Excel. I am also working on a Gantt Chart style template and will post it soon.. Stay Tuned!
        
        If you have any ideas, do share with me 🙂
        
        [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-1841)
        
6.  Thanks for posting this! I was looking for guidance to create Gantt Chart – your post makes it quite simple to understand and the Batman Suit example made it very interesting as well 🙂 I would definitely implement it in my work!
    
    [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-1795)
    
    *   Thanks for commenting Mehar.. Glad you found it useful 🙂
        
        [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-1796)
        
    *   Thanks for commenting Mehar.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/gantt-chart-in-excel/#comment-1797)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/gantt-chart-in-excel/#respond)

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