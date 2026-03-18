# How to Insert and Use a Radio Button (Option Button) in Excel

**Source:** https://trumpexcel.com/insert-use-radio-button-in-excel

---

[Skip to content](https://trumpexcel.com/insert-use-radio-button-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-use-radio-button-in-excel/#below-title)

A Radio Button in Excel (also called the Option Button) can be used to select one of the many choices/options.

You must have seen it on hundreds of web pages where you are asked to select an option by clicking on a small round shape next to the text. As soon as you select it, it gets a black dot in it (an indication that is marked).

The same thing can also be created in Excel. In this tutorial, I will refer to it as the Radio Button (as my Computer teacher taught me).

However, Excel refers to it as the ‘Option button’.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/insert-use-radio-button-in-excel/#)

To insert a radio button in Excel, you need to have the developer tab enabled in your workbook.

_Can’t see the developer tab?_

Don’t worry.. here are the steps.

Get the Developer Tab in Excel Ribbon
-------------------------------------

Below are the steps for getting the [developer tab](https://trumpexcel.com/excel-developer-tab/)
 in the ribbon in Excel 2013. While the screenshots I share here are of Excel 2013, the process is the same in Excel 2007 or 2010.

*   Right-click on any of the existing tabs in the ribbon and select Customize the Ribbon. It opens the Excel Options dialogue box.![Insert and Use Radio Button in Excel -Customize-the-ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20151'%3E%3C/svg%3E)
*   In the Excel Options dialogue box, you will have the Customize the Ribbon options. On the right, within the Main Tabs pane, check the Developer option.![Radio Button in Excel - Check the Developer Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20427'%3E%3C/svg%3E)
*   Click OK. This will make the developer tab appear as one of the tabs in the ribbon.![Developer Tab in Ribbon - for inserting the Option Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20128'%3E%3C/svg%3E)

Now with the developer tab visible, you get access to a variety of interactive controls. Let’s get on with it and insert that radio button we were talking about.

How to Insert a Radio Button in Excel
-------------------------------------

Here are the steps to insert a radio button in Excel:

*   Go to Developer Tab –> Controls –> Insert –> Form Controls –> Option Button.
    *   You would see that there are two kinds of interactive controls: Form Control and Interactive Control. While Form Controls are made to use only within Excel workbooks, interactive controls can be used in user forms as well. Interactive controls provide a lot more flexibility and have extensive properties. _In this tutorial, we will focus on Form Control Radio Button (also called Option button) only_.![Insert and Use Radio Button in Excel - Radio Option in Developer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20231'%3E%3C/svg%3E)
*   Hover the mouse anywhere in the worksheet. You will see a plus icon (instead of the regular cursor). Click anywhere, and it will insert a radio button.![Insert and Use Radio Button in Excel - Inserting Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20308'%3E%3C/svg%3E)
*   Congratulations! You have inserted a radio button in Excel. You can click on the button and check it. However, there is one small problem. As of now, this radio button is useless – it does nothing. For this to work, it needs to be connected with a cell in the worksheet. Only then will you be able to record the response (whether a person selects either option 1, or option 2, or option 3…). To configure this radio button, right-click on it and select Format Control.![Insert and Use Radio Button in Excel - Format Control](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20247%20243'%3E%3C/svg%3E)
*   In the Format Control dialogue box, in the Control tab, make the following changes:
    *   Value: Checked (this makes sure that the radio button is checked by default when you open the workbook).
    *   Cell Link: $A$1 (this is the cell linked to the radio button). You can manually enter this or select the cell to get the reference.![Formatting the Radio Button in Excel - Linking Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20420'%3E%3C/svg%3E)
*   Click OK.

Now your radio button is linked to cell A1. When you select the radio button, it will show 1 in cell A1.

![Insert and Use Radio Button in Excel - linked cell changes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20324%20132'%3E%3C/svg%3E)

The number you see in cell A1 (the linked cell) is the number of the radio button that has been selected. If you have multiple radio buttons, and if you select the second one, cell A1 will show 2.

Unlike [checkboxes in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
, in the case of a radio button, you can only select one of the radio buttons. This means that if you have more than one radio buttons, you can only select one of it (you can, however, group sets of radio buttons, covered later in this tutorial).

To work with radio buttons in Excel, you need to have more than one radio button in the worksheet. Let’s see how we can insert multiple radio buttons in Excel.

Adding Multiple Radio Buttons in Excel
--------------------------------------

There are three ways you can add multiple radio buttons in a worksheet in Excel.

### **#1 Inserting Radio Buttons using the Developer Tab**

The easiest way is to use the developer tab and insert the radio buttons (as shown above). With this method, you need to repeat the steps as many times as many radio buttons you want.

This can be the method of choice when you have to insert only a couple of radio buttons in Excel.

An interesting thing to note here is that if you have linked the first radio button with a cell in the worksheet, all the radio buttons that you insert after it would be linked to that same cell. Also, you will be able to check only one of the radio buttons.

### **#2 Copy Pasting the Radio Buttons**

A quick way to insert radio button is to copy and paste an existing radio button. You can do this by simply selecting the radio button and pressing Control + D.

This would create a copy of the existing radio button.

There are a couple of things you need to know when you use this method:

*   When you copy and paste an existing radio button, the Caption Name (text that you see to the right of the radio button) is also copied, but the background name (the name that Excel uses to refer to that object) changes. See the image below to understand the difference between the caption name and background name.![Insert and Use Radio Button in Excel -Caption Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20250'%3E%3C/svg%3E)
*   If the original radio button is linked to a cell in the worksheet, all the copied radio buttons would also be linked to that same cell.

### **#3 Drag and Fill Cells with Radio Buttons**

When you copy and paste a cell that contains a radio button, it creates a copy of the radio button as well.

Similarly, if you have a radio button in a cell and you select and drag the cell (as shown below), it will create copies of the radio button.

![Insert and Use Radio Button in Excel - insert by dragging](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20216%20288'%3E%3C/svg%3E)

These again follow the same rules discussed above:

*   When you create a copy of a radio button by copy pasting (or dragging) a cell that already has the radio button, the Caption Name (text that you see to the right of the radio button) of the radio button gets copied, but the background name (that Excel uses to refer to that object) changes.
*   If the original radio button is linked to a cell in the worksheet, all the copied radio buttons would also be linked to that same cell.

How to Group Radio Buttons in Excel
-----------------------------------

Imagine you have a survey with ten different questions. For each question, you can choose one answer (by clicking on the radio button for that answer). This means that you would make ten radio button selections in the survey.

Now to create such a survey in Excel, you would need to group the options with radio buttons, such that in a group, you can select only one option, but at the same time, you are allowed to check the radio button of some other group.

Something as shown below:

![Insert and Use Radio Button in Excel - select different groups](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20220'%3E%3C/svg%3E)

Here are the steps to group radio buttons in Excel:

*   Insert all the radio buttons that you want to group.
*   Go to Developer –> Controls –> Insert –> Group Box (Form Control).![Insert and Use Radio Button in Excel - Group control](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20237'%3E%3C/svg%3E)
*   Hover the mouse anywhere in the worksheet. You will see a plus icon (instead of the regular cursor). Click anywhere, and it will insert a group box.![Insert and Use Radio Button in Excel - Group control insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20328'%3E%3C/svg%3E)
*   Place the group box in such a way that all the radio buttons (that you want to group) are inside it. You can move and resize the radio buttons and the group box just like any other object.![Insert and Use Radio Button in Excel - Radio Buttons Grouped](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20240%20207'%3E%3C/svg%3E)
*   Link one of the radio buttons to a cell in the worksheet. All the radio buttons would automatically be linked to the same cell.
*   Repeat the steps above to create another group of radio buttons.

This way, you can have any number of independent groups where you can make only one selection within the group, the selection across groups is independent.

Deleting Radio Buttons in Excel
-------------------------------

You can easily delete a single radio button in Excel by selecting it and pressing the delete key. To select a radio button, you need to hold the Control key and the press the left button of the mouse.

If you want to delete multiple radio buttons:

*   Hold the Control key and select all the ones that you want to delete.
*   Press the Delete key.

If you have many radio buttons scattered in your worksheet, here is a way to get a list of all the radio buttons and delete at one go:

*   Go to Home –> Editing –> Find & Select –> Selection Pane.
    *   This will open a Selection Pane that will list all the objects on that worksheet (including radio buttons, checkboxes, shapes, and charts).![Insert and Use Radio Button in Excel - Selection Pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20364'%3E%3C/svg%3E)
*   Select all the radio buttons that you want to delete (to select multiple radio buttons, hold the control key while selecting) and hit the delete key.![Insert and Use Radio Button in Excel - Radio Buttons in Selection Pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20276%20210'%3E%3C/svg%3E)
    *   Note that the names of the radio buttons here are the backend names and not the caption names.

_Note: The selection pane displays all the objects on the active worksheet only._

How to Fix the Position of a Radio Button in Excel
--------------------------------------------------

One common issue with using shapes and objects in Excel is that when you resize cells or hide/delete rows/columns, it also affects the shapes/radio buttons.

Something as shown below:

![Insert and Use Radio Button in Excel - resize move](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20168'%3E%3C/svg%3E)

To stop the radio button from moving around when you resize or delete cells, do the following:

*   Left click on the radio button and select Format Control.![Insert and Use Radio Button in Excel - Format Control](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20247%20243'%3E%3C/svg%3E)
*   In the Format Control dialogue box, select the properties tab.![Insert and Use Radio Button in Excel - Properties](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20317'%3E%3C/svg%3E)
*   In the Properties tab, within Object Positioning, select Don’t move or size with cells.![Insert and Use Radio Button in Excel - Dont Move or Size](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20316'%3E%3C/svg%3E)
*   Click OK.

Now when you resize or delete cells, the radio button would stay put.

Enable Radio Buttons in a Protected Sheet in Excel
--------------------------------------------------

If you want to protect the entire worksheet, but want the radio buttons to work, here are the steps:

*   Right-click on the cell that is linked to the radio button and select Format Cell.![Insert and Use Radio Button in Excel - Format Cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20237%20361'%3E%3C/svg%3E)
*   In the Format Cells dialogue box, go to the Protection tab and uncheck the Locked Option.![Insert and Use Radio Button in Excel - locked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20376'%3E%3C/svg%3E)

Now when you protect the entire sheet, the radio button would still be working. Since Excel protects all the locked cells only, having the linked cell unlocked still makes it work.

Examples of Using Radio Button in Excel
---------------------------------------

Here are some examples where radio button is used:

*   [KPI Dashboard in Excel](https://trumpexcel.com/kpi-dashboard-in-excel-part-3/)
     (radio button used to extract data).
*   [Games of Thrones Dashboard](https://trumpexcel.com/game-of-thrones-dashboard/)
     (radio button used to sort data).

Radio Button Vs. Checkbox
-------------------------

While both the radio button and the checkbox looks similar, there are a few differences you need to know before using these.

A radio button allows a user to select only one of the radio buttons from a group. This means that if you have radio buttons for gender, you can only select one of the genders.

On the other hand, a checkbox is independent of other checkboxes, and you can select multiple at one time. For example, in a skill assessment survey, you can select multiple skills you have.

Here is the definition of radio button by [Wikipedia](https://en.wikipedia.org/wiki/Radio_button)
 that also covers the difference with a checkbox.

_“A radio button or option button is a graphical control element that allows the user to choose only one of a predefined set of mutually exclusive options. The singular property of a radio button makes it distinct from a checkbox, which allows more than one (or no) item to be selected and for the unselected state to be restored.”_

**You May Also Like the Following Excel Tutorials:**

*   [How to Insert a Scrollbar in Excel.](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
    
*   [Insert Checkmark in Excel](https://trumpexcel.com/check-mark/)
    .
*   [Complete Guide to Creating Excel Dashboards](https://trumpexcel.com/creating-excel-dashboard/)
    .
*   [Creating a Drop-down List in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [How to Create a Heat Map in Excel.](https://trumpexcel.com/heat-map-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “How to Insert and Use a Radio Button (Option Button) in Excel”
------------------------------------------------------------------------------

1.  Hi,
    
    Thank you for this tutorial, it really helped. I’m now wondering if it’s possible and how to change the format of the group box to remove the borders?
    
    Thank you
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-13568)
    
2.  I have a table which came with a Radio button on each row. There are over a 1000 rows. I am trying to get rid of all of them after retaining just the contents in another new column in the table. Having so many radio buttons in the spreadsheet makes the spreadsheet very very slow in opening, saving or refreshing.
    
    I tried the method you are suggesting here, but I find it totally impossible to select more than one radio button at a time. I have set up the Developer option in the ribbon, and I am holding down the CTRL key when selecting each one – but each one I select is de-selected as soon as I select the next one.
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-12886)
    
3.  Really useful & Thanks
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-11763)
    
4.  Say I create a radio button cell C10 – that is a yes/no. Is there a way to say , if response is no, to hide rows 11-18. Then put another radio button in c19 that is again a yes/no. If no is selected here to then hide rows 20-24, etc. etc. I have a checklist we are creating and this would make life easier.
    
    thanks,  
    Adam
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-10946)
    
    *   I can’t think of a way to hide it, but you can use conditional formatting to artificially hide the rows based on the radio button. Example  
        1\. link cell A1 to the radio button A & B, if A is selected, A1 = 1, if B is selected, A1 = 2.  
        2\. Put in conditional formatting based on A1. If A1 = 1, format cells so it appears empty (font = white etc…).
        
        [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-12374)
        
5.  Once a radio button is selected, is there a way to set it up to “uncheck” with a second click?
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-10585)
    
6.  After linking the radio button to a cell, I keep getting random numbers popping up. How can I get rid of this?
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-9957)
    
    *   link it to another empty cell instead. change the color to white font so it wont show.
        
        [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-10903)
        
7.  I have created 100 groups with 4 buttons in each…now each group have to be linked with the different cell. Linking one group with one cell manually takes a lot of time. Do anyone have suggestion to do it in easier and faster way….
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-3917)
    
    *   I DONT GIVE A DAMN
        
        [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-11594)
        
8.  How would one add a radio button or two, to convert cells from metric to imperial measurement?
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-3766)
    
    *   Radio buttons give the value of 1,2,3 and so on based on the choice, in to the designed cell.  
        So all you need is an if statement that checks the designated cell for the value and calculates acordingly.
        
        [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-13213)
        
9.  can i create more than four radio buttons in Excel within the same Group box?
    
    [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-3580)
    
    *   Yes you can.
        
        [Reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#comment-3618)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-use-radio-button-in-excel/#respond)

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