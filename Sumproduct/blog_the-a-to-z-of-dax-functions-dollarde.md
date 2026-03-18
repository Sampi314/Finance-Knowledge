# The A to Z of DAX Functions – DOLLARDE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DOLLARDE

*   June 13, 2023

The A to Z of DAX Functions – DOLLARDE
======================================

Power Pivot Principles: The A to Z of DAX Functions – DOLLARDE
==============================================================

13 June 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DOLLARDE**._

**_The DOLLARDE function_**

The **DOLLARDE** function is one of the financial functions, used to convert a dollar price expressed as an integer part and a fraction part into a dollar price expressed as a decimal number. The fractional dollar numbers are sometimes used for security prices.

The **fraction** part of the value is divided by an integer that you specify. For example, if you want your price to be expressed to a precision of 1/16 of a dollar, you divide the **fraction** part by 16. In this case, 1.02 represents $1.125 ($1 + 2/16 = $1.125).

It has the following syntax:

**DOLLARDE(fractional\_dollar,  
fraction)**

The **DOLLARDE** function has the following arguments:

*   **fractional\_dollar**: this is required and represents a number expressed as an integer part and a fraction part, separated by a decimal symbol
*   **fraction**: this is required and represents the integer to use in the denominator of the fraction.

It should be further noted that:

*   the fraction part of the value is divided by an integer that you specify in the **fraction** argument. For example, if you want your price to be expressed to a precision of 1/16 of a dollar, you divide the fraction part of **fractional\_dollar** by 16
*   fraction is rounded to the nearest integer
*   an error will return if 1 > **fraction** ≥ 0
*   an error will return if **fraction** < 0
*   the **DOLLARDE** function is not compatible with Power Pivot and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

For example, if you want to convert the 17 dollars and 1/22 of a dollar (expressed as 17.01), we can write the following DAX code in Power BI:

![](<Base64-Image-Removed>)

This will result in:

![](<Base64-Image-Removed>)

We can run some test to demonstrate what happen if 1 > **fraction** ≥ 0:

![](<Base64-Image-Removed>)

Attempting to display this measure in a visual will result in the following:

![](<Base64-Image-Removed>)

Clicking ‘See details’ here will provide us with more information about this error:

![](<Base64-Image-Removed>)

This is quite similar to the _#DIV/0!_error in Excel, which is a division by zero error.

We may also test what happens when **fraction** < 0:

![](<Base64-Image-Removed>)

This will return a similar visual:

![](<Base64-Image-Removed>)

Again, we can click on ‘See details’ for more information:

![](<Base64-Image-Removed>)

This is similar to the _#NUM!_ error in Excel.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-dollarde/#0 "close")

top