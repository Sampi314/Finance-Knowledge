# Using Current Currency Database For Invoices etc.

**Source:** https://edbodmer.com/using-current-currency-database-for-invoices-etc

---

This sheet demonstrates how you can use, modify and create a file that downloads a variety of selected currencies.  The file works retrieving data from the internet and then putting the relevant data at the top of the sheet. You can download the file you can quickly extract different currencies and copy the data into an excel file after clicking a couple of check boxes.  The file uses the workbooks.open method as well as multiple check boxes.

Introduction
------------

The file that you can download below uses current exchange rates from https://transferwise.com/us/currency-converter/usd-to-EUR-rate.  It formerly used the website [http://www.xe.com/currencyconverter/convert/?From=USD&To=CHF](http://www.xe.com/currencyconverter/convert/?From=USD&To=)
 but this website no longer allows you to scrape anything.

In the completed file below, you can select different exchange rates and press a button (Read Currencies in List) to get current updates of the exchange rate.  I have used the technique to use check boxes with TRUE and FALSE and Match as well as a macro that turns off all of the TRUE’s in all of the checkboxes.

If you download the file below, all you have to do is click on the currencies you want with the check boxes. Then click the macro box and all of your exchange rates are ready to be copied into any other file that you want.

**[File that Allows you to Quickly Retreive Exchange Rates for Many Currencies and Place Rates into an Excel File](https://edbodmer.com/wp-content/uploads/2018/08/Read-Current-Currencies.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2021/02/image-6.png)

Instructions for Using the Currency File
----------------------------------------

When you open the file, you may see something like what is in the screenshot below.  This screen shot has some existing data from a prior run.  I had begun clicking some currencies that I was interested in downloading.  Note the final currencies are included in the grey box with the date that you have downloaded the data.  This data in the grey box can be copied and pasted as values to your file.

![](https://edbodmer.com/wp-content/uploads/2018/08/currency-1.jpg)

The second screenshot shows how all the checkboxes are unclicked after pressing the button name “Set to False.”  You can see that all of the boxes are blanks.  In this case no currencies are selected.

![](https://edbodmer.com/wp-content/uploads/2018/08/Currency-2.jpg)

The third screenshot shows how after selecting Sterling and Euro, you get a new summary.  You just press the button named “Read Currencies in List”.  Technical details that explain how to create the macro to scrape the data that are part of the macro assigned to this button are shown in the next section.

![](https://edbodmer.com/wp-content/uploads/2018/08/Currency-3.jpg)

The fourth screenshot shows how you can copy the data into your spreadsheet after you have completed the download.

![](https://edbodmer.com/wp-content/uploads/2018/08/Currency-4.jpg)

Technical VBA Details
---------------------

In this section I have copied the VBA code that uses the workbooks.open technique to get the data.  The file works like other files in that you separate and make new URL’s and use the INDEX function.  Once you have the URL, the loop works through each currency, reads the currency from the internet.  The row for 1 USD is found and the entire row is copied to the base file.

.

.

Public row\_output\_number As Single
Public currency\_number As Single
Public base\_sheet As String

Sub all\_currencies()

Application.DisplayAlerts = False ' dont ask when close files
Application.ScreenUpdating = False ' dont show the screens

current\_calc = Application.Calculation

Application.Calculation = xlCalculationSemiautomatic

For Sheet = Sheets.Count To 1 Step -1

If Sheets(Sheet).Name = "Break Sheet" Then
Exit For
End If

Worksheets(Sheet).Delete

Next Sheet

Application.Calculation = xlCalculationSemiautomatic

base\_sheet = ActiveSheet.Name

date\_output = DateValue(Now) ' if you want to show the date somewhere

Range("date\_out") = date\_output ' put the title date at to
Range("date\_out").Select
Selection.NumberFormat = "d-mmm-yy"
Range("title\_1") = "Currencies for "

row\_output\_number = 200

Range("output").Clear

Range("total\_currencies").Calculate

MsgBox " This puts out beginning in row 200 " & Chr(13) & Chr(13) & " Reading " & Range("total\_currencies") & " currencies"

For i = 1 To Range("total\_currencies") ' from counta

Range("row\_num") = i

row\_output\_number = row\_output\_number + 1

read\_a\_currency

Next i

Application.StatusBar = False ' put the url name at the bottom

Sheets(base\_sheet).Select
Application.Calculation = current\_calc

End Sub

Sub read\_a\_currency() ' Subroutine that reads each link separately

Dim test\_value, test\_criteria As String

close\_file = Range("close\_file") ' Read option from sheet

Application.DisplayAlerts = False ' dont ask when close files

current\_book = ActiveWorkbook.Name ' record the existing location
current\_sheet = ActiveSheet.Name
current\_cell = ActiveCell.Address

Application.StatusBar = Range("url\_name") ' put the url name at the bottom

url\_name = Range("url\_name") ' each url name in the range name

Workbooks.Open (url\_name) ' read the file

temp\_book\_name = ActiveWorkbook.Name ' define the current sheet for closing later on

Cells.Select ' copy the sheet without ads etc
Selection.Copy
Sheets.Add ' add in the same sheet
Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks \_
:=False, Transpose:=False

test\_value = "1 USD" ' What to Look For
test\_criteria = "1 USD" ' What to Look For

evaluation = StrComp(test\_value, "1 USD", vbTextCompare) ' evaluation is zero when equal

evaluation = StrComp(test\_value, test\_criteria, vbTextCompare) ' evaluation is zero when equal


For Row = 1 To 150 ' look for the exchange rate

test\_value = Range("A:A").Cells(Row, 1) ' Look in Column A
test\_value = Left(test\_value, 5)
evaluation = StrComp(test\_value, test\_criteria, vbTextCompare)


If evaluation = 0 Then ' Zero is when found in the STRCOMP Function
match\_truncated = Row ' Retain the Row Number
Exit For
End If
Next Row

row\_number = Row ' find while in temp sheet

row\_name = row\_number & ":" & row\_number ' row name for copying

Range(row\_name).Select ' Select entire row
Selection.Copy ' Copy the entire row

If row\_output\_number = 0 Then row\_output\_number = 200

target\_cell = "A" & row\_output\_number ' where to place the result
target\_cell = row\_output\_number & ":" & row\_output\_number ' where to place the result

Workbooks(current\_book).Activate ' return to base sheet and copy
Sheets(base\_sheet).Activate
Range(target\_cell).Select

'
' Paste the single row from the currency URL
'
Sheets(base\_sheet).Select

Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks \_
:=False, Transpose:=False

If close\_file Then
Workbooks(temp\_book\_name).Close ' close the file from the URL
Else
Workbooks(temp\_book\_name).Activate

Cells.Select ' copy the sheet without ads etc
Selection.Copy

Workbooks(current\_book).Activate ' return to base sheet and copy
Sheets.Add ' add in the same sheet
Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks \_
:=False, Transpose:=False

On Error Resume Next
ActiveSheet.Name = Range("currency")

Workbooks(temp\_book\_name).Close ' close the file from the URL

ActiveSheet.Move After:=Sheets(Sheets.Count)

End If


Range(current\_cell).Select

End Sub

Sub ListBox2\_Change()

base\_cell = Selection.Address

For i = 1 To 10 ' decide how many possible items on the graph
Range("list\_out1").Cells(i, 1).Clear ' clear out the range name that will be re-filled
Next i ' note this output is named list\_out2; it can be renamed

ActiveSheet.Shapes.Range(Array("List Box 2")).Select ' change this name to the number of your box

Row = 1 ' Make a row counter to put output

For i = 1 To Selection.ListCount ' This is the number in the list box
If Selection.Selected(i) = True Then ' Only keep the selected items

Range("list\_out1").Cells(Row, 1) = Selection.List(i)

Row = Row + 1 ' Assign to the range name
End If
Next i ' Finish loop around the listbox items

Range(base\_cell).Select
Range(base\_cell).Activate

End Sub

Video Explanation of the Macro and Using the File
-------------------------------------------------

The video below shows you how to create a macro that finds the correct place in the file that is downloaded from the internet with the workbooks.open statement and how to set-up the file to download multiple exchange rates.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=5047&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10408&rand=0.9384998814627903)