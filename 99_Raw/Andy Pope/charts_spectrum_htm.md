# Specturm

**Source:** https://www.andypope.info/charts/spectrum.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

Content  

XY scatter colouration plot
---------------------------

 

##### The chart in both cases is a standard xy scatter plot where the plot order of each data point determines the colour of the marker.

##### The first chart sets the data markers colour but due to the limit of the colour palette it produces a more stepped colouration.

 ![](https://www.andypope.info/charts/spectrum1.gif)

##### The second chart uses an autoshape as a custom marker. The colour of the custom marker is not restricted by the colour palette so the colouration is smoother.

![](https://www.andypope.info/charts/spectrum2.gif)

##### The code sets the data markers colour according to the points order within the data series.  
You can specify the start and finish colours and the number of steps between.

 

##### In order for the code below to work you will need to create 2 charts and insert a autoshape onto a worksheet. The autoshape should be named Marker.  
  
To name the autoshape select it and enter the new name in the Name box next to the formula bar.

![](https://www.andypope.info/charts/spectrum4.gif)

##### The code allows you to specify the start and finish colour of your spectrum. You can also specify the number of colours to define within the span.

 

##### Code module: MSpectrum

Option Explicit  
  
Sub Main()    Dim clsSpectrum As CSpectrum        Set clsSpectrum = New CSpectrum    With clsSpectrum  
        .Count = 56                       ' number of colours in spectrum  
        .StartColor = RGB(0, 0, 255) ' Blue   
        .EndColor = RGB(255, 0, 0)   ' Red  
        .CreateSpectrum    End With  
    UsingMarkers clsSpectrum, ActiveSheet.ChartObjects(1).Chart  
    UsingCustomMarkers clsSpectrum, ActiveSheet.ChartObjects(2).Chart    End Sub  
  
Sub UsingMarkers(Spectrum As CSpectrum, Cht As Chart)  
'  
' Using builtin color palette  
'  
    Dim lngIndex As Long  
    Dim intPoint As Integer  
        With Cht        With .SeriesCollection(1)            For intPoint = 1 To .Points.Count  
                lngIndex = intPoint \* (Spectrum.Count / .Points.Count)                With .Points(intPoint)  
                    .MarkerBackgroundColor = Spectrum.SpectrumColor(lngIndex)  
                    .MarkerForegroundColor = Spectrum.SpectrumColor(lngIndex)                End With  
            Next  
        End With  
    End With  
    End Sub  
Sub UsingCustomMarkers(Spectrum As CSpectrum, Cht As Chart)  
'  
' Use a shape as a custom marker  
'  
    Dim shpMarker As Shape    Dim lngIndex As Long  
    Dim intPoint As Integer  
        Application.ScreenUpdating = False  
    Set shpMarker = ActiveSheet.Shapes("Marker")    With Cht        With .SeriesCollection(1)            For intPoint = 1 To .Points.Count  
                lngIndex = intPoint \* (Spectrum.Count / .Points.Count)  
                shpMarker.Fill.ForeColor.RGB = Spectrum.SpectrumColor(lngIndex)  
                shpMarker.CopyPicture  
                .Points(intPoint).Paste            Next  
        End With  
    End With  
    Application.ScreenUpdating = True  
    End Sub  

 

##### Class module: CSpectrum

 Zilpher Coloured Code

Option Explicit  
  
Private Enum enumSpectrum  
    Red = 1  
    Green  
    Blue  
End Enum  
  
Private m\_lngStartColor As Long  
Private m\_lngEndColor As Long  
Private m\_lngCountColor As Long  
Private m\_lngSpectrum() As Long  
Private m\_blnUpdatedSpectrum As Boolean  
Public Property Let Count(RHS As Long)    If RHS < 1 Then  
        m\_lngCountColor = 1  
    ElseIf RHS > 255 Then  
        m\_lngCountColor = 255    Else  
        m\_lngCountColor = RHS    End If  
        m\_blnUpdatedSpectrum = False  
End Property  
Public Property Get Count() As Long  
    Count = m\_lngCountColorEnd Property  
Public Sub CreateSpectrum()  
'  
' Calculate the spread of colours  
'  
    Dim lngIndex As Long  
    Dim lngColor As Long  
    Dim sngSpreadRed As Single  
    Dim sngSpreadGreen As Single  
    Dim sngSpreadBlue As Single  
    Dim sngRed As Single  
    Dim sngGreen As Single  
    Dim sngBlue As Single  
        If m\_lngCountColor = 0 Then  
        m\_lngCountColor = 2        ReDim m\_lngSpectrum(m\_lngCountColor) As Long  
        m\_lngSpectrum(1) = m\_lngStartColor  
        m\_lngSpectrum(2) = m\_lngEndColor  
        m\_blnUpdatedSpectrum = True  
    End If  
        ReDim m\_lngSpectrum(m\_lngCountColor) As Long  
    m\_lngSpectrum(1) = m\_lngStartColor  
    m\_lngSpectrum(m\_lngCountColor) = m\_lngEndColor  
    sngRed = CSng(m\_Color2RGB(m\_lngSpectrum(1), Red))  
    sngGreen = CSng(m\_Color2RGB(m\_lngSpectrum(1), Green))  
    sngBlue = CSng(m\_Color2RGB(m\_lngSpectrum(1), Blue))  
      
    sngSpreadRed = (m\_Color2RGB(m\_lngSpectrum(m\_lngCountColor), Red) - sngRed) / m\_lngCountColor  
    sngSpreadGreen = (m\_Color2RGB(m\_lngSpectrum(m\_lngCountColor), Green) - sngGreen) / m\_lngCountColor  
    sngSpreadBlue = (m\_Color2RGB(m\_lngSpectrum(m\_lngCountColor), Blue) - sngBlue) / m\_lngCountColor        For lngIndex = 2 To m\_lngCountColor - 1  
        sngRed = sngRed + sngSpreadRed  
        sngGreen = sngGreen + sngSpreadGreen  
        sngBlue = sngBlue + sngSpreadBlue  
        m\_lngSpectrum(lngIndex) = RGB(CInt(sngRed), CInt(sngGreen), CInt(sngBlue))    Next  
        m\_blnUpdatedSpectrum = True  
    End Sub  
Private Function m\_Color2RGB(Color As Long, Element As enumSpectrum) As Long  
'  
' Return RGB element for given color  
'  
    Select Case Element    Case enumSpectrum.Red  
        m\_Color2RGB = Color \\ 256 ^ 0 And 255    Case enumSpectrum.Green  
        m\_Color2RGB = Color \\ 256 ^ 1 And 255    Case enumSpectrum.Blue  
        m\_Color2RGB = Color \\ 256 ^ 2 And 255    End Select  
    End Function  
  
Public Property Get SpectrumColor(Index As Long) As Long  
    If Index > m\_lngCountColor Then  
        SpectrumColor = m\_lngSpectrum(m\_lngCountColor)  
    ElseIf Index < 1 Then  
        SpectrumColor = m\_lngSpectrum(1)    Else  
        SpectrumColor = m\_lngSpectrum(Index)    End If  
End Property  
Public Property Let StartColor(RHS As Long)  
    m\_lngStartColor = RHS  
    m\_blnUpdatedSpectrum = False  
End Property  
Public Property Let EndColor(RHS As Long)  
    m\_lngEndColor = RHS  
    m\_blnUpdatedSpectrum = False  
End Property  
Public Property Get StartColor() As Long  
    StartColor = m\_lngStartColorEnd Property  
Public Property Get EndColor() As Long  
    EndColor = m\_lngEndColorEnd Property  
Private Sub Class\_Initialize()  
  
    ' default settings    m\_lngCountColor = 56  
    m\_lngStartColor = RGB(0, 0, 255)  ' blue  
    m\_lngEndColor = RGB(255, 0, 0)    ' red  
    m\_blnUpdatedSpectrum = False  
    CreateSpectrum    End Sub

  

  

##### The code and charts are contained within this [example workbook](https://www.andypope.info/charts/Spectrum.zip)

 

    

Last updated 28th April 2007

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/spectrum.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope