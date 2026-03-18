# Highlight Map in Excel based on Drop Down Selection in Excel

**Source:** https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection

---

[Skip to content](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#below-title)

Here is a neat trick for people who use maps in Excel. In this blog, I will explain how to highlight map in excel based on a drop down selection.

I have taken an editable map of the US. The idea is to highlight a state in the US when its name is selected from a drop down.

Something as shown in the pic below:

![Highlight Map in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201096%20584'%3E%3C/svg%3E)

Now before I show you the code, here are a few prerequisites for this trick.

1.  Get an editable map of the US in which you can select different shapes that you want to highlight
2.  Create a list of all the 50 states in one column, and on the column to its right I wrote State 1, State 2, and so on  
    ![Statelist](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20297%20319'%3E%3C/svg%3E)
3.  Name each shape on the map. For example, I have 50 shapes here for 50 states, and I have named each Shape as State 1, State 2, State 3, and so on..To do this, select any shape, and go to the Name Box, which is on the left of formula bar, and enter its name from the State Number column. For example, I selected Alabama and named it State 1.![Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%2098'%3E%3C/svg%3E)
4.  Create an [Excel drop down list](https://trumpexcel.com/excel-drop-down-list/)
     with the names of all the states ($B$2 in this case)![Map Highlight Dropdown List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20154'%3E%3C/svg%3E)
5.  Use the [Vlookup function](https://trumpexcel.com/excel-vlookup-function/)
     to extract the state number when a state is selected from the drop down. Here is the formula that I have used in cell $B$3  
    \=VLOOKUP(B2,’State List’!$B$3:$C$52,2,FALSE)

##### _**Code to Highlight Map in Excel**_ 

Private Sub Worksheet\_Change(ByVal Target As Range)
 Dim N As Integer
 Dim ShapeName As String
 N = ActiveSheet.Shapes.count
     If Target.Address = "$B$2" Then
     For i = 1 To N
         ShapeName = ActiveSheet.Shapes(i).Name
         If Left(ShapeName, 6) = "State " Then
                 ActiveSheet.Shapes(i).Select
                 With Selection.ShapeRange.Fill
                         .Visible = msoFalse
                         .Transparency = 1
                 End With
         End If
     Next i
     StateNumber = Range("$B$3").Value
         ActiveSheet.Shapes(StateNumber).Select
         With Selection.ShapeRange.Fill
                 .Visible = msoTrue
                 .Visible = msoTrue
                 .ForeColor.RGB = RGB(192, 0, 0)
                 .Transparency = 0
                 .Solid
         End With
 ActiveSheet.Range("$B$2").Select
 End If
 End Sub

_**Follow these simple steps while pasting this code**_

1.  First, right-click on the sheet tab that has the map and select “View Code”. This will open the VB editor.  
    ![View Code Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20156%20206'%3E%3C/svg%3E)
2.  Paste the code.

_**Download the file from here and follow along  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/prx1kef16gvo3y7/Map-Highlight.xlsm?dl=1)
**_

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Highlight Part of a Map based on Drop Down Selection”
--------------------------------------------------------------------

1.  Hi  
    In the code, Is there suppose to a space between “StateNumber” or…
    
    [Reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#comment-11706)
    
2.  Hi…this is cool…but once highlighted, is it possible to show some data point…also I was looking at a way to plot data points statewise on a map..pls guide
    
    [Reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#comment-3609)
    
3.  Hello sumit! Would you please tell something about Excel VBA? I mean what language VBA communicates in and how can one learn this language to mould the excel work according to one’s desires.
    
    [Reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#comment-1625)
    
4.  How would you go about modifying the code to allow multiple states to be selected and highlighted on the map? For example if cells B2, B3, and B4 allowed user input and had Alabama, Alaska, and Arkansas with shape lookups in cells C2, C3, and C4, respectively, how would the code be expanded to include multiple input cells and highlight the multiple corresponding shapes?
    
    [Reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#comment-1336)
    
    *   Hi  
        That’s the holy grail to me. Do you happen to know where I could find out how to do this?
        
        [Reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#comment-11707)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-part-of-a-map-based-on-drop-down-selection/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK