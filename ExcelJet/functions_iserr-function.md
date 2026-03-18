# Excel ISERR function | Exceljet

**Source:** https://exceljet.net/functions/iserr-function

---

[Skip to main content](https://exceljet.net/functions/iserr-function#main-content)

[](https://exceljet.net/functions/iserr-function#)

*   [Previous](https://exceljet.net/functions/isblank-function)
    
*   [Next](https://exceljet.net/functions/iserror-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

ISERR Function
==============

by Dave Bruns · Updated 7 Sep 2021

Related functions 
------------------

[ISERROR](https://exceljet.net/functions/iserror-function)

[ERROR.TYPE](https://exceljet.net/functions/errortype-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

[ISLOGICAL](https://exceljet.net/functions/islogical-function)

[ISNA](https://exceljet.net/functions/isna-function)

[ISNONTEXT](https://exceljet.net/functions/isnontext-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[ISREF](https://exceljet.net/functions/isref-function)

[ISTEXT](https://exceljet.net/functions/istext-function)

![Excel ISERR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20iserr%20function.png "Excel ISERR function")

Summary
-------

The Excel ISERR function returns TRUE for any error type except the #N/A error. You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

Purpose 
--------

Test for any error but #N/A

Return value 
-------------

A logical value (TRUE or FALSE)

Syntax
------

    =ISERR(value)

*   _value_ - The value to check for any error but #N/A.

Using the ISERR function 
-------------------------

The ISERR function returns TRUE for any error type except the [#N/A](https://exceljet.net/formulas/how-to-fix-the-na-error)
 error. This includes [#VALUE!](https://exceljet.net/formulas/how-to-fix-the-value-error)
, [#REF!](https://exceljet.net/formulas/how-to-fix-the-ref-error)
, [#DIV/0!](https://exceljet.net/formulas/how-to-fix-the-div0-error)
, [#NUM!](https://exceljet.net/formulas/how-to-fix-the-num-error)
, [#NAME?](https://exceljet.net/formulas/how-to-fix-the-name-error)
, [#NULL!](https://exceljet.net/formulas/how-to-fix-the-null-error)
, [#CALC!](https://exceljet.net/formulas/how-to-fix-the-calc-error)
, and [#SPILL!](https://exceljet.net/formulas/how-to-fix-the-spill-error)
 errors. The ISERR function takes one argument, _value_, which is typically a cell reference. 

### Examples

ISERR will return TRUE if A1 contains any error except  #N/A:

    =ISERR(A1) // TRUE if A1 contains an error
    

You can use the ISERR function together with the IF function to test for an error and display a custom message, or perform a different calculation if found.

    =IF(ISERR(A1),"custom message") 
    

### Other error functions

Excel provides a number of error-related functions, each with a different behavior:

*   The [ISERR function](https://exceljet.net/functions/iserr-function)
     returns TRUE for any error type except the #N/A error.
*   The [ISERROR function](https://exceljet.net/functions/iserror-function)
     returns TRUE for any error.
*   The [ISNA function](https://exceljet.net/functions/isna-function)
     returns TRUE for #N/A errors only.
*   The [ERROR.TYPE function](https://exceljet.net/functions/errortype-function)
     returns the numeric code for a given error.
*   The [IFERROR function](https://exceljet.net/functions/iferror-function)
     traps errors and provides an alternative result.
*   The [IFNA function](https://exceljet.net/functions/ifna-function)
     traps #N/A errors and provides an alternative result.

ISERR function examples
-----------------------

[![Excel formula: Count cells that do not contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20errors.png "Excel formula: Count cells that do not contain errors")](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

### [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

In this example, the goal is to count the number of cells in a range that do not contain errors. The best way to solve this problem is to use the SUMPRODUCT function together with the ISERROR function. You can also use the COUNTIF function or COUNTIFS function to exclude specific errors. Both...

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

Related functions
-----------------

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel ERROR.TYPE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20error.type%20function.png "Excel ERROR.TYPE function")](https://exceljet.net/functions/errortype-function)

### [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)

The Excel ERROR.TYPE function returns a number that corresponds to a specific error value. You can use ERROR.TYPE to test for specific kinds of errors. If no error exists, ERROR.TYPE returns #N/A. See below for a key to the error codes returned by ERROR.TYPE. ...

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

[![Excel ISLOGICAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20islogical%20function.png "Excel ISLOGICAL function")](https://exceljet.net/functions/islogical-function)

### [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)

The Excel ISLOGICAL function returns TRUE when a cell contains the logical values TRUE or FALSE, and returns FALSE for cells that contain any other value, including empty cells. 

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel ISNONTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnontext%20function.png "Excel ISNONTEXT function")](https://exceljet.net/functions/isnontext-function)

### [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)

The Excel ISNONTEXT function returns TRUE when a cell contains any value except text. This includes numbers, dates, times, errors, and formulas that do not return text. ISNONTEXT also returns TRUE when a cell is empty.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

[![Excel ISTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20istext%20function.png "Excel ISTEXT function")](https://exceljet.net/functions/istext-function)

### [ISTEXT Function](https://exceljet.net/functions/istext-function)

The Excel ISTEXT function returns TRUE when a cell contains a [text value](https://exceljet.net/glossary/text-value)
, and FALSE if the cell contains any other value. You can use the ISTEXT function to check if a cell contains a text value, or a numeric value entered as text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)
    

### Functions

*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [ERROR.TYPE Function](https://exceljet.net/functions/errortype-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    
*   [ISLOGICAL Function](https://exceljet.net/functions/islogical-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [ISNONTEXT Function](https://exceljet.net/functions/isnontext-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
*   [ISTEXT Function](https://exceljet.net/functions/istext-function)
    

### Links

*   [Microsoft ISERR function documentation](https://support.office.com/en-us/article/is-functions-0f2d7971-6019-40a0-a171-f2d869135665)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)