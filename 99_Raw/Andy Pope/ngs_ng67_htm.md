# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng67.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Animated chart in PowerPoint

![](https://www.andypope.info/ngs/ng67d.png)  
  
I replied to a [post](http://chandoo.org/wp/2016/03/17/animated-charts-in-power-point/#comments)
 on Chandoo.org by _[Chirayu](http://chandoo.org/forum/members/chirayu.11314/)_ on animating a chart in PowerPoint.  
My suggestion was that VBA code was not required to alter the stack of images. Instead you could use the built in animated effects and triggers to display the required view of the select quarters data and hide the others  
  
This is an embedded <a target='\_blank' href='http://office.com'>Microsoft Office</a> presentation, powered by <a target='\_blank' href='http://office.com/webapps'>Office Online</a>.  
  
![](https://www.andypope.info/ngs/ng67a.png) Here is the animation pane showing the effects and triggers which vary which of the chart objects on the slide are shown at any one time.  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Also as an alternative to the VBA suggestion of altering the stack of images I used VBA to manipulate the chart series.  
The data within the chart needs to be layout as shown below. This will then create 5 series of columns. The Data series is used to display the out of focus columns for all months. The other 4 series are used to display each quarters data only.  
![](https://www.andypope.info/ngs/ng67c.png)  
  
The following VBA code is used to control the transparency of the quarter series.  
  
Option Explicit  
  
Sub FormatChart(VisibleSeries As String, HiddenSeries As Variant)  
  
    Dim item As Variant  
    With ActivePresentation.Slides(1).Shapes("Chart 3").Chart  
        .SeriesCollection(VisibleSeries).Format.Fill.Transparency = 0  
        For Each item In HiddenSeries  
            .SeriesCollection(item).Format.Fill.Transparency = 1  
        Next  
        .Refresh  
    End With  
End Sub  
  
Sub Q1\_Click()  
      
    FormatChart "Q1", Array("Q2", "Q3", "Q4")  
      
End Sub  
Sub Q4\_Click()  
      
    FormatChart "Q4", Array("Q1", "Q2", "Q3")  
      
End Sub  
Sub Q3\_Click()  
      
    FormatChart "Q3", Array("Q1", "Q2", "Q4")  
      
End Sub  
Sub Q2\_Click()  
      
    FormatChart "Q2", Array("Q1", "Q3", "Q4")  
      
End Sub  
  
  
  
Each of the Quarter shapes can then have a action assigned to them.  
  
![](https://www.andypope.info/ngs/ng67b.png)  
  
  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/ngs/ng67.zip)
[](https://www.andypope.info/ngs/Moveshapes.xlsm)

Created 19th March 2016

Last updated 19th March 2016 

  
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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng67.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope