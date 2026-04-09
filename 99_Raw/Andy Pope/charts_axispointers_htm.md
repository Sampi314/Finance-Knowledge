# Axis pointer

**Source:** https://www.andypope.info/charts/axispointers.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Axis pointer

![](https://www.andypope.info/charts/axispointer4.gif)  
Using a data label on a dummy data series.  
Here is our data set. The actual chart data is in the range A1:B6  
The values in A10:B10 are for positioning the dummy data point

|     |     |     |
| --- | --- | --- |
|     | A   | B   |
| 1   |     | My Data |
| 2   | Jan | 2   |
| 3   | Feb | 3.5 |
| 4   | Mar | 4   |
| 5   | Apr | 5.5 |
| 6   | May | 8   |
| 7   |     |     |
| 8   |     |     |
| 9   | X   | Y   |
| 10  | 5.5 | 0   |

  
Select the range A1:B6 and use the chart wizard to create a standard Line chart.  
![](https://www.andypope.info/charts/axispointer1.gif)  
Right click the chart, which will display a popup menu, select the Source Data... item. Add a new data series, which I have called 'Axis Arrow'  
![](https://www.andypope.info/charts/axispointer2.gif)  
Change the Chart Type of the 'Axis Arrow' data series to XY Scatter, markers only. Format the 'Axis Arrow' data series so Value data labels are displayed.  
![](https://www.andypope.info/charts/axispointer3.gif)  
Then use the Source Data dialog again to set the X and Y ranges.  
![](https://www.andypope.info/charts/axispointer6.gif)  
Edit the data label and replace the text with 4. If we then format the data label to use the Marlett font we will get a right hand arrow head. Increase the font size to suit your chart. Also adjust the label position so that it is centered over the data point.  
![](https://www.andypope.info/charts/axispointer5.gif)  
This will then give use the axis pointer.  
![](https://www.andypope.info/charts/axispointer4.gif)  
The same technique can be adapted for the Y axis.

|     |     |     |
| --- | --- | --- |
| ##### 3 | ##### 3 | ##### Left |
| ##### 4 | ##### 4 | ##### Right |
| ##### 5 | ##### 5 | ##### Up |
| ##### 6 | ##### 6 | ##### Down |

Using a custom marker on a dummy series. Another way if to use a custom data marker as the pointer.  
Create the chart and add a new data series as described above. No need for data labels this time. ![](https://www.andypope.info/charts/axispointer8.gif) Create a pointer using the Auto shapes. ![](https://www.andypope.info/charts/axispointer7.gif) Use the clipboard to copy and paste the autoshape to the data series marker. Select the autoshape and copy (CTRL+C) Select the data point and paste (CTRL+V) ![](https://www.andypope.info/charts/axispointer9.gif) Then use the Source Data dialog to set the X and Y ranges. ![](https://www.andypope.info/charts/axispointer10.gif) Once again the technique can be adapted for the Y axis.Created August 2004

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/axispointers.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope