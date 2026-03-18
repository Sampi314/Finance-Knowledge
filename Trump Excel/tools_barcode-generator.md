# Free Bulk Barcode Generator (Instant Download)

**Source:** https://trumpexcel.com/tools/barcode-generator

---

[Skip to content](https://trumpexcel.com/tools/barcode-generator/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/tools/barcode-generator/#below-title)

Barcode Generator
-----------------

Generate Code 128, Code 39, EAN-13 & UPC-A barcodes

BARCODE DATA (one value per line for bulk, max 100 lines)

BARCODE TYPE Code 128 Code 39 EAN-13 UPC-A

 Show text below barcode

BAR HEIGHT (PX) 80 

MODULE WIDTH (PX) 2 

Generate Barcodes

Download All as PNG

Made by [TrumpExcel.com](https://trumpexcel.com/)

Free Online Barcode Generator (Upto 100)
----------------------------------------

The barcode generator above lets you create barcodes in four standard formats: Code 128, Code 39, EAN-13, and UPC-A.

Type your data, pick the barcode type, and hit Generate.

Need multiple barcodes?

Enter one value per line and generate them all at once. You can adjust the bar height and width, then download individual barcodes or all of them as a single PNG.

The rest of this page covers which barcode type to pick, how these barcodes actually encode your data, and the mistakes that will make your barcode unscannable.

How to Use This Bulk Barcode Generator
--------------------------------------

1.  **Enter your data** in the text box. For a single barcode, just type the value. For multiple barcodes, enter one value per line (up to 100 at a time).
2.  **Select the barcode type** from the dropdown. Not sure which one? See the comparison table below.
3.  **Adjust the settings.** Use the sliders to change bar height and module width. Check or uncheck "Show text below barcode" based on your label design.
4.  **Click Generate Barcodes.** All barcodes appear instantly. Any invalid entries are flagged with an error message.
5.  **Download.** Each barcode has its own download button. If you generated multiple barcodes, use "Download All as PNG" to get a single image with all of them stacked together.

The barcodes update live when you adjust the sliders or toggle the text option, so you can fine-tune the size without clicking Generate again.

Which Barcode Type Should You Use?
----------------------------------

This is the question most barcode generator pages skip. Here's a quick guide:

| Use Case | Barcode Type | Why |
| --- | --- | --- |
| Selling products in US/Canada retail | **UPC-A** | 12-digit standard required by US retailers and Amazon |
| Selling products internationally | **EAN-13** | 13-digit standard used worldwide outside North America |
| Shipping labels and logistics | **Code 128** | Compact, supports full ASCII, industry standard for shipping |
| Internal inventory and asset tracking | **Code 128** | Most efficient for alphanumeric SKUs and serial numbers |
| Automotive or defense industry | **Code 39** | Legacy standard still required in these industries |
| Simple labels with letters and numbers | **Code 39** | Works with older scanners, no check digit needed |

**One important distinction:** This generator creates valid barcode images, but the numbers are not registered with GS1. For internal use (warehouse labels, asset tags, inventory tracking), that's perfectly fine. But if you're selling products in retail stores or on Amazon, you need a GS1-registered UPC or EAN number first. The GS1 registration is what makes the number unique worldwide. This tool then turns that registered number into a scannable barcode image.

How Barcodes Encode Data
------------------------

Every barcode is just a pattern of black bars and white spaces that represent characters.

The width of each bar and the space is what carries the information.

A scanner reads these widths and converts them back to text or numbers.

Here's how each type works:

### Code 128

Code 128 uses three bars and three spaces per character, with each element having a width of 1 to 4 modules. Every character takes exactly 11 modules. The barcode starts with a START pattern, followed by the encoded data, a calculated check digit, and a STOP pattern.

**Example:** To encode the text "HELLO", the generator:

1.  Starts with the START B pattern (for standard ASCII)
2.  Converts each letter: H=40, E=37, L=44, L=44, O=47 (ASCII code minus 32)
3.  Calculates the checksum: (104 + 40×1 + 37×2 + 44×3 + 44×4 + 47×5) mod 103 = 82
4.  Appends the check character (value 82) and the STOP pattern

The result is a tight barcode that any modern scanner picks up without issues.

### Code 39

Code 39 is simpler. Each character uses 9 elements (5 bars and 4 spaces), where exactly 3 of the 9 are wide. The name "Code 39" comes from the fact that it originally encoded 39 characters (it now encodes 43).

Every Code 39 barcode starts and ends with the asterisk (\*) character, which acts as a start/stop marker. That's why the text below a Code 39 barcode shows something like \*HELLO\*.

### EAN-13 and UPC-A

EAN-13 encodes 13 digits using a fixed structure: a start guard pattern, six left-side digits, a center guard, six right-side digits, and an end guard. The first digit determines the encoding pattern for the left side, which is how all 13 digits fit into just 12 visible digit positions.

UPC-A is actually a subset of EAN-13. Every 12-digit UPC-A code can be converted to a 13-digit EAN-13 by adding a leading zero. This generator handles that conversion automatically.

Both formats include a **check digit**. If you enter 12 digits for EAN-13 (or 11 for UPC-A), the generator calculates and appends the correct check digit. If you enter the full 13 (or 12) digits, it validates your check digit and warns you if it's wrong.

Barcode Types Compared
----------------------

| Feature | Code 128 | Code 39 | EAN-13 | UPC-A |
| --- | --- | --- | --- | --- |
| **Characters** | Full ASCII (letters, numbers, symbols) | A-Z, 0-9, and 7 symbols | Digits only | Digits only |
| **Length** | Variable | Variable | Fixed (13 digits) | Fixed (12 digits) |
| **Check digit** | Yes (automatic) | No  | Yes (automatic) | Yes (automatic) |
| **Density** | High (compact) | Low (takes more space) | Fixed size | Fixed size |
| **Common use** | Shipping, logistics, inventory | Automotive, defense, legacy | International retail | US/Canada retail |

**Code 128 is the best choice for most modern applications**.

It encodes the same data in roughly 30% less space than Code 39, and it supports lowercase letters, numbers, and symbols. Code 39 still has its place in industries that require it, but if you're starting fresh, go with Code 128.

In Case You Have Questions
--------------------------

**What barcode type should I use for Amazon or retail?**  
Amazon and most US retailers require UPC-A barcodes with GS1-registered numbers. You'll need to purchase a GS1 membership (starting around $250/year in the US) to get a legitimate company prefix, then use this generator to create the barcode image from your assigned numbers.

**Can I use these barcodes for commercial products?**  
The barcode images this tool generates are technically valid and scannable. For internal use (inventory, asset tracking, warehouse labels), they work perfectly. For retail sale, the barcode image is only part of it. You also need a GS1-registered number to ensure your product code is globally unique.

**Do barcodes expire?**  
The barcode itself never expires. It's just an image encoding a number. However, your GS1 membership (which makes your number officially registered) requires annual renewal. If your membership lapses, another company could eventually be assigned your prefix.

**Why won't my barcode scan?**  
The most common causes are: the quiet zone (white margin) is too small, the barcode is printed too small, the print quality is poor (smudged or faded bars), or there's not enough contrast between the bars and background. Try increasing the module width in this generator and printing on a clean white label.

**What's the difference between a barcode and a QR code?**  
Traditional barcodes (like the ones this tool generates) are one-dimensional. They encode data in a single row of bars. QR codes are two-dimensional and store data in a grid of squares. QR codes hold much more data (up to 7,089 characters vs. about 100 for 1D barcodes) and can be scanned with any smartphone camera. Use 1D barcodes for products and inventory; use QR codes for URLs, marketing, and situations where you need to encode more information.

**How do I create barcodes in bulk?**  
This generator supports bulk creation. Enter up to 100 values (one per line) and click Generate. Each barcode gets its own download button, and "Download All as PNG" gives you a single image with everything.

If you need more than 100 barcodes in one go, you can use the [Barcode Excel template](https://trumpexcel.com/barcodes-excel/)
 provided here.

**Other Related Tools / Calculators**:

*   [All Free Online Tools](https://trumpexcel.com/tools/)
    
*   [FREE QR Code Generator](https://trumpexcel.com/tools/qr-code-generator/)
    
*   [Random Group / Team Generator](https://trumpexcel.com/tools/random-team-generator/)
    
*   [Free Printable Calendar Generator](https://trumpexcel.com/tools/printable-calendar-generator/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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