# Polar plot

**Source:** https://www.andypope.info/charts/polarplot2.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Polar plots

 

|     |     |     |
| --- | --- | --- |
|     | ![](https://www.andypope.info/charts/ppex1.gif)<br>-----------------------------------------------<br><br>##### The polar plot is created using the Radar chart.  <br>This particular example requires 2 data series in order to generate the spiral effect.  <br>  <br>The angle and distance data is stored in a table with a named range. The radar chart has a point of each of the 360 degrees. Which points are plotted is determined by using a VLOOKUP function. For angles that are not contained within the data table the effect of the plot can be altered by charting either a zero or a #N/A. |     |
|     |
|     |
|     |
| ##### In the example workbook is a sheet containing data in order to build the following example |     |
|     |     |
| ![](https://www.andypope.info/charts/pp1.gif) | ##### Create a standard radar chart based on the 360 angles, which are contained in the range B2:B362 |
|     |     |
| ![](https://www.andypope.info/charts/pp2.gif) | ##### Clear the Category labels from the chart |
|     |     |
| ![](https://www.andypope.info/charts/pp3.gif) | ##### Remove all the lines by formatting the axis and setting the Line to None |
|     |     |
| ![](https://www.andypope.info/charts/pp4.gif) | ##### To construct the angle axis use a dummy data series. Add the information in range F2:F9 to the chart |
|     |     |
| ![](https://www.andypope.info/charts/pp5.gif) | ##### Move the dummy data series to the secondary axis |
|     |     |
| ![](https://www.andypope.info/charts/pp6.gif) | ##### You can set the Line pattern to None on the dummy series to make in invisible.  <br>Set the secondary axis category labels to the range E2:E9 |
|     |     |
| ![](https://www.andypope.info/charts/pp7.gif) | ##### Remove the legend and format the secondary axis as requried |
|     |     |
| ![](https://www.andypope.info/charts/pp8.gif) | ##### Depending on the plot you may wish to set the final points line style to None in order to remove the connecting line back to the zero.  <br>To do this select the series and then use the right arrow to cycle through the points in the series. On the last points format the line to None. |
|     |     |
| Example Plots |     |
| ![](https://www.andypope.info/charts/ppex7.gif) | ![](https://www.andypope.info/charts/ppex6.gif) |
| ![](https://www.andypope.info/charts/ppex5.gif) | ![](https://www.andypope.info/charts/ppex2.gif) |
| ![](https://www.andypope.info/charts/ppex4.gif) | ![](https://www.andypope.info/charts/ppex3.gif) |
|     |     |
| You can also use the filled radar plot |     |
| ![](https://www.andypope.info/charts/ppex8.gif) | ![](https://www.andypope.info/charts/ppex9.gif) |
| ![](https://www.andypope.info/charts/ppex10.gif) |     |
|     | ##### Example [workbook](https://www.andypope.info/charts/Polarplots.zip)<br> with data and formula |     |
|     |     |     |
|     |     |     |
|     |     |

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/Polarplots.zip)

Created August 2004

Last updated 5th August 2014 

  
           [![Return to main page](https://www.andypope.info/Site_Images/nav_home.png)](https://www.andypope.info/index.htm "Return to home page")
 [![Chart Section](https://www.andypope.info/Site_Images/nav_charts.png)](https://www.andypope.info/charts.htm "Goto Charts Section")
 [![VBA section](https://www.andypope.info/Site_Images/nav_vba.png)](https://www.andypope.info/vba.htm "Goto VBA Section")
 [![Fun and games section](https://www.andypope.info/Site_Images/nav_fun.png)](https://www.andypope.info/fun.htm "Goto Fun & Games Section")
 [![Forum files](https://www.andypope.info/Site_Images/nav_forum.png)](https://www.andypope.info/newsgroups.htm "Goto Forum Section")
 [![Tips section](https://www.andypope.info/Site_Images/nav_tips.png)](https://www.andypope.info/tips.htm "Goto Tips & Tricks Section")
 [![Links section](https://www.andypope.info/Site_Images/nav_links.png)](https://www.andypope.info/links.htm "Goto Excel Resources Section")
 [![Book section](https://www.andypope.info/Site_Images/nav_books.png)](https://www.andypope.info/books.htm "Goto Books section")
 [![Site information](https://www.andypope.info/Site_Images/nav_info.png)](https://www.andypope.info/about.htm "Goto About Section")
 [![Site Search](https://www.andypope.info/Site_Images/nav_search.png)](https://www.andypope.info/search.htm "Goto Site Search")
[![RSS feed](https://www.andypope.info/Site_Images/nav_rss.png)](https://www.andypope.info/feed/feed.xml "RSS Feed")
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/polarplot2.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope