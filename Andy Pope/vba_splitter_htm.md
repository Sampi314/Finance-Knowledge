# Splitter

**Source:** https://www.andypope.info/vba/splitter.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Userform Splitter class

   ![](https://www.andypope.info/images/xl2000.gif) (xl2000 and above)

![](https://www.andypope.info/vba/splitter.gif)
-----------------------------------------------

##### The workbook contains a class module, CAJPiSplitter, which can be added to a project to allow dynamic creation of a splitter control. The control can be used to resize controls on a userform. In the screen shot above the splitters have been position in and around listbox controls.

 

##### Example of vba required to setup a splitter control

 

##### ' create splitter between listboxes on left and right

##### Set m\_clsSplitterH = New CAJPiSplitter  
' Initialize splitter  
m\_clsSplitterH.Initialize Me  
' Specify which controls are to the left of the splitter  
m\_clsSplitterH.AddControlsLeft ListBox1, ListBox4  
' Specify which controls are to the right of the splitter  
m\_clsSplitterH.AddControlsRight ListBox2, ListBox3  
' Color background of grab handle to green  
m\_clsSplitterH.GrabHandleBackcolor = RGB(0, 255, 0)

##### [Example](https://www.andypope.info/vba/MSplitter.zip)
 workbook

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/MSplitter.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/splitter.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope