# VBA Blogs: Looking Up and Down

**Source:** https://sumproduct.com/blog/vba-blogs-looking-up-and-down/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Looking Up and Down

*   May 10, 2018

VBA Blogs: Looking Up and Down
==============================

VBA Blogs: Looking Up and Down
==============================

11 May 2018

Last week we set the **After** parameter for the **Find** method to distinguish which cell we wanted to start from. But it defaulted to go across the row. It can be set in order to go down the columns first using the **SearchOrder** parameter.

This is where we need to look at how VBA handles parameters.

When we type the **Find** method and open the brackets, we will see the tool tip for the parameter list – identical to when we use functions in Excel formulae.

![](https://sumproduct.com/wp-content/uploads/2025/05/69ba668caeec9c30554bc2705ecf0c8b.jpg)

The bolded parameter is the one we are currently entering. The parameters in square brackets are the _Optional_ parameters. We could skip to **SearchOrder** using:

searchRange.Find(“up”, Range(“C5”), , , xlByColumns)

But this isn’t a good approach. It is very easy (and we will admit to having done this) to put the wrong number of commas in and have the subroutine fail at that point in the code.

VBA allows us to assign values to specific parameters directly. This is done by naming the parameter followed by “:=” then the value. In the previous example that line is better written as:

searchRange.Find(“up”, After:=Range(“C5”), SearchOrder:=xlByColumns)

With that in mind, our full subroutine will look like this:

**Sub** FindAfterByColumns()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)  

**Dim** foundrange As Range

**Set** foundrange = searchRange.Find(“up”, After:=Range(“C5”), SearchOrder:=xlByColumns)

**If** foundrange **Is Nothing Then**

**Debug.Print** “not found!”

**Else**

**Debug.Print** foundrange

        **Debug.Print** foundrange.Address

   **End If**

**End Sub**

Which results in:

![](<Base64-Image-Removed>)

Next week we will pinpoint exactly how to dig up our column!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-looking-up-and-down/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-looking-up-and-down/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-looking-up-and-down/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-looking-up-and-down/#0)

[](https://sumproduct.com/blog/vba-blogs-looking-up-and-down/#0 "close")

top