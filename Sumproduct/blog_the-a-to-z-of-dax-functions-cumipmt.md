# The A to Z of DAX Functions – CUMIPMT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CUMIPMT

*   December 6, 2022

The A to Z of DAX Functions – CUMIPMT
=====================================

Power Pivot Principles: The A to Z of DAX Functions – CUMIPMT
=============================================================

6 December 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_CUMIPMT_**_._

**_The CUMIPMT function_**

The **CUMIPMT** function returns the cumulative interest that would be paid on a loan between a start period and an end period. It has the following syntax:

**CUMIPMT(rate, nper, pv, start\_period, end\_period, type)**

The six \[6\] arguments are as follow:

*   **rate**: this is required and represents the interest rate
*   **nper**: this is also required and represents the total number of payment periods
*   **pv**: this is required and represents the present value of the amount under finance
*   **start\_period**: this is required and represents the first period in the calculation (inclusive). Payment periods are numbered beginning with one \[1\] and are inclusive
*   **end\_period**: this is required and represents the last period in the calculation (inclusive)
*   **type**:this is required and represents the timing of the paymentwhere one \[1\] represents payment at the beginning of the period and zero \[0\] represents payment at the end of the period.

It should be noted that:

*   you need to ensure that you are consistent about the units you use for specifying **rate** and **nper**. If you make monthly payments on a four-year loan at an annual interest rate of 10%, use 10%/12 for **rate** and 4\*12 for **nper**. If you make annual payments on the same loan, use 10% for **rate** and four \[4\] for **nper**
*   the **start\_period**, **end\_period**, and **type** will be rounded to the nearest integer

*   an error will be returned if:
    
    *   **rate** ≤ 0
    
    *   **nper** < 1
    *   **pv** ≤ 0
    *   **start\_period** < 1
    *   **start \_period** > **end\_period**
    *   **end\_period** > **nper**
    *   **type** is any number other than 0 or 1
*   the **CUMIPMT** function is not compatible with Power Pivot and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please consider the following example:

![](https://sumproduct.com/wp-content/uploads/2025/06/60dfa5a3d83b4d644ed085751133f98b.jpg)

If the payments are monthly and we are interested in the interest payments from periods 13 to 24 (inclusively), we will write the following DAX query in Power BI:

**EVALUATE{**

    **CUMIPMT(0.09/12,  
30\*12, 125000, 13, 24, 1)**

**}**

![](<Base64-Image-Removed>)

This will return the cumulative interest payment of -11,052.34: the total interest paid in the second year of payments, periods 13 through 24, assuming that the payments are made at the beginning of each month.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-cumipmt/#0 "close")

top