# Pie zeros

**Source:** https://www.andypope.info/charts/piezeros.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

Content 

|     |     |
| --- | --- |
|     | Automatic removal of zero values in pie chart<br>---------------------------------------------<br><br>![](https://www.andypope.info/charts/pie0_1.GIF)  ![](https://www.andypope.info/charts/pie0_2.GIF)<br>-------------------------------------------------------------------------------------------------- |
|     | ##### You can see from the above images the effect of setting data items C and F to zero.<br><br>##### The [workbook](https://www.andypope.info/charts/piezeros.zip)<br> contains an example of a pie chart that automatically removes zero values from the pie and the legend.<br><br>##### The chart uses named ranges in order to dynamically expand or contract.<br><br>##### The formulas used to remove zero data points are courtesy of Doug Tyrrell ([www.dotxls.com](http://www.dotxls.com/)<br>)<br><br>##### Updated to include formula to handle data laid out in rows rather than columns.  <br><br>##### There is a bug in xl2007 that if you set all of the original data values to zero the named range  formula will report as reference error and then become detached from the chart. It will not automatically update the chart when new values are entered in to the data cells. To avoid this break of formula I have modified the named range formula to always include 1 point. This will allow the chart to automatically update when valid values are entered.  <br>Note this does not remove the warning of invalid formula that will appear with all cells are zero.<br><br>##### Download xl2007 version of [workbook](https://www.andypope.info/charts/piezeros_07.zip)<br> ![](https://www.andypope.info/Images/xl2007.bmp) |

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/piezeros_07.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/piezeros.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope