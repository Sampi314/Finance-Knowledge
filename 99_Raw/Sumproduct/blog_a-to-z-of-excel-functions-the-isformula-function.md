# A to Z of Excel Functions: The ISFORMULA Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ISFORMULA Function

*   May 23, 2021

A to Z of Excel Functions: The ISFORMULA Function
=================================================

A to Z of Excel Functions: The ISFORMULA Function
=================================================

24 May 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ISFORMULA** function._

**The ISFORMULA function**

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-193.jpg)

At the time of writing, there are 12 **IS** functions, _i.e._ functions that give rise to a TRUE or FALSE value depending upon whether a certain condition is met:

1.  **ISBLANK(reference):** checks whether the **reference** is to an empty cell
2.  **ISERR(value):** checks whether the **value** is an error (_e.g. #REF!, #DIV/0!, #NULL!_). This check specifically excludes _#N/A_
3.  **ISERROR(value):** checks whether the **value** is an error (_e.g. #REF!, #DIV/0!, #NULL!_). This is probably the most commonly used of these functions in financial modelling
4.  **ISEVEN(number):** checks to see if the **number** is even
5.  **ISFORMULA(reference):** checks to see whether the **reference** is to a cell containing a formula
6.  **ISLOGICAL(value):** checks to see whether the **value** is a logical (TRUE or FALSE) value
7.  **ISNA(value):** checks to see whether the **value** is _#N/A_. This gives us the rather crude identity **ISERR + ISNA = ISERROR**
8.  **ISNONTEXT(value):** checks whether the **value** is not text (_N.B._ blank cells are not text)
9.  **ISNUMBER(value):** checks whether the **value** is a number
10.  **ISODD(number):** checks to see if the **number** is odd. Personally, I find the number 46 very odd, but Excel doesn’t
11.  **ISREF(value):** checks whether the **value** is a reference
12.  **ISTEXT(value):** checks whether the **value** is text.

As stated above, the **ISFORMULA** function checks whether the reference is to a cell that contains a formula. It has the following syntax:

**ISFORMULA(reference)**

The **ISFORMULA** function has the following argument:

*   **reference:** this is required and represents the **reference** for which you wish to determine whether it contains a formula. This can be to one or more cells, a reference or a name that refers to one or more cells.

It should be further noted that:

*   if **reference** refers to more than one cell, as long as one cell contains a formula the result will be TRUE (FALSE otherwise)
*   if **reference** is not a valid data type, such as a defined name that is not a reference, **ISFORMULA** returns the _#VALUE!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isformula-function/#0 "close")

top