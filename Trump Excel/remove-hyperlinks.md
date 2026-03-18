# How to Quickly Remove Hyperlinks from a Worksheet in Excel

**Source:** https://trumpexcel.com/remove-hyperlinks

---

[Skip to content](https://trumpexcel.com/remove-hyperlinks/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-hyperlinks/#below-title)

**Watch Video – How to Remove Hyperlinks in Excel**

I often find it quite frustrating when Excel automatically creates a hyperlink as soon as I insert an email id or a URL in a cell and hit enter.

Now, when I try to select a cell (or double-click on it to get into the edit mode), it automatically opens the link in a new browser window.

Arghhh!

In such cases, there is a need to remove these hyperlinks from the worksheet.

In this tutorial, I will show you 2 methods to remove existing [hyperlinks in a worksheet](https://trumpexcel.com/hyperlinks/)
, and an awesome technique to prevent Excel from creating hyperlinks on its own.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-hyperlinks/#)

Remove Hyperlinks with 2 Clicks
-------------------------------

Suppose you have a dataset where Excel has automatically created hyperlinks in URLs or email ids.

Here are the steps to remove hyperlinks from the selected cells:

1.  Select the data from which you want to remove hyperlinks.
2.  Right-click on any of the selected cell.
3.  Click on the ‘Remove Hyperlink’ option.![Select Remove Hyperlinks option from the right-click menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20472'%3E%3C/svg%3E)

The above steps would instantly remove hyperlinks from the selected cells.

In case you want to remove hyperlinks from the entire worksheet, select all the cells and then follow the above steps.

Also read: [Extract URL from Hyperlinks in Excel](https://trumpexcel.com/extract-url-from-hyperlinks-excel/)

Remove Hyperlinks with VBA
--------------------------

While the above method of removing hyperlinks with 2 clicks is quite easy, you can also use VBA to bring this down to a single click.

But before it becomes a one-click functionality, there is some pre-work that you need to do (as described below).

The below VBA macro code instantly removes all the hyperlinks from the active worksheet.

Sub RemoveAllHyperlinks()
'Code by Sumit Bansal @ [trumpexcel.com](https://trumpexcel.com/)

ActiveSheet.Hyperlinks.Delete
End Sub

Here are the steps to put the VBA code in the backend and enable one-click hyperlink removal:

1.  Copy the above VBA code
2.  Go to the Developer tab.![Developer tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20128'%3E%3C/svg%3E)
3.  Click on Visual Basic.![Remove Hyperlinks in Excel - click on visual basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20129'%3E%3C/svg%3E)
4.  In the VB Editor, right-click on any of the workbook objects.
5.  Go to Insert and click on Module.![Remove Hyperlinks in Excel - insert module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20358'%3E%3C/svg%3E)
6.  In the module, paste the above VBA code.![Remove All Hyperlinks - Paste VBA code in module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20252'%3E%3C/svg%3E)
7.  Close the VB Editor.

The above steps ensure that the VBA code is in the backend and would remove hyperlinks from the entire sheet when it’s run.

Now to further simplify this process, you can add the macro to the Quick Access Toolbar (QAT). This will allow you to remove hyperlinks from the entire worksheet with a single click.

![Remove Hyperlinks in Excel - macro in QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%2077'%3E%3C/svg%3E)

Here are the steps to add the VBA macro to the QAT:

1.  Click on the Customize Quick Access Toolbar icon.![Remove Hyperlinks from a Worksheet in Excel - Add to QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20100'%3E%3C/svg%3E)
2.  Select ‘More Commands’.![More Commands to add macro to QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20403'%3E%3C/svg%3E)
3.  In the Excel Options dialogue box, in the ‘Choose command from’ dialog box, select ‘Macros’.![Remove Hyperlinks from a Worksheet in Excel - Macros in Excel Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20234'%3E%3C/svg%3E)
4.  Click on the Macro that you want to add to the QAT.![Select the macro that you want to add to QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20303'%3E%3C/svg%3E)
5.  Click on the Add button.
6.  Click OK.

The above steps would add the macro to the QAT.

Now to remove all the hyperlinks from the worksheet, all you need to do is click on the macro in the QAT.

If you don’t want to remove all the hyperlinks in a worksheet, but only the ones in the selected range, use the below VBA code:

Sub RemoveHyperlinksfromSelection()
 'Code by Sumit Bansal @ [trumpexcel.com](https://trumpexcel.com/)
 Selection.Hyperlinks.Delete
 End Sub

If you often have the need to remove hyperlinks from a worksheet (or a selected range), it’s a good idea to save this macro in your personal macro workbook.

Here is a detailed guide on how to save a macro in the [personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
.  Once saved in the personal macro workbook, it will be available in all the workbooks on your system.

Also read: [Remove Macros From Excel](https://trumpexcel.com/remove-macros-from-excel/)

Prevent Excel from Creating Hyperlinks Automatically
----------------------------------------------------

So far we have been treating the symptoms.

Now let’s see how to target the root cause of the issue – URLs/Emails automatically getting converted into hyperlinks.

The reason this happens as there is a setting in Excel that automatically converts ‘Internet and network paths’ into hyperlinks.

Here are the steps to disable this setting in Excel:

1.  Go to File.
2.  Click on Options.![Remove Hyperlinks in Excel - Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20284'%3E%3C/svg%3E)
3.  In the Excel Options dialog box, click on ‘Proofing’ in the left pane.![Proofing option in the left pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20254'%3E%3C/svg%3E)
4.  Click on the AutoCorrect Options button.![Remove All Hyperlinks - Autocorrect Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20254'%3E%3C/svg%3E)
5.  In the AutoCorrect dialog box, select the ‘AutoFormat As You Type’ tab.![Select Autoformat as you type tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20183'%3E%3C/svg%3E)
6.  Uncheck the option – ‘Internet and network paths with hyperlinks’![Uncheck Internet and Network Paths with hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20174'%3E%3C/svg%3E)
7.  Click OK.
8.  Close the Excel Options dialog box.

If you’ve completed the following steps, Excel would not automatically turn URLs, email address, and network paths into hyperlinks.

Note that this change is applied to the entire Excel application, and would be applied to all the workbooks that you work with.

**You May Also Like the Following Excel Tutorials:**

*   [How to Quickly Find Hyperlinks in Excel.](https://trumpexcel.com/find-hyperlinks-in-excel/)
    
*   [Create Dynamic Hyperlinks in Excel](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/)
    .
*   [Quickly Create Summary Worksheet with Hyperlinks in Excel](https://trumpexcel.com/create-summary-worksheet-in-excel/)
    .
*   [Useful Excel Macro Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-hyperlinks/#respond)

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