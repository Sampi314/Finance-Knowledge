# A to Z of Excel Functions: The EXPAND Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The EXPAND Function

*   April 17, 2022

A to Z of Excel Functions: The EXPAND Function
==============================================

A to Z of Excel Functions: The EXPAND Function
==============================================

18 April 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **EXPAND** function._

**The EXPAND function**

The **EXPAND** function expands (or pads) an array to specified row and column dimensions. It has the following syntax:

**EXPAND(array, rows, \[columns\], \[pad with\])**

The **EXPAND** function has the following arguments:

*   **array:** this is required and represents the selected array to be expanded
*   **rows:** this is also required and denotes the number of rows in the expanded **array**. If this argument is missing (not bad for a required argument!), **rows** will not be expanded
*   **columns:** this is optional and denotes the number of columns in the expanded **array**. Again, should **columns** not be specified, this dimension will not be expanded
*   **pad with:** this is an optional value with which to pad. The default is _N/A_.

It should be noted that:

*   if **rows** isn’t provided or is empty, the default value is the number of rows in the **array** argument (as aforementioned)
*   if **columns** isn’t provided or is empty, the default value is the number of columns in the **array** argument
*   if **pad with** is not provided and array has one value for that dimension, then that value is used. This operation is commonly referred to as array “broadcasting”; however, this does not appear to work presently
*   Excel returns an _#VALUE!_ error when the rows or columns argument is less than the **rows** or **columns** in the **array** argument
*   Excel returns an _#N/A_ error when **pad with** is greater than a single column or row
*   Excel returns an _#NUM!_ when **array** is too large.

Please see my examples below:

![](https://sumproduct.com/wp-content/uploads/2025/05/e6b301e3bfe7eb4eb3c118c8620ef889.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/ce93e9cba6a96882863c9a630e8e83b7.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/551ec7a7f8780954b8a84f81635f26b4.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/3d3a3a3194f984b54b569981ce248478.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-expand-function/#0 "close")

top