# A to Z of Excel Functions: The CUBESETCOUNT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CUBESETCOUNT Function

*   March 18, 2018

A to Z of Excel Functions: The CUBESETCOUNT Function
====================================================

A to Z of Excel Functions: The CUBESETCOUNT Function
====================================================

19 March 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CUBESETCOUNT** function._

**The CUBESETCOUNT function**

When the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source, this function returns the number of items in a set.

![](<Base64-Image-Removed>)

The **CUBESETCOUNT** function employs the following syntax to operate:

**CUBESETCOUNT(set)**

The **CUBESETCOUNT** function has the following arguments:

*   **set:** this is required and represents a text string of a Microsoft Excel expression that evaluates to a set defined by the **CUBESET** function
*   **set** can also be the **CUBESET** function, or a reference to a cell that contains the **CUBESET** function.

It should be further noted that:

*   the **CUBESETCOUNT** function is supported only when the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source
*   when the **CUBESETCOUNT** function evaluates, it temporarily displays a “#GETTING\_DATA…” message in the cell before all of the data is retrieved.

Please see my examples below:

**\=CUBESETCOUNT(A3)**

**\=CUBESETCOUNT(CUBESET(“Sales”,”\[Product\].\[All Products\].Children”,”Products”,1,”\[Measures\].\[Sales Amount\]”))**

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubesetcount-function/#0 "close")

top