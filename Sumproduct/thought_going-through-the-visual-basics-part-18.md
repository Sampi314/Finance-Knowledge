# Going Through the Visual Basics – Part 18

**Source:** https://sumproduct.com/thought/going-through-the-visual-basics-part-18/

---

[Home](https://sumproduct.com/)

\> Going Through the Visual Basics – Part 18

*   January 4, 2019

Going Through the Visual Basics – Part 18
=========================================

VBA Blogs: Going Through the Visual Basics – Part 18
====================================================

4 January 2019

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog marks the Event-ful end of this series…_

While most VBA scripts tend to be triggered by buttons or commands that a user can execute, it can also be programmed to run when a particular action is triggered elsewhere in the Excel workbook. We referred to this earlier in the series and will now address the process of creating these events.

These triggers can be found in the VBA Editor and navigating to a Sheet or to **ThisWorkbook**.

**  
Worksheet events**

There are a couple of key worksheet events generally used:

*   **Activate**
*   **SelectionChange**.

The Activate event will trigger whenever the worksheet in question is activated (_e.g._ if a user clicks on the worksheet tab in Excel).

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-698.jpg)

This sort of event can be used to trigger an update or clean-up of data on a sheet. It is commonly used to refresh PivotTables when a sheet is selected, with the code cycling through available PivotTables and refreshing each one.

The **SelectionChange** triggers whenever a new cell is selected within the worksheet, _e.g._ when a cell is clicked on or when the selection range is expanded or reduced. This event is a bit different, in that there is also an additional parameter that becomes available, initially referred to as “ByVal Target as Range”. This allows you to pass the selected area through to the VBA script being run. An example of this can be found in a previous blog that we’ve written [here](https://www.sumproduct.com/blog/article/vba-blogs/painting-with-excel)
.

**Workbook events**

There are several key workbook events that are commonly used in practice:

*   **Activate**
*   **BeforeClose**
*   **BeforeSave**
*   **Open**.

In particular, the **Open** event is commonly used to set up disclaimer messages, user guides and instructions, or for model clean-up. However, this relies upon the user enabling macros prior to the macro attempts to run. For a more robust process, any clean-up or disclaimer script should be written prior to the file being saved, so that any user will be required to respond to the disclaimer before the file can be used.

![](<Base64-Image-Removed>)

This is where the **BeforeSave** event is particularly useful. The event is triggered upon a **Save** or **SaveAs** command, and allows users to run any clean-up prior to the file being saved. The macro can be set to restore the file after it has been saved, so that the user won’t need to go through the disclaimer process, resulting in a seamless save action.

**Disabling events**

While events can be useful, at times you may need to save the file as part of another macro script, assuming that the event will not be triggered. In these instances, you need to include the command:

Application.EnableEvents = False 

This will prevent any events from being triggered until you restore the actions using:

Application.EnableEvents = True

If you decide to switch off events at the start of your macro to improve the speed and efficiency of your macro run, remember to switch it back on subsequently after your macro finishes running.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/going-through-the-visual-basics-part-18/#0)
    
*   [Register](https://sumproduct.com/thought/going-through-the-visual-basics-part-18/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/going-through-the-visual-basics-part-18/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/going-through-the-visual-basics-part-18/#0)

[](https://sumproduct.com/thought/going-through-the-visual-basics-part-18/#0 "close")

top