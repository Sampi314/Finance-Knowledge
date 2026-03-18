# A to Z of Excel Functions: The SHEET function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SHEET function

*   June 9, 2025

A to Z of Excel Functions: The SHEET function
=============================================

**The SHEET function**

![](<Base64-Image-Removed>)

Aw, **SHEET**…  Arriving in Excel 2013, the **SHEET** function in Excel returns the sheet number of the reference sheet.  This is cited as the ordinal position of the referenced sheet, including any hidden, very hidden, macro, chart or dialog sheets (_i.e._ if all sheets were unhidden what its position would be in the tab order).

This sheet number is not the same as the one resulting from its VBA counterpart, where the value is based upon the order of creating, adding or copying that sheet to the workbook.

The **SHEET** function employs the following syntax to operate:

> **SHEET(value)**

The **SHEET** function has the following argument:

*   **value:** this is optional and represents the name of a sheet or a reference for which you want the sheet number.  If **value** is omitted, **SHEET** returns the number of the sheet that contains the function.

It should be noted that:

*   **SHEET** includes all worksheets (visible, hidden or very hidden) in addition to all other sheet types (macro, chart or dialog sheets)
*   if the **value** argument is not a valid value, **SHEET** returns the _#REF!_ error value.  For example, **\=SHEET(Sheet1!#REF)** will return the _#REF!_ error value
*   if the **value** argument is a sheet name that is not valid, **SHEET** returns the _#N/A_ error value.  For example, **\=SHEET(“BadSheetName”)** will return the _#N/A_ error value
*   if the **value** argument contains a defined name which is limited to the worksheet that contains it, **SHEET** will return the _#NAME?_ error
*   **SHEET** is not available in the Object Model (OM) because the Object Model already includes similar functionality.

Please see my examples below: 

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._ 

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sheet-function/#0 "close")

top