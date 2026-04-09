# Going Through the Visual Basics – Part 10

**Source:** https://sumproduct.com/thought/going-through-the-visual-basics-part-10/

---

[Home](https://sumproduct.com/)

\> Going Through the Visual Basics – Part 10

*   October 19, 2018

Going Through the Visual Basics – Part 10
=========================================

VBA Blogs: Going Through the Visual Basics – Part 10
====================================================

19 October 2018

_We thought we’d run an elementary series going through the rudiments of Visual Basic for Applications (VBA) as a springboard for newer users. This blog looks at declaring constants._

It is highly recommended any values that are passed into formulae, subroutines and / or functions are variables. However, what if the value of that variable does not change? There is a way to make it immutable by declaring it as a constant. This means that it cannot be changed during execution. By declaring constants, they can easy to access without hardcoding the information more than once and make code much more readable and facilitate error checking.

Constants are declared in a similar way to **Dim** except using the keyword **Const** – except a constant should always be assigned a value when it is declared.

![](<Base64-Image-Removed>)

If somewhere in the code, it tries to reassign the value, the VBA Compiler spits an error message before execution.

![](<Base64-Image-Removed>)

The compiler determines what the data type is from the type of expression of the constant. However, it is always good form to explicitly state a data type. This is particularly important if you plan on doing arithmetic expressions in your code that results in what is known as a Long value and having an Integer constant will cause overflow errors. Using the **As** statement in a similar way to the **Dim** statement the data type of the constant may be cast.

![](<Base64-Image-Removed>)

Multiple constants can be declared on a single line as well:

![](<Base64-Image-Removed>)

Now knowing how constants are declared, like variables, the scope of the constants is also put under consideration. This is declared the same way as variables – the subject of our past two articles ([Part 8](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-going-through-the-visual-basics-part-8)
 and [Part 9](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-going-through-the-visual-basics-part-9)
).

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/going-through-the-visual-basics-part-10/#0)
    
*   [Register](https://sumproduct.com/thought/going-through-the-visual-basics-part-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/going-through-the-visual-basics-part-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/going-through-the-visual-basics-part-10/#0)

[](https://sumproduct.com/thought/going-through-the-visual-basics-part-10/#0 "close")

top