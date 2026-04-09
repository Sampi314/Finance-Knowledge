# A to Z of Excel Functions: The MDETERM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MDETERM Function

*   February 6, 2022

A to Z of Excel Functions: The MDETERM Function
===============================================

A to Z of Excel Functions: The MDETERM Function
===============================================

7 February 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MDETERM** function._

**The MDETERM function**

In mathematics, especially in areas such as linear algebra, matrices may be used to solve simultaneous equations. For the record, a matrix is not just a movie it’s a rectangular arrangement of **mn** elements, in the dimensions of **m** rows by **n** columns, _e.g._ a matrix **A**_(say)_ may be represented as

![](<Base64-Image-Removed>)

It is often written in compact form as

![](<Base64-Image-Removed>)

Should the matrix be square (_i.e._**m** \= **n**), then we may calculate a scalar value, known as the **determinant** which can be used to calculate matrix inverses, solve systems of linear equations and assist with calculus (unless it’s really stuck on your teeth). For a square matrix **A**, this determinant is denoted by

det **A** _or_  |**A**|

For example, with a 3 x 3 matrix, the determinant may be represented as

![](<Base64-Image-Removed>)

Some texts state that if the determinant is zero, the matrix inverse does not exist, but this is not strictly correct, as there may be another multiplicative identity for such a matrix – but that’s _way_ beyond what we wish to talk about here!

To calculate it, the idea is as follows. For a 2 x 2 matrix,

![](<Base64-Image-Removed>)

For a 3 x 3 matrix, the calculation extends:

![](<Base64-Image-Removed>)

In this situation, each determinant of the three 2 × 2 matrices is called a **minor** of the matrix **A**. This procedure can be extended to give a recursive definition for the determinant of an **n** × **n** matrix, known as a **Laplace expansion**. It sounds a bit like my waistline.

The Excel function **MDETERM** returns the matrix determinant of an array. It has the following syntax:

**MDETERM(array)**

where:

*   **array** is required, and represents a numerical **array** with an equal number of rows and columns.

It should be noted that:

*   **array** may be given as:

o a cell range, _e.g._**A1:C3**

o an **array** constant, such as **{1,2,3;4,5,6;7,8,9}**

o a name to either of these

*   **MDETERM** returns the _#VALUE!_ error when:

o any cells in array are empty or contain text

o **array** does not have an equal number of rows and columns

*   the matrix determinant is a number derived from the values in the **array**. For a three-row, three-column array, **A1:C3**, the determinant is defined as:

**MDETERM(A1:C3)** equals

**A1 \* (B2 \* C3 – B3 \* C2) + A2 \* (B3 \* C1 – B1 \* C3) + A3 \* (B1 \* C2 – B2 \* C1)  
**

*   matrix determinants are generally used for solving systems of mathematical equations that involve several variables

*   **MDETERM** is calculated with an accuracy of approximately 16 digits, which may lead to a small numeric error when the calculation is not complete. For example, the determinant of a singular matrix may differ from zero by 1E-16.

As an example:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mdeterm-function/#0 "close")

top