# How to Visualise Data in Tableau | Step-by-Step Tutorial | ChallengeJP

**Source:** https://www.challengejp.com/blog/how-to-visualise-data-tableau-tutorial

---

How to Visualise Data in Tableau
================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   April 21, 2021February 9, 2026

Last Updated on February 9, 2026

This tutorial will introduce you to Tableau and data visualisation. It will use an example of data downloaded from Destasis, Germany’s Federal Statistical Office, to visualise Germany’s 2020 International Trading Partners by Turnover, Export and Import values. You can access the original and the latest data from [Destatis.de](https://www.destatis.de/EN/Themes/Economy/Foreign-Trade/Tables/order-rank-germany-trading-partners.html)
 or download its transformed version in a CSV format [here](https://www.challengejp.com/wp-content/uploads/2021/04/germany_trade_dataset.csv)
.

Table of Contents

Toggle

**Step 1: Import and Inspect Data File**
----------------------------------------

Before you can start visualising data, import the data file. Tableau makes it very easy by listing possible data sources on the left side of the first screen. As our data file is in a CSV format, click on the _Text file_ source and select the data file you want to import.

After a while, you should be able to see a data file extract with the following three columns:

*   **Country:** An origin/destination from/to which Germany imports/exports its goods
*   **Activity:** A category of trade, e.g. Imports, Exports or Turnover
*   **Eur(000):** The value of the trade activity expressed in 000s of Eur.

[![importing germany trade csv file into tableau example](https://www.challengejp.com/wp-content/uploads/2021/04/step1_tableau_import_csv_file-e1619087342256.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step1_tableau_import_csv_file-e1619087342256.png)

Step 1: Example of Importing a CSV File in Tableau

After you have inspected and understood the data set better, it’s time to use Tableau to visualise the data on a map.

**Step 2: Set Up Your First Tableau Sheet**
-------------------------------------------

To set the data visualisation, click on the Sheet 1 tab at the bottom of the screen. You should now see an empty Tableau workspace divided into the following sections:

*   **Sidebar:** The left part of the screen where you can find the names of the data fields. Notice that most labels correspond to the columns in the original data set. You should also see additional fields like _Latitude_ and _Longitude_. Tableau automatically generates them, and they will help display the Countries in the correct position on a map.
*   **Marks:** This is where you can drop one of the data fields to start your visualisation and analysis. We will primarily use the _Color_ and _Text_ marks, but you can drop the fields onto others to see how it affects your visualisation.
*   **Workspace:** That’s the largest area of the screen. Notice _Columns_ and _Rows_ at the top of the screen. We will use them in the latter part of this tutorial to create a Tableau table.
*   **Filters:** Here, you can drop one of the Tableau fields to limit the number of values displayed and set conditions for their selection.

[![setting up a new tableau data visualisation sheet](https://www.challengejp.com/wp-content/uploads/2021/04/step2_tableau_new_sheet_create-e1619087376342.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step2_tableau_new_sheet_create-e1619087376342.png)

Step 2: Example of Setting Up a New Sheet in Tableau

Note how Tableau assigns different colours to the fields. For simplicity, assume that the blue labels in our example correspond to descriptive values such as labels (e.g. country name), and green ones correspond to measure values (e.g. trade value). To learn more about the difference between green and blue fields, visit [this Tableau’s webpage](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles.htm)
.

**Step 3: Use Tableau Map to Visualise Geographic Data**
--------------------------------------------------------

Drag and drop the Country field into the middle of the empty workspace to display your Tableau data on a map. After a short moment, you should see a map with several dots spread across it. While this is a good start, you want to make the visualisation more meaningful. Drag the _EUR(000)_ field from the sidebar and then drop it onto the _Color_ mark. Consequently, you should see that Tableau has now filled the map with different colours.

Upon inspection of the map, you should notice that the colour’s shade corresponds to the trade’s total value. For example, dark blue relates to the highest numbers. Therefore, you can already see that the biggest of Germany’s trading partners in 2020 were China, the Netherlands, the United States, France and Poland.

[![setting up data map visualisation in tableau example](https://www.challengejp.com/wp-content/uploads/2021/04/step3_tableau_map_visualisation_set_up_example-e1619087160715.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step3_tableau_map_visualisation_set_up_example-e1619087160715.png)

Step 3: Example of Setting Up a Map Visualisation in Tableau

Notice that some of the countries on the map, for example, Libya, are blank. There is also a “21 unknown” text displayed at the lower right corner of the Tableau map. The missing colour and the notification indicate a mismatch between the country names from the original data file and what Tableau would expect to see.

To assign the missing locations to the correct value, go to Tableau’s Map menu and click _Edit Locations…_ You should now see a list of territories with _Unrecognised_ red text in the corresponding Matching Location column. Click on one of them and start typing the country name to find the right match. Once you have finished, click OK, and you should see that the map now displays the locations as expected.

**Step 4: Add Filters to Improve Your Data Visualisation**
----------------------------------------------------------

Let’s use a filter to add an ability to visualise data based on a selected value. To add a filter in Tableau and limit the selection to just one category:

1.  Go to the sidebar and drag a relevant field (in our example, this will be _Activity_) and drag it into the Filters pane.
2.  Right-click on its name and select the _Show Filters_ option. You should see the list of activity names on the right of the screen.
3.  Click on the black arrow to the right of the filter title and then choose _Single Value (dropdown)_.

[![setting a single value dropdown filter in tableau](https://www.challengejp.com/wp-content/uploads/2021/04/step4_tableau_filter_single_value_dropdown_example-e1619089320265.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step4_tableau_filter_single_value_dropdown_example-e1619087186394.png)

Step 4: Example of Creating a Single Value Drop-Down Filter in Tableau

Consequently, you should see a drop-down menu with a list of the Activities. Iterate between Turnover, Export, and Import to test how your selection affects the Tableau map’s visualisation.

**Step 5: Create Parameters and Combine Them with Filters**
-----------------------------------------------------------

In the following steps, we want to keep the existing Tableau map visualisation but display trading partners of Germany with the highest turnover only. Firstly, create a Top N parameter to limit the number of countries displayed. To create a parameter in Tableau:

1.  Click on the black arrow on the sidebar, just above the Tables title, and select _Create Parameter…_
2.  Type in _Top N_ as the name field at the top of the Parameter Window.
3.  Choose _Integer_ as the data type, set the _Current Value_ to 5 and then pick _Range_ from the list of Allowable values.
4.  In the _Range of Values_ section, check the _Minimum_ box and set it to 0. Then, set the Maximum to 250 and _Step Size_ to 5.

[![creating a Tableau parameter example](https://www.challengejp.com/wp-content/uploads/2021/04/step5_tableau_create_parameter_how_to_example-e1619087217884.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step5_tableau_create_parameter_how_to_example-e1619087217884.png)

Step 5: Example of Setting Up a Parameter in Tableau

Click OK and then go to the parameter’s name in the lower-left corner of the Tableau screen. Right-click it and then select _Show Parameter_ from the menu. You should now see a Top N slider under the Activity Filter.

**Step 6: Make Tableau’s Data Visualisation Dynamic**
-----------------------------------------------------

If you change the values in the Top N slider, you will notice that it currently doesn’t affect how the map displays the data. To make Tableau’s dynamic, link the parameter with a new filter.

To combine the Top N Parameter with a Country filter:

1.  Add the _Country_ field to the Filter pane. Right-click on it and select _Edit Filter_ from the menu.
2.  Select the _Top tab_ in the _Filter window_.
3.  Click on the _Field Option_ and replace number 10 with the Top N.
4.  Select Eur(000) from the list below, and ensure you selected _Sum_ in the field to the right.

Click OK. As a result, changing Top N should now affect the number of countries displayed on your Tableau map.

[![combining tableau filter and top n parameter example](https://www.challengejp.com/wp-content/uploads/2021/04/step6_tableau_filter_top_n_parameter-e1619087410846.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step6_tableau_filter_top_n_parameter-e1619087410846.png)

Step 6: Example of Combining a Top N Parameter and Filter in Tableau

**Step 7: Create a Table to Complete Data Visualisation**
---------------------------------------------------------

Let’s set up a Tableau table to aid in map visualisation. We want to display the trade categories’ breakdown and their corresponding values. To create a new Tableau sheet, click on the + icon, which you will find next to the current tab. As a result, you should now see an empty Tableau workspace.

Creating a table in Tableau is similar to [building a Pivot Table in Microsoft Excel](https://www.challengejp.com/blog/learn-excel-beginner-tutorial/#Step_10_How_to_create_a_Pivot_Table_in_Excel)
. Drag and drop the Country field into the rows section to display the country names in the first columns. Then, place the _Activity_ field in the _Columns_ section to expand the table to add other columns with activity names. Finally, drag the _Eur(000)_ field and drop it in the space below the headers to display the values in the Tableau table.

You should now see a Tableau table with the Country names listed to the left, followed by Export, Import and Turnover columns. To rearrange the columns’ order in Tableau, click and drag the _Turnover_ header and move it to the left.

Finally, go to the _Turnover_ header and click on the symbol (three lines) to rearrange the table. The table should now show the countries with the highest trade turnover first.

[![germany trading countries data table visualisation](https://www.challengejp.com/wp-content/uploads/2021/04/step7_tableau_table_germany_trading_countries_example-e1619087250128.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step7_tableau_table_germany_trading_countries_example-e1619087250128.png)

Step 7: Tableau’s Table with Germany’s Trading Partners Sorted by Turnover. For the latest source data, visit [Destatis](https://www.destatis.de/EN/Themes/Economy/Foreign-Trade/Tables/order-rank-germany-trading-partners.html)
.

Notice that changing the Top N parameter only affects the Map visualisation, while the Country list in the table stays the same. To change it and apply the same Tableau filter to both sheets, return to the filter’s pane in the Map sheet. Then, right-click on the _Country_ field and select _Apply to Worksheets…_ Finally, choose the _Selected Worksheets_ option, tick the box next to the Map sheet, and click OK.

**Step 8: Visualise Data with Tableau Dashboard**
-------------------------------------------------

Let’s create a dashboard to bring the two Tableau sheets into one place. We want to show the map and data visualisation on the top and the table below with Germany’s Turnover, Export, and Import values.

To create a Tableau dashboard:

1.  Click on the _New Dashboard_ icon at the bottom of the window.
2.  Adjust the dimensions of the Tableau dashboard by clicking on the Size values in the left pane.
3.  Choose _Generic Desktop_ to adjust the dashboard’s width.

Drag and drop the map sheet to the top of the new tab, then place the sheet with the countries table beneath it. Then, right-click on the table window, select _Fit_ and click on _Fit Width_ to adjust the window size automatically.

Finally, right-click on the Map sheet name and click _Hide Title_. Repeat the same step for the Table sheet. To add a title to the dashboard, go to the toolbar, click on Dashboard and select _Show Title_. Then, Double-click the header and change it to _Germany’s Trading Partners by Turnover_.

[![germany trade data visualisation dashboard](https://www.challengejp.com/wp-content/uploads/2021/04/step8_tableau_dashboard_data_visualisation_example-e1619087303973.png)](https://www.challengejp.com/wp-content/uploads/2021/04/step8_tableau_dashboard_data_visualisation_example-e1619087303973.png)

Step 8: Germany’s Top 10 Trading Partners – Example of Tableau’s Dashboard. For the latest data source, visit [Destatis](https://www.destatis.de/EN/Themes/Economy/Foreign-Trade/Tables/order-rank-germany-trading-partners.html)
.

You can also use a table to change the number of countries on the map. For example, to turn the Table sheet into a filter, go to the upper-right corner of the dashboard’s window and select the _Use as Filter_ icon. Then, hold a Ctrl key and click on the country names to display them on the map.

**Summary: From a CSV File to a Data Visualisation**
----------------------------------------------------

This tutorial has taken you through taking a simple CSV file and converting it into a meaningful data visualisation in Tableau. First, you downloaded a data file with Germany’s international trading partners’ numbers and imported it into Tableau. Then, you visualised the country data using the created field.

In the next step, you made Tableau’s map more interactive by adding filters and combining them with parameters. As a result, you could visualise the data by category and limit the number of countries to the most significant contributors to Germany’s trade balance.

You then created a dashboard to finalise the visualisation. First, you set up a separate table that explained the numbers in more detail. Then, you brought the Tableau sheets onto a dashboard. Finally, you turned the table sheet into a filter to make the dashboard more dynamic.

Get in Touch
------------

_[![challengejp_data_analyst](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, my name is Jacek, and I love spreadsheets! I h__ope you’ve enjoyed reading this tutorial as much as I did writing it. If you have any questions about Tableau and data analysis, don’t hesitate to **[get in touch](https://www.challengejp.com/contact/)
**._

_[**Explore my other tutorials**](https://www.challengejp.com/blog/)
 to learn more about data or financial analysis. If you need further support, find out about my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and **[Data Analytics Services](https://www.challengejp.com/services/data-analytics/)
**._

Learn More
----------

[Analyze and Forecast Customer](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)
 [Churn and Revenue](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)
 – Build a churn/retention model in Power BI using DAX, cohort analysis, and interactive forecasts.

[Learn How to Become a Self-Taught Data Analyst](https://www.challengejp.com/blog/learn-to-become-data-analyst/)
 – In this post, I share my experiences and tips on how I have taught myself Data Analysis.

[How to Analyse Data in Microsoft Excel with Power Query and a Pivot Table](https://www.challengejp.com/blog/how-to-analyse-data-excel-tutorial/)
 – This tutorial will take you through a step-by-step process of using Power Query and a Pivot Table to analyse data in Microsoft Excel.

[How to Use Python and Pandas for Data Consolidation and Transformation](https://www.challengejp.com/blog/python-excel-data-consolidation-transformation/)
 – If you are unfamiliar with Python, this tutorial will show you how to write simple scripts to consolidate and manipulate small and large data files.

[Your First Steps in Microsoft Excel Beginner’s Crash Tutorial](https://www.challengejp.com/blog/learn-excel-beginner-tutorial/)
 – This tutorial will give you a quick overview of the main functionalities and formulas and show you how to set up your first spreadsheet.

Tags:[Data Analytics](https://www.challengejp.com/blog/tag/data-analytics/ "Data Analytics")
[Tableau Tutorial](https://www.challengejp.com/blog/tag/tableau-tutorial/ "Tableau Tutorial")

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.