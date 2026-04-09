# VBA Blogs: Going Through the Visual Basics – Part 7

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 7

*   September 20, 2018

VBA Blogs: Going Through the Visual Basics – Part 7
===================================================

VBA Blogs: Going Through the Visual Basics – Part 7
===================================================

21 September 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at declaring variables._

To maintain good coding practice to declare variables, it is easy to ask VBA to force the coder to declare them all the time. This is done using the opening statement **Option Explicit**.

When **Option Explicit** appears in a file, you must explicitly declare all variables by using the **Dim** or **ReDim** statements. If you try to use an undeclared variable name, an error occurs at compile time.

As an example, let’s start with the following code:

Option Explicit

Sub OETest()

    myTestString = “Hello World!”

    MsgBox myTestString

End Sub

Running this code results in the following:

![](<Base64-Image-Removed>)

The compiler stops with an error alert and snaps back to the Visual Basic Editor to the variable that has not been declared. The procedure must be stopped and the declaration statements added before it will successfully execute.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-7/#0 "close")

top