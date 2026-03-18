# Display Y axis on both sides

**Source:** https://www.andypope.info/tips/tip005.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Displaying Y axis values on both sides of plot area

In order to display Y axis values on both sides of the plot area you need to add an additional data series and plot it on the secondary axis. Create a standard column chart based on the data in A1:B6

|     |     |     |
| --- | --- | --- |
|     | A   | B   |
| 1   |     | Expenditure |
| 2   | Jan | 56.3 |
| 3   | Feb | 22.3 |
| 4   | Mar | 46.4 |
| 5   | Apr | 92.7 |
| 6   | May | 15.5 |

![](https://www.andypope.info/tips/tip005a.gif)

Add an duplicate set of data to the chart. This can be done by either

*   Select the range B1:B6 and then drag & drop the data onto the chart
*   From the chart menu use Add Data.. and select the range B1:B6
*   Use the Source data dialog to add a series and then select the range B1:B6

The reason for using the same data twice is the automatic values used for the scales minimum, maximum, major and minor steps should be the same.

![](https://www.andypope.info/tips/tip005b.gif)

The second set of data is currently displayed next to the original data and is still using the same Y axis. Double click the original data series and change it so the data is plotted on the Secondary axis.

![](https://www.andypope.info/tips/tip005c.gif)

The only reason for moving the original data to the secondary axis is that the data on the secondary axis is plotted in front of the data on primary axis and it is likely that you might have already formatted the column in terms if fill pattern and borders. If you require a legend you will have to [remove the duplicate](https://www.andypope.info/charts/deletelegendentry.htm)
 data series.

![](https://www.andypope.info/tips/tip005d.gif)

Created 28th April 2012

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip005.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope