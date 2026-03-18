# A to Z of Excel Functions: The MMULT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MMULT Function

*   July 3, 2022

A to Z of Excel Functions: The MMULT Function
=============================================

A to Z of Excel Functions: The MMULT Function
=============================================

4 July 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MMULT** function._

**The MMULT function**

![](<Base64-Image-Removed>)

In mathematics, matrix multiplication is what’s known as a binary operation that produces a matrix from two matrices. For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix. The resulting matrix, known as the matrix product, has the number of rows of the first and the number of columns of the second matrix, _i.e._

![](<Base64-Image-Removed>)

Algebraically, if **A** is an **m** x **n** matrix and **B** is an **n** x **p** matrix,

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

then the matrix product **C** \= **AB** is determined to be the **m** x **p** matrix

![](<Base64-Image-Removed>)

_i.e._

![](<Base64-Image-Removed>)

The Excel function **MMULT** returns the matrix product of two arrays, **array1** and **array2** (the Excel equivalent of a matrix). The result is an array with the same number of rows as **array1** and the same number of columns as **array2**.

It has the following syntax:

**MMULT(array1, array2)**

where:

*   **array1** and **array2** are required, and represent the two arrays you wish to multiply.

It should be noted that:

*   as explained above, the number of columns in **array1** must be the same as the number of rows in **array2**, and both arrays must contain only numbers
*   **array1** and **array2** may be given as cell ranges, array constants or references
*   **MMULT** returns the _#VALUE!_ error when:
    *   any cells are empty or contain text
    *   the number of columns in **array1** is different from the number of rows in **array2**

*   The matrix product array, **a**, of two arrays, **b** and **c**, is:

![](<Base64-Image-Removed>)

where **i** is the row number and **j** is the column number.

If you are using Microsoft 365, then you can simply enter the formula in the top left cell of the output range, then press **ENTER** to confirm the formula as a [dynamic array formula](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
. Otherwise, the formula must be entered as a legacy array formula by first selecting the output range, entering the formula in the top-left-cell of the output range, and then pressing **CTRL + SHIFT + ENTER** to confirm it. Excel inserts braces (curly brackets) automatically.

As examples:

**_Legacy Approach_**

![](<Base64-Image-Removed>)

**_Using Dynamic Arrays_**

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mmult-function/#0 "close")

top