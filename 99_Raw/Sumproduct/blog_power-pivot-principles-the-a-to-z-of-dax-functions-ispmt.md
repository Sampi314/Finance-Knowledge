# The A to Z of DAX Functions – ISPMT

**Source:** https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISPMT

*   January 13, 2026

The A to Z of DAX Functions – ISPMT
===================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISPMT**._

**_The_** _**ISPMT**_ **_function_**

![](<Base64-Image-Removed>)

This function calculates the interest paid (or received) for the specified period of a loan (or an investment) for a constant instant rate with equal principal repayments.  In reality, this is quite an easy financial instrument to calculate using basic formulae, but the **ISPMT** function makes it slightly simpler than computing from first principles.

The **ISPMT** function is one function that calculates the interest paid (or received) for the specified period of a loan (or investment) with even principal payments:

**`ISPMT (rate, per, nper, pv)`**

There are four \[4\] main arguments in this function:

*   **rate**: the interest rate for the investment
*   **per:** the period for which you want to find the interest.  This must be between zero \[0\] and **nper**\-1 (inclusive)
*   **nper:** the total number of payment periods for the investment
*   **pv:** the present value of the investment.  For a loan, **pv** is the loan amount.

Here are a few remarks about the **ISPMT** function:

*   make sure that you are consistent about the units you use for specifying rate and **nper**.  If you make monthly payments on a four-year loan at an annual interest rate of 12%, use 0.12/12 for rate and 4\*12 for **nper**.  If you make annual payments on the same loan, use 0.12 for **rate** and four \[4\] for **nper**
*   for all the arguments, the cash you pay out, such as deposits to savings or other withdrawals, is represented by negative numbers; the cash you receive, such as dividend checks and other deposits, is represented by positive numbers
*   **ISPMT** counts each period beginning with zero \[0\], not one \[1\]
*   most loans use a repayment schedule with even periodic payments.  The **IPMT** function returns the interest payment for a given period for this type of loan
*   some loans use a repayment schedule with even principal payments.  The **ISPMT** function returns the interest payment for a given period for this type of loan
*   an error is returned if:
*   **nper** = 0 \[zero\]
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, we can write the following formula in **DAX**:

**`DEFINE   VAR NumPaymentPeriods = 4   VAR PaymentPeriods = GENERATESERIES(0, NumPaymentPeriods-1)   EVALUATE   ADDCOLUMNS (    PaymentPeriods,    "Interest Payment",    ISPMT(0.1, [Value], NumPaymentPeriods, 4000)   )`**

![](<Base64-Image-Removed>)

This means we borrowed $4,000 over four \[4\] periods at a 10% interest rate.  It generates each payment period (zero \[0\] to three \[3\]) and uses the **ISPMT** function to calculate how much of the repayment is interest in each specific period.

This returns the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/#0)

[](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-ispmt/#0 "close")

top