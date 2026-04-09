# VBA Explanations

**Source:** https://edbodmer.com/technical-details-of-vba-code-in-read-pdf-and-generic-macros

---

This page documents and explains some of the VBA code used in the generic macros file. I walk through the fundamental use of CELLS and FOR NEXT which is the foundation of many of the methods used in the file. My style in programming is very old fashioned and different from other techniques you will find on the internet. The methods for constructing macros that copy to the right and that create colours are explained along with some of the UDF’s in the generic macros file. You can find all of the VBA code in the generic macros file and in the read PDF file by just going to the macro list. I have tried to separate macros in the generic macro file into different modules so you can look at different code. The screenshot below illustrates how this works.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image.png)

.

The buttons below allow you to download the Generic Macro and Read PDF to Excel files.  After you open the files, press ALT, F8 and then you can look at the VBA code.

.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2019/01/VBA-Question.png)

Error Trapping with VBA
-----------------------

The file and the VBA code that you can download below illustrates the issue of error trapping.  It took me many years to figure out the problem of where you have an error trap in a loop.  Unless you get out of the entire loop you will have problems.

[Excel File that Finds Circular References Used to Illustrate VBA Techniques Including Cell, Sheet and Workbook Issues](https://edbodmer.com/wp-content/uploads/2019/01/Circular-Reference-Find.xlsm)

VBA Illustration Using Circular Reference Find
----------------------------------------------

In demonstrating VBA code, there are a bunch of examples where you find a cell and do something with that cell.  It could be finding a cell that has a precedent from another file and colouring that cell.  It could be finding a cell with the sheet name that you want to delete. It could be finding a cell so you can copy to the right. It could be finding numbers.

.

[Excel File with VBA Techniques including Error Trapping Using For Next Loop and Worksheetfunction Statement](javascript:void(0);)

.

I have made a video that walks through the VBA code and some VBA principles.  It is intended to be the second in a series of videos the describe VBA code.  The first video describes how to make a data table where the goal seek is operated for each sensitivity case. I use the code in the circular reference find macro to illustrate a few principles that include:

*   Use of msgbox
*   Use of inputbox
*   Finding circular references
*   Error Trapping in Loops
*   For/Next Loops
*   VBA philosophy of Workbooks, Sheets and Cells
*   Using Recorded Macros

The VBA Code finds, colours and lists circular references.  The file includes various different circular references as illustrated in the screenshot below.  The coloured cells contain circular references and the colouring is accomplished with the VBA code.  In addition, the VBA code includes the option to add comments to the circular references which are created by the code.  The process of adding comments and adding colours is part of the video description.

![](https://edbodmer.com/wp-content/uploads/2019/01/Circular-Reference-Input.png)

.

When operating the VBA code, a few message boxes and input boxes are used for options.  A message box is used for a YES/NO question involving whether to add comments.  Input boxes are used to select which sheets are used for adding colours and comments to the all of the circular references.  The screenshot below illustrates the idea:

.

![](https://edbodmer.com/wp-content/uploads/2019/01/Circular-VBA-Code.png)

The VBA code adds a sheet and lists the address and the formulas for the circular references. The VBA code uses the CELLS statement with a loop to do this.  Results of this process are illustrated in the screenshot below and discussed in detail in the video.

![](https://edbodmer.com/wp-content/uploads/2019/01/Circular-Reference-output.png)

The VBA code that is used to find the circular references is listed below.

. Sub Find\_circular() ‘ Before Loop Around Sheets MsgBox ” This progam finds circular references and lists them on a sheet” comment\_question = MsgBox(“Do you want to include Comments on the Circular References?”, vbYesNoCancel) ‘ 6 is yes and 7 is no ‘ ‘ Input box ‘ Dim start\_sheet, end\_sheet As Single start\_sheet = InputBox(“Number (not name) of Starting Sheet”) end\_sheet = InputBox(“Number (not name) of Final Sheet”) ‘ ‘ Cells, Sheets and Workbooks Add a sheet ‘ Application.DisplayAlerts = False ‘ You are going to delete a sheet and you don’t want the are you sure question On Error Resume Next ‘ Error trapping can be a real pain Sheets(“Circular References”).Delete ‘ May or may not exist Sheets.Add ActiveSheet.Name = “Circular References” ‘ Re-name the sheet and understand that you have workbooks, sheets, and cells Count\_of\_circular\_references = 4 ‘ Initialsise row number for output. I do not bother defining it ‘ ‘ Loop around all of the sheets ‘ Dim cell\_string1 As String For Sheet = start\_sheet To end\_sheet ‘ For loop and other kinds of loops are key in VBA Sheets(Sheet).Select ‘ Sheets() with name or number base\_sheet = ActiveSheet.Name Cells.Select ‘ Select all of the cells Selection.ClearFormats ‘ Clear all of the comments from the sheet ActiveSheet.Calculate For Row = 1 To 20 ‘ Get used to looping around rows and columns For col = 1 To 20 cell\_string = Cells(Row, col).Formula ‘ Can get formula and address from a cell cell\_address = Cells(Row, col).Address cell\_string1 = “‘” & cell\_string ‘ So you can print out a formula If Left(cell\_string, 1) = “=” Then On Error GoTo notcircular ‘ BIG point. When trap error, need to get out of the loop cell\_precedent = Cells(Row, col).Precedents.Address ‘ ‘ This is the big formula to find if there are circular references ‘ If cell intersects with precedents, cell has circular reference. ‘ result = Intersect(Range(cell\_address), ActiveSheet.Range(cell\_precedent)) Count\_of\_circular\_references = Count\_of\_circular\_references + 1 ‘ count circular references in sheet Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 3) = ” Circular Cell Address ” Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 4) = cell\_address Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 5) = ” Formula ” Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 6) = cell\_string1 Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 7) = ” Precedents in Formula ” Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 8) = cell\_precedent Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 1) = ” Sheet Name ” Sheets(“Circular References”).Cells(Count\_of\_circular\_references, 2) = base\_sheet Cells(Row, col).Select ‘ Select the cells for colouring With Selection.Interior .Pattern = xlSolid .PatternColorIndex = xlAutomatic .Color = 65535 End With If comment\_question = 6 Then Cells(Row, col).AddComment Selection.Comment.Visible = True Selection.Comment.Text Text:=”Circular Reference Formula:” & cell\_string & Chr(10) & “Address” & cell\_address & Chr(10) & \_ ” Precedents” & cell\_precedent End If End If Next col skipitem: Next Row Next Sheet Sheets(“Circular References”).Select Columns(“A:H”).Select Columns(“A:H”).EntireColumn.AutoFit Exit Sub notcircular: Resume skipitem: End Sub

.

Technical Discussion of Colouring Macros
----------------------------------------

A lot of the excel short-cuts are pretty useless and you can use the menu or the mouse just as fast. But there are a few short-cuts that can be helpful are the subject of this page.

When you press CNTL, ALT, C if the generic macros file is open somewhere

Macro to Remove Zeros from List
-------------------------------

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2873&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8600&rand=0.07935564865388145)