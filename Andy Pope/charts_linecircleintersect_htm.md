# Line, circle intersection

**Source:** https://www.andypope.info/charts/linecircleintersect.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Intersection points between line and circle

 

|     |     |     |
| --- | --- | --- |
|     | ![](https://www.andypope.info/charts/linecircleintersect.gif)<br>-------------------------------------------------------------<br><br>![](https://www.andypope.info/charts/circlecircleintersect.gif) <br>----------------------------------------------------------------<br><br>##### The workbook contains code for 2 User Defined Functions array functions which output the intersection points between a Circle and either another Circle or a line. |     |
|     |
| ##### IntersectLineCircle:<br><br>##### \=IntersectLineCircle( LineCoordinates , CircleX , CircleY , Radius )<br><br>> ##### LineCoordinates is a 2 column range which contains the x and y points for a line.<br>> <br>> ##### CircleX is the X position of the circles center point. Can be a value or range reference.<br>> <br>> ##### CircleY is the Y position of the circles center point. Can be a value or range reference.<br>> <br>> ##### Radius is the radius of the circle. Can be a value or range reference.<br><br>##### The function returns an array of X and Y intersect points. As the number of possible intersect points between a line and circle has a maximum of 2 points the size of the array formula can be determined from the input information. The number of possible intersections is (Line segments-1)\*2 |     |
|     |     |
| ##### IntersectCircleCircle:<br><br>##### \=IntersectCircleCircle( Circle1X , Circle1Y , Radius1 , Circle2X , Circle2Y , Radius2 )<br><br>> ##### Circle1X and Circle2X are the X position of the circles center point. Can be a value or range reference.<br>> <br>> ##### Circle1Y and Circle2Y are the Y position of the circles center point. Can be a value or range reference.<br>> <br>> ##### Radius1 and Radius2 are the radius of the circle. Can be a value or range reference.<br><br>##### The function returns an array of 2 X and Y intersect points. |     |
|     |     |
| ##### **Remember when using array formula to commit the formula with CTRL + SHIFT + ENTER** |     |
|     |     |
| ##### The [download](https://www.andypope.info/charts/CircleIntersection.zip)<br> contains both example charts and associated data sets and required vba code. |     |
|     |     |
|     | ##### ![](https://www.andypope.info/images/xl2007.bmp) Tested in xl2007 |     |
|     |     |     |

  [![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/CircleIntersection.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/linecircleintersect.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope