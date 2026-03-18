# How to Run a Macro in Excel - A Complete Step-by-Step Guide

**Source:** https://trumpexcel.com/run-a-macro-excel

---

[Skip to content](https://trumpexcel.com/run-a-macro-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/run-a-macro-excel/#below-title)

**Watch Video – How to Run a Macro in Excel**

In Excel, you can create a macro by [recording it](https://trumpexcel.com/record-macro-vba/)
 or by writing code in the [VB editor](https://trumpexcel.com/visual-basic-editor/)
.

Once created, you need to run the macro.

In this tutorial, I’ll show you different ways to run a macro in Excel.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/run-a-macro-excel/#)

How to Run a Macro in Excel
---------------------------

For the purpose of this tutorial, let’s say we have a macro named ‘ColorCell’ with the following code:

Sub ColorCell()
Range("A1").Interior.Color = vbRed
End Sub

This one line code would fill the cell A1 of the active sheet with red color.

Now let’s see various ways to run this macro in Excel.

### Run the Macro by Clicking on a Shape

One of the easiest ways to run a macro is to have a button in the worksheet and click that button to execute the macro.

It’s easy and intuitive.

The benefit of this method is that it makes it really easy and intuitive for anyone to run the macro. Even if you share the workbook with someone who has no knowledge of VBA, he/she can just click on the button and see the actions take place (without even knowing what happens in the back end).

Something as shown below:

![How to Run a Macro in Excel - Button Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20136'%3E%3C/svg%3E)

Here are the steps to do this:

*   Click the Insert tab.
*   In the Illustrations group, click on the Shapes icon. Insert any shape to which you want to assign the macro.![How to Run a Macro in Excel - Insert Shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20458%20213'%3E%3C/svg%3E)
*   Click anywhere on the worksheet. It will insert the shape object in the worksheet.![How to Run a Macro in Excel - insert Shape click](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20340'%3E%3C/svg%3E)
*   Resize/Format the shape the way you want. In the example above, I have changed the size, color, and border. You can also insert any text in the shape by simply selecting it and typing the text.![How to Run a Macro in Excel - format shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20293%20103'%3E%3C/svg%3E)
*   Right-click on the shape and select the Assign Macro option. This opens the Assign Macro dialogue box.![How to Run a Macro in Excel - Assign macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20259%20466'%3E%3C/svg%3E)
*   In the Assign Macro dialogue box, select the macro you want to assign to the shape and click the OK button.![How to Run a Macro in Excel - Assign Macro Dialogue box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20372'%3E%3C/svg%3E)

That’s it! Now the shape would work as a button and whenever you click on it, it will run the assigned macro.![How to Run a Macro in Excel - Button Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20136'%3E%3C/svg%3E)

### Run Macro By Clicking a Button

While the shape is something you can format, a button has a standard format.

Here is how it looks:

![How to Run a Macro in Excel - button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20136'%3E%3C/svg%3E)

You can assign a macro to a button and then can run the macro by simply clicking that button.

Here are the steps to [assign a macro to a button](https://trumpexcel.com/assign-macro-to-button-in-excel/)
:

*   Go to the Developer tab –> Controls –> Insert –> Form Controls –> Button.
    *   [Developer tab](https://trumpexcel.com/excel-developer-tab/)
         is not visible on the ribbon by default and you may need to add it before using it..![How to Run a Macro in Excel - Insert Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20268%20243'%3E%3C/svg%3E)
*   Click anywhere on the worksheet. As soon as you do this, it will open the Assign Macro dialogue box.
*   Select the macro you want to assign to the button and click on OK. This would insert the button in the worksheet.![How to Run a Macro in Excel - Assign Macro Dialogue box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20372'%3E%3C/svg%3E)

The button inserted using this technique is a standard one and you can’t change the formatting of the button (unlike shapes, where you can change practically everything).

However, you can change the text of the button. To do this, right-click on it and select Edit Text.

![How to Run a Macro in Excel - change button text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20231%20246'%3E%3C/svg%3E)

_Note: You can also assign a macro to other interactive controls, such as a [checkbox](https://trumpexcel.com/insert-checkbox-in-excel/)
 or [scrollbar](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
._

### Run a Macro from the Ribbon (Developer Tab)

If you have multiple macros in the workbook, you can see a list of all the macros in the Macros dialogue box. It makes it easy to run multiple macros from a single place.

Here are the steps:

*   Go to the Developer Tab –> Code –> Macros.![How to Run a Macro in Excel - Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20621%20130'%3E%3C/svg%3E)
*   The Macros dialogue box lists all the macros in the workbook. Select the one that you want to run.![How to Run a Macro in Excel - Select Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20374'%3E%3C/svg%3E)
*   Click Run.![How to Run a Macro in Excel - Macro Run](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20373'%3E%3C/svg%3E)

### Run a Macro from the VB Editor

If you are the one writing and testing macros, then instead of inserting buttons, you can directly run a macro from the VB Editor.

Here are the steps:

*   Select any line within the code in the code window. If you have multiple macros/subs, make sure your cursor is in the macro that you want to run.
*   Go to the toolbar and click on the Green triangle icon (you can also use the keyboard shortcut – F5).![How to Run a Macro in Excel - From VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20203'%3E%3C/svg%3E)

As soon as you do this, the macro would be executed.

If you only have the VB Editor open (and you can’t see the worksheet), you may not see the change happening in the worksheet. You can minimize the VB Editor screen and then run the macro to see the changes in real-time.

**You May Also Like the Following Excel VBA Tutorials:**

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
*   [Creating User-Defined Functions in Excel](https://trumpexcel.com/user-defined-function-vba/)
    .
*   [Excel VBA Events – An Easy (and Complete) Guide.](https://trumpexcel.com/vba-events/)
    
*   [How to Create and Use Personal Macro Workbook in Excel](https://trumpexcel.com/personal-macro-workbook/)
    .
*   [24 Useful Excel Macro Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .
*   [Guide to Using For Next Loop in Excel VBA](https://trumpexcel.com/for-next-loop-excel-vba/)
    
*   [How to Enable Macros in Excel?](https://trumpexcel.com/enable-macros-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “How to Run a Macro in Excel?”
--------------------------------------------

1.  Is there a way to carry comments over week to week
    
    [Reply](https://trumpexcel.com/run-a-macro-excel/#comment-14614)
    
2.  Yes
    
    [Reply](https://trumpexcel.com/run-a-macro-excel/#comment-11740)
    
3.  do i able to put a macro for different sheet together to get them print in one click button
    
    [Reply](https://trumpexcel.com/run-a-macro-excel/#comment-11053)
    
4.  Ok, I have an interesting challenge here. I need to run a macro which will link my first columns (A), which is a drop down list of job positions (5 entries), to my 2nd column (B), which are check boxes of skill requirements (10 entries), and my 3rd column (C), which is a list of training activities (50 entries). I’m trying to be able to select a job position which will generate the skill requirements and the related training activities. As an example: If selected Job position “A2” = “skill B1”, “skill B2”, “skill B5” = training activities “C4”, “C7”, “C18”, “C21”, “C37”, “C45”, “C49”. Thanks for your help!
    
    [Reply](https://trumpexcel.com/run-a-macro-excel/#comment-3325)
    
5.  Ok, I have an interesting challenge here. I need to run a macro which will link my first columns (A), which is a drop down list of job positions (5 entries), to my 2nd column (B), which are check boxes of skill requirements (10 entries), and my 3rd column (C), which is a list of training activities (50 entries). I’m trying to be able to select a job position which will generate the skill requirements and the related training activities. As an example: If selected Job position “A2” = “skill B1”, “skill B2”, “skill B5” = training activities “C4”, “C7”, “C18”, “C21”, “C37”, “C45”, “C49”. Thanks for your help!
    
    [Reply](https://trumpexcel.com/run-a-macro-excel/#comment-3324)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/run-a-macro-excel/#respond)

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