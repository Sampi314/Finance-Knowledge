# A to Z of Excel Functions: The NETWORKDAYS.INTL Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NETWORKDAYS.INTL Function

*   November 13, 2022

A to Z of Excel Functions: The NETWORKDAYS.INTL Function
========================================================

A to Z of Excel Functions: The NETWORKDAYS.INTL Function
========================================================

14 November 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NETWORKDAYS.INTL**function._

**The NETWORKDAYS.INTL function**

Workdays typically include Monday to Friday, excluding any holidays. However, this isn’t the case everywhere in the world.

The **NETWORKDAYS.INTL** function returns the number of whole working days between a start date and an end date, using parameters to indicate which and how many days are considered weekends / not workdays. The specified weekends are excluded as well as a custom list of dates to account for regional holidays. This can be used to calculate employee benefits the accrue based on the number of days worked during a specific term.

The **NETWORKDAYS.INTL**function employs the following syntax to operate:

**NETWORKDAYS.INTL(start\_date,  
end\_date, \[weekend\], \[holidays\])**

The **NETWORKDAYS.INTL** function has the following arguments:

*   **start\_date**: this is required and is a date representing the start of the period
*   **end\_date**: this is also required. This is a date representing the end of the period
*   **weekend**: this is optional. This is an integer that indicates the days of the week that should be considered as weekends. They can be any value between 1 and 17 and indicate the following weekend days:

![](<Base64-Image-Removed>)

*   **holidays**:this is also optional. This is an optional range of one or more dates to be excluded from the working calendar. This list can be either a range of cells containing the dates or an array constant of serial numbers representing the dates.

It should be further noted that:

*   if the **start\_date** is later than the **end\_date**, the return value will be negative, and the magnitude will be the number of whole workdays
*   if the **start\_date** is out of range for the current date base value, **NETWORKDAYS.INTL** returns the _#NUM!_ error value
*   if the **end\_date** is out of range for the current date base value, **NETWORKDAYS.INTL** returns the _#NUM!_ error value
*   if a **weekend** string is of invalid length or contains invalid characters, **NETWORKDAYS.INTL** returns the _#VALUE!_ error value
*   dates should be entered by using the **DATE** function, or as results of other formulas or functions. For example, use **DATE(2012,5,23)** for the 23rd day of May, 2012. Problems can occur if dates are entered as text
*   Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2012 is serial number 40909 because it is 40,908 days after January 1, 1900.

Please see my example below:

![](<Base64-Image-Removed>)

As you can see above, the function can be used to calculate the number of working days in a period with varying weekend consideration, potentially also excluding a custom list of holidays.

_  
We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-networkdays-intl-function/#0 "close")

top