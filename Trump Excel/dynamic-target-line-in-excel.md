# Create Dynamic Target Line in Excel Bar Chart

**Source:** https://trumpexcel.com/dynamic-target-line-in-excel

---

[Skip to content](https://trumpexcel.com/dynamic-target-line-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-target-line-in-excel/#below-title)

If you are in the sales department and your life is all about targets, this charting technique is for you. And if you are not, read it anyway to learn some cool excel charting tricks.

In this blog post, I will show you a super way to create a dynamic target line in an Excel chart, that can help you track your performance over the months. Something as shown below: ![Dynamic Target Line in Excel Chart](https://trumpexcel.com/wp-content/uploads/2014/04/Dynamic-Target-Line-in-Excel-Chart.gif)

The target line is controlled by the [scroll bar](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
, and as if the target is met (or exceeded) in any of the months, it gets highlighted in green.

Creating a Dynamic Target Line in Excel Bar Chart
-------------------------------------------------

There are 3 parts to this chart:

1.  The bar chart
2.  The target line (horizontal dotted line)
3.  The scroll bar (to control the target value)

_**The Bar Chart**_

I have data as shown below:

![Dynamic Target Line in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20285'%3E%3C/svg%3E)

Cells B2:B13 has all the values while C2:C13 only shows a value if it exceeds the target value (in cell F2). If the value is lower than the target value, it shows #N/A. Now we need to plot these values in a cluster chart

1.  Select the entire data set (A1:C13)
2.  Go to Insert –> Charts –> Clustered Column Chart  
    ![Dynamic Target Line in Excel - Clustered Column Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20101'%3E%3C/svg%3E)
3.  Select any of the bars for ‘Above Target’ values and right click and select Format Data Series  
    ![Dynamic Target Line in Excel - Select Format Series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20245'%3E%3C/svg%3E)
4.  In the Series Option section, change Series Overlap value to 100%  
    ![Dynamic Target Line in Excel - 100 Percent Overlap in Chart Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20218%20218'%3E%3C/svg%3E)
5.  This creates a chart, where all the values that exceed the target are highlighted in a different color (you can check this by changing the target value)  
    ![Dynamic Target Line in Excel - Target Values Highlighted in Different Color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20276'%3E%3C/svg%3E)

 _**The Target Line**_

Here let me show you a smart way to create a target line using [error bars](https://trumpexcel.com/error-bars-excel/)

1.  Select the chart and go to Design –> Select Data  
    ![Dynamic Target Line in Excel - Excel Chart Select Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20109'%3E%3C/svg%3E)
2.  In the Select Data Source dialog box, Click Add
3.  In the Edit Series box, Type Series Name as ‘Target Line’ and in Series Value select your Target Value cell  
    ![Dynamic Target Line in Excel - Adding a target line bar in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20338%20169'%3E%3C/svg%3E)
4.  This will insert a bar chart only for the first data point (January)  
    ![Dynamic Target Line in Excel - Adding a target line bar in Excel Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20316%20251'%3E%3C/svg%3E)
5.  Select this data bar and right click and select Change Series Chart Type  
    ![Dynamic Target Line in Excel - Change Series Chart Type in Excel Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20239'%3E%3C/svg%3E)
6.  Change its Chart Type to [Scatter Chart](https://trumpexcel.com/scatter-plot-excel/)
    . This will change the bar into a single dot in January  
    ![Dynamic Target Line in Excel - Bar changed to scatter in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20249'%3E%3C/svg%3E)
7.  Select the data point and go to Design –> Chart Layouts –> Add Chart Element –> Error Bars –> More Error Bars Options
    *   _For Excel 2010, select the data point and go to Layout –> Analysis –> Error Bars –> More Error Bars Options_  
        ![Dynamic Target Line in Excel - Error Bars in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20267%20326'%3E%3C/svg%3E)
8.  You will notice horizontal error bar lines on both sides of the scatter point. Select that horizontal error bar and then in the Error Bar Options section, select Custom and click on Specify Value  
    ![Dynamic Target Line in Excel - Using Error Bars in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20630%20309'%3E%3C/svg%3E)
9.  Give positive value as 11 and negative value as 0 (you can use hit and trial to see what value look good for your chart)  
    ![Dynamic Target Line in Excel - Setting Values for Error Bars in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20224%20162'%3E%3C/svg%3E)
10.  Select the Scatter data point and right-click and select Format Series Data. Go to Marker Options and select Marker Type as none. This removes the data point and you only have the error bar (which is your target line)
11.  Note that your error bar would change whenever you change the target value. Just format it to make it a [dotted line](https://trumpexcel.com/remove-dotted-lines-excel/)
     and change its color to make it look better

_**The Scroll Bar**_

1.  Create a scroll bar and align it with the chart. Fit the scroll bar along with the chart. [_Click here to learn how to create a scroll bar in Excel_](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
    .
2.  Make the maximum value of the scroll bar equal to the maximum value in your chart, and link the scroll bar value to any cell (I have used G2)
3.  In the cell that has the target value, use the formula \=500-G2 (500 is the maximum value in the chart)
4.  This is to make sure that your target value now moves with the scroll bar

That’s it!! Now when you move the scroll bar and change the target values, the bars that meet the target will automatically get highlighted in a different color.

_**Try it yourself.. Download the file**_  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/11/Dynamic-Target-Line-in-Excel-Bar-Charts.xlsx)

**You May Also Like the Following Excel Tutorials:**

*   [Dynamic Pareto Chart – The 80/20 phenomenon](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Dynamic Charting – Highlight Data points with a click of a button](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
    .
*   [Creating a Gantt Chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
    .
*   [Creating a Milestone chart in Excel](https://trumpexcel.com/milestone-chart-in-excel/)
    .
*   [How to Make a Histogram in Excel.](https://trumpexcel.com/histogram-in-excel/)
    
*   [Creating Actual Vs Target Charts in Excel](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    .
*   [Creating Combination Charts in Excel](https://trumpexcel.com/combination-charts-in-excel/)
    .
*   [How to Create a Dynamic Chart Range in Excel](https://trumpexcel.com/dynamic-chart-range/)
    .
*   [Adding Trendlines in Excel Charts](https://trumpexcel.com/trendline/)
    .
*   [How to Add Axis Titles in Charts in Excel?](https://trumpexcel.com/add-axis-titles-in-charts-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

24 thoughts on “Create Dynamic Target Line in Excel Bar Charts”
---------------------------------------------------------------

1.  If i wanted the target to be between -10% and +10% how would i do the formula?
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-16933)
    
2.  DID NOT WORK!!!!!! SUCKS!!!!!
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-14261)
    
3.  Very useful video. Thanks
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-13326)
    
4.  This is very educative. It has saved me a lot of time and has answered most of my questions. Thanks so much for sharing such a helpful information
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-12480)
    
5.  thank you, thank you, thank you
    
    your are the best, God protect you brother
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-10940)
    
6.  I love this tutorial but the I cannot overlap the data if I have more than one type of sum and one target. It works like the example with one, but if you apply this to one than one column, it tires to cover it as a series. Is this possible to go around?
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-9413)
    
7.  Hello! Thank you for your post, it worked well. If you are still accepting queries, I am an educator looking to create a dynamic target line across multiple assessments on the same chart. Using your method above, I can create one chart for each test a student has taken, but when I attempt for multiple tests for each student, the step that tells me to move the Series Overlap to 100%, it causes all but one bar to show per student. I would like to combine all tests for all students in a class into one chart, having each multiple test bar per student react to the dynamic target line as you show for the sales bar per month. (Basically, for each month in your example and all on one chart, I would like to track the sales of 7 different products, and have each product sales bar show up next to each other, and all change color depending on the target line’s value). Is that something that can be done?
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-3919)
    
    *   I have the same problem. I love this tutorial but the I cannot overlap the data if I have more than one type of sum and one target. It works like the example with one, but if you apply this to one than one column, it tires to cover it as a series. Is this possible to go around? Did you ever get an answer?
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-9414)
        
8.  fantastic post also share some dashboard example
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-3266)
    
9.  Great trick. This was very useful today. I am sure that I will use this often. Thanks for sharing.
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2491)
    
10.  Greetings Sumit, I really like this as it addresses something I’ve been thinking about for some time. Creating a Histogram and using the standard deviation and color the chart accordingly. Your method would allow me to assign the target line as the Standard deviation line, those below the line are my outliers and those above are within the acceptable range. Unfortunately I work on a Mac so I will be finding a way around my limitations to make this work. Thank you for your inspirations!
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2229)
    
11.  Hello Sumit,
    
    That’s really awesome but How can i do it in Excel 2010.
    
    Thanks,  
    Mahesh
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2143)
    
    *   Hello Mahesh,
        
        Great question, and I’m certain if you follow the instructions in the video, it should work well for you as it does for me, and I’m working on a Mac(Excel 2011) which has less capability than Excel 2010 for Windows.
        
        I hoped that answered your question
        
        Regards,  
        Dane
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2253)
        
12.  I think you are the best in excel dashboard.
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2087)
    
    *   Thanks for the kind words Pablo 🙂
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-2090)
        
13.  downloaded template and works wonders
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1923)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1924)
        
    *   Hi Sumit. Any tips on how to create a excel dashboard.
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1930)
        
        *   I would soon be writing more about dashboard examples and how to create it.
            
            [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1931)
            
14.  Hello Sumit! I downloaded this template but target line is not moving by scrolling.Do I need to change some excel opetions?
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1622)
    
    *   Hello Imran.. Thanks for pointing out. I have updated the download file.
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1623)
        
15.  For a different approach: [http://hesseldewalle.blogspot.nl/2014/04/excel-chart-with-target-line-based-on.html](http://hesseldewalle.blogspot.nl/2014/04/excel-chart-with-target-line-based-on.html)
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1356)
    
16.  Dear Sumit,
    
    Nice post sumit….
    
    Regards,  
    pAvi
    
    [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1345)
    
    *   Thanks Pavi.. Glad you liked it.
        
        [Reply](https://trumpexcel.com/dynamic-target-line-in-excel/#comment-1346)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-target-line-in-excel/#respond)

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