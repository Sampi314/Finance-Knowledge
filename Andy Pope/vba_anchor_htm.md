# Anchor controls

**Source:** https://www.andypope.info/vba/anchor.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Anchor controls and resizing userform

  

![](https://www.andypope.info/vba/Anchor.JPG)
---------------------------------------------

##### This is a class object that allows for automatic resizing of controls as the userform is resized.  
  
All the code to resize and reposition the controls is handled within the class. There is no complex API code required.  
  
The default action is to anchor controls to the top and left position of the form. This means that they maintain their position and size. You can override this setting for any of the controls. For example the Ok button in the userform above has been set to have anchors for Bottom and Right. This means that the distance from the bottom of the control and the bottom of the userform is maintained. The same for the Right edges. This results in the controls size remaining constant but it's location in anchored to the bottom right corner.

   

##### Private Sub UserForm\_Initialize()  
  
    Set m\_clsAnchors = New CAnchors  
      
    Set m\_clsAnchors.Parent = Me  
      
    ' restrict minimum size of userform  
    m\_clsAnchors.MinimumWidth = 45  
    m\_clsAnchors.MinimumHeight = 250  
      
    With m\_clsAnchors  
        .Anchor("Textbox1").AnchorStyle = enumAnchorStyleLeft Or enumAnchorStyleRight  
        .Anchor("cmdBrowse").AnchorStyle = enumAnchorStyleTop Or enumAnchorStyleRight  
        .Anchor("labDiv1").AnchorStyle = enumAnchorStyleLeft Or enumAnchorStyleRight  
        With .Anchor("frame1")  
            .AnchorStyle = enumAnchorStyleLeft Or enumAnchorStyleRight Or \_  
                           enumAnchorStyleBottom Or enumAnchorStyleTop  
            .MinimumHeight = 120  
        End With  
        .Anchor("listbox1").AnchorStyle = enumAnchorStyleLeft Or \_  
                                          enumAnchorStyleRight Or \_  
                                          enumAnchorStyleBottom Or \_  
                                          enumAnchorStyleTop  
        With .Anchor("cmdClear")  
            .AnchorStyle = enumAnchorStyleBottom Or enumAnchorStyleRight  
            .MinimumTop = 90  
        End With  
          
        .Anchor("labDiv2").AnchorStyle = enumAnchorStyleLeft Or \_  
                                         enumAnchorStyleRight Or \_                                         enumAnchorStyleBottom  
        .Anchor("cmdAbout").AnchorStyle = enumAnchorStyleLeft Or enumAnchorStyleBottom  
        .Anchor("checkbox1").AnchorStyle = enumAnchorStyleBottom  
        .Anchor("cmdOk").AnchorStyle = enumAnchorStyleBottom Or enumAnchorStyleRight  
    End With  
      
    ' live updates whilst resizing  
    CheckBox1.Value = True  
    ListBox1.RowSource = "B12:B19"  
      
End Sub

##### To use this in your projects you need to :-

> *   ##### include the 2 class modules.
>     
> *   ##### the enumeration declaration in the code module.
>     
> *   ##### in the userform itself you need to declare a private class object and set the Parent reference to the userform
>     

##### All existing controls will be added when the Parent assignment is made. This includes controls added dynamically, as long as  the controls where added before the Parent assignment. For controls added to the userform afterwards you can use the Add method to add additional controls. 

##### ![](https://www.andypope.info/images/xl2000.gif) [Example](https://www.andypope.info/vba/AnchorControls.zip)
 workbook

##### This will work in xl97 if you replace the enum with constant names instead.

    
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/AnchorControls.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/anchor.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope