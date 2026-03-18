# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng34.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

  

RE: setting the radius of a pie chart
-------------------------------------

![](https://www.andypope.info/ngs/ng34_1.gif)  ![](https://www.andypope.info/ngs/ng34_2.gif)
--------------------------------------------------------------------------------------------

![](https://www.andypope.info/ngs/ng34_3.gif)  ![](https://www.andypope.info/ngs/ng34_4.gif)

 

##### The plotarea size of the charts is changed in proportion to its total value in comparison with the other pie charts.

##### Here is the data used to create the 4 separate pie charts.

![](https://www.andypope.info/ngs/ng34_5.gif)

##### Here are the formula used for Pie1. The other pies use similar formula

![](https://www.andypope.info/ngs/ng34_6.gif)

##### The sizing is done via VBA code

Sub SizePies()
'
' Resize pie charts plot area according to a
'
Dim sngNormalSize As Single
Dim objCht As ChartObject
Dim rngSizes As Range
Dim intIndex As Integer
Dim sngTop As Single
Dim sngWidth As Single

' size proportions of pies
Set rngSizes = ActiveSheet.Range("B9:E9")
Set objCht = ActiveSheet.ChartObjects(1)

' Using first chart as point of reference
sngNormalSize = objCht.Chart.PlotArea.Width
sngTop = objCht.Chart.PlotArea.Top

' go thru and resize each pie
For Each objCht In ActiveSheet.ChartObjects
    With objCht.Chart
        intIndex = intIndex + 1
        sngWidth = sngNormalSize \* rngSizes.Cells(1, intIndex)
        If sngWidth > 10 Then
            .PlotArea.Width = sngWidth
            .PlotArea.Left = (.ChartArea.Width - .PlotArea.Width) / 2
            .PlotArea.Top = sngTop + ((.ChartArea.Height - sngTop) - .PlotArea.Height) / 2
        End If
    End With
Next

End Sub

##### This [workbook](https://www.andypope.info/ngs/ng34.zip)
 contains an all the formula, charts and VBA code.

 

  

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng34.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope