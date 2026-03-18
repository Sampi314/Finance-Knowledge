# A to Z of Excel Functions: The AND Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The AND Function

*   August 2, 2016

A to Z of Excel Functions: The AND Function
===========================================

A to Z of Excel Functions: The AND Function
===========================================

3 August 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **AND** Function._

**The ANDfunction**

My old English teacher said you should never start or finish a sentence with the word “and”. **AND** is one of several Excel logic functions (others include **NOT**, **OR** and **XOR**). It returns TRUE if all of its arguments evaluate to TRUE; it returns FALSE if one or more arguments evaluate to FALSE.

One common use for the **AND** function is to expand the usefulness of other functions that perform logical tests. For example, the **IF** function performs a logical test and then returns one value if the test evaluates to **TRUE** and another value if the test evaluates to **FALSE.** By using the **AND** function as the **logical\_test** argument of the **IF** function, you can test many different conditions instead of just one.

For example, imagine you are in New York on a Monday. Consider the expression

**\=AND(condition1, condition2, condition3)**

where:

*   **condition1** is the condition, “today is Monday”
*   **condition2** is the condition, “you are in New York” _and_
*   **condition3** is the condition, “this author is the best looking guy you have ever seen”.

This would clearly be FALSE as not everywhere in the world it would be Monday (_i.e._**condition1** would be breached)…

As alluded to above, the syntax for **AND** is as follows:

**AND(logical1, \[logical2\], …)**

where:

*   **logical1:** the first condition that you want to test that can evaluate to either TRUE or FALSE
*   **logical2:** additional conditions that you want to test that can evaluate to either TRUE or FALSE, up to a maximum of 225 conditions. **logical2** is optional and is not needed in the syntax.

It should be noted that:

*   The arguments must evaluate to logical values, such as TRUE or FALSE, or the arguments must be arrays or references that contain logical values
*   If an array or reference argument contains text or empty cells, those values are ignored
*   If the specified range contains no logical values, the **AND** function returns the _#VALUE!_ error values.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
.  
_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-and-function/#0 "close")

top