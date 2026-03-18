# Additional Short-Cuts

**Source:** https://edbodmer.com/additional-short-cuts

---

The generic macros file has a few added short-cut keys that I use a lot including getting back the CNTL TAB and being able to cut and transpose cells.  In addition I have included some other hand-made short-cuts. Please do not go to the styles menu and think you are good. The generic macros file and a workbook named fm.xls includes a lot of different functions and macros. Some of the more important macros that create table of contents and remove the current sheet name from formulas and finds the links are shown below. As explained above, none of these macros have any irritating passwords and you can copy the macros into your files. The fm.xlsm file below has some of the older macros that I made a few years ago. The example calendar shows how you can create a macro that puts a password in a file and uses MATCH and INDEX over and over again with conditional formatting to make a calendar in excel (I doubt very much that you will use this).

Cutting and Pasting with Transpose
----------------------------------

Sometimes you need to transpose with the cut. The copy and paste special does not work. I have written a program to do this that you can copy below.

Sub Cut\_and\_Transpose()
'
`debug2 = False` 
`start_cell = InputBox(" Enter the Start Cell to Cut", , "A3") end_cell = InputBox(" Enter the End Cell to Cut", , "M15")`
`start_row = Range(start_cell).row` 

`start_col = Range(start_cell).Column end_row = Range(end_cell).row end_col = Range(end_cell).Column`

`Tot_Rows = end_row - start_row + 0` 
`Tot_cols = end_col - start_col + 0` 

`If debug2 Then MsgBox " Total Rows " & Tot_Rows` 

`Target_cell = InputBox(" Enter the Target Cell ", , "C24") target_row = Range(Target_cell).row` 
`Target_col = Range(Target_cell).Column` 

`If debug2 Then MsgBox " Target Col " & Target_col` 
`For row = start_row To Tot_Rows + start_row` 
    `to_col = row + col * 0 + Target_col - start_row` 
    `For col = start_col To Tot_cols + start_col` 
          `to_row = col + row * 0 + target_row - start_col` 
          `If debug2 = True Then MsgBox " Row From " & row & " Row To " & to_row & Chr(10) & " Col From " & col & " Col To " & to_col` 

`Cells(row, col).Select` 
`Selection.Copy Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False Selection.Cut` 
`Cells(to_row, to_col).Select` 

`value_in_cells = Selection.Value` 

`If IsEmpty(value_in_cells) Then` 
     `ActiveSheet.Paste` 
`Else MsgBox " Cell is not empty "` 
`End If` 
`Next col` 
`Next row`
End Sub

Miscellaneous Other Subroutines in Generic Macros
-------------------------------------------------

The generic macros file and a workbook named fm.xls includes a lot of different functions and macros. Some of the more important macros that create table of contents and remove the current sheet name from formulas and finds the links are shown below. As explained above, none of these macros have any irritating passwords and you can copy the macros into your files. The fm.xlsm file below has some of the older macros that I made a few years ago. The example calendar shows how you can create a macro that puts a password in a file and uses MATCH and INDEX over and over again with conditional formatting to make a calendar in excel (I doubt very much that you will use this).

Sub x\_replace\_sheet\_name() Takes away current name of sheet in formulas  
Sub x\_Delete\_cols() Deletes columns that are blank  
Sub x\_Delete\_rows() Deletes rows that are blank  
Sub x\_fix\_decimal() Fixes Problems with auto formatting  
Sub x\_find\_rows() Finds number of rows in sheet  
Sub x\_find\_cols() Finds number of cols in sheet  
Sub x\_colourTitles() Colours titles for the first column  
Sub x\_Create\_Table\_of\_Contents\_From\_Sheet\_Names() Creates Contents with links  
Sub x\_find\_externl\_links() Find External Links  
Sub x\_hide\_sheets\_after() Hide Sheets after Given Name

Functions in Generic Macros
---------------------------

In addition to macros, I put a bunch of user defined functions in the generic macros file. These macros do things like find the sheet name or the file name. They can also show who saved the file last and make a payback function. Unlinke the subroutine macros, you cannot just have the file open the functions. Instead, you must find the functions and then copy them into your file.

Function sheet\_name(cell)  
Function sum\_labels(series)  
Function File\_name() As Variant  
Function MyUDF(LastSaved1 As Boolean) As Double  
Function Last\_save\_by() As Variant  
Function LastSaved() As String  
Function lookup\_NA(lookup\_value, test\_array, result\_array)  
Function match\_adj(lookup\_value, lookup\_array)  
Function payback(series)  
Function dpayback(d\_rate, series)  
Function period\_of\_year(period, timing)  
Function show\_formula(cell)  
Function show\_formulaR(cell)  
Function show\_formulaL(cell)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8857&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.3684583700268469)