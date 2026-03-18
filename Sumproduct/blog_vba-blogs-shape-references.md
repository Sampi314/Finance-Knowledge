# VBA Blogs: Shape References

**Source:** https://sumproduct.com/blog/vba-blogs-shape-references/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Shape References

*   June 6, 2019

VBA Blogs: Shape References
===========================

VBA Blogs: Shape References
===========================

7 June 2019

_Welcome back to the VBA blog! This week we are going to cover something we’ve had to do in one of our consulting jobs. It is a little niche, but it may be a good source of inspiration for some of us._

We had to create a large number of shapes that displayed the text value of the cell each shape covered. Sometimes these cells and / or shapes would move. We thought that going through the shapes manually and relinking each shape to its respective cell reference would prove to be quite time consuming. So, we wrote a small macro to help us!

Say we have the following worksheet layout:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-415.jpg)

The next step is to create some shapes and position them over some of the cells with text in them.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-430.jpg)

We can then run the following macro that we wrote:

Sub Shapes ()

Dim sh As Shape

Dim shformula As Variant

For Each sh In ActiveSheet.Shapes

    Set shformula = ActiveSheet.Shapes.Range(Array(sh.Name))

    shformula.Select

    Selection.Formula = “=” & sh.TopLeftCell.Address

Next sh

End Sub

The first three lines of code begin the macro and defines our variables that the rest of the code will reference.

The 4th line of code:

For Each sh In ActiveSheet.Shapes

starts a loop for the code to run for every shape. The 5th line:

    Set shformula = ActiveSheet.Shapes.Range(Array(sh.Name))

defines the variable shformula as the object formula that we are defining. The 6th line selects the variable shformula, and the 7th line assigns the reference of the cell that is located on the top left corner of the shape, to the shape’s formula.

Curiously the macro does not work if you combine the 6th and 7th lines of code to:

    shformula.Formula = “=” & sh.TopLeftCell.Address

the macro just returns with an error when we execute it in this form.

After running the macro, the shapes now have cell references the respective text values:

![](<Base64-Image-Removed>)

We can also reallocate the shapes to new positions:

![](<Base64-Image-Removed>)

Then re-run the macro to update their contents:

![](<Base64-Image-Removed>)

That’s it for this week! Come back next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-shape-references/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-shape-references/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-shape-references/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-shape-references/#0)

[](https://sumproduct.com/blog/vba-blogs-shape-references/#0 "close")

top