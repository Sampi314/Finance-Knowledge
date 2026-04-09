# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng60.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

 

|     |     |
| --- | --- |
|     | Re: Doughnut Chart & Conditional Formats<br>---------------------------------------- |
|     | ##### This creates a coloured section within a donut chart depending upon the month status value.  <br>The valid values are R, A, G or blank.<br><br>##### ![](https://www.andypope.info/ngs/ng60a.gif)<br><br>##### The chart actually has a section of each of the 4 possible values per month. By using formula the correct data point will be given a value of 1. The remaining 3 data points will have a value of zero.  <br>  <br>The labels are provided by a series on the secondary axis with a value of 1 for each month<br><br>##### Start by creating a 2 series donut on the full set of data. To make it easier to format the individual data points used a data series which consisted of 1's so each of the 4 possible colours is visible.  <br>Format an individual point by first select the series and then selecting the data point. Once you format the first data point you can use the right cursor key to move through to the fifth data point and use the F4 button to repeat formatting. You will need to do this for all 4 sets of colours.<br><br>##### ![](https://www.andypope.info/ngs/ng60b.gif) <br><br>##### Next we need to move the outer series to the secondary axis. In xl2003 and before you can simply change the series to the secondary axis. In xl2007 the option is not available via the dialogs.  <br>To get around this first we need to change the 2nd series to a Pie chart. Then you can set the pie chart series to the secondary axis<br><br>![](https://www.andypope.info/ngs/ng60c.gif)<br><br>##### Add a border to the second series<br><br>![](https://www.andypope.info/ngs/ng60d.gif)<br><br>##### Reduce the data range for the series to 12 points. Also set the secondary category labels to the month names.  <br>You can then apply data labels showing category labels to the series.<br><br>![](https://www.andypope.info/ngs/ng60e.gif)<br><br>##### The final step is to change the 1st series data source to that of the formulas so only 1 in 4 data points are displayed.<br><br>##### The download file contains both .xls and .xlsx files with instructions.  <br>  <br>ng60.zip [![](https://www.andypope.info/Images/download.gif)](https://www.andypope.info/ngs/ng60.zip)<br> (79kb) |
|     |
|     |
|     |

  

Created August 2004

Last updated 23rd May 2009 

  
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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng60.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope