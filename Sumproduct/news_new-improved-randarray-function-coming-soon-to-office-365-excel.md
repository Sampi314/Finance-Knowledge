# New Improved RANDARRAY Function Coming Soon to Office 365 Excel

**Source:** https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/

---

[Home](https://sumproduct.com/)

\> New Improved RANDARRAY Function Coming Soon to Office 365 Excel

*   February 6, 2019

New Improved RANDARRAY Function Coming Soon to Office 365 Excel
===============================================================

New Improved RANDARRAY Function Coming Soon to Office 365 Excel
===============================================================

6 February 2019

OK, so this is still in what Microsoft refers to as “Preview” mode, _i.e._ it’s not yet “Generally Available” but it is on the outskirts of civilisation. **RANDARRAY** is still a relatively new function found in some editions of the “Office Insider” programme which is an Office 365 fast track. You can register in **File -> Account -> Office Insider** in Excel’s backstage area.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-59.jpg)

Even then, you’re not guaranteed a ticket to the ball as only some will receive the new features as Microsoft slowly roll out these features and functions. Please don’t let that put you off. These features will be with all Office 365 subscribers soon.

We first mentioned **RANDARRAY** back in [September](https://www.sumproduct.com/news/article/getting-arrays-spilling-the-beans-on-seven-new-functions)
. Even though it’s not yet Generally Available, it’s already had a facelift. Oh yes – Microsoft is invested in these functions!

Originally, the **RANDARRAY** function returned an array of random numbers between 0 and 1. It’s not clear from Microsoft, analogous to the pre-existing **RAND** function, which generates a number greater than or equal to zero and strictly less than one. However, there was a general sense of underwhelm with this function and the new and improved version has just been released. It now allows you to set you own maximum and minimum _and_ decide whether you want the values returned to be decimals (_e.g._ 17.4381672…) or integers (whole numbers).

The new syntax for the function is now as follows:

**\=RANDARRAY(\[rows\], \[columns\],\[min\],\[max\],\[integer\])**.

The function has five arguments, all supposedly optional (but upon testing, we weren’t quite as convinced):

*   **rows:** this specifies how many **rows** the results should spill over. If omitted, the default value is 1
*   **columns:** this specifies how many **columns** the results should spill over. If omitted, the default value is also 1
*   **min:** this is the minimum value that may be selected randomly. If this is not specified, it is assumed to be zero (0)
*   **max:** this is the maximum value that may be selected randomly. If this is not specified, it is assumed to be 1
*   **integer:** if this is set to TRUE, only integer outputs are allowed; the default value (FALSE) provides non-integer (decimal) results.

Other points to note:

*   if **rows** or **columns** refers to a blank cell reference, this will generate the new _#CALC!_ error
*   if **rows** or **columns** are entered as decimals, the values used will be truncated to the number before the decimal point (_e.g._ 3.999 will be treated as 3 digits)
*   if **rows** or **columns** is a value less than 1, _#CALC!_ will be returned
*   if **integer** is set to TRUE and either **min** or **max** is not an integer, this will generate an _#VALUE!_ error
*   **max** must be greater than or equal to **min**, else the error _#VALUE!_ is returned.

When we originally discussed the **RANDARRAY** function, we used this rather comprehensive example to create a list of random integers between two values:

![](<Base64-Image-Removed>)

Originally, the formula in cell **F44** was

**\=ROUNDDOWN(RANDARRAY(H36,H37)\*(H39-H38+1),0)+INT(H38)**

and the article explained how this worked. However, it’s much easier now:

![](<Base64-Image-Removed>)

The “new improved” formula in cell **F45** (it’s moved down a row due to the additional argument required in cell **H40**) is simply

**\=RANDARRAY(H36,H37,H38,H39,H40)**.

Cool, eh?

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/#0)
    
*   [Register](https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/#0)

[](https://sumproduct.com/news/new-improved-randarray-function-coming-soon-to-office-365-excel/#0 "close")

top