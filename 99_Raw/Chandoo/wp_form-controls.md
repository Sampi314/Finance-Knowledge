# Form Controls, Adding Interactivity to your Excel Worksheets

**Source:** https://chandoo.org/wp/form-controls

---

*   [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Form Controls – Adding Interactivity to Your Worksheets
=======================================================

*   Last updated on January 7, 2013

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

**Form Controls**
-----------------

### **What Are Form Controls?**

Form Controls are objects which you can place onto an Excel Worksheet which give you the functionality to interact with your models data.

You can use these controls on worksheets to help select data. For example, drop-down boxes, list boxes, spinners, and scroll bars are useful for selecting items from a list. Option Buttons and Check Boxes allow selection of various options. Buttons allow execution of VBA code.

By adding a control to a worksheet and linking it to a cell, you can return a numeric value for the current position of the control. You can use that numeric value in conjunction with the Offset, Index or other worksheet functions to return values from lists.

**Use below links to quickly learn about Form Controls:**

*   [What are form controls & introduction](https://chandoo.org/wp/form-controls/#definition)
    
*   [Button Control](https://chandoo.org/wp/form-controls/#button)
    
*   [Label Control](https://chandoo.org/wp/form-controls/#label)
    
*   [Check box Control](https://chandoo.org/wp/form-controls/#check-box)
    
*   [Option Button Control](https://chandoo.org/wp/form-controls/#option-button)
    
*   [List box Control](https://chandoo.org/wp/form-controls/#list-box)
    
*   [Combo box Control](https://chandoo.org/wp/form-controls/#combo-box)
    
*   [Spin Button Control](https://chandoo.org/wp/form-controls/#spin-button)
    
*   [Scroll bar Control](https://chandoo.org/wp/form-controls/#scroll-bar)
    
*   [Group box Controlg](https://chandoo.org/wp/form-controls/#group-box)
    
*   [Using Form Controls – techniques & examples](https://chandoo.org/wp/form-controls/#usages)
    
*   [Other Controls in Excel](https://chandoo.org/wp/form-controls/#other-controls)
    

### **Where Are Form Controls?**

Form Controls are located on the Developer Tab under Insert Form Control.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-1.jpg "Form Control 1")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-1.jpg)

**PS: If you do not have developer tab, [learn how to enable it](http://chandoo.org/wp/2009/05/26/excel-2007-productivity-tips/ "Where is Developer Tab")
.**

You will notice 2 types of Form Controls, being Form Controls and Active X controls.

This post will only be dealing with Form Controls. The Active X controls, similarities and differences will be discussed towards the end of the post.

### How Do I Insert a Form Control

To Insert a Form Control goto the Form Control Menu and click on the Form Control you want to insert.

Now click on the worksheet in the location you want your form control.

Don’t worry about the location or size you can change those later.

### **What Are The Different Form Controls?**

There are several types of Form Controls offering a range of interactivity from a simple display through to interactive controls which allow multiple selection or interactive selection of values.

|     |     |     |
| --- | --- | --- |
| **Control Name** | **Description** | **Function** |
| Button | Push Button | Executes a macro |
| Check Box | Allow selection of non-exclusive options | Multiple On/Off options |
| Combo Box | Drop Down selection Box | Select items from a Drop down list |
| Group Box | Layout element which groups common elements | Nil |
| Label | A Text label | Can be static or linked to a cell |
| List Box | Fixed selection box | Select items from a list |
| Option Button | Allow selection of exclusive options | Exclusive Single On/Off option |
| Scroll bar | Allow Horizontal or Vertical scrolling | Increases or decreases a cells value by a fixed amount |
| Spin Button | Increment/decrement a value by a fixed amount | Increases or decreases a cells in steps by a fixed amount |

These are discussed individually below

**Form Control Types**
----------------------

   

### **Button (Form Control)**

The Button Form Control is as its name suggests simply a Button.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-2.png "Form Control 2")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-2.png)

Pressing the Button allows execution of a macro.

The Button has no other controls.

Button Text

You can right click on the button and change the buttons Text (**Edit Text**) and enter the text you want displayed on the button.

The Button’s text can be linked to a cell, select the Button, In the formula Bar enter a link to a cell. eg: =$C$3 and accept. The Button’s text will now change as the contents of the cell C3 change.

You can change the Text Style including Font, Color and Text Direction using the Format Control  (Ctrl 1) option.

Assign Macro

Right click on the Button and select **Assign Macro**

The Assign Macro dialog will pop up.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-3.png "Form Control 3")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-3.png)

Select the macro you want to assign to the button.  

### **Label (Form Control)**

**[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-4.png "Form Control 4")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-4.png)
**

The Label Form Control is also as its name suggests simply a Label.

The Label will display text either fixed or from a linked cell

You can right click on the button and change the buttons text (**Edit Text**).

The Button’s text can be linked to a cell, select the Button, In the formula Bar enter a link to a cell

eg: =$C$3 and accept. The Button’s text will now change as the contents of the cell C3 change.

Unlike the Button you cannot change the Text Style, Font, Color or Text Direction.

Typically a label is put in front of another Control to explain or add a title to the control.

Labels would rarely be used on a Worksheet as a label as they have limited text format properties.

Users would be better served using either cell text or a Text Box where full text formatting is allowed.

Labels come into use when setting up custom Dialog Forms which are used by VBA applications for custom data entry or other uses.

   

### **Check Box (Form Control)**

The Check Box form Control allows selection of a number of non-exclusive options.

**[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-5.png "Form Control 5")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-5.png)
**

That is any number of Check Box controls may be implemented and they independently be on or off and have no relationship to each other.

The Check Box Form Control returns the value indicating its status, either True (selected) or False (not selected),  to a linked cell.

To link a Format Control to a cell, Right Click the Format Control and select **Format Control…**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-6.png "Form Control 6")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-6.png)

### **Option Button (Form Control)**

The Option Button form Control allows the selection of an exclusive option from a number of alternatives.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-7.png "Form Control 7")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-7.png)

That is only one Option Button Form Control may be selected at a time, the remainder are automatically turned off.

The Option Button Form Control returns the value of the Option Button indicating its status to a linked cell.

In the Example above the Option Buttons are linked to cell E2.

You only need link one Option Button to cell E2, Excel automatically links the remaining option buttons to teh same cell.

Selecting a Different Option Button automatically deselelects the other Option Buttons and changes the linked cells value

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-7a.png "Form Control 7a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-7a.png)

### **List Box (Form Control)**

The List box allows the selection of one or more items from a list.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-8.png "Form Control 8")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-8.png)

The list is sourced from a Range of cells in the above case it was F2:F17.

The List Form Control returns an Index Number or position of the selected item to the Cell Link, 5 in the example above.

The Input Range and Cell Link are setup by Right Clicking the control and select **Format Control…**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-8a.png "Form Control 8a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-8a.png)

The Number of items visible in the list box is determined by the size of the list box

If there are more items than will fit in the list box then a scroll bar is automatically added to the list box to enable there selection.

### **Combo Box (Form Control)**

The Combo Box allows the selection of one or more items from a drop down list.

The Combo Box use is similar to the list box except that it has a drop down selection list instead of a fixed length selection list.

**[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9a.png "Form Control 9a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9a.png)
  
**

The list is sourced from a Range of cells in the example below it was F2:F17.

The List Form Control returns an Index Number or position of the selected item to the Cell Link B10, 9 in the example below.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9b.png "Form Control 9b")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9b.png)

The Input Range, Cell Link and size of the Drtop Down Box are setup by Right Clicking the control and select **Format Control…**

****[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9c.png "Form Control 9c")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-9c.png)
****  

### **Spin Button (Form Control)**

The Spin Button is a simple toggle button that allows the increase or decrease of a linked cells value by a certain pre-defined amount.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-10a.png "Form Control 10a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-10a.png)

The Cell Link and Lower, Upper Limits and Step Size parameters are setup by Right Clicking the control and select **Format Control…**

The Lower, Upper Limits and Step Size must be Integers. If you want to increase a cell by fractional amounts you will need to for example set the range from 0 to 1000 in steps of 1 and then devide the linked cell by 10 which will give a Range of 0 to 100 in steps of 0.1

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-10b.png "Form Control 10b")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-10b.png)

### **Scroll Bar (Form Control)**

The Scroll Bar Form Control often referred to as a Slider is a simple linear slider that allows the increase or decrease of a linked cells value by sliding a bar either left/right or up/down.

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-11a.png "Form Control 11a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-11a.png)

Scroll Bars can be placed either Horizontally or Vertically by dragging the corner.

Scroll bars are incremented by the Step Size by clicking the ends of the bars or dragging the slider or by a Page Jump Size by using Page up\[/down or clicking either side of the slider bar.\
\
The Cell Link, Lower, Upper Limits, Incremental Change and Page Change parameters are setup by Right Clicking the control and select **Format Control…**\
\
[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-11b.png "Form Control 11b")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-11b.png)\
\
The Lower, Upper Limits, Incremental Change and Page Change must be Integers. If you want to increase a cell by fractional amounts you will need to for example set the range from 0 to 1000 in steps of 1 and then devide the linked cell by 10 which will give a Range of 0 to 100 in steps of 0.1  \
\
### **Group Box (Form Control)**\
\
The Group Box Form Control isn’t really a Form Control at all, as it allows no interactivity.\
\
What it is used for is grouping similar controls so that functional groups of controls can be maintained and the users flow is directed around a form.\
\
[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-12.png "Form Control 12")](https://chandoo.org/wp/wp-content/uploads/2011/03/Form-Control-12.png)\
\
**Using the Form Controls**\
---------------------------\
\
### **General Use**\
\
The use of the information from a form control is limited by your imagination.\
\
Typical uses are\
\
*   Selecting items for a chart\
*   Selecting data sets\
*   Moving data sets\
*   Adjusting values in a model\
\
As described in each of the above Form Controls is that the Form Controls do not return a value directly from a list, they all return either a number or an index number relative to the position of the item in a list.\
\
Examples of all the Form Controls and examples of their use can be found in the attached file:\
\
[Excel 2003 Examples](http://rapidshare.com/files/455058938/Form_Controls.xls "Form Controls - Excel 2003 Examples")\
 or [Excel 2007+ Examples](http://rapidshare.com/files/455058939/Form_Controls.xlsm "Form Controls - Excel 2007+ Examples")\
\
or\
\
Have a browse through the dashboards presented during [Dashboard Week](http://chandoo.org/wp/tag/dashboard-week/ "Dashboard Week")\
\
or\
\
For some Extreme Examples of Spreadsheet Interactivity using Form Controls and a little bit of VBA code:\
\
[ExcelHero.com](http://www.excelhero.com/blog/2010/05/animated-business-chart.html "ExcelHero.com")\
\
**Running Macros**\
\
Apart from the Button Form Control whose only purpose is to Run Macro’s, all Form Controls can be linked to a Macro.\
\
This is done by Right Clicking on the Form Control and selecting Assign Macro.\
\
It is worth noting that the macro is only executed after the control is released.\
\
EG: If you have a macro linked to a Spin Button, If the Spin Button is held down and hence repeatedly increments its value, the macro will only be executed after the control is released.\
\
### **Moving and Resizing Form Controls**\
\
You can move and resize form controls as with all other worksheet Objects.\
\
Select the form control by right clicking on it\
\
Use the handles to resize or drag the edges to move the controls\
\
**Hint:** You can use Alt while dragging or resizing to snap the control to cell boundaries.\
\
### **3D, Printing & Locking Form Controls**\
\
You can lock Form Controls as well as enable them to be printed or not\
\
Right Clicking the control and select **Format Control…**\
\
Use the Size, Protection and Properties Tabs as required.\
\
The 3D option enables a 3D version of the Control instead of a flat control, which can add a bit of sparkle in some instances.\
\
### **Limitations of Form Controls**\
\
Form controls offer a limited set of functions but do those functions very well.\
\
Limitations are Form Controls:\
\
*   Form Controls can only increase or decrease by integer numbers\
*   Form Controls only return the index of an item in a list\
*   Form Controls have limited format properties (Font, Color etc)\
\
### **What are the Active X Controls**\
\
Active X controls are like Form Controls on Steroids in that they have a much wider range of properties than Form Controls.\
\
They also have much better ties to VBA in terms of programmability and have a number of events that can be accessed programmatically.\
\
The main limitation of Active X controls are that they use a Microsft Active X component. This means that if you are sharing your workbook with an Apple Mac user using Excel for Mac  these functions wont be available as Active X isn’t avilable on that Platform.\
\
Workbooks with Form Controls will happily work on a an Apple Mac.\
\
**Other Controls Available in Excel  \
**\
----------------------------------------\
\
A number of other Excel objects can be used to add interactivity to your worksheets.\
\
Shapes\
\
These include:\
\
*   Shapes\
*   Charts\
*   Text Boxes\
*   Word Art\
\
All these can have macro’s linked to them which effectively act the same as a Button Form Control without the moving button effect.\
\
A stunning example of using Text Boxes was recently posted at: [The Grammy Bump Chart](http://chandoo.org/wp/2011/02/22/the-grammy-bump-chart-in-excel/ "Grammy Bump Chart")\
\
Where the Artists Stats Box (Top Left of Chart) is using several Text Boxes linked to cells to show the Selected Artsists Statistics.\
\
HyperLinks\
\
Inserting Hyperlinks at stratgic locations throughout worksheets provides a great way to simplify navigation around pages and between pages\
\
Other Links\
-----------\
\
[http://office.microsoft.com/en-us/excel-help/overview-of-forms-form-controls-and-activex-controls-on-a-worksheet-HA010237663.aspx](http://office.microsoft.com/en-us/excel-help/overview-of-forms-form-controls-and-activex-controls-on-a-worksheet-HA010237663.aspx "Overview of Form Controls")\
\
Where have you used Form Controls ?  \
\
--------------------------------------\
\
Where have you used Form Controls?\
\
Let us know in the comments below:\
\
Facebook\
\
Twitter\
\
LinkedIn\
\
**Share this tip** with your colleagues\
\
![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)\
\
### Get FREE Excel + Power BI Tips\
\
Simple, fun and useful emails, once per week.  \
  \
**Learn & be awesome.**\
\
*   [104 Comments](https://chandoo.org/wp/form-controls/#comments)\
    \
*   [Ask a question or say something...](https://chandoo.org/wp/form-controls/#respond)\
    \
*   Tagged under [Button](https://chandoo.org/wp/tag/button/)\
    , [Check Box](https://chandoo.org/wp/tag/check-box/)\
    , [combo box](https://chandoo.org/wp/tag/combo-box/)\
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)\
    , [Form Control](https://chandoo.org/wp/tag/form-control/)\
    , [Group Box](https://chandoo.org/wp/tag/group-box/)\
    , [Label](https://chandoo.org/wp/tag/label/)\
    , [List Box](https://chandoo.org/wp/tag/list-box/)\
    , [Option Button](https://chandoo.org/wp/tag/option-button/)\
    , [Scroll Bar](https://chandoo.org/wp/tag/scroll-bar/)\
    , [Slider](https://chandoo.org/wp/tag/slider/)\
    , [Spin Button](https://chandoo.org/wp/tag/spin-button/)\
    \
*   Category: [excel apps](https://chandoo.org/wp/category/excel-apps/)\
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)\
    , [Huis](https://chandoo.org/wp/category/huis/)\
    , [Learn Excel](https://chandoo.org/wp/category/excel/)\
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)\
    \
\
[PrevPreviousLearning Dashboards? – Go thru these 33 Recommended Resources](https://chandoo.org/wp/resources-for-making-dashboards/)\
\
[NextBeam Me Up Scotty – Excel HyperlinksNext](https://chandoo.org/wp/excel-hyperlinks/)\
\
![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)\
\
### Welcome to Chandoo.org\
\
Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  \
  \
[Read my story](https://chandoo.org/wp/about/)\
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)\
\
[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)\
\
[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)\
\
[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)\
\
Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.\
\
![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)\
\
Rebekah S\
\
Reporting Analyst\
\
[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)\
\
[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)\
\
[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)\
\
From simple to complex, there is a formula for every occasion. Check out the list now.\
\
[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)\
\
[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)\
\
Calendars, invoices, trackers and much more. All free, fun and fantastic.\
\
[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)\
\
[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)\
\
Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.\
\
[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)\
\
[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)\
\
Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.\
\
Recent Articles on Chandoo.org\
\
[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.\
\
[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)\
\
### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)\
\
[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)\
\
### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)\
\
[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
Best of the lot\
\
*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)\
    \
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)\
    \
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)\
    \
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)\
    \
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)\
    \
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)\
    \
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)\
    \
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)\
    \
\
Related Tips\
------------\
\
[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
Learn Excel\
\
### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)\
\
[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
Excel Challenges\
\
### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)\
\
[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
Excel Howtos\
\
### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)\
\
[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)\
\
Excel Howtos\
\
### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)\
\
[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)\
\
Excel Howtos\
\
### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)\
\
[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)\
\
Excel Howtos\
\
### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)\
\
### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”\
\
1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:\
    \
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)\
    \
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.\
    \
    [Reply](https://chandoo.org/wp/form-controls/#comment-2107616)\
    \
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)\
         says:\
        \
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)\
        \
        Good question. You can check for the =0 as countifs result. for example,  \
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  \
        should work in this case.\
        \
        PS: I have added this example to the article now.\
        \
        [Reply](https://chandoo.org/wp/form-controls/#comment-2107623)\
        \
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)\
     says:\
    \
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)\
    \
    Hi there!\
    \
    Could i check if there was a way to return certain fields of the table only?\
    \
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).\
    \
    [Reply](https://chandoo.org/wp/form-controls/#comment-2122498)\
    \
\
### Leave a Reply\
\
[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)\
\
 Name (required)\
\
 Mail (will not be published) (required)\
\
 Website\
\
  \
\
 Notify me of when new comments are posted via e-mail\
\
Δ