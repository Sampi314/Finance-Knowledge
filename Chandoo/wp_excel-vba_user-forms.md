# User Forms & Controls in VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-vba/user-forms

---

[![Excel VBA - Tutorials, Examples, Information & Resources](https://cache.chandoo.org/logos/excel-vba.png "Excel VBA - Tutorials, Examples, Information & Resources")](https://chandoo.org/wp/excel-vba/)

[**Excel VBA**](https://chandoo.org/wp/excel-vba/)
 > [Examples](https://chandoo.org/wp/excel-vba/examples/)
 [Videos](https://chandoo.org/wp/excel-vba/videos/)
 [VBA Tips](https://chandoo.org/wp/excel-vba/vba-tips/)
 [User Forms & Controls](https://chandoo.org/wp/excel-vba/user-forms/)
 [Books](https://chandoo.org/wp/excel-vba/books/)
 [References](https://chandoo.org/wp/excel-vba/references/)
 [Training](https://chandoo.org/wp/excel-vba/training/)
 [FREE Newsletter](https://chandoo.org/wp/excel-vba/newsletter/)

User Forms & Controls in VBA
============================

User forms are custom user interface screens that you can develop in VBA to interact with your users. An example user form is shown below.

![Example UserForm - Excel VBA](https://cache.chandoo.org/media/example-user-form-in-vba.png)

Learn how to use various form controls & user form features in this section.

|     |     |
| --- | --- |
| **In this page**<br><br>[What are Form Controls?](https://chandoo.org/wp/excel-vba/user-forms/#form_controls)<br>  <br>[Using Excel Form Controls](https://chandoo.org/wp/excel-vba/user-forms/#using_form_controls)<br>  <br>[Different Form Controls & What they do](https://chandoo.org/wp/excel-vba/user-forms/#various_controls)<br>  <br>[What are Events](https://chandoo.org/wp/excel-vba/user-forms/#events)<br>  <br>[What are Active-X Controls?](https://chandoo.org/wp/excel-vba/user-forms/#active-x_controls)<br>  <br>[Using Form Controls inside Excel Workbooks](https://chandoo.org/wp/excel-vba/user-forms/#form_controls_in_excel)<br>  <br>[VBA User Form Examples](https://chandoo.org/wp/excel-vba/user-forms/#user_form_examples)<br>  <br>[References on Form Controls & User Forms](https://chandoo.org/wp/excel-vba/user-forms/#references) | **More on Excel VBA**<br><br>**[Excel VBA Homepage](http://chandoo.org/wp/excel-vba/)<br>**  <br>[Excel VBA Examples](http://chandoo.org/wp/excel-vba/examples/)<br>  <br>[Video Tutorials on Excel VBA, Macros](http://chandoo.org/wp/excel-vba/videos/)<br>  <br>[Excel VBA Tips](http://chandoo.org/wp/excel-vba/vba-tips/)<br>  <br>_User Forms & Controls in VBA_  <br>[Books on Excel VBA](http://chandoo.org/wp/excel-vba/books/)<br>  <br>[References on Excel VBA](http://chandoo.org/wp/excel-vba/references/)<br>  <br>[Training on Excel VBA](http://chandoo.org/wp/excel-vba/training/)<br>  <br>[Join our Excel Newsletter](http://chandoo.org/wp/excel-vba/newsletter/) |

What are Form Controls?
-----------------------

Form Controls are objects which you can place onto an Excel Worksheet or User Forms, which give you the functionality to interact with your data.

You can use these controls to help select data. For example, drop-down boxes, list boxes, spinners, and scroll bars are useful for selecting items from a list. Option Buttons and Check Boxes allow selection of various options. Buttons allow execution of VBA code.

You can place form controls on user forms (created from Visual Basic Editor) or inside Excel worksheets.

By adding form controls to user forms, we can tell Excel how the value entered in that should be treated. This is done a special type of macros called as _**Events**_.

By adding a control to a worksheet and linking it to a cell, you can return a numeric value for the current position of the control. You can use that numeric value in conjunction with the Offset, Index or other worksheet functions to return values from lists.  

Using Excel Form Controls
-------------------------

You can use form controls in 2 contexts – (1) in User Forms (2) in regular Excel worksheets.

### Using Form Controls in User Forms

To use form controls, this is the process we need to follow.

1.  Go to Visual Basic Editor (ALT+F11)
2.  Insert UserForm
3.  Select the UserForm, you should see Toolbox with all userform controls.
4.  If the Toolbox is not displayed, you can enable if from View menu.
5.  Select any userform control and draw it on the userform.
6.  Design the form as per your desire.
7.  Change captions & settings of each control by using Properties window
8.  Tip: You can adjust properties of multiple controls by selecting them all and then making changes to their properties.

### Creating your first UserForm – Demo

See this short animated demo to understand how to create & design a UserForm.  
  

Different Form Controls & What they do?
---------------------------------------

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
| Scroll bar | Allow Horizontal or Vertical scrolling | Increases or decreases a value by a fixed amount. Can be linked to a cell. |
| Spin Button | Increment/decrement a value by a fixed amount | Increases or decreases a value in steps by a fixed amount. Can be linked to a cell. |

For more information, read [**Form Controls & how to use them in the context of Excel**](http://chandoo.org/wp/2011/03/30/form-controls/)
.  

What are Events?
----------------

Events are a special type of Macros (VBA instructions) that run whenever user interacts with userform controls. For example, you can write an event to tell Excel what to do **_whenever user clicks on the submit button._** Each userform controls supports various events.  

What are Active-x Controls?
---------------------------

Active X controls are like Form Controls on Steroids in that they have a much wider range of properties than Form Controls.

They also have much better ties to VBA in terms of programmability and have a number of events that can be accessed programmatically.

The main limitation of Active X controls are that they use a Microsoft Active X component. This means that if you are sharing your workbook with an Apple Mac user using Excel for Mac  these functions wont be available as Active X isn’t available on that Platform.

Workbooks with Form Controls will happily work on a an Apple Mac.  

Using Form Controls inside Excel Workbook
-----------------------------------------

Using Form controls inside Excel is a great way to add interactivity to your workbooks. Below you can see one such example.

![Excel Dynamic Chart made with Form Controls](https://img.chandoo.org/c/dynamic-chart-with-check-boxes-demo.gif)

We, at Chandoo.org have lots of examples & detailed tutorials on these. Please visit these pages for more information on this.

*   [Introduction to Form Controls & how to use them in Excel](http://chandoo.org/wp/2011/03/30/form-controls/)
    
*   [Excel Dynamic Charts made with Form Controls](http://chandoo.org/wp/tag/dynamic-charts/)
     \[lots of examples\]
*   [Examples on Excel Form Controls](http://chandoo.org/wp/tag/form-controls/)
    

VBA User Form Examples
----------------------

_Please check back again. We are adding new examples to this area._  

References on Excel VBA UserForms & Controls
--------------------------------------------

Please read thru these references to learn more about UserForms & Form Controls in Excel VBA.

*   [Introduction & Overview of Form Controls & Active-x Controls](http://office.microsoft.com/en-us/excel-help/overview-of-forms-form-controls-and-activex-controls-on-a-worksheet-HA010237663.aspx)
    
*   [Excel User Form Example](http://www.excel-vba-easy.com/vba-userform-excel-vba.html)
     \[excel-vba-easy.com\]
*   [Excel User Form Code Samples](http://www.ozgrid.com/VBA/UserForms.htm)
     \[ozgrid.com\]
*   [Extending UsefForm capabilities with Windows API](http://www.cpearson.com/excel/formcontrol.aspx)
     \[cpearson.com\]
*   [UserForm Tips](http://www.j-walk.com/ss/excel/tips/userformtips.htm)
     \[j-walk.com\]
*   [Create an Excel UserForm](http://www.contextures.com/xlUserForm01.html)
     \[contextures.com\]

[^ Go to Top](https://chandoo.org/wp/excel-vba/user-forms/#top)
 [**Excel VBA**](https://chandoo.org/wp/excel-vba/)
 [Examples](https://chandoo.org/wp/excel-vba/examples/)
 [Videos](https://chandoo.org/wp/excel-vba/videos/)
 [VBA Tips](https://chandoo.org/wp/excel-vba/vba-tips/)
 [User Forms & Controls](https://chandoo.org/wp/excel-vba/user-forms/)
 [Books](https://chandoo.org/wp/excel-vba/books/)
 [References](https://chandoo.org/wp/excel-vba/references/)
 [Training](https://chandoo.org/wp/excel-vba/training/)
 [FREE Newsletter](https://chandoo.org/wp/excel-vba/newsletter/)

[![Excel VBA - Tutorials, Examples, Information & Resources](https://cache.chandoo.org/logos/excel-vba.png "Excel VBA - Tutorials, Examples, Information & Resources")](https://chandoo.org/wp/excel-vba/)