# VBA Blogs: Op-TRIM-isation

**Source:** https://sumproduct.com/blog/vba-blogs-op-trim-isation/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Op-TRIM-isation

*   June 21, 2018

VBA Blogs: Op-TRIM-isation
==========================

VBA Blogs: Op-TRIM-isation
==========================

22 June 2018

One thing a regular coder always has to consider is optimisation. Code optimisation is the process of modifying code to improve quality and efficiency. By looking doing code optimisation, programs can become more lightweight in size, consume less memory, execute more rapidly and perform fewer operations.

The first introduction to VBA for most users is recording a macro.

I’m going to record a macro doing the following things in a fresh workbo

*   Type “Hello World” in **A1**
*   Change **A1**‘s fill colour to Red
*   Type the number 1 in **A50**
*   Drag down my number to **A60**
*   Sum the values.

This is what my macro recorded:

**Sub** Macro1()

‘ Macro1 Macro

    ActiveCell.FormulaR1C1 = “Hello World”

    Range(“A1”).Select

**With** Selection.Interior

        .Pattern = xlSolid

        .PatternColorIndex = xlAutomatic

        .Color = 65535

        .TintAndShade = 0

        .PatternTintAndShade = 0

**End With**

    ActiveWindow.SmallScroll Down:=27

    Range(“A50”).Select

    ActiveCell.FormulaR1C1 = “1”

    Range(“A50”).Select

    Selection.AutoFill Destination:=Range(“A50:A60”), Type:=xlFillDefault

    Range(“A50:A60”).Select

    Range(“A61”).Select

    ActiveCell.FormulaR1C1 = “=SUM(R\[-11\]C:R\[-1\]C)”

    Range(“A62”).Select

**End Sub**

That’s a lot of lines!

Notice what the Macro has done:

*   It has recorded every specific step that was made. It’s generated a **Range.Select line** whenever I moved the cursor to do an action upon a cell – it’s even recorded my scroll movement that I took to get to **A50**
*   When changing the cell fill colour, it’s not just set the properties for the colour, but for everything else around it

Let’s simplify our recorded Macro.

Before we start that, please note we will need to change the first line! It starts with **ActiveCell** because I just opened a workbook, it was set to **A1** and off it went. Let’s reference it to **A1** directly because otherwise if my cursor is focused on any other cell then it will type “Hello World” there.

So replace

    ActiveCell.FormulaR1C1 = “Hello World”

With

    Range(“A1”).FormulaR1C1 = “Hello World”

Next, we’ve got our colour change statement. In order for us to be clear exactly what we are doing, I’m only going to leave the **.Color** line. However, the **With** statement is unnecessary if I’ve only got one line. We can remove that as well.

So

**With** Selection.Interior

        .Pattern = xlSolid

        .PatternColorIndex = xlAutomatic

        .Color = 65535

        .TintAndShade = 0

        .PatternTintAndShade = 0

**End With**

Becomes

    Selection.Interior.Color = 65535

Let’s remove the scroll movement altogether. There is no need for the program to change the screen, that scroll movement was an action that I had to take, not the program!

So delete

    ActiveWindow.SmallScroll Down:=27

Finally, we can remove .**Select** statements! Notice that after a **.Select** line there is a **Selection** or **ActiveCell** statement. We can simply just replace those with the **Range** that was selected.

So for example:

    Range(“A50”).Select

    ActiveCell.FormulaR1C1 = “1”

Can simply become

    Range(“A50”).FormulaR1C1 = “1”

So how will my end code look?

**Sub** Macro1()

‘ Macro1 Macro

    Range(“A1”).FormulaR1C1 = “Hello World”

    Range(“A1”).Color = 65535

    Range(“A50”).FormulaR1C1 = “1”

    Range(“A50”).AutoFill Destination:=Range(“A50:A60”), Type:=xlFillDefault

    Range(“A61”).FormulaR1C1 = “=SUM(R\[-11\]C:R\[-1\]C)”

**End Sub**

Wow! So I’ve trimmed the recorded Macro which generated 18 lines of code down to 5 lines – which is more indicative of the 5 actions that were performed.

Recording macros is a great way to get started especially if it’s a task you’ve done over and over again and unsure of syntax, but always look at ways to trim down the code. Each additional line of code is more operations that VBA will do and require more system resources. Code optimisation is not out of reach for the novice VBA user!

Next week we’ll look at more advanced optimsiation tricks so make it’ll be an efficient use of time to come back and visit!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-op-trim-isation/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-op-trim-isation/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-op-trim-isation/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-op-trim-isation/#0)

[](https://sumproduct.com/blog/vba-blogs-op-trim-isation/#0 "close")

top