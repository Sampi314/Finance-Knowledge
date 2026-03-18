# A to Z of Excel Functions: The EFFECT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The EFFECT Function

*   December 16, 2018

A to Z of Excel Functions: The EFFECT Function
==============================================

A to Z of Excel Functions: The EFFECT Function
==============================================

17 December 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **EFFECT** function._

**The EFFECT function**

Does Excel sometimes not have the desired **EFFECT**? This function returns the effective annual interest rate, given the nominal annual interest rate and the number of compounding periods per year.

The **EFFECT** function employs the following syntax to operate:

**EFFECT(nominal\_rate, npery)**

The **EFFECT** function has the following arguments:

*   **nominal\_rate:** this is required and represents the nominal interest rate
*   **npery:** this is also required. This is the number of compounding periods per year.

It should be further noted that:

*   **npery** is truncated to an integer
*   if either argument is nonnumeric, **EFFECT** returns the _#VALUE!_ error value
*   if **nominal\_rate** ≤ 0 or if **npery** < 1, **EFFECT** returns the _#NUM!_error value.

**EFFECT** is calculated as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e1a396eec0ccaf557bc634b101ad392a.jpg)

**EFFECT** (**nominal\_rate**, **npery**) is related to the function **NOMINAL**(**effect\_rate**, **npery**) through the identity

![](https://sumproduct.com/wp-content/uploads/2025/05/09050a7f3f885f9bd25fe9ce7a8986e1.jpg)

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-539.jpg)

These types of calculations give rise to common errors in financial spreadsheets. One common issue is the inability of many analysts to convert an annual interest rate into a monthly or quarterly rate correctly. Sometimes the error is immaterial; other times, it can cause major issues (e.g. for bank forecasts). This isn’t so much an Excel issue as a mathematical problem, but it is still relevant to financial modellers and more often than not, it’s calculated incorrectly.

The key thing any modeller charged with this exercise must do is read the debt term sheet or deposit account prospectus to see what the **effective annual rate** is. Accountants talk about nominal interest rates and such like, but the effective annual rate is the amount of interest expressed as a percentage of the opening debt or cash balance if interest were to be paid and calculated as per the terms of the underlying document.

It’s easier said than done.

Let me demonstrate with an example: consider a loan of $100 where interest is calculated in arrears on a monthly compounding basis paid quarterly at the end of each quarter. The effective rate is determined to be 12%. The question is, what is the appropriate monthly rate be for cashflow calculations?

Who said 1%? That’s a common answer, derived as 12% divided by the number of months in a year (12). It sounds good, but if I crunch the numbers I will get the following result:

![](<Base64-Image-Removed>)

On a $100 balance with interest of 1% monthly paid quarterly, the total interest for the year will be $12.12 – that’s an effective annual rate of 12.12% rather than 12% (12.00%). This is not correct, as interest is being rolled up at the end of each of the first two months in the quarter and is attracting further interest, _i.e._ interest is compounding and has not been taken into account by simply dividing the annual rate by the number of months in a year.

So, what about using the compounding formula instead? Interest can then be calculated as

**\=(1+12%)1/12 – 1**

This equates to 0.9489% per month. This will take into account compounding – well, sort of:

![](<Base64-Image-Removed>)

This hasn’t worked either: interest has been under-accrued (that’s a good word I’ve just made up) as only $11.49 has been computed for the year – an effective rate of 11.49%.

Here, the calculation is again too simplistic as it does not take into account that the interest is paid quarterly. This means that compounding throughout the year does not occur, hence the shortfall of 0.51%.

The correct formula is:

**\=(1+(Effective Annual Interest Rate x Payment Frequency / Months in Year))1/Payment Frequency – 1**

If payments are made once every three months then there are four payments (equal to **Months in Year / Payment Frequency** or 12 / 3) each year. At these points, compounding stops. Therefore, the interest rate of 12% per annum is effectively 3% per quarter. The compounding formula can then be applied to the quarterly rate to get the monthly rate accordingly:

**\=(1+3%)1/3 – 1**

This equates to 0.9902%. This is correct, _viz_.

![](<Base64-Image-Removed>)

Success!

This is the formula that should be applied to calculate the appropriate monthly interest rate from a quoted effective annual one. The [attached Excel file](https://sumproduct.com/assets/blog-pictures/2018/a-to-z-functions/141/sp-interest-rates-example-model.xlsx)
 provides examples and a template that may be used.

It should be noted that if interest is paid monthly, the formula above reduces to the simple interest rate method (_i.e._ simply divide the rate by 12). Similarly, if interest is only paid at the end of the year, the compounding formula is correct too. Essentially, the formula explained above is the “halfway house” between the two.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-effect-function/#0 "close")

top