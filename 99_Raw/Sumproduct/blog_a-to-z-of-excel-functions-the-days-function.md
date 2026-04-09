# A to Z of Excel Functions: The DAYS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DAYS Function

*   April 19, 2018

A to Z of Excel Functions: The DAYS Function
============================================

A to Z of Excel Functions: The DAYS Function
============================================

20 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DAYS** function._

**The DAYS function**

This function returns the number of days between two dates.

![](<Base64-Image-Removed>)

The **DAYS** function employs the following syntax to operate:

**DAYS(end\_date, start\_date)**

The **DAYS** function has the following arguments:

*   **end\_date:** this is required and should be a date not prior to **start\_date**
*   **start\_date:** this is also required. The dates **start\_date** and **end\_date** are the two dates between which you want to know the number of days.

It should be further noted that:

*   Excel stores dates as sequential serial numbers so that they can be used in calculations. By default, Jan 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39447 days after January 1, 1900
*   If both date arguments are numbers, **DAYS** uses **end\_date** – **start\_date** to calculate the number of days in between both dates. Be clear, **start\_date** is not counted in the number of days between the two dates
*   If either one of the date arguments is text, that argument is treated as **DATEVALUE(date\_text)** and returns an integer date instead of a time component
*   If date arguments are numeric values that fall outside the range of valid dates, **DAYS** returns the _#NUM!_ error value
*   If date arguments are strings that cannot be parsed as valid dates, **DAYS** returns the _#VALUE!_ error value
*   This function was new to Excel 2013.

Please see my example below:

![](<Base64-Image-Removed>)

Still not sure why you can’t just subtract one date from another…

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-days-function/#0 "close")

top