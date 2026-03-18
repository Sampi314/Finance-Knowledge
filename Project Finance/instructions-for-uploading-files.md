# On-Line Course for Using Webrequest Method

**Source:** https://edbodmer.com/instructions-for-uploading-files

---

This website describes an alternative way to read data from yahoo.finance into excel.  The method is more complex, but it provides an alternative when you are having trouble reading using the Workbooks.open.  Details of the technique have changed, but it can be used to read the adjusted stock prices from yahoo.finance.

Credit
------

This method was provided by people at a website named signal.com.  There are a some programmers who are very smart and I have just copied and adjusted their method.  The technique uses something named WebRequest and requires that URL’s are adjusted.  The adjustments involve cookies and crumbs.  I do not claim to understand it all, but the method is very effective and it can be used for other applications.

Requirements
------------

When you use the method, you must have an add-in to VBA installed.

VBA Code Introduction
---------------------

The key code is shown below.

Set WebRequest = New WinHttp.WinHttpRequest ' This is the core of the method -- you need this statement

With WebRequest 'FETCH THE DATA:
   .Open "GET", WebRequestURL, False ' Need to define the URL
   .setRequestHeader "Cookie", Cookie ' This is a painful part
   .send
   .waitForResponse (response\_wait) ' Test how long to wait
End With

OutRow = Split(WebRequest.ResponseText, vbLf): RowMax = UBound(OutRow) - 1 ' Split a single row when hit vbLF

Other Code
----------

Cleaning Up CSV and Putting in Separate Cells
---------------------------------------------

The code below demonstrates how to re-format the data so that it can be used

.

Sheets.Add ' Add a new sheet to put output

For i = 1 To RowMax ' This is for speeding up things
matrix(i, 1) = OutRow(i - 1) ' Puts into separate rows with a single column
Next i

range\_name = "A1:A" & RowMax ' Where to put output

Range(range\_name) = matrix ' Put the output into a range name

clean\_yahoo ' This changes the CSV to separate columns

Application.Calculation = current\_status

End Sub

Sub clean\_yahoo()

Application.DisplayAlerts = False

Columns("A:A").Select ' Select column for text to columns

Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, \_
TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, \_
Semicolon:=False, Comma:=True, Space:=False, Other:=True, OtherChar:= \_
"=", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, 1), \_
Array(6, 1), Array(7, 1)), TrailingMinusNumbers:=True

Columns("A:A").EntireColumn.AutoFit ' Format first column

sheet\_name = Range("sheet\_name\_yahoo") ' Change the sheet name

On Error GoTo new\_name: ' Delete if existing name
Sheets(sheet\_name).Delete

new\_name:
ActiveSheet.Name = sheet\_name
ActiveSheet.Move after:=Sheets(Sheets.Count)
End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1142&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9172&rand=0.3367655970568789)