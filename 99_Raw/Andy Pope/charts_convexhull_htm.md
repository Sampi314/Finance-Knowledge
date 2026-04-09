# Convex hull

**Source:** https://www.andypope.info/charts/convexhull.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Bounding area in xy scatter chart

 

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     | ![](https://www.andypope.info/charts/chull1.gif)<br><br>##### This is a standard xy scatter chart. It has 2 data series plotted as markers only. The VBA code will then calculate the bounding area and output the necessary X and Y values in order to plot the encapsulating lines. |     |
|     |     |     |
|     | ##### The technique for determining the bounding line is one known as 'gift wrapping'.<br><br>##### The lowest x value point is chosen as the starting point and the each other point is checked to find the one that causes the smallest change in angle. | ![](https://www.andypope.info/charts/chull_ani.gif) |
|     | ##### The [example workbook](https://www.andypope.info/charts/ConvexHull.zip)<br> contains the relevant class code to produce a set of bounding x and y values.  <br>The animation property is purely for fun and demonstration.<br><br>##### There is also a property to  to control how tight the bounding line fits the points.  <br>The example above is not a tight fit as the bounding lines are not touching the points. |     |

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/ConvexHull.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/convexhull.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope