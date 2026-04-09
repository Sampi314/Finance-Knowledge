# A to Z of Excel Functions: The PMT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PMT Function

*   October 22, 2023

A to Z of Excel Functions: The PMT Function
===========================================

A to Z of Excel Functions: The PMT Function
===========================================

23 October 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PMT** function._

This function is often referred to as the _mortgage calculator_. Here, the aim is to calculate what the regular repayment is per period to service and pay off a debt over a given amount of time – just like a common mortgage, but with a fixed (rather than a variable) interest rate.

For example, if I borrow $300,000 over 25 years at an interest rate of 6% p.a. what will my regular monthly payments be (assuming no change of rate)?

The answer to this question is given by the formula:

**P = Ai / (1 – (1 + i)\-N)** 

where:

*   **P** = regular periodic payment
*   **A** = amount borrowed
*   **i** = periodic interest rate
*   **N** \= total number of repayment periods

(Interesting that the acronym for remembering the mortgage variables is **PAiN**!)

In our example, crunching the numbers (using a periodic interest rate of 0.50%, being 6% / 12 (since the interest does not compound as it is paid monthly) and total number of periods being 25 x 12 = 300) gives a monthly repayment of $1,932.90, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f75e733e5377481c4579a66b4e22dd30.jpg)

It should be noted that using **PMT** will give the same solution, but be negative instead. This is because Excel’s financial functions distinguish between cash inflows (positive) and outflows (negative).

![](https://sumproduct.com/wp-content/uploads/2025/05/265c69e76933035523e0b8d8226cf67b.jpg)

**PMT** calculates the payment for a loan based on constant payments and a constant interest rate. It employs the following syntax to operate:

**PMT(rate, nper, pv, \[fv\], \[type\])**

The **PMT**function has the following arguments:

*   **rate:** this is required and represents the constant interest rate for the loan
*   **nper:** this is also required and denotes the total number of payments for the loan
*   **pv:** also necessary, this is the present value, or the total amount that a series of future payments is worth now, also known as the principal (_i.e._ what you are borrowing)
*   **fv:** this is the first of two optional arguments. This is the future value, or a cash balance you want to attain, after the last payment is made. If **fv** is omitted, it is assumed to be zero (0), _i.e._ the future value of a loan is nil
*   **type:**this final argument is also optional. This the number zero (0) or one (1) and indicates when payments are due:

![](https://sumproduct.com/wp-content/uploads/2025/05/8438ae0ef61305f10589054063d7cd0c.jpg)

It should be further noted that:

*   the payment returned by **PMT** includes principal and interest but considers no taxes, reserve payments or other fees sometimes associated with loans
*   make sure that you are consistent about the units you use for specifying **rate** and **nper**. If you make monthly payments on a four-year loan at an annual interest rate of 12%, use 12%/12 for **rate** and 4\*12 for **nper**. If you make annual payments on the same loan, use 12% for the **rate** and 4 for **nper**
*   to find the total amount paid over the duration of the loan, multiply the returned **PMT** value by **nper**.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pmt-function/#0 "close")

top