# VBA Blogs: Going Through the Visual Basics – Part 8

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 8

*   October 4, 2018

VBA Blogs: Going Through the Visual Basics – Part 8
===================================================

VBA Blogs: Going Through the Visual Basics – Part 8
===================================================

5 October 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at the concept of a variable scope at a module level._

Variables can also be used in different subroutines and functions. If there are items that are known to have constant values throughout the entire workbook, they can be declared explicitly in one place for easy reference.

**Module Level**

Let’s write a new module as follows:

Option Explicit

Sub ScopeTest()

    Dim myTestString As String

    myTestString = “Hello World!”

End Sub

Sub NextScopeTest()

    MsgBox myTestString

End Sub

The declaration for the variable is in **ScopeTest** but the subroutine **NextScopeTest** calling it is not the one that defined it. What happens upon execution?

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-555.jpg)

The ‘Variable not defined’ message pops up again. Let’s move the declaration OUTSIDE the subroutine, under the ‘Option Explicit’ statement as follows:

Option Explicit

Dim myTestString As String

Sub ScopeTest()

    myTestString = “Hello World!”

End Sub

Sub NextScopeTest()

    MsgBox myTestString

End Sub

When **NextScopeTest** is run the following happens:

![](<Base64-Image-Removed>)

This is because though the variable has been declared, it has not been _initialised_. If **ScopeTest** is run prior to **NextScopeTest** then:

![](<Base64-Image-Removed>)

These shows that the variable is accessible to the entire module and is changed as required. The **Dim** statement outside any subroutines means the variable is accessible within the module that it is declared in.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-8/#0 "close")

top