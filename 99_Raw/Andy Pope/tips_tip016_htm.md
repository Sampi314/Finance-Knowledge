# VBA to delete chart title

**Source:** https://www.andypope.info/tips/tip016.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### VBA code to delete automatic chart title when plotting single series in xl2007

Here is code and an example workbook on how to work around the deletion of the automatic chart title added when plotting a single series chart via code.  
  
When the code inserts the chartobject and adds a single series Excel automatically uses the new series name as the chart title. Removal of the title should simply be a case of setting the HasTitle property to False. But there is a timing issue when running code and the setting to False is not applied. If you step through the code then the property is set correctly.  
  
Simply by forcing the chart title on you can then delete it with the standard code.  

Sub CreateChart()  
  
Dim chtTemp As Chart  
Dim serTemp As Series  
  
' Add chart.  
Set chtTemp = ActiveSheet.ChartObjects.Add(150, 50, 300, 250).Chart  
' Add series to chart.  
Set serTemp = chtTemp.SeriesCollection.NewSeries  
serTemp.Name = "Data Series"  
serTemp.Values = Range("B2:B5")  
serTemp.XValues = Range("A2:A5")  
  
' force chart title on so the following removal works  
chtTemp.HasTitle = True  
' remove default chart title  
chtTemp.HasTitle = False  
  
End Sub

VBA Remove automatic chart title code [![](https://www.andypope.info/Images/download.gif)](https://www.andypope.info/tips/RemoveChartTitle.zip)
(15kb) [![](https://www.andypope.info/images/Thumbnails/download.jpg)](https://www.andypope.info/tips/RemoveChartTitle.zip)
Created 1st May 2010

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip016.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope