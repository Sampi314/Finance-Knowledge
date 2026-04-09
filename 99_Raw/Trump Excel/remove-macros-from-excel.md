# How to Remove Macros From an Excel Workbook (3 Easy Ways)

**Source:** https://trumpexcel.com/remove-macros-from-excel

---

[Skip to content](https://trumpexcel.com/remove-macros-from-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-macros-from-excel/#below-title)

Using VBA Macros in Excel can be a huge time saver. You can automate a lot of repetitive tasks and create new functions and functionalities in Excel with simple VBA macro codes.

But in some cases, you may want to remove all the macros from an Excel workbook (or delete specific macros only).

This may be the case when you get a workbook from someone else and you want to make it macro-free, or when you’re sending a file with macros to someone and the receipt doesn’t need these in the workbook.

In this tutorial, I will show you a couple of really simple ways to **remove macros from a workbook in Microsoft Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-macros-from-excel/#)

Remove All Macros by Saving the File in XLSX format
---------------------------------------------------

If you want to get rid of all the macros at once, the easiest way to do this would be to save the existing workbook with the XLSX format.

By design, you can not have any VBA macro code in the XLSX file format. In case you do, it would be removed automatically while saving the Excel file.

With Excel, you can only have the macros in the .XLSM, .XLSB, and the older .XLS formats. When you save the workbook in any other format, the macros are immediately lost.

Suppose you have a file called Example.xlsm (with macros), below are the steps to remove all the macros from this file:

1.  Click the File tab![Click on the File Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20198'%3E%3C/svg%3E)
2.  Click on ‘Save As’ option (it’s ‘Save a Copy’ in new Excel versions)![Click on Save a Copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20542'%3E%3C/svg%3E)
3.  Click on Browse. This will open the Save As dialog box.![Click on Browse](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20659%20574'%3E%3C/svg%3E)
4.  In the Save As dialogue box, enter the name of the file with which you want to save it. You can also keep the existing name if you want![Enter the name of the file from which you want to remove the macros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20525'%3E%3C/svg%3E)
5.  Click on the Save As type drop-down
6.  Select the Excel Workbook (\*.xlsx) option![Select XLSX as the Save as Type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20657'%3E%3C/svg%3E)
7.  Click on Save
8.  In the prompt that appears, click on Yes. It’s just informing you that the VB Code will be lost if you save this file in the .XLSX format.![Click on Yes in the VB Prompt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20706%20227'%3E%3C/svg%3E)

That’s it! Your file is now macro-free.

This method is great as it removes all the macros from the current Excel workbook in one go. However, if you want to remove some macros and delete some, this method will not work for you (see the one using the Macro dialog box for this).

Another good thing about this method is that you still have a copy of the original file that has all the macros (in case you need it in the future).

Also read: [How to Remove Hyperlink in Excel](https://trumpexcel.com/remove-hyperlinks/)

Remove Specific Macros from the Macro dialog box
------------------------------------------------

While the previous method would delete all the macros. this one allows you to choose the ones that you want to be removed.

And in case you want to delete all the macros, you can do that as well.

Suppose you have a file called Example.xlsm that has some macros.

Below are the steps to delete a macro from this workbook:

1.  Click the Developer tab (in case you don’t see the Developer tab, see the note in yellow after the steps)![Click on the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20158'%3E%3C/svg%3E)
2.  Click on the Macros button. This will open the Macro dialogue box where you can see all the macros in the workbook![Click on Macros option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20158'%3E%3C/svg%3E)
3.  In the ‘Macros in’ drop-down, make sure ‘This Workbook’ is selected.![Select This Workbook in macros in option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20471'%3E%3C/svg%3E)
4.  Select the macro name that you want to delete from the macro list![Select the macro to delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20471'%3E%3C/svg%3E)
5.  Click on the Delete button. This will delete that selected macro![click on the delete button to remove the selected macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20471'%3E%3C/svg%3E)

If you want to remove multiple (or all) macros, repeat steps 4 and 5.

Note: In case you don’t see the developer tab, [click here to read](https://trumpexcel.com/excel-developer-tab/)
 on how to get the developer tab to show up in the ribbon in Excel. Alternatively, you can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 – ALT + 8 to open the Macro dialog box.

_Alternatively, you can also click on the Views tab, click on the Macros drop-down and then click on View Macros option. This will also open the Macros dialog box._

While this method works great, it would only allow you to remove macros that are stored in a module in the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
. In case you have event macros (in specific worksheets or ThisWorkbook) or macros in the [personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
, those can not be removed with this method.

Also read: [How to Remove Add-Ins in Excel](https://trumpexcel.com/remove-add-ins-excel/)

Remove the Module that has the Macro
------------------------------------

Another way to remove macros is to go to the Visual Basic Editor and remove macros from there.

This method gives you the most control as you can access all the macros (be it in the module or objects or personal macro workbook).

Below are the steps to delete a macro from the Visual Basic Editor:

1.  Click on the Developer tab in the ribbon![Click on the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20158'%3E%3C/svg%3E)
2.  Click on Visual Basic option (or use the keyboard shortcut – ALT + F11)![Click on Visual basic button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20158'%3E%3C/svg%3E)
3.  In the VB Editor, you will have all the workbook objects in the Project Explorer. If you don’t see the Project Explorer, click on the View option in the menu and then click on Project Explorer![Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20389%20327'%3E%3C/svg%3E)
4.  In the Project Explorer, double click on the object that has the macro code. This could be a module, a [worksheet object](https://trumpexcel.com/vba-worksheets/)
    , or [ThisWorkbook](https://trumpexcel.com/vba-workbook/)
    .![Double click on the module which has the code to delete](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20389%20327'%3E%3C/svg%3E)
5.  In the code window that opens, delete the macros you want to remove. If you want to remove all, just select everything and hit the delete key.

In case you have a module that has the code that you want to remove, you can right-click on the module object and then click on Remove module option.

![Remove Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20582'%3E%3C/svg%3E)

So these are three ways you can use to remove macros from a Microsoft Excel workbook.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to Assign a Macro to a Button in Excel](https://trumpexcel.com/assign-macro-to-button-in-excel/)
    
*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    
*   [Useful Excel Macro Examples for VBA Beginners (Ready-to-use)](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    
*   [How to Enable Macros in Excel?](https://trumpexcel.com/enable-macros-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Remove Macros From an Excel Workbook (3 Easy Ways)”
-------------------------------------------------------------------------

1.  Thanks Sir,  
    learn the lot of things from you website and you tube channel
    
    [Reply](https://trumpexcel.com/remove-macros-from-excel/#comment-47193)
    
    *   Thank you Ramesh… Glad you are finding the videos and the articles helpful.
        
        [Reply](https://trumpexcel.com/remove-macros-from-excel/#comment-47451)
        
2.  Hi, I’m not sure if you handle my type of inquiry.  
    Recently my Norton AV quarantined all my Excel spreadsheets claiming that they were infected with something called “XLS:Nastya \[Trj\]”. Those spreadsheets contain important, for me, information gathered for very long time. Norton indicates that these files should be removed (deleted) from the computer. Needless to say that’s not an option for me to consider. Would you happen to have any ideas how this situation can be rectified?
    
    Than you for your attention.  
    Richard
    
    [Reply](https://trumpexcel.com/remove-macros-from-excel/#comment-41607)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-macros-from-excel/#respond)

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