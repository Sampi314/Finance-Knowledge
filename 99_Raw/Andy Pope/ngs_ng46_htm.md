# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng46.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

 

|     |     |
| --- | --- |
|     | RE: Goal range in a graph<br>------------------------- |
|     | ##### There are a few ways you can add a goal line or band to MSGraph.<br><br>![](https://www.andypope.info/ngs/ng46c.gif)  <br>![](https://www.andypope.info/ngs/ng46b.gif)  <br>![](https://www.andypope.info/ngs/ng46d.gif)<br><br>##### They are all constructed in the same way. |
| ##### From the datasheet below you can see the original data for series East, West and North. I have added a padding series which will be used either as the bottom line or the data series to pad the hi-lite area or column. |
|     | ![](https://www.andypope.info/ngs/ng46a.gif) |
| ##### With the new data series added to the datasheet you can now update the chart. |
| ##### Line and Area style<br><br>##### Start by changing the chart type of the 2 new series, either stacked Line or Stacked Area. Then move them both to the secondary Y axis. The Y axis should be set to the same Minimum and Maximum values as the primary axis. Use the Chart Options dialog to enable the secondary X axis. You need this in order to uncheck the Crosses between Categories. With this unchecked the line and area charts will extend right up to the plot area. Format the secondary X axis so no labels, tickmarks or lines are displayed. Format the secondary Y axis the same and uncheck the "Category (X) axis crosses at Maximum Value".<br><br>##### Column Style<br><br>##### The data set for this need only include the first value. Then set the 2 series to the secondary Y axis and the change the chart type to stacked column. The rest of the steps needed are the same as for the Line and Area. Notice though that the Cross between categories makes the first column appear to straddle the Y axis and be half the thickness.<br><br>##### It is possible to get the complete by to appear by using advance fill options. On the Patterns tab press the Fill Effects button and go to the Pattern tab set the fore and background colour to be the same and with the aid of what I assume is a bug when MSGraph is deselected the whole column is displayed.<br><br>#####   <br>![](https://www.andypope.info/ngs/ng46e.gif)<br><br>##### You can use a value of all of the categories and then reduce the Gap Width to zero. This will give you a band similar to the area chart version but the band will be infront of the columns. |
| ##### [Example ppt file](https://www.andypope.info/ngs/ng46.zip) |
|     |

  

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng46.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope