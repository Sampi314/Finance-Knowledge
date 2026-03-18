# Add Sheet Name to Header or Footer in Excel (Easy Steps)

**Source:** https://trumpexcel.com/add-sheet-name-to-header-footer-excel

---

[Skip to content](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/#below-title)

It’s easy to add sheet names to header or footer in Excel.

Once done, the sheet name will appear In the header or the footer of the page when you print it.

This is especially useful when you’re working with a large workbook and need to [print multiple worksheets](https://trumpexcel.com/print-multiple-sheets-excel/)
. Having the sheet name in the header or footer section allows you to quickly identify which page belongs to which worksheet.

Let’s see how to do this.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/#)

Add Sheet Name to Header or Footer
----------------------------------

Below are the steps to add the sheet name to the header or footer of a specific worksheet:

1.  Open the Excel file and activate the worksheet in which you want to add the sheet name to the header or footer section
2.  Click on the _Page Layout_ tab

![Click the page layout tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20267'%3E%3C/svg%3E)

3.  In the Page Setup group, click on the dialog box launcher (the small tilted arrow at the bottom right edge of the Page Setup group).

![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20224'%3E%3C/svg%3E)

_Pro Tip: You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 **ALT + P + S + P** to open the page setup dialog box_

4.  In the Page Setup dialog box that opens, click on the Header/Footer tab.

![Click on the header footer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20552'%3E%3C/svg%3E)

4.  Click on the Custom Header option or the Custom Footer option depending on where you want to add the sheet name. For this example, I will click on the Custom Header option.

![Click on the custom header or custom footer option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20598'%3E%3C/svg%3E)

4.  In the Header dialog box that opens, place your cursor in the Left, Center, or Right section, depending on where you want the sheet name to appear on the printed sheet.

![Place the cursor in the section where you want the sheet name in the header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20323'%3E%3C/svg%3E)

4.  With the cursor in the right section, click on the _Insert Sheet Name_ icon listed above the sections. Alternatively, you can manually enter **&\[Tab\]**

![Click on sheet name option to get the code for tab name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20323'%3E%3C/svg%3E)

4.  Click OK
5.  Click OK in the Page Setup dialog box.

Now when you print the worksheet, the sheet named will automatically appear in the section where you placed the **&\[Tab\]** code.

In case you want the sheet name in the footer, you can follow the same steps click on the custom footer option in step 5.

You can check the result before printing by opening the print preview (by using the shortcut Control + P). If you’ve added the code in the header or footer, it should appear in the print preview of the worksheet (as shown below):

![Sheet name appears in the print preview in the header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20453'%3E%3C/svg%3E)

_These parts only show up when you print the sheet or use the Print Preview. They don’t appear in the normal view of your spreadsheet. This keeps your work area clean while still adding key details to printed pages._

Note: In this example I selected one specific sheet for which I wanted the name to appear in the header or footer. If you want to apply this to all the worksheets in your workbook, select all the worksheets in one go and then follow the above steps.

If you want to remove the sheet name from the header or footer while printing, follow the exact same steps shown above and remove the code **&\[Tab\]** From the header or footer sections.

### Formatting Sheet Name Code in Header / Footer

Excel allows you to do some basic formatting to the [sheet name](https://trumpexcel.com/get-sheet-name-excel/)
 that you put in the header or footer. For example you can change the font type/size, font color, bold/italicize the sheet name, etc.

You can find the formatting options when you click on the formatting icon in the Header dialog box.

![Formatting option in header or footer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20323'%3E%3C/svg%3E)

This will open the Font dialog box where you can make the changes.

You can also choose to format part of the code that you are putting in the header or photo section.

For example, if I have used **&\[Tab\] – &\[Page\]** to give Me the sheet name followed by the page number, I can only select **&\[Tab\]** and then click on the formatting icon to open the Font dialog box.

Now whatever formatting you apply would only be applied to the sheet name and not the page number part when printed.

Also read: [How to Print the Top Row on Every Page in Excel (Repeat Row/Column Headers)](https://trumpexcel.com/print-top-row-on-every-page-excel/)

Useful Codes To Use With the Sheet Name in Header / Footer
----------------------------------------------------------

While you can only add the sheet name to the header or footer while printing, it would be more useful to have more information such as page numbers or the date.

Below are some useful codes that you can put in the header of the footer section to get this additional information:

| Expected Result | Code |
| --- | --- |
| Sheet Name | &\[Tab\] |
| Sheet Name – Page Number | &\[Tab\] – &\[Page\] |
| Sheet Name – Page Number of Number of Pages | &\[Tab\] – &\[Page\] of &\[Pages\] |
| Sheet Name – Printing Date | &\[Tab\] – &\[Date\] |
| Sheet Name – Printing Time | &\[Tab\] – &\[Time\] |

In this article, I showed you how to insert the sheet name into the header or footer of an Excel workbook. I also covered how to format the sheet name when it’s printed.

**Other Excel articles you may also like:**

*   [How to Print Excel Sheet on One Page (Fit to One Page)](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Print Comments in Excel](https://trumpexcel.com/print-comments-excel/)
    
*   [How to Change Page Orientation in Excel?](https://trumpexcel.com/change-page-orientation-excel/)
    
*   [How to Set the Print Area in Excel Worksheets](https://trumpexcel.com/how-to-set-the-print-area-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/#respond)

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