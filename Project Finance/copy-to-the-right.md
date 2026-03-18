# Copy to the Right (SHIFT,CNTL,R)

**Source:** https://edbodmer.com/copy-to-the-right

---

It is amazing that excel does not have a way to automatically copy a formula to the right. I have written some code in generic macros that allows you to efficiently copy to the right (SHIFT, CNTL, R). I have tried to make the copy to the right macro flexible meaning that you can define parameters differntly. So, if you have the generic macro sheet open, and if you have a row of numbers somewhere, you can press SHIFT, CNTL, R and the numbers will copy to the right for as long as your row of numbers.  Some people have asked me if there is a way to put the Shift, CNTL, R code into your file so that generic macros does not have to be open.  The file below has that allows you to do this.  All you have to do is to copy the code from the macro to your macro and include the “on key” code. The file is attached to the button below.  The full code is listed at the bottom of this page.

**[File with Code that Allows you to Copy the SHIFT, CNTL, R macro into one of your files (So you don't have to open Generic Macros)](https://edbodmer.com/wp-content/uploads/2019/12/Shift-CNTL-R-Macro.xlsm)
**

How to Use Generic Macros to Copy to the Right
----------------------------------------------

To see this, go to a blank sheet and press the number one somewhere near the top (for example in cell D4.  Then press either ALT, E, I, S or ALT, or ALT, H, FI, S. (In French it is a bit more complicated). You will get a little menu like the following:

![](https://edbodmer.com/wp-content/uploads/2018/08/EIS.jpg)

Then press the number 9 as the stop value and you will have a row of numbers.  Just below the row of numbers (i.e. below the number 1), enter a few more numbers.  I put in 100, 200 and then used the ALT, = short cut to add the numbers together as shown on the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/08/Shift-Cntl-R-1.jpg)

Next, select the three numbers (the 100, 200 and 300) and press SHIFT, CNTL, R.  The numbers should copy to the right as shown in the screenshot below.  If this is not working, then you probably either do not have generic macros.xls open or the file is not enabled.

![](https://edbodmer.com/wp-content/uploads/2018/08/Shift-Cntl-R-2.jpg)

Undo Option with Copying to the Right (SHIFT, CNTL, S)
------------------------------------------------------

I have also tried to add an undo option to the Shift, CNLT, R macro which you can access with SHIFT, CNLT, S. Test the SHIFT,CNTL,S you can enter some other formula in the third row that currently contains 300.  Then press SHIFT,CNTL,S.  You should get the original number back.

You can also adjust the SHIFT, CNTL, R to look up to different rows and test other things. To adjust the generic macro file, you go to the first sheet of the file and change the parameters. After you change the parameters however you must run the implement macros macro.

If you want to put the SHIFT,CNTL, R macro in your workbook or in your personal workbook, I suggest copying the entire module where the macro is located in the generic macros.

Videos that Illustrate use of Generic Macros File
-------------------------------------------------

The first video below demonstrates how to use the Generic Macros file that you must download to colour your sheet efficiently.

Code for Copying the SHIFT, CNTL, R macro into your file
--------------------------------------------------------

Note that when you are copying this code that you may not want to use the auto\_open if there are some kind of restrictions on its use.  You can then just re-name the auto open function.

Option Base 1
Public calculation\_state As Single

Public max\_row As Single ' for finding number of rows in sheet
Public max\_col As Single ' for finding number of cols in sheet

Public end\_row As Single ' end row in shift cntl R
Public end\_row\_scan As Single ' maximum number of rows to scan

Public scan\_cols As Single ' number of colums to scan in finding rows
Public end\_col As Single ' end col in shift cntl R
Public end\_col\_scan As Single ' number of columns to scan
Public scan\_rows As Single ' number of rows to scan in finding columns

Public max\_test\_row As Single
Public shortest\_col\_for\_test As Single
Public look\_in\_up\_rows As Boolean

Public data\_to\_save(10000) As Variant ' for undoing the shift CNTL R
Public end\_col\_range As Single
Public row\_to\_save As Single
Public col\_to\_save As Single

Public col\_start As Single
Public col\_end As Single
Public row\_selected As Single

Public initial\_end\_row\_scan As Single

'
' Copy the public variables above
'


Public Sub Auto\_Open()
'
'
' When set to mannual will not recalculate on save
'
Application.CalculateBeforeSave = False
Application.ScreenUpdating = False
Sheets(1).Select
calculation\_state = Application.Calculation
Application.Calculation = xlCalculationManual

generic\_macro\_file = ActiveWorkbook.Name

'
'---------------------------------------------------------------------------------------------------------------------------------
'
' Assign Short-cut keys ^ is CNTL, % is ALT, + is Shift
' Shift is very dangerous because you may change the keyboard
' Alt does not work with things like Alt D and Alt E because these are reserved
'

Application.OnKey "^R", "x\_fill\_right"
Application.OnKey "^S", "x\_undo\_fill\_right"

' These are defaults from range names in the first sheet of generic macros
' parameters for shift cntl R
'
max\_test\_row = 20
shortest\_col\_for\_test = 5
look\_in\_up\_rows = False


End Sub


' This is a key program that defines max\_row that is used in many other programs with a public variable

Sub x\_find\_rows() ' The find rows is used in the colour macro a lot and in other macros that go around rows
' defines the max\_row with is a public variable
start\_row = 1
start\_col = 1
max\_row = 0 ' max row is a public variable that used elsewhere
same\_row = 0
Start = 1

If end\_row\_scan = 0 Then
end\_row\_scan = 450

MsgBox " Must Initialise Generic Macros for Row and Column Definition "

end\_row\_scan = initial\_end\_row\_scan

' End ' Unless end the system crashes
End If

For row = Start To end\_row\_scan ' the end row is a maximum row defined to make the process not to slow
' end row is a public variable
For col = start\_col To scan\_cols ' colums to test whether there is anything in row; allowance for blank columns on left

last\_max = max\_row

' If row Mod 10 = 0 Then ' only display every 10 rows - not used in program
' MsgBox " col " & col & " row " & row & " max\_row " & max\_row & " start row " & start\_row
' End If

' this is the major test -- look for text or numbers

On Error Resume Next
If WorksheetFunction.IsText(Cells(row, col)) = True Or WorksheetFunction.IsNumber(Cells(row, col)) = True Then
If row > max\_row Then max\_row = row ' see if row of text > earlier max
End If

Next col ' end of scan around cols

Next row

Start = max\_row ' use max row from test

' If max\_row > 0 Then max\_row = max\_row + 15 ' add some rows

If max\_row = last\_max Then same\_row = same\_row + 1
If same\_row > 10 Then

Exit Sub
End If

End Sub

' This is similar to the find rows routine -- it makes the programs work much faster and finds the columns used in a sheet

Sub x\_find\_cols()

start\_row = 1
start\_col = 1
max\_col = 0
same\_col = 0

If end\_col\_scan = 0 Then
end\_col\_scan = 450
MsgBox " Must Initialise Generic Macros to find Column Dimension "
' End
End If

For col = start\_col To end\_col\_scan

For row = start\_row To scan\_rows ' scan rows is public variable

last\_col = max\_col

' If col Mod 10 = 0 Then
' MsgBox " col " & col & " row " & row & " max\_row " & max\_col & " start col " & start\_col
' End If

On Error Resume Next ' find and re-set the maximum column
If WorksheetFunction.IsText(Cells(row, col)) = True Or WorksheetFunction.IsNumber(Cells(row, col)) = True Then
If col > max\_col Then max\_col = col
End If
Next row
Next col

start\_col = max\_col

End Sub
'||||||||||||||||||||||| These are macros for the colouring sheet |||||||||||||||||||||||||

Sub x\_select\_area() ' Finding the number of rows and or columsn is key for a lot of other macros

' This runs both rows and columns to test what is going on; it is not used


x\_find\_rows
x\_find\_cols

Range(Cells(1, 1), Cells(max\_row, max\_col)).Select


End Sub


'
' This is the SHIFT, CNTL, R function
'
' You could copy this into your personal workbook if you want and use the application.onkey
'

Sub x\_fill\_right()

calculation\_state = Application.Calculation
Application.Calculation = xlCalculationManual

Application.ScreenUpdating = False

If show\_status\_bar Then \_
Application.StatusBar = "SHIFT,CNTL,M to Clear Status Bar; SHIFT,CNTL Z --> First Sheet; SHIFT,CNTL,R --> Copy to Right; SHIFT,CNTL,S --> Undo Copy to Right; SHIFT,CNTL,C --> Colour Sheets "

' first section: define basic parameters

last\_col = 16000 ' Last column definded from empty row. works with 2007 and later. Should adjust for verion

If shortest\_col\_for\_test = 0 Then ' Test the data in public variables
shortest\_col\_for\_test = 5 ' MsgBox " Shortest Column is Zero, Please press the implement button in generic macros "
End If

If max\_test\_row = 0 Then
max\_test\_row = 10 ' MsgBox " Max test to look up or down is zero, Please press the implement button in generic macros "
End If

row\_num = Selection.Rows.Count ' the selection is the area that is hilighted. find how many rows hilighted
col = Selection.Columns.Count ' this is the same for the number of cols hilighted (not used)

cell\_start = Selection.Cells(1, 1) ' this is the starting cell that will be copied

org\_col = Selection.Cells(1, 1).Column ' get the column of the starting point
org\_row = Selection.Cells(1, 1).row ' get the row of the starting point

up\_move = 1 ' how many rows to move up... this will change if there are blank rows
max\_col = 0
counter = 0

col\_to\_use\_up = 1
end\_col\_down = 1

'-----------------------------------------------------------------------------------------------------------------------------
' SECTION 2: analysis for looking up to find longest col
'-----------------------------------------------------------------------------------------------------------------------------

copy\_process: ' this is for checking rows below

' find the base number of columns for copying -- could be below or above

counter = counter + 1 ' count how many times looked in up col

If org\_row = 1 Then ' skip the looking up if the first row
col\_to\_use\_up = 0
GoTo move\_down
End If

On Error GoTo exit1 ' doesnt work on first row

Cells(org\_row, org\_col).Select ' Go to the base for copying -- start with original row and go up go up by the up\_move... first is 1
Selection.End(xlToRight).Select ' go to the end of the upwards row
end\_col\_range = ActiveCell.Column - 1 ' find the end col for the entire base row selected

test\_cell = Cells(org\_row, end\_col\_range) ' test cell is the end of the column

test\_cell = WorksheetFunction.IfError(test\_cell, " ")

' Go back and get the data to copy from the starting column

If end\_col\_range < last\_col Then ' If end\_col is less than last\_col then there is stuff at the end

For k = 1 To end\_col\_range + 1 ' MsgBox " cells org\_row k " & Cells(org\_row, k).Formula & " k " & k & " org\_row " & org\_row

data\_to\_save(k) = Cells(org\_row, k + org\_col).Formula ' This is for the undo; do this before copying
row\_to\_save = org\_row
col\_to\_save = org\_col
Next k
End If

If end\_col\_range < last\_col And test\_cell = "" Then ' If end\_col is less than last\_col then there is stuff at the end
col\_to\_use\_up = end\_col\_range
GoTo final\_col
End If

Cells(org\_row - up\_move, org\_col + 1).Select ' start with original row and go up go up by the up\_move... first is 1
Selection.End(xlToRight).Select ' go to the end of the upwards row

end\_col = ActiveCell.Column ' find the end col for the entire row selected
end\_row = ActiveCell.row ' dont really need this

' check if have to go up further
' last col is the end of the sheet; does not work with excel 2003 with fewer cols

While org\_row - up\_move > 0 ' go around until get to top row ' MsgBox " in while - move up " & up\_move
up\_move = up\_move + 1 ' keep going up
'
' Try to find the number of columns to copy to the right - before was simply the longest column
'
If end\_col < last\_col And end\_col > max\_col Then
max\_col = end\_col ' find max column
col\_to\_use\_up = max\_col

If end\_row = 1 Then GoTo move\_down: ' MsgBox " max col adjusted - max col " & max\_col

End If

If end\_col < last\_col And end\_col > shortest\_col\_for\_test Then

col\_to\_use\_up = end\_col ' find max column ' MsgBox " test 1 going to final end col " & end\_col
GoTo final\_col
End If

'
' Limit the number of rows to look for
'
If counter > max\_test\_row Then
col\_to\_use\_up = max\_col ' find max column ' MsgBox " test 2 going to move down end col " & end\_col & " Max test row " & max\_text\_row & " max col " & max\_col

GoTo move\_down: ' limit the rows to look up
End If

If col\_to\_use\_up >= shortest\_col\_for\_test Then
col\_to\_use\_up = end\_col ' find max column ' MsgBox " test 3 going to move down - end col " & end\_col

' GoTo move\_down: ' limit the rows to look up
End If

' MsgBox " end of copy process Max col " & max\_col & " end col " & end\_col & " counter " & counter

If end\_row = 1 Then GoTo move\_down:

GoTo copy\_process ' go back, repeat the look down and find end col

Wend

' If look\_in\_up\_rows = False Then GoTo final\_col

move\_down:

end\_col = max\_col
If end\_col > last\_col Then end\_col = 1 ' this happens when go through loop and still have the entire sheet

down\_move = 1

copy\_process\_down:

On Error GoTo exit1 ' doesnt work on first row
Cells(org\_row + down\_move, org\_col).Select ' go up by the up\_move

Selection.End(xlToRight).Select ' select the row

end\_col\_down = ActiveCell.Column ' find the end col
end\_row\_down = ActiveCell.row

' check if have to go down further
' last col is dend of sheet

If end\_col\_down > last\_col Then ' if a blank row then go up and try again
down\_move = down\_move + 1
If down\_move < max\_test\_row Then GoTo copy\_process\_down ' cannot work when get to the top
End If

If end\_col < last\_col And end\_col < shortest\_col\_for\_test Then
col\_to\_use\_down = end\_col ' find max column
GoTo final\_col
End If


final\_col:

If end\_col\_down > last\_col Then end\_col\_down = 0 ' reset end col if not founc

end\_col = WorksheetFunction.Max(col\_to\_use\_up, end\_col\_down) ' the final end col to use

For row = org\_row To org\_row + row\_num - 1 ' this is like CNTL R

If end\_col > 14000 Then
MsgBox " Attmpting to copy MORE THAN 14,000 COLUMNS " & Chr(13) & " Run Implement Macros " & Chr(13) & "Technical data - col to use up " & col\_to\_use\_up & " End col down " & end\_col\_down
Exit Sub
End If

Range(Cells(row, org\_col), Cells(row, end\_col)).Select ' select the appropriate area
Selection.FillRight ' Finally do the copy CNTL R

'
' This is for the undo stuff
'
Next row

col\_start = org\_col
col\_end = end\_col
row\_selected = row

Cells(org\_row, org\_col).Activate ' go back to original cell

exit1:

Application.Calculation = calculation\_state


End Sub


Sub x\_undo\_test()

test = Selection.Formula

' MsgBox test

test1 = Selection.Cells(1, 1).Formula

Selection.Clear

Selection.Cells(1, 1) = test1

End Sub
Sub x\_undo\_fill\_right()

calculation\_state = Application.Calculation
current\_status = Application.Calculation
Application.Calculation = xlCalculationManual

Application.ScreenUpdating = False

On Error Resume Next

current\_row = Selection.row

If current\_row <> row\_to\_save Then
MsgBox " Undo only works after you have used Shift, CNTL, R TWO TIMES (There is no Data after the first time)"
Exit Sub
End If

' MsgBox " Current Row " & current\_row & " Row to save " & row\_to\_save & " Col to Save " & col\_to\_save

For k = 1 To end\_col\_range + 1
Cells(row\_to\_save, col\_to\_save + k) = data\_to\_save(k)
Next k

Cells(row\_to\_save, col\_to\_save + 1).Select
Selection.Copy
Cells(row\_to\_save, col\_to\_save).Select
ActiveSheet.Paste

Application.CutCopyMode = False

Application.Calculation = calculation\_state

End Sub


' The programs need to know how many rows and columns are in the sheet

'------------------------------------------------------------------------------------------------------------
' You need this for other macros
'------------------------------------------------------------------------------------------------------------

Sub x\_find\_rows\_and\_cols() ' Finding the number of rows and or columsn is key for a lot of other macros

' This runs both rows and columns to test what is going on; it is not used

x\_find\_rows
x\_find\_cols

' This shows the result -- this subroutine is not directly used

MsgBox " Rows in Sheet " & max\_row & " Colums Scanned to Find Max Row " & scan\_cols & " End Row for Scan " & end\_row\_scan
MsgBox " Cols in Sheet " & max\_col & " Rows Scanned to Find Max Column " & scan\_rows & " End Column for Scan " & end\_col\_scan

' current\_file = ActiveWorkbook.Name

' MsgBox " Active Book " & current\_file

' Workbooks(generic\_file).Activate

' Range("max\_row") = max\_row

' Workbooks(current\_file).Activate


' Workbooks(generic\_book).Range("max\_row") = max\_row
' Workbooks(generic\_book).Range("max\_col") = max\_col

' Workbooks(generic\_book).Range("current\_file") = current\_file


End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8851&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11348&rand=0.24218199349717995)