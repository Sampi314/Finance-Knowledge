# Shape adjustment

**Source:** https://www.andypope.info/tips/tip013.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Shape Adjustment in xl2007

Many autoshapes have additional adjustments that be made to then to alter their appearance. ![](https://www.andypope.info/tips/adjust01.PNG)  
When a shape is selected in addition to the normal sizing handles, in white, the yellow adjustment handle(s) are displayed. You can click and drag one of the handles to alter the shape. When dragging a semi transparent view of the new shape is displayed. ![](https://www.andypope.info/tips/adjust02.PNG) Here we are dragging the handle to the right and decreasing the crosses thickness. ![](https://www.andypope.info/tips/adjust03.PNG) Here we are dragging the handle to the left and increasing the crosses thickness. The number of adjustment handles is dependent upon the shape. Here is an example of a shape with 3 adjustment handles ![](https://www.andypope.info/tips/adjust04.PNG)  
  
You can use VBA to alter the adjustment values of a shape.

ActiveSheet.Shapes("Cross 1").Adjustments(1) = 0.5

The value is usually a number in the range 0 to 1. Although for some shapes, such as the trapezoid, the value is a ratio. The download workbook contains a table of shapes and the number of adjustment they have. It also has a sheet for each of the adjustments levels.  
On some I have used a user defined function to allow you to change the adjustment values for the shapes on the sheet via scroll bar controls.  
Shape\_adjustments [![](https://www.andypope.info/Images/download.gif)](https://www.andypope.info/tips/Shape_adjustments.zip)
(86kb)

Created 3rd May 2008

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip013.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope