# Excel Sparklines - A Complete Guide with Examples

**Source:** https://trumpexcel.com/sparklines

---

[Skip to content](https://trumpexcel.com/sparklines/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sparklines/#below-title)

Sparklines feature was introduced in Excel 2010.

In this article, you’ll learn all about Excel Sparklines and see some useful examples of it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sparklines/#)

What are Sparklines?
--------------------

Sparklines are tiny charts that reside in a cell in Excel. These charts are used to show a trend over time or the variation in the dataset.

You can use these sparklines to make your bland data look better by adding this layer of visual analysis.

While Sparklines are tiny charts, they have limited functionality (as compared with regular charts in Excel). Despite that, Sparklines are great as you can create these easy to show a trend (and even outliers/high-low points) and make your reports and dashboard more reader-friendly.

Unlike regular charts, Sparklines are not objects. These reside in a cell as the background of that cell.

Types of Sparklines in Excel
----------------------------

In Excel, there are three types of sparklines:

*   Line
*   Column
*   Win-loss

In the below image, I have created an example of all these three types of sparklines.

![Excel Sparklines - All three types](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20184'%3E%3C/svg%3E)

The first one in G2 is a line type sparkline, in G3 is a column type and in G4 is the win-loss type.

Here are a few important things to know about Excel Sparklines:

1.  Sparklines are dynamic and are dependent on the underlying dataset. When the underlying dataset changes, the sparkline would automatically update. This makes it a useful tool to use when [creating Excel dashboards](https://trumpexcel.com/creating-excel-dashboard/)
    .
2.  Sparklines size is dependent on the size of the cell. If you [change the cell height](https://trumpexcel.com/change-row-height-excel/)
     or width, the sparkline would adjust accordingly.
3.  While you have sparkline in a cell, you can also enter a text in it.
4.  You can customize these sparklines – such as change the color, add an axis, highlight maximum/minimum data points, etc. We will see how to do this for each sparkline type later in this tutorial.

**Note**: A Win-loss sparkline is just like a column sparkline, but it doesn’t show the magnitude of the value. It is better used in situations where the outcome is binary, such as Yes/No, True/False, Head/Tail, 1/-1, etc. For example, if you’re plotting whether it rained in the past 7 days or not, you can plot a win-loss with 1 for days when it rained and -1 for days when it didn’t. In this tutorial, everything covered for column sparklines can also be applied to the win-loss sparklines.

![Win-loss sparkline in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20697%20108'%3E%3C/svg%3E)

Now let’s cover each of these types of sparklines and all the customizations you can do with it.

Inserting Sparklines in Excel
-----------------------------

Let’s say that you want to insert a line sparkline (as shown below).

![Line Sparkline in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20103'%3E%3C/svg%3E)

Here are the steps to insert a line sparkline in Excel:

1.  Select the cell in which you want the sparkline.
2.  Click on the Insert tab.![Insert Tab in the Ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20196'%3E%3C/svg%3E)
3.  In the Sparklines group click on the Line option.![Click on the Line Sparkline Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20135'%3E%3C/svg%3E)
4.  In the ‘Create Sparklines’ dialog box, select the data range (A2:F2 in this example).![DataRange for the Line Sparkline - dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20238'%3E%3C/svg%3E)
5.  Click OK.

This will insert a line sparkline in cell G2.

![Line Sparkline in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20103'%3E%3C/svg%3E)

To insert a ‘Column’ or ‘Win-loss’ sparkline, you need to follow the same above steps, and select Columns or Win-loss instead of the Line (in step 3).

While the above steps insert a basic sparkline in the cell, you can do some customization to make it better.

When you select a cell that has a Sparkline, you’ll notice that a contextual tab – **Sparkline Tools Design** – becomes available. In this contextual tab, you’ll find all the customization option for the selected sparkline type.

![Excel Sparklines Design Tools - Contextual Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20210'%3E%3C/svg%3E)

Editing the DataSet of Existing Sparklines
------------------------------------------

You can edit the data of an existing sparkline by using the Edit Data option. When you click on the Edit Data drop down, you get the following options:

*   **Edit Group Location & Data**: Use this when you have grouped multiple sparklines and you want to change the data for the entire group (grouping is covered later in this tutorial).
*   **Edit Single Sparkline’s Data**: Use this to change the data for the selected sparkline only.

![Edit Group option in Sparkline design tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20267'%3E%3C/svg%3E)

Clicking on any of these options open the Edit Sparklines dialog box where you can change the data range.

Handling Hidden and Empty Cells
-------------------------------

When you create a line sparkline with a dataset that has an empty cell, you will notice that the sparkline shows a gap for that empty cell.

![Line Sparkline in Excel - mising datapoint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20155'%3E%3C/svg%3E)

In the above dataset, the value for April is missing which creates a gap in the first sparkline.

Here is an example where there is a missing data point in a column sparkline.

![Column Sparkline in Excel - missing data point](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20145'%3E%3C/svg%3E)

You can specify how you want these empty cells to be treated.

Here are the steps:

1.  Click the cell that has the sparkline.
2.  Click the Design Tab (a contextual tab that becomes available only when you select the cell that has a sparkline).
3.  Click on the Edit Data option (click on the text part and not the icon of it).
4.  In the drop-down, select ‘Hidden & Empty Cells’ option.![Hidden or Empty cells option in sparklines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20265'%3E%3C/svg%3E)
5.  In the dialog box that opens, select whether you want to show
    *   Empty cells as gaps
    *   Empty cells as zero
    *   Connect the before and after data points with a line \[this option is available for line sparklines only\].![Hidden or Empty cells settigns dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%20187'%3E%3C/svg%3E)

In case the data for the sparkline is in cells that are hidden, you can check the ‘Show data in hidden rows and columns’ to make sure the data form these cells is also plotted. If you don’t do this, data from hidden cells will be ignored.

Below is an example of all three options for a line sparkline:

![Line Sparkline in Excel - handing data gaps and empty cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20183'%3E%3C/svg%3E)

1.  Cell G2 is what happens when you choose to show a gap in the sparkline.
2.  Cell G3 is what happens when you choose to show a zero instead.
3.  Cell G2 is what happens when you choose to show a continuous line by connecting the data points.

You can do the same with column and win-loss sparklines as well (not the connecting data point option).

Changing the Sparkline Type
---------------------------

If you want to quickly change the sparkline type – from line to column or vice versa, you can do that using the following steps:

*   Click the sparkline you want to change.
*   Click the Sparkline Tools Design tab.
*   In the Type group, select the sparkline you want.

![Changing the sparkline type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20201'%3E%3C/svg%3E)

Highlighting Data Points in Sparklines
--------------------------------------

While a simple sparkline shows the trend over time, you can also use some markers and highlights to make it more meaningful.

For example, you can highlight the maximum and the minimum data points, first and the last data point, as well as all the negative data points.

Below is an example where I have highlighted the maximum and minimum data points in a line and column sparkline.

![Sparklines in Excel - highlight data points](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20148'%3E%3C/svg%3E)

These options are available in the Sparkline Tools tab (in the show group).

![Sparklines Show markers option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20197'%3E%3C/svg%3E)

Here are the different options available:

1.  **High/Low Point**: You can use any one or both of these to highlight the maximum and/or the minimum data point.
2.  **First/Last Point**: You can use any one or both of these to highlight the first and/or the last data point.
3.  **Negative Points**: In case you have negative data points, you can use this option to highlight all of these at once.
4.  **Markers**: This option is available only for line sparklines. It will highlight all the data points with a marker. You can change the color of the marker using the ‘Marker Color’ option.

Sparklines Color and Style
--------------------------

You can change the way sparklines look using the style and color options.

It allows you to change the sparkline color (of lines or columns) as well as the markers.

![Style and Color Options in Sparklines in Excel - color and marker](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20160'%3E%3C/svg%3E)

You can also use the pre-made style options. To get the full list of options. click on the drop-down icon in the bottom-right of the style box.

![Drop-down icon of the style options for sparklines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20160'%3E%3C/svg%3E)

**Pro Tip**: If you’re are using markers to highlight certain data points, it’s a good idea to choose a line color that is light in color and marker that is bright and dark (red works great in most cases).

Adding an Axis
--------------

When you create a sparkline, in its default form, it shows the lowest data point at the bottom and all the other data points are relative to it.

In some cases, you may not want this to be the case as it seems to show a huge variation.

In the below example, the variation is only 5 points (where the entire data set is between 95 and 100). But since the axis starts from the lowest point (which is 95), the variation looks huge.

![Line Sparkline in Excel - axis variation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20111'%3E%3C/svg%3E)

This difference is a lot more prominent in a column sparkline:

![Column Sparkline in Excel - axis variation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20104'%3E%3C/svg%3E)

In the above column sparkline, it may look like the Jan value is close to 0.

To adjust this, you can change the axis in the sparklines (make it start at a specific value).

Here is how to do this:

1.  Select the cell with the sparkline(s).
2.  Click on the Sparkline Tools Design tab.
3.  Click on the Axis option.![Axis Option in Excel Sparklines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20199'%3E%3C/svg%3E)
4.  In the drop-down, select Custom Value (in the Vertical Axis Minimum Value Options).![Custom Value in Axis Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20488'%3E%3C/svg%3E)
5.  In the Sparkline Vertical Axis Settings dialog box, enter the value as 0.![Custom Axis Value as 0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20132'%3E%3C/svg%3E)
6.  Click OK.

This will give you the result as shown below.

![Column Sparkline in Excel - custom axis value at 0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20105'%3E%3C/svg%3E)

By setting the customs value at 0, we have forced the sparkline to start at 0. This gives a true representation of the variation.

Note: In case you have negative numbers in your data set, it’s best to not set the axis. For example, if you set the axis to 0, the negative numbers would not be shown in the sparkline (as it begins from 0).

You can also make the axis visible by selecting the Show Axis option. This is useful only when you have numbers that cross the axis. For example, if you have the axis set at 0 and have both positive and negative numbers, then the axis would be visible.

![Show Axis option in sparklines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20486'%3E%3C/svg%3E)

Group & Ungroup Sparklines
--------------------------

If you have a number of sparklines in your report or dashboard, you can group some of these together. Doing this makes it easy to make changes to the whole group instead of doing it one by one.

To group Sparklines:

1.  Select the ones that you want to group.
2.  Click on the Sparklines Tools Design tab.
3.  Click the Group icon.![Group Sparklines in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20195'%3E%3C/svg%3E)

Now when you select any of the Sparkline that has been grouped, it will automatically select all the ones in that group.

You can ungroup these sparklines by using the Ungroup Option.

Deleting the Sparklines
-----------------------

You can not delete a sparkline by selecting the cell and hitting the delete key.

To delete a sparkline, follow the steps below:

1.  Select the cell that has the sparkline that you want to delete.
2.  Click the Sparkline Tools Design tab.
3.  Click the Clear option.

![Clear Sparklines from Excel Cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20198'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [Using Conditional Formatting in Excel (The Ultimate Guide + Examples)](https://trumpexcel.com/excel-conditional-formatting/)
    .
*   [How to Create a Heat Map in Excel.](https://trumpexcel.com/heat-map-excel/)
    
*   [Creating the Actual vs Target Chart in Excel.](https://trumpexcel.com/actual-vs-target-chart-in-excel/)
    
*   [Sparklines in Google Sheets](https://productivityspot.com/sparkline-google-sheets/)
    
*   [How to Rotate Text in Cells in Excel](https://trumpexcel.com/rotate-text-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “Excel Sparklines – A Complete Guide with Examples”
-----------------------------------------------------------------

1.  Fabulous, one question though – how do i highlight the marker on a sparkline?
    
    [Reply](https://trumpexcel.com/sparklines/#comment-14505)
    
2.  Excellent explanation about sparklines. Thank you very much.
    
    [Reply](https://trumpexcel.com/sparklines/#comment-12187)
    
3.  All of my sparklines are coming out as a flat line – even though there is variation in the data. I am wondering if the data needs to be in a particular format ?
    
    [Reply](https://trumpexcel.com/sparklines/#comment-11730)
    
4.  Great tutorial thanks. I am trying to add a marker to the last point of a Sparkline with data (not the end of the Sparkline which is blank) but it does not show up. Situation is a Sparkline for data for the 12 months of the year, but within the year (say July) the remainder of the year’s months are empty. I want to show the full year so one can get a sense of being part way through but then I suspect excel thinks the last data point is Dec and the marker is placed there and does not show up as blanks are not shown. In this situation I want a dynamic last point marker of July and next month of Aug etc, while ignoring the blanks months until year end. Anyone have a solution to this?
    
    [Reply](https://trumpexcel.com/sparklines/#comment-11200)
    
5.  İt is great tutorials. I am working for as a Athletic performance coach in a soccer clup. Therefore l would like to organize Gps data with excell heat map etc. Raw data formulas from opponent data etc.
    
    [Reply](https://trumpexcel.com/sparklines/#comment-10337)
    
6.  Awesome content like it  
    [https://www.govtstaffing.com/2018/07/ssc-gd-constable-vacancy-57000.html](https://www.govtstaffing.com/2018/07/ssc-gd-constable-vacancy-57000.html)
    
    [Reply](https://trumpexcel.com/sparklines/#comment-10246)
    
7.  [https://www.govtstaffing.com/](https://www.govtstaffing.com/)
    
    [Reply](https://trumpexcel.com/sparklines/#comment-10212)
    
    *   I like this notes and it very useful to me
        
        [Reply](https://trumpexcel.com/sparklines/#comment-14392)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/sparklines/#respond)

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