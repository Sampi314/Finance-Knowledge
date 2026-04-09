# The A to Z of DAX Functions – IPMT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – IPMT

*   August 12, 2025

The A to Z of DAX Functions – IPMT
==================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **IPMT**._

**_The_** _**IPMT**_ **_function_**

![](<Base64-Image-Removed>)

The **IPMT** function is one function that returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate.

****_IPMT(rate, per, nper, pv\[, fv\[, type\]\])_****

There is six \[6\] main argument in this function:

*   **rate**: this is the interest rate per period
*   **per:** this is the period for which you want to find the interest.  This must be between one \[1\] and **nper** (inclusive)
*   **nper:** this is the total number of payment periods in the annuity
*   **pv:** this is the present value, or the lump-sum amount that a series of future payments is worth right now
*   **fv:** (Optional) this is the future value, or a cash balance you want to attain after the last payment is made.  If **fv** is omitted, it is assumed to be **BLANK**
*   **type:** (Optional) this is the type of day count basis to use.  If basis is omitted, it is assumed to be zero \[0\].  The accepted values are listed below this table:

![](<Base64-Image-Removed>)

Here are a few remarks about the **IPMT** function:

*   make sure that you are consistent about the units you use for specifying rate and **nper**.  If you make monthly payments on a four-year loan at 12 percent annual interest, use 0.12/12 for rate and 4\*12 for **nper**.  If you make annual payments on the same loan, use 0.12 for rate and four \[4\] for **nper**
*   for all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers
*   **type** is rounded to the nearest integer
*   an error is returned if:
    *   **per** < 1 or **per** > **nper**
    *   **nper** < 1
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, we can write the following formula in Dax:

![](<Base64-Image-Removed>)

This means we invested $8,000 in a 3-year bond which has 10% annual interest rate, the formula calculates the interest due in the first month.

This will return the monthly interest due in the first month for a loan with the terms specified above.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ipmt/#0 "close")

top