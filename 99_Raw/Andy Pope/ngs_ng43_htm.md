# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng43.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

 

|     |     |
| --- | --- |
|     | RE: Graph - axis switching for a line graph<br>------------------------------------------- |     |
|     | ##### Unfortunately you can not combine a bar chart with a xy scatter graph using MSGraph.  <br>So to get the points to appear with the bars you can use a couple of dummy data series work arounds.column.<br><br>![](https://www.andypope.info/ngs/ng43a.gif) |     |
| ##### Add 2 extra data series. Format both to be on the secondary axis and of the stacked bar chart style.<br><br>##### For clarity I have left the Pad series with a fill pattern in the finish chart this would be set to None.<br><br>##### The Dot data series has a custom fill pattern. To get this I generated a circle using the Autoshapes and formatted with a fill colour and border. Copy, using CTRL+C, the autoshape to the clipboard and then edit the graph and select the Dot series. CTRL+V fill apply the autoshape as the fill pattern.<br><br>##### Now apply data labels on the Dot series you will have to manually change the value displayed to that required.<br><br>##### As you can see the values in the data sheet are not those actually displayed by the data labels. The Pad values need to be less than the required value by half that of the Dot value. The Dot value is bit of trial and error depending on the under lying data and a value that does not distort the fill pattern. Adjusting the bars gap width will also effect the value used. Once completed the extra legend entries can be deleted. | ![](https://www.andypope.info/ngs/ng43a.gif)<br><br>![](https://www.andypope.info/ngs/ng43b.gif) |
|     |     |     |
| ##### This version uses a similar technique but this time the bar gap width is set to the maximum, in order to get a smaller thickness as possible as this will distort the connecting lines. The values of Pad are now exactly the values required in order to position the data labels. The data labels themselves actually belong to the Dot series and have to be manually edited. The data labels are needed to mask the fact that the connecting lines do not meet exactly at the center of the bar but rather at either side of the bar. | ![](https://www.andypope.info/ngs/ng43d.gif)<br><br>![](https://www.andypope.info/ngs/ng43c.gif) |
|     |     |
| ##### If the above is not suitable then the combination of bar and XY scatter can be achieved by using an Excel chart. |     |
|     |     |
|     |     |

  

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng43.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope