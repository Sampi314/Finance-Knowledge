# A to Z of Excel Functions: The NETWORKDAYS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NETWORKDAYS Function

*   November 6, 2022

A to Z of Excel Functions: The NETWORKDAYS Function
===================================================

A to Z of Excel Functions: The NETWORKDAYS Function
===================================================

7 November 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the NETWORKDAYS function._

**The NETWORKDAYS function**

Workdays typically include Monday to Friday, excluding any holidays. However, holidays may differ depending upon the region of the world you live in.

The **NETWORKDAYS** function returns the number of whole working days between a start date and an end date. This excludes weekends by default and may also except a custom list of dates to account for regional holidays. This can be used to calculate employee benefits the accrue based upon the number of days worked during a specific term.

The **NETWORKDAYS**function employs the following syntax to operate:

**NETWORKDAYS(start\_date,  
end\_date, holidays)**

The **NETWORKDAYS** function has the following arguments:

*   **start\_date**: this is required and is a date representing the start of the period
*   **end\_date**: this is also required. This is a date representing the end of the period
*   **holidays**: this is optional. This represents an optional range of one or more dates to be excluded from the working calendar. This list can be either a range of cells containing the dates or an array constant of serial numbers representing the dates.

It should be further noted that:

*   dates should be entered by using the **DATE** function, or as results of other formulas or functions. For example, use **DATE**(2012,5,23) for the 23rd day of May, 2012. Problems can occur if dates are entered as text
*   Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2012 is serial number 40909 because it is 40,908 days after January 1, 1900.
*   if any argument is not a valid date, **NETWORKDAYS** returns the _#VALUE!_ error value.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f3f4e06f9cd19e7f643d53237804f8e9.jpg)

As you can see above, the function may be used to calculate the number of non-weekend days in a period, potentially excluding a custom list of holidays too.

_  
We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-function/#0 "close")

top