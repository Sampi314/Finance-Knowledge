# Table of Contents Marco and Hyper Link Macros

**Source:** https://edbodmer.com/table-of-contents-marco-with-hyper-links

---

This page of the website explains how to use and create a table of contents macro for an excel sheet and how to quickly create hyperlinks to different sheets.  The table of contents menu and process is from VBA code in the Generic Macros File.  I have revised the table of contents code and I have left the simpler code as well as the results at the bottom of the sheet.  In addition, a couple of functions that show who last saved the file and when the file was last saved are described below. The revised table of contents includes options for a colour code key as well as company logo etc.  It also includes sub headings to the table of contents that includes the title sections which are often included in column A of the spreadsheet. An example of the table of contents produced by the generic macros code is shown below.  The generic macro file that allows you to make the table of contents is attached to the button below the screenshot.

![](https://edbodmer.com/wp-content/uploads/2019/11/TOC-Complete.jpg)

Once you run the table of contents and create something like the contents above, there are links to the title rows.  I have tried to illustrate this in the screenshot below. When you click on column A in the screenshot, the hyperlink will take you back to the table of contents.  In addition, if there is text in the first row of the sheet, a hyper link can be inserted to easily take you back to the table of contents from the text (this is optional as shown below).

![](https://edbodmer.com/wp-content/uploads/2019/11/Sheets-with-Links.jpg)

When you run the ALT, CNTL, C function from the generic macros, an option to make a table of contents appears at the top left.  The Table of Contents menu from CNTL, ALT, C is shown in the first screenshot below.  I have tried to circle the button that takes you to the table of contents.  To make the table of contents menu, you should press this button.  Note that you should make sure the sheet is blank or it is an earlier table of contents menu.

![](https://edbodmer.com/wp-content/uploads/2019/11/Color-Menu.jpg)

Once you press the table of contents button, another screen appears that includes options for the table of contents options.  These options include whether you want to include colour codes, the last saved stuff and the logo.  The logo pictures are included in the generic macros file and you can include your own logo on the “colour codes” sheet of this page.  These options are shown on the left hand side of the screen menu.  The option to change the maximum number of rows allows you to create sub menus with more rows.

![](https://edbodmer.com/wp-content/uploads/2019/11/Contents-Menu.jpg)

Simpler Code for Creating Menus
-------------------------------

The VBA code for creating a table of contents is basic and all you really need to know is how to make a loop and use the CELLS function. You should first delete the exiting table of contents or sheets (you can press CNTL, A and then CNTL – ).  If you want the last saved function and the person who last saved, copy the functions below into your file.

.

Function File\_name() As Variant
Application.Volatile
File\_name = ActiveWorkbook.FullName
End Function

Function MyUDF(LastSaved1 As Boolean) As Double
 ' Good practice to call this on the first line.
 Application.Volatile (LastSaved1)
 MyUDF = Now
End Function

Function Last\_save\_by() As Variant
Application.Volatile
Last\_save\_by = ActiveWorkbook.BuiltinDocumentProperties(7)
End Function

Function LastSaved() As String
Application.Volatile (True)
LastSaved = ThisWorkbook.BuiltinDocumentProperties("Last Save Time")
Selection.NumberFormat = "dd-mmmm-yyyy hh:mm"
Selection.HorizontalAlignment = xlLeft
End Function


.

If you want to make your own macro, you can watch the video below.  This video demonstrates how the use a for loop along with the cells function.

Hyper Link Macros
-----------------

A very helpful short-cut key that is part of excel is CNTL K.  This short-cut allows you to make a hyper link pretty quickly.  I have also created a little macro that allows you to create a hyper link.  To do this yourself, you can follow the step by step process below.  This process will allow you to create a cell link from your own cell where you link to another sheet in your workbook.

*   You should first create a formula with the range name for the cell.  Sometimes you need to put in the ” ‘ ” sequence if the sheet name contains a blank or a number etc.
*   Then you name the cell which will be used in the macro below.
*   Then you copy the macro below and adjust the range names.
*   When you adjust this macro, make sure and name the range and you can put in a button as illustrate in the screenshot below.

After the hyperlink brings you to the source page and cell, you can press the F5 key to return to the where you were.  I use this to check databases when reading in a lot of data and putting the data in different sheets. You can also assign this to a drop-down box so that the hyperlink changes whenever you make a new selection as shown in the screenshot below.  The second screenshot illustrates use of CNTL, K and the code below the screenshots can be copied into your spreadsheet so you can create the hyper link from a flexible range name.

![](https://edbodmer.com/wp-content/uploads/2019/09/Create-Hyperlink.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/09/Hyperlink-with-CNTL-K.jpg)

Sub assign\_links2() ' This puts a hyper link for the current company
'

MsgBox " Assigning Hyperlink with Range Name Assign2 " & Range("assign2")

current\_calc = Application.Calculation

Application.Calculation = xlCalculationManual

range\_name = Range("assign2")
range\_text = Range("assign2")

' Put the range name here

Range("assign2").Select
Selection.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= \_
range\_name, TextToDisplay:=range\_text


Application.Calculation = current\_calc

End Sub

.

VBA Code for Creating Table of Contents
---------------------------------------

You can copy that code below to put a table of contents in your sheet.  It is long just because of formatting — the core is very simple and please do not be impressed.

Sheets(1).Select
For i = 1 To Sheets.Count

On Error Resume Next ' need this error check for the graph sheets

Sheets(i).Select

' Gets the name and puts in array sht\_name

sht\_name(i) = ActiveSheet.Name ' save the sheet name in an array for display

If (i < num) Then ActiveSheet.Next.Select
Next i

' Go back to contents sheet

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3569&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=14036&rand=0.6467119536197843)