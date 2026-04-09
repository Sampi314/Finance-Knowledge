# Visual Basic Editor - How to Open and Use it in Excel

**Source:** https://trumpexcel.com/visual-basic-editor

---

[Skip to content](https://trumpexcel.com/visual-basic-editor/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/visual-basic-editor/#below-title)

The first step to working with [VBA in Excel](https://trumpexcel.com/excel-vba/)
 is to get yourself familiarized with the Visual Basic Editor (also called the VBA Editor or VB Editor).

In this tutorial, I will cover all there is to know about the VBA Editor and some useful options that you should know when coding in Excel VBA.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/visual-basic-editor/#)

What is Visual Basic Editor in Excel?
-------------------------------------

Visual Basic Editor is a separate application that is a part of Excel and opens whenever you open an Excel workbook. By default, it’s hidden and to access it, you need to activate it.

VB Editor is the place where you keep the VB code.

There are multiple ways you get the code in the VB Editor:

1.  When you [record a macro](https://trumpexcel.com/record-macro-vba/)
    , it automatically creates a new module in the VB Editor and inserts the code in that module.
2.  You can manually type VB code in the VB editor.
3.  You can copy a code from some other workbook or from the internet and paste it in the VB Editor.

Opening the VB Editor
---------------------

There are various ways to open the Visual Basic Editor in Excel:

1.  Using a Keyboard Shortcut (easiest and fastest)
2.  Using the Developer Tab.
3.  Using the Worksheet Tabs.

Let’s go through each of these quickly.

### Keyboard Shortcut to Open the Visual Basic Editor

The easiest way to open the Visual Basic editor is to use the keyboard shortcut – **ALT + F11** (hold the ALT key and press the F11 key).

![Keyboard Shortcut to open Visual Basic Editor in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20100'%3E%3C/svg%3E)

As soon as you do this, it will open a separate window for the Visual Basic editor.

This shortcut works as a toggle, so when you use it again, it will take you back to the Excel application (without closing the VB Editor).

_The shortcut for the Mac version is **Opt + F11** or **Fn + Opt + F11**_

### Using the Developer Tab

To open the Visual Basic Editor from the ribbon:

1.  Click the Developer tab (if you don’t see a developer tab, [read this](https://trumpexcel.com/excel-developer-tab/)
     on how to get it).
2.  In the Code group, click on Visual Basic.

![Visual Basic Editor button in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20707%20191'%3E%3C/svg%3E)

### Using the Worksheet Tab

This is a less used method to open the Vb Editor.

Go to any of the worksheet tabs, right-click, and select ‘View Code’.

![View code to open the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20279%20337'%3E%3C/svg%3E)

This method wouldn’t just open the VB Editor, it will also take you to the code window for that worksheet object.

This is useful when you want to write code that works only for a specific worksheet. This is usually the case with [worksheet events](https://trumpexcel.com/vba-events/)
.

Anatomy of the Visual Basic Editor in Excel
-------------------------------------------

When you open the VB Editor for the first time, it may look a bit overwhelming.

There are different options and sections that may seem completely new at first.

Also, it still has an old Excel 97 days look. While Excel has improved tremendously in design and usability over the years, the VB Editor has not seen any change in the way it looks.

In this section, I will take you through the different parts of the Visual Basic Editor application.

Note: When I started using VBA years ago, I was quite overwhelmed with all these new options and windows. But as you get used to working with VBA, you would get comfortable with most of these. And most of the time, you’ll not be required to use all the options, only a hand full.

Below is an image of the different components of the VB Editor. These are then described in detail in the below sections of this tutorial.

![Different Parts of the VB Editor in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20400'%3E%3C/svg%3E)

Now let’s quickly go through each of these components and understand what it does:

### Menu Bar

This is where you have all the options that you can use in the VB Editor. It is similar to the Excel ribbon where you have tabs and options with each tab.

You can explore the available options by clicking on each of the menu element.

You will notice that most of the options in VB Editor have keyboard shortcuts mentioned next to it. Once you get used to a few keyboard shortcuts, working with the VB Editor becomes really easy.

### Tool Bar

By default, there is a toolbar in the VB Editor which has some useful options that you’re likely to need most often. This is just like the Quick Access Toolbar in Excel. It gives you quick access to some of the useful options.

You can customize it a little by removing or adding options to it (by clicking on the small downward pointing arrow at the end of the toolbar).

![Add or Remove options in the toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20152'%3E%3C/svg%3E)

In most cases, the default toolbar is all you need when working with the VB Editor.

You can move the toolbar above the menu bar by clicking on the three gray dots (at the beginning of the toolbar) and dragging it above the menu bar.

Note: There are four toolbars in the VB Editor – Standard, Debug, Edit, and User form. What you see in the image above (which is also the default) is the standard toolbar. You can access other toolbars by going to the View option and hovering the cursor on the Toolbars option. You can add one or more toolbars to the VB Editor if you want.

### Project Explorer

Project Explorer is a window on the left that shows all the objects currently open in Excel.

When you’re working with Excel, every workbook or add-in that is open is a project. And each of these projects can have a collection of objects in it.

For example, in the below image, the Project Explorer shows the two workbooks that are open (Book1 and Book2) and the objects in each workbook (worksheets, ThisWorkbook, and Module in Book1).

There is a plus icon to the left of objects that you can use to collapse the list of objects or expand and see the complete list of objects.

![Project Explorer in Excel VBA Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20313%20495'%3E%3C/svg%3E)

The following objects can be a part of the Project Explorer:

1.  All open Workbooks – within each workbook (which is also called a project), you can have the following objects:
    *   _Worksheet object_ for each worksheet in the workbook
    *   _ThisWorkbook object_ which represents the workbook itself
    *   Chartsheet _object_ for each chart sheet (these are not as common as worksheets)
    *   _Modules_ – This is where the code that is generated with a macro recorder goes. You can also write or copy-paste VBA code here.
2.  All open Add-ins

Consider the Project Explorer as a place that outlines all the objects open in Excel at the given time.

The keyboard shortcut to open the Project Explorer is **Control + R** (hold the control key and then press R). To close it, simply click the close icon at the top right of the Project Explorer window.

Note: For every object in Project Explorer, there is a code window in which you can write the code (or copy and paste it from somewhere). The code window appears when you double click on the object.

### Properties Window

Properties window is where you get to see the properties of the select object. If you don’t have the Properties window already, you can get it by using the keyboard shortcut F4 (or go to the View tab and click Properties window).

Properties window is a floating window which you can dock in the VB Editor. In the below example, I have docked it just below the Project Explorer.

![Properties Window is docked below Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20306%20337'%3E%3C/svg%3E)

Properties window allows us to change the properties of a selected object. For example, if I want to make a worksheet hidden (or very hidden), I can do that by changing the Visible Property of the selected worksheet object.

![Changing the Visible Property of the Worksheet in Properties Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20306%20548'%3E%3C/svg%3E)

**Related**: [Hiding a Worksheet in Excel](https://trumpexcel.com/hide-worksheet/)
 (that can not be un-hidden easily)

### Code Window

There is a code window for each object that is listed in the Project Explorer. You can open the code window for an object by double-clicking on it in the Project Explorer area.

Code window is where you’ll write your code or copy paste a code from somewhere else.

When you record a macro, the code for it goes into the code window of a module. Excel automatically inserts a module to place the code in it when recording a macro.

**Related**: [How to Run a Macro (VBA Code) in Excel](https://trumpexcel.com/run-a-macro-excel/)
.

### Immediate Window

The [Immediate window](https://trumpexcel.com/vba-immediate-window/)
 is mostly used when debugging code. One way I use the Immediate window is by using a Print.Debug statement within the code and then run the code.

It helps me to debug the code and determine where my code gets stuck. If I get the result of Print.Debug in the immediate window, I know the code worked at least till that line.

If you’re new to VBA coding, it may take you some time to be able to use the immediate window for debugging.

By default, the immediate window is not visible in the VB Editor. You can get it by using the keyboard shortcut Control + G (or can go to the View tab and click on ‘Immediate Window’).

Where to Add Code in the VB Editor
----------------------------------

I hope you now have a basic understanding of what VB Editor is and what all parts it has.

In this section of this tutorial, I will show you where to add a VBA code in the Visual Basic Editor.

There are two places where you can add the VBA code in Excel:

1.  The code window for an object. These objects can be a workbook, worksheet, User Form, etc.
2.  The code window of a module.

### Module Code Window Vs Object Code Window

Let me first quickly clear the difference between adding a code in a module vs adding a code in an object code window.

When you add a code to any of the objects, it’s dependent on some action of that object that will trigger that code. For example, if you want to unhide all the worksheets in a workbook as soon as you open that workbook, then the code would go in the ThisWorkbook object (which represents the workbook).

The trigger, in this case, is opening the workbook.

Similarly, if you want to protect a worksheet as soon as some other worksheet is activated, the code for that would go in the worksheet code window.

These triggers are called events and you can associate a code to be executed when an event occurs.

**Related**: [Learn more about Events in VBA](https://trumpexcel.com/vba-events/)
.

On the contrary, the code in the module needs to be executed either manually (or it can be called from other subroutines as well).

When you record a macro, Excel automatically creates a module and inserts the recorded macro code in it. Now if you have to run this code, you need to manually execute the macro.

### Adding VBA Code in Module

While recording a macro automatically creates a module and inserts the code in it, there are some limitations when using a macro recorder. For example, it can not use [loops](https://trumpexcel.com/vba-loops/)
 or [If Then Else](https://trumpexcel.com/if-then-else-vba/)
 conditions.

In such cases, it’s better to either copy and paste the code manually or write the code yourself.

A module can be used to hold the following types of VBA codes:

1.  **Declarations**: You can declare variables in a module. Declaring variables allows you to specify what type of data a variable can hold. You can declare a variable for a sub-routine only or for all sub-routines in the module (or all modules)
2.  **Subroutines (Procedures)**: This is the code that has the steps you want VBA to perform.
3.  **Function Procedures**: This is a code that returns a single value and you can use it to create custom functions (also called [User Defined Functions or UDFs in VBA](https://trumpexcel.com/user-defined-function-vba/)
    )

By default, a module is not a part of the workbook. You need to insert it first before using it.

#### Adding a Module in the VB Editor

Below are the steps to add a module:

1.  Right-click on any object of the workbook (in which you want the module).![Right click on any object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20422'%3E%3C/svg%3E)
2.  Hover the cursor on the Insert option.
3.  Click on Module.![Click on Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20421'%3E%3C/svg%3E)

This would instantly create a folder called Module and insert an object called Module 1. If you already have a module inserted, the above steps would insert another module.

![Inserted Module in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20297%20262'%3E%3C/svg%3E)

Once the module is inserted, you can double click on the module object in the Project Explorer and it will open the code window for it.

Now you can copy-paste the code or write it yourself.

#### Removing the Module

Below are the steps to remove a module in Excel VBA:

1.  Right-click on the module that you want to remove.
2.  Click on Remove Module option.![Remove Module for a Project in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20528'%3E%3C/svg%3E)
3.  In the dialog box that opens, click on No.![Prompt before a module is deleted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20208'%3E%3C/svg%3E)

Note: You can export a module before removing it. It gets saved as a .bas file and you can import it in some other project. To export a module, right-click on the module and click on ‘Export file’.

### Adding Code to the Object Code Window

To open the code window for an object, simply double-click on it.

When it opens, you can enter the code manually or copy-paste the code from other modules or from the internet.

Note that some of the objects allow you to choose the event for which you want to write the code.

For example, if you want to write a code for something to happen when selection is changed in the worksheet, you need to first select worksheets from the drop-down at the top left of the code window and then select the change event from the drop-down on the right.

![Selection Change Event in VBA Code Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20328'%3E%3C/svg%3E)

Note: These events are specific to the object. When you open the code window for a workbook, you will see the events related to the [workbook object](https://trumpexcel.com/vba-workbook/)
. When you open the code window for a worksheet, you will see the events related to the worksheet object.

Customizing the VB Editor
-------------------------

While the default settings of the Visual Basic Editor are good enough for most users, it does allow you to further customize the interface and a few functionalities.

In this section of the tutorial, I will show you all the options you have when customizing the VB Editor.

To customize the VB Editor environment, click Tools in the menu bar and then click on Options.

This would open the Options dialog box which will give you all the customization options in the VB Editor. The ‘Options’ dialog box has four tabs (as shown below) that have various customizations options for the Visual Basic Editor.

![Options to customize the Vb Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20440'%3E%3C/svg%3E)

Let’s quickly go through each of these tabs and the important options in each.

### Editor Tab

While the inbuilt settings work fine in most cases, let me still go through the options in this tab.

As you get more proficient working with VBA in Excel, you may want to customize the VB Editor using some of these options.

#### Auto Syntax Check

When working with VBA in Excel, as soon as you make a syntax error, you will be greeted by a pop-up dialog box (with some description about the error). Something as shown below:

![Auto Syntax Check in Visual Basic Editor Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20328'%3E%3C/svg%3E)

If you disable this option, this pop-up box will not appear even when you make a syntax error. However, there would be a change in color in the code text to indicate that there is an error.

If you’re a beginner, I recommend you keep this option enabled. As you get more experienced with coding, you may start finding these pop-up boxes irritating, and then you can disable this option.

#### Require Variable Declaration

This is one option I recommend enabling.

When you’re working with VBA, you would be using variables to hold different data types and objects.

When you enable this option, it automatically inserts the ‘Option Explicit’ statement at the top of the code window. This forces you to declare all the variables that you’re using in your code. If you don’t declare a variable and try to execute the code, it will show an error (as shown below).

![Varibale Not Declared Error in Excel VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20328'%3E%3C/svg%3E)

In the above case, I used the variable Var, but I didn’t declare it. So when I try to run the code, it shows an error.

This option is quite useful when you have a lot of variables. It often helps me find misspelled variables names as they are considered as undeclared and an error is shown.

Note: When you enable this option, it does not impact the existing modules.

#### Auto List Member

This option is quite useful as it helps you get a list of properties of methods for an object.

For example, if I want to [delete a worksheet (Sheet1](https://trumpexcel.com/delete-sheets-excel/)
), I need to use the line Sheet1.Delete.

While I am typing the code, as soon as I type the dot, it will show me all the methods and properties associated with the Worksheet object (as shown below).

![Autolist Member Option in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20328'%3E%3C/svg%3E)

Auto list feature is great as it allows you to:

*   Quickly select the property and method from the list and saves time
*   Shows you all the properties and methods which you may not be aware of
*   Avoid making spelling errors

This option is enabled by default and I recommend keeping it that way.

#### Auto Quick Info Options

When you type a function in Excel worksheet, it shows you some information about the function – such as the arguments it takes.

Similarly, when you type a function in VBA, it shows you some information (as shown below). But for that to happen, you need to make sure the Auto Quick Info option is enabled (which it is by default).

![Auto Quick Info Option in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20181'%3E%3C/svg%3E)

#### Auto Data Tips Options

When you’re going through your code line by line and place your cursor above a variable name, it will show you the value of the variable.

I find it quite useful when debugging the code or going through the code line by line which has loops in it.

![Auto Data Tips Option in Visual Basic Editor Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20205'%3E%3C/svg%3E)

In the above example, as soon as I put the cursor over the variable (var), it shows the value it holds.

This option is enabled by default and I recommend you keep it that way.

### Auto Indent

Since VBA codes can get long and messy, using [indentation](https://trumpexcel.com/how-to-indent-in-excel/)
 increases the readability of the code.

When writing code, you can indent using the tab key.

This option ensures that when you are done with the indented line and hit enter, the next line doesn’t start from the very beginning, but has the same indentation as the previous line.

![Indentation enabled in the VB Editor code windows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20240'%3E%3C/svg%3E)

In the above example, after I write the Debug.Print line and hit enter, it will start right below it (with the same indentation level).

I find this option useful and turning this off would mean manually indenting each line in a block of code that I want indented.

You can change the indentation value if you want. I keep it at the default value.

#### Drag and Drop Text Editing

When this option is enabled, it allows you to select a block of code and drag and drop it.

It saves time as you don’t have to first cut and then paste it. You can simply select and drag it.

This option is enabled by default and I recommend you keep it that way.

#### Default to Full Module View

When this option is enabled, you will be able to see all the procedures in a module in one single scrollable list.

If you disable this option, you will only be able to see one module at a time. You will have to make a selection of the module you want to see from the drop-down at the top right of the code window.

This option is enabled by default and I recommend keeping it that way.

One reason you may want to disable it when you have multiple procedures that are huge and scrolling across these is taking time, or when you have a lot of procedures and you want to quickly find it instead of wasting time in scrolling.

#### Procedure Separator

When this option is enabled, you will see a line (a kind of divider) between two procedures.

I find this useful as it visually shows when one procedure ends and the other one starts.

![Procedure Separator Option in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20373'%3E%3C/svg%3E)

It’s enabled by default and I recommend keeping it that way.

### Editor Format Tab

With the options in the Editor Format tab, you can customize the way your code looks in the code window.

Personally, I keep all the default options as I am fine with it. If you want, you can tweak this based on your preference.

To make a change, you need to first select an option in the Code Colors box. Once an option is selected, you can modify the foreground, background, and indicator color for it.

The font type and font size can also be set in this tab. It’s recommended to use a fixed-width font such as Courier New, as it makes the code more readable.

Note that the font type and size setting will remain the same for all code types (i.e., all the code types shown in the code color box).

Below is an image where I have selected Breakpoint, and I can change the formatting of it.

![Editor Format Options in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20440'%3E%3C/svg%3E)

Note: The Margin Indicator Bar option when enabled shows a little margin bar to the left of the code. It’s helpful as it shows useful indicators when executing the code. In the above example, when you set a breakpoint, it will automatically show a red dot to the left of the line in the margin bar. Alternatively, to set a breakpoint, you can simply click on the margin bar on the left of the code line that you want as the breakpoint.

By default, Margin Indicator Bar is enabled and I recommend keeping it that way.

One of my [VBA course](https://trumpexcel.com/excel-vba-jetpack-course/)
 students found this customization options useful and she was color blind. Using the options here, she was able to set the color and formats that made it easy for her to work with VBA.

### General Tab

The General tab has many options but you don’t need to change any of it.

I recommend you keep all the options as is.

One important option to know about in this tab is Error Handling.

By default, ‘Break on Unhandled Errors’ is selected and I recommend keeping it that way.

This option means that if your code encounters an error, and you have not handled that error in your code already, then it will break and stop. But if you have addressed the error (such as by using On Error Resume Next or On Error Goto options), then it will not break (as the errors are not unhandled).

#### Docking Tab

In this tab, you can specify which windows you want to get docked.

Docking means that you can fix the position of a window (such as project explorer or the Properties window) so that it doesn’t float around and you can view all the different windows at the same time.

If you don’t dock, you will be able to view one window at a time in full-screen mode and will have to switch to the other one.

I recommend keeping the default settings.

**Other Excel tutorials you may like:**

*   [How to Remove Macros From an Excel Workbook](https://trumpexcel.com/remove-macros-from-excel/)
    
*   [Comments in Excel VBA (Add, Remove, Block Commenting)](https://trumpexcel.com/comments-excel-vba/)
    
*   [Using Active Cell in VBA in Excel (Examples)](https://trumpexcel.com/active-cell-vba-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Visual Basic Editor – How to Open and Use it in Excel”
---------------------------------------------------------------------

1.  nicely done. thanks
    
    [Reply](https://trumpexcel.com/visual-basic-editor/#comment-14911)
    
2.  Very educational topics.
    
    [Reply](https://trumpexcel.com/visual-basic-editor/#comment-14626)
    
3.  I found this tutorial to be very helpful. Thank you.
    
    [Reply](https://trumpexcel.com/visual-basic-editor/#comment-14194)
    
4.  very nice
    
    [Reply](https://trumpexcel.com/visual-basic-editor/#comment-11967)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/visual-basic-editor/#respond)

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