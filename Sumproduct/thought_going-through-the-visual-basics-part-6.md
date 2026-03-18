# Going Through the Visual Basics – Part 6

**Source:** https://sumproduct.com/thought/going-through-the-visual-basics-part-6/

---

[Home](https://sumproduct.com/)

\> Going Through the Visual Basics – Part 6

*   September 14, 2018

Going Through the Visual Basics – Part 6
========================================

VBA Blogs: Going Through the Visual Basics – Part 6
===================================================

14 September 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at running a macro._

There are a few ways to run a macro:

1.  From the ‘Macro’ dialog box
2.  Running it from the VBA Editor
3.  Using a predefined keyboard shortcut
4.  Anchoring the macro to a form control
5.  Setting it to automatically run on a specific event.

Let’s consider each of these scenarios.

**1\. From the ‘Macro’ dialog box**

Select the intended macro from the list in the dialog (**ALT + L + PM**) and hit the ‘Run’ button:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-691.jpg)

It’s not rocket science.

**2\. Running it from the VBA Editor**

In the VBA Editor (**ALT + F11**), there is a tool bar at the top:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-797.jpg)

The ‘Run Sub / UserForm (Shortcut: **F5**)’ button looks similar to the ‘Play’ button on most electronic devices. Ensure the cursor is in the Code Window _within the procedure_ to be run. If the cursor is not within any procedure then the ‘Macro’ dialog box will pop up to prompt to select one to run.

**3\. Using a predefined shortcut  
**Initially when recording the macro, the option to create a shortcut key is presented. This can be set after the fact by clicking on the ‘Options…’ button on the ‘Macro’ dialog box:

![](https://sumproduct.com/wp-content/uploads/2025/06/f1140ff857fc3b6f5f97a6a24f4a6fc7-714.jpg)

The ‘Macro Options’ dialog box will appear:

![](https://sumproduct.com/wp-content/uploads/2025/06/72aa864d2854c6fefb1083fba0ab5792-666.jpg)

Any alphanumeric key can be used to create shortcut key. **SHIFT** can also be combined as well, by holding shift in conjunction with the key.

![](https://sumproduct.com/wp-content/uploads/2025/06/36776d1da4d05b45bb5a5d09375f407c-570.jpg)

However, macro shortcut keys take precedence over Excel. This means that if an action is assigned to a keyboard shortcut that is already assigned to Excel, this keyboard shortcut replaces the Access key assignment. For example, **CTRL + C** is the keyboard shortcut for the ‘Copy’ command; if we assign this keyboard shortcut to a macro, Excel will run the macro instead of the ‘Copy’ command.

**4\. Anchoring the macro to a form control**

In the ‘Developer’ tab of the Ribbon, there is the ‘Controls’ category:

![](https://sumproduct.com/wp-content/uploads/2025/06/23912d3b1671861e02bebcd5183f1607-499.jpg)

Clicking on ‘Insert’, a drop down will appear of different things that can be included to create UserForms.

![](https://sumproduct.com/wp-content/uploads/2025/06/6f49c288a0d88a66b427eaf4ece923d6-426.jpg)

There are two types of controls: Form Controls and ActiveX controls:

*   Form controls are built in to Excel whereas ActiveX controls are loaded separately
*   ActiveX controls allow for more flexible design and should be used when the job just can’t be done with a basic Forms control.

However, many users’ computers won’t trust ActiveX by default, therefore ActiveX controls are usually disabled and may be required to be manually added to the Trust Center. One more thing to note is that ActiveX is a Microsoft-based technology and is not supported on the Mac. However, this may change very soon.

Bearing all this in mind, click on the first ‘Form Control’ button:

![](<Base64-Image-Removed>)

The cursor will turn into a cross and draw a rectangle with like when inserting shapes. An ‘Assign Macro’ dialog will appear. It will give the option for creating a “Button1\_Click”, but any previously written macro can be selected.

![](<Base64-Image-Removed>)

A button will appear on the worksheet ready for use.

![](<Base64-Image-Removed>)

**5\.** **Setting it to automatically run on a specific event**

Ah, that’s a little more sophisticated – and we’ll return to that in another blog (we have to keep you on tenterhooks somehow…).

Stay tuned next week for more VBA!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/going-through-the-visual-basics-part-6/#0)
    
*   [Register](https://sumproduct.com/thought/going-through-the-visual-basics-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/going-through-the-visual-basics-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/going-through-the-visual-basics-part-6/#0)

[](https://sumproduct.com/thought/going-through-the-visual-basics-part-6/#0 "close")

top