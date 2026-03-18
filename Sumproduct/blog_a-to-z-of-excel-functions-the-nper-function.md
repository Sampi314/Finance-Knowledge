# A to Z of Excel Functions: The NPER Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NPER Function

*   March 5, 2023

A to Z of Excel Functions: The NPER Function
============================================

A to Z of Excel Functions: The NPER Function
============================================

6 March 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NPER** function._

**The NPER function**

![](<Base64-Image-Removed>)

If you have ever been involved calculating financials, you will appreciate interest is a fundamental aspect. Annuities often need to be calculated, _i.e._ regular, periodic payments of identical amounts earning a similar rate of return.

Perhaps the easiest way to think of it is as follows:

*   Let’s assume interest is set at 10% (and we will assume this is after tax)
*   Something that is invested at $100 this year will increase by 10% next year, _i.e._ be valued at $110
*   Something that is invested at $100 this year will increase by 10% over the next two years, _i.e._ be valued at $121
*   Something that is invested at $100 this year will increase by 10% over the next three years, _i.e._ be valued at $133.10. _etc._

![](<Base64-Image-Removed>)

Note that all of these valuations are for a _point_ of time not a _period_. This is a common mistake in modelling.

The **NPER** function returns the number of periods for an investment based upon periodic, constant payments and a constant interest rate. Its syntax is as follows:

**NPER(rate, pmt, pv,  
\[fv\], \[type\])**

The **NPER** function has the following arguments:

*   **rate**: this is required and represents the interest rate per period. For example, if you obtain a personal loan at a 10% annual interest rate and make monthly payments, your interest rate per month will 10% divided by 12 (number of months) or 0.83%. You would enter 10%/12, or 0.83%, or 0.0083, into the formula as the rate
*   **pmt**: this too is required. This is the payment made each period; it cannot change over the life of the annuity. Typically, **pmt** contains principal and interest but no other fees or taxes. For example, if the monthly payments on a $10,000, four-year car loan at 12% are $263.33 you would enter -263.33 into the formula as the **pmt**
*   **pv**: this argument is also required. This is the present value, or the lump-sum amount, that a series of future payments is worth right now
*   **fv**: this is the first of two optional arguments. This represents the future value or a cash balance you want to attain after the last payment is made. If **fv** is omitted, it is assumed to be zero \[0\] (the future value of a loan, for example, is zero)
*   **type**: this is also optional. The **type** should either be zero \[0\] or one \[1\] and indicates when payments are due. If **type** is omitted, it is assumed to be zero \[0\]:

![](<Base64-Image-Removed>)

For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend receipts, is represented by positive numbers.

Sometimes, the numbers aren’t quite what you expect for this function. That’s because Microsoft uses the following relationship to be consistent across its related financial functions:

![](<Base64-Image-Removed>)

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-nper-function/#0 "close")

top