# The A to Z of DAX Functions – ACCRINTM

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ACCRINTM

*   February 22, 2022

The A to Z of DAX Functions – ACCRINTM
======================================

Power Pivot Principles: The A to Z of DAX Functions – ACCRINTM
==============================================================

22 February 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **ACCRINTM**._

**_The ACCRINTM function_**

The **ACCRINTM** function returns the accrued interest for a security that pays interest upon maturity. This differs from the [**ACCRINT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-accrint)
 function discussed last time as that pays interest on a periodic basis.

To use **ACCRINTM**, please note the following syntax:

**\=ACCRINTM(issue\_date, maturity\_date, rate, par, \[basis\])**

The arguments are defined as follows:

*   **issue\_date**: this is required and represents the issue date of the security
*   **maturity\_date**: also mandatory, this is the, er, maturity date of the security
*   **rate**: this is required too and is the security’s annual coupon rate (be careful this is entered correctly)
*   **par**: another necessary argument, this is the security’s par value, which is the face value of a share or other security rather than its market value
*   **basis**: this is an optional argument (assumed to be zero \[0\] if omitted). There are five options:

| Basis | Day count basis |
| --- | --- |
| 0 or omitted | US (NASD) 30 / 360 |
| 1   | Actual / actual |
| 2   | Actual / 360 |
| 3   | Actual / 365 |
| 4   | European 30 / 360 |

It should be noted that:

*   dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day zero \[0\], and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899
*   **ACCRINTM** is calculated as follows:

![](<Base64-Image-Removed>)

where:

*   *   **A** = number of accrued days, according to a monthly basis. For interest at maturity items, the number of days from the **issue\_date** to the **maturity\_date** is used
    *   **D** \= annual year **basis**

*   **issue\_date** and **maturity\_date** are truncated to integers
*   **basis** is rounded to the nearest integer

*   an error is returned if:
    *   **issue\_date** and / or **maturity\_date** is / are not (a) valid date(s)
    *   **issue\_date** ≥ **maturity\_date**
    *   **rate** ≤ 0
    *   **par** ≤ 0
    *   **basis** < 0 or **basis** \> 4
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

![](<Base64-Image-Removed>)

returns the accrued interest of 20.55, for a security with the terms specified above.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-accrintm/#0 "close")

top