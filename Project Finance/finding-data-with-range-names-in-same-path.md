# Finding Data with Range Names in Same Path

**Source:** https://edbodmer.com/finding-data-with-range-names-in-same-path

---

This page explains how you can look in a directory for data that has the same range names.  Say for example that you have a whole lot of models in a single directory and each file has the same range names. For example, each file may have a range name with min\_DSCR or equity\_IRR.  Alternatively, each file may have array range names with data for a bunch of years.  Let’s say that you want to collect data from each file and accumulate the data in a single file.  This page shows you a macro to accomplish this.  Unlike other situations where I download a single file, in this case you can download an entire zipped directory. When you download the zipped file attached to the button below, put the zipped file in a directory and unzip the file.  Then you open the file, Find Range Names2.xlsm.  This file contains the macros that accumulate the data.

**[Zipped File that Includes File that Finds Data with Range Names Either from Single Range Names or From Array Data](https://edbodmer.com/wp-content/uploads/2019/05/Finding-Array-Range.zip)
**

Introduction and List of Files
------------------------------

When you open the file, you should see something like this.  You can first test if the directory contains the file that you are testing and that directory name is correct.  You can press the button shown in the screenshot below named “Get List of Files”.  In this example, the file itself is in the folder you can use the FIND and the MID functions to make the name of the directory.

![](https://edbodmer.com/wp-content/uploads/2019/05/Introduction-Page.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/Introduction-with-Instructions.jpg)

The macro to list the files is listed below.  The big deal about this is that you make a loop around files in the directory.

.

Sub Get\_list\_of\_files()

Application.DisplayAlerts = False
Application.ScreenUpdating = False

Dim filename As String

base\_book = ActiveWorkbook.Name ' name of this book so you can go back

directory\_name = Range("directory\_name") ' get the directory name from the spreadsheet

MsgBox " This puts the files that are in " & directory\_name

' loop through each file name and open it if the extension is correct

filename = Dir(directory\_name & "\*.xl\*") ' this is a big deal --> look in the directory for excel files

Count = 1 ' Count the number of files for the output

While filename <> ""

workbookname = filename

Workbooks(base\_book).Sheets("File List").Cells(Count + 2, 2) = Count
Workbooks(base\_book).Sheets("File List").Cells(Count + 2, 3) = workbookname

Count = Count + 1

filename = Dir() ' This is also a big deal -- get the next file name

Wend

End Sub

.

![](https://edbodmer.com/wp-content/uploads/2019/05/List-of-Files.jpg)

Extracting Data in Single Range Names
-------------------------------------

The next section shows how to get data when the data is defined by a single range name.

![](https://edbodmer.com/wp-content/uploads/2019/05/One-Range-Example.jpg)

.

Sub Find\_Single\_range()

Application.DisplayAlerts = False
Application.DisplayStatusBar = True
Application.EnableEvents = True

Dim sFile As String 'File Name
Dim filename, directory\_name As String
Dim range1, range2, range3 As String
Dim result1, result2, result3 As Variant
Dim address1, address2, address3 As Variant

debug\_switch = Range("debug\_switch")

Application.ScreenUpdating = True ' choose to not show what is going on
If debug\_switch = False Then Application.ScreenUpdating = False ' shows what is happening when macro is running

base\_book = ActiveWorkbook.Name ' name of this book so you can go back to the file and print etc.
base\_sheet = ActiveSheet.Name ' name of this sheet so you can go back to the file and print etc.

directory\_name = Range("directory\_name")

' loop through each file name and open it if the extension is correct

Count = 0

range1 = Range("range1")
range2 = Range("range2")
range3 = Range("range3")

' This clears the output range (you must be in the sheet to remove this

Sheets("Output").Select
Range(Cells(Count + Range("start\_row"), Range("start\_col")), Cells(Count + Range("start\_row") + 20, Range("start\_col") + 20)).ClearContents
Sheets(base\_sheet).Select

filename = Dir(directory\_name & "\*.xl\*") ' Look of all excel files

' arg = "'" & directory\_name & "\[" & filename & "\]" & Sheet & "'!" & Range(ref).Range("A1").Address(, , xlR1C1)

While filename <> "" ' loops around each file in the folder that is defined; when there is no more, the loop is finished

' This defines the name that is used in EeecuteExcel4Macro to get the data

mydata1 = "'" & directory\_name & filename & "'!" & range1
mydata2 = "'" & directory\_name & filename & "'!" & range2
mydata3 = "'" & directory\_name & filename & "'!" & range3

DoEvents

Application.StatusBar = " Range Name 1 " & mydata1 & " In file -- " & filename

' this is the thing that retrieves the data

result1 = ExecuteExcel4Macro(mydata1)
result2 = Application.ExecuteExcel4Macro(mydata2)
result3 = Application.ExecuteExcel4Macro(mydata3)

address1 = ExecuteExcel4Macro(mydata1a)

On Error Resume Next
If result1 = "#NAME?" Then result1 = ""
If result2 = "#NAME?" Then result2 = ""
If result3 = "#NAME?" Then result3 = ""

' MsgBox " Result 1 " & mydata1 & " " & range1 & " " & result1
' MsgBox " Result 2 " & mydata2 & " " & range2 & " " & result2
' MsgBox " Result 3 " & mydata3 & " " & range3 & " " & result3
' result1 = GetValue(directory\_name, filename, range1)

workbookname = filename

range1\_output = result1
range2\_output = result2
range3\_output = result3

Workbooks(base\_book).Activate ' now go back to the base file to get the next item

If workbookname <> base\_book Then

Sheets("Output").Select

Workbooks(base\_book).Sheets("Output").Cells(2, Range("start\_col") + 1) = directory\_name

Workbooks(base\_book).Sheets("Output").Cells(Count + Range("start\_row"), Range("start\_col") + 1) = workbookname

Workbooks(base\_book).Sheets("Output").Cells(Count + Range("start\_row"), Range("start\_col") + 2) = range1\_output
Workbooks(base\_book).Sheets("Output").Cells(Count + Range("start\_row"), Range("start\_col") + 3) = range2\_output
Workbooks(base\_book).Sheets("Output").Cells(Count + Range("start\_row"), Range("start\_col") + 4) = range3\_output

End If

filename = Dir() ' Define the next file name in the directory

Count = Count + 1 ' Count for the output

Wend

after\_while:

Workbooks(base\_book).Activate

Application.StatusBar = False

End Sub

.

Reading Data Defined by Array Range Name
----------------------------------------

![](https://edbodmer.com/wp-content/uploads/2019/05/Results-of-Array-Analysis.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/Results-of-Array-Parameters.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/Results-of-Single.jpg)

.

Sub LoopThroughFiles()

Application.DisplayAlerts = False
Dim sFile As String 'File Name
' Dim range1\_output As Range

debug\_switch = Range("debug\_switch")

Application.ScreenUpdating = True ' choose to not show what is going on
If debug\_switch = False Then Application.ScreenUpdating = False ' shows what is happening when macro is running

base\_book = ActiveWorkbook.Name ' name of this book so you can go back to the file and print etc.
base\_sheet = ActiveSheet.Name ' name of this sheet so you can go back to the file and print etc.

Application.ScreenUpdating = True ' choose to not show what is going on

start\_row = Range("start\_row")
start\_col = Range("start\_col")

directory\_name = Range("directory\_name")

If debug\_switch = True Then MsgBox " Debug Switch is on"

' loop through each file name and open it if the extension is correct

Count = 0
Count1 = 0

array1 = Range("array\_1")
array2 = Range("array\_2")
array3 = Range("array\_3")


Sheets("Array 1 Results").Select
Range(Cells(Count + start\_row, start\_col), Cells(Count + start\_row + 40, start\_col + 40)).ClearContents
Sheets("Array 2 Results").Select
Range(Cells(Count + start\_row, start\_col), Cells(Count + start\_row + 40, start\_col + 40)).ClearContents
Sheets("Array Parameters").Select
Range(Cells(Count + start\_row, start\_col), Cells(Count + start\_row + 40, start\_col + 40)).ClearContents

sFile = Dir(directory\_name)
workbookname = sFile

Sheets("Array 1 Results").Select

Do Until sFile = ""

' Calculate

Workbooks.Open (directory\_name & sFile) ' Open the workbook

' On Error Resume Next

Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 1) = workbookname

On Error GoTo after\_while:

Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 2) = Range(array1).Address
Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 3) = directory\_name
Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 4) = Range(array1).Columns.Count
Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 5) = Range(array1).Row
Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 6) = Range(array1).Column
Workbooks(base\_book).Sheets("Array Parameters").Cells(Count1 + start\_row, start\_col + 7) = Range(array1).Worksheet.Name

cols = Range(array1).Columns.Count ' Number of columns in array so that you can make for loops

' This section is for finding the year

row\_cell = Range(array1).Columns.Row
col\_cell = Range(array1).Columns.Column

Cells(row\_cell, col\_cell).Select ' Go to starting cell so you can count upwards
Cells(row\_cell, col\_cell).Activate

' MsgBox " Beforre Find Year Cell row " & row\_cell & " col cell " & col\_cell & " value of cell " & Cells(row\_cell, col\_cell)

For test\_row = 1 To 10
test\_year = Cells(row\_cell - test\_row, col\_cell)
If test\_year > 1980 And test\_year < 2020 Then
' MsgBox " Row up Year " & test\_year & " test row " & test\_row
Exit For
End If
Next test\_row

year\_row = row\_cell - test\_row

Workbooks(base\_book).Sheets("Array 1 Results").Cells(Count + start\_row, start\_col + 1) = workbookname
Workbooks(base\_book).Sheets("Array 2 Results").Cells(Count + start\_row, start\_col + 1) = workbookname

For col = 1 To cols
Workbooks(base\_book).Sheets("Array 1 Results").Cells(Count + start\_row - 1, start\_col + 2 + col) = Cells(row\_cell - test\_row, col\_cell + col - 1)
Workbooks(base\_book).Sheets("Array 1 Results").Cells(Count + start\_row, start\_col + 2 + col) = Range(array1).Cells(1, col)
Next col

For col = 1 To cols
Workbooks(base\_book).Sheets("Array 2 Results").Cells(Count + start\_row - 1, start\_col + 2 + col) = Cells(row\_cell - test\_row, col\_cell + col - 1)
Workbooks(base\_book).Sheets("Array 2 Results").Cells(Count + start\_row, start\_col + 2 + col) = Range(array2).Cells(1, col)
Next col


' If Right(sFile, 4) = sExt Then GetInfo sFile

If debug\_switch = True Then MsgBox " Closing " & ActiveWorkbook.Name

ActiveWorkbook.Close
' Workbooks(workbookname).Close

Workbooks(base\_book).Activate

Resume1:

sFile = Dir ' This is the big one where define the next file name

workbookname = sFile

Count1 = Count1 + 1

Count = Count + 3


Loop

GoTo finish1:

after\_while:

MsgBox " No Range Name in File " & worbookname

If debug\_switch = True Then MsgBox " Error " & sFile & " " & sFile & " workbook name " & workbookname

' GoTo Resume1

finish1:

Workbooks(base\_book).Activate

End Sub

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8472&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9748&rand=0.5261624972682367)