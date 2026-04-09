# A to Z of Excel Functions: The DATEVALUE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DATEVALUE Function

*   April 8, 2018

A to Z of Excel Functions: The DATEVALUE Function
=================================================

A to Z of Excel Functions: The DATEVALUE Function
=================================================

9 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DATEVALUE** function._

**The DATEVALUE function**

This function converts a date that is stored as text to a serial number that Excel recognises as a date. For example, the formula **\=DATEVALUE(“1/1/2020”)** returns 43831, the serial number of the date January 1, 2020. Do note though that your computer’s system date setting may cause the results of a **DATEVALUE** function to vary from this example.

![](https://sumproduct.com/wp-content/uploads/2025/05/2e62251d3d2234c90af8867b07b7d42d.jpg)

The **DATEVALUE** function is helpful in cases where a worksheet contains dates in a text format that you want to filter, sort, or format as dates, or use in date calculations. To view a date serial number as a date, you must apply a date format to the cell.

The **DATEVALUE** function employs the following syntax to operate:

**DATEVALUE(date\_text)**

The **DATEVALUE** function has the following arguments:

*   **date\_text**: this is required and should be the text that represents a date in an Excel date format, or a reference to a cell that contains text that represents a date in an Excel date format. For example, “1/1/2020” or “1-Jan-2020” are text strings within quotation marks that represent dates
*   using the default date system in Microsoft Excel for Windows, the **date\_text** argument must represent a date between January 1, 1900 and December 31, 9999. The **DATEVALUE** function returns the _#VALUE!_ error value if the value of the **date\_text** argument falls outside of this range
*   if the year portion of the **date\_text** argument is omitted, the **DATEVALUE** function uses the current year from your computer’s built-in clock. Time information in the **date\_text** argument is ignored.

It should be further noted that:

*   Excel stores dates as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2020 is serial number 43831 because it is 43,830 days after January 1, 1900
*   most functions automatically convert date values to serial numbers.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datevalue-function/#0 "close")

top