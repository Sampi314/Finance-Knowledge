# The A to Z of DAX Functions – ISEVEN

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISEVEN

*   October 28, 2025

The A to Z of DAX Functions – ISEVEN
====================================

____In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISEVEN**.____

**_**_**_The_** _**ISEVEN**_ **_function_**_**_**

![](<Base64-Image-Removed>)

The **ISEVEN** function is one of the information functions that checks whether a number is even (and is nothing to do with i7 computer chips!):

> **ISEVEN(number)**

There is one \[1\] main argument in this function:

*   **number**: this is the value to test.  If the **number** is not an integer, it is truncated.

Here are a few remarks about the **ISEVEN** function:

*   it returns **TRUE** if the **number** is even
*   it returns **FALSE** if the **number** is odd
*   if number is nonnumeric, **ISEVEN** returns the _#VALUE!_ error value
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s write a few tests with different types of values to see how this function evaluates each of them:

**EVALUATE**

**ROW(**

 **“Check1”,** **IFERROR(ISEVEN(4),** **“Error”),**

 **“Check2”,** **IFERROR(ISEVEN(7),** **“Error”),**

 **“Check3”,** **IFERROR(ISEVEN(-2),** **“Error”),**

 **“Check4”,** **IFERROR(ISEVEN(4.8),** **“Error”),**

 **“Check5”,** **IFERROR(ISEVEN(4.2),** **“Error”),**

 **“Check6”,** **IFERROR(ISEVEN(“DAX”),** **“Error”)**

**)**

![](<Base64-Image-Removed>)

This returns the following table:

![](<Base64-Image-Removed>)

If the number is not a whole number, **ISEVEN** truncates it before checking (_e.g._ 4.8 becomes 5 and 4.2 becomes 4); if the value is nonnumeric, **ISEVEN** returns an error.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-iseven/#0 "close")

top