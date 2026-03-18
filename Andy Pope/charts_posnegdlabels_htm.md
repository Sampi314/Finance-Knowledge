# Pos/Neg data labels

**Source:** https://www.andypope.info/charts/posnegdlabels.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Positive/negative axis labels on a bar chart

   

![](https://www.andypope.info/charts/posneg10.gif)

##### This example uses a dummy data series to plot the category name either side of the axis depending on whether the bar is positive or negative.

##### Create a bar chart on the data in the range A1:B11  
As you can see the category labels on the negative side of the axis are obscured by the bars.  
_For this example I have already reversed the plot order of the bars to match that of the data, [see here for details](https://www.andypope.info/tips/tip007.htm)
_

|     |     |     |     |
| --- | --- | --- | --- |
|     | A   | B   | C   |
| 1   |     | Score |     |
| 2   | One | 0.18 | \-0.36 |
| 3   | Two | \-0.36 | 0.47 |
| 4   | Three | 0.47 | \-0.36 |
| 5   | Four | \-0.17 | 0.47 |
| 6   | Five | 0.08 | \-0.36 |
| 7   | Six | \-0.23 | 0.47 |
| 8   | Seven | 0.44 | \-0.36 |
| 9   | Eight | 0.20 | \-0.36 |
| 10  | Nine | \-0.09 | 0.47 |
| 11  | Ten | \-0.07 | 0.47 |

![](https://www.andypope.info/charts/posneg1.gif)

##### One possible way around this is to set category axis tick mark labels to the Low position.

 ![](https://www.andypope.info/charts/posneg2.gif)

##### But to keep the text next to the axis whilst not being obscured by the bars you can do the following.

##### Add the following formula to C2: \=IF(B2<0,MAX($B$2:$B$11),MIN($B$2:$B$11))  
and then copy down to C11. Add this new data series to the chart.

 ![](https://www.andypope.info/charts/posneg11.gif)

##### Double click either series and change the Overlap value to 100

 ![](https://www.andypope.info/charts/posneg4.gif)

 ![](https://www.andypope.info/charts/posneg3.gif)

##### Now format the category axis to remove the axis labels by setting the Tick mark labels to None.

 ![](https://www.andypope.info/charts/posneg6.gif)

##### Apply Data labels to the new dummy series, displaying category name.

 ![](https://www.andypope.info/charts/posneg7.gif)

##### Change the data labels position to Inside Base

 ![](https://www.andypope.info/charts/posneg9.gif)

##### giving you a chart that displays the category name opposite the bar

 ![](https://www.andypope.info/charts/posneg8.gif)

##### Finally set the Pattern Fill and Border to None for the dummy series. Remove the legend.

 ![](https://www.andypope.info/charts/posneg10.gif)

##### This technique will also work with column charts

       

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/posnegdlabels.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope