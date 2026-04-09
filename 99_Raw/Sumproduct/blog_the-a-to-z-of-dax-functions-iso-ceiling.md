# The A to Z of DAX Functions – ISO.CEILING

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISO.CEILING

*   December 23, 2025

The A to Z of DAX Functions – ISO.CEILING
=========================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISO.CEILING**._

**_The_** _**ISO.CEILING**_ **_function_**

![](<Base64-Image-Removed>)

The **ISO.CEILING** function is one of the information functions that returns a number that is rounded up to the nearest integer or to the nearest multiple of significance:

**ISO.CEILING** **(number,** **\[significance\])**

There are two \[2\] main arguments in this function:

*   **number**: this is required which is the value to be rounded
*   **significance**: this is optional which is the multiple to which number is to be rounded.  If significance is omitted, its default value is one \[1\].

Here are a couple of remarks about the **ISO.CEILING** function:

*   it emulates the behaviour of the **CEILING** function in Excel
*   it follows the ISO-defined behaviour for determining the ceiling value.

Let’s write a few tests with different types of values to see how this function evaluates each of them:

**`EVALUATE   ROW(    "Check1", ISO.CEILING( 3 ),    "Check2", ISO.CEILING( -3 ),    "Check3", ISO.CEILING( 2.5 ),    "Check4", ISO.CEILING( -2.5 )   )`**

![](<Base64-Image-Removed>)

This returns the following table:

![](<Base64-Image-Removed>)

The significance defaults to one \[1\], so integers remain unchanged, positive non-integers are rounded up to the next integer and negative numbers are rounded toward zero \[0\].

Next if we set the significance to -2:

**`EVALUATE   ROW(    "Check1", ISO.CEILING( 3, -2 ),    "Check2", ISO.CEILING( -3, -2 ),    "Check3", ISO.CEILING( 2.5, -2 ),    "Check4", ISO.CEILING( -2.5, -2 )   )`**

![](<Base64-Image-Removed>)

This returns the following table:

![](<Base64-Image-Removed>)

The significance is set to -2, so numbers are rounded to the nearest multiple of -2.  Positive numbers are rounded down to the next negative multiple, whilst negative numbers are rounded up toward zero \[0\] along negative multiples.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iso-ceiling/#0 "close")

top