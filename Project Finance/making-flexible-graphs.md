# Making Flexible Graphs

**Source:** https://edbodmer.com/making-flexible-graphs

---

I think effective presentation of data is the most fundamental aspect of statistics and an important component of financial modelling. This page demonstrates how to create a variety of different types of flexible graphs in your models and analysis. I have tried to make files that demonstrate how to select different items from a database, how to make flexible x-scales, how to select a different number of series in the graph, how to change titles on the graph, how to create waterfall graphs that were not excel before 2016, how to make scatter and bubble carts and other things. The graph types described include standard line graphs, bubble graphs, confidence interval graphs, football field graphs and graphs where the x-axis is flexible depending on an input in the model. To create graphs with a flexible x-axis you can either use the OFFSET function and create a flexible range name or use the #NA method. Files on this page also demonstrate how to make add macros to automate items in graphs and to automate min and max scales. Videos associated with making the various graphs are shown below the graphs.

Note that some of the graphs can be created more easily with Power BI. I think Power BI can be in some sense thought of as a fancy graphic package that you can use after you are finished with your excel analysis. I have used this red text to point out when Power BI can be used to present the data.

Using the INDEX Function and a User Form to Graph Items Multiple Items on a Spreadsheet in Seconds
--------------------------------------------------------------------------------------------------

I think one of the most useful and quick things to do with a whole lot of data (for example a set of historic financial statements) is to use the INDEX function to graph all of the items on a sheet. All you have to do is to use a code number for the row of the sheet that you want graphed and then use the INDEX function with an entire column. You can then add a drop down box or a spinner box. The file below demonstrates how you can take just about any file and then add a drop down box (combo box) to graph any line on the page. You can also get a little fancier by using multiple columns for the name and avoiding blank rows. The technique and avoiding blank or title lines is a bit more difficult where you can include TRUE/FALSE switches on each line and then count the number with the MATCH function.

As long as you have the field name at the top as the years and the item, you could do this pretty easily in Power BI. One this one however, I think it is so easy to do with the INDEX function and a user form, you can do this in minutes. The problem with Power BI is that you may have to spend a lot of time fixing things to get the file ready for making graphs.

**[Link to My Youtube Channel Where You Can Look At All of the Different Videos that I have Made](https://www.youtube.com/channel/UC2g_Ih-lK1sa3L_1xHacA8w)
**

Graphs with Index Function.xlsm

Making Flexible Graphs with Switches, Match, Index, and Offset function
-----------------------------------------------------------------------

The file and video below shows how to make a graph that presents flexible items on the x-scale. In the example, there are different categories on the x-scale (countries and technologies). There are different numbers of items on the x-scale and check boxes are used to selectively graph various items on the x-scale. The process begins by defining items to be graphed with a check box. Values of TRUE and FALSE are used create a series of TRUE or FALSE switches in the data. The TRUE and FALSE switches are used to create a counter where a counter is accumulated. For example, if there are four TRUE’s in the series, the first in row 10, then next in row 15, the third in row 17 and the last in row 25. The counter begins with zero, increases to 1 at row 10, stays at row 1 until row 15 and then increases to 2. The process continues until the number 4 occurs in row 25. With the counters created from the TRUE and FALSE you can use the MATCH function to find the row. To do this create a simple counter list. Next to the counter use the MATCH function to find the row. Then you can use the INDEX function along with the MATCH function to select different items from the data. The final step in the process is to use the OFFSET function because a different number of rows may be selected. This means the height parameter in the OFFSET function has to be adjusted. The video below explains file below demonstrates how to work through process. The second file below named LCOE database uses and example of the process. Other videos describe how to make similar graphs using Power BI.

You can do this in Power BI with a filter (I think some call this a slicer). The advantage of working in excel only is that you can immediately see the sensitivity and that you can have more flexibility in selecting variables to graph.

LCOE Analysis with Database.xlsm

LCOE Analysis with Database.xlsm

Quickly Making Scatter Charts and Bubble Charts that are a Cousin of Scatter Charts
-----------------------------------------------------------------------------------

The file below demonstrates how to create flexible bubble charts from scatter plots. It also shows you how to use macros to make labels on the bubbles and to make various groups of bubbles have alternative colours. To make a bubble chart very quickly you can set up your data without an x-axis title and then select the area and press the F11 sheet. Then you select the scatter plot and the bubble chart option. The file below demonstrates how to set up data with an extra row or column for the bubble size and then use F11 key to create scatter plot and then make it into a bubble chart. You can do this in minutes if you eliminate the x-axis title before you make the selection. Putting labels on bubbles and making the bubbles have different colours is more difficult. The file below is associated with three videos that show you how to make macros to automatically add labels to each bubble and how to create colour codes to make each bubble a separate colour. The videos are listed in the table at the bottom of this page that are named bubble charts.

You can make effective scatter plots in Power BI. You can also add labels easily in Power BI. It is not obvious how to add trend lines to the scatter plots in power BI.

Example bubble chart.xlsm

Using Index Function, Offset Function and Frequency Function for Data Analysis
------------------------------------------------------------------------------

The commodity price file listed below demonstrates a lot of subjects associated with making graphs and includes macros to read data and make graphs of forecast and actual with list box. Graphs have flexible x-scales by using the #N/A technique and the OFFSET function. Using the OFFSET function with dynamic range names has some advantages over the #N/A method in that you can show things like averages, standard deviations and volatility on the top of the graph and that these statistics change when the x-scale changes. Other graphs use the LISTBOX technique described above. In addition the file demonstrates how to make frequency distributions and test for normality using the FREQUENCY function. The distribution graphs are made by computing percent changes and then comparing the results with the distribution that would occur from a normal distribution.

Commodity Price Analysis.xlsm

Comprehensive Graphing Examples with Associated Videos
------------------------------------------------------

The two files below include a comprehensive set of elements that can be used to make flexible graphs. The first file shows how to make a flexible graph including varying time, flexible dates, selection of alternative items, multiple series options, alternative styles etc. It can be used together with the set of videos listed in the table at the bottom of the page that walk through different flexible graphing techniques in a step-by-step manner. Choosing a single series from a lot of data is easy — it can be accomplished with the INDEX function. Making the x-scale flexible and including alternative numbers of series on charts is more difficult and is demonstrated in the file. Making the graphs even more flexible through allowing a different number of series to be presented on the graph with a list box is even more difficult.

The second file listed below illustrates how to include confidence intervals in graphs and how to make flexible bubble charts. This second file is also associated with a video in the table at the bottom of the page. In this file macros are included to set labels and colours for the bubbles. I think it may be a good idea just to open the file and get some ideas about how to make really dynamic graphs.

You can do a whole lot of this in Power BI — especially the flexible bubble charge if you use a slicer. I have included confidence interval graphs in this file which can be very effective. I copied these from my friend and I do not know how to do this in Power BI.

Oil and Gas Production and Flaring and Venting for Flexible Graphs.xlsm

Flexible Charts with Confidence Intervals and Bubbles, Listboxes.xlsm

Football Field Graphs (American Football) to Illustrate Ranges in Value
-----------------------------------------------------------------------

A football field graph is a pretty silly name used to present alternative valuation techniques with different ranges. While the name is irritating, the idea is good because it shows that different valuation techniques can be used and that it is naive to believe a single valuation level is reasonable. Making a basic football field graph is quite simple with the bar chart selection in excel. The problem comes when you put labels on bars in the chart. The files below demonstrate how you can construct such a flexible football field diagram that includes the valuation amounts as labels on the graphs. Putting lables on the football field involves adding a separate series to make spaces and it can be painful. The good news is that no macros are necessary.

Valuation Example.xlsm

AZIZA Tuesday.xlsm

Footbal Field Graph.xlsx

Using a Listbox Form with Multiple Selections to Allow Different Series to be Presented on a Graph
--------------------------------------------------------------------------------------------------

A thing that I have not been able to do for years is to be able select either a different number of series on a graph with a list box. By this I mean you may for example want to pick two different countries or alternatively ten countries to display on a graph. You could then choose to not show one series on a graph by de-selecting the item from the listbox. To use a list box in a graph or in other circumstances with multiple entries you need to add a macro to the list box. This process is illustrated in the file below that has macros that allow you to use the LISTBOX Form with MULTIPLE selections.

Lets say you are not interested in macros but you want to use this listbox process you can just copy it from the listbox in the file to a listbox in your workbook. If you download the file, you can right click on the list box, select the macro and copy it to your file. You just have re-name the list box number in the macro. The list box can be effective in making graphs where you may want to present a different amount of series. For example, you may want to compare 10 stocks or only two stocks on a graph. The problem is that to use the LISTBOX you need to attach it to a macro to collect data from multiple sources. This macro and process is demonstrated in the file.

Flex Multiple Series on Graph.xlsm

Using Multiple Check-Boxes to Make Flexible Graphs
--------------------------------------------------

If you want multiple options to put on a graph, you can add check boxes instead of using the list box. To do this, you can create a lot of check boxes and then use the TRUE or FALSE created by the check boxes to count the number of selections. Since you know that TRUE is 1 and FALSE is zero, you can create a column that adds the check boxes that are counted. This counter can then be matched against a counter variable to find the items that have been checked. You add a separate counter (you can use ALT, E, I, S) and then apply the MATCH function to find the number of the selection. Finally, use the INDEX function to put the items that are checked at the top. This process is illustrated below from the comprehensive stock price file.

The most difficult thing about this is copying the check boxes when you may have more than 100 different possible selections. To do this I have make a macro. It is not perfect and you have to be careful when operating it. The first step is to copy the check boxes and make sure that you have new numbers for the check box (that you can find with looking at a macro as demonstrated below). You cannot do this with manual calculation. After copying the checkbox you can run the macro with SHIFT, CNTL, E. As with other macros, save your file before running the macro.

The process for creating check boxes is illustrated below from the template file named “Attach Multiple Checkboxes”

Using the OFFSET Function to Create and Graph Dynamic Range Names
-----------------------------------------------------------------

The file below demonstrates how you can use the OFFSET function to make dynamic range names that allow you to make flexible graphs. In particular, you can make the timing completely flexible on the charts. Making a dynamic range name involves using the height and width optional arguments in the OFFSET function. Whilst you have to make separate range names for each series, the technique can be very useful for statistical analysis. To fund the range names you use with the OFFSET function you can use the CNTL, F3 short-cut.

Exercise 6 – Offset Graph.xls

Creating Flexible X-Scales with the #N/A Method
-----------------------------------------------

The file below demonstrates how to make flexible graphs using the NA() method. This is a very simple way to make the x-scale flexible when you have a time series in the x-scale. To apply this method you substitute the #N/A for the date on the x-scale and you make sure that the x-scale is classified as a date axis. This can be created with a template that is saved in the file and is very good for presenting various statistical analyses. The file demonstrates how to gather data for the graphs wih the INDEX, MATCH and INDIRECT function along with using TRUE/FALSE switches to limit the graph to selected items. It also includes use of the OFFSET function in order to change the number of items that appear on the x-axis. The bubble graphs are created using the macros that are included in the bubble file example above and in a video.

Dynamic graphs with #NA.xlsm

### Spinner Box to Change the Scale on Graphs

The simple video below shows how to put a spinner box on a graph to allow you change the scale on a graph. All you do is to start recording a macro and then go to the graph and change the scale. After you record the macro you can enter the minimum scale somewhere in the file and name the range. Then just go back to your macro and replace the number you entered for the minimum amount with the range name using RANGE(“min”). Of course, you need to name the range.

Waterfall Charts.xlsm

Making Graphs that Can Display Annual, Quarterly or Monthly Data
----------------------------------------------------------------

Sometimes you may want to make graphs that display data in different time increments. To do this I think you need to first create one or a number of series using the AVERAGEIF function. Then you can graph data with the OFFSET function or the #N/A method. The file below demonstrates this in the context of hourly prices in the Philippines market.

Nigeria Analysis Fixed.xlsm

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Excel Exercise File |     | Video |     |
|     |     |     |     |     |     |
| Making Bubble Charts Quickly with F11 |     | Example Bubble Chart |     | [https://www.youtube.com/watch?v=\_wrZB1HeHkI](https://www.youtube.com/watch?v=_wrZB1HeHkI) |     |
| Adding Labels to Bubble Charts |     | Example Bubble Chart |     | [https://www.youtube.com/watch?v=DWiPO6lo\_EY](https://www.youtube.com/watch?v=DWiPO6lo_EY) |     |
| Adding Colours to Bubble Charts |     | Example Bubble Chart |     | [https://www.youtube.com/watch?v=iW4eZ0cF\_vI](https://www.youtube.com/watch?v=iW4eZ0cF_vI) |     |
| Flexible Bubble and Confidence Charts |     | Flexible Bubble and Confidence Intervals |     | [https://www.youtube.com/watch?v=JyNxrbnNH2k](https://www.youtube.com/watch?v=JyNxrbnNH2k) |     |
| Commodity Price Analysis with List Box |     | Commodity Price Analysis |     | [https://www.youtube.com/watch?v=3qUgcVwgzWo](https://www.youtube.com/watch?v=3qUgcVwgzWo) |     |
| Macro for List Box |     | Flex Multiple Series on Graph |     | [https://www.youtube.com/watch?v=b7S3\_9iCQgs](https://www.youtube.com/watch?v=b7S3_9iCQgs) |     |
| Adjusting Macro for List Box on Graph |     | Flex Multiple Series on Graph |     | [https://www.youtube.com/watch?v=N2M\_1mTHjtQ](https://www.youtube.com/watch?v=N2M_1mTHjtQ) |     |
| Adding Labels with List Box |     | Flex Multiple Series on Graph |     | [https://www.youtube.com/watch?v=zE0\_QNBjYfQ](https://www.youtube.com/watch?v=zE0_QNBjYfQ) |     |
| Flexible Graphs of Stock Prices with #N/A |     | Saudi Stocks |     | [https://www.youtube.com/watch?v=C\_Sz6-iO-OQ](https://www.youtube.com/watch?v=C_Sz6-iO-OQ) |     |
| Presentation of Operating Assumptions with INDEX |     | Mongolia Mining |     | [https://www.youtube.com/watch?v=MHBdhFuWmaQ](https://www.youtube.com/watch?v=MHBdhFuWmaQ) |     |
| Creating Single Graph with #N/A and Index |     | Housing Data |     | [https://www.youtube.com/watch?v=sGDDr7egXuo](https://www.youtube.com/watch?v=sGDDr7egXuo) |     |
| Adjusting Nominal Data for Inflation |     | Housing Data |     | [https://www.youtube.com/watch?v=L2TM2VG72MU](https://www.youtube.com/watch?v=L2TM2VG72MU) |     |
| Creating Graph with multiple Serise with TRUE/FALSE |     | Housing Data |     | [https://www.youtube.com/watch?v=c8k8LrJobX4](https://www.youtube.com/watch?v=c8k8LrJobX4) |     |
| Basic Graph with Index Function |     |     |     |     |     |
| Flexible Graph with INDEX function |     | IEA Prices and Statistics |     | [https://www.youtube.com/watch?v=IbbOgBTY50s](https://www.youtube.com/watch?v=IbbOgBTY50s) |     |
| Flexible Styles in Graphs with Macros |     | OA and OB History and Forecast |     | [https://www.youtube.com/watch?v=EbaaTlc4yVc](https://www.youtube.com/watch?v=EbaaTlc4yVc) |     |
| Flexible Timing with years, quarters month |     | OA and OB History and Forecast |     | [https://www.youtube.com/watch?v=nhmUcGezgxI](https://www.youtube.com/watch?v=nhmUcGezgxI) |     |
| Creating Football Field Diagram |     | Football Field |     | [https://www.youtube.com/watch?v=7u\_En5nkTq0](https://www.youtube.com/watch?v=7u_En5nkTq0) |     |
| Flex Minimum and Max on Charts |     | Actual vs Forecast |     | [https://www.youtube.com/watch?v=G5C3LKhHRdM](https://www.youtube.com/watch?v=G5C3LKhHRdM) |     |
| U.S. Markets Merchant Analysis by Region |     | EIA Merchant Analysis |     | [https://www.youtube.com/watch?v=JiV-n5zQ7AQ](https://www.youtube.com/watch?v=JiV-n5zQ7AQ) |     |
| Use of Offset together with Match and Index |     | Nigeria Summary Analysis |     | [https://www.youtube.com/watch?v=VkD2mLYPYyA](https://www.youtube.com/watch?v=VkD2mLYPYyA) |     |
| Duplicating Graphs and Analysis with Match and Index |     | Nigeria Summary Analysis |     | [https://www.youtube.com/watch?v=s6puxvXF1SQ](https://www.youtube.com/watch?v=s6puxvXF1SQ) |     |
| Graphs with Detail and Averages |     | PJM Hub Prices |     | [https://www.youtube.com/watch?v=M0x\_fdt\_s8c](https://www.youtube.com/watch?v=M0x_fdt_s8c) |     |
| Graphs with Moving Averages |     | Interpolate and Lookup |     | [https://www.youtube.com/watch?v=D9vJYvjf3i8](https://www.youtube.com/watch?v=D9vJYvjf3i8) |     |
| Flexible Y-Scale |     | Integrated Generation Analysis |     |     |     |
| Graphs that show Hourly, Daily, Monthly, Quarterly with Button |     | WESM Prices Phillippines |     |     |     |
| History and Projections for Assumption Graphs |     | Kalitta Corporate Model |     | [https://www.youtube.com/watch?v=pMlgHgQvTqY](https://www.youtube.com/watch?v=pMlgHgQvTqY) |     |
| …………………………………………………………………………………………….. | ….. | …………………………………………………………….. | …   | ………………………………………………………………………………………………. | ….. |

OA and OB History and Forecast 1.xlsm

Corporate Financial Model.xlsx

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=518&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10812&rand=0.12307816299454333)