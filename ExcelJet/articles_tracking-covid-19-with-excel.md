# Tracking COVID-19 with Excel | Exceljet

**Source:** https://exceljet.net/articles/tracking-covid-19-with-excel

---

[Skip to main content](https://exceljet.net/articles/tracking-covid-19-with-excel#main-content)

[](https://exceljet.net/articles/tracking-covid-19-with-excel#)

*   [Previous](https://exceljet.net/articles/download-coronavirus-data-to-excel)
    
*   [Next](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

Tracking COVID-19 with Excel
============================

by Dave Bruns · Updated 21 Nov 2022

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/5913/download?token=K1xTCWlJ)
 (22.29 KB)

![Tracking COVID-19 with Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Covid-19_tracking.jpeg)

Summary
-------

A quick example of how to track testing for COVID-19 using Excel and publicly available data. In this project, the data is fetched and "shaped" with Power Query, then dropped back into Excel, where it can be refreshed with a single click.

![Tracking COVID-19 testing with Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/covid-19%20tracking%20in%20Excel.png?itok=Us4R2NfU "Tracking COVID-19 testing with Excel")

_Above: Tracking public COVID-19 testing data in Excel with Power Query_

In this article, I want to share a quick example of how to track testing for COVID-19 using Excel and publicly available data. This is a bare bones tutorial, focused only on the basics of connecting Excel with publicly available data. 

The end result is a simple Excel table that shows the most recent testing data by state. The data is fetched and "shaped" with [Power Query](https://exceljet.net/glossary/power-query)
, then dropped back into Excel, where it can be refreshed with a single click. The approach is general and can be used with all kinds of public data. The complete Excel file is attached below for reference.

### The data

For this example, we're going to use data from the COVID tracking project website. [The COVID Tracking Project](https://covidtracking.com/)
 collects data at the U.S. State level on testing for coronavirus, SARS-CoV-2. The data is not perfect, and varies state-by-state. You can read more about it on the website. The API for requesting data is [explained here](https://covidtracking.com/api/)
. In this example, we are fetching "States Current Values" data which, as of this writing contains 19 columns, most of which we discard.

### Requirements

This project depends on Power Query, so you'll need Excel 2013 or later on Windows. On the Mac, you can _refresh_ queries with Office 365 Excel, but I don't think you can edit or create queries yet? I'll update when I have better info.

### Getting the data into Excel

The best tool for the job is Power Query. Power Query is part of Microsoft's BI suite. In a nutshell, Power Query is a tool for fetching, cleaning, and shaping data.

If you are new to Power Query, be aware that it has a vast feature set and an intimidating interface. Even if you spend a lot of time in Excel, you are going to feel like you've landed in an alien world. Familiar, yet distinctly different.

Never fear, we are going to keep things as simple as possible. There are many ways this example can be improved or embellished once you get things working.

### High-level overview

To orient you, here are the high level steps we are going to perform:

1.  Create new excel workbook
2.  Create a new query to fetch data
3.  Edit query to shape data
4.  Load data back to Excel Table
5.  Add formulas as desired

The first two steps happen in Excel. The last two steps are done in power query. Once you have the query set up, you can right-click inside the table and select refresh. Fresh data will be collected, and the data will be shaped according to the steps defined in the query. 

### Steps to create the query

_April 2 - the data for this project has been changing as more columns are tracked in the same file. The steps below need to be updated slightly, but the query in the attached Excel workbook is current._

These are the steps I used to create the query that fetches data from the tracking website.

1.  Click Data > Get Data  > From web  
      
    ![Click From Web on the Data tab of the ribbon](https://exceljet.net/sites/default/files/images/articles/inline/get%20data%20from%20web.png "Click From Web on the Data tab of the ribbon")  
     
2.  Enter the url: https://covidtracking.com/api/states.csv and click OK  
      
    ![Click From Web - fill in URL](https://exceljet.net/sites/default/files/images/articles/inline/get%20data%20from%20web%20dialog.png "Click From Web - fill in URL")  
     
3.  Click the Transform Data button to launch Power Query:  
      
    ![Click the Transform Data button](https://exceljet.net/sites/default/files/images/articles/inline/click%20the%20transform%20data%20button.png "Click the Transform Data button")  
     
4.  Power Query will automatically add three steps: Source, Promote Headers and Change type. If you select a step, you can see what it does.   
      
    ![Automatic query steps](https://exceljet.net/sites/default/files/images/articles/inline/automatic%20query%20steps.png "Automatic query steps")  
     
5.  Remove the automatic "Change Type" step. Hover and click on the "X" on the left. We will manually change type again below to make the query more resilient.  
     
6.  Control-click to select five columns: state, positive, death, dateModified, totalTestResults. Then, right-click on a select column and choose "Remove other columns".  
      
    ![Right-click, select Remove Other Columns](https://exceljet.net/sites/default/files/images/articles/inline/remove%20other%20columns.png "Right-click, select Remove Other Columns")  
      
     
7.  For each column select the "ABC", and Change Type: state (text), positive (whole number), death (whole number), dateModified (date time), totalTestResults (whole number).  
      
    ![Change Type for each column](https://exceljet.net/sites/default/files/images/articles/inline/change%20type%20for%20each%20column.png "Change Type for each column")  
     
8.  Drag to reorder columns: state, positive, death, dateModified, totalTestResults.  
      
    ![Click and drag columns to reorder](https://exceljet.net/sites/default/files/images/articles/inline/click%20and%20drag%20columns%20to%20reorder2.png "Click and drag columns to reorder")  
     
9.  Rename columns to: state, positive, death, modified, total. Double-click header to rename columns.  
      
    ![Double-click header to rename columns](https://exceljet.net/sites/default/files/images/articles/inline/double%20click%20header%20to%20rename.png "Double-click header to rename columns")  
     
10.  Sort data by the "positive" column in descending order.  
      
    ![Sort data by the "positive" column in descending order](https://exceljet.net/sites/default/files/images/articles/inline/sort%20descending%20by%20positive.png "Sort data by the "positive" column in descending order")  
     
11.  Rename Query to "states":  
      
    ![Rename query to "states"](https://exceljet.net/sites/default/files/images/articles/inline/rename%20query2.png "Rename query to "states"")  
     
12.  Verify you have five columns of data like this:  
      
    ![Verify you have five columns of data](https://exceljet.net/sites/default/files/images/articles/inline/verify%20data2.png "Verify you have five columns of data")  
     
13.  Click Close and Load button on Data tab of ribbon.  
      
    ![Click the close and load button](https://exceljet.net/sites/default/files/images/articles/inline/click%20the%20close%20and%20load%20button.png "Click the close and load button")  
     
14.  The data will end up in an Excel Table called "states"

### Refreshing data

To fetch the latest data, right-click in the table and select "Refresh". 

![Right click table and select refresh](https://exceljet.net/sites/default/files/images/articles/inline/right%20click%20table%20and%20select%20refresh.png "Right click table and select refresh")

Power Query will pull down a fresh set of source data, run through the steps defined above, and deliver the result back to Excel. The screens below show the data on March 26 (before refresh, and March 27 (after refresh).

![Data before refresh on March 26](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20states%20-%20before%20refresh.png "Data before refresh on March 26")

![Data after refresh on March 27](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20states%20-%20after%20refresh.png "Data after refresh on March 27")

### Back in Excel

Once the data is in an Excel table, I added a column called "pos %" that calculates what percentage of total tests are positive with this formula:

    =[@positive]/[@total] // calculate percent positive
    

This is just something I was curious about. It could be added in Power Query instead (before loading to Excel) but to keep things simple, the formula was added manually in Excel. Since it lives in an [Excel Table](https://exceljet.net/glossary/excel-table)
, it stays up to date when date changes.

Then I added formulas to summarize the data:

    =SUM(states[total]) // J4
    =SUM(states[positive]) // J5
    =J5/J4 // J6
    =SUM(states[deaths]) // J7
    =MAX(states[modified]) // J9
    =MIN(states[modified]) // J10
    

Note: most of these formulas use [structured references](https://exceljet.net/glossary/structured-reference)
, the formula syntax for Excel Tables.

### How to edit the query

1.  Click Queries and Connections on the Data tab of the ribbon  
      
    ![Ribbon > Data tab > Queries and Connections](https://exceljet.net/sites/default/files/images/articles/inline/ribbon%20queries%20and%20connections.png "Ribbon > Data tab > Queries and Connections")  
     
2.  Double click the "states" query to edit  
      
    ![Double-click query in Queries and Connections](https://exceljet.net/sites/default/files/images/articles/inline/queries%20and%20connections.png "Double-click query in Queries and Connections")  
     

### More data

Here are a [few more Coronavirus datasets](https://exceljet.net/articles/download-coronavirus-data-to-excel)
 with sample files you can try out.

### Notes

1.  Many of the articles I've read about COVID-19 warn against focusing on testing only, because it can distract from the more serious problem, [exponential spread](https://www.washingtonpost.com/graphics/2020/world/corona-simulator/?itid=pm_pop)
     of a contagious disease. To be clear, this article's only purpose is to show an example of how to get public data into Excel.
2.  I've posted more examples of Coronavirus datasets you can download [in this article](https://exceljet.net/articles/download-coronavirus-data-to-excel)
    .

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)