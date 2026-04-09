# A to Z of Excel Functions: The HSTACK Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The HSTACK Function

*   April 24, 2022

A to Z of Excel Functions: The HSTACK Function
==============================================

A to Z of Excel Functions: The HSTACK Function
==============================================

25 April 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **HSTACK** function._

**The HSTACK function**

The **HSTACK** function returns the array formed by appending each of the array arguments in a column-wise fashion (Microsoft’s jargon, not ours). It has the following syntax:

**HSTACK(array1, \[array2, …\])**

The **HSTACK** function has the following argument(s):

*   **array:** the first argument is required (others are optional) and represents the **array**(s) to append.

It should be noted that:

*   **HSTACK** returns the array formed by appending each of the array arguments in a column-wise fashion. The resulting **array**will be the following dimensions:
    *   columns: the maximum of the column count from each of the array arguments
    *   rows: the combined count of all the rows from each of the array arguments

*   Excel returns an _#N/A_ error if an array has fewer rows or columns than the maximum in any selected array. To remove the errors, you should use the **IFERROR** function.

Please see my examples below:

![](https://sumproduct.com/wp-content/uploads/2025/05/7cc73cf68d8f05e0f2cb9c71172fddd4.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/ff7b34e3fbed7b5be335fe266d776018.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/274d0378a3b76edbfddea836e5828e76.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/48e2179f388586c6ca49bce1e59e4a27.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/#0 "close")

top