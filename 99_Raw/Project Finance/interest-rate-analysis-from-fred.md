# Interest Rate and Credit Spread Analysis from FRED

**Source:** https://edbodmer.com/interest-rate-analysis-from-fred

---

This page describes how you can quickly create an interest rate and credit spread database with automatic updates. The database retrieves information on interest rates and presents flexible graphs on credit spreads, the term structure of interest rates, interest rates in different currencies and other items.  You can mix and match the interest rate statistics to compare credit spreads with long-term or short-term interest rates. As with other database files, the process uses the WORKBOOKS.OPEN function to retrieve data and download from the internet to excel. Note that in August 2024 FRED changed the way the files are available and I changed the macros. The file below has the new method for scraping the data with workbooks.open.

You can download the interest rate database download by pressing the button below. The interest rate database attached to the button may not be current to the latest month. To update the database you can follow the instructions in the section below (you press the Clear Button and after the sheets a cleared out, press the Create Button). If you have suggestions about presenting the data please email me at edwardbodmer@gmail.com.

.

.**[Database with Interest Rates, Credit Spreads and Other Data from the FRED Database for Comparison and Presentation](https://edbodmer.com/wp-content/uploads/2026/03/Interest-Rates-16.04.2025.xlsm)
**

.

A few years ago you had to pay a lot for interest rate data from sources like Bloomberg.  It was very difficult for example to find public data on credit spreads of bonds with different ratings. Now you can get very good historic data from the St. Louis Fed. This includes all sorts of interest rate maturities, swap rates, credit spreads and credit spreads from different countries. There are a couple of examples of downloading interest rates from the St. Louis Fed and the Federal Reserve Economic Database (FRED) below.

Using the Interest Rate Database
--------------------------------

The screenshots below demonstrate how you can use the database.  You can go to different sheets of the file and work with the graphs. The first screenshot illustrates presentation of a single data item that is available for download. As is usual for drop-down and boxes, you can select alternative data items. Similarly, you can select different dates.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Single-Graph.jpg)

The second example is a very common use of the file where you can compare two items. In the screenshot below the example compares credit spreads of BBB bonds and BB bonds over time.  You can select different time periods and different periods.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Double-Graph.jpg)

.

The third example in the screenshot below demonstrates how you can add two series to make an analysis. In this case, the credit spread in BBB bonds is added to a 5-year interest rate to give an indicative rate for 5-year swaps.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Area-Graph.jpg)

.

Updating the Interest Rate Database
-----------------------------------

The screenshot below illustrate how you can update the database. You go to the page named “Get Data” and then first press the “CLEAR SHEETS” button as shown below. (It is a good idea to press the F12 key and to re-save the file as all of the detailed sheets will be deleted).  After clearing the sheets, press the “Get All Series” button and the new data will be placed into sheets at the end of the file.  As shown on the screenshot, this should take less than two minutes unless you have a very slow internet connection.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Read.jpg)
---------------------------------------------------------------------------

If you use the webrequest method, you can see the progress of reading the different series. You can also look at the documentation of the series in the individual sheets.

![](https://edbodmer.com/wp-content/uploads/2022/06/image-5.png)

.

Other Examples
--------------

The screenshots below illustrate how you can compare different currencies and different tenures.  It also illustrates how you can evaluate implied expected inflation from bonds that are tied to the inflation rate.

![](https://edbodmer.com/wp-content/uploads/2020/01/Database-Short-term-and-currencies.jpg)

![](https://edbodmer.com/wp-content/uploads/2020/01/Interest-Database-Inflation.jpg)

Technical Details of Compiling the Database
-------------------------------------------

The database is created by extracting data from individual sheets and putting the data together in a summary sheet.  The compiled database is illustrated in the screenshot below. The process works with by combining the INDIRECT function with the INDEX and MATCH functions.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Database-Summary.jpg)

.

The screenshot below demonstrates one of the sheets that is created by reading an individual item from the FRED database.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Intrest-Rate-Detailed-Download.jpg)

.

Technical Discussion on Creating Databases from Downloaded Data
---------------------------------------------------------------

.

The process of collecting interest rates uses techniques where you plop the downloaded files into different sheets using the WORKBOOKS.OPEN method.  Then, you use a little VBA code with a FOR NEXT loop and the INDEX function to collect the data and put it into a database summary sheet. To summarise data, you can use the MATCH, INDEX and INDIRECT functions. Some of the techniques to create databases with the workbooks.open method are described in the powerpoint slides below.

[Power Point Slides that Explain Technical Details of the Comprehensive Database with Financial Data, Multiples and Cost of Capital](https://edbodmer.com/wp-content/uploads/2018/04/A-Z-Reading-Financial-Ratios-1.pptx)

[Power Point Slides the Explain the Technical Details Associated with the Comprehensive Stock Price File](https://edbodmer.com/wp-content/uploads/2018/04/Comprehensive-Stock-Prices.pptx)

.

VBA Code for Reading and Organising Data
----------------------------------------

The first program shows how to use the workbooks.open to get data. You can find this code in the interest rate workbook that is available for download.

.

Sub GetData()

base\_book = ActiveWorkbook.Name
base\_sheet = ActiveSheet.Name

num\_sheets = Sheets.Count

On Error GoTo exit1:
Workbooks.Open (Range("econ\_url"))

temp\_book = ActiveWorkbook.Name
temp\_sheet = ActiveSheet.Name

'
Columns("A:A").Select
Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, \_
TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=True, Tab:=True, \_
Semicolon:=False, Comma:=False, Space:=True, Other:=False, FieldInfo \_
:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, 1), Array(6, 1), \_
Array(7, 1)), TrailingMinusNumbers:=True
Sheets(temp\_sheet).Copy after:=Workbooks(base\_book).Sheets(num\_sheets)

If Range("quick\_read") = False Then

min\_date = WorksheetFunction.Min(Range("A:A")) ' get min date
data\_row\_start = WorksheetFunction.Match(min\_date, Range("A:A"), 0) ' fin row number

For Row = 1 To data\_row\_start - 1
For col = 2 To 20
Cells(Row, 1) = Cells(Row, 1) & " " & Cells(Row, col)
Cells(Row, col) = ""
Next col
Next Row

End If

On Error GoTo problem\_reading
ActiveSheet.Name = Range("series\_name")

GoTo skip2:

problem\_reading:
MsgBox "problem with sheet name " & Range("series\_name")
On Error GoTo 0

skip2:
Workbooks(temp\_book).Close

exit1:

End Sub
.



.
Sub get\_all\_data()

calc\_status = Application.Calculation
Application.Calculation = xlCalculationManual

Application.DisplayAlerts = False
Application.ScreenUpdating = False

base\_sheet = ActiveSheet.Name

Range("start\_time") = Time

For i = 1 To Range("total\_to\_read")

Range("code") = i

Sheets(base\_sheet).Select
ActiveSheet.Calculate

On Error Resume Next
Application.StatusBar = " Downloading " & Range("series\_name") & " Series " & i & " Out of " & Range("total\_to\_read")

GetData ' Run the file that gets the data for a single series

Range("all\_data").Cells(i, 1).Select

series\_name = Range("series\_name")

ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= \_
"'" & series\_name & "'!A1", TextToDisplay:=sheet\_name

Next i

Application.Calculation = calc\_status
Application.StatusBar = False

Range("end\_time") = Time

Sheets(1).Select

End Sub

Sub clear\_sheets()

calc\_status = Application.Calculation
Application.Calculation = xlCalculationManual

Application.DisplayAlerts = False

For i = Sheets.Count To 1 Step -1

If Sheets(i).Name = "BREAK" Then
Application.Calculation = calc\_status
Exit Sub
End If

Sheets(i).Delete

Next i

Application.Calculation = calc\_status

End Sub

Alternative to Indirect Function
--------------------------------

You can use some rough programming where you copy the sheet name to the LOOKUP function and replace the INDIRECT function. The VBA code below illustrates this process.

.

This page describes how you can quickly create an interest rate and credit spread database with automatic updates. The database retrieves information on interest rates and presents flexible graphs on credit spreads, the term structure of interest rates, interest rates in different currencies and other items.  You can mix and match the interest rate statistics to compare credit spreads with long-term or short-term interest rates. As with other database files, the process uses the WORKBOOKS.OPEN function to retrieve data and download from the internet to excel.

The interest rate database is available for download by pressing the button below. The interest rate database attached to the button may not be current to the latest month. To update the database you can follow the instructions in the section below (you press the Clear Button and after the sheets a cleared out, press the Create Button).

**[Interest Rate Database that Extracts Data from the FRED Database with Quick Updates and Flexible Graphs](https://edbodmer.com/wp-content/uploads/2020/01/Interest-Rates.xlsm)
**

A few years ago you had to pay a lot for interest rate data from sources like Bloomberg.  It was very difficult for example to find public data on credit spreads of bonds with different ratings. Now you can get very good historic data from the St. Louis Fed. This includes all sorts of interest rate maturities, swap rates, credit spreads and credit spreads from different countries. There are a couple of examples of downloading interest rates from the St. Louis Fed and the Federal Reserve Economic Database (FRED) below.

Using the Interest Rate Database
--------------------------------

The screenshots below demonstrate how you can use the database.  You can go to different sheets of the file and work with the graphs. The first screenshot illustrates presentation of a single data item that is available for download. As is usual for drop-down and boxes, you can select alternative data items. Similarly, you can select different dates.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Single-Graph.jpg)

The second example is a very common use of the file where you can compare two items. In the screenshot below the example compares credit spreads of BBB bonds and BB bonds over time.  You can select different time periods and different periods.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Double-Graph.jpg)

The third example in the screenshot below demonstrates how you can add two series to make an analysis. In this case, the credit spread in BBB bonds is added to a 5-year interest rate to give an indicative rate for 5-year swaps.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Area-Graph.jpg)

Updating the Interest Rate Database
-----------------------------------

The screenshot below illustrate how you can update the database. You go to the page named “Get Data” and then first press the “CLEAR SHEETS” button as shown below. (It is a good idea to press the F12 key and to re-save the file as all of the detailed sheets will be deleted).  After clearing the sheets, press the “Get All Series” button and the new data will be placed into sheets at the end of the file.  As shown on the screenshot, this should take less than two minutes unless you have a very slow internet connection.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Read.jpg)
---------------------------------------------------------------------------

.

Other Examples
--------------

The screenshots below illustrate how you can compare different currencies and different tenures.  It also illustrates how you can evaluate implied expected inflation from bonds that are tied to the inflation rate.

![](https://edbodmer.com/wp-content/uploads/2020/01/Database-Short-term-and-currencies.jpg)

![](https://edbodmer.com/wp-content/uploads/2020/01/Interest-Database-Inflation.jpg)

.

Technical Details of Compiling the Database
-------------------------------------------

.

The database is created by extracting data from individual sheets and putting the data together in a summary sheet.  The compiled database is illustrated in the screenshot below. The process works with by combining the INDIRECT function with the INDEX and MATCH functions.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Interest-Rate-Database-Summary.jpg)

.

The screenshot below demonstrates one of the sheets that is created by reading an individual item from the FRED database.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Intrest-Rate-Detailed-Download.jpg)

Technical Discussion on Creating Databases from Downloaded Data
---------------------------------------------------------------

The process of collecting interest rates uses techniques where you plop the downloaded files into different sheets using the WORKBOOKS.OPEN method.  Then, you use a little VBA code with a FOR NEXT loop and the INDEX function to collect the data and put it into a database summary sheet. To summarise data, you can use the MATCH, INDEX and INDIRECT functions. Some of the techniques to create databases with the workbooks.open method are described in the powerpoint slides below.

.

[Power Point Slides that Explain Technical Details of the Comprehensive Database with Financial Data, Multiples and Cost of Capital](https://edbodmer.com/wp-content/uploads/2018/04/A-Z-Reading-Financial-Ratios-1.pptx)

.

[Power Point Slides the Explain the Technical Details Associated with the Comprehensive Stock Price File](https://edbodmer.com/wp-content/uploads/2018/04/Comprehensive-Stock-Prices.pptx)

.

.

VBA Code for Reading and Organising Data
----------------------------------------

The first program shows how to use the workbooks.open to get data. You can find this code in the interest rate workbook that is available for download.

.

.**[Interest Rate Database that Extracts Data from the FRED Database with Quick Updates and Flexible Graphs](https://edbodmer.com/wp-content/uploads/2020/01/Interest-Rates.xlsm)
**

.

    Sub Indirect_replace()
    '
    ' Alternative to Indirect
    '
    
    '
    For col = 1 To Range("sheet_names").Columns.Count              ' sheet_names is range name with sheets to get
            
        name_of_sheet = Range("sheet_names").Cells(1, col)         ' Work through the name of each sheet
        
        name_to_replace = "'" & name_of_sheet & "'"                ' create a range name for lookup
            
                                                                   '    MsgBox name_to_replace
            
        lookup_name = "=LOOKUP($A5," & name_to_replace & "!A:A," & name_to_replace & "!B:B)"
            
                                                                   '    MsgBox lookup_name
            
        Range("row_2").Cells(1, col) = lookup_name                 ' Make sure the row_1 name is there
        
    
    Next col
    
        Range("row_2").Select
        Range(Selection, Selection.End(xlDown)).Select
        Selection.FillDown
    
    
    End Sub
    

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=508&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9232&rand=0.950662611331225)