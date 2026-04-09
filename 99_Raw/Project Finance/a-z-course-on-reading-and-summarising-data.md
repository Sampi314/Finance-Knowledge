# A-Z Course on Reading and Summarising Data

**Source:** https://edbodmer.com/a-z-course-on-reading-and-summarising-data

---

This page explains how you can automatically download data from the internet to excel using the WORKBOOKS.OPEN statement along with the INDIRECT function.  I show you how to test whether you can read data and then create a system that adjusts the URL to read a whole bunch of data and put the data together. When you do this, you can put together databases that can be used to present data in a creative and flexible manner. The method below explains how to do the following to create a database with multiple ticker symbols that can be automatically updated:

1.  First use the workbooks.open method to read a data from a url and put it in a new sheet.  This can be a page of data or a file that you can download.  The first task is to copy the url to the excel sheet and potentially modify the url for different stock tickers, different FRED codes, different currency codes or different dates.
2.  After creating a macro with the WORKBOOKS.OPEN method, the file is read into a new workbook.  The next step is to move the data in this new workbook back to the base workbook that has the url.  To do this you can record a macro that either copies the data or moves the sheet.  Yo must record the macro in the new sheet and then copy this macro to the original macro with the WORKBOOKS.OPEN.
3.  Once you have moved the the data to the base workbook, then re-name the sheet and close the sheet that was created using for the internet read.
4.  After you have created a sheet that reads one file, make a second macro that loops around the number of urls that you want to read. These multiple urls can be the entire urls or parts of a url that are put together with a common beginning and end.

An illustration of the macro that uses this process to read multiple stock statistics is shown below.  The first excerpt shows how to put-together a list of urls and create a flexible process that changes the url with different ticker symbols.  First find the URL as demonstrated below and copy it to a spreadsheet

![](https://edbodmer.com/wp-content/uploads/2018/03/GE-Yahoo.jpg)

Once you have a URL that works (there is a fancy word for this API or something).  Note that sometimes the URL does not work.  If it does work and it has financial data for different companies, you will probably see the ticker symbol somewhere. Split up the URL and create and INDEX function into the spreadsheet.  This enables a flexible URL that can be changed when you change the yahoo code used in the INDEX function.

![](https://edbodmer.com/wp-content/uploads/2018/03/URLS.jpg)

Once you have this, create a macro that makes a single read  of the URL with the WORKBOOKS.OPEN technique as shown below.  This will not be exactly the same for all of the different databases you can create.

After you read into different sheets, you can use the INDIRECT function to put together data from sheets.  This is illustrated in the excerpt below.

![](https://edbodmer.com/wp-content/uploads/2018/03/INDIRECT.jpg)

Example File with VBA Code for Downloading Data using WORKBOOKS.OPEN
--------------------------------------------------------------------

The file below contains the example that is described in the video and with the various VBA code.  It also demonstrates how to read from marketwatch and from google finance using the same ideas.  You can download the file and see the process and open up the VBA code or you can watch the videos below.

[Generic Macro File for Copying to Right (SHIFT, CNTL, R), Formatting (CNTL, ALT, C) and Other Functions (UDFs)](https://edbodmer.com/wp-content/uploads/2026/03/Generic-Macros.xlsm)

Videos that Demonstrate the Process of Reading Data from the Internet using the WORKBOOKS.OPEN method
-----------------------------------------------------------------------------------------------------

I have made too many videos that demonstrate this process.    The first  two videos below demonstrate the process with yahoo (note that the urls have changed from the time I made the video).

The video below demonstrates how to use the INDIRECT function once you have downloaded the data.

The video below demonstrates how to clear data from multiple sheets after you have created a database.

.



Sub read\_yahoo()

' First - Define where you began

base\_book = ActiveWorkbook.Name
base\_sheet = ActiveSheet.Name
base\_cell = ActiveCell.Address
num\_sheets = Sheets.Count

Application.DisplayAlerts = False

Workbooks.Open (Range("yahoo\_url")) ' Read the url
temp\_book = ActiveSheet.Name ' Remember the sheet of the existing URL

Cells.Select ' Select all of the cells in the existing sheet
 Selection.Copy ' Copy all of the cells from the new sheet
 
 Windows(base\_book).Activate ' Go back to your original workbook
 Sheets.Add After:=Sheets(num\_sheets) ' Put at the end
 
On Error GoTo clear\_data: ' If there is an existing sheet, skip this part and delete existing sheet
 ActiveSheet.Name = Range("yahoo\_sheet") ' make a rage name
 GoTo skip\_clear:

clear\_data: ' This is if there is and existing sheet
 ActiveSheet.Delete
 yahoo\_sheet = Range("yahoo\_sheet")
 Sheets(yahoo\_sheet).Select ' Select the existing sheet
 Cells.Clear ' clear the existing sheet stuff

skip\_clear:
 Range("A1").Select ' This applies to exiting sheet
 
 Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks \_
 :=False, Transpose:=False ' Paste special to get rid of advertisosnt
 
 Sheets(base\_sheet).Select
 Range(base\_cell).Select
 Windows(temp\_book).Close ' Close the first sheet (could do this with worbooks(temp\_book).close
End Sub


The VBA code for putting everything together is shown below.



For i = 1 To 8

Range("yahoo\_code") = i
 read\_yahoo

Next i

End Sub



.


India Case Study with Reading Data

![](https://edbodmer.com/wp-content/uploads/2019/03/India-Read-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/03/India-Summary.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/03/India-URLS-2.jpg)

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Subject |     | Excel Exercise File |     | Video |     | Chapter Reference |     | Page Reference |
|     |     |     |     |     |     |     |     |     |     |
|     | Reading Basic Data from the Yahoo.Finance.com |     | Basic Read from Yahoo |     | [https://www.youtube.com/watch?v=0u9lBxfpD6A](https://www.youtube.com/watch?v=0u9lBxfpD6A) |     |     |     |     |
|     | Reading Text Files from the Internet and placing files in new sheets |     | Upload Exercise 2: Reading Text Files |     | [https://www.youtube.com/watch?v=vLXOCZTuVZ0](https://www.youtube.com/watch?v=vLXOCZTuVZ0) |     | Chapter 16 |     | 193 |
|     | Reading Stocks from Yahoo – Reading One URL with Workbooks.open |     | Financial Ratio Download 1 |     |     |     | Chapter 16 |     | 201 |
|     | Using Match, Index and Indirect to Summarise Downloaded Data |     | Housing Data |     |     |     | Chapter 16 |     | 193 |
|     | Reading Data on Gas Prices |     | Upload Exercise 1: Gas Price Upload |     | [https://www.youtube.com/watch?v=ZfO9K0STL8M](https://www.youtube.com/watch?v=ZfO9K0STL8M) |     | Chapter 16 |     | 193 |
|     | Reading and Extracting Data from St. Louis Fed 1 with multiple urls |     | Financial Ratio Download 1 |     | [https://www.youtube.com/watch?v=yxJuhYqQEdM](https://www.youtube.com/watch?v=yxJuhYqQEdM) |     | Chapter 16 |     | 193 |
|     | Upload Multiple Web Pages to Excel |     | Upload Exercise 2: Hydro Upload |     | [https://www.youtube.com/watch?v=mDGR1Pdmp20](https://www.youtube.com/watch?v=mDGR1Pdmp20) |     | Chapter 16 |     | 193 |
|     | Reading Data on Gas Prices |     | Upload Exercise 1: Gas Price Upload |     | [https://www.youtube.com/watch?v=ZfO9K0STL8M](https://www.youtube.com/watch?v=ZfO9K0STL8M) |     | Chapter 16 |     | 193 |
|     | Electricity price read all macros |     | US Electricity Prices |     | [https://www.youtube.com/watch?v=uNKQxKOlxog](https://www.youtube.com/watch?v=uNKQxKOlxog) |     | Chapter 16 |     | 193 |
|     | Electricity price extraction |     | US Electricity Prices |     | [https://www.youtube.com/watch?v=cmw4fm1lQxw](https://www.youtube.com/watch?v=cmw4fm1lQxw) |     | Chapter 16 |     | 193 |
|     | Electricity price reading |     | US Electricity Prices |     | [https://www.youtube.com/watch?v=G2Rbh2F6luc](https://www.youtube.com/watch?v=G2Rbh2F6luc) |     | Chapter 16 |     | 193 |
|     | Retrieving Currencies and Importing to Excel File |     | Get Currencies |     |     |     | Chapter 16 |     | 193 |
|     | Downloading Data on Saudi Stock Bubble |     | Saudi Stocks |     | [https://www.youtube.com/watch?v=C\_Sz6-iO-OQ](https://www.youtube.com/watch?v=C_Sz6-iO-OQ) |     | Chapter 2 |     | 40  |
|     | Downloading Data on House Prices and Demand 1 |     | Housing Data 1 |     | [https://www.youtube.com/watch?v=U-EJ2D1JVpM](https://www.youtube.com/watch?v=U-EJ2D1JVpM) |     | Chapter 16 |     | 193 |
|     | Clearing Sheets to Enable Updating of Data |     | Housing Data 1 |     |     |     | Chapter 16 |     | 193 |
|     | Adjusting Nominal Data for Inflation |     | Housing Data |     | [https://www.youtube.com/watch?v=L2TM2VG72MU](https://www.youtube.com/watch?v=L2TM2VG72MU) |     | Chapter 16 |     | 193 |
|     | Read Yield Curve as Basis for Forward Interest Rate Analysis |     | Yield Curve |     | [https://www.youtube.com/watch?v=PwRPLB\_ungE](https://www.youtube.com/watch?v=PwRPLB_ungE) |     |     |     |     |
|     | Read Stock Prices from Google – Part 3; Reading Indicies |     | Read Indicies |     | [https://www.youtube.com/watch?v=5ivVds9a9Wc](https://www.youtube.com/watch?v=5ivVds9a9Wc) |     | Chapter 16 |     | 201 |
|     | Read Stock Prices from Google – Part 1 |     | Read Saudi Stocks |     | [https://www.youtube.com/watch?v=2ZZqy0hczPw](https://www.youtube.com/watch?v=2ZZqy0hczPw) |     | Chapter 16 |     | 193 |
|     | Read Stock Prices from Google – Part 2 |     | Read Saudi Stocks |     | [https://www.youtube.com/watch?v=v8n\_Jv9WyHQ](https://www.youtube.com/watch?v=v8n_Jv9WyHQ) |     | Chapter 16 |     | 201 |
|     | Read Stock Prices from Google – Part 4; Match/Index/Indirect |     | Read Saudi Stocks |     | [https://www.youtube.com/watch?v=W\_pg\_nFLoaM](https://www.youtube.com/watch?v=W_pg_nFLoaM) |     | Chapter 16 |     | 201 |
|     | Read Stock Prices from Google – Part 5; Graphs with #N/A |     | Read Saudi Stocks |     | [https://www.youtube.com/watch?v=C\_Sz6-iO-OQ](https://www.youtube.com/watch?v=C_Sz6-iO-OQ) |     | Chapter 16 |     | 201 |
|     | Summarizing Annual Stock Prices – Stock Summary by Date |     | Financial Ratio Download 2 |     | [https://www.youtube.com/watch?v=IqQLg7y61pg](https://www.youtube.com/watch?v=IqQLg7y61pg) |     | Chapter 16 |     | 201 |
|     | Read Industry Data and Put in New Sheets from FRED |     | Read Airfreight Industry Data |     | [https://www.youtube.com/watch?v=9-ZEicsj0iw](https://www.youtube.com/watch?v=9-ZEicsj0iw) |     |     |     |     |
|     | Update of Read Stocks |     | Read Oil Stocks |     | [https://www.youtube.com/watch?v=-OgyfFub\_do](https://www.youtube.com/watch?v=-OgyfFub_do) |     |     |     |     |
|     | Reading Financial Data |     | Raw Financial Data.xls |     |     |     |     |     |     |
|     | Simple Classification Exercise |     | Simple Classification.xls |     |     |     |     |     |     |
|     | Complex Classification Exercise |     | Raw Financial Data.xls |     |     |     |     |     |     |
|     | Financial Ratio Download 1 – Finding Tickers |     | Financial Ratio Download 1 |     |     |     |     |     |     |
|     | Financial Ratio Download 2 – Reading One URL with Workbooks.open |     | Financial Ratio Download 1 |     | [https://www.youtube.com/watch?v=VLmzmcw\_s](https://www.youtube.com/watch?v=VLmzmcw_s) |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 3 – Stock Summary by Date |     | Financial Ratio Download 2 |     | [https://www.youtube.com/watch?v=IqQLg7y61pg](https://www.youtube.com/watch?v=IqQLg7y61pg) |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 4 – Moving Sheets |     | Financial Ratio Download 3 |     |     |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 5 – Reading Multiple Companies |     | Financial Ratio Download 4 |     | [https://www.youtube.com/watch?v=\_byg3ojjUgo](https://www.youtube.com/watch?v=_byg3ojjUgo) |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 6 – Extracting Data from Sheets |     | Financial Ratio Download 5 |     | [https://www.youtube.com/watch?v=D2mClmUwkro](https://www.youtube.com/watch?v=D2mClmUwkro) |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 7 – Selecting Companies with TRUE/FALSE |     | Financial Ratio Download 5 |     | [https://www.youtube.com/watch?v=Nri1In4rDw0](https://www.youtube.com/watch?v=Nri1In4rDw0) |     | Chapter 16 |     | 193 |
|     | Financial Ratio Download 8 – Reading Companies from Market Watch |     |     |     |     |     |     |     |     |
|     | Shows how to read in a set of companies and then analyse the data |     | Yieldco Download and Cost of Capital |     | [https://www.youtube.com/watch?v=hGMFl6czx6A](https://www.youtube.com/watch?v=hGMFl6czx6A) |     |     |     |     |
|     | ………………………………………………………………………………… |

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1360&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7832&rand=0.4540976401583555)