# A to Z of Excel Functions: The PPMT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PPMT Function

*   December 24, 2023

A to Z of Excel Functions: The PPMT Function
============================================

A to Z of Excel Functions: The PPMT Function
============================================

25 December 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PPMT** function._

**The PPMT function**

Imagine I were to borrow $300,000 over 25 years at an interest rate of 6% p.a. Assuming no final amount to pay (_i.e._ no bullet repayment) and payments were made monthly at the end of each month (“in arrears”), interest would accrue over the month at 6%/12 = 0.50% per month (since there would be no compounding of interest monthly as it would be paid each month and I will simplify that all months are of equal length).

Using Goal Seek, the **PMT** function or algebraic methods, I could soon determine the monthly payment would be $1,932.90:

![](https://sumproduct.com/wp-content/uploads/2025/05/19b6006156e389e3e26a3d67e923d9ad.jpg)

You can see that over the 300 months the outstanding balance reduces to zero from an initial loan of $300,000. The monthly payments (column **H**) remain constant, but the interest reduces as it calculates the opening balance (for payments in arrears, _i.e._ the repayment is not included) multiplied by the monthly interest rate, _e.g._ for cell **I29**, interest is calculated as

**\=G29\*$I$13**

The principal (calculated in column **L**) is then simply the monthly payment less the interest payment, _e.g._ for cell **L29**, this formula is

**\=-H29-I29**

As long as you calculate this table, the formulae are simple. But what if you don’t want to have to generate this time every time you wanted to know the principal element of the monthly payment for a given month? You may use the **PPMT** function, which will give the same solution, but be negative instead. This is because Excel’s financial functions distinguish between cash inflows (positive) and outflows (negative).

It employs the following syntax to operate:

**PPMT(rate,  
per, nper, pv, \[fv\], \[type\])**

The **PPMT** function has the following arguments:

*   **rate:** this is required and represents the constant interest rate for the loan
*   **per:** this is required, and specified the period to be considered, between periods 1 and **nper**
*   **nper:** this is also required and denotes the total number of payments for the loan
*   **pv:** also necessary, this is the present value, or the total amount that a series of future payments is worth now, also known as the principal (_i.e._ what you are borrowing)
*   **fv:** this is the first of two optional arguments. This is the future value, or a cash balance you want to attain, after the last payment is made. If **fv** is omitted, it is assumed to be zero (0), _i.e._ the future value of a loan is nil
*   **type:**this final argument is also optional. This the number zero (0) or one (1) and indicates when payments are due:

![](<Base64-Image-Removed>)

It should be further noted that:

*   the payment returned by **PPMT** relates to the principal but considers no taxes, reserve payments or other fees sometimes associated with loans
*   make sure that you are consistent about the units you use for specifying **rate** and **nper**. If you make monthly payments on a four-year loan at an annual interest rate of 12%, use 12%/12 for **rate** and 4\*12 for **nper**. If you make annual payments on the same loan, use 12% for the **rate** and 4 for **nper**.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ppmt-function/#0 "close")

top