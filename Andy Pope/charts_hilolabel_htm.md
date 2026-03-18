# Hi-Lo labels

**Source:** https://www.andypope.info/charts/hilolabel.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Label high-low line with values

  

![](https://www.andypope.info/charts/hiloline1.gif)

##### Use an additional data series plotted on the secondary axis to add values to the high-low lines. 

 

#####  

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     | A   | B   | C   | D   | E   |
| 1   |     | Actual | Expect | HI-Lo | Label |
| 2   | Jan | 8   | 6   | \=B2+((C2-B2)/2) | \=C2-B2 |
| 3   | Feb | 7   | 5   | \=B3+((C3-B3)/2) | \=C3-B3 |
| 4   | Mar | 7   | 1   | \=B4+((C4-B4)/2) | \=C4-B4 |
| 5   | Apr | 1   | 3   | \=B5+((C5-B5)/2) | \=C5-B5 |
| 6   | May | 9   | 10  | \=B6+((C6-B6)/2) | \=C6-B6 |
| 7   | Jun | 3   | 5   | \=B7+((C7-B7)/2) | \=C7-B7 |
| 8   | Jul | 1   | 7   | \=B8+((C8-B8)/2) | \=C8-B8 |
| 9   | Aug | 8   | 4   | \=B9+((C9-B9)/2) | \=C9-B9 |
| 10  | Sep | 6   | 6   | \=B10+((C10-B10)/2) | \=C10-B10 |
| 11  | Oct | 1   | 10  | \=B11+((C11-B11)/2) | \=C11-B11 |
| 12  | Nov | 6   | 6   | \=B12+((C12-B12)/2) | \=C12-B12 |
| 13  | Dec | 8   | 6   | \=B13+((C13-B13)/2) | \=C13-B13 |

##### The formulas in column D define the mid-point position between the 2 lines.  
The formulas in column E define the actual distance between the 2 lines and are also used as the category labels for the secondary x axis. Whilst the secondary x axis is not displayed the values can be used automatically by the data labels.

  

##### Using the chart wizard create a line chart based on the range A1:D13

 ![](https://www.andypope.info/charts/hiloline2.gif) 

##### Double click the Hi-Lo data series and change the series to the secondary axis

 ![](https://www.andypope.info/charts/hiloline4.gif)

![](https://www.andypope.info/charts/hiloline3.gif)

 

##### Use the chart options dialog to enable the secondary x axis.

 ![](https://www.andypope.info/charts/hiloline6.gif)

![](https://www.andypope.info/charts/hiloline5.gif)

 

##### Use the Source data dialog do set the secondary category axis labels to the range E2:E13

 ![](https://www.andypope.info/charts/hiloline8.gif) 

![](https://www.andypope.info/charts/hiloline7.gif)

 

##### Format the secondary x axis so the tick marks and labels are not displayed.

 ![](https://www.andypope.info/charts/hiloline10.gif)

![](https://www.andypope.info/charts/hiloline9.gif)

 

##### Apply data labels to the Hi-Lo series. Display the Category values.

 ![](https://www.andypope.info/charts/hiloline11.gif)   

##### Apply the High-Low lines the to series and format the line to have no pattern.

  ![](https://www.andypope.info/charts/hiloline12.gif)   

##### Double click the data labels and change the label position to Center.

  ![](https://www.andypope.info/charts/hiloline14.gif)

![](https://www.andypope.info/charts/hiloline13.gif)

   

##### Final tidy up the formatting of the high-low lines.  
Set the background font to Opaque so the values are not obscured by the lines.  
Remove the extra data series from the [legend](https://www.andypope.info/charts/deletelegendentry.htm)
.

  ![](https://www.andypope.info/charts/hiloline17.gif)

![](https://www.andypope.info/charts/hiloline15.gif)

      

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/hilolabel.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope