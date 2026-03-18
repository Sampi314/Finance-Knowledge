# A to Z of Excel Functions: The ACCRINT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ACCRINT Function

*   June 14, 2016

A to Z of Excel Functions: The ACCRINT Function
===============================================

A to Z of Excel Functions: The ACCRINT Function
===============================================

15 June 2016

Welcome to our regular blog post on the A to Z of Excel functions. Do you know them all? We bet you don’t! Some of them are useful, some are obscure, some may save your bacon. We try to accrue interest in this new feature by looking at ACCRINT, who we think along with Stanley might be a football team…

### The ACCRINT Function

The ACCRINT function returns the accrued interest for a security that pays interest on a periodic basis. If you are still awake, let me explain further.

It uses the following syntax:

**\=ACCRINT(issue\_date, first\_interest\_date, settlement\_date, rate, par, frequency, \[basis\], \[calculation\_method\])**

Please note: Both basis and calculation method is optional, which is why they appear in square brackets (don’t add the square brackets!).

ACCRINT ( issue\_date, first\_interest\_date, settlement\_date, rate, par, frequency )

The arguments are defined as follows:

*   issue\_date – this is the issue date of the security (duh!)
*   first\_interest\_date – this represents the initial date of interest
*   settlement\_date – this is the date after the issue date when the security is traded to the buyer
*   rate – the security’s annual coupon rate (be careful this is entered correctly)
*   par – the security’s par value, which is the face value of a share or other security rather than its market value
*   frequency – this represents number of coupon payments per year. For annual payments, frequency = 1; for semi-annually, frequency = 2; for quarterly, frequency = 4. In other words, calculate based on 12 (number of months in year) divided by the duration (in months) between payments
*   basis – The type of day count basis to use (check Excel for a full explanation)
*   calculation\_method – this value determines the way to calculate the total accrued interest when the date of settlement is after the first\_interest\_date. A value of TRUE (1) returns the total accrued interest from issue date to settlement\_date. A value of FALSE (0) returns the accrued interest from first\_interest\_date to settlement\_date. As mentioned, this argument is optional; if not specified, the default value is TRUE.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-accrint-function/#0 "close")

top