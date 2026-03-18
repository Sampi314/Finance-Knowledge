# VBA Blogs: Going Through the Visual Basics – Part 9

**Source:** https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Going Through the Visual Basics – Part 9

*   October 11, 2018

VBA Blogs: Going Through the Visual Basics – Part 9
===================================================

VBA Blogs: Going Through the Visual Basics – Part 9
===================================================

12 October 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at the concept of a variable scope at a project level._

Variables can also be used in different subroutines and functions. If there are items that are known to have constant values throughout the entire workbook, they can be declared explicitly in one place for easy reference.

**Project Level**

Sharing variables between procedures within the same module was very simple but what if another module wanted to reuse the same variable?

![](<Base64-Image-Removed>)

**Module2** wants to use **myTestString** but it is declared in **Module1**.

![](<Base64-Image-Removed>)

Upon running, it again says the ‘Variable not defined’. In order to force a variable to be accessible to the entire workbook the statement, the ‘Public’ statement may be used.

![](<Base64-Image-Removed>)

Now this will be accessible from **Module2** so when the following code is called.

![](<Base64-Image-Removed>)

The variable is used as necessary and the expected result eventuates.

![](<Base64-Image-Removed>)

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/#0)

[](https://sumproduct.com/blog/vba-blogs-going-through-the-visual-basics-part-9/#0 "close")

top