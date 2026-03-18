# The A to Z of DAX Functions – ISODD

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISODD

*   December 30, 2025

The A to Z of DAX Functions – ISODD
===================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISODD**._

**_The_** _**ISODD**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/11/image-132.png)

The **ISODD** function is one of the information functions that checks whether a number is odd:

**`ISODD (number)`**

There is one \[1\] main argument in this function:

*   **number**: this is the value to test.  If the **number** is not an integer, it is truncated.

Here are a few remarks about the **ISODD** function:

*   it returns **TRUE** if the **number** is odd
*   it returns **FALSE** if the **number** is even
*   if number is nonnumeric, **ISODD** returns the _#VALUE!_ error value
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s write a few tests with different types of values to see how this function evaluates each of them:

**EVALUATE**

**ROW(**

 **“Check1”,** **IFERROR(ISODD(4),** **“Error”),**

 **“Check2”,** **IFERROR(ISODD(7),** **“Error”),**

 **“Check3”,** **IFERROR(ISODD(-3),** **“Error”),**

 **“Check4”,** **IFERROR(ISODD(4.8),** **“Error”),**

 **“Check5”,** **IFERROR(ISODD(4.2),** **“Error”),**

 **“Check6”,** **IFERROR(ISODD(“DAX”),** **“Error”)**

**)**

![](<Base64-Image-Removed>)

This returns the following table:

![](<Base64-Image-Removed>)

If the number is not a whole number, **ISODD** truncates it before checking (for example, 4.8 becomes 5 and 4.2 becomes 4).  If the value is nonnumeric, **ISODD** returns an error.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isodd/#0 "close")

top