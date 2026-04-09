# Download Coronavirus data to Excel | Exceljet

**Source:** https://exceljet.net/articles/download-coronavirus-data-to-excel

---

[Skip to main content](https://exceljet.net/articles/download-coronavirus-data-to-excel#main-content)

[](https://exceljet.net/articles/download-coronavirus-data-to-excel#)

*   [Previous](https://exceljet.net/articles/excels-racon-functions)
    
*   [Next](https://exceljet.net/articles/tracking-covid-19-with-excel)
    

Download Coronavirus data to Excel
==================================

by Dave Bruns · Updated 21 Nov 2022

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/5916/download?token=2mjE4oRO)
 (22.29 KB)

![Download Coronavirus data to Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/covid-19_data.jpeg)

Summary
-------

This article provides examples of public Coronavirus data you can download to Excel with Power Query. Each example has a link, a screenshot to show what the data looks like in Excel after being imported, and an Excel workbook.

This page provides examples of public Coronavirus data you can download to Excel with [Power Query](https://exceljet.net/glossary/power-query)
. Each example has a link, a screenshot to show what the data looks like in Excel after being imported, and an Excel workbook.

The attached Excel workbooks include a working query, and each query returns data to an [Excel Table](https://exceljet.net/glossary/excel-table)
. You can refresh the data by right-clicking in the table and selecting "Refresh". When data has changed, you will see more recent data appear.

If you're new to Power Query, [this article](https://exceljet.net/articles/tracking-covid-19-with-excel)
 explains how to build a single query in more detail.

### Requirements

This project depends on Power Query, so you'll need Excel 2013 or later on Windows. On a Mac, you can refresh queries with Office 365 Excel, but you can't yet edit or create queries. 

Sample Coronavirus Data
-----------------------

_The purpose of this article is to show examples of how to get Coronavirus testing data into Excel. I can't vouch for the quality of the data. The links below provide more information about each website. The COVID Tracking Project provides a grade for each state._

_Excel workbooks are attached below the descriptions. To download fresh data, right-click inside the table and select "Refresh"._

_To inspect or edit a query, click Queries and Connections on the Data tab of the ribbon, then double-click on the query. [This article](https://exceljet.net/articles/tracking-covid-19-with-excel)
 explains how to build a single query in more detail._

### United States - current

Source: COVID Tracking Project (https://covidtracking.com/api)

This data contains the latest snapshot of Coronavirus testing data for the United States at the state level. It contains current totals only, not historical data. [This page](https://exceljet.net/articles/tracking-covid-19-with-excel)
 describes in detail how the query was created.

![COVID-19 US States Current](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20us%20states%20current.png "COVID-19 US States Current")

### United States  - historical

Source: COVID Tracking Project (https://covidtracking.com/api)

This data contains historical Coronavirus testing data for the United States at the state level. Each row in the data has a date.

![COVID-19 US States Historical](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20us%20states%20historical.png "COVID-19 US States Historical")

### Worldwide - current

Source: Worldometers (https://www.worldometers.info/coronavirus/)

This is an example of data retrieved directly from a table on a web page. In general, a web page is not as reliable as a data file, since the structure of a web page is more complex and might change.

_Note: you'll get an expression error if you try to refresh on a Mac. Power Query on Mac does not support web sources yet._

![COVID-19 World Current](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20world%20current%20worldometers.png "COVID-19 World Current")

### Worldwide - historical

Source: EU Open Data Portal (https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data)

This example shows how you can connect directly to an Excel workbook. Data Europa has a JSON api as well. Data is by country by day, and would be a good candidate for a [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
 to provide totals.

![COVID-19 World Historical](https://exceljet.net/sites/default/files/images/articles/inline/covid-19%20world%20historical%20eudata.png "COVID-19 World Historical")

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