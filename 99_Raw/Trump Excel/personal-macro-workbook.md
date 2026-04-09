# Excel Personal Macro Workbook | Save & Use Macros in All Workbooks

**Source:** https://trumpexcel.com/personal-macro-workbook

---

[Skip to content](https://trumpexcel.com/personal-macro-workbook/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/personal-macro-workbook/#below-title)

When you create/[record a macro](https://trumpexcel.com/record-macro-vba/)
 in a workbook in Excel, it can only be used in that workbook.

But what if you have a list of [useful Excel macros](https://trumpexcel.com/excel-macro-examples/)
 that you want to use in all the workbooks?  In such a case, it’s a good idea to save these in your Personal Macro Workbook.

Doing this would allow you to access the macro code from any workbook on your system.

This will save time as you don’t have to recreate the same macros again and again for every workbook. Instead, you can just create it once, store it in the personal macro workbook, and access it from any workbook.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/personal-macro-workbook/#)

What is a Personal Macro Workbook?
----------------------------------

A Personal Macro Workbook is a hidden workbook in your system that opens whenever you open the Excel application.

_Related: [How to Automatically Open Specific Excel Files on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
_

It’s a place where you can store macro codes and then access these macros from any workbook. It’s a great place to store those macros that you want to use often.

To give you an example, suppose you regularly get data from your colleagues, and you’re required to clean the data and format it. Since you need to follow the same steps every time, you can create a macro to do this and save it in the Personal Macro Workbook.

Now, whenever you get the Excel file, you just need to run the macro (which is stored in the personal workbook and can be accessed from any workbook), and you’re done.

Where Can I Find the Personal Macro Workbook?
---------------------------------------------

By default, the personal macro workbook doesn’t exist. You need to first create it.

Here are the steps to create a Personal Macro Workbook in Excel:

*   Open a new workbook or any existing workbook.
*   Go to the Developer tab in the ribbon.
*   Click on Record Macro.![Record a Macro to create the Personal Macro Workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20128'%3E%3C/svg%3E)
*   In the Record Macro dialog box, specify a name (default is fine too).
*   In the ‘Store Macro in’ drop down, select Personal Macro Workbook.![Save Macro in Personal Macro Workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20288'%3E%3C/svg%3E)
*   Click OK.

Note: If you can’t see the developer tab in the ribbon, [here are the steps](https://trumpexcel.com/excel-developer-tab/)
 to enable it.

Doing this would create a new workbook with the name PERSONAL.XLSB and store the macro in this workbook.

Since we did absolutely nothing, the macro has no code in it. This was done to create the Personal Macro Workbook.

Now that the Personal Macro Workbook is created, you need to **Close** all the open workbooks. Doing this would show a prompt as shown below:

![Click on Save to create the Personal Macro Workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20141'%3E%3C/svg%3E)

**Select Save**.

When this is done, Excel will create and store the PERSONAL.XLSB file in the start folder, where it would automatically open in the backend whenever you open Excel.

How to Copy Macros in the Personal Macro Workbook?
--------------------------------------------------

Once the PERSONAL.XLSB file is created and saved, you can copy macros that you wish to reuse again.

Here are the steps to copy macros in the Personal Macro Workbook:

*   Open Excel.
*   Go to the Developer tab.
*   Click on Visual Basic option. This will open the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
     (or use ALT + F11).![Click on Visual Basic Editor to Copy Macro in Personal Macro Workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20128'%3E%3C/svg%3E)
*   In the VB Editor, within the Project Explorer, you will see the PERSONAL.XLSB object.![VB Editor has the Personal Macro Workbook now](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20299%20277'%3E%3C/svg%3E)
*   Double-click on Module 1.![Double click on Module in Personal Macro Object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20299%20277'%3E%3C/svg%3E)
*   Copy and paste the macro code in the Module code window.
*   Close the Vb Editor.
*   Close and Save Excel.

The above steps would save the macros you want to reuse in the Personal Macro Workbook.

Also read: [How to Remove Macros From an Excel Workbook](https://trumpexcel.com/remove-macros-from-excel/)

How to Use Macros Stored in Personal Macro Workbook?
----------------------------------------------------

Suppose you have a list of macros saved in the Personal Macro workbook and you want to use it on a new Excel file you get.

Here are the steps to do this:

*   Go to the Developer tab.
*   Click on Macros.
*   In the Macro dialog box, select the macro that you want to run.
*   Click on Run.

Note that the macro dialog box shows you the list of all the macros that are available for use in the open workbook. This would include the macros stored in the workbook as well as the ones stored in the Personal Macro Workbook.

You can also [run a macro](https://trumpexcel.com/run-a-macro-excel/)
 by assigning a keyboard shortcut to the macro or [insert a shape/button and assign the macro](https://trumpexcel.com/assign-macro-to-button-in-excel/)
 to it.

You can also use the Personal Macro Workbook to store custom functions (user-defined functions) created in VBA.

**You May Also Like the Following Excel Tutorials:**

*   [Working with Cells and Ranges in Excel VBA](https://trumpexcel.com/vba-ranges/)
    .
*   [Working with Worksheets in Excel VBA](https://trumpexcel.com/vba-worksheets/)
    .
*   [Working with Workbooks in Excel VBA](https://trumpexcel.com/vba-workbook/)
    .
*   [Creating a User Defined Function in Excel using VBA](https://trumpexcel.com/user-defined-function-vba/)
    .
*   [Excel VBA Events – An Easy (and Complete) Guide.](https://trumpexcel.com/vba-events/)
    
*   [Using Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .
*   [If Then Else Statement in Excel VBA](https://trumpexcel.com/if-then-else-vba/)
    .
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “Excel Personal Macro Workbook | Save & Use Macros in All Workbooks”
----------------------------------------------------------------------------------

1.  Thank You It helped me alot
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-14835)
    
2.  Very helpful. It works. The Excel has features to use macro on all workbooks. 🙂
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-13340)
    
3.  An excellent help to the students and senior mediocre like me
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-12286)
    
4.  Thanks a lot! Didn’t know about the Personal Macro Workbook, it really helped me.
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-12133)
    
5.  Thanks a lot! I knew about most of the excel features, but this is about \*combining\* them in the right way! 🙂
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-11886)
    
6.  Thanks for your so much favour,Puneet can you tell me code to split column category wise like we have written Category as column header and under it we have data that like department accounts,store,complaints etc. How can we split our data based upon this criteria
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-11390)
    
7.  I created a Function in my Personal.xlsb. It works, but I cannot access it just by typing =FUNCTIONNAME. I have to click on Insert Functions, More Functions, User Defined. Is there a way to make the Functions accessible as easy as =SUM…?
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-9432)
    
    *   Save the excel file as .xlsm
        
        [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-9477)
        
8.  You can also add a tab to the ribbon to access your macros from.  
    File>Options>Customize Ribbon. From the dropdown, “Choose Commands From” select Macros.
    
    On the other side “Customize The Ribbon”, make sure that “Main Tabs” is selected. At the bottom, click “New Tab”. You can then drag and drop your macros, name the tab and group, and assign icons to each macro.
    
    [Reply](https://trumpexcel.com/personal-macro-workbook/#comment-9426)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/personal-macro-workbook/#respond)

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