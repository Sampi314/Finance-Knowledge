# Create Barcodes in Excel (Free Barcode Generator)

**Source:** https://trumpexcel.com/barcodes-excel

---

[Skip to content](https://trumpexcel.com/barcodes-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/barcodes-excel/#below-title)

Creating barcodes in Excel can be useful for inventory management, product labeling, or any scenario where you need to generate scannable codes directly from your spreadsheet data.

While Excel doesn’t have a built-in barcode generator, this can be done by using the IMAGE function or by installing a barcode form.

In this article, I will show you how to use both of these methods and also create a barcode generator template in Excel.

[**_Click here to download the barcode generator template_**](https://www.dropbox.com/scl/fi/n1mcy9n7ws88g2r3v6sdy/Barcodes-in-Excel.xlsx?rlkey=8coof55ltxe9meabtsjp8psji&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/barcodes-excel/#)

Create Barcode Using IMAGE Function
-----------------------------------

If you’re using Excel with Microsoft 365 or Excel on the web, you would have access to the new image function that makes it very easy to generate barcodes in Excel.

Let me show you how it works.

Below I have a dataset where I have some product codes in column A and I want to generate barcodes for them in column F.

![Dataset to generate barcodes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201752%20412'%3E%3C/svg%3E)

Here is the formula that will do this:

\=IMAGE("https://barcodeapi.org/api/code128/"&A2)

Copy this formula for all the cells in the column. You might have to adjust the row height to make the barcode bigger.

![Barcode is generated in Excel using the image function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201753%201119'%3E%3C/svg%3E)

The above formula uses an external website called barcodeapi.org and generates the barcode on this site. Once the barcode is generated on the website, the IMAGE function fetches the image of the barcode into the cell in Excel.

Let me explain the URL used in the IMAGE function:

*   _https://barcodeapi.org/api/_ – This is the base URL for the BarcodeAPI.org service. It’s the main web address where Excel goes to request a barcode from this particular service.
*   _code128/_ – This specifies the type of barcode we want to generate. Unlike the TEC-IT service that uses a parameter, BarcodeAPI.org includes the barcode type directly in the URL path. In this case, we’re requesting a Code 128 barcode. If you wanted a Code 39 barcode, you’d change this to “code39/”.
*   _&A2_ – This is where we attach the actual data that we want to convert into a barcode. The & symbol joins whatever is in cell A2 to the end of the URL. So if A2 contains “PRD001”, the final URL becomes “https://barcodeapi.org/api/code128/PRD001”.

When Excel computes this formula, it combines all these parts to create a complete URL request, sends it to the barcode service wesbite where the bar code is generated. The IMAGE function then fetches that image into the cell in Excel.

The beauty of this approach is that if you change the value in A2, the barcode will automatically update to reflect the new data.

I believe this is the easiest way to generate barcodes in Excel, but there are a couple of things to keep in mind:

*   This requires you to have an internet connection because the image function contacts an external website.
*   If you’re generating barcodes in bulk, the barcode generation website may have usage limits
*   The generated barcodes are images, so they’ll scale well when printed

If for some reason you are not allowed to open external URLs through your Excel files, you won’t be able to use this method.

In that case, you can see if you’re allowed to install barcode fonts on your system, and then you can generate barcodes without using a formula (as shown in the next method)

Also read: [How to Create QR Codes in Excel (QR Code Generator)](https://trumpexcel.com/create-qr-codes-excel/)

Using Barcode Fonts in Exel (Code 39)
-------------------------------------

In this method, we first need to install a barcode font on our system and then use that to quickly convert text in a cell into a barcode.

### Step 1 – Download and Install the Font

Here are the steps to do this:

1.  Go to the following website and download Code 39 font on your system.

[https://fonts.google.com/specimen/Libre+Barcode+39](https://fonts.google.com/specimen/Libre+Barcode+39)

2.  Open the zip file and double-click on the LibreBarcode39-Regular.ttf file

![Open the Libre Barcode 39 font file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201387%20702'%3E%3C/svg%3E)

3.  In the dialog box that opens, click on the Install button. This will install the font on your system that can now be used in any Microsoft application (including Excel).

![Click on the Install button in the Libre Barcode 39 font dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20910%20611'%3E%3C/svg%3E)

4.  Close all the Excel files that you have open and then restart Excel again.

### Step 2 – Using the Newly Installed Barcode Font

Now let’s use this newly installed barcode font to convert our data into barcode.

Below I have a dataset where I want to convert the text in column A into bar codes and get them in column F.

Here are the steps to do this.

1.  In column F, enter the following formula

\="\*"&A2&"\*"

2.  Select the cell and then go to Home tab and change the font to Libre Barcode 39

![Change the font of the cells that have the barcodes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201759%201058'%3E%3C/svg%3E)

3.  Increase the font size and adjust the row height to make the barcode bigger

![Increase the font of the barcode and change the row height and column width](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202073%201128'%3E%3C/svg%3E)

That’s it! You’re done.

You can now check with any barcode reader machine, and your barcode should be working fine.

A few important things you need to know when using this method:

*   Barcode 39 font only works with uppercase letters. If you have lowercase letters and you use the Barcode39 font, you would still see the barcode but it won’t work with a scanner.
*   If you share this file with someone else who does not have the same barcode font installed, they would just see the regular text.

#### Why add the asterisk (\*) before and after the text?

This is a quirk when using barcode fonts that you need to apply specific encoding to the text for it to be readable by the barcode scanners.

With font barcode 39, you need to have an asterisk before and after the text for it to be recognized as a proper barcode by the scanners.

If you do not add this, while you may get the barcode, it won’t be correct and the scanner might not even read it.

### What about using Barcode 128 Font?

If you want to use barcode font 128, it gets a lot more complicated, as it needs a different kind of encoding.

While with code 39, we were able to add an asterisk before and after the text and make the barcode work, with code 128, you need to have a calculated checksum digit value after the code, which is difficult to calculate and may not always work.

I’ve seen some formulas online that try to calculate this value and append it to the text. I wasn’t able to reliably replicate it in all the cases.

So I recommend you stick with using the IMAGE function when generating a Code 128 barcode, as the encoding is done by the barcode-generating website, and your IMAGE function then fetches the image into the cell.

Generate barcodes quickly in bulk from your browser – check this [free bulk barcode generation tool](https://trumpexcel.com/tools/barcode-generator/)

Which Method Should You Choose?
-------------------------------

**Use the IMAGE Function Method when:**

*   You have Excel 365 or using Excel on the Web
*   Internet connection is available
*   You have the permission to access external URLs from your Excel file.

**Use the Font Method when:**

*   You need to work offline
*   You’re using older Excel versions
*   You want more control over barcode appearance
*   You’re comfortable with barcode formatting requirements (such as adding an asterisk before and after the text)

In this article, I’ve covered how to quickly generate barcodes in Excel using the image function and using a specific barcode font.

I hope you found this article helpful.If you have any questions or suggestions for me, please let me know in the comment section.

**Other Excel articles you may also like:**

*   [How to do a Picture Lookup in Excel](https://trumpexcel.com/picture-lookup/)
    
*   [How to Insert a Picture in Excel Comment](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [How to Insert/Draw a Line in Excel (Straight Line, Arrows, Connectors)](https://trumpexcel.com/draw-line-excel/)
    
*   [How to Create a Heat Map in Excel](https://trumpexcel.com/heat-map-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/barcodes-excel/#respond)

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