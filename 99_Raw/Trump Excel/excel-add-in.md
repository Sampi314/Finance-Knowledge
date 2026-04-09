# How to Create and Use an Excel Add-in (Step-by-Step Tutorial)

**Source:** https://trumpexcel.com/excel-add-in

---

[Skip to content](https://trumpexcel.com/excel-add-in/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-add-in/#below-title)

An Excel add-in can be really useful when you have to [run a macro](https://trumpexcel.com/run-a-macro-excel/)
 often in different workbooks.

For example, suppose you want to highlight all the cells that have an error in it, you can easily create an Excel add-in that will highlight errors with a click of a button.

Something as shown below (the macro has been added to the Quick Access Toolbar to run it with a single click):

![Create an Excel Add-in - Demo](https://trumpexcel.com/wp-content/uploads/2016/03/Create-an-Excel-Add-in-Demo.gif)

Similarly, you may want to [create a custom Excel function](https://trumpexcel.com/user-defined-function-vba/)
 and use it in all the Excel workbooks, instead of copy pasting the code again and again.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-add-in/#)

Creating an Excel Add-in
------------------------

In this tutorial, you’ll learn how to create an Excel add-in. There are three steps to create an add-in and make it available in the QAT.

*   Write/Record the code in a module.
*   Save as an Excel Add-in.
*   Add the macro to the Quick Access Toolbar.

### Write/Record the Code in a Module

In this example, we will use a simple code to highlight all the cells that have error values:

Sub HighlightErrors()
 Selection.SpecialCells(xlCellTypeFormulas, xlErrors).Select
 Selection.Interior.Color = vbRed
End Sub

If you are writing code (or copy-pasting it from somewhere), here are steps:

*   Open an Excel Workbook.
*   Press Alt + F11 to open the VB Editor Window.
*   In the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    , you would see the workbook objects listed in the project explorer. If you can’t see that, go to View –> Project Explorer.![Create an Excel Add-in - Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20267'%3E%3C/svg%3E)
*   Right-click on any of the objects in the workbook. Go to Insert option and click on ‘Module’. This will insert a module object.![Create an Excel Add-in - Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20415'%3E%3C/svg%3E)
*   Double-click on the module and enter the above code (copy-paste it).![Create an Excel Add-in - Macro Code in Module Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20156'%3E%3C/svg%3E)
*   Press Alt+F11 to go back to the Excel Worksheet.

_**Note:** If you are [recording a macro](https://trumpexcel.com/record-macro-vba/)
, Excel automatically takes care_ of _inserting a module and putting the code in it._

Now let’s go ahead and create an add-in out of this code.

Also read: [How to Create QR Codes in Excel (QR Code Generator)](https://trumpexcel.com/create-qr-codes-excel/)

### Save and Install the Add-in

Follow the below steps when you are in the workbook where you have inserted the code.

*   Click the File tab.
*   Click on ‘Save As’.![Create an Excel Add-in - Save as](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20284'%3E%3C/svg%3E)
*   In the Save As dialogue box, change the ‘Save as’ type to .xlam. The name you assign to the file would be the name of your add-in. In this example, the file is saved with the name Highlight Errors.
    *   You’ll notice that the path of the file where it gets saved automatically changes. You can use the default one or change it if you want.![Create an Excel Add-in - Save as drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20515'%3E%3C/svg%3E)
*   Open an Excel workbook and Go to Developer –> Add-ins –> Excel Add-ins.![Create an Excel Add-in - add-in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20133'%3E%3C/svg%3E)
*   In the Add-ins dialogue box, browse and locate the file that you saved, and click OK.![Create an Excel Add-in - browse add-in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20407'%3E%3C/svg%3E)

Now the add-in has been activated.

_You may not see any tab or option appear in the ribbon, but the add-in gets activated at this stage and the code is available to be used now._

The next step is to add the macro to the Quick Access Toolbar so that you can run the macro with a single click.

**Note**: If you are creating an add-in that has a custom function, then you don’t need to go to step 3. By the end of step 2, you’ll have the function available in all the workbooks. Step 3 is for such codes where you want something to happen when you run the code (such as highlight cells with errors).

Also read: [How to Remove (Disable) Add-Ins in Excel?](https://trumpexcel.com/remove-add-ins-excel/)

### Adding Add-in to Quick Access Toolbar

To do this:

*   Right-click on any of the ribbon tabs and select Customize Quick Access Toolbar.![Create an Excel Add-in - Customize Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20351%20125'%3E%3C/svg%3E)
*   In the Excel Options dialog box, Select Macros from the Choose commands from the drop-down. You’ll notice that the macro ‘HighlightErrors’ is listed there.![Create an Excel Add-in - qat macro select](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20381'%3E%3C/svg%3E)
*   Click on the ‘HighlightErrors’ Macro and click on Add. This will add the macro to the list on the right.![Create an Excel Add-in - Add to QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20354'%3E%3C/svg%3E)
*   Click OK. This will add the macro to the Quick Access Toolbar.![Create an Excel Add-in - Macro Icon in QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%2087'%3E%3C/svg%3E)

Now, to run this code in any workbook, select the dataset and click on the macro icon in the QAT.

![Create an Excel Add-in - Demo](https://trumpexcel.com/wp-content/uploads/2016/03/Create-an-Excel-Add-in-Demo.gif)

This will highlight all the cells with errors in red color. You can also use this macro in any workbook since you have enabled the add-in.

**Caution**: The changes done by the macro can’t be undone using Control + Z.

You can also create custom functions and then save it as an Excel add-in. Now, when you enable the add-in, the custom functions will be available in all your Excel workbooks.

**You May Also Like the Following Excel Tutorials:**

*   [Working with Cells and Ranges in Excel VBA](https://trumpexcel.com/vba-ranges/)
    .
*   [Working with Worksheets in VBA](https://trumpexcel.com/vba-worksheets/)
    .
*   [Working with Workbooks in VBA](https://trumpexcel.com/vba-workbook/)
    .
*   [Using Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .
*   [Using IF Then Else Statement in Excel VBA](https://trumpexcel.com/if-then-else-vba/)
    .
*   [How to Create and Use Personal Macro Workbook in Excel](https://trumpexcel.com/personal-macro-workbook/)
    .
*   [Useful Excel Macro Code Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [Using For Next Loop in Excel VBA.](https://trumpexcel.com/for-next-loop-excel-vba/)
    
*   [Excel VBA Events – An Easy (and Complete) Guide.](https://trumpexcel.com/vba-events/)
    
*   [Excel VBA Error Handling](https://trumpexcel.com/vba-error-handling/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “How to Create and Use an Excel Add-in”
------------------------------------------------------

1.  I did all but my macro didn’t show in the macro list to be added to the QAT. I looked up and one site said macros in add-ins don’t show in macro list! Now what?
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-14699)
    
2.  I am intrigued by the idea of the add in… but how is this different than putting vba code in a personal macro workbook?
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-14341)
    
3.  I want the code in my add-in to run when I double-click any cell on any sheet. How do I capture that event in an add-in without requiring the user to add VBA to their own Workbook module?
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-14085)
    
4.  Sumit,
    
    This is very good. It was just what I needed. Thanks.
    
    When I was searching for information on creating add-in modules, I did see couple of links to your website, but I was put off by the name. The orange asshole in the White House is so repulsive that I cannot stand to even see that name. I checked out every other link and only came back here because none of the others were any good.
    
    I may not be the only one who has this reaction. If you change the name of your site, you may get more traffic. How about something like Excel-Step-by-Step or ExcelUnraveled or ExcelYourWay or Excel4Everyone or EasyExcel or ExcelGuide?
    
    Anything but the name of that horrible monster.
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-14055)
    
    *   I was excited to read your posting. I even made a Facebook page called “I hate Trump Because He \_\_\_\_\_\_\_\_\_\_”. Nobody will ever tell me what he did. Do you know what he did? I’ve been searching for (4) years now. Twitter me: @chernipeski if you know something.
        
        [Reply](https://trumpexcel.com/excel-add-in/#comment-14086)
        
5.  Thanks
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-13555)
    
6.  Hi sir i want to vba add-in compare two sheets if i have id no list sheet 1 ans sheet 2 also have same id but not same cell serch that id then check all data like name possition etc..if there is any speling mistek or any another typing mistake highlight both sheets…its possibul sir..please can u help me..
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-12819)
    
7.  Is it possible to have the ‘ADD-IN’ as a macro button (for end users to click – more visible) on the excel file versus on the ribbon tab? Thanks
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-12607)
    
    *   Can u help me please
        
        [Reply](https://trumpexcel.com/excel-add-in/#comment-12820)
        
8.  Dear Sir,
    
    Do you know how to modify the file name inside ‘add-ins dialogue box’? It is currently shown as ‘Highlight Errors’. Is there a way to change this name to something else and add a description under this name?
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-11970)
    
9.  Do you know of a way to make a VLookup Macro work on multiple Workbooks without having the same data
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-10192)
    
10.  This sounds easier to manage than adding macros to Personal.xlsb like I am doing now. I have a couple computers I would like to keep the macros in sync for. Is it possible to store the .add-in file on One Drive and have both copies of Excel access the file? Both computers are set to have off-line access to One Drive, so the add-in file would always be available. That way, I can edit a macro in one location (I have one that needs to be edited every year to point to a new file) and have both computers access the most recent version.
    
    [Reply](https://trumpexcel.com/excel-add-in/#comment-3126)
    
    *   Hello Omar.. I believe it should work even if you have the file in One drive folder
        
        [Reply](https://trumpexcel.com/excel-add-in/#comment-3127)
        
        *   Thanks. I’ll do some testing. On of my concerns is what happens if both computers have Excel open at the same time. I’ll look into that.
            
            [Reply](https://trumpexcel.com/excel-add-in/#comment-3141)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-add-in/#respond)

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