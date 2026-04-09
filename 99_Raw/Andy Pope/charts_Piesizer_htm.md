# Pie sizer

**Source:** https://www.andypope.info/charts/Piesizer.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Size Pie in relation to sum of data

 

|     |     |
| --- | --- |
|     | ![](https://www.andypope.info/charts/piesizer.gif)<br>---------------------------------------------------<br><br>##### The VBA code determines the pie chart with the largest sum of values and then resizes the plot areas of the other pie charts in proportion to the largest ones diameter or area.<br><br>##### The plot areas take there position from the largest pie chart. |
|     |
| #####    <br>Sub SizePies()  <br>'  <br>' Resize pie charts based on sum of the slice values  <br>' Either in relation to the diameter of the area  <br>'  <br>    Dim chtPies() As Chart  <br>    Dim chtBiggestPie As Chart  <br>    Dim dblTotal() As Double  <br>    Dim lngPieCount As Long  <br>    Dim objTemp As ChartObject  <br>    Dim objWSF As WorksheetFunction  <br>    Dim lngIndex As Long  <br>    Dim dblArea As Double  <br>      <br>    Set objWSF = Application.WorksheetFunction  <br>      <br>    For Each objTemp In ActiveSheet.ChartObjects  <br>        Select Case objTemp.Chart.ChartType  <br>        Case xl3DPie, xl3DPieExploded, xlPie, xlPieExploded  <br>            lngPieCount = lngPieCount + 1  <br>            ReDim Preserve dblTotal(lngPieCount) As Double  <br>            ReDim Preserve chtPies(lngPieCount) As Chart  <br>              <br>            Set chtPies(lngPieCount) = objTemp.Chart  <br>            dblTotal(lngPieCount) = objWSF.Sum(objTemp.Chart.SeriesCollection(1).Values)  <br>            If dblTotal(lngPieCount) > dblTotal(0) Then  <br>                dblTotal(0) = dblTotal(lngPieCount)  <br>                Set chtBiggestPie = chtPies(lngPieCount)  <br>            End If  <br>        End Select  <br>    Next  <br>      <br>    ' don't bother if only 1 chart or no data  <br>    If lngPieCount <= 1 Then Exit Sub  <br>    If dblTotal(0) = 0 Then Exit Sub  <br>      <br>    If Range("N4") Then  <br>        ' Size relative to diameter  <br>        For lngIndex = 1 To lngPieCount  <br>            With chtPies(lngIndex)  <br>                .ChartTitle.Text = Format$(dblTotal(lngIndex) \_  <br>/ dblTotal(0), "0.0%") & " D" & Format$(dblTotal(lngIndex), "0.0")  <br>                With .PlotArea  <br>                    .Width = chtBiggestPie.PlotArea.Width \* (dblTotal(lngIndex) / dblTotal(0))  <br>                    ' center plotarea  <br>                    .Left = chtBiggestPie.PlotArea.Left + \_  <br>((chtBiggestPie.PlotArea.Width - .Width) / 2)  <br>                    .Top = chtBiggestPie.PlotArea.Top + \_  <br>((chtBiggestPie.PlotArea.Height - .Height) / 2)  <br>                End With  <br>            End With  <br>        Next  <br>    End If  <br>      <br>    If Range("N6") Then  <br>        ' Size relative to area  <br>        dblArea = objWSF.Pi \* ((chtBiggestPie.PlotArea.Width / 2) ^ 2)  <br>        For lngIndex = 1 To lngPieCount  <br>            With chtPies(lngIndex)  <br>                .ChartTitle.Text = Format$(dblTotal(lngIndex) / dblTotal(0), "0.0%") & \_  <br>" A" & Format$(dblTotal(lngIndex), "0.0")  <br>                With .PlotArea  <br>                    .Width = (((dblArea \* (dblTotal(lngIndex) / dblTotal(0))) / objWSF.Pi) \_  <br>^ 0.5) \* 2  <br>                    ' center plotarea  <br>                    .Left = chtBiggestPie.PlotArea.Left + \_  <br>((chtBiggestPie.PlotArea.Width - .Width) / 2)  <br>                    .Top = chtBiggestPie.PlotArea.Top + \_  <br>((chtBiggestPie.PlotArea.Height - .Height) / 2)  <br>                End With  <br>            End With  <br>        Next  <br>    End If  <br>End Sub |
|     |
| ##### The [download](https://www.andypope.info/charts/PieSizer.zip)<br> contains the 9 pie charts and option buttons to all sizing according to diameter or area. |
|     |     |

  [![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/PieSizer.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/Piesizer.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope