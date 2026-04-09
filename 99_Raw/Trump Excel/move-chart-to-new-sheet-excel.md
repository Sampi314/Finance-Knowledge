# How to Move Chart to New Sheet in Excel? 2 Easy Ways!

**Source:** https://trumpexcel.com/move-chart-to-new-sheet-excel

---

[Skip to content](https://trumpexcel.com/move-chart-to-new-sheet-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/move-chart-to-new-sheet-excel/#below-title)

By default, when you insert a chart in Excel, it’s created in the same worksheet where you have the source dataset.

But in many cases, you may want to move the chart from the sheet where it’s created to another worksheet (or a chart sheet – which has nothing but the chart).

This can be useful when you’re [creating dashboards](https://trumpexcel.com/creating-excel-dashboard/)
, where the data can be scattered throughout the workbook, but you can get all the important charts in the sheet that has the dashboard.

When it comes to moving a chart to another sheet, you can:

*   Move it as a chart object from one sheet to another
*   Move the chart to a chart sheet, where you have only the chart

In this tutorial, I will show a step-by-step process to move the chart to a new sheet in Excel.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/move-chart-to-new-sheet-excel/#)

Chart Object vs Chart Sheet
---------------------------

Before I get into the steps of moving a chart to a new sheet in excel, let me quickly explain the **difference between a chart object and a chart sheet**.

When you create a chart in a worksheet that already has the data, what you get is a chart object (which is a chart that sits above your worksheet and you can move it around like an object).

On the contrary, a chart sheet is a completely different sheet that is dedicated to a single chart. So when you move an existing excel chart into a new chart sheet, you would only have the chart in that sheet (and there won’t be any cells or tables like a regular worksheet).

In this tutorial, I will show you how to move an existing chart into a new worksheet (as an object) or to a new chart sheet.

Moving Chart to a New Worksheet (or Another Existing Sheet)
-----------------------------------------------------------

Suppose you have the data set as shown below and you have created a chart using it.

![Data with Chart that needs to be moved](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20325'%3E%3C/svg%3E)

Now, I want to move this chart to a different worksheet in the same workbook (this worksheet – to which I want to move the chart – should already exist in the workbook).

Below are the steps to do this:

1.  Click on the chart object that you want to move
2.  Click on the Chart Design tab (this is a contextual tab that only appears when you select any chart)

![Click on Chart Design](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20171'%3E%3C/svg%3E)

3.  In the Location group, click on the ‘Move Chart’ icon

![Click on Move Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20168'%3E%3C/svg%3E)

4.  In the Move Chart dialog box, make sure ‘Object in’ option is selected.

![Select Object in option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20237'%3E%3C/svg%3E)

5.  From the drop-down, select the sheet where you want to move the selected chart. In this example, I am moving the chart to a sheet named ‘Summary’

![Select the sheet to which you want to move the chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20237'%3E%3C/svg%3E)

6.  Click OK

The above steps would move the selected chart from the existing worksheet to the worksheet you selected in Step 5.

In case you want to move this chart to a completely new blank worksheet, you will first have to add that new worksheet and then repeat the process (so that the name of this new worksheet is shown in Step 5)

Note that the above steps would remove the chart from the source worksheet and move it to the destination worksheet.

In case you want to keep the chart in the source worksheet and get a copy of it in the new worksheet, you need to first create a copy of the chart (using a simple Control C and Control V), and then move one of these charts to the destination worksheet.

### Move Chart by Copy Pasting

Another really quick way to move a chart to a new worksheet is by simply copying the chart and pasting it in the new worksheet.

Doing this would create a copy of the chart in the new worksheet. So if you want to completely move the chart and not have it where you have the data, you can simply keep the copy and delete the original chart (or use Cut-Paste instead of Copy-Paste).

Below are the steps to move a chart using simple copy-paste:

1.  Create a [new sheet](https://trumpexcel.com/insert-new-worksheet-excel/)
     where you want to move the chart (if you don’t have that already)
2.  Activate the sheet where you have the chart that you want to move
3.  Right-click on the chart and select Copy (or select the chart and use Control + C)

![Right click and copy the chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20378'%3E%3C/svg%3E)

4.  Go to the Sheet where you want to get a copy of the chart
5.  Right-click and in the [Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
     option, click on the ‘Use Destination Theme’ icon (or use the keyboard shortcut Control + V to paste)

![Right click and then click on Paste while keeping destination formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20357'%3E%3C/svg%3E)

The above steps would create a copy of the chart in the current worksheet.

Moving a Chart to a New Chart Sheet
-----------------------------------

If you want to move a specific chart into its own chart sheet (which is meant to contain nothing else but a chart), you can use the below steps:

1.  Click on the chart object that you want to move to a new chart sheet
2.  Click on the Chart Design tab

![Click on Chart Design](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20171'%3E%3C/svg%3E)

3.  In the Location group, click on the ‘Move Chart’ icon

![Click on Move Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20168'%3E%3C/svg%3E)

4.  In the Move Chart dialog box, select ‘New Sheet’

![Click on New Sheet option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20237'%3E%3C/svg%3E)

5.  Give a [name to the sheet](https://trumpexcel.com/get-sheet-name-excel/)
     where this chart would be moved (or keep the default Chart1 name)

![Give a name to the Chart Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20255'%3E%3C/svg%3E)

6.  Click OK

The above steps would remove the chart from the current worksheet, create a new chart sheet, and move the chart to this new chart sheet.

![New Sales Chart Sheet is inserted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20360'%3E%3C/svg%3E)

All the customizations that you can do with a chart object can also be done with a chart that’s in the chart sheet (except resizing and moving around the chart).

Note that you can also move other charts into this newly inserted Chart Sheet, but the one that you inserted first would remain in the background and all the other charts would be treated as an object that floats over that chart.

Moving All the Charts in the Workbook to a New Sheet
----------------------------------------------------

While the manual way of moving a chart to another worksheet or chart sheet is quite easy, it could become quite tedious in case you have a lot of charts that you want to move.

Imagine 20 sheets with one chart in each sheet that you want to move to the summary or dashboard sheet.

In such a scenario, you can use a [simple VBA code](https://trumpexcel.com/excel-vba/)
 that would go through all the charts in your workbook and move these two into the specified worksheet.

Below is the [VBA code](https://trumpexcel.com/excel-macro-examples/)
 that would move all the charts from all the worksheets to one destination worksheet (in this example, it’s the sheet with the ‘Dashboard’)

'Code Developed by Sumit Bansal from https://trumpexcel.com
Sub MoveCharts()
Dim chartObject As Object
Dim SheetwithCharts As Worksheet
For Each SheetwithCharts In Application.ActiveWorkbook.Worksheets
If SheetwithCharts.Name <> "Dashboard" Then
For Each chartObject In SheetwithCharts.ChartObjects
chartObject.Chart.Location xlLocationAsObject, "Dashboard"
Next chartObject
End If
Next SheetwithCharts
End Sub

In the above code, I have hard-coded the name of the destination sheet where the charts would be moved (the destination sheet name used is ‘Dashboard’).

In case you want to move these charts to any other worksheet, just replace the word Dashboard with the name of that worksheet.

Below are the steps to run this VBA macro code in Excel:

1.  Click the Developer tab in the ribbon (if you can’t see the Developer tab, [read this guide to enable it](https://trumpexcel.com/excel-developer-tab/)
    )

![Click the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20166'%3E%3C/svg%3E)

2.  Click on Visual Basic icon. This will open the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    

![Click on Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20131'%3E%3C/svg%3E)

3.  In the Project Explorer, select any object of the workbook that has the charts (if you don’t see Project Explorer, click on ‘View’ option in the menu and then click on Project Explorer)

![View Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20294%20498'%3E%3C/svg%3E)

4.  Click the ‘Insert’ option in the menu and then click on ‘Module’. This will insert a new module for the workbook

![Insert a Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20310'%3E%3C/svg%3E)

5.  Copy and paste the above code in the Module code window (you can open the module code window anytime by double-clicking on the module name in the Project Explorer)

![Copy paste the code to the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20276'%3E%3C/svg%3E)

6.  Select any line in the code
7.  Press the F5 key (or click the green play button in the toolbar)

![Run the Macro to move all charts to a specified sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%2092'%3E%3C/svg%3E)

The above steps would move all the charts from all the sheets in the workbook into the sheet named ‘Dashboard’.

**How do the Code works – A Simple Explanation**

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through all the worksheets in the workbook. It then uses an if condition to check whether the name of the worksheet is ‘Dashboard’ or not.

If the name of the worksheet is ‘Dashboard’, nothing happens, and in case it’s not, then the code goes through each chart in that worksheet (this is again done using a For Next loop).

Each chart in the sheet is then moved to the dashboard worksheet (and also removed from the sheet where it originally existed).

**Pro Tip**: I strongly recommend you create a copy of the original file before you run this code (as the changes done by the VBA code can not be undone)

So these are some simple ways that you can use to move a chart to any specific sheet in the workbook (or to a new chart sheet).

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Save Excel Charts as Images (save as PNG, JPG, BMP)](https://trumpexcel.com/save-excel-charts-as-images/)
    
*   [How to Create a Dynamic Chart Range in Excel](https://trumpexcel.com/dynamic-chart-range/)
    
*   [How to Create Dynamic Chart Titles in Excel](https://trumpexcel.com/dynamic-chart-titles-in-excel/)
    
*   [How to Insert New Worksheet in Excel (Shortcuts)](https://trumpexcel.com/insert-new-worksheet-excel/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [How to Copy Chart (Graph) Format in Excel](https://trumpexcel.com/copy-chart-format-excel/)
    
*   [Move Pivot Table to Different Worksheet or Workbook](https://trumpexcel.com/move-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/move-chart-to-new-sheet-excel/#respond)

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