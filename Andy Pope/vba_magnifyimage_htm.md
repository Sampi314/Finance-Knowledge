# Magnify Image

**Source:** https://www.andypope.info/vba/magnifyimage.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

Rollover image magnifier
------------------------

![](https://www.andypope.info/vba/magnify_2.png)

  
The rollover image magnification effect is created by moving a frame, containing an image control, over the source image. By setting the image contained within the frame to a size factor of the compressed image it gives the illusion of magnifying the image under the frame.

Option Explicit

Private m\_ZoomFactor As Double
Private Sub CheckBox1\_Click()

    If CheckBox1.Value Then
        Image2.AutoSize = False
        Image2.PictureSizeMode = fmPictureSizeModeStretch
        Image2.Width = Image2.Width \* 2
        Image2.Height = Image2.Height
    Else
        Image2.PictureSizeMode = fmPictureSizeModeClip
        Image2.AutoSize = True
    End If
    
End Sub

Private Sub CommandButton1\_Click()
    Unload Me
End Sub

Private Sub Image1\_MouseDown(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)

    If Button = 1 Then
        With Frame1
            .Left = X
            .Top = Y
            .Visible = True
        End With
    End If
    
End Sub

Private Sub Image1\_MouseMove(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)

    Dim RatioX As Double
    Dim RatioY As Double
        
    If Button = 1 Then
        Frame1.Left = Image1.Left + X - (Frame1.Width / 2)
        Frame1.Top = Image1.Top + Y - (Frame1.Height / 2)
    
        RatioX = X / Image1.Width
        RatioY = Y / Image1.Height
        
        Image2.Left = -(Image2.Width \* RatioX) + (Frame1.Width / 2)
        Image2.Top = -(Image2.Height \* RatioY) + (Frame1.Height / 2)
        
    End If
End Sub

Private Sub Image1\_MouseUp(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)

    If Button = 1 Then
        Frame1.Left = Image1.Left + Image1.Width
        Frame1.Top = Image1.Top + Image1.Height
        Frame1.Visible = False
    End If
End Sub

Private Sub UserForm\_Initialize()

    Image2.Picture = Image1.Picture
    Image2.AutoSize = True
    Frame1.SpecialEffect = fmSpecialEffectRaised
    Frame1.Visible = False
    
    m\_ZoomFactor = 1
    ZoomFactor.List = Array("1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "5.0", "10.0")
    ZoomFactor.ListIndex = 0
    
End Sub

Private Sub ZoomFactor\_Change()

    m\_ZoomFactor = CDbl(ZoomFactor.Value)
    
    Image2.AutoSize = True
    If ZoomFactor.ListIndex > 0 Then
        Image2.AutoSize = False
        Image2.PictureSizeMode = fmPictureSizeModeStretch
        Image2.Width = Image2.Width \* m\_ZoomFactor
        Image2.Height = Image2.Height \* m\_ZoomFactor
    Else
        Image2.PictureSizeMode = fmPictureSizeModeClip
    End If
    
End Sub

For the best effect the large source image should be size such that it retains it's aspect ratio.  
  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/magnifyimage.xlsm)
 

Created 15th Novemebr 2014

Last updated 15th November 2014 

  
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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/magnifyimage.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope