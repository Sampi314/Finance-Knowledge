# Set square area

**Source:** https://www.andypope.info/charts/SetSquareAxis.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Set Square Axis

 

|     |     |
| --- | --- |
|     | ![](https://www.andypope.info/charts/ssa_1.jpg)         ![](https://www.andypope.info/charts/ssa_2.jpg)<br>------------------------------------------------------------------------------------------------------- |
|     | #####  I would like to thank my forum buddy [shg](http://www.excelforum.com/members/shg.html)<br> for providing the material for this page.  <br><br>##### Scatter plots in Excel show data that has no intrinsic spatial component; e.g., time series of cash flows for financial applications, waveforms for engineering applications, etc. Left to its own devices, Excel sets chart scales automatically, adjusting them generally to maximize the area of the plot that contains the data within the overall plot area -- and generally does it pretty well.  <br>  <br>Sometimes, though, we use scatter plots where the x and y axes represent true linear dimensions, and in those cases, Excel's default behavior doesn't help at all. We'd like equal spans (the size of max - min on each axis) to be the same, so that squares, for example, are actually square. A sub in the attached workbook does that, and shows a simple example that compares what the sub does to what Excel does by default.  <br>  <br>In your own application, you (the user) first create a chart that has equal height and width for the plot area. Then as data changes, you pass the min and max x and y values to the sub and it adjusts the scales to have equal spans and the major unit to be common to both axes. In the example, the major unit is a fixed size, but you could compute it based on the data if you wish.  <br>  <br>There's another (and more practical) example at [http://www.excelforum.com/excel-general/672617-calculating-the-radius-of-a-curve.html](http://www.excelforum.com/excel-general/672617-calculating-the-radius-of-a-curve.html)<br>  <br>  <br><br>Function SetSquareAxes(cht As Chart, dBuf As Double, dInc As Double, \_  <br>                       ByVal xMin As Double, ByVal xMax As Double, \_  <br>                       ByVal yMin As Double, ByVal yMax As Double) As Boolean  <br>    ' shg 2009-0220  <br>  <br>    ' Sets the chart scales to  <br>    '   o   be of equal span  <br>    '   o   start and end on a multiple of dInc, and have dInc as the major unit  <br>    '   o   contain all points with a minimum buffer distance of dBuf to the edges  <br>    '   o   center the points in the plot area within the constraints above  <br>  <br>    ' E.g.,  <br>  <br>    '    SetSquareAxes Sheet1.ChartObjects(1).Chart, 100, 500, \_  <br>    '                  WorksheetFunction.Min(rngX.Value), \_  <br>    '                  WorksheetFunction.Max(rngX.Value), \_  <br>    '                  WorksheetFunction.Min(rngY.Value), \_  <br>    '                  WorksheetFunction.Max(rngY.Value)  <br>      <br>    ' Returns True if successful  <br>  <br>    Static WF   As WorksheetFunction  <br>    Dim xCtr    As Double  <br>    Dim yCtr    As Double  <br>    Dim dRad    As Double   ' half-dimension of bounding box  <br>    Dim dDelta  As Double   ' common span of x and y scales  <br>  <br>    ' verify cht is a scatterchart  <br>    Select Case cht.SeriesCollection(1).ChartType  <br>        Case xlXYScatter, xlXYScatterLines, xlXYScatterSmooth, \_  <br>             xlXYScatterLinesNoMarkers, xlXYScatterSmoothNoMarkers  <br>             ' all good ...  <br>        Case Else  <br>            MsgBox "Chart type must be XY (Scatter)", vbOKOnly, "SetSquareAxes"  <br>            Exit Function  <br>    End Select  <br>  <br>    If WF Is Nothing Then Set WF = WorksheetFunction  <br>  <br>    ' compute center and bounding box radius  <br>    xCtr = (xMax + xMin) / 2#  <br>    yCtr = (yMax + yMin) / 2#  <br>    dRad = WF.Max(xMax - xCtr, yMax - yCtr) + dBuf  <br>  <br>    ' compute the scale minima  <br>    xMin = Int((xCtr - dRad) / dInc) \* dInc  <br>    yMin = Int((yCtr - dRad) / dInc) \* dInc  <br>  <br>    ' compute the common span and the scale maxima  <br>    dDelta = WF.Ceiling(WF.Max(xMax - xMin, yMax - yMin) + dBuf, dInc)  <br>    xMax = xMin + dDelta  <br>    yMax = yMin + dDelta  <br>  <br>    With cht.Axes(xlCategory)  <br>        .MinimumScale = xMin  <br>        .MaximumScale = xMax  <br>        .MinorUnitIsAuto = True  <br>        .MajorUnitIsAuto = False  <br>        .MajorUnit = dInc  <br>    End With  <br>  <br>    With cht.Axes(xlValue)  <br>        .MinimumScale = yMin  <br>        .MaximumScale = yMax  <br>        .MinorUnitIsAuto = True  <br>        .MajorUnitIsAuto = False  <br>        .MajorUnit = dInc  <br>    End With  <br>    SetSquareAxes = True  <br>End Function <br><br>##### The example file, [setsquareaxis](https://www.andypope.info/charts/setsquareaxis.zip)<br> contains charts and VBA code. |
|     |     |

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/setsquareaxis.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/SetSquareAxis.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope