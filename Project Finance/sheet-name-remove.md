# Sheet Name Remove

**Source:** https://edbodmer.com/sheet-name-remove

---

This page shows how to create a macro that automatically removes the sheet names of the current sheet in formulas of an excel spreadsheet. Through using a macro, you can take out the current sheet from all of the formulas in that use the current sheet name of your workbook. The method used is to get the sheet name with a function and then use the instring function to replace the sheet name with a function. The VBA code for running this program is shown in this page.

Mechanics of Running the Macro if you Don’t Care About the VBA
--------------------------------------------------------------

If you refer to another sheet when typing in a formula in an excel sheet, the current sheet name will appear in formula. The current sheet name is of course not necessary for making the formula work. Further, the current sheet name  can be irritating and make the formulas difficult to read and interpret.  An example of the problem is shown on the screenshot below.

To remove the sheet links you can use the Generic Macros excel file. One of the buttons on the form that appears after pressing CNTL, ALT, C will scan your sheet and remove the names. The purple button that allows you to do this is shown in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/05/generic-macros-1.jpg)

VBA Code for Removing Sheet Links
---------------------------------

You could  VBA code can be copied into your sheet or your personal workbook if you want to use it. If you try this be careful wth the functions that find rows and columns of the sheet.  Note that instead of using the find function with worksheetfunction, the INSTR VBA function is used.  This function is a lot more stable then using the find function when there is an error.  The macro shown below works through cells in a sheet and replaces the sheet name with a blank. It allows for five sheet names in the formula.

.

Sub x\_replace\_sheet\_name()

Dim sheet\_name\_lenght As Single

x\_find\_rows ' run programs to find the number of rows to reduce the time
x\_find\_cols

Application.StatusBar = " Searching to Replace in " & max\_row & " Rows and " & max\_col & " Columns "

calculation\_state = Application.Calculation
Application.Calculation = xlCalculationManual

sheet\_name\_active = ActiveSheet.Name ' get the current sheet name so you can look for this.

test\_start = Left(sheet\_name\_active, 1) ' test\_start is the leftmost character in the current sheet name

space\_test = False ' When there is a space in the sheet name, then ""
For i = 1 To Len(sheet\_name\_active)
sheet\_name\_char = Mid(sheet\_name\_active, i, 1)
If sheet\_name\_char = " " Then space\_test = True
Next i

If space\_test Then ' put quotes around the sheet name
sheet\_name\_test = "'" & sheet\_name\_active & "'!"
Else
sheet\_name\_test = sheet\_name\_active & "!"
End If

sheet\_name\_length = Len(sheet\_name\_test)

msgtest = MsgBox(" Looking for sheet name " & sheet\_name\_test & " Is this ok ", vbOKCancel, " Sheet Name Replace Program")

If msgtest = 2 Then Exit Sub

For row = 1 To max\_row
For col = 1 To max\_col

Cells(row, col).Select
cell\_string = Cells(row, col).Formula ' Only replace formulas
left\_character = Left(cell\_string, 1)
If left\_character <> "=" Then GoTo continue1:

If cell\_string = "" Then GoTo continue1: ' Skip over blanks

' Replace the cell string with blank

start\_mid = 1

For j = 1 To 5

If start\_mid = 0 Then GoTo continue2:

start\_mid = InStr(start\_mid, cell\_string, sheet\_name\_test) ' key item that replaces

If start\_mid = 0 Then GoTo continue2:

MsgBox " Trying to Replace " & cell\_string & " Starting in " & start\_mid & " Row " & row & " Column " & col

cell\_string = WorksheetFunction.Replace(cell\_string, start\_mid, sheet\_name\_length, "") ' key item that replaces

On Error Resume Next
Cells(row, col).Formula = cell\_string

continue2:
Next j
continue1:

Next col

Next row

Application.Calculation = calculation\_state
Application.StatusBar = False

Range("A1").Select
'
Application.Goto Range("A1")

End Sub

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3983&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=16784&rand=0.989898244445337)