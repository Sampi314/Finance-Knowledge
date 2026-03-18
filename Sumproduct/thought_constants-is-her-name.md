# Constants is Her Name

**Source:** https://sumproduct.com/thought/constants-is-her-name/

---

[Home](https://sumproduct.com/)

\> Constants is Her Name

*   November 3, 2017

Constants is Her Name
=====================

VBA Blogs: Constants is Her Name
================================

3 November 2017

It is highly recommended that values that are passed into formulae, subroutines and functions are variables. However what if the value of that variable does not change? There is a way to make it immutable by declaring it as a constant. This means that it cannot be changed during execution.

By declaring constants, they can easy to access without hardcoding the information more than once and make code much more readable and facilitate error checking.

Constants are declared in a similar way to “Dim” except using the keyword “Const” – except a constant should always be assigned a value when it is declared.

![](<Base64-Image-Removed>)

If somewhere in the code, it tries to reassign the value, the VBA Compiler spits an error message before execution.

![](<Base64-Image-Removed>)

The compiler determines what the data type is from the type of expression of the constant. However it is always good form to explicitly state a data type. This is particularly important if you plan on doing arithmetic expressions in your code that results in a Long value and having an Integer constant will cause overflow errors. Using the “As” statement like used in “Dim” the data type of the constant can be cast.

![](<Base64-Image-Removed>)

Multiple constants can be declared on a single line as well:

![](<Base64-Image-Removed>)

Now knowing how constants are declared, like variables, the scope of the constants are also put under consideration. This is declared the same way as variables as discussed in the [VBA Blog: Scoping Variables](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-scoping-variables)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/constants-is-her-name/#0)
    
*   [Register](https://sumproduct.com/thought/constants-is-her-name/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/constants-is-her-name/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/constants-is-her-name/#0)

[](https://sumproduct.com/thought/constants-is-her-name/#0 "close")

top