# A to Z of Excel Functions: The RATE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The RATE Function

*   July 21, 2024

A to Z of Excel Functions: The RATE Function
============================================

A to Z of Excel Functions: The RATE Function
============================================

22 July 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **RATE** function._

**The RATE function**

![](https://sumproduct.com/wp-content/uploads/2025/05/4f09c3435d5136ad887024782c5074db-1.jpg)

If you have ever been involved calculating financials, you will appreciate interest is a fundamental aspect. Annuities often need to be calculated, _i.e._ regular, periodic payments of identical amounts earning a similar rate of return.

Perhaps the easiest way to think of it is as follows:

*   Let’s assume interest is set at 10% (and we will assume this is after tax)
*   Something that is invested at $100 this year will increase by 10% next year, _i.e._ be valued at $110
*   Something that is invested at $100 this year will increase by 10% over the next two years, _i.e._ be valued at $121
*   Something that is invested at $100 this year will increase by 10% over the next three years, _i.e._ be valued at $133.10. _etc._

![](https://sumproduct.com/wp-content/uploads/2025/05/b222c973c42bd32a56704abd94372ab8-1.jpg)

Note that all of these valuations are for a _point_ of time not a _period_. This is a common mistake in modelling.

The **RATE** function returns the interest rate per period of such an annuity. **RATE** is calculated by iteration and can have zero \[0\] or more solutions. If the successive results of **RATE** do not converge to within 0.0000001 after 20 iterations, **RATE** returns the _#NUM!_ error value.

The **RATE** function has the followingsyntax:

**RATE(nper, pmt, pv, \[fv\], \[type\], \[guess\])**

The **RATE** function has the following arguments:

*   **nper:** this is required and represents the total number of payment periods in an annuity
*   **pmt:** this is also required. This is the payment made each period; it cannot change over the life of the annuity. Typically, **pmt** contains principal and interest but no other fees or taxes. If **pmt** is omitted, you must include the **pv** argument
*   **pv:** this argument is also required. This is the present value, or the lump-sum amount, that a series of future payments is worth right now. If **pv** is unspecified, it is assumed to be zero \[0\]
*   **fv:** this argument is optional and represents the future value, or a cash balance, you want to attain after the last payment is made. If **fv** is omitted, it is assumed to be zero \[0\] (the future value of a loan, for example, is 0). If **fv** is omitted, you must include the **pmt** argument (which is a weird thing to say given it is required!)
*   **type:** this is also optional. The **type** should either be zero \[0\] or one \[1\] and indicates when payments are due. If **type** is omitted, it is assumed to be zero \[0\]

![](<Base64-Image-Removed>)

*   **guess:** another optional argument. Your guess for what the rate will be. If you omit the **guess**, it is assumed to be 10%. If **RATE** does not converge, try different values for **guess**. **RATE** usually converges if **guess** is between zero \[0\] and one \[1\].

Make sure that you are consistent about the units you use for specifying **guess** and **nper**. If you make monthly payments on a four-year loan at 12% annual interest, use 12%/12 for **guess** and 4\*12 for **nper**. If you make annual payments on the same loan, use 12% for **guess** and 4 for **nper**.

For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend receipts, is represented by positive numbers.

Sometimes, the numbers aren’t quite what you expect for this function. That’s because Microsoft uses the following relationship to be consistent across its related financial functions:

![](<Base64-Image-Removed>)

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._ _A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rate-function/#0 "close")

top