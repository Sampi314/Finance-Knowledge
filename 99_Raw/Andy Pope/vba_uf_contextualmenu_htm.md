# Contextual menu

**Source:** https://www.andypope.info/vba/uf_contextualmenu.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Userform Contextual Menu class code

 

|     |     |
| --- | --- |
|     | ![](https://www.andypope.info/vba/ufcmenu_1.png)<br>------------------------------------------------ |
|     | ##### The class module handles the construction of the contextual menu, the capture of right clicking in textboxes and the actual Cut. Copy and Paste actions. The class makes use of the userform's ActiveControl object. The code even handles controls within container controls such as Frames and Multipage.<br><br>#####   <br>The follow Initialization code, from the userform, shows how simple it is to define and use the class object. You only need declare a variable to the object and then set a reference for each textbox you want to have contextual menu capabilities.  <br><br>Private m\_colContextMenus As Collection  <br>  <br>Private Sub UserForm\_Initialize()  <br>  <br>    Dim clsContextMenu As CTextBox\_ContextMenu  <br>  <br>    Set m\_colContextMenus = New Collection  <br>  <br>    Set clsContextMenu = New CTextBox\_ContextMenu  <br>    With clsContextMenu  <br>        Set .TBox = UserForm1.TextBox1  <br>        Set .Parent = Me  <br>    End With  <br>    m\_colContextMenus.Add clsContextMenu, CStr(m\_colContextMenus.Count + 1)  <br>  <br>    Set clsContextMenu = New CTextBox\_ContextMenu  <br>    With clsContextMenu  <br>        Set .TBox = UserForm1.TextBox2  <br>        Set .Parent = Me  <br>    End With  <br>    m\_colContextMenus.Add clsContextMenu, CStr(m\_colContextMenus.Count + 1)  <br>  <br>    Set clsContextMenu = New CTextBox\_ContextMenu  <br>    With clsContextMenu  <br>        Set .TBox = UserForm1.TextBox3  <br>        Set .Parent = Me  <br>    End With  <br>    m\_colContextMenus.Add clsContextMenu, CStr(m\_colContextMenus.Count + 1)  <br>      <br>    Set clsContextMenu = New CTextBox\_ContextMenu  <br>    With clsContextMenu  <br>        Set .TBox = UserForm1.TextBox4  <br>        Set .Parent = Me  <br>    End With  <br>    m\_colContextMenus.Add clsContextMenu, CStr(m\_colContextMenus.Count + 1)  <br>          <br>    Set clsContextMenu = New CTextBox\_ContextMenu  <br>    With clsContextMenu  <br>        Set .TBox = UserForm1.TextBox5  <br>        Set .Parent = Me  <br>    End With  <br>    m\_colContextMenus.Add clsContextMenu, CStr(m\_colContextMenus.Count + 1)  <br>          <br>End Sub |
|     |     |
|     |

    
Download example workbook which contains both .xls and .xlsm files  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/UF_ContextualMenu.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/uf_contextualmenu.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope