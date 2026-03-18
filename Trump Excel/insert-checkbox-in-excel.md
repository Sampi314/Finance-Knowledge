# How to Insert Checkbox in Excel (Easy Step-by-Step Guide)

**Source:** https://trumpexcel.com/insert-checkbox-in-excel

---

[Skip to content](https://trumpexcel.com/insert-checkbox-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-checkbox-in-excel/#below-title)

**Watch Video – How to Insert and Use a Checkbox in Excel**

In Excel, a checkbox is an interactive tool that can be used to select or deselect an option. You must have seen it in many web form available online.

You can use a checkbox in Excel to create [interactive checklists](https://trumpexcel.com/excel-to-do-list-template-download/)
, dynamic charts, and [dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

This Excel tutorial covers the following topics:

*   [How to Get the Developer Tab in Excel Ribbon](https://trumpexcel.com/insert-checkbox-in-excel/#developertab)
    .
*   [How to Insert a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/#insertcheckbox)
    .
*   [Examples of Using Checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/#examples)
    .
*   [How to Insert Multiple Checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/#mulitplecheckbox)
    .
*   [How to Delete a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/#deletingcheckbox)
    .
*   [How to Fix the Position of a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/#fixcheckbox)
    .
*   [Caption Name Vs. Backend Name](https://trumpexcel.com/insert-checkbox-in-excel/#captionname)
    

To insert a checkbox in Excel, you first need to have the Developer tab enabled in your workbook.

_Can’t see the developer tab?_ 

_Don’t worry and keep reading!_

Get the Developer Tab in Excel Ribbon
-------------------------------------

The first step in inserting a checkbox in Excel is to have the developer tab visible in the ribbons area. The developer tab contains the checkbox control that we need to use to insert a checkbox in Excel.

Below are the steps for getting the [developer tab](https://trumpexcel.com/excel-developer-tab/)
 in the Excel ribbon.

*   Right click on any of the existing tabs in the Excel ribbon and select Customize the Ribbon. It opens the Excel Options dialog box.![Customize the ribbon to add developer tab for checkbox](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20151'%3E%3C/svg%3E)
*   In the Excel Options dialog box, you will have the Customize the Ribbon options. On the right, within the Main Tabs pane, check the Developer option.![Adding the Developer tab to insert checkbox in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20427'%3E%3C/svg%3E)
*   Click OK. This will make the developer tab appear as one of the tabs in the ribbon.![Developer tab visible in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20128'%3E%3C/svg%3E)

Now with the Developer tab visible, you get access to a variety of interactive controls.

How to Insert a Checkbox in Excel
---------------------------------

Here are the steps to insert a checkbox in Excel:

1.  Go to Developer Tab –> Controls –> Insert –> Form Controls –> Check Box.  
    ![Adding a checkbox in Excel- Select the checkmark in form controls](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20256'%3E%3C/svg%3E)
2.  Click anywhere in the worksheet, and it will insert a checkbox (as shown below).![Click anywhere on the worksheet to insert the checkbox](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20624%20304'%3E%3C/svg%3E)
3.  Now to need to link the checkbox to a cell in Excel. To do this, right-click on the checkbox and select Format Control.![Right click on the checkbox and select Format Control](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20221%20212'%3E%3C/svg%3E)
4.  In the Format Control dialog box, in the Control tab, make the following changes:
    *   Value: Checked (this makes sure that the checkbox is checked by default when you open the workbook)
    *   Cell Link: $A$1 (this is the cell linked to the checkbox). You can manually enter this or select the cell to get the reference.![Link a check box to a cell in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20424'%3E%3C/svg%3E)
5.  Click OK.

Now your checkbox is linked to cell A1, and when you check the checkbox, it will show TRUE in cell A1, and when you uncheck it, it will show FALSE.

![Excel Checkbox is now linked to the cell A1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20280'%3E%3C/svg%3E)

Examples of Using a Checkbox in Excel
-------------------------------------

Here are a couple of examples where you can use a checkbox in Excel.

### **Creating an Interactive To-Do List in Excel**

Below is an example of a To-Do list that uses checkboxes to mark the task as complete.

![To Do List using check boxes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20756%20228'%3E%3C/svg%3E)

A couple of things are happening in the example above:

*   As soon as you check the checkbox for an item/task, the status changes to Done (from To be Done), the cell gets a green shade, and the text gets a [strikethrough format](https://trumpexcel.com/strikethrough-in-excel-shortcut/)
    .
*   The value of the cell link for that checkbox changes from FALSE to TRUE.
*   The ‘Task Completed’ and ‘% of Task Completed’ numbers (in cell H3 and H4) change based on how many tasks have been marked as completed.

Here is how to make this:

*   Have the activities listed in cell A2:A7.
*   Insert checkboxes and place it in cell B2:B7.
*   Link these checkboxes to cell E2:E7. There is no way to link all the checkboxes at one go. You’ll have to manually link each checkbox one by one.
*   In cell C2, enter the following formula: \=[IF](https://trumpexcel.com/excel-if-function/)
    (E2,”Done”,”To Be Done”) and drag for all the cells (C2:C7).
    *   In cell C2:C7, apply [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
         to give the cell a green background color and strikethrough format when the value in the cell is Done.
*   In cell H3, use the following formula: \=[COUNTIF](https://trumpexcel.com/excel-countif-function/)
    ($E$2:$E$7,TRUE)
    *   This will count the total numbers of tasks that have been marked as completed.
*   In cell H4, use the following formula: \=COUNTIF($E$2:$E$7,TRUE)/COUNTIF($E$2:$E$7,”<>”)
    *   This will show the percentage of tasks completed.

[Click here to download the checklist](https://trumpexcel.com/wp-content/uploads/2015/11/Checklist-in-Excel.xlsx)
.

[![Online Excel Dashboard Training - 728x90](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%2090'%3E%3C/svg%3E)](https://trumpexcel.com/excel-dashboard-course/)

### **Creating a Dynamic Chart in Excel**

You can use an Excel checkbox to create a [dynamic chart](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
 as shown below:

![Insert a Checkbox in Excel - Dynamic Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20356'%3E%3C/svg%3E)

In this case, the checkbox above the chart is linked to cell C7 and C8.

If you check the checkbox for 2013, the value of cell C7 becomes TRUE. Similarly, if you check the checkbox in for 2014, the value of cell C8 becomes TRUE.

The data used in creating this chart is in C11 to F13. The data for 2013 and 2014 is dependent on the linked cell (C7 and C8). If the value in cell C7 is TRUE, you see the values in C11:F11, else you see the #N/A error. Same is the case with data for 2014.

Now based on which checkbox is checked, that data is shown as a line in the chart.

**[Click here to download the dynamic chart template](https://trumpexcel.com/wp-content/uploads/2015/11/Dynamic-Chart-Series-Selection-Check-box.xlsx)
**.

Inserting Multiple Checkboxes in Excel
--------------------------------------

There are a couple of ways you can insert multiple checkboxes in the same worksheet.

### **#1 Inserting a Checkbox using the Developer Tab**

To insert more than one checkbox, go to the Developer Tab –> Controls –> Insert –> Form Controls –> Check Box.

Now when you click anywhere in the worksheet, it will insert a new checkbox.

You can repeat the same process to insert multiple checkboxes in Excel.

_Note:_

*   _The checkbox inserted this way are not linked to any cell. You need to manually link all the checkboxes._ 
*   _The checkbox would have different caption names, such as Check Box 1 and Check Box 2, and so on._

### **#2 Copy Pasting the Checkbox**

Select an existing checkbox, copy it and paste it. You can also use the keyboard shortcut (Control + D).

_Note:_ 

*   _The copied checkboxes are linked to the same cell as that of the original checkbox. You need to manually change the cell link for each checkbox._
*   _The caption names of all the copied checkboxes are the same. However, the backend name would be different (as these are separate objects)._

### **#3 Drag and Fill Cells with Checkbox**

If you have a checkbox in a cell in Excel and you drag all [fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
 down, it will create copies of the checkbox. Something as shown below:

![Inserting Multiple Checkboxes in Excel - Drag and Copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20268'%3E%3C/svg%3E)

_Note:_

*   _The caption names of all the new checkboxes are the same. However, the backend name would be different (as these are separate objects)._
*   _All these checkboxes would be linked to the same cell (if you linked the first one). You need to manually change the link of all these one by one._

Deleting the Checkbox in Excel
------------------------------

You can easily [delete a single checkbox](https://spreadsheetplanet.com/delete-remove-checkbox-excel/)
 by selecting it and pressing the delete key. To select a checkbox, you need to hold the Control key and the press the left button of the mouse.

If you want to delete multiple checkboxes:

*   Hold the Control key and select all the ones that you want to delete.
*   Press the Delete key.

If you have many checkboxes scattered in your worksheet, here is a way to get a list of all the checkbox and delete at one go:

*   Go to Home –> Editing –> Find & Select –> Selection Pane.
    *   This will open a Selection Pane that will list all the objects on that worksheet (including checkboxes, shapes, and charts).![Insert a Checkbox in Excel - Selection Pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20364'%3E%3C/svg%3E)
*   Select all the checkboxes you want to delete (to select multiple checkboxes, hold the control key while selecting) and hit the delete key.
    *   Note that the names of the checkboxes here are the backend names and not the caption names.![Insert a Checkbox in Excel - Selection Pane items](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20248'%3E%3C/svg%3E)

_Note: The selection pane displays all the objects of the active worksheet only._

How Fix the Position of a Checkbox in Excel
-------------------------------------------

One common issue with using shapes and objects in Excel is that when you resize cells or hide/delete rows/columns, it also affects the shapes/checkboxes. Something as shown below:

![Insert a Checkbox in Excel - Move Size Fixed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20204'%3E%3C/svg%3E)

To stop the checkbox from moving around when you resize or delete cells, do the following:

*   Left click on the checkbox and select Format Control.![Insert a Checkbox in Excel - Format Control resize](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20223%20236'%3E%3C/svg%3E)
*   In the Format Control dialog box, select the properties tab.![Insert a Checkbox in Excel - Properties](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20317'%3E%3C/svg%3E)
*   In the properties tab, within Object Positioning, select Don’t move or size with cells.![Steps to Insert Check Marks in Excel - Don't move or size](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20316'%3E%3C/svg%3E)
*   Click OK.

Now when you resize or delete cells, the checkbox would stay put.

Caption Name Vs. Name
---------------------

When you insert a checkbox in Excel, you see a name in front of the box (such as Check Box 1 or Check Box 2).

![Insert a Checkbox in Excel - Caption Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20225%20142'%3E%3C/svg%3E)

This text – in front of the box –  is the Caption Name of the checkbox. To edit this text, right-click and select the ‘Edit Text’ option.

![Insert a Checkbox in Excel - Change Caption Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20272'%3E%3C/svg%3E)

While you see the new text, in the backend, Excel continues to refer to this checkbox as Check Box 1.

If you select the checkbox and look at the Name Box field, you will see the name Excel uses for this checkbox in the backend.

![Insert a Checkbox in Excel - Caption and Backend Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20272'%3E%3C/svg%3E)

You can easily change this backend name by first selecting the checkbox in the worksheet and then typing the name in the name box (the naming rules are same as that of [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
).

See Also: [How to Insert a Checkbox in Google Sheets](https://spreadsheetpoint.com/checkbox-google-sheets/)
.

**You May Also Like the Following Excel Tutorials:**

*   [Inserting Checkmark in Excel](https://trumpexcel.com/check-mark/)
    .
*   [Create Dynamic Chart using Checkbox](https://trumpexcel.com/dynamic-excel-chart-check-box/)
    .
*   [Create Checklists using Checkbox in Excel.](https://trumpexcel.com/excel-to-do-list-template-download/)
    
*   [VBA Guide to Using Checkboxes in Excel](http://wellsr.com/vba/2015/excel/complete-guide-to-excel-vba-form-control-checkboxes/)
    .
*   [How to Insert a Scroll Bar in Excel](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
    .
*   [How to Insert and Use a Radio Button in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

17 thoughts on “How to Insert Checkbox in Excel (to Create Interactive Lists and Charts)”
-----------------------------------------------------------------------------------------

1.  How do you get the check boxes to match going across? I can’t figure out how to make them online on my spreadsheet, without formatting each cell individually.
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-13711)
    
2.  I copy/pasted the formula for the Percentage of Tasks Completed function, with alterations re where my TRUE/FALSE parameters are but I get a DIV/0 error. Excel claims that I have made a divide by zero error.
    
    What am I doing wrong?
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-13418)
    
3.  very very good wlshes for whom help us learn from two  
    Ocean that is between us
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-13066)
    
4.  We should not have to manually link each checkbox to each cell.
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-12845)
    
5.  Can you use this to insert a checkbox inside of a cell instead of laying on top like a graph or just linking to a separate cell? I found another guide that does this using special characters but it would be nice if I could just represent the cell’s true/false value by a checked or unchecked box.
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-11999)
    
6.  Thank you Sumit – great tips and tutorials! I would like to find out if there’s a way to take this further. I want to create a spreadsheet with a row for each of the 50 United States. Each row would contain data specific to our industry in each state. I would like to insert a checkbox in each row. A user would check off the set of states involved in a transaction, and then click a “Filter” button, which would leave only the checked states columns visible. I would then want to create a report which would pull data only from the checked rows. Is this possible? Thanks again!
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-11355)
    
7.  how can you filter by check boxes? I have one column with check boxes and what if I would like to filter by the check boxes which have a tick and which doesn’t…?
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-11080)
    
8.  thanks Sumit. very useful tips.
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-11045)
    
9.  Hi  
    I have a question, I have an excel table, where I input my data in first 5 columns, next 3 have formulas which are Calculated automatically based on first 5 columns. Last 1 column has a check box which is linked to the cell.  
    Now whenever I add another row in Table all formulas are copied from above table row with new range. but check box is not copied automatically. and if copy it manually and paste in new row. the new check box is also linked to the above cell instead of new row.  
    I want it to copy automatically, same like formulas. I also want to be linked with the new row.
    
    Can you please advice me, how to do it?
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-10574)
    
10.  Thanks! very useful. Keep it up!
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-9741)
    
11.  Thanks for posting this. Big help! Keep it up!
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-9740)
    
12.  Sumit it very useful when you have to display data for more than 2-3 years its easy and cosmetic too.  
    Thanks.
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-3224)
    
13.  sumit these tutorials are v useful…..tell me either to work with developer is easy or using formulas ..i want to learn dynamic filter with formulas also if easy
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-3043)
    
    *   Hello Raz.. Both have their benefits. Formulas are easy to apply and replicate, however, may have some limitations. With VBA, you can do a lot more (but that would require a working knowledge of VBA). Here is an example of creating a dynamic filter (non-vba) – [http://trumpexcel.com/2015/01/dynamic-excel-filter/](http://trumpexcel.com/2015/01/dynamic-excel-filter/)
        
        [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-3057)
        
14.  Check Box are very useful if you are working on some constant data formats. You can control your functions with check boxes. Very Nice Post. Thanks
    
    [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-2695)
    
    *   Thanks for commenting Puneet.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-2772)
        
        *   can i ask u some question
            
            [Reply](https://trumpexcel.com/insert-checkbox-in-excel/#comment-8484)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-checkbox-in-excel/#respond)

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