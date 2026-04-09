# FREE QR Code Generator (Single & Bulk)

**Source:** https://trumpexcel.com/tools/qr-code-generator

---

[Skip to content](https://trumpexcel.com/tools/qr-code-generator/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/tools/qr-code-generator/#below-title)

QR Code Generator

Create free QR codes for URLs, WiFi, contacts, and more

URL Text Email Phone SMS WiFi vCard

Bulk mode Generate one QR code

Website URL 

URLs (one per line) Enter up to 50 URLs, one per line. Each generates a separate QR code.

Bulk mode Generate one QR code

Plain Text

Text values (one per line) Enter up to 50 text values, one per line. Useful for voucher codes, serial numbers, or SKUs.

Recipient Email 

Subject (optional) 

Body (optional)

Bulk mode Generate one QR code

Phone Number 

Phone numbers (one per line) Enter up to 50 phone numbers, one per line. Useful for team directories or department listings.

Phone Number 

Message (optional)

Network Name (SSID) 

Password 

Encryption WPA / WPA2 WEP None (Open)

 Hidden network

First Name 

Last Name 

Phone 

Email 

Organization 

Website 

Note (optional) 

Customize

Size

 250 px

Error Correction i How much of the QR code can be damaged or covered and still scan correctly.  
  
**For screen use:** Medium (default).  
**For print or stickers:** Quartile or High.  
**Adding a logo:** Use High. Low (L) — 7% Medium (M) — 15% Quartile (Q) — 25% High (H) — 30%

Foreground

 #000000

Background

 #ffffff

Generate QR Code

  
Download PNG

Download All as ZIP

Made by [trumpexcel.com](https://trumpexcel.com/)

This is a free QR code generator that creates QR codes (downloadable) for seven different content types:

1.  URLs (Single & Bulk)
2.  Plain text (Single & Bulk)
3.  Email addresses
4.  Phone numbers (Single & Bulk)
5.  SMS messages
6.  WiFi networks and
7.  vCards (digital business cards).

No account needed, no watermarks. The code is generated right in your browser, and you can **download it as a PNG** to use anywhere.

Pick your content type, fill in the fields, hit Generate, and download. That’s it.

This tool runs entirely in your browser. Nothing you type is sent to a server, stored in a database, or shared with anyone.  
  
The QR code is generated on your device itself, which means it works even without an internet connection. Close the tab, and everything is gone.

Types of QR Codes This Generator Creates
----------------------------------------

Different use cases need different QR code formats. Here’s what each type does:

### URL

The most common type.

Encodes a web address so scanning it opens the page directly in the phone’s browser. Works with any URL, including ones with tracking parameters.

### Plain Text

Encodes raw text with no special action.

The phone’s scanner displays the text. Useful for short messages, codes, or any information you want to share as-is.

### Email

Opens the phone’s email app with the recipient, subject, and body pre-filled.

The person just hits Send. Great for feedback forms, contact pages, or event sign-up prompts.

### Phone

Triggers a call prompt when scanned. The number appears on the screen and the user taps to dial. Useful on business cards and flyers.

### SMS

Opens the messaging app with a phone number and optional pre-filled message. Handy for any situation where you want people to text a specific number without copying it down.

### WiFi

Shares network credentials without typing. When someone scans it, their phone offers to join the network automatically. If you manage an office or run a cafe, put this one on a printed card.

### vCard

Encodes a full contact entry: name, phone, email, company, and website. Scanning it offers to save the person directly to the phone’s contacts. A QR code on a business card that actually does something.

What Error Correction Means
---------------------------

Error correction is one of those settings most people ignore. It matters more than it looks.

QR codes have four error correction levels:

*   **L (Low):** 7% of the code can be damaged, and it still scans.
*   **M (Medium):** 15% damage tolerance. Good default for most uses.
*   **Q (Quartile):** 25% tolerance. Better for codes on physical materials that might get dirty or worn.
*   **H (High):** 30% tolerance. Useful if you want to overlay a logo on the code without breaking it.

Higher error correction means the QR code has more redundant data, which makes it larger and denser.

For a simple URL on a clean web page, Medium is fine. For a code that’ll be printed on a cardboard box or a t-shirt, use Q or H.

How to Create QR Codes in Excel
-------------------------------

If you need QR codes for a list of URLs or data in a spreadsheet, you don’t have to generate them one by one. Excel has a way to do it in bulk.

**Using the IMAGE function (Microsoft 365 only):**

    =IMAGE("https://quickchart.io/qr?text=" & ENCODEURL(A2))

Put your URLs or text in column A, then enter this formula in column B.

It pulls a QR code image from the QuickChart API and displays it inside the cell. ENCODEURL() handles special characters in the data so the formula doesn’t break.

A few things to know:

*   The IMAGE function requires Microsoft 365 (it’s not available in Excel 2019 or earlier).
*   You need an internet connection each time the file recalculates, since the image loads from an external URL.
*   Resize the row height and column width to make the QR codes large enough to scan.

_Here is a detailed article where you can learn [how to create QR codes in Excel](https://trumpexcel.com/create-qr-codes-excel/)
._

Common Mistakes to Avoid
------------------------

**Using a URL that changes after printing.** If you print a QR code linking to a page and then move that page, the code breaks. Either use a URL shortener (so you can redirect it later) or make sure the destination URL is permanent before printing.

**Making the code too small.** QR codes need to be large enough for phones to scan reliably. The minimum usable size is roughly 2 x 2 cm for a code scanned at arm’s length. On screen, 200px or larger is fine. For print, scale up.

**Using low contrast colors.** Pale grey on white won’t scan. The dark-on-light default exists for a reason. If you want custom colors, test the code with a real phone before you commit to printing anything.

**Skipping the test scan.** Always scan your QR code before distributing it, especially for WiFi and vCard codes. These formats are more sensitive to encoding errors than a simple URL.

**Forgetting the quiet zone.** QR codes need a border of white space around them (called the quiet zone). This generator adds it automatically. If you’re placing the downloaded image into a design, don’t crop it right to the edge of the pattern.

Still Have Questions?
---------------------

**What’s the maximum amount of data a QR code can hold?**  
A QR code can technically store up to around 3,000 characters of text, but in practice, longer codes become denser and harder to scan reliably. Keep it short. URLs and contact details work great; embedding long documents does not.

**Are QR codes free to use?**  
Yes. The QR code standard itself is open. This generator is free, and the codes you download have no license restrictions or watermarks.

**Do QR codes expire?**  
Static QR codes never expire. The data is permanently encoded in the pattern. As long as the destination (like a website) stays live, the code works indefinitely.

**Why won’t my WiFi QR code work on some phones?**  
WiFi QR codes require Android 10+ or iOS 11+ to be recognized automatically by the camera app. Older devices may need a third-party QR scanner app that supports the WiFi format.

**Can I use the same QR code for multiple people?**  
Yes. A QR code is just an image. You can print it, share it digitally, or embed it anywhere. Every scan goes to the same destination.

**Other Related Tools / Calculators**:

*   [All Free Online Tools](https://trumpexcel.com/tools/)
    
*   [Free Bulk Barcode Generator](https://trumpexcel.com/tools/barcode-generator/)
    
*   [Random Group / Team Generator](https://trumpexcel.com/tools/random-team-generator/)
    
*   [Free Printable Calendar Generator (Weekly, Monthly, Yearly)](https://trumpexcel.com/tools/printable-calendar-generator/)
    
*   [Number to Words Converter](https://trumpexcel.com/tools/number-to-words-converter/)
    

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