# Resize userform

**Source:** https://www.andypope.info/vba/resizeform.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/vba.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Resize userform

 

|     |     |
| --- | --- |
|     | ![Form Resizer](https://www.andypope.info/vba/formresizer.png) <br>---------------------------------------------------------------<br><br>##### The clase code will add a control to the user form which will allow you to resize the form by dragging the resize handle. No complex APIs required just some code in the Mouse events of the control.<br><br>##### Userform Code<br><br>Option Explicit<br><br>Private m\_clsResizer As CResizer<br><br>Private Sub CommandButton1\_Click()<br><br>    Unload Me<br><br>End Sub<br><br>Private Sub CommandButton2\_Click()<br><br>    With Me<br><br>        .Move .Left, .Top, .Width \* 1.3, .Height \* 1.3<br><br>    End With<br><br>End Sub<br><br>Private Sub CommandButton3\_Click()<br><br>    With Me<br><br>        .Move .Left, .Top, .Width / 1.3, .Height / 1.3<br><br>    End With<br><br>End Sub<br><br>Private Sub UserForm\_Initialize()<br><br>    Set m\_clsResizer = New CResizer<br><br>    m\_clsResizer.Add Me<br><br>End Sub<br><br>Private Sub UserForm\_Terminate()<br><br>    Set m\_clsResizer = Nothing<br><br>End Sub |
|     | Class CResizer code  <br><br>Option Explicit<br><br>Private Const MFrameResizer = "FrameResizeGrab"<br><br>Private Const MResizer = "ResizeGrab"<br><br>Private WithEvents m\_objResizer As MSForms.Frame<br><br>Private m\_sngLeftResizePos As Single<br><br>Private m\_sngTopResizePos As Single<br><br>Private m\_blnResizing As Single<br><br>Private WithEvents m\_frmParent As MSForms.UserForm<br><br>Private m\_objParent As Object<br><br>Private Sub Class\_Terminate()<br><br>    m\_objParent.Controls.Remove MResizer<br><br>End Sub<br><br>Private Sub m\_frmParent\_Layout()<br><br>    If Not m\_blnResizing Then<br><br>        With m\_objResizer<br><br>            .Top = m\_objParent.InsideHeight - .Height<br><br>            .Left = m\_objParent.InsideWidth - .Width<br><br>        End With<br><br>    End If<br><br>End Sub<br><br>Private Sub m\_objResizer\_MouseDown(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)<br><br>    If Button = 1 Then<br><br>        m\_sngLeftResizePos = X<br><br>        m\_sngTopResizePos = Y<br><br>        m\_blnResizing = True<br><br>    End If<br><br>End Sub<br><br>Private Sub m\_objResizer\_MouseMove(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)<br><br>    If Button = 1 Then<br><br>        With m\_objResizer<br><br>            .Move .Left + X - m\_sngLeftResizePos, .Top + Y - m\_sngTopResizePos<br><br>            m\_objParent.Width = m\_objParent.Width + X - m\_sngLeftResizePos<br><br>            m\_objParent.Height = m\_objParent.Height + Y - m\_sngTopResizePos<br><br>            .Left = m\_objParent.InsideWidth - .Width<br><br>            .Top = m\_objParent.InsideHeight - .Height<br><br>        End With<br><br>    End If<br><br>End Sub<br><br>Private Sub m\_objResizer\_MouseUp(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)<br><br>    If Button = 1 Then<br><br>        m\_blnResizing = False<br><br>    End If<br><br>End Sub<br><br>Public Function Add(Parent As Object) As MSForms.Frame<br><br>'<br><br>' add resizing control to bottom righthand corner of userform<br><br>'<br><br>    Dim labTemp As MSForms.Label<br><br>    Set m\_frmParent = Parent<br><br>    Set m\_objParent = Parent<br><br>    Set m\_objResizer = m\_objParent.Controls.Add("Forms.Frame.1", MFrameResizer, True)<br><br>    Set labTemp = m\_objResizer.Add("Forms.label.1", MResizer, True)<br><br>    With labTemp<br><br>        With .Font<br><br>            .Name = "Marlett"<br><br>            .Charset = 2<br><br>            .Size = 14<br><br>            .Bold = True<br><br>        End With<br><br>        .BackStyle = fmBackStyleTransparent<br><br>        .AutoSize = True<br><br>        .BorderStyle = fmBorderStyleNone<br><br>        .Caption = "o"<br><br>        .MousePointer = fmMousePointerSizeNWSE<br><br>        .ForeColor = RGB(100, 100, 100)<br><br>        .ZOrder<br><br>        .Top = 1<br><br>        .Left = 1<br><br>        .Enabled = False<br><br>    End With<br><br>    With m\_objResizer<br><br>        .MousePointer = fmMousePointerSizeNWSE<br><br>        .BorderStyle = fmBorderStyleNone<br><br>        .SpecialEffect = fmSpecialEffectFlat<br><br>        .ZOrder<br><br>        .Caption = ""<br><br>        .Width = labTemp.Width + 1<br><br>        .Height = labTemp.Height + 1<br><br>        .Top = m\_objParent.InsideHeight - .Height<br><br>        .Left = m\_objParent.InsideWidth - .Width<br><br>    End With<br><br>End Function |
|     |     |
|     |
| ##### Thanks to László Balogh for pointing out the floating sizing handle bug.   <br>Also thanks to Gary Winey for suggesting the Layout event for altering the position of the resizer control when userform size is alter by other code.<br><br>##### The latest code also uses a frame to hold the label which allows the resizer to appear above controls that a label on its own would not be able to. |
| ##### ![](https://www.andypope.info/images/xl2000.gif) [Example](https://www.andypope.info/vba/FormResizer.zip)<br> workbook |
|     |

  [![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/FormResizer.zip)

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/resizeform.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope