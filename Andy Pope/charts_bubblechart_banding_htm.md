# Plot area banding

**Source:** https://www.andypope.info/charts/bubblechart_banding.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Banding Plot Area of Bubble chart

  
![](https://www.andypope.info/charts/bubband1.gif)  
The normal techniques used to create banding colours in the plot area will not work for Bubble charts as they do are one of the chart styles that can not be combined.  
To get around this problem we will use a second chart to handle the banding and use some VBA code to align the plot areas of both charts. Of course if you wanted you could do it manually.  
First create a bubble chart in the normal way with 3 sets of data for X, Y and size.  
![](https://www.andypope.info/charts/bubband2.gif)

![](https://www.andypope.info/charts/bubband3.gif)

##### You will need to set the Pattern of the Chart Area and Plot Area to be none. This will make the chart transparent when not selected.

|     |     |
| --- | --- |
| Excel 2003 | Excel 2007 |
| ![](https://www.andypope.info/charts/bubband4.gif) | ![](https://www.andypope.info/charts/bubband5.gif) |

##### The other thing will need to do is fix the Value axis. The reason for this is we want to align the bands on one chart with the values on another and if the axis is not fixed on the chart with the banding we will have a gap at the top of the plotarea.

|     |     |
| --- | --- |
| Excel 2003 | Excel 2007 |
| ![](https://www.andypope.info/charts/bubband6.gif) | ![](https://www.andypope.info/charts/bubband7.gif) |

##### We now need to create a clustered column chart for the banding, based on the data in F1:G4.  
The values specify the height of each of the bands. Not that you will need to plot the data by rows in order to get 3 series rather than 1 series with 3 categories.

![](https://www.andypope.info/charts/bubband8.gif)

##### Then format the cluster column chart to have a Overlap of 100 and Gap width of 100. Once the Value axis is set to the same values as the bubble chart the columns will fill the whole of the plot area.  
Change the colour of each of the bands to suit. I have gone with the traffic light Red, Yellow, Green.![](https://www.andypope.info/charts/bubband9.gif)

|     |     |
| --- | --- |
| Excel 2003 | Excel 2007 |
| ![](https://www.andypope.info/charts/bubband10.gif) | ![](https://www.andypope.info/charts/bubband11.gif) |

##### To complete the banding chart you will need to remove Legend, any chart titles, Category axis labels and tickmarks. The same for the Value axis. You should end up with a chart that looks like this. Do not worry about the size or position of the chart or it's plot area. The VBA routine will deal with all of that.

![](https://www.andypope.info/charts/bubband12.gif)

##### The only thing left to do is identify each charts name so we can tell the routine which is the bubble chart and which is the banding one. For this post I have kept things relatively simple and not built a UI to allow selection of each chart.  
In Excel 2003 the quickest way is to select the chart whilst holding the SHIFT key. This will select the chart as an object and display it's name in the Name Box, next to the formula bar. In the example workbook the bubble chart is called "Chart 8"  
![](https://www.andypope.info/charts/bubband13.gif)

##### For Excel 2007 it is much easier as the charts name is displayed on the Layout tab within the Properties group.  
![](https://www.andypope.info/charts/bubband14.gif)

##### Once you have the names of both charts you can enter them in the code.

Sub Test()  
  
    With ActiveSheet  
        AlignPlotAreas .ChartObjects("Chart 8").Chart, .ChartObjects("Chart 12").Chart  
    End With  
      
End Sub 

##### This is the routine that positions the chart and plotarea.

  
Function AlignPlotAreas(TopChart As Chart, BottomChart As Chart)  
  
    Dim lngPreviousValue As Long  
      
    With TopChart.Parent  
        BottomChart.Parent.Left = .Left  
        BottomChart.Parent.Top = .Top  
        BottomChart.Parent.Width = .Width  
        BottomChart.Parent.Height = .Height  
    End With  
      
    ' reduce width/height so we can move area around without hitting edges  
    BottomChart.PlotArea.Width = TopChart.PlotArea.Width \* 0.5  
    BottomChart.PlotArea.Height = TopChart.PlotArea.Height \* 0.5  
      
    BottomChart.PlotArea.Left = TopChart.PlotArea.Left  
    lngPreviousValue = BottomChart.PlotArea.Left  
    Do While BottomChart.PlotArea.InsideLeft < TopChart.PlotArea.InsideLeft  
        BottomChart.PlotArea.Left = BottomChart.PlotArea.Left + 1  
        If lngPreviousValue = BottomChart.PlotArea.Left Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Left  
    Loop  
      
    lngPreviousValue = BottomChart.PlotArea.Left  
    Do While BottomChart.PlotArea.InsideLeft > TopChart.PlotArea.InsideLeft  
        BottomChart.PlotArea.Left = BottomChart.PlotArea.Left - 1  
        If lngPreviousValue = BottomChart.PlotArea.Left Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Left  
    Loop  
      
    BottomChart.PlotArea.Top = TopChart.PlotArea.Top  
    lngPreviousValue = BottomChart.PlotArea.Top  
    Do While BottomChart.PlotArea.InsideTop < TopChart.PlotArea.InsideTop  
        BottomChart.PlotArea.Top = BottomChart.PlotArea.Top + 1  
        If lngPreviousValue = BottomChart.PlotArea.Top Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Top  
    Loop  
      
    lngPreviousValue = BottomChart.PlotArea.Top  
    Do While BottomChart.PlotArea.InsideTop > TopChart.PlotArea.InsideTop  
        BottomChart.PlotArea.Top = BottomChart.PlotArea.Top - 1  
        If lngPreviousValue = BottomChart.PlotArea.Top Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Top  
    Loop  
      
    BottomChart.PlotArea.Width = TopChart.PlotArea.Width  
    lngPreviousValue = BottomChart.PlotArea.Width  
    Do While BottomChart.PlotArea.InsideWidth < TopChart.PlotArea.InsideWidth  
        BottomChart.PlotArea.Width = BottomChart.PlotArea.Width + 1  
        If lngPreviousValue = BottomChart.PlotArea.Width Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Width  
    Loop  
      
    lngPreviousValue = BottomChart.PlotArea.Width  
    Do While BottomChart.PlotArea.InsideWidth > TopChart.PlotArea.InsideWidth  
        BottomChart.PlotArea.Width = BottomChart.PlotArea.Width - 1  
        If lngPreviousValue = BottomChart.PlotArea.Width Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Width  
    Loop  
      
    BottomChart.PlotArea.Height = TopChart.PlotArea.Height  
    lngPreviousValue = BottomChart.PlotArea.Height  
    Do While BottomChart.PlotArea.InsideHeight < TopChart.PlotArea.InsideHeight  
        BottomChart.PlotArea.Height = BottomChart.PlotArea.Height + 1  
        If lngPreviousValue = BottomChart.PlotArea.Height Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Height  
    Loop  
      
    lngPreviousValue = BottomChart.PlotArea.Height  
    Do While BottomChart.PlotArea.InsideHeight > TopChart.PlotArea.InsideHeight  
        BottomChart.PlotArea.Height = BottomChart.PlotArea.Height - 1  
        If lngPreviousValue = BottomChart.PlotArea.Height Then  
            Exit Do  
        End If  
        lngPreviousValue = BottomChart.PlotArea.Height  
    Loop  
      
End Function  
 

##### The example file, [bubblebanding](https://www.andypope.info/charts/BubbleBands.zip)
 contains charts and VBA code.

[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/charts/BubbleBands.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/bubblechart_banding.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope