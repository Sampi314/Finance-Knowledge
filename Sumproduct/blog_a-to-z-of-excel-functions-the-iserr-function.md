# A to Z of Excel Functions: The ISERR Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ISERR Function

*   May 2, 2021

A to Z of Excel Functions: The ISERR Function
=============================================

A to Z of Excel Functions: The ISERR Function
=============================================

3 May 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ISERR** function._

**The ISERR function**

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

As stated above, the **ISERR** function checks whether the value is an error and returns either TRUE or FALSE accordingly. This specifically checks for all types of _prima facie_ errors (_e.g. #VALUE!_, _#REF!_, _#NAME?_ and the relatively new ones, _#CALC!_, _#SPILL!_ and _#FIELD!_) except for _#N/A._ It has the following syntax:

**ISERR(value)**

The **ISERR** function has the following argument:

*   **value:** this is required and represents the **value** for which you wish to determine whether it is an error (excluding _#N/A_).

It should be further noted that:

*   technically, _#N/A_ is not an error: it is a special value that you may manually enter into a cell to indicate that the necessary value is not available yet
*   _#####_ is also not technically an error: this denotes that the column is not wide enough to display all the characters required in the current cell width
*   The #_CALC!_ and _#SPILL!_ errors are only recognised in versions of Excel that support dynamic arrays; otherwise, these are treated as text strings and therefore are not considered errors.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iserr-function/#0 "close")

top