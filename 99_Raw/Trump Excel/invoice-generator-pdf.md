# [FREE Invoice Generator Template] Save Excel Invoice as PDF

**Source:** https://trumpexcel.com/invoice-generator-pdf

---

[Skip to content](https://trumpexcel.com/invoice-generator-pdf/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/invoice-generator-pdf/#below-title)

I recently had to get myself registered under Goods and Services Tax (GST) so that I can file for GST on my earnings.

Once you have a GST number, you need to file your tax return every month (in India).

So every month, my Charted Accountant would reach out to me asking for sales invoices so that he can file for the GST.

In my case, there only a handful of invoices to be created, as I have only a few sources of income.

However, since this is additional work, I wanted to get this done as quickly as possible.

So to minimize my effort, I created an Invoice Generator template in Excel that allows me to have all the data in one place, and then it automatically creates PDF invoices for all the data points.

As you can see below, **all I need to do is double-click on the client’s name** (in column B), and it would instantly create and save the invoice in the PDF format in the specified folder.

![Creating Invoice Generator Template in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20876'%3E%3C/svg%3E)

You can also modify the invoice template to suit your company’s format (which would require you to change the VBA code a little – explained below).

It creates an invoice as shown below:

![GST Invoice format in PDF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20649%20601'%3E%3C/svg%3E)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/invoice-generator-pdf/#)

How does this Invoice Generator Template Works?
-----------------------------------------------

In this invoice template, there are two worksheets:

1.  _Details_ – This is where you need to specify the details of the sale/transaction. To keep everything together, I have created one row for each record. All the details of a transaction are recorded in the row.
2.  _Invoice Template_ – This is a placeholder template of the invoice where some fields are left empty.  I need to generate a separate invoice for all the sale records and the details for each invoice is picked up from the Details worksheet.

I also have a folder on my desktop with the name ‘Invoice PDFs’. This is the folder where the newly created PDF invoices are saved.

Now let’s see how this works:

**You need to double-click on the client’s name (highlighted in orange in the Details sheet)**.

That’s it!

When you double-click on the client name, it kickstarts the VBA magic in the back end and the following things happen:

1.  Details for the client and the sale transaction are picked up and the invoice template sheet is populated with these details.
2.  A new workbook is created that has the details of the selected client (on which you double-clicked).
3.  This workbook is saved as a PDF in the Invoice PDF folder.
4.  The new workbook is closed without saving.

In case there are any changes in the invoice details, you can double-click on the client name again, and a new invoice will be created (and this will overwrite the old one).

Note that the names of the invoices are based on the month and the invoice number.

For example, an invoice with the date **15-04-2019** and the invoice number as **1** would be saved with the name  **April 2019\_1.pdf**. This helps in keeping track of the invoices in case you have too many.

You can download the Invoice Generator Template by clicking on the button below:

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/o7ilh7kwa7r3bzm/Invoice-Template.xlsm?dl=1)

Modifying the Invoice Generator Template
----------------------------------------

I created this invoice template with a format that I needed for my GST filings.

If you need a different format, you’ll have to edit the template and then adjust the backend VBA code.

Let me first show you the code and explain how it works:

Sub CreateInvoice(RowNum As Integer)
Application.ScreenUpdating = False
Dim wb As Workbook
Dim sh As Worksheet
With shInvoiceTemplate
.Range("D10") = shDetails.Range("A" & RowNum)
.Range("D11") = shDetails.Range("B" & RowNum)
.Range("D12") = shDetails.Range("C" & RowNum)
.Range("B15") = shDetails.Range("D" & RowNum)
.Range("D15") = shDetails.Range("F" & RowNum)
.Range("D16") = shDetails.Range("G" & RowNum)
.Range("D18") = shDetails.Range("E" & RowNum)
End With
FPath = "C:\\Users\\sumit\\Desktop\\Invoice PDFs"
Fname = Format(shInvoiceTemplate.Range("D10"), "mmmm yyyy") \_
& "\_" & shInvoiceTemplate.Range("D12")
shInvoiceTemplate.Copy
ActiveSheet.Name = "InvTemp"
Set wb = ActiveWorkbook
Set sh = ActiveSheet
sh.ExportAsFixedFormat Type:=xlTypePDF, Filename:= \_
FPath & "\\" & Fname, Quality:=xlQualityStandard, IncludeDocProperties:=True, \_
IgnorePrintAreas:=False, OpenAfterPublish:=False
wb.Close SaveChanges:=False
ThisWorkbook.Activate
Application.ScreenUpdating = True
End Sub

The above code is what copies the details of a transaction, fills the invoice placeholder template with those details, creates a new workbook, and save the new workbook as a PDF in the specified folder.

If you have a different template or a different folder location, you need to modify the below-highlighted parts of the code:

![GST Invoice Generator Template in Excel 2018 modifying the code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20546'%3E%3C/svg%3E)

1.  The first highlighted section is what takes the details from the Details sheet and populates the invoice template. If you decide to modify the invoice template, you need to make sure you are picking the right details by modifying this part of the code.
2.  This line specifies the folder location. In my case, it was a folder on my Desktop. You can specify the address of the folder where you want the invoices to be saved.

Note that I have renamed the worksheet code name to ‘shDetails’. I have done this so that I can use the name – shDetails – in my code and it would continue to work even if you change the name of the sheets in the worksheet.

If you want to learn more about the sheet name and the code name, [have a look at this](https://trumpexcel.com/vba-worksheets/)
 (check out the section on using the Worksheet code name).

### **Where is the code in the workbook?**

The code is placed in the back-end of the Excel workbook in a module.

To access the code, follow the below steps:

1.  Click the Developer tab.
2.  Click the Visual Basic option. This will open the VB Editor window.
3.  In the Visual Basic editor, double-click on the Module to open its code window. You’ll find the code mentioned above.![GST Invoice Generator Template in Excel code in the module window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20379'%3E%3C/svg%3E)

In case you’re creating a template yourself, you may not find the Module in a new workbook. You need to right-click on any of the workbook objects, go to Insert, and then click on Module. This will insert a new module. ![Insert a new module in VB Editor Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20405'%3E%3C/svg%3E)

Making the Double-click functionality to Work
---------------------------------------------

The above code does all the heavy lifting, but you need to connect it to the [double-click event](https://trumpexcel.com/vba-events/)
.

This means that the above VBA macro code needs to run whenever someone double-clicks on the filled cells in the client name column.

This can be done by inserting the following code in the worksheet code window:

Private Sub Worksheet\_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
If Target.Cells <> "" And Target.Column = 2 Then
Cancel = True
Call CreateInvoice(Target.Row)
End If
End Sub

Here are the steps to insert this code in the worksheet backend:

*   Right-click on the ‘Details’ worksheet tab
*   Click on the ‘View Code’ option.![GST Invoice Generator Template in Excel 2018 click on view code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20336'%3E%3C/svg%3E)
*   Copy and paste the above code into the code window that appears.![Invoice Generator Template in Excel 2018 double click code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20162'%3E%3C/svg%3E)

The above code does the following things:

1.  Checks if the cell that has been double-clicked has the client details or not. It uses the [IF statement](https://trumpexcel.com/if-then-else-vba/)
     to check and [run the code](https://trumpexcel.com/run-a-macro-excel/)
     only if the cell is not empty and in Column B.
2.  If both the specified criteria are met, it disables double-click functionality (which is to get into the edit mode) and calls the ‘CreateInvoice’ subroutine, which is stored in the Module. It also passes the row number value to the subroutine. For example, if I double-click on the client name in the third row, it will pass 3 as the value to the CreateInvoice subroutine.
3.  Once the ‘CreateInvoice’ subroutine is executed – which creates the PDF of the invoice – it ends.

[**Click here to download the Invoice Generator Template file**](https://www.dropbox.com/s/o7ilh7kwa7r3bzm/Invoice-Template.xlsm?dl=1)
.

Saving the Invoice Template as Excel (instead of PDF)
-----------------------------------------------------

If you want to save the invoice templates as Excel files and not as PDFs, you can use the below code instead:

Sub CreateInvoice(RowNum As Integer)
Application.ScreenUpdating = False
Dim wb As Workbook
Dim sh As Worksheet
With shInvoiceTemplate
.Range("D10") = shDetails.Range("A" & RowNum)
.Range("D11") = shDetails.Range("B" & RowNum)
.Range("D12") = shDetails.Range("C" & RowNum)
.Range("B15") = shDetails.Range("D" & RowNum)
.Range("D15") = shDetails.Range("F" & RowNum)
.Range("D16") = shDetails.Range("G" & RowNum)
.Range("D18") = shDetails.Range("E" & RowNum)
End With
FPath = "C:\\Users\\sumit\\Desktop\\Invoice PDFs"
Fname = Format(shInvoiceTemplate.Range("D10"), "mmmm yyyy") \_
& "\_" & shInvoiceTemplate.Range("D12")
shInvoiceTemplate.Copy
ActiveSheet.Name = "InvTemp"
Set wb = ActiveWorkbook
Set sh = ActiveSheet
sh.Name = Fname
wb.SaveAs Filename:=FPath & "\\" & Fname
wb.Close SaveChanges:=False
ThisWorkbook.Activate
Application.ScreenUpdating = True
End Sub

The above code saves the invoice as an Excel workbook with the same naming convention. The worksheet in the workbook that contains the filled invoice in each saved workbook is also named the same.

**You May Also Like the Following Excel Tutorials Useful:**

*   [How to Convert Excel to PDF Using VBA](https://trumpexcel.com/convert-excel-to-pdf/)
    .
*   [Embed PDF in Excel](https://trumpexcel.com/embed-pdf-file-excel/)
    .
*   [Extract Data From PDF to Excel with this Converter.](https://trumpexcel.com/pdf-to-excel/)
    
*   [Excel Timesheet Calculator Template.](https://trumpexcel.com/excel-timesheet-calculator-template/)
    
*   [Excel Leave Tracker Template.](https://trumpexcel.com/excel-leave-tracker/)
    
*   [Free Excel Templates](https://trumpexcel.com/free-excel-templates/)
    
*   [Loan Amortization Schedule in Excel (Free Template)](https://trumpexcel.com/loan-ammortization-schedule-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “\[FREE Invoice Generator Template\] Save Excel Invoice as PDF”
------------------------------------------------------------------------------

1.  sir i want to extend excel file name charters please help
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-33468)
    
2.  Hi
    
    how insert figures in template, if we need insert different signature in template.
    
    also instead of clicking each cell, how loop clicks so we do not have to click each cell manually for generating PDFs
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-16012)
    
3.  Hi Sumit  
    I am trying to create an employment contract out of the excel data. How do i do that rather than an invoice.
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-14285)
    
4.  Can you creat something for me, as per my requirements, if i explain to you,  
    i can pay you for this,
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-13467)
    
5.  I like the Invoice, easy to use. Thanks
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-13067)
    
6.  HI do this work for online sellers to prepare their invoices
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-13015)
    
7.  Error 1004 in Office 2019:  
    sh.ExportAsFixedFormat Type:=xlTypePDF, Filename:= \_  
    FPath & “” & Fname, Quality:=xlQualityStandard, IncludeDocProperties:=True, \_  
    IgnorePrintAreas:=False, OpenAfterPublish:=False
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-13001)
    
8.  Great generator! Thank you!
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-12838)
    
9.  Do I have to download VB for coding
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-12200)
    
10.  How to add CGST and SGST instead of IGST
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11975)
    
11.  Runtime error 1004 when double clicked.
    
    Debug – sh.ExportAsFixedFormat Type:=xlTypePDF, Filename:= \_  
    FPath & “” & Fname, Quality:=xlQualityStandard, IncludeDocProperties:=True, \_  
    IgnorePrintAreas:=False, OpenAfterPublish:=False
    
    I have no faintest clue what is the above… LOLz  
    Really nice job btw.
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11955)
    
12.  Very use full
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11872)
    
13.  Thank you for the good tip.  
    Could you please advise me regarding below topic.  
    I would like to have several products in one invoice. which part of the code should I change?
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11558)
    
14.  Unable to download the file. Seems corrupted. Please help us for downloading the file.
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11497)
    
    *   I have sorted the issue. You can download it now
        
        [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11500)
        
15.  {Free invoice generator template save excel invoice as pdf }Many time try to download file but file download error
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11473)
    
    *   I have sorted the issue. You can download it now
        
        [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-11499)
        
16.  I like the Invoice a lot, easy to use. Thanks
    
    [Reply](https://trumpexcel.com/invoice-generator-pdf/#comment-10889)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/invoice-generator-pdf/#respond)

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