# Listbox Mover

**Source:** https://www.andypope.info/vba/listboxmover.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Moving listbox items class code

 

|     |     |
| --- | --- |
|     | ![](https://www.andypope.info/vba/listmover.gif)<br>------------------------------------------------ |
|     | ##### The class module handles the moving of listbox items up and down or between two specified listboxes.  <br>  <br>If the listbox is set to multi-select the selected items will be moved up and down whilst retaining the spacing. Once a item reaches the top or bottom it will stop being moved and the spacing between that and the nearest selected item will be reduced. This will continue until all selected items are position at the top or bottom of the list. When the listbox contains multiple columns all the content of each line item is also repositioned.  <br>  <br>When transferring list items between listboxes it is possible to either remove or retain selected items in the original listbox. When items are moved between listboxes the items are always appended to the existing content. No ordering is applied or retained.  <br>  <br>The class module will not function for listboxes that are populated via the RowSource method.  <br>  <br>The follow code, from the userform, shows how simple it is to define an use the class object.  <br>You only need declare a variable to the object and then set a reference for the listbox to be used and the buttons that control the desired action.  <br><br>Private m\_clsListMoveUpDown As CListMover  <br>Private m\_clsListMoveIn As CListMover  <br>Private m\_clsListMoveOut As CListMover  <br>  <br>Private Sub UserForm\_Initialize()  <br>  <br>    Set m\_clsListMoveUpDown = New CListMover  <br>    With m\_clsListMoveUpDown  <br>        Set .MoveDownButton = Me.cmdDown  <br>        Set .MoveUpButton = Me.cmdUp  <br>        Set .UpDownList = Me.ListBox1  <br>    End With  <br>      <br>    Set m\_clsListMoveIn = New CListMover  <br>    With m\_clsListMoveIn  <br>        Set .TransferButton = Me.cmdMoveIn  <br>        Set .TransferFromList = Me.ListBox2  <br>        Set .TransferToList = Me.ListBox3  <br>        .RemoveItemOnTransfer = CheckBox1.Value  <br>    End With  <br>  <br>    Set m\_clsListMoveOut = New CListMover  <br>    With m\_clsListMoveOut  <br>        Set .TransferButton = Me.cmdMoveOut  <br>        Set .TransferFromList = Me.ListBox3  <br>        Set .TransferToList = Me.ListBox2  <br>        .RemoveItemOnTransfer = True  <br>    End With  <br>      <br>End Sub  <br> <br><br>##### The [example workbook](https://www.andypope.info/vba/ListBoxMover2.zip)<br> contains the demonstration userform and the class code. |
|     |     |
|     |

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/ListBoxMover2.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/listboxmover.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope