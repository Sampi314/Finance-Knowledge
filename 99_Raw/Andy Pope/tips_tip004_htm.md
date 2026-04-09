# Chart Name

**Source:** https://www.andypope.info/tips/tip004.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Changing name of embedded chart

You can manually change the name of a embedded chart via the Name box. Although to get this to contain the charts name you have to select the chart as an object rather than have the chart selected. Hold the Shift key whilst selecting the chart. Notice that the subtle different in selection is denoted by the colour of the selection handles. They are white instead of the normal black. The current chart name is now displayed in the Name box and can be edited.  
There is a 32 character limit on the name when entering via the name box

![](https://www.andypope.info/tips/tip004a.gif)

  
In xl2007 and xl2010 the ribbon offers a more direct way to change the chart name via the Chart Name textbox in the Properties group of the Layout contextual tab of Chart Tools.  

![](https://www.andypope.info/tips/tip004e.png)

  
  
  
In xl2013 then chart name box was removed from the ribbon but can still be added back by customising the ribbon via the File tab and the Options button on the Backstage view.

![](https://www.andypope.info/tips/tip004c.png)

Select All commands and Tools tab. With the Chart Tools tab you can add a new Group and then add the Chart Name control.

![](https://www.andypope.info/tips/tip004b.png)

Another alternative is to use the Selection pane. ALT+F10 will toggle selection pane view.  
You can then select the name and use F2 to edit name.

![](https://www.andypope.info/tips/tip004d.png)

  
Finally you can change the chart object name using VBA code.  

ActiveChart.Parent.Name = "MyChartname"

Created 28th April 2012

Last updated 7th August 2014 

  
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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip004.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope