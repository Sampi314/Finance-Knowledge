# Draw on userform

**Source:** https://www.andypope.info/vba/userformdraw.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Drawing on userform

 

|     |     |
| --- | --- |
|     | (Excel 2000 and above)<br><br>![](https://www.andypope.info/vba/ufd1.gif)<br>------------------------------------------- |
|     | ##### The question of drawing lines and shapes on a userform comes up quite often.   <br>The normal approach for straight horizontal or vertical lines is to use the border of a label control and set its height or width to 1.   <br>When it comes to anything more fancy then the approach is to create the drawing on the worksheet using the built-in auto-shapes and then at design time manual copy and paste it to an image control's picture property.   <br>Or for the brave you could go down the API route.<br><br>##### I have taken the auto-shape route. The main differences being that shapes can be added at run time and multiple shapes can be handled.  <br>Shapes can be created and formatted as required before they are painted to the userform. <br><br>##### The example above is a very gaudy example of what is possible.<br><br>##### Here is the syntax used to create the blue box<br><br>Set shpTemp = m\_objDrawing.Box(10, 10, 40, 30)<br>If Not shpTemp Is Nothing Then <br>    shpTemp.Fill.ForeColor.SchemeColor = 12<br>End If<br><br>##### As you can see it is very similar to normal VBA code used when adding and formatting auto-shapes.<br><br>##### I have included two versions of the same demonstration for down loading.   <br>One version contains all the modules and class code within a project. It makes seeing the demonstration easier but requires extra work sharing the code if used on other projects. <br><br>##### Download the [Self contained demonstration](https://www.andypope.info/vba/contained_UFD.zip) <br><br>##### The other version of the demonstration requires the UFDraw.xla to be loaded in order for it to work. <br><br>##### If you are using Excel 2000 then the code will automatically try and locate and load the file. Failing that it will give you the choice to locate the file manually.<br><br>##### If you are using versions xl2002 or xl2003 then you will need to adjust your security setting to allow the code to automatically set vbproject references.  <br>  <br>This message box will be displayed if you have not enabled 'Trust access to Visual Basic Projects'<br><br>![](https://www.andypope.info/vba/ufd2.gif)<br><br>##### The is the dialog needed to change the setting.<br><br>![](https://www.andypope.info/vba/ufd3.gif)<br><br>##### If you load the xla manually then you can run the Demo macro rather than the DemoUserformDrawing macro, which is linked to the button on the worksheet.<br><br>##### Download the [XLA demonstration](https://www.andypope.info/vba/UFD.zip) |
|     |     |
|     |

    
Download the self contained demonstration  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/contained_UFD.zip)
  
  
Download the XLA demonstration  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/UFD.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/userformdraw.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope