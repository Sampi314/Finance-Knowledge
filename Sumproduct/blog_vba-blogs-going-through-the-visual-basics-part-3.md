# VBA Blogs: Going Through the Visual Basics – Part 3

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 3

*   August 16, 2018

VBA Blogs: Going Through the Visual Basics – Part 3
===================================================

VBA Blogs: Going Through the Visual Basics – Part 3
===================================================

17 August 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at actually recording a macro._

[Last time out](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-going-through-the-visual-basics-part-2)
 I talked through the four ways of recording a macro. Let’s assume we’ve got that initiated. After pressing ‘Record Macro’, the ‘Record Macro’ dialog box will appear. Let’s start by giving the macro a name and description and press ‘OK’:

![](<Base64-Image-Removed>)

After hitting ‘OK’ the recording mode will start in Excel. Looking back at the status bar in Excel, the icon next to ‘Ready’ has changed into a stop button:

![](<Base64-Image-Removed>)

Pressing the stop button will stop the recording of the macro. ‘Stop Recording’ will also replace the ‘Record Macro’ buttons on the Developer and View tabs, as will the keyboard shortcut **ALT + W + M + R**.

![](<Base64-Image-Removed>)

For our first example macro, lets perform the following actions

*   Clicked on the ‘Record Macro’ button
*   Fill cell **A5** red
*   Copy cell **A5** to **B3**
*   Type “colour” in cell **C6**
*   Click on the ‘Stop recording’ button.

![](<Base64-Image-Removed>)

That’s our first macro recorded!

Going back to the ‘Macros’ button in the Ribbon and select ‘View Macros’:

![](<Base64-Image-Removed>)

A list of all the macros in the workbook will come up including our macro that we have just recorded.

![](<Base64-Image-Removed>)

From there we can press ‘Edit’ to go to the VBA Editor which will snap to the newly written macro:

![](<Base64-Image-Removed>)

We can see that we’ve got some text in the top right, and that’s the code for our macro:

Sub Test1()

‘

‘ Test1 Macro

‘ My First Macro

‘

‘

    With Selection.Interior

        .Pattern = xlSolid

        .PatternColorIndex = xlAutomatic

        .Color = 255

        .TintAndShade = 0

        .PatternTintAndShade = 0

    End With

    Selection.Copy

    Range(“B3”).Select

    ActiveSheet.Paste

    Range(“C6”).Select

    Application.CutCopyMode = False

    ActiveCell.FormulaR1C1 = “colour”

    Range(“C7”).Select

End Sub

Recording macros is great when you are unsure how to program a specific task, making it easier to look up the relevant syntax to code up more complex procedures. However, there are certain drawbacks.

Note the comments (in green with apostrophes) – this is how you can “document” your procedures, _i.e._ tell other people what your code is doing. You should always try to remember to do this, especially as you become more experienced and your macros become more complex.

The inherent ‘Relative Referencing’ setting allows recording for things to occur in relation to the current cell. If the ‘Relative Referencing’ setting is not used, it will hard code the direct cell reference in the code which might not be the intention. This setting is activated on the ‘Developer’ tab in the Ribbon.

The recording also produces extra lines indicating the movement of the screen. In the code example above, every time the mouse moved to select a cell like **Range(“C6”).Select**, this action was also recorded, however this isn’t strictly necessary in terms of achieving the outcome of this routine.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-3/#0 "close")

top