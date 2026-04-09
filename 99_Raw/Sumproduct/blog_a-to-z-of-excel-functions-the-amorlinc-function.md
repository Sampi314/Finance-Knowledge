# A to Z of Excel Functions: The AMORLINC Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The AMORLINC Function

*   July 26, 2016

A to Z of Excel Functions: The AMORLINC Function
================================================

A to Z of Excel Functions: The AMORLINC Function
================================================

27 July 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **AMORLINC** function._

**The AMORLINC function**

The **AMORLINC** function in Microsoft Excel is similar to the last function we discussed, **AMORDEGRC**. The difference is that this function returns the depreciation for each accounting period, as provided for the French accounting system. If an asset is purchased in the middle of the accounting period, the pro-rated depreciation is taken into account instead.

**AMORLINC** uses the following syntax:

**AMORLINC(cost, date\_purchased, first\_period, salvage, period, rate, \[basis\])**

**Important:** Dates should be entered by using the **DATE** function, or as results of other formulas or functions. For example, use **DATE(2016,5, 23)** for the 23rd day of May, 2016. Problems can occur if dates are entered as text.

The **AMORLINC** function syntax has the following arguments:

*   **cost:** this is required. This represents the cost of the asset
*   **date\_purchased:** also required. The date of the purchase of the asset
*   **first\_period:** required. The date of the end of the first period
*   **salvage:** required. The salvage value at the end of the life of the asset
*   **period:** required. The period in question
*   **rate:** required. The rate of depreciation
*   **basis:** optional. The year basis to be used.

Some notes to remember on how the **basis** argument works (there’s no number **2**):

![](<Base64-Image-Removed>)

Also note:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post at least every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-amorlinc-function/#0 "close")

top