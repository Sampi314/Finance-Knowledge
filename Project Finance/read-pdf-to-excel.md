# Read PDF to Excel

**Source:** https://edbodmer.com/read-pdf-to-excel

---

This page describes a file that can be used to convert many PDF files to Excel (unlike other programs, it is free.) To convert a PDF file into  excel you have to have open the excel file named read pdf to excel that has various macros.  The read PDF to excel macro sets deal with different types of problems that can arise when copying from PDF to Excel using alternative macros. Unlike other PDF to excel programs that you can purchase, all of the macros are provided on an open source basis and of course there is no charge. The conversions from PDF to Excel are geared to financial modelling applications. When using the PDF tool, copy and paste special as unicode text. Also the the read PDF file is geared for efficiently working with financial statements where you do not have to download a PDF file, but you can take it directly from the internet. When you run the read pdf to excel program, it does not work perfectly every time because of the vagaries in the way data comes into excel from pdf programs.  I think I have been able to solve very many of the practical programs, but not every one.  If you are having problems, please do not hesitate to send me an e-mail at edwardbodmer@gmail.com.  [An example of a more complex example is included at on a subsequent page. https://edbodmer.com/complex-a-z-example/](https://edbodmer.com/complex-a-z-example/)
 If you want to try this, click on the button below and then download the file.  Make sure that the status bar at the bottom of your excel file has the Shift, CNTL A instructions.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

**[Asian Version of Excel File the Reads PDF (or Internet) to Excel with Macros that are Implemented with SHIFT CNTL Afor](https://edbodmer.com/wp-content/uploads/2018/10/Read-PDF-to-Excel-Asian.xlsm)
**

**[File with Macros that Format Data Copied into and Excel File from the U.S.Securities and Exchange Website](https://edbodmer.com/wp-content/uploads/2019/04/Scenario-Reporter.xlsm)
**

The discussion below walks through different problems and issues that arise when pasting data from a PDF file to and Excel file.

The first case is the most common situation where the PDF file is compressed into rows of data with multiple values. The data appear in excel without separation into different columns.

The second case is the situation where each piece of data is in a separate row. In this case there is one data value and the data is not compressed into a single column.

The third situation describes correcting the situation where data has an elegant European format with spaces instead of commas and a comma instead of decimals.

Other issues are addressed include fixing titles after you have re-formatted the data.

Basic Read PDF to Excel – Multiple Data and Words Compressed into One Column for Each Line
------------------------------------------------------------------------------------------

The fundamental process for the read PDF to excel file is to have the read\_pdf\_to\_excel.xls file open and make sure to enable macros.  Then, with the file open you copy and paste data from a PDF file to your blank excel sheet (best into cell A1).  After the data is there, you press SHIFT, CNTL, A. Normally, the data should be re-formatted and you should be happy.

Converting PDF to Excel does depend on the type of format that appears in excel from copying the pdf file; whether the pdf file is locked; and, whether the copying is directly from the internet or from a downloaded file that is read into acrobat. The normal case is when the copied data is in a single un-formatted column (maybe 80%-90% of the time).  An example of a pdf file with the normal format can be found in the pdf file below (go to page 17 and copy the financial summary to a blank excel sheet somewhere).

**[Example PDF file with Normal Conversion Format (Sun Edison 2013 Report -- Numbers on Page 17 or F1)](https://edbodmer.com/wp-content/uploads/2018/07/2013-ANNUAL-REPORT-FINAL.pdf)
**

In this case the PDF can be copied into excel and the macro in the the macro can be easily implemented. The process works in situations where the data is copied directly from a file opened in the internet (although not with Microsoft’s horrible explorer) or whether the file is downloaded and then read into acrobat. An example of what happens when you copy from the pdf to excel in this typical case is show below:

![PDF Example 5.PNG](https://edbodmer.wikispaces.com/file/view/PDF%20Example%205.PNG/536810198/482x205/PDF%20Example%205.PNG "PDF Example 5.PNG")

In this typical case the macro in the PDF\_to\_Excel file below can be run. I am being repetitive, but you press SHIFT CNTL A from the sheet with the raw data.  After you press Shift, CNTL, A a menu like the one shown on the screenshot below should appear.  Just press the top green button.

.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PFD-Sheet.jpg)

.

Pressing the top green button should be done whether the pdf is copied directly from the internet or whether the file is downloaded and then read into acrobat. The result is illustrated below:

.

![CapturePDF Example 2.PNG](https://edbodmer.wikispaces.com/file/view/CapturePDF%20Example%202.PNG/536697742/354x284/CapturePDF%20Example%202.PNG "CapturePDF Example 2.PNG")

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

**[Link to My Youtube Channel Where You Can Look At All of the Different Videos that I have Made](https://www.youtube.com/channel/UC2g_Ih-lK1sa3L_1xHacA8w)
**

Cleaning Up PDF Data in Excel When each Data Item is in a Separate Row in a Single Column
-----------------------------------------------------------------------------------------

Sometimes when you copy data into excel it appears in a format where each data item is in a separate row as shown in the screenshot below. As long as the number of rows are consistent, then the copied data can be cleaned up.  You can do this by pressing the second rather than the first green button after you press the Shift, CNTL, A sequence.

Note that after you run the read pdf program using this method, the data is transposed from rows to columns.

![PDF Example 3.PNG](https://edbodmer.wikispaces.com/file/view/PDF%20Example%203.PNG/536698028/272x423/PDF%20Example%203.PNG "PDF Example 3.PNG")

In this case the pdf must be downloaded and then read from acrobat. After copying the data into WORD and then copying the word table into excel, the result is illustrated below:

![PDF Example 4.PNG](https://edbodmer.wikispaces.com/file/view/PDF%20Example%204.PNG/536804812/444x192/PDF%20Example%204.PNG "PDF Example 4.PNG")

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

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=774&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10008&rand=0.2586745103374978)