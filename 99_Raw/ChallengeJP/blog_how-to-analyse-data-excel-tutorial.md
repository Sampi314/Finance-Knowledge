# How to Analyse Data in Microsoft Excel with Power Query and a Pivot Table | Tutorial

**Source:** https://www.challengejp.com/blog/how-to-analyse-data-excel-tutorial

---

How to Analyse Data in Microsoft Excel with Power Query and a Pivot Table
=========================================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   February 26, 2021January 3, 2026

Last Updated on January 3, 2026

This step-by-step tutorial will show you how to analyse data and Excel spreadsheets using Power Query and Pivot Tables. It will use an example of a data set to examine the popularity and length of songs by their release year. The analysis will use Spotify data, which you can access and download from the Kaggle website [here](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks)
.

Table of Contents

Toggle

**Step 1: Use Power Query Editor to Inspect Data**
--------------------------------------------------

Before you can analyse your data in Microsoft Excel, make sure to inspect it first. This will allow you to understand the data set’s structure and each record’s usefulness. You can then select and limit the data that you need to load into your spreadsheet.

Load the data into Power Query first to inspect and transform your CSV or Excel file. To import a CSV file:

1.  Create a new Excel workbook and click on the _Data_ tab.
2.  Click the _Get Data_ icon, then select _From File_ and finally, _From Text/CSV_.
3.  Choose the file you want to import. You will see a window with a preview of the data.
4.  Click on the _Transform Data_ button to load the data into the Power Query editor.

[![loading csv data into excel power query](https://www.challengejp.com/wp-content/uploads/2021/02/step1_load_csv_data_in_power_query.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step1_load_csv_data_in_power_query.png)

Step 1: Loading a CSV file into Power Query

We can divide our data set into two parts: categorical and quantitative. In our example, the categorical data will consist of _id, artist or track name_. Similarly, the quantitative data will consist of numerical values such as _tempo, volume or duration_.

**Step 2: Handling Large Excel Files in Power Query**
-----------------------------------------------------

Analysing big data sets in Microsoft Excel can be overwhelming, so we want to limit the size of the imported data. Our goal is to examine tracks released on or after the year 1960 and to analyse their popularity and duration. Consequently, we can cut our spreadsheet’s size by only keeping the records we are interested in.

First, let’s limit the number of columns. After loading the data into the Power Query editor, go to the _Home_ tab and click on _Choose Columns_. We want to analyse duration, popularity, and tempo metrics, so tick those columns. Also, keep the data that will allow you to identify and describe tracks, so select _id, name, year_, and _artists_.

[![transforming excel data with power query example](https://www.challengejp.com/wp-content/uploads/2021/02/step2_power_query_choose_columns-e1652087769258.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step2_power_query_choose_columns-e1652087769258.png)

Step 2: Choosing Columns in Power Query Editor

Since our analysis will focus only on data released after 1960, I will exclude any records released before that year. To filter the row selections, click on the filter arrow next to the header name. Then, select _Number Filters_ and click on _Greater Than or Equal To…._ Finally, type the value 1960 in the _Filter Rows_ and click _OK_.

To load the data, click on the _Close & Load_ icon at the upper left corner of the Power Query editor. Your spreadsheet will now populate the data with a table containing limited rows and columns. Head to the _Data_ tab to explore how to [filter](https://www.excel-easy.com/data-analysis/filter.html)
, group and [sort](https://www.howtogeek.com/679749/how-to-sort-by-date-in-microsoft-excel/)
 your Excel data table.

**Step 3: Transforming and Converting Data with Power Query**
-------------------------------------------------------------

Instead of using Excel formulas to calculate new values, you can add a custom column in Power Query. We aim to use the existing data and convert it into new records. Calculating new data in Power Query will make the analysis faster and our spreadsheet more robust.

To add a new column in your existing Power Query, go to the _Query_ tab and click on the _Edit_ button. This will take you back to the Power Query editor. Then, click on the _Custom Column_, which you will find in the _Add Column_ tab.

We aim to convert the ‘Duration\_ms’ column from milliseconds to minutes. Go to the _Available Columns_ area, where you will see a list of all available column names. Then, double-click on the ‘duration\_ms’ field to add it to the _Custom column formula_ box and type in ‘/ 60000’. Lastly, type ‘Duration\_mins’ in the _New column name_ box and click _OK_.

[![creating a custom column in power query example](https://www.challengejp.com/wp-content/uploads/2021/02/step_3_power_query_custom_column-e1652087760245.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_3_power_query_custom_column-e1652087760245.png)

Step 3: Creating a Custom Column in Power Query Editor

Before moving on, we want to create one more custom column with unique descriptive data for each track:

1.  Click on the _Add Column_ icon again and double-click on the ‘artists’ field.
2.  Type in ‘&” “&’ and double click on the ‘name’ field. This will combine text from the two columns and separate them by a space.
3.  Type ‘artists+track’ in the _New column name_ box to label the new record and click _OK_.

Go back to the _Home_ tab and click on the _Close & Load_ icon. You should see an Excel table refreshed with the new data.

**Step 4: Set Up a Pivot Table in Microsoft Excel**
---------------------------------------------------

Pivot tables allow you to quickly analyse your spreadsheets, aggregate values and group them into categories.

To create a new Pivot Table:

1.  Go to your spreadsheet and select all data in the table.
2.  Click on the _Pivot Table_ icon in the _Insert_ tab.
3.  Select the _New Worksheet_ option in the _Create PivotTable_ window and then click _OK_.

You will now see a spreadsheet with an empty pivot table to the left and _PivotTable Fields_ to the right.

Using our data example, we want to examine the track names by their release date. Drag the year from the PivotTable fields to the Rows area to display year values. You will find the _Rows area_ at the lower-right corner, below the list of the available fields. Then, drag the ‘artists+name’ and place it below the ‘year’ field.

To change the Pivot Table’s layout, click on the _Design_ tab at the top of the Excel workbook and click on the _Report Layout_. Then, select the _Show in Tabular Form_ option to change the Pivot Table’s layout.

Your pivot table should now display rows containing year values and corresponding artists’ and tracks’ names to their right. Adjust the width of the columns to fit the Pivot Table onto the screen.

[![setting up a pivot table to analyse excel data](https://www.challengejp.com/wp-content/uploads/2021/02/step_4_pivot_table_report_layout-e1652087749583.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_4_pivot_table_report_layout-e1652087749583.png)

Step 4: Setting up a Pivot Table Layout

Tip: To preserve the column width setup, right-click on the PivotTable, select _Pivot Table Options…_ and then untick the A_utofit column widths on the update_ checkbox.

**Step 5: Analysing Excel Data with Pivot Tables**
--------------------------------------------------

To complete the data analysis, go to the _PivotTable Fields_ area and drag the data into the _Values_ area below. Our task is to examine the popularity of each track, so we will use the Popularity field as the measure. Hence, drag the field into the _Values_ area. Notice the ‘Sum of Popularity’ column added in the Pivot Table. You may need to [adjust the column widths](https://www.howtogeek.com/270296/how-to-set-row-height-and-column-width-in-excel/)
 to fit the table onto the screen.

We want to display the numbers as averages, so let’s change the value settings. Return to the _Values_ area and click on the _Sum of Popularity_ field. Then, choose _Value Field Settings…_ and you will see a _Summarize Values By_ window. Finally, select _Average_ from the list of options and click _OK_.

Our goal is only to analyse the most popular tracks for every release year. To limit the number, click on the filter arrow next to the ‘artists+track’ header. Then, select _Value Filters_ and click on the _Top 10…_ In the _Top 10 Filter_ window, change the value from ’10’ to ‘1’.

[![pivot table top 10 values example](https://www.challengejp.com/wp-content/uploads/2021/02/step_5_pivot_table_top10_example-e1652087802536.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_5_pivot_table_top10_example-e1652087802536.png)

Step 5: Using Top 10 Value Filter in Pivot Table

Finally, go to the _Design_ tab, click the _Subtotals_ icon and select _Do Not Show Subtotals_. Then, click the _Grand Totals_ icon and select _Off for Rows and Columns_. You will now see a list of only the most popular tracks grouped by their release year.

**Step 6: Aggregating Data in Pivot Table**
-------------------------------------------

One advantage of using a Pivot Table to analyse Excel data is the ease of grouping values. As an example, we will group our year values into ten-year intervals. We will then examine the most popular songs by the decade in which they were released.

To aggregate the data, right-click on one of the values in the ‘Year’ column and select the _Group…_ option. Then, in the _Grouping_ window, type in ‘1960’ as your starting value and ‘2020’ as the end. To aggregate the year values into ten-year intervals, type ’10’ in the _by_ field. Lastly, click _OK_, and you will see the track data collapsed into ten-year buckets, for instance, ‘1960-69’.

[![analysing and grouping excel data with pivot table example](https://www.challengejp.com/wp-content/uploads/2021/02/step_6_pivot_table_grouping_data-e1652087791236.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_6_pivot_table_grouping_data-e1652087791236.png)

Step 6: Grouping Pivot Table Numbers by Range

Let’s expand our analysis to include the five most popular songs from every decade:

1.  Click on the filter arrow next to the ‘artist+track’ header and select _Top 10…_ from the _Value Filters_ menu.
2.  Change the value from 1 to 5 in the _Top Filter_ window and click _OK_.
3.  Sort the values in descending order to show the most popular tracks at the top of each period.

**Step 7: Analyse the Results and Cleanse Data**
------------------------------------------------

Our initial data analysis suggests that the most popular songs are tracks related to winter tunes. That doesn’t seem right. After looking at the source data description, we realised the popularity measure was calculated in December. As a result, the overall number of downloads and the calculation of popularity were skewed towards holiday tunes. To rectify that, we want to exclude the data from our analysis.

We don’t want to remove any data from the Excel table, so instead, let’s use the Pivot Table’s functionalities. To clean and filter out data, drag the ‘name’ field into the _Filters_ area. Then, click the arrow next to the ‘All’ value in cell B1. You will see the list of unique values from the name column.

Tick the _Select Multiple items_ checkbox and click on the _Search_ field at the top of the box. Type in ‘snow’ and then untick the _(Select All Search Results)_ checkbox. As a result, you will now see the names of all tracks containing ‘snow’ in their titles. Untick the _Add current selection to filter_ checkbox and then click _OK_. Finally, repeat the same step for other search terms such as ‘Christmas’, and ‘sleigh’ until your name list looks clean.

[![pivot table filter excluding data example](https://www.challengejp.com/wp-content/uploads/2021/02/step_7_pivot_table_filtering_data-e1652087740547.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_7_pivot_table_filtering_data-e1652087740547.png)

Step 7: Filtering and Excluding Data in a Pivot Table

**Step 8: Using a Pivot Chart to Visualise Data**
-------------------------------------------------

Pivot Table helps analyse Excel data and allows you to visualise it. So, let’s expand our data analysis and examine how the average duration of songs evolved over the decades. To save time, we will use the Pivot Table created in the previous steps as a template.

First, remove some of the values and fields from the Pivot Table. Drag and remove the ‘artists+track’ field from the _rows_ area. Then, remove the _Average of Popularity_ field in the _Values_ area. Consequently, the Pivot Table should now be showing a list of decades only.

To display average duration values, drag the ‘duration\_mins’ field into the V_alues_ area. The ‘duration\_mins’ was the Power Query’s custom column we created earlier. Then, click on the field name and choose _Value Field Settings_. Finally, select _Average_ from the list of options in the _Summarize value field by_ window.

To insert a chart, go to the _PivotChart Design_ tab and click the _PivotChart_ icon. I have chosen the horizontal bar chart to visualise and quickly compare the data over time. Right-click on the chart to change the layout, style or add new elements. Lastly, untick the gridlines checkbox in the _View_ tab to remove any background distractions.

[![analysing excel data with pivot chart](https://www.challengejp.com/wp-content/uploads/2021/02/step_8_analysing_excel_data_pivot_chart-e1652087728185.png)](https://www.challengejp.com/wp-content/uploads/2021/02/step_8_analysing_excel_data_pivot_chart-e1652087728185.png)

Step 8: Analysing Excel Data with Pivot Chart

**Summary: Using Power Query and Pivot Tables to Analyse Data**
---------------------------------------------------------------

This tutorial has shown how to analyse data in Microsoft Excel. We used the Power Query to handle a large data file and applied filters to limit the number of imported rows and columns. We also created new custom columns to transform the existing data.

With the data loaded into an Excel table, we used a Pivot table to analyse it. By aggregating and filtering the data, we could examine songs’ popularity by the year or the decade of their release.

To visualise the data, we used a pivot table graph. Using a horizontal bar chart helped us to analyse the data over time. Lastly, we learned how to use a filter to adjust the results without removing any source data.

To practice analysing data, you can download the original data source from [this Kaggle’s page](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks)
.

Get in Touch
------------

_[![challengejp_data_analyst](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, my name is Jacek and I love spreadsheets! I h__ope you’ve enjoyed reading this tutorial as much as I did writing it! If you have any questions about Microsoft Excel and data analysis, don’t hesitate to [get in touch](https://www.challengejp.com/contact/)
._

_[**Explore my other tutorials**](https://www.challengejp.com/blog/)
 to learn more about data or financial analysis. If you need further support, find out about my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and **[Data Analytics Services](https://www.challengejp.com/services/data-analytics/)
**._

Learn More
----------

[Analyze and Forecast Customer Churn and Revenue](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)
 – Build a churn/retention model in Microsoft Power BI using DAX, cohort analysis, and interactive forecasts.

[Power BI Consolidated P&L & Forecast Tutorial](https://www.challengejp.com/blog/power-bi-consolidated-pl-forecast-tutorial-template/)
 — learn how to merge data from multiple entities, apply FX conversions, and create a complete forecasting model in Microsoft Power BI.

[Your First Steps in Microsoft Excel – Beginner’s Crash Tutorial](https://www.challengejp.com/blog/learn-excel-beginner-tutorial/)
 – This post will take you through the basic functionalities and refresh your knowledge of spreadsheets.

[How to Use Python and Pandas for Data Consolidation and Transformation](https://www.challengejp.com/blog/python-excel-data-consolidation-transformation/)
 – This introductory tutorial will introduce you to Python and show you how to write scripts to analyse and manipulate your CSV or Excel data files.

[How to Visualise Data in Tableau](https://www.challengejp.com/blog/how-to-visualise-data-tableau-tutorial/)
 – If you want to learn more about data visualisation tools, this tutorial will take you through the basics of Tableau and show you how to transform a simple CSV file into an interactive dashboard.

[How to Use Cohort Analysis to Calculate Retention and Churn Rate in Microsoft Excel](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/)
 – This step-by-step tutorial will guide you through an example of applying data analysis skills in practice.

[Learn How to Become a Self-Taught Data Analyst](https://www.challengejp.com/blog/learn-to-become-data-analyst/)
 – Here, you will find a few practical tips and links to resources, which I found useful while learning to become a data analyst.

Tags:[Data Analytics](https://www.challengejp.com/blog/tag/data-analytics/ "Data Analytics")
[Excel Tutorial](https://www.challengejp.com/blog/tag/excel-tutorial/ "Excel Tutorial")

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.