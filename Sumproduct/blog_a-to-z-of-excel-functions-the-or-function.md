# A to Z of Excel Functions: The OR Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The OR Function

*   June 18, 2023

A to Z of Excel Functions: The OR Function
==========================================

A to Z of Excel Functions: The OR Function
==========================================

19 June 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **OR** function._

**The OR function**

The **OR** function is similar to **[AND](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-and-function)
**, but only requires one condition to be TRUE. Similar to **AND**, the **OR** function may be used to expand the usefulness of other functions that perform logical tests. For example, the **IF** function performs a logical test and then returns one value if the test evaluates to TRUE and another value if the test evaluates to FALSE. By using the **OR** function as the **logical\_test** argument of the **IF** function, you can test many different conditions instead of just one.

For example, imagine you are in London on a Tuesday. Consider the expression

**\=OR(condition1, condition2, condition3)**

where:

*   **condition1** is the condition, “today is Tuesday”
*   **condition2** is the condition, “you are in London” _and_
*   **condition3** is the condition, “the Earth is flat”.

This would clearly be TRUE as you are definitely in London (that is, **condition2** holds).

The syntax for **OR** is as follows:

**OR(logical1, \[logical2\], …)**

where:

*   **logical1:** the first condition that you want to test that can evaluate to either TRUE or FALSE
*   **logical2:** additional conditions that you want to test that can evaluate to either TRUE or FALSE, up to a maximum of 255 conditions. **logical2** is optional and is not needed in the syntax.

It should be noted that:

*   The arguments must evaluate to logical values, such as TRUE or FALSE, or the arguments must be arrays or references that contain logical values
*   If an array or reference argument contains text or empty cells, those values are ignored
*   If the specified range contains no logical values, the **OR** function returns the _#VALUE!_ error value.

In summary, **OR** works as follows:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-or-function/#0 "close")

top