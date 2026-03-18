# A to Z of Excel Functions: The EUROCONVERT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The EUROCONVERT Function

*   January 17, 2019

A to Z of Excel Functions: The EUROCONVERT Function
===================================================

A to Z of Excel Functions: The EUROCONVERT Function
===================================================

18 January 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **EUROCONVERT** function._

**The EUROCONVERT function**

If you use this function, then I suppose **EUROCONVERT**! This function has several features:

*   it converts a number to Euros
*   it converts a number from Euros to a Euro member currency
*   it converts a number from one Euro member currency to another by using the Euro as an intermediary (triangulation).

The currencies available for conversion are those of European Union (EU) members that have adopted the Euro. The function uses fixed conversion rates that are established by the EU.

If this function is not available, and returns the _#NAME?_ error, install and load the Euro Currency Tools Add-in. To install and load the Euro Currency Tools Add-in:

1.  On the **File** tab, click **Options**, and then click **Add-Ins**
2.  In the **Manage** list box, select **Excel Add-ins**, and then click **Go**
3.  In the **Add-Ins Available** list, select the **Euro Currency Tools** box, and then click **OK**
4.  If necessary, follow the instructions in the setup program.

The **EUROCONVERT** function employs the following syntax to operate:

**EUROCONVERT(number, source, target, full\_precision, triangulation\_precision)**

The **EUROCONVERT** function has the following arguments:

*   **number:** this is required and represents the currency value you want to convert or a reference to a cell containing the value
*   **source:** this is also required. This is denoted by a three-letter string or reference to a cell containing the string, corresponding to the International Organization for Standardization (ISO) code for the source currency. The following currency codes are available in the **EUROCONVERT** function:

![](<Base64-Image-Removed>)

*   **target:** again, required. This too is a three-letter string or cell reference, corresponding to the ISO code of the currency to which you want to convert the number. See the previous source table _(above)_ for the ISOcodes.
*   **full\_precision:** this is another required field. This is a logical value (TRUE or FALSE), or an expression that evaluates to a value of **TRUE** or **FALSE**, that specifies how to display the result:

![](<Base64-Image-Removed>)

*   the following table shows the currency specific rounding rules, _i.e._ how many decimal places Excel uses to calculate a currency’s conversion and display the result:

![](<Base64-Image-Removed>)

*   **triangulation\_precision:** this is also required. This represents an integer greater than or equal to three (3) that specifies the number of significant digits to be used for the intermediate Euro value when converting between two Euro member currencies. If you omit this argument, Excel does not round the intermediate Euro value. If you include this argument when converting from a Euro member currency to the Euro, Excel calculates the intermediate Euro value that could then be converted to a euro member currency.

It should be further noted that:

*   Excel truncates any trailing zeros in the return value
*   if the source ISO code is the same as the target ISO code, Excel returns the original value of the number
*   invalid parameters return _#VALUE!_
*   this function does not apply a number format
*   this function cannot be used in array formulae.

Please see my example below:

![](<Base64-Image-Removed>)

Further observations:

*   these examples assume conversion rates of 1 Euro = 6.55957 French francs and 1.95583 deutsche marks. The **EUROCONVERT** function uses the current rates established by the EU. Microsoft will update the function if the rates change. To get full information about the rules and the rates currently in effect, see the European Commission publications about the Euro
*   The examples show the resulting value stored in the cell, not the formatted value
*   In the sample spreadsheet, trailing zeros are truncated.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-euroconvert-function/#0 "close")

top