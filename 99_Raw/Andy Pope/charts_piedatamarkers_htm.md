# Pie data markers

**Source:** https://www.andypope.info/charts/piedatamarkers.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Pie chart data markers

   

![](https://www.andypope.info/charts/piemarker3.gif)

##### This is an example of using a pie chart as the custom marker within another chart.

##### You need to create a small pie chart that will be used as the custom marker.  
Format the chart area to have no fill pattern and no border.  
Format the slices as required.

##### ![](https://www.andypope.info/charts/piemarker1.gif)

##### To apply the chart as a data marker we first need to create a picture copy of it. This can be done manually within Excel. Hold the Shift key whilst selecting the pie chart.

##### ![](https://www.andypope.info/charts/piemarker6.gif)

##### Then whilst still holding the shift key click the Edit menu.  
Notice the appearance of a new menu item, Copy Picture.

##### ![](https://www.andypope.info/charts/piemarker7.gif)

##### Selecting Copy Picture... will display a dialog that allows you to set some characteristics of the image that will be created on the clipboard.

#####  ![](https://www.andypope.info/charts/piemarker8.gif)

##### On your xy scatter chart you need to click the data series and then click the appropriate data point.  
(See this tip for details of [manually selecting individual chart elements](https://www.andypope.info/tips/tip003.htm)
) 

##### With the data point selected you can paste the pie chart using CTRL+V

##### ![](https://www.andypope.info/charts/piemarker10.gif)

##### To do this for your whole chart you will need to change the data relating to the pie chart and the repeat the process of copying, selecting data point and pasting.

##### You can use VBA code to automate this process, which can be especially useful if the chart contains a lot of points or the data is changed at some point. As the pie data markers are static views of the data and are will not update with the data.

##### Sub PieMarkers()  
      
    Dim chtMarker As Chart  
    Dim chtMain As Chart  
    Dim intPoint As Integer  
    Dim rngRow As Range  
    Dim lngPointIndex As Long  
      
    Application.ScreenUpdating = False  
     ' reference to pie chart  
    Set chtMarker = ActiveSheet.ChartObjects("chtPieMarker").Chart  
     ' reference to chart that pie markers will be applied to  
    Set chtMain = ActiveSheet.ChartObjects(1).Chart  
      
     ' pie chart data which will be processed by rows  
    For Each rngRow In Range("F4:J11").Rows  
         ' assign new values to pie chart  
        chtMarker.SeriesCollection(1).Values = rngRow  
         ' copy pie  
        chtMarker.Parent.CopyPicture  xlScreen, xlPicture  
         ' paste to appropriate data point  
        lngPointIndex = lngPointIndex + 1  
        chtMain.SeriesCollection(1).Points(lngPointIndex).Paste  
    Next  
      
     ' release objects  
    Set chtMarker = Nothing  
    Set chtMain = Nothing  
    Application.ScreenUpdating = False  
      
End Sub

##### The same technique can be applied to a Bubble chart where the size of the pie is related to the bubble size value.

![](https://www.andypope.info/charts/piemarker2.gif)

##### It can also be applied to a line chart.

![](https://www.andypope.info/charts/piemarker4.gif)

##### The code and chart examples are contained within this [workbook](https://www.andypope.info/charts/piedatamarkers.zip)
.

       
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/piedatamarkers.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/piedatamarkers.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope