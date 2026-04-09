# Event handler

**Source:** https://www.andypope.info/vba/ufevents.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

Control array event handler
---------------------------

![](https://www.andypope.info/vba/ufevents_3.png)

The guys at [Webucator training services](https://www.webucator.com/microsoft-training/vba.cfm)
 but together a [video](https://youtu.be/5iVDy23srtA)
 based on this approach.  
  
  
Within VBA it is not possible to have an array of controls. Each control must have a unique name and it's own set of events. If you want to handle an event, such as Click, for multiple controls with similar code you have two approaches available. The first is to add code to the event of each control. The other is to use a class taking advantage of the WithEvents and create objects based on the class.  
  
The first approach means that lots of code, often repetitive in nature, is required. Also the controls must be present at design time in order to add the code to the controls event.  
  
The second approach reduces the repetitive code and can be applied to controls created at run time.  
  
In this article I want to address the issue of loose and tight coupling within the class approach. Most explanations of the technique use a tightly coupled approach. This is were the class includes an explicit reference(s) to the userform containing the control. This means the class can not easily be reused in other projects without altering code in either the class or userform or both.  
  
As an example I will create a colour picker userform using each approach. Each user form will appear the same and have the same functionailty, which is to allow the user to select a colour by clicking from a swatch of colours. When a colour is clicked the larger colour tile is updated to reflect the selected colour.  
  
All examples have a routine, m\_CreatePalette, to layout the labels used for the colours.  
_If the AddControls argument is TRUE then the controls will also be added to the userform at run time._  

Private Const mCOLORPOT\_PREFIX = "ColorPot\_"
Private Sub m\_CreatePalette(AddControls As Boolean)

    Dim RowIndex As Long
    Dim ColIndex As Long
    Dim TempCtl As MSForms.Label
    Dim Left As Single
    Dim Top As Single
    Dim Name As String
    Dim Palette As Range
    Const COLORPOT\_GAP = 2
    Const COLORPOT\_SIZE = 24
    
    Set Palette = ThisWorkbook.Names("COLOR\_PALETTE").RefersToRange
    
    Top = COLORPOT\_GAP
    For RowIndex = 1 To Palette.Rows.Count
        Left = COLORPOT\_GAP
        For ColIndex = 1 To Palette.Columns.Count
            Name = mCOLORPOT\_PREFIX & Format(RowIndex, "00") & "\_" & Format(ColIndex, "00")
            If AddControls Then
                Set TempCtl = Me.Controls.Add("Forms.Label.1", Name, True)
            Else
                Set TempCtl = Me.Controls(Name)
            End If
            With TempCtl
                .Left = Left
                .Top = Top
                .Width = COLORPOT\_SIZE
                .Height = COLORPOT\_SIZE
                .Caption = ""
                .SpecialEffect = fmSpecialEffectSunken
                .BackColor = Palette.Cells(RowIndex, ColIndex).Interior.Color
            End With
            Left = Left + COLORPOT\_SIZE + COLORPOT\_GAP
        Next
        Top = Top + COLORPOT\_GAP + COLORPOT\_SIZE
    Next
            
End Sub			

  

### Non class events

![](https://www.andypope.info/vba/ufevents_1.png)  

Each control was created at design time and has code for the Click event. Below is only the code for 7 of the controls but hopefully you get the idea of how much reptetive code is required.

Private Sub ColorPot\_01\_01\_Click()
    CurrentColor.BackColor = ColorPot\_01\_01.BackColor
End Sub
Private Sub ColorPot\_01\_02\_Click()
    CurrentColor.BackColor = ColorPot\_01\_02.BackColor
End Sub
Private Sub ColorPot\_01\_03\_Click()
    CurrentColor.BackColor = ColorPot\_01\_03.BackColor
End Sub
Private Sub ColorPot\_01\_04\_Click()
    CurrentColor.BackColor = ColorPot\_01\_04.BackColor
End Sub
Private Sub ColorPot\_01\_05\_Click()
    CurrentColor.BackColor = ColorPot\_01\_05.BackColor
End Sub
Private Sub ColorPot\_01\_06\_Click()
    CurrentColor.BackColor = ColorPot\_01\_06.BackColor
End Sub
Private Sub ColorPot\_01\_07\_Click()
    CurrentColor.BackColor = ColorPot\_01\_07.BackColor
End Sub
'
' ... more Click event code for remaining 53 labels removed for brevity
'			

### Class events

![](https://www.andypope.info/vba/ufevents_2.png)

The class event approach requires code in the userform to store the objects and link them to the controls.

Private m\_Pots As Collection
Private Sub m\_AssignEvents()

    Dim Palette As Range
    Dim RowIndex As Long
    Dim ColIndex As Long
    Dim Name As String
    Dim ColorPot As CEventTight
    
    Set Palette = ThisWorkbook.Names("COLOR\_PALETTE").RefersToRange
    For RowIndex = 1 To Palette.Rows.Count
        For ColIndex = 1 To Palette.Columns.Count
            Name = mCOLORPOT\_PREFIX & Format(RowIndex, "00") & "\_" & Format(ColIndex, "00")
            Set ColorPot = New CEventTight
            Set ColorPot.Pot = Me.Controls(Name)
            m\_Pots.Add ColorPot, CStr(m\_Pots.Count + 1)
        Next
    Next

End Sub			

The class is named CEventTight

Public WithEvents Pot As MSForms.Label

Private Sub Pot\_Click()

    Pot.Parent.CurrentColor.BackColor = Pot.BackColor
    
End Sub			

Whilst the quantity of code in the class is small it is tightly coupled as it references the CurrentColor control in the user form. This means that to reuse the class the form must have a control named CurrentColor.

### Class event handler

![](https://www.andypope.info/vba/ufevents_3.png)

There are actually 2 classes required. One acts as storage of references to indiviual objects. It also raises the event which can be exposed in the userform.  
  
CEventHandler  

Public Event Click(Index As Long)
Private m\_Pots As Collection
Public Function Add(Ctl As MSForms.Label) As CEventLoose

    Dim TempCtl As CEventLoose
    
    Set TempCtl = New CEventLoose
    TempCtl.Index = m\_Pots.Count + 1
    Set TempCtl.Parent = Me
    Set TempCtl.Pot = Ctl
    m\_Pots.Add TempCtl, Ctl.Name
    
    Set Add = TempCtl
    
End Function
Public Property Get Count() As Long
    Count = m\_Pots.Count
End Property
Public Function Item(Index As Variant) As CEventLoose
    On Error Resume Next
    Set Item = m\_Pots(Index)
    Exit Function
End Function
Public Function Items() As Collection
    Set Items = m\_Pots
End Function
Public Sub Remove(Index As Variant)
    On Error Resume Next
    m\_Pots.Remove Index
    Exit Sub
End Sub
Private Sub Class\_Initialize()

    Set m\_Pots = New Collection
    
End Sub
Private Sub Class\_Terminate()

    Do While m\_Pots.Count > 0
        m\_Pots.Remove m\_Pots.Count
    Loop
    Set m\_Pots = Nothing
    
End Sub
Public Sub EventClick(Index As Long)
    RaiseEvent Click(Index)
End Sub		

CEventLoose  

Public WithEvents Pot As MSForms.Label
Public Parent As CEventHandler
Public Index As Long
Private Sub Pot\_Click()
    Me.Parent.EventClick Index
End Sub			

Userform code to declare and consume the event handler  

Private WithEvents m\_Pots As CEventHandler
Private Sub m\_Pots\_Click(Index As Long)

    CurrentColor.BackColor = m\_Pots.Item(Index).Pot.BackColor
    
End Sub
Private Sub m\_AssignEventHandler()

    Dim Palette As Range
    Dim RowIndex As Long
    Dim ColIndex As Long
    Dim Name As String
    Dim ColorPot As MSForms.Label
    
    Set Palette = ThisWorkbook.Names("COLOR\_PALETTE").RefersToRange
    For RowIndex = 1 To Palette.Rows.Count
        For ColIndex = 1 To Palette.Columns.Count
            Name = mCOLORPOT\_PREFIX & Format(RowIndex, "00") & "\_" & Format(ColIndex, "00")
            Set ColorPot = Me.Controls(Name)
            m\_Pots.Add ColorPot
        Next
    Next

End Sub

The CEventLoose class captures the click event in the same way as the CEventTight does. But rather than changing the property of a control directly it calls a routine in the CEventHandler class, passing information about which object it is, allowing the handler to raise an event. This event is exposed by the object when declared WithEvents in the userform. When the event fires code within the userform can process any actions required. This means the 2 classes can be used in any project without the need for code changes. All project specific code is done within the userform.  
  
In the example I have only used the Click event but the principle can be extended to all events that are exposed when using WithEvents. Unfortunately this is not the complete complement of events as a few, such as Enter and Exit, are only exposed when used in a suitable  container object.  
  
The download file also includes another example file where events are reported to a listbox. Along with event code to provide special textboxes for upper case, lower case and numeric entry only.  
  
[![](https://www.andypope.info/site_images/nav_download.png)](https://www.andypope.info/vba/ufevents.zip)
 

Created 6th September 2014

Last updated 6th September 2014 

  
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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/vba/ufevents.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope