# Delete Blank Row

**Source:** https://edbodmer.com/delete-blank-row

---

This page demonstrates how you can use and create a macro that deletes blank rows in excel.  In working with this program, you need to define a column that is used to test for blanks.  A loop works through the rows for the selected column.  When a blank is found it is deleted.  You should work backwards from the bottom of the sheet.  A new sheet is make in case there is a problem with the macro.

Using the Delete Rows Macro in Generic Macros
---------------------------------------------

The sheet below demonstrates an example of a file that has some blanks.  If you want to delete the rows that are blank you can use the generic macro file.

![](https://edbodmer.com/wp-content/uploads/2018/07/Karnen-Raw-Data.jpg)

The generic macro file that has the delete blank row macro is available for downloading below.  If you have already downloaded the file you do not have to do it again.

**[Generic Macro File that Allows you to Copy to the Right (Shift, CNTL, R) and to Colour and Format Sheets (CNTL, ALT, C)](https://edbodmer.com/wp-content/uploads/2024/04/Generic-Macros.xlsm)
**

To remove blank rows, I created a macro in the generic macros file.  So, open the generic macro file.  Then press the CNTL, ALT, C sequence to get the colouring menu.  On this menu there is a option for deleting blank rows as shown in the screenshot below.  Sorry about the crude circle.

![](https://edbodmer.com/wp-content/uploads/2018/07/Karnen-Colour-Menu.jpg)

After you press the delete rows button, a input box message appears.  In this box, you enter the column number to test for deleting rows.  This means that if the column you selected has a blank, the row will be deleted.  The screenshot below demonstrates how you enter the column number (not the column letter).

![](https://edbodmer.com/wp-content/uploads/2018/07/Karnen-Delete-Blank-Rows.jpg)

After you enter the column number, the rows are deleted and the results are put in a new sheet (in case you do something wrong and to much is deleted).  The manner in which the blank rows are deleted is demonstrated in the screenshot below.  Notice that sheet1 — the place where the original rows were read in is now sheet1(5) — this is a new sheet with the deleted blank rows.  The original sheet is still there.

![](https://edbodmer.com/wp-content/uploads/2018/07/Karnen-Delete-Blank-Rows-Finished.jpg)

Technical Details for Writing Your Own Macro
--------------------------------------------

The VBA code below demonstrates how you can do this yourself.  You need to find the number of rows and work backward with a for loop.   A macro for deleting rows and deleting columns is presented.

.

Sub x\_Delete\_rows()

Dim col\_test As Single

x\_find\_rows
x\_find\_cols

On Error GoTo set\_zero:
col\_test = InputBox("Column Number as Basis to Test for Deletion (Blank or Zero tests that Entire Column is Blank)" \_
& Chr(13) & Chr(13) & " Enter a NUMBER not a letter")
GoTo skip:
set\_zero:
col\_test = 0
skip:

copy\_sheet

If col\_test = zero Then
start\_col = 1
end\_col = max\_col
Else
start\_col = col\_test
end\_col = col\_test
End If

' MsgBox " Maximum Rows " & max\_row & " Maximum Columns " & max\_col

For delete\_row = max\_row To 1 Step -1 ' work through rows from end
keep\_row = False ' keep rows set to false (meaning delete)
Cells(delete\_row, 1).Select

For col = start\_col To end\_col ' work around cols check if anything there

If WorksheetFunction.IsNumber(Cells(delete\_row, col)) = True \_
Or WorksheetFunction.IsText(Cells(delete\_row, col)) = True Then
keep\_row = True
End If
Next col

If keep\_row = False Then ' delete row if you havent found anything
Selection.EntireRow.Delete
End If

Next delete\_row

End Sub

Sub x\_Delete\_cols()
'
x\_find\_rows ' find rows and cols from this function
x\_find\_cols

' MsgBox " Maximum Rows " & max\_row & " Maximum Columns " & max\_col

For delete\_col = max\_col To 1 Step -1 ' key is to work backwards
keep\_col = False
Cells(1, delete\_col).Select
For row = 1 To max\_row
If WorksheetFunction.IsNumber(Cells(row, delete\_col)) = True \_
Or WorksheetFunction.IsText(Cells(row, delete\_col)) = True Then
keep\_col = True
End If
Next row

If keep\_col = False Then ' After finding blank colum, delete
Selection.EntireColumn.Delete
End If

Next delete\_col

End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=4923&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12268&rand=0.9083533983558495)