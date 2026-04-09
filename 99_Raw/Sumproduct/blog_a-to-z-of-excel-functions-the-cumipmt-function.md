# A to Z of Excel Functions: The CUMIPMT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CUMIPMT Function

*   March 25, 2017

A to Z of Excel Functions: The CUMIPMT Function
===============================================

A to Z of Excel Functions: The CUMIPMT Function
===============================================

26 March 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CUMIPMT** function._

**The CUMIPMT function**

This function returns the cumulative interest paid (“cumulative interest payment”) on a loan between a designated **start\_period** and **end\_period** given a constant periodic discount rate.

![](https://sumproduct.com/wp-content/uploads/2025/05/d94fb7d09fa221a08c9a864ae370b97a.jpg)

The example illustrated above may be downloaded [here](https://sumproduct.com/assets/blog-pictures/2018/a-to-z-functions/03-march/sp-cumipmt-example.xlsm)
.

The **CUMIPMT**function employs the following syntax to operate:

**CUMIPMT(rate, nper, pv, start\_period, end\_period, type)**

The **CUMIPMT** function has the following arguments:

*   **rate**: this is required and represents the interest rate
*   **nper:** this is also required and represents the total number of payment periods
*   **pv**: this is required and represents the present value of the amount under finance
*   **start\_period**: this is required and represents the first period in the calculation. Payment periods are numbered beginning with 1
*   **end\_period:** this is required and represents the last period in the calculation
*   **type:** this is required and represents the timing of the payment.

![](https://sumproduct.com/wp-content/uploads/2025/05/f4e4430e6baf8449300b34ef4e7abe02.jpg)

It should be further noted that:

*   you ensure that you are consistent about the units you use for specifying rate and **nper**. If you make monthly payments on a four-year loan at an annual interest rate of 10%, use 10%/12 for rate and 4\*12 for **nper.** If you make annual payments on the same loan, use 10% for rate and 4 for **nper**
*   if **rate** ≤ 0, **nper** ≤ 0, or **pv** ≤ 0, **CUMIPMT** returns the _#NUM!_ error value
*   if **start\_period** < 1, **end\_period** < 1, or **start\_period** > **end\_period**, **CUMIPMT** returns the _#NUM!_ error value
*   if **type** is any number other than 0 or 1, **CUMIPMT** returns the _#NUM!_error value.

Please see my example below:

![](<Base64-Image-Removed>)

Other key points:

*   to get a monthly rate, divide the interest rate by 12 (the number of months in a year) and multiply the years the money is paid out by 12 in order to get the number of payments
*   in Excel Online, to view the result in its proper format, select the cell, and then on the ‘Home’ tab and in the ‘Number’ group, click the arrow next to ‘Number Format’ and select ‘General’.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cumipmt-function/#0 "close")

top