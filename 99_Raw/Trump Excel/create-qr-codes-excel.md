# How to Create QR Codes in Excel (QR Code Generator)

**Source:** https://trumpexcel.com/create-qr-codes-excel

---

[Skip to content](https://trumpexcel.com/create-qr-codes-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/create-qr-codes-excel/#below-title)

I was recently working on a project where I had to create QR codes (Quick Response codes) in bulk in Excel for some of the URLs I had in a column.

I figured out a couple of different ways to do this, and in this article, I’m going to share four methods you can use to quickly create QR codes in Excel.

You can also **[click here to download the QR code generator template](https://www.dropbox.com/s/8tiwuzryh13sk8c/QR%20Code%20Generator%20Excel.xlsm?dl=1)
,** where you can specify the data in column A and then instantly generate the QR codes.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/create-qr-codes-excel/#)

Using the IMAGE Function (for Excel with Microsoft 365)
-------------------------------------------------------

If you’re using Excel with Microsoft 365 (or Excel on the web), the easiest way to create QR codes would be by using the IMAGE function.

IMAGE is a new function that is only available in Excel with Microsoft 365, so if you are using older versions of Excel, you will have to use the other methods covered in this tutorial

Let me show you how to use the IMAGE function to create QR codes.

Below is a data set where I have some URLs in column A for which I want to generate the QR codes in column B.

![Dataset to generate QR codes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20357'%3E%3C/svg%3E)

Here is the formula that will do this:

\=IMAGE("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="&A2)

![Getting QR code in Excel using Formula qr server](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20253'%3E%3C/svg%3E)

Enter this formula in cell B2, and then copy it for all the other cells where you want the QR codes.

_Note: You may see a lag of a few seconds as the IMAGE function tries to access the QR Server URL, generates the QR code, and fetches it back in the cell._

It’s as easy as this!

**Note**: In this example, I’ve shown you how to create QR codes for URLs, but you can do the same thing for any kind of data set, including numbers or text (such as names or addresses)

**How does this work?**

QR server website has this free service where you can generate QR codes by using the URL _https://api.qrserver.com/v1/create-qr-code/?size=150×150&data=**\[Your Text\]**_

You need to use the same URL and replace **\[Your Text\]** with the text or URL for which you want to generate the QR code.

With the IMAGE function, we use this URL to generate the QR code for the data that we have in column A and then fetch that image in the cell.

IMAGE function has the following syntax:

\=IMAGE(source, \[alt\_text\], \[sizing\], \[height\], \[width\])

In the image function, the source argument must be provided, which should be the URL from which you want to fetch the image. The rest of the arguments are optional, so I’ve left them out.

A few things you need to know about this method:

*   The QR code you get from the IMAGE function is embedded within the cell. If you delete the cell, then it will get deleted as well, and if you resize the cell, then it will also get resized with the cell.
*   The size of the QR code to be generated is already mentioned in the URL (100X100). You can change this if you want.
*   Unfortunately, there is no way for you to download this image that the IMAGE function has given to your system.

**Note**: The IMAGE function is also available in Google Sheets, so you can use the same formula in Google Sheets as well

Also read: [Create Barcodes in Excel (Free Barcode Generator)](https://trumpexcel.com/barcodes-excel/)

Using VBA Code to Generate Custom Function
------------------------------------------

If you do not have the IMAGE function in [your Excel version](https://trumpexcel.com/excel-version/)
 and you want to generate QR codes in bulk, the next best thing would be to use a simple VBA code to create your own function to do this.

Below is the VBA code that creates a user-defined function called GETQRCODES, which can be used within a cell, and it would instantly generate the QR code for the given data point.

    'Code by Sumit Bansal from https://trumpexcel.com
    Function GETQRCODES(QrCodeValues As String)
    Dim URL As String
    Dim CellValues As Range
    Set CellValues = Application.Caller
    URL = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" & QrCodeValues
    On Error Resume Next
    ActiveSheet.Pictures("Generated_QR_CODES_" & CellValues.Address(False, False)).Delete
    On Error GoTo 0
    ActiveSheet.Pictures.Insert(URL).Select
    With Selection.ShapeRange(1)
        .Name = "Generated_QR_CODES_" & CellValues.Address(False, False)
        .Left = CellValues.Left + 2
        .Top = CellValues.Top + 2
    End With
    GETQRCODES = ""
    End Function
    

Let me show you how to use this code.

Below is the data set where I have some URLs in column A, and I want to generate the QR codes in column B using the above VBA code.

![Dataset to generate QR codes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20357'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Open the VB editor by clicking the Developer tab and then the Visual Basic icon. You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     ALT + F11 to open the VB editor.

![Click on the Visual Basic icon in the developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20805%20222'%3E%3C/svg%3E)

2.  Click on the Insert option in the menu.
3.  Click on the Module option. This will insert a new module for the workbook where we are going to copy and paste our VBA code.

![Insert a module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20306'%3E%3C/svg%3E)

4.  Copy and paste the above VBA code to the module code window.

![Paste to the VB code in module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20273'%3E%3C/svg%3E)

5.  Go back to the Excel worksheet.
6.  Enter the following formula in cell B2

\=GETQRCODES(A2)

As soon as you enter this formula and hit the enter key, it is going to take a few seconds and then give you the QR code image right there above the cell where you entered the formula. Resize the cell to fit the QR code in the cell.

![QR code inserted using the VBA code function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20630'%3E%3C/svg%3E)

7.  Copy this formula for the other cells in column B to generate the QR codes for the remaining cells.

![Apply the formula to all other cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20576'%3E%3C/svg%3E)

The above VBA code uses a QR Server website API URL ([https://api.qrserver.com/v1/create-qr-code/?size=150×150&data=](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=)
) to create the QR code for each cell.

The custom formula GETQRCODES that we have created returns no value except the QR code image.

**Note**: Unlike the IMAGE function, the QR code image that you get using the VBA code is like a shape/object that floats over your worksheet (and is not embedded into the cell in which the formula is used). So once you have the QR code image, you need to resize the cell and make space so that the QR code can be placed in the cell.

Using Third Party Add-ins
-------------------------

You can also take advantage of some third-party adding that can be used to create QR codes in Excel.

This method is suitable in cases where you only have a few data points for which you want to create the QR code (as you need to create the QR code one by one for each cell).

Below, I have the same data set where I have some URLs in column A, and I want to create the QR codes for them in column B.

![Dataset to generate QR codes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20357'%3E%3C/svg%3E)

Here are the steps to first install and add-in and then use that add-in to create the QR codes:

1.  Click the Developer tab. If you do not see the Developer tab, [click here to read](https://trumpexcel.com/excel-developer-tab/)
     how to get the Developer tab in your Excel ribbon
2.  Click on the Add-ins option. This will open the office add-ins dialog box

![Click on the add ins option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20486%20222'%3E%3C/svg%3E)

3.  Click on the ‘STORE’ options

![Store option in the office add insurance dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20526'%3E%3C/svg%3E)

4.  Enter the term ‘Qr Code’ in the search box and then hit the enter key. This will show you all the add-ins that can be used to make QR codes in Excel.

![Enter QR code in the search bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20429'%3E%3C/svg%3E)

5.  In the list, spot the QR4Office add-in and click on the Add button.

![Click the add button for the QR4 office add in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20614'%3E%3C/svg%3E)

6.  Click on the Continue button in the dialog box that opens. This will install this add-in in your Excel and also open the QR4Office pane on the right side.

![Click the continue button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20348'%3E%3C/svg%3E)

7.  In the ‘Enter the URL/text you’d like to encode:’ drop-down, select the https:// option. You can make the selection based on the data type that you have. In this case, because I have URLs, I have selected the https:// option.

![select the HTTPS option from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20666'%3E%3C/svg%3E)

8.  Copy and paste the URL in the box next to the drop-down.

![Copy paste the URL in the search bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20635'%3E%3C/svg%3E)

9.  \[Optional\] Specify the color, background color, or size of the QR code
10.  Click on Insert

![Click on the insert button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20635'%3E%3C/svg%3E)

The above steps would insert the QR code for the URL in the worksheet.

Once you have the QR code, you can resize the cells and place the QR code in column B.

Now you need to repeat the same process for all the other URLs.

**Note**: One obvious drawback of this method is that you need to generate these QR codes one by one, Which may not be the most efficient method in case you have a lot of URLs.

Also read: [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)

Using External Website
----------------------

If you do not want to add a third party adds into your Excel file, or you do not have permission to do that, another method you can use is by creating QR codes in an external website and then importing them into Excel.

There are many different websites you can use to create QR codes, and the one that I will show you in this tutorial is [QR Code Generator](https://www.qr-code-generator.com/)
.

Just like the add-in method, here also you will have to create these QR codes one by one.

Below I have the same data set where I want to create the QR code for the given URLs in column B.

![Dataset to generate QR codes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20357'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Open a browser and navigate to the URL https://www.qr-code-generator.com/
2.  Return to the Excel sheet and copy the first URL for which you want to generate the QR code.
3.  Return to the QR code generator website, select the URL option, and paste the copied URL in the box. You’ll see that the QR code has instantly been generated and is being shown on the right.

![QR code generated using the website](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20325'%3E%3C/svg%3E)

4.  \[Optional\] Make the customization, such as selecting the frame or changing the shape or color of the QR code

![Customizations to the QR code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20724'%3E%3C/svg%3E)

5.  Click the Download button. This will download the image of the generated QR code on your system.

![Click on the download button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20724'%3E%3C/svg%3E)

6.  Return to Excel, click the Insert tab, then click on the Pictures option, and then click on the ‘This Device’ option.

![Insert picture from this device](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20486%20366'%3E%3C/svg%3E)

7.  In the ‘Insert Picture’ dialog box that opens, locate the file, select it, and then click on the Insert button.
8.  Resize the cells and place the QR code image in the cell in column B.

You need to repeat these steps for all the data points for which you want to generate the QR code and insert the image in Excel.

**Note**: Since you need to create these QR codes one by one, this method is suited when you have a few data points only. In case you have a large data set, it is better to use the VBA method.

_[Click here to download the QR code generator template](https://www.dropbox.com/s/8tiwuzryh13sk8c/QR%20Code%20Generator%20Excel.xlsm?dl=1)
**,** where you can specify the data in column A and then instantly generate the QR codes_

In this article, I’ve shown you four ways you can use to generate QR codes in Excel.

If you are using Excel with Microsoft 365, the best way would be to use the IMAGE function.

In case you do not have access to the IMAGE function and you want to generate these QR codes in bulk, you can use the VBA method.

And in case you want to generate these only for a few cells then you can use the add-in or the external website method.

**Other Excel articles you may also like:**

*   [Quickly Generate Military Alphabet Code for a Word in Excel](https://trumpexcel.com/generate-military-alphabet-code-excel/)
    
*   [How to Insert a Picture in Excel Comment](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [How to do a Picture Lookup in Excel](https://trumpexcel.com/picture-lookup/)
    
*   [How to Insert/Draw a Line in Excel (Straight Line, Arrows, Connectors)](https://trumpexcel.com/draw-line-excel/)
    
*   [How to Create a Heat Map in Excel](https://trumpexcel.com/heat-map-excel/)
    
*   [FREE QR Code Generator](https://trumpexcel.com/tools/qr-code-generator/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Create QR Codes in Excel (QR Code Generator)”
-------------------------------------------------------------------

1.  I apreciate your small UDF to create QR Codes. Thanks alot. Work very well.  
    But I have a question. I tried to convert the UDF into sub procedure but it doesn’t work.  
    When I run the sub procedur then this command got error  
    Set CellValues = Application.Caller –> need object  
    What’s wrong? Thank you
    
    [Reply](https://trumpexcel.com/create-qr-codes-excel/#comment-40844)
    
2.  I also can’t get the Excel formula to work and would really appriceate any help to find the error / resolve it!
    
    [Reply](https://trumpexcel.com/create-qr-codes-excel/#comment-33472)
    
3.  Do you happen to know what happened to the formula for QR codes posted at the top of the document? it is no longer working. Also, I tried using the QR4 code generator in excel, but it keeps giving me the wrong information. Any chance you have time to review?  
    Thank you for this information!
    
    [Reply](https://trumpexcel.com/create-qr-codes-excel/#comment-33331)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/create-qr-codes-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK