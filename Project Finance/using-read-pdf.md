# Using Read PDF

**Source:** https://edbodmer.com/using-read-pdf

---

This page explains how to use an excel file read PDF to excel with VBA code that allows you to convert many PDF files to Excel. To use the read PDF to Excel and format a PDF file into a usable excel file you should open the file below that a number of different various macros.  The read PDF to excel macro sets deal with different types of problems that can arise when copying from PDF to Excel using alternative macros. Unlike other PDF to excel programs that you can purchase, all of the macros are provided on an open source basis. The conversions from PDF to Excel are geared to financial modelling applications where you want the data in excel. When using the excel model with macros to convert, you should first copy and paste special the stuff you want from the PDF file (this can be straight from google chrome or from adobe).  When you paste, paste special as unicode text. You do not have to download a PDF file, but you can take it directly from the internet (not with the internet explorer). [A step-by-step example of how to use the read pdf program is included in the case studies page.](https://edbodmer.com/dabhol-ipp-analysis-and-project-finance/)

Please note that when you run the read pdf to excel program, it does not work perfectly every time because of the vagaries in the way data comes into excel from pdf programs.  I hope you do not give up when this happens. I think I have been able to solve very many of the practical problems, but not every single one.  If you are having problems, please do not hesitate to send me an e-mail at edwardbodmer@gmail.com.  [An example of a more complex example is included at on a subsequent page. https://edbodmer.com/complex-a-z-example/.](https://edbodmer.com/complex-a-z-example/)
 To re-format pdf’s, click on the button below and then download the file.  Make sure that the status bar at the bottom of your excel file has the Shift, CNTL A instructions.  This status bar should show up in other excel files that you move to.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

**[Asian Version of Excel File the Reads PDF (or Internet) to Excel with Macros that are Implemented with SHIFT CNTL Afor](https://edbodmer.com/wp-content/uploads/2018/10/Read-PDF-to-Excel-Asian.xlsm)
**

**[File with Macros that Format Data Copied into and Excel File from the U.S.Securities and Exchange Website](https://edbodmer.com/wp-content/uploads/2019/04/Scenario-Reporter.xlsm)
**

On this page I walk through different problems and issues that arise when copying data from a PDF file and pasting it to an Excel file.

1.  The first case is the most common situation where the PDF file is compressed into rows of data with multiple values. The data appear in excel without separation into different columns.
2.  The second case is the situation where each piece of data is in a separate row. In this case there is one data value and the data is not compressed into a single column.
3.  The third situation describes correcting the situation where data has an elegant European format with spaces instead of commas and a comma instead of decimals.
4.  Other issues are addressed include fixing titles after you have re-formatted the data.

Basic Read PDF to Excel – Multiple Data and Words Compressed into One Column for Each Line
------------------------------------------------------------------------------------------

In any of the cases for formatting data, the excel file “read\_pdf\_to\_excel.xls” must be open and make sure you enable macros.  Then, with the file open you copy and paste data from a PDF file to your blank excel sheet (best into cell A1).  After the data is there, you press SHIFT, CNTL, A. Normally, the data should be re-formatted and you should be happy.

Converting PDF to Excel does depend on the type of format that appears in excel from copying the pdf file; whether the pdf file is locked; and, whether the copying is directly from the internet or from a downloaded file that is read into acrobat. The normal case discussed in this section is the situation were the copied data is in a single un-formatted column (maybe 80%-90% of the time).  An example of a pdf file with the normal format can be found in the pdf file below (go to page 17 and copy the financial summary to a blank excel sheet somewhere).

**[Example PDF file with Normal Conversion Format (Sun Edison 2013 Report -- Numbers on Page 17 or F1)](https://edbodmer.com/wp-content/uploads/2018/07/2013-ANNUAL-REPORT-FINAL.pdf)
**

In this case of multiple pieces of data squeezed into a single row, the PDF can be copied into excel and the macro in the the macro can be easily implemented. The process works in situations where the data is copied directly from a file opened in the internet with Chrome or Firefox (although not with Microsoft’s horrible explorer where the data all goes into one line) or whether the file is downloaded and then read into acrobat. An example of what happens when you copy from the pdf to excel in this typical case is show below:

### ![](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-Raw.jpg)

In this typical case, the macro in the PDF\_to\_Excel file below can be run. I am being repetitive, but you press SHIFT CNTL A from the sheet with the raw data.  After you press Shift, CNTL, A a menu like the one shown on the screenshot below should appear.  Just press the top green button.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PFD-Sheet.jpg)

.

Pressing the top green button should be done whether the pdf is copied directly from the internet or whether the file is downloaded and then read into acrobat. The result is illustrated below:

.

![](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-Formatted.jpg)

.

Sometimes, you may get repetitive rows after you press the green button. In this case you can re-do the SHIFT, CNTL, A from the raw data page — make sure you go back to the page with the messy stuff.  But before pressing the green button, press the little yellow button named CONVERSIONS AND ADJUSTMENTS.  Then, click the COMBINE ROWS check box.  After doing this, press exit and the press the green button again.  The output should the be cleaned.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Adjustments-and-Conversions.jpg)
-----------------------------------------------------------------------------------------

.
-

Videos Illustrating the Read PDF Process in the Basic Case
----------------------------------------------------------

Over the last few years I have made a bunch of videos that endeavor to explain various issues that can arise with the Read PDF to Excel tool. Some of the videos are now obsolete because I have changed the way the VBA code works a bit.

The videos in the table below address a whole lot of different things that can happen if you try to copy PDF files into Excel. Many can be solved with the macros that are included in the file available to download from the button above. Other problems with reading PDF to excel can be solved with the “WORD” method as described in one of the videos. Another problem of locked pdf files can be addressed with an odd technique of uploading the files to google drive. The first video works through a basic case.  It could be a short video but I ramble too much.  This is the case where the data is in a single compressed column as shown above.

.

The second video below explains what to do when there are a whole bunch of dots and you can make an adjustment in the the column width option from the screen form.

.

.

Note: If the read PDF is not working from Firefox, it may work better using Google Chrome and then pasting with unicode text (sorry about this).

Cleaning Up PDF Data in Excel When each Data Item is in a Separate Row in a Single Column
-----------------------------------------------------------------------------------------

Sometimes when you copy data into excel it appears in a format where each data item is in a separate row as shown in the screenshot below. As long as the number of rows are consistent, then the copied data can be cleaned up.  You can do this by pressing the second rather than the first green button after you press the Shift, CNTL, A sequence that has a title of single pieces of data in separate rows.  After you press this button, a second screen that looks something like the screenshot below will appear (I say something like, because I change the program more often than I change the website).

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PDF-Single-Column.jpg)

In cases like this, there are various ways to adjust the data to get it to a consistent format. These methods include:

– You have the problem walk down the rows.  As soon as there is text, the program will begin a new row and then put the data after the text. This works if there is text, then data, then text etc. like the example below.  In this case, DO NOT check any of the boxes in the screen that appears.

– You can have the program walk down a fixed number of rows.  This works when the data is not interrupted by text.  For example if the PDF has 31 rows (like in the complex example on the next page), you can enter the number 31 and after the number of rows is hit, the data is put into a second column.  In this case use the first check box in the screen above.

– You can have the program automatically start a new column of data as soon as a year (like 2018) appears in the data. In this case, check the box named “Break with Years”

In all of these cases,  after you run the read pdf program using this method, the data is transposed from rows to columns.

![](https://edbodmer.com/wp-content/uploads/2019/04/PDF-Example-3.png)

![](https://edbodmer.com/wp-content/uploads/2019/04/PDF-Example-4.png)

![](https://edbodmer.com/wp-content/uploads/2019/04/PDF-Example-5.png)

![](https://edbodmer.com/wp-content/uploads/2019/04/ReadPDF4.jpg)

' Here define the start year and end year for testing
' careful with this
' add a test with mod cells(row,1) mod 1 = 0
' Note if you are using the year and you have more historic years you can adjust this


If use\_year = True And Cells(Row, 1) > 2000 And Cells(Row, 1) < 2040 Then ' this tests if year -- if year make a string
year\_text = "'" & Cells(Row, 1)
Cells(Row, 1) = year\_text
End If

.
-

Read PDF to Excel with Titles Adjustments

I have struggled with getting the macros to correctly adjust the titles in the read pdf to excel file after the you process the information.  The video below explains how you can use the SHIFT, CNTL, T short-cut to access a menu that allows you to fix the titles.  The video also illustrates how to get data from excel into Power BI after you have read in the data.

The second video describes some additional features that I have added including adjusting the titles.

.

Reading PDF Files that are Locked with Passwords
------------------------------------------------

If the PDF file is locked with a password, there is trick you can do to get around the problem. This involves uploading the file into Google Drive. With the file uploaded, you can copy information to excel. When you copy to to excel, the format is like number 1 above and there are blank lines. A macro is included in the PDF\_to\_EXCEL file that deletes blank lines to deal with this. 4. Sometimes, the PDF files that are read in have odd spaces inbetween numbers and spaces between the brackets. I have no idea why this sometimes happens and it is a real pain. The PDF to Excel file has macros that “clean up” the numbers so that the macro discussed in step 1 can be used. The example below illustrates a corrupted file that must be fixed:

In this case the pdf may be copied into a WORD file which can the be copied into excel. The macro in the PDF\_to\_EXCEL file does not have to be run. This does not work when the pdf is copied directly from the internet

Case with Corruption in Numbers
-------------------------------

.

Read PDF to Excel.xlsm

Read PDF Columns.xlsm

Format SEC.xlsm

CO Springs 2013annualreport.pdf

energy bal.pdf

FPL Standard and Poors.pdf

The PDF to Excel videos are summarised below. To watch the video, just click on the link

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Subject |     | Excel Exercise File |     | Video |     | Chapter Reference |     | Page Reference |
|     |     |     |     |     |     |     |     |     |     |
|     | Explains the different options in the Read PDF File |     | Revised Read PDF to Excel – Alternative Methods |     | [https://www.youtube.com/watch?v=GZpKXrK07BM](https://www.youtube.com/watch?v=GZpKXrK07BM) |     | Chapter 4 |     | 28  |
|     | Comparison of PDF Macro and Word Import 1 |     | Read PDF to Excel/Sun Edison |     |     |     | Chapter 4 |     | 28  |
|     | Comparison of PDF Macro and Word Import 2 |     | Read PDF to Excel/Chesapeak Annual Report |     |     |     | Chapter 4 |     | 28  |
|     | Common PDF Read with One Column Case 1 |     | Read PDF to Excel |     | [https://www.youtube.com/watch?v=wG2K-\_XX22U](https://www.youtube.com/watch?v=wG2K-_XX22U) |     | Chapter 4 |     | 28  |
|     | Common PDF Read with One Column Case 2 |     | Read PDF to Excel/Sun Edison |     | [https://www.youtube.com/watch?v=SlbkSw0R8uM](https://www.youtube.com/watch?v=SlbkSw0R8uM) |     | Chapter 4 |     | 28  |
|     | Common PDF Read with One Column Case 3 |     | Read PDF to Excel/Chesapeak Annual Report |     | [https://www.youtube.com/watch?v=xZGtswFGA6s](https://www.youtube.com/watch?v=xZGtswFGA6s) |     | Chapter 4 |     | 28  |
|     | PDF Read with One Column and Dots in Financial Reports |     | Read PDF to Excel/Tribune Company |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Corruption in Numbers 1 |     | Read PDF to Excel/Co Springs |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Corruption in Numbers 2 |     | Read PDF to Excel/Chesapeak Annual Report |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Word Adjustment Case 1 |     | Read PDF to Excel/FPL S&P |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Word Adjustment Case 2 |     | Read PDF to Excel/Range Resources |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Password Locked File 1 |     | Read PDF to Excel/Plymoth Case Study |     |     |     | Chapter 4 |     | 28  |
|     | Read PDF to Excel with Password Locked File 2 |     | Read PDF to Excel/IEA File |     | [https://www.youtube.com/watch?v=MKmlslyEsfc](https://www.youtube.com/watch?v=MKmlslyEsfc) |     | Chapter 4 |     | 28  |
|     | Using Read PDF to Excel with Checking Account |     |     |     | [https://www.youtube.com/watch?v=1gGFphxbEGE](https://www.youtube.com/watch?v=1gGFphxbEGE) |     | Chapter 4 |     | 28  |
|     | Creating a PDF File to Read Two Columns of Data |     | Read PDF with Multiple Columns |     | [https://www.youtube.com/watch?v=1gd8s2Q3mVE](https://www.youtube.com/watch?v=1gd8s2Q3mVE) |     |     |     |     |
|     | Adjusting the User-form Screen in Read to PDF File |     | Read PDF |     |     |     |     |     |     |
|     | Demonstration of Read to PDF with Two Columns |     | Read PDF/Multiple Columns |     |     |     |     |     |     |
|     | Reading SEC Text Files with Read PDF Function |     | Read PDF |     |     |     |     |     |     |
|     | Re-formatting SEC Files with Macro |     |     |     |     |     |     |     |     |
|     |     |     | Format Files with European Data |     |     |     |     |     |     |
|     | Reading Financial Statements Efficiently with UNION Function |     | Read PDF |     |     |     |     |     |     |
|     | Development of Union Function for Reading Financial Statements |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
| ….. | …………………………………………………………………………………………………………… | ….  | …………………………………………………………………………………………………….. | …   | ……………………………………………………………………………………….. | …   | ……………………………… | ….  | ………………………….. |

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=4837&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12288&rand=0.703252901024825)