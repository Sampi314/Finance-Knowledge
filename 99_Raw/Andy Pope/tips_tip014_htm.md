# Error bars

**Source:** https://www.andypope.info/tips/tip014.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### VBA code to set custom error bars in xl2007

Here is code and example workbook on how to set Custom values for error bars in xl2007

Sub ErrorFromRange()  
  
Dim chtTemp As Chart  
Dim objSeries As Series  
Dim objErrBars As ErrorBars  
Dim rngUseErrors As Range  
Dim rngMinusX As Range  
Dim rngPlusX As Range  
Dim rngMinusY As Range  
Dim rngPlusY As Range  
  
Set chtTemp = ActiveSheet.ChartObjects(1).Chart  
Set objSeries = chtTemp.SeriesCollection(1)  
Set rngUseErrors = Range("N1:N4")  
Set rngMinusX = Range("D2:D10")  
Set rngPlusX = Range("E2:E10")  
Set rngMinusY = Range("F2:F10")  
Set rngPlusY = Range("G2:G10")  
  
If rngUseErrors.Cells(1, 1) Then  
    ' -X  
    If rngUseErrors.Cells(2, 1) Then  
        ' and +X  
        objSeries.ErrorBar xlX, xlErrorBarIncludeBoth, xlErrorBarTypeCustom, "='" & rngPlusX.Parent.Name & "'!" & rngPlusX.Address(, , xlR1C1), "'" & rngMinusX.Parent.Name & "'!" & rngMinusX.Address(, , xlR1C1)  
    Else  
        ' only  
        objSeries.ErrorBar xlX, xlErrorBarIncludeMinusValues, xlErrorBarTypeCustom, "", "='" & rngMinusX.Parent.Name & "'!" & rngMinusX.Address(, , xlR1C1)  
    End If  
ElseIf rngUseErrors.Cells(2, 1) Then  
    ' +X  
    objSeries.ErrorBar xlX, xlErrorBarIncludePlusValues, xlErrorBarTypeCustom, "='" & rngPlusX.Parent.Name & "'!" & rngPlusX.Address(, , xlR1C1), ""  
Else  
    objSeries.ErrorBar xlX, xlErrorBarIncludeNone, xlErrorBarTypeFixedValue  
End If  
  
If rngUseErrors.Cells(3, 1) Then  
    ' -Y  
    If rngUseErrors.Cells(4, 1) Then  
        ' and +Y  
        objSeries.ErrorBar xlY, xlErrorBarIncludeBoth, xlErrorBarTypeCustom, "='" & rngPlusY.Parent.Name & "'!" & rngPlusY.Address(, , xlR1C1), "='" & rngMinusY.Parent.Name & "'!" & rngMinusY.Address(, , xlR1C1)  
    Else  
    ' only  
        objSeries.ErrorBar xlY, xlErrorBarIncludeMinusValues, xlErrorBarTypeCustom, "", "='" & rngMinusY.Parent.Name & "'!" & rngMinusY.Address(, , xlR1C1)  
    End If  
ElseIf rngUseErrors.Cells(4, 1) Then  
    ' +Y  
    objSeries.ErrorBar xlY, xlErrorBarIncludePlusValues, xlErrorBarTypeCustom, "='" & rngPlusY.Parent.Name & "'!" & rngPlusY.Address(, , xlR1C1), ""  
Else  
    objSeries.ErrorBar xlY, xlErrorBarIncludeNone, xlErrorBarTypeFixedValue  
End If  
  
End Sub  
  

  
VBA Custom Error Bar code [![](https://www.andypope.info/Images/download.gif)](https://www.andypope.info/tips/CustomErrorBars.zip)
(18kb) [![](https://www.andypope.info/images/Thumbnails/download.jpg)](https://www.andypope.info/tips/CustomErrorBars.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip014.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope