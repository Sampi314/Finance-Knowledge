# Finding No Dependent and Transfers

**Source:** https://edbodmer.com/finding-no-dependent-inputs

---

This page explains how to find a mark input cells that do not have dependents and how to mark and colour cells that go to another sheet.  I describe how to make a macro that works through rows and columns in an input sheet and find items that are not used by the model using the ShowDependent item in VBA. Finding cells with no dependents is a little tricky because when you try and use the .dependents statement in VBA, it only finds the dependents in one sheet.  I though this would be something that you should easily find on the internet, but I could not because of looking in different sheets. The method that I came up may be a bit crude.  It uses the “ShowDependents” statement in VBA.  When you create a blue arrow it is counted as a shape. If there is a blue arrow then there is a dependent. The problem is that as you work through cells, you need to re-set the number of shapes so you can design a test.

Finding Cells with No Dependents
--------------------------------

I have put code for finding input cells that do not have a dependent in the generic macros file and also in a separate file with a focused example.  The code that I use is shown below with various comments that hopefully illustrate the logic.  I have attached a file with the code for finding the dependent cells below.  The screenshot illustrates a simple example. I begin by counting the number of shapes so that you can later delete the shapes created by the ShowDependents. Some of the cells have dependents in the same page.  Other inputs have dependents in other cells.  The cells without dependents are coloured in yellow.  You can be safe in deleting these cells without causing any #REF problems. The screenshot below illustrates results of the transferred variables.  The variables in purple are cells that are cells that are stuck out there and have no uses anywhere in the workbook.  You can see how this works by pressing the button named “Find Cells with No Dependents.”  The video below the screenshot explains how the create the macro and the code at the bottom demonstrates the code itself.

**[Excel File with VBA Code and Macro for Determing Whether an Input Cell has a Depenednt and Marking It](https://edbodmer.com/wp-content/uploads/2020/05/IDC-and-Dependents.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2020/05/No-Dependents.png)

Finding Transferred Variables
-----------------------------

The screenshot below illustrates results of the transferred variables.  The variables in purple are cells that are transferred outside of the sheet to a different sheet.  You can see how this works by pressing the button named “File Transfers.”  The video below the screenshot explains how the create the macro and the code at the bottom demonstrates the code itself.

![](https://edbodmer.com/wp-content/uploads/2020/05/Transfer-Example.png)

Code for Finding Inputs with No Dependents
------------------------------------------

.

' ----------------------------------------------------------------------------------------------------------
' This finds the INPUT cells with NO DEPENDENTS
' You can find the number of dependents including dependents that go to another sheet
' This is done with the .showdependents extension
' To implement this you can first find the shapes that were in the sheet before you run the macro
' Then, you can find the added shapes from arrows associated with dependents
' If the total shapes is zero than colour the cell

' You can use RGB for the colours with range names
'
' Loop around rows and columns like other files
' ----------------------------------------------------------------------------------------------------------

Sub cells\_no\_dependents()

Dim shp As Shape, start\_row, start\_col, end\_row, end\_col As Single

' Clear Existing Cells

clear\_sheet ' Clear the formatting macro
ActiveSheet.ClearArrows

Application.ScreenUpdating = False

calculation\_status = Application.Calculation
Application.Calculation = xlCalculationManual


' Find the number of shapes that you do not want to delete (New shapes from dependent lines will be deleted)

shape\_number = 0

For Each shp In ActiveSheet.Shapes
shape\_number = shape\_number + 1
Next shp

Start\_Shape = shape\_number

' Loop around rows and columns like other files

For col = Range("col\_start") To Range("col\_end") ' First go around the columns

For Row = Range("row\_start") To Range("row\_end") ' Go around rows and columns

' Skip items that are not fixed numbers so the program works much faster

If WorksheetFunction.IsFormula(Cells(Row, col)) = True Then GoTo Finish\_Loop:
If WorksheetFunction.IsText(Cells(Row, col)) = True Then GoTo Finish\_Loop:
If WorksheetFunction.IsError(Cells(Row, col)) = True Then GoTo Finish\_Loop:
If WorksheetFunction.IsNumber(Cells(Row, col)) = False Then GoTo Finish\_Loop:

ActiveSheet.ClearArrows

' The show dependents for each cell; creates arrows that you can count

Cells(Row, col).ShowDependents ' This creates additional shapes; there is no error if no dependents

' The shape count has been reset; this counts the total amount of shapes including all of the lines from the show precedent

ShapeCount = ActiveSheet.Shapes.Count

If Range("slow") Then Application.Wait (Now + 0.000008) ' Wait to show the arrows

If Start\_Shape = ShapeCount Then GoTo no\_dependent: ' Skip over everything if no arrows and the number of shapes

' Delete the added sheets to re-start with the next cell

For Shape = ShapeCount To Start\_Shape + 1 Step -1 ' Delete additional shapes for next go around
On Error Resume Next
ActiveSheet.Shapes(Shape).Delete
Next Shape

On Error GoTo 0 ' Re-start the error checking

' Now compute the sheet dependents to find situations on other sheets

GoTo Finish\_Loop: ' Skip when found dependent

no\_dependent: ' Comes here when no arrows found

Cells(Row, col).Interior.Color = RGB(Range("Red"), Range("Green"), Range("Blue")) ' Colour the cell with no dependent
Cells(Row, col).Font.Color = RGB(0, 0, 0) ' colour font of cell with no dependent

' Cells(Row, col).Font.Bold = True

Finish\_Loop:

Next Row

Next col

End Sub

Code for Finding Equations and Inputs Transferred to Other Sheets
-----------------------------------------------------------------

' ----------------------------------------------------------------------------------------------------------
' This finds the transfers to other sheets
' You can find the number of dependents including dependents that go to another sheet
' You can also find the number of dependents that only go to the same sheet
' The difference between these two number is the number of dependents that go to another sheet
'
' You can find the total number of shapes with the .showdependents extension
' You can find the dependents in the current sheet with the .dependents extension
'
' Loop around rows and columns like other files
' ----------------------------------------------------------------------------------------------------------

Sub transfer\_colour()

Dim shp As Shape, start\_row, start\_col, end\_row, end\_col As Single

Application.ScreenUpdating = False

calculation\_status = Application.Calculation
Application.Calculation = xlCalculationManual

' Clear Existing Cells

clear\_sheet ' Another macro that re-sets the sheet
ActiveSheet.ClearArrows ' Clear all the blue arrows
current\_cell = ActiveCell.Address ' So you can go back to the current cell

' Find the number of shapes that you do not want to delete (New shapes from dependent lines will be deleted)

shape\_number = 0 ' This will count the number of shapes in the sheet

For Each shp In ActiveSheet.Shapes
shape\_number = shape\_number + 1
Next shp

Start\_Shape = shape\_number ' after counting the shapes find the initial shape number

' ----------------------------------------------------------------------------------------------------------
' Loop around rows and columns like other files
' In generic macros, you can
' ----------------------------------------------------------------------------------------------------------

For col = Range("col\_start") To Range("col\_end") ' First go around the columns

For Row = Range("row\_start") To Range("row\_end") ' Go around rows and columns

Range("C1") = col ' print the column number that will change as you go around
Range("C2") = Row ' print the row number that will change as you go around

' Skip items that are not fixed numbers

If WorksheetFunction.IsText(Cells(Row, col)) = True Then GoTo finish\_the\_calculations:
If WorksheetFunction.IsError(Cells(Row, col)) = True Then GoTo finish\_the\_calculations:
If WorksheetFunction.IsNumber(Cells(Row, col)) = False Then GoTo finish\_the\_calculations:

' ----------------------------------------------------------------------------------------------------------
' This is the first section that finds the number of arrows that go to all sheets
' You can count the number of arrows to find the number of dependents
' Then, you can finde the cells that have no dependents as the number of added shapes will be zero
' ----------------------------------------------------------------------------------------------------------

ActiveSheet.ClearArrows ' Start by clear the arrows from dependents

Cells(Row, col).ShowDependents ' This creates additional shapes; there is no error if no dependents

ShapeCount = ActiveSheet.Shapes.Count ' This is the total shapes including the arrows from the dependents

Dependents\_All\_Sheets = ShapeCount - Start\_Shape ' This includes all of the sheets

If Range("slow") Then Application.Wait (Now + 0.000006) ' This waits so that you can see the arrow

If Start\_Shape = ShapeCount Then GoTo finish\_the\_calculations: ' When no arrows, skip to no\_dependent section

For Shape = ShapeCount To Start\_Shape + 1 Step -1 ' Delete additional shapes for next go around
On Error Resume Next ' If there were no dependents, then this will produce an error
ActiveSheet.Shapes(Shape).Delete
Next Shape

On Error GoTo 0 ' Re-set the error

' ----------------------------------------------------------------------------------------------------------
' This is the second section that finds the number of dependents in the same sheet
' You count the number of dependents with the .dependents.count
' Then, you can finde the cells that have no dependents as the number of added shapes will be zero
' ----------------------------------------------------------------------------------------------------------

This\_Sheet\_Dependents = 0

On Error Resume Next

Cells(Row, col).DirectDependents.Select ' This creates additional shapes; there is no error if no dependents

This\_Sheet\_Dependents = Cells(Row, col).DirectDependents.Count ' This creates additional shapes; there is no error if no dependents

Other\_sheet\_dependents = Dependents\_All\_Sheets - This\_Sheet\_Dependents ' This is the first section for total less this sheet

If Other\_sheet\_dependents > 0 Then ' Only colour when there are some other sheet dependents

Cells(Row, col).Interior.Color = RGB(Range("Red"), Range("Green"), Range("Blue")) ' Colour the cell with no dependent
Cells(Row, col).Font.Color = RGB(0, 0, 0) ' colour font of cell with no dependent
' Cells(Row, col).Font.Bold = True

End If

GoTo finish\_the\_calculations:

no\_dependent\_at\_all:


finish\_the\_calculations:

Next Row

Next col


Range(current\_cell).Select

Application.Calculation = calculation\_status

End Sub

Sub clear\_sheet()

Cells.Select
With Selection.Interior
.Pattern = xlNone
.TintAndShade = 0
.PatternTintAndShade = 0
End With
With Selection.Font
.ColorIndex = xlAutomatic
.TintAndShade = 0
End With

Selection.Font.Bold = False


End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9789&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9424&rand=0.1514848937295331)