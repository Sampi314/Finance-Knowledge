# Custom leader lines

**Source:** https://www.andypope.info/charts/customerleaderlines.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Custom leader lines

   

![](https://www.andypope.info/charts/cleader1.gif)

##### This chart has 2 textboxes for displaying information regarding the 1st and 4th slice. The custom leader lines will adjust along with the pie chart data to always connect the textbox corner with the two end points of the pie slice.

##### This effect is created by using a combination chart, pie and xy-scatter, and some math formula.

##### Below is all the data and formula required to create the chart. The highlighted cells contain the actual charted data.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | A   | B   | C   | D   | E   | F   |
| 1   |     | Auto leader lines |     | %   | Angle | Radius |
| 2   | a   | 3   |     | 0.272727273 | 98.18182 | 0.61 |
| 3   | b   | 1   |     | 0.090909091 | 32.72727 |     |
| 4   | c   | 1   |     | 0.090909091 | 32.72727 |     |
| 5   | d   | 3   |     | 0.272727273 | 98.18182 |     |
| 6   | e   | 3   |     | 0.272727273 | 98.18182 |     |
| 7   |     |     |     |     |     |     |
| 8   |     |     |     |     |     |     |
| 9   | Slice |     | X   | Y   |     |     |
| 10  | 1   | 90.00 | 3.74E-17 | 0.61 |     |     |
| 11  |     |     | 0.95 | 0.95 |     |     |
| 12  |     | \-8.18 | 0.603791 | \-0.086812051 |     |     |
| 13  |     |     |     |     |     |     |
| 14  | 4   | \-73.64 | 0.171857 | \-0.585290714 |     |     |
| 15  |     |     | \-0.95 | \-0.95 |     |     |
| 16  |     | \-171.82 | \-0.60379 | \-0.086812051 |     |     |

##### Formulas

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | A   | B   | C   | D   | E   | F   |
| 1   |     | Auto leader lines |     | %   | Angle | Radius |
| 2   | a   | 3   |     | \=B2/SUM($B$2:$B$6) | \=360\*D2 | 0.61 |
| 3   | b   | 1   |     | \=B3/SUM($B$2:$B$6) | \=360\*D3 |     |
| 4   | c   | 1   |     | \=B4/SUM($B$2:$B$6) | \=360\*D4 |     |
| 5   | d   | 3   |     | \=B5/SUM($B$2:$B$6) | \=360\*D5 |     |
| 6   | e   | 3   |     | \=B6/SUM($B$2:$B$6) | \=360\*D6 |     |
| 7   |     |     |     |     |     |     |
| 8   |     |     |     |     |     |     |
| 9   | Slice |     | X   | Y   |     |     |
| 10  | 1   | 90  | \=COS(RADIANS(B10))\*$F$2 | \=SIN(RADIANS(B10))\*$F$2 |     |     |
| 11  |     |     | 0.95 | 0.95 |     |     |
| 12  |     | \=B10-E2 | \=COS(RADIANS(B12))\*$F$2 | \=SIN(RADIANS(B12))\*$F$2 |     |     |
| 13  |     |     |     |     |     |     |
| 14  | 4   | \=90-SUM(E2:E4) | \=COS(RADIANS(B14))\*$F$2 | \=SIN(RADIANS(B14))\*$F$2 |     |     |
| 15  |     |     | \-0.95 | \-0.95 |     |     |
| 16  |     | \=B14-E5 | \=COS(RADIANS(B16))\*$F$2 | \=SIN(RADIANS(B16))\*$F$2 |     |     |

 

##### Although the finished chart is a pie chart it is easier to construct if we begin with the xy-scatter chart.

##### Select the range C10:D16 and use the chart wizard to create a standard xy-scatter chart.

 ![](https://www.andypope.info/charts/cleader2.gif) 

##### Use the source data dialog to add another series to the chart.

 ![](https://www.andypope.info/charts/cleader4.gif)

![](https://www.andypope.info/charts/cleader3.gif)

 

##### Select the 2nd data series and change the chart type to pie.

 

![](https://www.andypope.info/charts/cleader5.gif)

 

##### Use the source data to specify the location of data, B2:B6, and labels, A2:A6, for the pie chart.

 ![](https://www.andypope.info/charts/cleader7.gif)

![](https://www.andypope.info/charts/cleader6.gif)

 

##### Change the axis properties for both x and y axis. Set the minimum and maximum value to -1 and 1 respectively.

 ![](https://www.andypope.info/charts/cleader9.gif) 

##### The only problem with the chart in its current configuration is that the area available for the leader lines is restricted to the plot area, which is too close to the edge of the pie chart.

 ![](https://www.andypope.info/charts/cleader8.gif) 

##### To increase this area we need to explode and re assemble the pie chart.  
Select the pie and drag the slices away from the center. The further away you drag the slices the smaller the pie chart will end up.

 ![](https://www.andypope.info/charts/cleader10.gif) 

##### After exploding and thereby reducing the size of the pie we need to drag the slice back together. If you do this whilst all the slices are selected then the pie will return to its original size. You have to do each piece individually. So select the pie and then select an individual slice. Drag this back to the center and then repeat for all the other pieces.

 ![](https://www.andypope.info/charts/cleader11.gif) 

##### You now have a smaller pie chart which will allow more space for the leader lines.

##### The actual radius of the chart can be entered in to the cell F2  
The end point of the leader lines, where the 2 lines meet, is controlled by the values used in cells C11:D11 and C15:D15. The position of contact of the leader lines with the pies circumference is calculated via the formulas.

 ![](https://www.andypope.info/charts/cleader12.gif) 

##### Format both axis to remove lines, labels and tickmarks.

 ![](https://www.andypope.info/charts/cleader14.gif) 

##### You should now have a pie chart with leader lines for slices 1 and 4. This will automatically adjust for any changes in the pie charts data.

 ![](https://www.andypope.info/charts/cleader13.gif) 

##### Further formatting of the pie, leader lines, legend and chart can be applied.  
As can the textboxes used to hold any information needed.

        

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/customerleaderlines.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope